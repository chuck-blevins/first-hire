---
id: paying-founders
title: "How Founders Pay Themselves, by Entity Type"
questions: ["How do I pay myself?", "Should I take a salary or draws?", "Should my LLC elect S-corp?", "What is reasonable compensation for an S-corp owner?", "Can I work for free until we raise?", "Can I put myself on payroll as an LLC owner?", "Do I need to pay quarterly estimated taxes?", "What salary do investors expect founders to take?"]
jurisdiction: [US-federal, GA]
tags: [founder-compensation, s-corp, llc, c-corp, estimated-taxes, self-employment-tax]
audience: [pre-revenue, funded-2-10]
related: [ga-employer-taxes, equity-for-early-hires, exempt-vs-nonexempt-pay-rules, delaware-entity-in-georgia, payroll-peo-and-benefits]
last_verified: 2026-10-25
status: active
---

# How Founders Pay Themselves, by Entity Type

> General information for founders, not legal or tax advice. Confirm specifics with a CPA or attorney before acting.

## Short answer
How you pay yourself depends on how the company is **taxed**:
- **LLC (single-member or partnership):** draws or distributions, never W-2 payroll. You owe self-employment (SE) tax on your share of profit whether or not you take the cash.
- **S-corp:** a "reasonable" W-2 salary, then distributions free of Social Security and Medicare tax. It pays off only once profit comfortably covers that salary plus the extra payroll and filing costs.
- **C-corp:** founders who work in the business are W-2 employees, and dividends are taxed twice.

If nothing is withheld from what you take, pay quarterly estimates to the IRS (1040-ES) and Georgia (500-ES).

## By stage
- **Pre-revenue founders:** You don't have to pay yourself. A 20%+ owner who runs the company is exempt from federal minimum wage (item 6), and an LLC with no profit owes no SE tax. **Now:** separate business and personal money, document money you put in (loan or capital), and skip the S-corp until there's real profit. **Can wait:** your own payroll and the PTE election.
- **Funded teams hiring 2–10:** Most VC-backed companies are Delaware C-corps, so founders go on W-2 payroll with the first hires (GA_EMPLOYER_TAXES.md). An S-corp stops working at priced rounds: it can't have preferred stock or fund shareholders ([i2553](https://www.irs.gov/instructions/i2553)). Founder-officers count toward Georgia's 3-employee workers' comp threshold (FIRST_HIRE_CHECKLIST.md).

## What you need to know

**1. Single-member LLC (disregarded).**
- **Not an employee:** the LLC "is not the employer of its owner," so no W-2 for you ([26 CFR 301.7701-2(c)(2)(iv)(C)(2)](https://www.law.cornell.edu/cfr/text/26/301.7701-2); [IRS: SMLLCs](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies)). Draws move cash whenever you like. Profit is what's taxed, taken or not.
- **SE tax:** 15.3% (12.4% Social Security + 2.9% Medicare) on 92.35% of net SE earnings of $400 or more. You deduct half, on Schedule SE ([IRS Topic 554](https://www.irs.gov/taxtopics/tc554)). The Social Security part stops at the $184,500 2026 wage base ([2026 Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) p.9). An extra 0.9% Medicare applies above $200,000 single / $250,000 joint ([Topic 554](https://www.irs.gov/taxtopics/tc554)). Hired employees go on payroll under the LLC's own EIN (`REFERENCE/INFO/first-hire/2026 Employers_Tax_Guide.pdf` p.28).

**2. Multi-member LLC (partnership).**
- **Not employees:** "Partners are not employees and shouldn't be issued a Form W-2"; they get a K-1 ([IRS: Partnerships](https://www.irs.gov/businesses/small-businesses-self-employed/partnerships)). No withholding, FICA or FUTA on partner payments (`REFERENCE/INFO/first-hire/p15.pdf` p.51).
- **Guaranteed payments** are fixed pay for your work, set regardless of profit. The partnership deducts them, and you report ordinary income with nothing withheld. **Distributions** are cash against your share of profit and reduce your basis ([IRS Pub 541](https://www.irs.gov/publications/p541), Rev. 12/2025). Your share of profit is taxed either way.
- **SE tax:** general partners pay on guaranteed payments plus their share of profit. Limited partners pay only on guaranteed payments for services ([Schedule SE instructions](https://www.irs.gov/instructions/i1040sse)). Whether *LLC members* qualify as limited partners is unsettled, with appeals pending ([Cooley, 2026-10-13](https://www.cooley.com/news/insight/2026/2026-10-13-recent-circuit-court-decisions-coalesce-on-scope-of-lp-self-employment-tax-exception), *secondary*). Working members should assume SE tax on their full share.
- **Nonresident members:** Georgia requires 4% withholding on their distributions (`2026 Employers_Tax_Guide.pdf` p.25).

**3. S-corp election.**
- **Form 2553:** a corporation or LLC files it (an LLC needs no Form 8832) **within 2 months and 15 days after the start of the tax year** it should take effect, or any time the year before. For a calendar-year company that's March 15. File by mail or fax, with every shareholder's consent. Late relief (Rev. Proc. 2013-30) runs 3 years and 75 days ([i2553](https://www.irs.gov/instructions/i2553), Rev. 12/2020).
- **Eligibility:** 100 or fewer shareholders, individuals only (or certain trusts and estates), no nonresident aliens, one class of stock ([i2553](https://www.irs.gov/instructions/i2553)).
- **Reasonable compensation:** pay a reasonable W-2 salary before distributions. The IRS weighs training, duties, time spent, and "what comparable businesses pay for similar services," and it can reclassify distributions as wages ([IRS: S-corp compensation](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues); `p15.pdf` p.50). No official percentage or formula exists.
- **Trade-off (simplified illustration):** on $120,000 of profit, a single-member LLC owes about $16,955 SE tax ($120,000 × 92.35% × 15.3%). An S-corp paying a $70,000 salary owes $10,710 FICA, plus $42 FUTA and $256.50 GA UI (2.70% × $9,500, per GA_EMPLOYER_TAXES.md). That saves about **$5,900/yr** before payroll-provider and CPA fees for the 1120-S and GA 600S. Have a CPA model your numbers.
- **2% shareholder health insurance:** premiums for a >2% owner go in W-2 box 1 only, not boxes 3/5 (no FICA or FUTA). The owner may then take the self-employed health insurance deduction ([IRS: S-corp compensation](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues); `p15.pdf` p.20).
- **Georgia recognizes S-corps**; I found no separate state election. Each nonresident shareholder must sign Form 600S-CA, or Georgia taxes the company as a C-corp ([GA DOR S-corp FAQ](https://dor.georgia.gov/s-corporations-faq)).
- **GA pass-through entity (PTE) tax election: still available.** S-corps and partnerships can elect yearly (tax years from 2022 on) to pay Georgia tax at the entity level, on Form 600S or 700 by the extended due date. It's irrevocable after that, and the entity then pays estimates like a C-corp ([HB 149 FAQ](https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq)). Rate: 4.99% ([GA DOR partnerships](https://dor.georgia.gov/taxes/taxes-partnerships)). The payoff depends on federal SALT-deduction rules, so ask a CPA.

**4. C-corp.**
- **Founders are employees:** officers who work in the business are employees (`p15.pdf` p.14), on payroll like any hire (GA_EMPLOYER_TAXES.md).
- **Double tax:** the corporation deducts a "reasonable allowance for salaries" ([26 USC 162(a)(1)](https://www.law.cornell.edu/uscode/text/26/162)) and pays 21% federal ([26 USC 11(b)](https://www.law.cornell.edu/uscode/text/26/11)) plus Georgia's 4.99% (DELAWARE_ENTITY_IN_GEORGIA.md). Dividends come out of what's left and are taxed again to you, at capital-gain rates if qualified ([IRS Topic 404](https://www.irs.gov/taxtopics/tc404)). Most startups pay none.
- **Accountable plan:** reimbursements aren't wages if the plan requires a business expense, receipts within a reasonable time, and return of any excess. Pub 15's safe timing is advance within 30 days, receipts within 60, excess back within 120. Otherwise the reimbursements are taxable wages (`p15.pdf` p.19). S-corps can use one too.

**5. Getting paid before revenue.**
- **Deferring** (taking nothing) is simplest. 20%+ owner-managers: see item 6.
- **Accruing salary has risks.** It's real debt the company owes you. The company can't deduct it until paid if you own >50% of a C-corp or any share of an S-corp or partnership ([26 USC 267(a)(2), (b)(2), (e)](https://www.law.cornell.edu/uscode/text/26/267)). Pay that's owed in one year but paid after the 2½-month short-term window can fall under 409A ([26 CFR 1.409A-1(b)(1), (b)(4)](https://www.law.cornell.edu/cfr/text/26/1.409A-1)). When it's paid, it's wages that year, with full payroll tax. *Practice note, not from an official source:* investors often ask founders to waive accrued salary at a priced round.
- **Founder loans to the company:** sign a promissory note with the amount, interest, repayment terms, and board or member approval. Loans below the applicable federal rate (AFR) trigger imputed interest on corporation-shareholder loans over $10,000 ([26 USC 7872](https://www.law.cornell.edu/uscode/text/26/7872); [IRS AFR](https://www.irs.gov/applicable-federal-rates)). *Practice note:* without a note, repayments are harder to defend as non-taxable.

**6. The minimum-wage trap.**
- **Rule:** employees "may not volunteer services to for-profit private sector employers" ([DOL elaws](https://webapps.dol.gov/elaws/whd/flsa/docs/volunteers.asp)). The federal minimum is $7.25/hr; Georgia's $5.15 doesn't apply to FLSA-covered employers ([DOL](https://www.dol.gov/agencies/whd/minimum-wage/state)). Enterprise coverage starts at $500,000 in sales, but workers who regularly do interstate work are covered at any size ([Fact Sheet 14](https://www.dol.gov/agencies/whd/fact-sheets/14-flsa-coverage)).
- **Exemption (confirmed):** an owner with "at least a bona fide 20-percent equity interest" who is "actively engaged in its management" is an exempt executive, with no salary test ([29 CFR 541.101](https://www.law.cornell.edu/cfr/text/29/541.101); [Fact Sheet 17B](https://www.dol.gov/agencies/whd/fact-sheets/17b-overtime-executive)).
- **Risk:** an officer or "co-founder" under 20% working unpaid or for equity only. Partners and sole proprietors aren't employees at all.

**7. Quarterly estimated taxes.**
- **Federal:** required if you expect to owe $1,000+ after withholding ([IRS](https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes)). Safe harbor: pay the smaller of 90% of this year's tax or 100% of last year's (110% if last year's AGI topped $150,000, or $75,000 married filing separately). 2026 dates: Apr 15, Jun 15, Sep 15, and Jan 15, 2027 ([2026 Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) pp.1, 5).
- **Georgia (500-ES):** required if you expect more than $1,000 of income not subject to withholding, beyond exemptions and deductions. Same four dates ([GA 500-ES](https://dor.georgia.gov/500-es-individual-and-fiduciary-estimated-tax-payment-voucher)). Form 500-UET sets each payment at the lesser of 100% of last year's tax or 70% of this year's; I found no 110% rule. The penalty is 9%/yr ([500-UET](https://dor.georgia.gov/500-uet-underpayment-estimated-tax-individualfiduciary)). *Discrepancy:* the "2026" 500-ES download is Rev. 05/12/25 with 2025 deduction amounts.
- **W-2 founders** (S-corp or C-corp) can raise their withholding instead of paying estimates (same sources).

**8. Georgia unemployment insurance (UI) for founders.**
- **Corporate officers, including S-corp officers, are employees by statute.** Their wages are covered at the rates in GA_EMPLOYER_TAXES.md (`REFERENCE/INFO/first-hire/dol224.pdf` p.48), and FUTA applies too (`p15.pdf` p.14).
- **Not covered:** proprietors and partners (`dol224.pdf` p.54).
- **LLCs follow their tax status:** taxed as a partnership, treated as one; taxed as a corporation, treated as one ([GA Rule 300-2-7-.12](https://rules.sos.ga.gov/gac/300-2-7)). So an LLC with an S election owes UI on owner-officer salaries. Managing members can be personally liable for unpaid contributions (same rule).

**9. What investors expect** *(secondary, ranges only).*
Kruze Consulting's 2026 payroll data on VC-backed clients shows CEO pay around **$153K seed, $203K Series A, $216K Series B** ([Kruze](https://kruzeconsulting.com/blog/startup-ceo-salary-report), updated 2026-09-03; the page labels these both averages and medians). Other surveys run lower. Runway and the board set the real number.

### Decision table
| Taxed as | How you get paid | Payroll for you? | SE tax or FICA | GA UI on your pay | Extra filings |
|---|---|---|---|---|---|
| SMLLC (disregarded) | Draws | No | SE tax on all profit | No | Sched. C + SE; 1040-ES/500-ES |
| Partnership LLC | Guaranteed payments + distributions | No | SE tax (scope for members is unsettled) | No | 1065/K-1; GA 700; estimates |
| S-corp | Reasonable W-2 salary + distributions | Yes | FICA on salary only | Yes | 2553; 1120-S; GA 600S (+600S-CA); payroll |
| C-corp | W-2 salary (dividends rare) | Yes | FICA on salary | Yes | 1120; GA 600; payroll |

## Steps
1. [ ] **Confirm your tax status** from your EIN letter and any Form 2553/8832 ([IRS EIN](https://www.irs.gov/businesses/employer-identification-number)), and your entity record at [GA SOS](https://sos.ga.gov/index.php/corporations) (verify manually). *You get:* your row in the decision table.
2. [ ] **Pay yourself only from a business bank account**, logging each transfer as a draw, distribution, loan repayment, or payroll. *You get:* clean books.
3. [ ] **Document founder loans** with a note at or above the [AFR](https://www.irs.gov/applicable-federal-rates), approved by the board or members. *You get:* a defensible loan.
4. [ ] **Pay quarterly estimates:** federal via [IRS Direct Pay](https://www.irs.gov/payments/direct-pay), Georgia via the [Georgia Tax Center](https://gtc.dor.ga.gov/_/) (the founder logs in). *You get:* no underpayment penalty.
5. [ ] **Decide on the S-corp with a CPA** once profit is steady, then file [Form 2553](https://www.irs.gov/forms-pubs/about-form-2553) on time. *You get:* an IRS acceptance letter.
6. [ ] **S-corp or C-corp: put yourself on payroll** using the registrations in GA_EMPLOYER_TAXES.md (EFTPS, GTC, GA DOL Employer Portal), and write down how you set the salary. *You get:* W-2 wages and a reasonable-comp file.
7. [ ] **S-corp health premiums:** the company pays them, and payroll reports them in box 1 only. *You get:* the self-employed health insurance deduction.
8. [ ] **Adopt a written accountable plan.** *You get:* tax-free reimbursements.
9. [ ] **Every year:** revisit the PTE election, reasonable comp, and your safe-harbor amount.

## Links
| Resource | URL | Why |
|----------|-----|-----|
| IRS: SMLLCs | https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies | Owner SE tax; LLC employment taxes |
| IRS Topic 554 | https://www.irs.gov/taxtopics/tc554 | SE tax mechanics |
| IRS Pub 541 | https://www.irs.gov/publications/p541 | Guaranteed payments, distributions |
| Form 2553 instructions | https://www.irs.gov/instructions/i2553 | S election deadline, eligibility, late relief |
| IRS: S-corp compensation | https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues | Reasonable comp; 2% shareholder health |
| 2026 Form 1040-ES | https://www.irs.gov/pub/irs-pdf/f1040es.pdf | Safe harbor, 2026 due dates |
| GA 500-ES | https://dor.georgia.gov/500-es-individual-and-fiduciary-estimated-tax-payment-voucher | GA estimated tax |
| GA 500-UET | https://dor.georgia.gov/500-uet-underpayment-estimated-tax-individualfiduciary | GA penalty exceptions |
| GA HB 149 PTE FAQ | https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq | Entity-level tax election |
| GA DOR S-corp FAQ | https://dor.georgia.gov/s-corporations-faq | 600S-CA nonresident consent |
| GA Rule 300-2-7-.12 | https://rules.sos.ga.gov/gac/300-2-7 | LLCs under GA UI law |
| 29 CFR 541.101 | https://www.law.cornell.edu/cfr/text/29/541.101 | 20% owner FLSA exemption |
| DOL elaws: volunteers | https://webapps.dol.gov/elaws/whd/flsa/docs/volunteers.asp | No volunteering for for-profits |
| IRS AFR tables | https://www.irs.gov/applicable-federal-rates | Founder loan interest floor |
| Georgia Tax Center | https://gtc.dor.ga.gov/_/ | GA estimated payments (founder logs in) |
| EFTPS | https://www.eftps.gov | Federal payroll deposits (founder logs in) |

## Double-check before sending
| Item | Value as of last check | Where to verify | Last verified |
|------|------------------------|-----------------|---------------|
| SE tax rate / base / threshold | 15.3% on 92.35% of net SE earnings; $400 minimum | IRS Topic 554 | 2026-10-25 |
| 2026 Social Security wage base | $184,500 (matches GA_EMPLOYER_TAXES.md) | 2026 Form 1040-ES p.9; Pub 15 p.2 | 2026-10-25 |
| Additional Medicare (SE) | 0.9% over $200K single / $250K MFJ / $125K MFS | IRS Topic 554 | 2026-10-25 |
| Form 2553 deadline | 2 months 15 days after start of tax year (Mar 15 for calendar year) | i2553 (Rev. 12/2020) | 2026-10-25 |
| Late S election relief | Within 3 years 75 days (Rev. Proc. 2013-30) | i2553 | 2026-10-25 |
| S-corp eligibility | ≤100 shareholders; one class of stock | i2553 | 2026-10-25 |
| 2% shareholder health rule | Box 1 only, not 3/5 | IRS S-corp page; Pub 15 p.20 | 2026-10-25 |
| GA PTE election | Available; annual; on 600S/700 by extended due date; irrevocable | HB 149 FAQ (page shows no update date) | 2026-10-25 |
| GA PTE rate | 4.99% | GA DOR partnerships page | 2026-10-25 |
| GA nonresident distribution withholding | 4% | 2026 DOR Employer's Tax Guide p.25 | 2026-10-25 |
| Federal corporate rate | 21% | 26 USC 11(b) | 2026-10-25 |
| GA corporate rate | 4.99% (per DELAWARE_ENTITY_IN_GEORGIA.md) | GA DOR corporate income tax page | 2026-10-25 (from that package) |
| Accountable plan time limits | 30 / 60 / 120 days | Pub 15 (2026) p.19 | 2026-10-25 |
| 7872 de minimis | $10,000 | 26 USC 7872(c)(3) | 2026-10-25 |
| AFR | Changes monthly | irs.gov/applicable-federal-rates | Not checked (look up at signing) |
| Federal minimum wage / GA rate | $7.25 / $5.15 (non-FLSA employers only) | DOL state minimum wage page | 2026-10-25 |
| FLSA enterprise threshold | $500,000 | DOL Fact Sheet 14 | 2026-10-25 |
| FLSA owner exemption | ≥20% equity and actively managing; no salary test | 29 CFR 541.101; Fact Sheet 17B | 2026-10-25 |
| Federal estimate threshold / safe harbor | $1,000; 90% / 100% (110% if AGI >$150K) | 2026 Form 1040-ES p.1 | 2026-10-25 |
| 2026 federal estimate dates | Apr 15, Jun 15, Sep 15 2026; Jan 15 2027 | 2026 Form 1040-ES p.5 | 2026-10-25 |
| GA estimate threshold / dates | >$1,000 not withheld; same 4 dates | GA 500-ES (Rev. 05/12/25; no true 2026 revision found) | 2026-10-25 |
| GA underpayment exceptions / penalty | Lesser of 100% prior / 70% current; 9%/yr | GA 500-UET (2025+) | 2026-10-25 |
| GA UI: officers covered; partners and proprietors not | As stated | dol224.pdf p.48, 54; Rule 300-2-7-.12 | 2026-10-25 |
| GA UI wage base / new-employer rate | $9,500 / 2.70% (see GA_EMPLOYER_TAXES.md; the 0.06% piece expires 12/31/26) | GA DOL | 2026-10-25 |
| LLC-member SE tax (limited-partner exception) | Unsettled; circuit litigation ongoing | Cooley 2026-10-13 (secondary); no IRS guidance found | Not verified officially |
| Founder salary ranges (secondary) | ~$153K seed / $203K A / $216K B | Kruze (secondary) | 2026-10-25 |

## When to bring in a professional
- **CPA:** before an S election; setting reasonable salary; the PTE election; nonresident or multi-state owners; accrued salary; uneven income (annualized estimates).
- **Tax attorney:** SE tax for non-managing LLC members, a missed 2553 deadline, LLC-to-C-corp conversion before a raise.
- **Employment attorney:** anyone unpaid or equity-only who isn't a 20%+ owner-manager.
- **Corporate attorney:** founder loan notes, waiving accrued salary at a financing, board approval of founder pay.

## Related packages
- `FIRST_HIRE_CHECKLIST.md`: the step-by-step hub
- `EMPLOYEE_VS_CONTRACTOR.md`: classifying the worker
- `EXEMPT_VS_NONEXEMPT_PAY_RULES.md`: overtime, minimum wage, pay frequency
- `EQUITY_FOR_EARLY_HIRES.md`: options, profits interests, 83(b), 409A
- `GA_EMPLOYER_TAXES.md`: withholding, FICA, FUTA, GA UI, filing calendar
- `PAYROLL_PEO_AND_BENEFITS.md`: payroll provider vs. PEO, health and retirement benefits
- `REMOTE_AND_OUT_OF_STATE_HIRES.md`: employees in other states and abroad
- `FIRING_AND_OFFBOARDING_GA.md`: terminations, final pay, severance, equity on exit
- `HEADCOUNT_TRIGGERS_AND_COMPLIANCE_CALENDAR.md`: laws by headcount, plus annual deadlines
- `DELAWARE_ENTITY_IN_GEORGIA.md`: foreign registration and costs in both states
- `LOCAL_BUSINESS_LICENSES_METRO_ATLANTA.md`: city and county occupation tax certificates
