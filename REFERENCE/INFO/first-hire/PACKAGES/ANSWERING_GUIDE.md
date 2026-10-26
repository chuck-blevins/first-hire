---
title: "Answering Guide for Any Assistant Using These Packages"
tags: [first-hire, agent-instructions, rag]
status: active
created: 2026-10-25
last_verified: 2026-10-25
---

# Answering Guide for Any Assistant Using These Packages

This file is model-neutral. Any assistant (Claude or another LLM) or retrieval (RAG) pipeline answering founder questions from `REFERENCE/INFO/first-hire/PACKAGES/` should follow it. It doesn't depend on any one vendor's memory or tools.

## Scope
- **Audience:** startup founders, both pre-revenue and funded teams hiring 2–10 people.
- **Jurisdiction:** US federal plus Georgia. Delaware only as the state of formation.
- **Not legal or tax advice.** For judgment calls (entity choice, classification of a specific worker, equity terms), point the founder to a CPA or attorney.

## How to answer
1. **Find the package.** Use `README.md` (question → package map) or match the founder's question against each package's `questions:` frontmatter.
2. **Answer from the package first:** start with the Short answer, add the By stage notes for the founder's stage, then Steps and Links.
3. **Re-check what changes.** Any figure you use that appears in a package's "Double-check before sending" table (a rate, wage base, fee, threshold, or due date) has to be re-checked against the live URL in that row before you send it. If you can't fetch it, give the figure with its `last_verified` date and say so.
4. **Cite.** Give the official URL for each fact. Give local PDFs as `REFERENCE/INFO/first-hire/<file>.pdf` p.N.
5. **Point, don't log in.** Login portals (Georgia Tax Center, GA DOL Employer Portal, EFTPS, IRS EIN) are where the founder goes. Never ask for their credentials.

## Sources you can't trust as-is
- `dol224.pdf` (GA DOL handbook): outdated overtime figures and pre-*Bostock* statements. Don't quote it for either.
- `p1635.pdf` (2014) and `dol4e.pdf` (2016): superseded. Use the live versions.
- `GA-At-Will Employment.pdf`: State Accounting Office policy for state employees, not Georgia law.
- Any fact the packages flag as "Couldn't verify": say it's unverified when you use it.

## Freshness
- A package whose `last_verified` date is more than 12 months old, or older than the most recent January, is stale. Re-verify its double-check rows before relying on it.
- If a package and a live official source disagree, the live source wins. Tell the founder about the discrepancy and flag it to the package maintainer.
