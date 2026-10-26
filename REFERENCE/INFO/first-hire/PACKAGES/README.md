# First-hire packages

Cached answers for founder questions, written for two personas: pre-revenue founders and funded teams hiring 2–10. Each package has a short answer, steps, links, and a "Double-check before sending" table.

| Founder asks about… | Package |
|---------------------|---------|
| "What do I need to do to hire my first employee?" (the hub; start here) | `FIRST_HIRE_CHECKLIST.md` |
| Full-time hire vs. contractor, 1099 vs. W-2, IP ownership for dev work | `EMPLOYEE_VS_CONTRACTOR.md` |
| Equity for hires: options, vesting, 83(b), 409A, LLC profits interests | `EQUITY_FOR_EARLY_HIRES.md` |
| What taxes to withhold, pay, and file in GA (federal and state) | `GA_EMPLOYER_TAXES.md` |
| A Delaware LLC or corp operating in GA, and DE vs. GA formation | `DELAWARE_ENTITY_IN_GEORGIA.md` |
| How do I pay myself? Draws vs. salary, S-corp election, estimated taxes | `PAYING_FOUNDERS.md` |
| Which laws apply at 1/15/20/50/100 employees, and what's due this year | `HEADCOUNT_TRIGGERS_AND_COMPLIANCE_CALENDAR.md` |
| Overtime, exempt vs. non-exempt, minimum wage, pay frequency, interns, paying in equity | `EXEMPT_VS_NONEXEMPT_PAY_RULES.md` |
| Payroll provider vs. PEO, health insurance, QSEHRA/ICHRA, retirement plans, PTO | `PAYROLL_PEO_AND_BENEFITS.md` |
| Hiring someone in another state or another country, remote I-9, visas | `REMOTE_AND_OUT_OF_STATE_HIRES.md` |
| Firing, final pay, separation notice, severance, non-competes, equity when someone leaves | `FIRING_AND_OFFBOARDING_GA.md` |
| City or county business license or occupation tax (metro Atlanta) | `LOCAL_BUSINESS_LICENSES_METRO_ATLANTA.md` |
| Something not listed above: see `QUESTION_BANK.md` for planned topics | `QUESTION_BANK.md` |

## Using a package
The full rules for any assistant answering from these packages are in `ANSWERING_GUIDE.md`. In short:
1. Answer from the package, and cite its sources.
2. **Before sending**, re-check every row in "Double-check before sending" that the answer depends on. Fetch the live page. If the value changed, update the package and its `last_verified` date.
3. If a row is marked "verify manually" (sos.ga.gov and census.gov block automated access), tell the founder to confirm it at that link.
4. Point founders to the portals (Georgia Tax Center, the GA DOL Employer Portal, EFTPS, E-Verify) to do their own filings. We never log in.
5. These packages are general information, not legal or tax advice. Each package has a "When to bring in a professional" section. Use it.

## Format (any model, any retrieval pipeline)
- **Plain Markdown with YAML frontmatter:** `id`, `title`, `questions`, `tags`, `jurisdiction`, `audience`, `related`, `last_verified`, `status`. Use `questions` and `tags` for retrieval metadata.
- **Self-contained sections:** each `##` section stands on its own, so the files can be chunked by heading. No "see above". Dates are absolute.
- **No tool- or model-specific instructions:** the "Using a package" steps above describe *what* to do (fetch the live page, cite it), not *which tool* to use.
- **Text copies of every source PDF:** in `../text/<name>.txt`, each with a provenance header. Index those, not the PDFs.
- **Machine-readable index:** `../manifest.json` lists every package (path, questions, tags, related, sections, last verified) and every source document. Regenerate it after any change with `python3 -I ../build_manifest.py`. The script needs only the standard library, and it also lints for missing frontmatter, a missing By stage section, and "see above".
- **Suggested RAG setup:** index `PACKAGES/*.md` (skip `_TEMPLATE.md`), `../SOURCES.md`, and `../text/*.txt`. Chunk on `##` headings and carry the frontmatter as chunk metadata. Rank packages above raw source text, and prefer the newer `last_verified`.

## Upkeep
- Re-verify everything each January, after the new rates, wage bases, and form revisions are published. Also re-verify after the November FUTA credit-reduction announcement.
- Known time bombs as of 2026-10-25:
  - The GA SUI 0.06% assessment expires Dec 31, 2026.
  - The 2026 FUTA credit-reduction list is due after Nov 10, 2026.
  - The DE LLC tax goes up to $400 for the 2026 tax year, due June 1, 2027.
- Known source-PDF problems: `dol224.pdf` (R-11-24) prints outdated FLSA figures ($455/wk, a $100K HCE threshold, and the old intern test) and an outdated federal sexual-orientation statement (pre-*Bostock*). `p1635.pdf` (2014) and `dol4e.pdf` (2016) are stale. Prefer the live pages.
- New package: copy `_TEMPLATE.md` and add a row above.
