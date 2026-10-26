#!/usr/bin/env python3
"""Build manifest.json for the first-hire knowledge base and lint package frontmatter.

Usage: python3 -I build_manifest.py            (run from any directory)
Writes manifest.json next to this script. Exits 1 if any package fails lint.
Standard library only, so any environment or pipeline can run it.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PKG_DIR = ROOT / "PACKAGES"
TEXT_DIR = ROOT / "text"
WORKSPACE = ROOT.parents[2]  # .../.buzz
REQUIRED = ["id", "title", "questions", "tags", "jurisdiction", "audience", "related", "last_verified", "status"]
SKIP = {"README.md", "_TEMPLATE.md", "QUESTION_BANK.md", "ANSWERING_GUIDE.md"}


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, val = line.split(":", 1)
        val = val.strip()
        if val.startswith("["):
            try:
                val = json.loads(val)
            except json.JSONDecodeError:
                val = [v.strip().strip("\"'") for v in val.strip("[]").split(",") if v.strip()]
        else:
            val = val.strip("\"'")
        meta[key.strip()] = val
    return meta


def sections(text):
    return [h.strip() for h in re.findall(r"^## (.+)$", text, re.M)]


def rel(p):
    return str(p.relative_to(WORKSPACE))


def main():
    packages, problems = [], []
    ids = set()
    for f in sorted(PKG_DIR.glob("*.md")):
        if f.name in SKIP:
            continue
        text = f.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        missing = [k for k in REQUIRED if k not in meta or meta[k] in ("", [])]
        if missing:
            problems.append(f"{f.name}: missing frontmatter {missing}")
        if "By stage" not in sections(text):
            problems.append(f"{f.name}: no '## By stage' section")
        if re.search(r"\b(see above|see below)\b", text, re.I):
            problems.append(f"{f.name}: contains 'see above/below' (sections must stand alone)")
        ids.add(meta.get("id"))
        packages.append({
            "id": meta.get("id"),
            "path": rel(f),
            "title": meta.get("title"),
            "questions": meta.get("questions", []),
            "tags": meta.get("tags", []),
            "jurisdiction": meta.get("jurisdiction", []),
            "audience": meta.get("audience", []),
            "related": meta.get("related", []),
            "last_verified": meta.get("last_verified"),
            "status": meta.get("status"),
            "sections": sections(text),
            "words": len(text.split()),
        })
    for p in packages:
        for r in p["related"] or []:
            if r not in ids:
                problems.append(f"{p['path']}: related id '{r}' has no package")
    sources = [{"pdf": rel(pdf), "text": rel(TEXT_DIR / (pdf.stem + ".txt")) if (TEXT_DIR / (pdf.stem + ".txt")).exists() else None}
               for pdf in sorted(ROOT.glob("*.pdf"))]
    manifest = {
        "name": "first-hire knowledge base",
        "description": "Cached, cited guidance for startup founders in Georgia (US) on hiring, payroll, taxes, compliance, and entity questions. General information, not legal or tax advice.",
        "generated": max((p["last_verified"] for p in packages if p["last_verified"]), default=None),
        "conventions": rel(PKG_DIR / "README.md"),
        "source_index": rel(ROOT / "SOURCES.md"),
        "question_bank": rel(PKG_DIR / "QUESTION_BANK.md"),
        "answering_guide": rel(PKG_DIR / "ANSWERING_GUIDE.md"),
        "packages": packages,
        "source_documents": sources,
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"manifest.json: {len(packages)} packages, {len(sources)} source documents")
    for p in problems:
        print("LINT:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
