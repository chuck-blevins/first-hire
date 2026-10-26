# first-hire

A cited knowledge base for startup founders in Georgia (US) who are making their first hires. It covers employee vs. contractor, equity, payroll taxes, paying founders, pay rules, benefits and PEOs, remote hires, firing, compliance deadlines, Delaware entities operating in Georgia, and metro Atlanta business licenses.

> General information, not legal or tax advice. Figures change, so every package lists what to re-verify and where.

## Layout

| Path | What it is |
|------|------------|
| `REFERENCE/INFO/first-hire/PACKAGES/` | Answer packages: one Markdown file per topic, with YAML frontmatter. Start with `README.md` there |
| `REFERENCE/INFO/first-hire/PACKAGES/ANSWERING_GUIDE.md` | Rules for any assistant or retrieval pipeline answering from the packages |
| `REFERENCE/INFO/first-hire/SOURCES.md` | Official links and saved source documents, with access notes and staleness warnings |
| `REFERENCE/INFO/first-hire/*.pdf` | Saved source documents (IRS, GA DOR, GA DOL, USCIS, GA OCI) |
| `REFERENCE/INFO/first-hire/text/` | Plain-text copies of each PDF, with page markers, for indexing |
| `REFERENCE/INFO/first-hire/manifest.json` | Machine-readable index of packages and sources |
| `REFERENCE/INFO/first-hire/build_manifest.py` | Rebuilds `manifest.json` and lints the packages (Python standard library only) |
| `REFERENCE/FORMS/` | Forms and templates |

## Using it with an LLM or RAG pipeline

1. **Index:** index `PACKAGES/*.md` (skip `_TEMPLATE.md`), `SOURCES.md`, and `text/*.txt`.
2. **Chunk:** split on `##` headings and keep the frontmatter as chunk metadata.
3. **Answer:** follow `ANSWERING_GUIDE.md`. Re-check each "Double-check before sending" row against its live source before quoting a figure.

All paths are relative to the repo root.

## Updating

- **Edit packages in place:** after editing, run `python3 -I REFERENCE/INFO/first-hire/build_manifest.py` and commit the regenerated `manifest.json`. The script exits non-zero if a package is missing frontmatter or has broken cross-references.
- **New packages:** copy `PACKAGES/_TEMPLATE.md`, then add a row to `PACKAGES/README.md`.
