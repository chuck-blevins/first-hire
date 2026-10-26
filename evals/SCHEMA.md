# questions.jsonl schema

One JSON object per line.

```json
{
  "id": "q01",
  "persona": "pre-revenue",
  "question": "The founder's question, written the way a founder would ask it.",
  "packages": ["ga-employer-taxes", "first-hire-checklist"],
  "must_include": [
    {"fact": "GA income tax withholding is a flat 4.99% (since May 11, 2026)", "patterns": ["4\\.99\\s*%"], "row": "GA_EMPLOYER_TAXES: GA withholding rate"}
  ],
  "must_not_say": [
    {"trap": "Quotes the outdated $455/week FLSA salary threshold from dol224.pdf", "patterns": ["\\$\\s*455"]}
  ],
  "expected_behavior": ["cite_official_source", "date_or_recheck_figures", "refer_professional", "route_portal"],
  "portals": ["Georgia Tax Center"],
  "notes": "Why this question is in the set, and what a great answer does."
}
```

| Field | Meaning |
|-------|---------|
| `id` | Stable id (`q01`…). Never reuse an id after deleting a question |
| `persona` | `pre-revenue` or `funded-2-10` |
| `packages` | Package ids a good answer should draw on (see `REFERENCE/INFO/first-hire/manifest.json`) |
| `must_include[].patterns` | Case-insensitive Python regexes. The fact counts as present if **any** pattern matches. Keep them tolerant of formatting (`\s*`, optional commas) |
| `must_include[].row` | Which package and double-check row the fact comes from, so a figure change can be traced to the questions it affects |
| `must_not_say[].patterns` | Any match is a hard failure for that question |
| `expected_behavior` | Any of: `cite_official_source`, `date_or_recheck_figures`, `refer_professional`, `route_portal`, `out_of_scope`, `ask_clarifying`. The LLM judge and human reviewers score these; the script does only light heuristic checks |
| `portals` | Portal or form names the answer should send the founder to (checked as substrings) |

When a figure changes in a package, grep `questions.jsonl` for its `row` and update the matching patterns in the same PR.
