# 2026-10-26 baseline

- **Answerer:** the Buzz agent "about your first hire" (Claude), answering cold from the packages at commit 7ecb90a, before the package fixes in PR #3. It used live re-checks and did not see the answer keys or the rubric.
- **Judge:** Claude Sonnet 5.5 via `claude -p`. It's a different model from the answerer, but the same vendor, so treat these scores as **provisional**. Re-judge with a non-Anthropic model when one is available.
- **Automated checks:** fact recall is 92% with 0 trap hits, after tuning the scope, clarifying-question, and q17 trap heuristics. The answers had triggered false positives on those.
- **Result:** 34 of 35 pass (97%), with no Safety 0. **The run passes.** The only failure is q35 (GA sales tax on SaaS, a topic no package covers). It scored 5/10 because it gave a tentative answer instead of declaring the question out of scope.
- **Weakest dimension:** Grounding (1.66 of 2). Figures were often stated without an inline citation even when the package has one.
