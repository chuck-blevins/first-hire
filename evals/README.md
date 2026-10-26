# Evals

Measures whether an assistant answering from this knowledge base gives founders correct, grounded, current, well-fitted, and safe answers. The method is model-agnostic: the same questions and rubric work for any model, so models can be compared before switching.

| File | What it is |
|------|------------|
| `questions.jsonl` | Golden founder questions with answer keys. The format is in `SCHEMA.md` |
| `rubric.md` | The 5-dimension, 10-point rubric and pass bar, for scripts, LLM judges, and humans |
| `run_eval.py` | Runner: generate answers, score them, compare runs. Python standard library only |
| `runs/<run-name>/` | One folder per run: `answers/<id>.md`, `scores.json`, `report.md` |

## Running an eval

1. **Get answers.** Pick one of these:
   - **Any CLI or API wrapper** that reads the question on stdin and prints the answer:
     `python3 -I evals/run_eval.py generate --run 2026-10-26-baseline --answer-cmd "<your command>"`
   - **An agent answering by hand** (e.g. in Buzz): answer each question cold, the way you would for a founder. Save each answer as `evals/runs/<run-name>/answers/<id>.md`.
2. **Score them.**
   `python3 -I evals/run_eval.py score --run 2026-10-26-baseline --judge-cmd "<judge command>"`
   - **Without `--judge-cmd`:** you get the automated checks only. These cover fact recall against `must_include`, trap hits from `must_not_say`, portal mentions, and heuristic checks for citations, dates, referrals, scope, and credential requests.
   - **With `--judge-cmd`:** the judge gets the rubric, the answer key, and the answer on stdin, and must print JSON scores. **Use a different model from the one that answered.**
3. **Read `runs/<run-name>/report.md`.** The pass bar is 90% of questions at 8/10 or higher, with no trap hits and no Safety score of 0.
4. **Compare runs** before changing packages or models:
   `python3 -I evals/run_eval.py compare <run-a> <run-b>`

## When to run
- **Package changes:** on any PR that changes a package figure. Also update the affected question patterns: grep `questions.jsonl` for the package's `row`.
- **Model changes:** before switching the answering model. Run the same set on the current model and the candidate, then compare.
- **January refresh:** after the yearly rate and form updates.
- **Expert review:** every quarter, a GA employment attorney or CPA grades 5–10 answers. That calibrates the judge.

## Growing the set
- **Corrections:** every mistake a founder or expert catches becomes a new question. Use the next unused id, and never reuse ids.
- **Unanswerable questions:** questions the assistant can't answer go to `REFERENCE/INFO/first-hire/PACKAGES/QUESTION_BANK.md` first.

The automated checks are a smoke test, not a grade. Regex can't tell a correct number in a wrong sentence from a correct one. Use them to catch regressions, and use the judge and human review for real scores.
