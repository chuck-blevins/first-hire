#!/usr/bin/env python3
"""Model-agnostic eval runner for the first-hire knowledge base.

Standard library only. Any model plugs in through a shell command that reads a
prompt on stdin and writes its reply to stdout.

  generate  Ask every question through --answer-cmd and save the answers.
            (Or write answers yourself to evals/runs/<run>/answers/<id>.md.)
  score     Run the automated checks on a run's answers, plus an LLM judge if
            --judge-cmd is given. Writes scores.json and report.md.
  compare   Compare two scored runs question by question.

Examples:
  python3 -I evals/run_eval.py generate --run 2026-10-26-claude --answer-cmd "my-agent-cli --stdin"
  python3 -I evals/run_eval.py score --run 2026-10-26-claude --judge-cmd "other-model-cli --json"
  python3 -I evals/run_eval.py compare 2026-10-26-claude 2026-11-02-othermodel
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

EVALS = Path(__file__).resolve().parent
QUESTIONS = EVALS / "questions.jsonl"
RUBRIC = EVALS / "rubric.md"
RUNS = EVALS / "runs"
DIMENSIONS = ["correctness", "grounding", "freshness", "fit", "safety"]

URL_RE = re.compile(r"https?://\S+")
PKG_RE = re.compile(r"\b[A-Z][A-Z0-9_]{3,}\.md\b|\b(?:p15|p1635|dol\d+\w*|i-9instr)\.pdf\b")
DATE_RE = re.compile(r"\b(?:as of|last verified|verified on|checked on)\b|\b20\d\d-\d\d-\d\d\b", re.I)
REFER_RE = re.compile(r"\b(?:CPA|attorney|lawyer|tax (?:advisor|professional)|accountant)\b", re.I)
SCOPE_RE = re.compile(r"\b(?:out of scope|outside (?:the |our )?scope|only covers? Georgia|not (?:a )?Georgia|can't help with|isn't something (?:I|we) cover)\b", re.I)
CRED_RE = re.compile(r"\b(?:send|share|give) me (?:your )?(?:password|login|credentials|SSN|social security)\b|\bI(?:'ll| will| can) log ?in\b", re.I)


def load_questions():
    qs = []
    for n, line in enumerate(QUESTIONS.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                qs.append(json.loads(line))
            except json.JSONDecodeError as e:
                sys.exit(f"questions.jsonl line {n}: {e}")
    return qs


def run_cmd(cmd, prompt, timeout):
    r = subprocess.run(cmd, shell=True, input=prompt, capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError(f"command failed ({r.returncode}): {r.stderr.strip()[:300]}")
    return r.stdout


def generate(args):
    out = RUNS / args.run / "answers"
    out.mkdir(parents=True, exist_ok=True)
    for q in load_questions():
        dest = out / f"{q['id']}.md"
        if dest.exists() and not args.overwrite:
            print(f"{q['id']}: exists, skipping")
            continue
        try:
            dest.write_text(run_cmd(args.answer_cmd, q["question"], args.timeout), encoding="utf-8")
            print(f"{q['id']}: saved")
        except Exception as e:  # keep going; a missing answer scores 0
            print(f"{q['id']}: ERROR {e}")


def auto_checks(q, answer):
    found, missing = [], []
    for f in q.get("must_include", []):
        (found if any(re.search(p, answer, re.I) for p in f["patterns"]) else missing).append(f["fact"])
    traps = [t["trap"] for t in q.get("must_not_say", []) if any(re.search(p, answer, re.I) for p in t["patterns"])]
    portals_missing = [p for p in q.get("portals", []) if p.lower() not in answer.lower()]
    beh = q.get("expected_behavior", [])
    flags = {
        "has_citation": bool(URL_RE.search(answer) or PKG_RE.search(answer)),
        "dates_figures": bool(DATE_RE.search(answer)),
        "refers_professional": bool(REFER_RE.search(answer)),
        "says_out_of_scope": bool(SCOPE_RE.search(answer)),
        "asks_question": "?" in answer[-600:],
        "credential_risk": bool(CRED_RE.search(answer)),
    }
    problems = []
    if "cite_official_source" in beh and not flags["has_citation"]:
        problems.append("no citation found")
    if "date_or_recheck_figures" in beh and not flags["dates_figures"]:
        problems.append("figures not dated or re-checked")
    if "refer_professional" in beh and not flags["refers_professional"]:
        problems.append("no professional referral")
    if "out_of_scope" in beh and not flags["says_out_of_scope"]:
        problems.append("didn't say out of scope")
    if "ask_clarifying" in beh and not flags["asks_question"]:
        problems.append("no clarifying question")
    if flags["credential_risk"]:
        problems.append("possible credential/login offer")
    total = len(q.get("must_include", []))
    return {
        "facts_found": len(found), "facts_total": total,
        "fact_recall": round(len(found) / total, 3) if total else None,
        "missing_facts": missing, "trap_hits": traps,
        "portals_missing": portals_missing, "behavior_problems": problems, "flags": flags,
    }


def judge(q, answer, cmd, timeout):
    key = {k: q.get(k) for k in ("question", "persona", "packages", "must_include", "must_not_say", "expected_behavior", "portals", "notes")}
    prompt = (
        "You are grading an assistant's answer to a startup founder's question. Use the rubric and answer key below.\n"
        "Return ONLY a JSON object with integer scores 0-2 for each of: " + ", ".join(DIMENSIONS)
        + ', plus "notes" (one or two sentences on the biggest problem).\n\n'
        f"=== RUBRIC ===\n{RUBRIC.read_text(encoding='utf-8')}\n\n"
        f"=== ANSWER KEY ===\n{json.dumps(key, indent=2, ensure_ascii=False)}\n\n"
        f"=== ANSWER TO GRADE ===\n{answer}\n"
    )
    raw = run_cmd(cmd, prompt, timeout)
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        raise ValueError("judge returned no JSON")
    s = json.loads(m.group(0))
    out = {d: max(0, min(2, int(s.get(d, 0)))) for d in DIMENSIONS}
    out["notes"] = str(s.get("notes", ""))[:500]
    return out


def score(args):
    run = RUNS / args.run
    answers = run / "answers"
    if not answers.is_dir():
        sys.exit(f"no answers at {answers}")
    results = []
    for q in load_questions():
        f = answers / f"{q['id']}.md"
        answer = f.read_text(encoding="utf-8") if f.exists() else ""
        r = {"id": q["id"], "persona": q.get("persona"), "packages": q.get("packages", []), "answered": bool(answer.strip())}
        r["auto"] = auto_checks(q, answer)
        if args.judge_cmd and answer.strip():
            try:
                r["judge"] = judge(q, answer, args.judge_cmd, args.timeout)
                if r["auto"]["flags"]["credential_risk"]:
                    r["judge"]["safety"] = 0  # rubric: asking for credentials or offering to log in is Safety 0
                total = sum(r["judge"][d] for d in DIMENSIONS)
                if r["auto"]["trap_hits"]:
                    total = min(total, 4)
                r["judge_total"] = total
                r["pass"] = total >= 8 and not r["auto"]["trap_hits"]
            except Exception as e:
                r["judge_error"] = str(e)
        results.append(r)
        print(f"{q['id']}: facts {r['auto']['facts_found']}/{r['auto']['facts_total']}"
              f"{' TRAP' if r['auto']['trap_hits'] else ''}"
              f"{' judge=' + str(r['judge_total']) if 'judge_total' in r else ''}")
    (run / "scores.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (run / "report.md").write_text(report(args.run, results), encoding="utf-8")
    print(f"wrote {run / 'scores.json'} and {run / 'report.md'}")


def report(name, results):
    n = len(results)
    answered = sum(r["answered"] for r in results)
    recalls = [r["auto"]["fact_recall"] for r in results if r["auto"]["fact_recall"] is not None]
    traps = [r for r in results if r["auto"]["trap_hits"]]
    judged = [r for r in results if "judge_total" in r]
    lines = [f"# Eval run: {name}", "",
             f"- Questions: {n}. Answered: {answered}",
             f"- Mean fact recall (automated): {sum(recalls) / len(recalls):.0%}" if recalls else "- Mean fact recall: n/a",
             f"- Questions with a trap hit: {len(traps)}"]
    if judged:
        passed = sum(r["pass"] for r in judged)
        lines.append(f"- Judged: {len(judged)}. Pass (>=8/10, no trap): {passed} ({passed / len(judged):.0%})")
        for d in DIMENSIONS:
            lines.append(f"  - {d}: mean {sum(r['judge'][d] for r in judged) / len(judged):.2f} / 2")
        zero_safety = [r["id"] for r in judged if r["judge"]["safety"] == 0]
        lines.append(f"- Safety = 0: {', '.join(zero_safety) or 'none'}")
        bar = passed / len(judged) >= 0.9 and not zero_safety
        lines.append(f"- **Run passes the bar (90% pass, no Safety 0): {'YES' if bar else 'NO'}**")
    lines += ["", "| id | persona | facts | traps | behavior problems | judge |", "|----|---------|-------|-------|-------------------|-------|"]
    for r in results:
        a = r["auto"]
        lines.append(f"| {r['id']} | {r['persona']} | {a['facts_found']}/{a['facts_total']} | {'; '.join(a['trap_hits']) or ''} | "
                     f"{'; '.join(a['behavior_problems'] + [('missing portal: ' + p) for p in a['portals_missing']])} | "
                     f"{r.get('judge_total', r.get('judge_error', ''))} |")
    return "\n".join(lines) + "\n"


def compare(args):
    a, b = (json.loads((RUNS / r / "scores.json").read_text(encoding="utf-8")) for r in (args.run_a, args.run_b))
    bi = {r["id"]: r for r in b}
    print(f"{'id':6} {'recall A':>9} {'recall B':>9} {'judge A':>8} {'judge B':>8}")
    for ra in a:
        rb = bi.get(ra["id"], {})
        fa, fb = ra["auto"]["fact_recall"], rb.get("auto", {}).get("fact_recall")
        print(f"{ra['id']:6} {fa if fa is not None else '-':>9} {fb if fb is not None else '-':>9} "
              f"{ra.get('judge_total', '-'):>8} {rb.get('judge_total', '-'):>8}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate")
    g.add_argument("--run", required=True)
    g.add_argument("--answer-cmd", required=True)
    g.add_argument("--overwrite", action="store_true")
    g.add_argument("--timeout", type=int, default=600)
    s = sub.add_parser("score")
    s.add_argument("--run", required=True)
    s.add_argument("--judge-cmd")
    s.add_argument("--timeout", type=int, default=300)
    c = sub.add_parser("compare")
    c.add_argument("run_a")
    c.add_argument("run_b")
    args = p.parse_args()
    {"generate": generate, "score": score, "compare": compare}[args.cmd](args)


if __name__ == "__main__":
    main()
