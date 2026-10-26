---
id: equity-for-early-hires
title: "Equity for Early Hires"
questions: ["How do I deal with equity planning and division for new hires?", "How much equity should I give my first employee?", "Can my LLC give stock options?", "What is a 409A and do I need one before granting options?", "What's an 83(b) election?", "Can I give equity to a contractor?"]
tags: [equity, stock-options, iso, nso, restricted-stock, 409a, 83b-election, profits-interests, option-pool, rule-701]
jurisdiction: [US-federal, GA]
audience: [pre-revenue, funded-2-10]
related: [first-hire-checklist, employee-vs-contractor, paying-founders, delaware-entity-in-georgia, ga-employer-taxes, exempt-vs-nonexempt-pay-rules, headcount-triggers-and-compliance-calendar]
last_verified: 2026-10-26
status: active
---

# Equity for Early Hires

> General information for founders, not legal or tax advice. Confirm specifics with a CPA or attorney before acting.

## Short answer
Your entity type decides what you can grant. A C-corp can grant stock options (ISOs or NSOs) or restricted stock. An LLC taxed as a partnership grants profits interests instead, and the holder becomes a partner who gets a K-1. Before granting options, adopt a board-approved equity plan, get a 409A valuation, and set the strike price at or above fair market value. The usual vesting is 4 years with a 1-year cliff. Anyone getting restricted stock has 30 days to file an 83(b) election. Pool and grant sizes are market norms, not rules.

## By stage
- **Pre-revenue founders:**
  - Your entity decides what you can grant. An LLC taxed as a partnership grants profits interests, and the holder becomes a partner who gets a K-1 instead of a W-2 and leaves normal payroll ([IRS Entities FAQ](https://www.irs.gov/faqs/small-business-self-employed-other-business/entities/entities-1)). If you'll want to grant options, ask counsel about converting to a C-corp before the first grant.
  - Founders with vesting restricted stock usually file an 83(b) election, which must be filed no later than 30 days after the shares are transferred ([26 CFR 1.83-2(b)](https://www.law.cornell.edu/cfr/text/26/1.83-2); [Cooley GO, secondary](https://www.cooleygo.com/founder-basics-founders-stock/)).
  - Before granting any option: adopt a board-approved plan, get a 409A valuation no more than 12 months old at grant, and set the strike at or above FMV ([26 CFR 1.409A-1(b)(5)](https://www.law.cornell.edu/cfr/text/26/1.409A-1)).
  - **Can wait:** Rule 701's extra disclosure applies only above $10 million in grants in 12 months ([17 CFR 230.701(e)](https://www.law.cornell.edu/cfr/text/17/230.701)).
- **Funded teams hiring 2–10:**
  - Size the pool to 12–18 months of hiring. Carta materials put seed-stage pools at about 10–15% of fully diluted shares (secondary, [Carta option pool guide](https://carta.com/learn/startups/equity-management/option-pool/)).
  - Carta data shows a median first grant of about 1.49% of fully diluted shares for hire #1, falling to about 0.3% by hire #5–6 (secondary, [Carta](https://carta.com/data/linkedin-first-hire-equity-benchmarks-by-sector/)).
  - The board approves each grant, and the 409A valuation must still be no more than 12 months old at each grant date.
  - Payroll has to handle NSO exercises by employees (supplemental withholding, W-2 code V) and Form 3921 for ISO exercises ([Pub 5992](https://www.irs.gov/pub/irs-pdf/p5992.pdf) p.10; [Form 3921](https://www.irs.gov/forms-pubs/about-form-3921)).
  - Check the ISO $100,000 annual limit and the Rule 701 12-month totals every year.
  - Double-trigger acceleration is far more common than single-trigger, and investors often resist single-trigger ([Cooley GO](https://www.cooleygo.com/what-are-single-and-double-trigger-acceleration-and-how-do-they-work/), secondary).

## What you need to know

**1. Entity type**
- **C-corp:** can grant both kinds of option.
  - **ISOs** (incentive stock options): employees only. The holder must be employed from grant until 3 months before exercise ([26 USC 422(a)(2)](https://www.law.cornell.edu/uscode/text/26/422)). Requirements: shareholder approval of the plan within 12 months, a strike of at least FMV (fair market value), and a term of 10 years or less. For holders of more than 10%, the strike must be 110% of FMV and the term 5 years or less ([422(b), (c)(5)](https://www.law.cornell.edu/uscode/text/26/422)). The employee owes no regular income tax at exercise but may owe AMT ([IRS Topic 427](https://www.irs.gov/taxtopics/tc427)).
  - **NSOs** (nonstatutory options): can go to employees, directors, or contractors. The spread at exercise (FMV minus strike) is taxable income when there's no readily determinable value at grant, which is the normal case for a private company ([Topic 427](https://www.irs.gov/taxtopics/tc427)).
  - **Restricted stock (RSAs):** the person receives actual shares that vest over time. Income is taxed as the shares vest unless the holder files an 83(b) election ([IRS Pub 5992, ATG](https://www.irs.gov/pub/irs-pdf/p5992.pdf) pp.8–9).
- **Board's role:** for a Georgia corporation, the board sets option terms ([O.C.G.A. § 14-2-624](https://codes.findlaw.com/ga/title-14-corporations-partnerships-and-associations/ga-code-sect-14-2-624/)) and must determine that the consideration for shares is adequate ([§ 14-2-621](https://codes.findlaw.com/ga/title-14-corporations-partnerships-and-associations/ga-code-sect-14-2-621/)). Both are FindLaw copies current as of March 28, 2024. A Delaware corporation follows Delaware law instead.
- **LLC taxed as a partnership:** the usual tool is a **profits interest**, a share of future growth only. The IRS doesn't treat the grant of a profits interest as taxable if the conditions of Rev. Proc. 93-27 are met. Rev. Proc. 2001-43 extends this to unvested interests, with three conditions. The holder is treated as a partner from grant and reports their share of income, nobody deducts the interest's value, and no 83(b) election is needed ([Rev. Proc. 2001-43, IRB 2001-34 pp.191–192](https://www.irs.gov/pub/irs-irbs/irb01-34.pdf)). The catch is that partners aren't employees. They're self-employed, get a K-1 instead of a W-2, and pay self-employment tax ([IRS Entities FAQ](https://www.irs.gov/faqs/small-business-self-employed-other-business/entities/entities-1)). That takes the hire off normal payroll. For LLC "unit options" I found no simple official guidance, so ask a tax attorney.

**2. 409A and strike price**
An option counts as deferred compensation unless its strike price can never be below FMV on the grant date ([26 CFR 1.409A-1(b)(5)](https://www.law.cornell.edu/cfr/text/26/1.409A-1)). If an option breaks the 409A rules, the income becomes taxable immediately, plus a 20% additional tax and interest ([26 USC 409A(a)(1)](https://www.law.cornell.edu/uscode/text/26/409A)). The regulation lists three valuation methods presumed reasonable ([1.409A-1(b)(5)(iv)(B)](https://www.law.cornell.edu/cfr/text/26/1.409A-1)):
- An independent appraisal dated no more than 12 months before the grant.
- A written startup valuation (company under 10 years old) by a qualified person. Not available if a sale is expected within 90 days or an IPO within 180 days.
- A formula valuation that meets the regulation's conditions.

**3. ISO $100k limit**
ISOs that become exercisable for the first time in one calendar year can cover at most $100,000 of stock, measured at grant-date FMV. Anything above that is treated as an NSO ([422(d)](https://www.law.cornell.edu/uscode/text/26/422); [Pub 5992](https://www.irs.gov/pub/irs-pdf/p5992.pdf) p.11).

**4. 83(b) election**
The holder can choose to be taxed now, at the shares' current value, instead of as they vest. The election must be filed no later than 30 days after the property is transferred ([26 CFR 1.83-2(b)](https://www.law.cornell.edu/cfr/text/26/1.83-2)). If day 30 falls on a weekend or holiday, a postmark on the next business day still counts. Mail it to the IRS using Form 15620 (Rev. 4-2025) or a written statement, and give a copy to the company. It can't be revoked without IRS consent ([Form 15620](https://www.irs.gov/pub/irs-pdf/f15620.pdf)). Founders with vesting stock usually file one ([Cooley GO, secondary](https://www.cooleygo.com/founder-basics-founders-stock/)).

**5. Vesting and acceleration (secondary sources)**
- A common schedule is 4 years, vesting monthly or quarterly, often with a 1-year cliff ([Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/)).
- **Single-trigger acceleration:** vesting speeds up on one event, usually a sale of the company.
- **Double-trigger acceleration:** vesting speeds up only after both a sale and a qualifying termination, usually within 9–18 months after closing. Double-trigger is far more common, and investors often resist single-trigger ([Cooley GO](https://www.cooleygo.com/what-are-single-and-double-trigger-acceleration-and-how-do-they-work/)).

**6. Pool size and grant ranges (secondary, market norms only)**
- **Pool size:** Carta materials put seed-stage pools at about 10–15% of fully diluted shares, with seed medians around 12–14%. They recommend sizing the pool to 12–18 months of hiring ([Carta option pool guide](https://carta.com/learn/startups/equity-management/option-pool/); [Carta data](https://carta.com/data/linkedin-employee-option-pool-by-company-stage/)).
- **First grants:** Carta data covering about 8,000 grants (June 2023–June 2024) shows a median of about 1.49% of fully diluted shares for hire #1, falling to about 0.3% by hire #5–6 ([Carta](https://carta.com/data/linkedin-first-hire-equity-benchmarks-by-sector/)).
- **Caveat:** Carta blocks automated fetches, so these figures come from search excerpts, not full pages. Treat them as rough ranges.

**7. Securities law**
- **Federal:** Rule 701 exempts grants by private companies under a written compensatory plan. It covers employees, directors, officers, and individual consultants whose services aren't tied to fundraising ([17 CFR 230.701(c)](https://www.law.cornell.edu/cfr/text/17/230.701)).
  - **12-month cap:** the greatest of $1,000,000, 15% of total assets, or 15% of the outstanding class ([701(d)](https://www.law.cornell.edu/cfr/text/17/230.701)).
  - **Above $10 million in 12 months:** extra disclosure is required, including risk information and financial statements ([701(e)](https://www.law.cornell.edu/cfr/text/17/230.701)).
  - **Also:** the shares are restricted securities, and antifraud rules still apply.
- **Georgia:** O.C.G.A. § 10-5-11(21) exempts employee stock option, purchase, and similar benefit-plan securities. It covers employees, directors, officers, consultants, and advisers. The FindLaw copy (current as of March 28, 2024) shows no notice filing ([FindLaw](https://codes.findlaw.com/ga/title-10-commerce-and-trade/ga-code-sect-10-5-11/)). One Georgia rule still cites the older paragraph number, (14) ([GA Rule 590-4-1-.01](https://rules.sos.ga.gov/gac/590-4-1)).

**8. Employer tax side**
- **ISO exercise:** no Social Security, Medicare, FUTA, or income tax withholding ([Pub 15-B](https://www.irs.gov/publications/p15b); [Pub 5992](https://www.irs.gov/pub/irs-pdf/p5992.pdf) p.10).
- **ISO sold early** (within 2 years of grant or 1 year of exercise): the income is W-2 wages, but with no Social Security, Medicare, FUTA, or income tax withholding ([Pub 5992](https://www.irs.gov/pub/irs-pdf/p5992.pdf) pp.10–11).
- **ISO reporting:** the corporation files Form 3921 for each ISO exercise ([IRS](https://www.irs.gov/forms-pubs/about-form-3921)).
- **NSO exercise by an employee:** the spread is wages. It's subject to Social Security, Medicare, FUTA, and income tax withholding at exercise ([Pub 5992](https://www.irs.gov/pub/irs-pdf/p5992.pdf) p.10, citing Rev. Rul. 78-185). (Pub 5992 says it isn't an official IRS pronouncement.)
  - **W-2:** report the spread in boxes 1, 3 (up to the wage base), and 5, and in box 12 with code V ([Pub 15-B](https://www.irs.gov/publications/p15b); [Pub 525](https://www.irs.gov/publications/p525)).
  - **Federal withholding:** treated as supplemental wages, at a flat 22%, or 37% on supplemental wages above $1 million in the year. Social Security, Medicare, and FUTA still apply (`REFERENCE/INFO/first-hire/p15.pdf` p.2 and pp.23–24).
  - **Georgia withholding:** bonuses and other compensation are withheld at the Georgia income tax rate in effect. That was 5.19%, and employers could switch to 4.99% starting May 11, 2026 (`REFERENCE/INFO/first-hire/2026 Employers_Tax_Guide.pdf` p.14). The guide doesn't specifically mention option spreads.
  - **Cash problem:** the exercise pays no cash, so decide in advance how the employee will fund the withholding. Settle the mechanics with your CPA.
  - **Deduction:** the company generally gets a matching deduction under IRC 83(h) ([Pub 5992](https://www.irs.gov/pub/irs-pdf/p5992.pdf) p.8).
- **Contractors:** contractors can receive NSOs or restricted stock but not ISOs. The IRS reports nonemployee compensation on Form 1099-NEC ([1099 instructions](https://www.irs.gov/instructions/i1099mec)). I didn't find IRS text on option spreads for that form, so confirm with a CPA.
- **Founder vs. employee equity:** founders usually hold restricted common stock with vesting, file an 83(b) election, and are subject to buyback of unvested shares if they leave. Employees usually get options ([Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/), secondary).

## Steps
1. **Confirm your entity and tax status.** Check your Georgia SOS record (sos.ga.gov blocks automated access, so verify manually) and your IRS election. An LLC that wants options should ask counsel about converting before the first grant. You get an options vs. profits-interest decision.
2. **Adopt an equity incentive plan.** Counsel drafts it, the board adopts it, and shareholders approve it within 12 months so it can grant ISOs ([26 USC 422(b)](https://www.law.cornell.edu/uscode/text/26/422)). You get a plan and a reserved pool.
3. **Size the pool** to your 12–18 month hiring plan (secondary Carta benchmarks: about 10–15% of fully diluted shares at seed). You get a pool number on the cap table.
4. **Get a 409A valuation** from an independent appraiser. To get the safe harbor, it must be no more than 12 months old at grant ([1.409A-1(b)(5)(iv)(B)](https://www.law.cornell.edu/cfr/text/26/1.409A-1)). You get the FMV per share.
5. **Set up a cap table tool** with founder shares, the pool, and any SAFEs or notes. You get one source of truth for ownership.
6. **Board approves each grant:** recipient, shares, ISO or NSO, strike at or above FMV, vesting, and acceleration ([§ 14-2-624](https://codes.findlaw.com/ga/title-14-corporations-partnerships-and-associations/ga-code-sect-14-2-624/)). You get minutes or a written consent.
7. **Sign the grant agreement** and deliver a copy of the plan ([Rule 701(e)](https://www.law.cornell.edu/cfr/text/17/230.701)). You get a signed agreement.
8. **Restricted stock or early exercise:** the holder mails the 83(b) election within 30 days ([Form 15620](https://www.irs.gov/pub/irs-pdf/f15620.pdf)) and gives the company a copy. You keep proof of mailing on file.
9. **Payroll:** set up NSO exercise handling (supplemental withholding, W-2 code V) and Form 3921 filing for ISO exercises ([Form 3921](https://www.irs.gov/forms-pubs/about-form-3921)). You get correct withholding and year-end forms.
10. **Every year:** check the ISO $100k limit and the Rule 701 12-month totals.

## Links
| Resource | URL | Why |
|----------|-----|-----|
| 26 USC 422 (ISOs) | https://www.law.cornell.edu/uscode/text/26/422 | ISO rules, $100k limit |
| 26 CFR 1.409A-1 | https://www.law.cornell.edu/cfr/text/26/1.409A-1 | FMV and valuation safe harbors |
| 26 CFR 1.83-2 | https://www.law.cornell.edu/cfr/text/26/1.83-2 | 83(b) election rules |
| Form 15620 | https://www.irs.gov/pub/irs-pdf/f15620.pdf | IRS 83(b) form |
| Pub 15-B | https://www.irs.gov/publications/p15b | Option W-2 and FICA treatment |
| Pub 5992 (Equity ATG) | https://www.irs.gov/pub/irs-pdf/p5992.pdf | IRS examiner view of NSO/ISO taxes |
| Rev. Proc. 2001-43 | https://www.irs.gov/pub/irs-irbs/irb01-34.pdf | LLC profits interests |
| SEC Rule 701 | https://www.law.cornell.edu/cfr/text/17/230.701 | Federal securities exemption |
| O.C.G.A. 10-5-11 | https://codes.findlaw.com/ga/title-10-commerce-and-trade/ga-code-sect-10-5-11/ | Georgia exemption |
| IRS Pub 15 (2026) | `REFERENCE/INFO/first-hire/p15.pdf` | Supplemental wage withholding |

## Double-check before sending
| Item | Value as of last check | Where to verify | Last verified |
|------|------------------------|-----------------|---------------|
| 83(b) deadline | 30 days after transfer; next business day if weekend or holiday | Form 15620 instructions; 26 CFR 1.83-2(b) | 2026-10-25 |
| Form 15620 revision | Rev. 4-2025, filed by mail | irs.gov/pub/irs-pdf/f15620.pdf | 2026-10-25 |
| ISO annual limit | $100,000 (grant-date FMV) | 26 USC 422(d) | 2026-10-25 |
| ISO plan approval / term | Shareholders within 12 months; 10-year term (5 years and 110% of FMV for >10% owners) | 26 USC 422(b), (c)(5) | 2026-10-25 |
| 409A appraisal age | No more than 12 months old; startup method for companies under 10 years old | 26 CFR 1.409A-1(b)(5)(iv)(B) | 2026-10-25 |
| 409A penalty | 20% additional tax plus interest | 26 USC 409A(a)(1)(B) | 2026-10-25 |
| Rule 701 cap | Greatest of $1M, 15% of assets, or 15% of class per 12 months | 17 CFR 230.701(d) | 2026-10-25 |
| Rule 701 disclosure trigger | More than $10M in 12 months | 17 CFR 230.701(e) | 2026-10-25 |
| GA exemption paragraph | § 10-5-11(21) (FindLaw copy, current as of 3/28/2024) | Official O.C.G.A. (verify manually) | 2026-10-25 |
| Federal supplemental withholding | 22%; 37% above $1M | p15.pdf p.2, pp.23–24 | 2026-10-25 |
| 2026 Social Security wage base | $184,500 | p15.pdf p.2 | 2026-10-25 |
| 2027 Social Security wage base | $192,300 (announced by SSA Oct 14, 2026; applies to NSO spreads and other wages paid in 2027) | https://www.ssa.gov/oact/cola/cbb.html (returns 403 to automated checks; read from the Internet Archive capture of 2026-10-20) | 2026-10-26 |
| GA supplemental withholding | 5.19%, then 4.99% from May 11, 2026 | GA DOR guide p.14 | 2026-10-25 |
| Seed pool norm (secondary) | ~10–15% fully diluted | Carta (blocked; verify manually) | 2026-10-25 (excerpt only) |
| First-hire median grant (secondary) | ~1.49% (2023–24 data); ~0.3% by hire 5–6 | Carta data posts (verify manually) | 2026-10-25 (excerpt only) |
| Double-trigger window (secondary) | Usually 9–18 months after closing | Cooley GO | 2026-10-25 |

## When to bring in a professional
- **Corporate attorney:** plan and grant documents, LLC-to-C-corp conversion, grants to contractors or advisers, acceleration terms, total grants near $10M in 12 months, and hires outside Georgia.
- **CPA or tax attorney:** profits interests and LLC unit options, early exercise and 83(b) elections, ISO vs. NSO questions, funding NSO withholding, and grants to anyone owning more than 10%.
- **Valuation firm:** the 409A appraisal.

## Related packages
- `FIRST_HIRE_CHECKLIST.md`: the step-by-step hub
- `EMPLOYEE_VS_CONTRACTOR.md`: classifying the worker
- `EXEMPT_VS_NONEXEMPT_PAY_RULES.md`: overtime, minimum wage, pay frequency
- `PAYING_FOUNDERS.md`: draws, salary, S-corp election
- `GA_EMPLOYER_TAXES.md`: withholding, FICA, FUTA, GA UI, filing calendar
- `PAYROLL_PEO_AND_BENEFITS.md`: payroll provider vs. PEO, health and retirement benefits
- `REMOTE_AND_OUT_OF_STATE_HIRES.md`: employees in other states and abroad
- `FIRING_AND_OFFBOARDING_GA.md`: terminations, final pay, severance, equity on exit
- `HEADCOUNT_TRIGGERS_AND_COMPLIANCE_CALENDAR.md`: laws by headcount, plus annual deadlines
- `DELAWARE_ENTITY_IN_GEORGIA.md`: foreign registration and costs in both states
- `LOCAL_BUSINESS_LICENSES_METRO_ATLANTA.md`: city and county occupation tax certificates
