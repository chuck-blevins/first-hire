---
id: employee-vs-contractor
title: "Employee vs. Independent Contractor for Your First Technical Hire"
questions: ["I need to bring on a developer or first technical hire. Should it be a full-time employee or a contractor?", "Can I just pay my developer on a 1099?", "What does it cost to hire an employee vs. a contractor in Georgia?", "Who owns the code a contractor writes for me?", "Can I start someone as a contractor and convert them later?"]
tags: [worker-classification, independent-contractor, form-1099-nec, ip-assignment, ga-unemployment-insurance, flsa, contract-to-hire]
jurisdiction: [US-federal, GA]
audience: [pre-revenue, funded-2-10]
related: [first-hire-checklist, exempt-vs-nonexempt-pay-rules, ga-employer-taxes, equity-for-early-hires, paying-founders, headcount-triggers-and-compliance-calendar, remote-and-out-of-state-hires, payroll-peo-and-benefits]
last_verified: 2026-10-26
status: active
---

# Employee vs. Independent Contractor for Your First Technical Hire

> General information for founders, not legal or tax advice. Confirm specifics with a CPA or attorney before acting.

## Short answer
You don't get to pick the label. The facts of the working relationship decide it. If you control how, when, and where someone works, and the work is ongoing and core to your product, that person is probably an employee under IRS and Georgia rules. A contractor fits a defined project, done with the contractor's own methods and tools, by someone who also serves other clients. Employees cost roughly 8% on top of salary in required payroll taxes, plus workers' comp once you have 3 or more employees, plus any benefits you choose to offer. Contractors cost no payroll tax, but you need a W-9 up front and a 1099-NEC at year end. Either way, get a signed IP agreement before any code is written. A contractor's code is not automatically yours.

## By stage
- **Pre-revenue founders:**
  - A 1099 contractor costs no payroll tax, but being pre-revenue doesn't change the classification tests. A developer who works your hours, only for you, on your core product is probably an employee under the IRS common-law test and Georgia's UI test (`REFERENCE/INFO/first-hire/p15.pdf` p.14; `REFERENCE/INFO/first-hire/dol224.pdf` p.52).
  - **Now:** get a signed IP assignment before a contractor writes any code ([Copyright Office Circular 30](https://www.copyright.gov/circs/circ30.pdf) pp.2–3). Collect a W-9 before the first payment. Send and file a 1099-NEC by January 31 for anyone you paid $2,000 or more in 2026 ([1099-NEC instructions](https://www.irs.gov/instructions/i1099mec)).
  - **Before fundraising:** clean up IP for any early code written without an assignment, because investors check IP chain of title.
  - **Can wait:** workers' comp isn't required until you have 3 or more employees, but founder-officers and LLC members count toward the 3 ([SBWC](https://sbwc.georgia.gov/employer-information); FIRST_HIRE_CHECKLIST.md).
- **Funded teams hiring 2–10:**
  - Each employee adds required payroll tax of about 7.9% of a $120,000 Georgia salary in 2026, plus workers' comp once you have 3 or more employees (`p15.pdf` pp.1–2, p.44; [GA DOL FAQ](https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance)).
  - Roles that manage others, take equity, or serve as the long-term "founding engineer" point toward employee status.
  - Contract-to-hire works only if the contract phase is project-scoped and time-boxed. At conversion, do full employee onboarding: W-4, G-4, I-9, and PIIA.
  - If you've already misclassified someone, ask a CPA about the VCSP (Form 8952) or Section 530 relief (`p15.pdf` p.15).
  - Out-of-state or overseas workers may fall under a different state's or country's rules (`remote-and-out-of-state-hires`).

## What you need to know

**1. The IRS common-law test: who has the right to control?**
A worker is an employee "if you have the right to control what will be done and how it will be done," even if you never use that right (`REFERENCE/INFO/first-hire/p15.pdf` p.14). The IRS groups the evidence into three categories ([IRS: Independent contractor or employee](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee)):
- **Behavioral:** set hours, required tools, detailed instructions, training on your methods. These point to an employee.
- **Financial:** the worker's own investment and unreimbursed expenses, a chance of profit or loss, other clients, and flat-fee pay. These point to a contractor.
- **Relationship:** benefits, an open-ended engagement, and work that is a key part of your business point to an employee. A contract that calls someone a contractor "is not sufficient" on its own ([IRS FS-2017-09, archived](https://www.irs.gov/newsroom/understanding-employee-vs-contractor-designation)).

No single factor decides the question. Calling someone a contractor doesn't change the answer (`p15.pdf` p.14). For an official ruling, either party can file **Form SS-8**. The IRS says a determination "may take at least six months" ([IRS](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee); [About Form SS-8](https://www.irs.gov/forms-pubs/about-form-ss-8)).

**2. Georgia's test for unemployment insurance (UI) is stricter in one way.**
Georgia says its standard "differs from the standard used by the IRS" (`REFERENCE/INFO/first-hire/dol224.pdf` p.49). Anyone you pay is treated as an employee for UI purposes unless you can prove one of these (O.C.G.A. § 34-8-35(f); `dol224.pdf` p.52):
- **Both** (A) the worker is free from your control or direction, under the contract *and in fact*, **and** (B) the worker is customarily engaged in an independently established trade or business, **or**
- (C) the IRS issued an SS-8 ruling that the worker is not an employee. GA DOL accepts that ruling.

GA DOL says contractors "are not independent just because that is what their employer calls them... or because they sign an 'independent contractor agreement'" (`dol224.pdf` p.51). It lists misclassifying employees as contractors as employer fraud (`dol224.pdf` p.141).

**3. The federal wage-law (FLSA) "economic reality" test is in flux.**
The FLSA governs minimum wage and overtime. A misclassified employee can lose both ([DOL WHD](https://www.dol.gov/agencies/whd/flsa/misclassification)). Status as of 2026-10-25:
- **2024 rule** (29 CFR Part 795, six factors, no factor weighted more) took effect March 11, 2024 ([DOL WHD](https://www.dol.gov/agencies/whd/flsa/misclassification)).
- **May 1, 2025:** Field Assistance Bulletin 2025-1 said the DOL's Wage and Hour Division no longer applies the 2024 rule in its investigations. It uses the 2008 Fact Sheet #13 instead. The 2024 rule "remains in effect for purposes of private litigation" ([Federal Register NPRM, 2026-03962](https://www.govinfo.gov/content/pkg/FR-2026-02-27/html/2026-03962.htm)).
- **Feb 27, 2026 proposed rule:** this would bring back the 2021 test, with two "core" factors: control over the work, and the worker's chance of profit or loss. Comments closed April 28, 2026 (same source). A Federal Register search on 2026-10-25 found **no final rule yet** ([FR search](https://www.federalregister.gov/api/v1/documents.json?conditions[term]=independent%20contractor%20employee%20status&conditions[agencies][]=wage-and-hour-division&order=newest)).

**4. Penalties for getting it wrong.**
- **Federal:** you owe the employer share of FICA and are liable for income tax you didn't withhold. You can't recover the employee share from the worker. Reduced section 3509 rates may apply. They are higher if you never filed 1099s, and they aren't available if you intentionally disregarded the rules (`p15.pdf` p.15). The **Section 530 relief** provision needs a reasonable basis plus consistent 1099 filing. The **Voluntary Classification Settlement Program (VCSP)**, filed on Form 8952, lets you reclassify going forward with partial relief (`p15.pdf` p.15).
- **VCSP specifics (IRS):**
  - *Eligibility:* you must have consistently treated the workers as contractors, including filing all required Forms 1099 for them for the previous three years. You can't currently be under an IRS employment tax audit, or under a DOL or state agency audit about these workers' classification. If the IRS or DOL audited their classification before, you qualify only if you complied with the result and aren't contesting it in court.
  - *Payment:* 10% of the employment tax liability that would have been due on the workers' compensation for the most recent tax year, computed at the reduced section 3509(a) rates. No interest or penalties on that amount, and no employment tax audit of those workers' classification for prior years.
  - *Timing:* file Form 8952 at least 120 days before the date you want to start treating the workers as employees.
  - Source: [IRS VCSP page](https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program) (checked 2026-10-26).
- **Georgia UI:** penalty of $20 or 0.05% of gross payroll, whichever is greater, per month delinquent, plus 1.5% interest per month on the extra tax due (`dol224.pdf` p.146). GA DOL rules also allow a per-employee penalty under O.C.G.A. § 34-8-257 and an investigation fee ([GA DOL rulemaking notice, 06/15/2026](https://dol.georgia.gov/document/gdol-rules/rulemaking-notice-06-15-2026/download) p.7). The per-employee amount was not confirmed.

**5. Cost comparison (example: $120,000 salary, Georgia, 2026)**

| Cost | Employee | Contractor (1099) |
|------|----------|-------------------|
| Employer Social Security, 6.2% up to $184,500 in wages (2026; $192,300 for 2027) | $7,440 | $0 |
| Employer Medicare, 1.45%, no cap | $1,740 | $0 |
| FUTA, 0.6% net on first $7,000 (`p15.pdf` p.44) | $42 | $0 |
| GA SUTA, new employer 2.70% total on first $9,500 ([GA DOL FAQ](https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance)) | $256.50 | $0 |
| Workers' comp, required at 3+ employees, part-time counts ([SBWC](https://sbwc.georgia.gov/employer-information)) | Insurer quote | Not required for true contractors |
| Benefits (health, PTO, 401k) | Your choice. ACA mandate starts at 50+ full-time equivalents (`dol224.pdf` p.31) | None |
| **Required payroll tax total** | **about $9,479 (7.9%)** | **$0. Expect a higher rate, since contractors pay their own self-employment tax and benefits** |

FICA rates and wage base: `p15.pdf` pp.1–2. For 2027, SSA announced a Social Security wage base of $192,300 on Oct 14, 2026 ([SSA](https://www.ssa.gov/oact/cola/cbb.html)). A $120,000 salary is under both the 2026 and 2027 bases, so the employer Social Security cost in this example is $7,440 in either year.

## Steps
1. **Run the employee-vs-contractor decision checklist at the end of these steps.** Write down your reasoning. The IRS expects you to document it ([IRS](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee)).
2. **Sign the IP agreement before work starts.**
   - *Contractor:* use a written **IP assignment** agreement. Software usually isn't one of the nine categories of commissioned work that can be "work made for hire," so the contract must *assign* the rights. A copyright transfer must be in writing and signed ([Copyright Office Circular 30](https://www.copyright.gov/circs/circ30.pdf) pp.2–3; 17 U.S.C. § 204(a)). Add confidentiality terms and a list of any prior inventions the contractor is excluding.
   - *Employee:* code written within the scope of the job is generally work made for hire (Circ. 30 p.2). Still use a **PIIA** (Proprietary Information and Inventions Assignment) agreement to cover patents, inventions, side work, and confidentiality.
3. **Contractor path:** collect **Form W-9** (rev. 03/2024) before the first payment ([IRS](https://www.irs.gov/forms-pubs/about-form-w-9)). Pay on invoices, with no withholding. By **January 31**, send **Form 1099-NEC** to the contractor and file it with the IRS if you paid **$2,000 or more** in 2026 ($600 for 2025 payments). If you file 10 or more information returns of any type in total, you must e-file ([1099-NEC instructions](https://www.irs.gov/instructions/i1099mec); `p15.pdf` p.7). Georgia DOR doesn't need a copy of a 1099-NEC unless it reports Georgia tax withheld. In that case it goes with Form G-1003 (`REFERENCE/INFO/first-hire/2026 Employers_Tax_Guide.pdf` p.7, 19–20).
4. **Employee path:**
   - Register for GA withholding ([GA DOR](https://dor.georgia.gov/taxes/register-new-business-georgia)) and for a GA DOL UI account (file the DOL-1A after the first payroll) ([GA DOL FAQ](https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance)).
   - Collect **Form W-4** ([IRS](https://www.irs.gov/forms-pubs/about-form-w-4)) and **Form G-4** (Rev. 06/03/26, `TSD_Employees_Withholding_Allowance_Certificate_G-4.pdf`).
   - Complete **Form I-9**. The employee fills out Section 1 by the first day of work, and you complete Section 2 within 3 business days (`i-9instr.pdf` p.1). Keep it 3 years after hire or 1 year after termination, whichever is later ([USCIS](https://www.uscis.gov/i-9)).
   - Get a workers' comp policy once you hit 3 employees.
   - You, the founder, manage accounts in the [Georgia Tax Center](https://gtc.dor.ga.gov/_/) and the [GA DOL Employer Portal](https://www.dol.state.ga.us/public/uitax/emplportal/login), the link on GA DOL's Online Services page. An alternate login URL, https://eresponse.gdol.ga.gov/idp/sso/employer/login, also loads.
5. **Unsure? File Form SS-8,** or ask a CPA. If you've already misclassified someone, ask about the VCSP (`p15.pdf` p.15). File Form 8952 at least 120 days before you want to start treating the workers as employees ([IRS VCSP](https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program)).

**Contract-to-hire:** this is a legitimate way to try out a working relationship. The contract phase still has to pass the IRS common-law test, Georgia's UI test, and the FLSA economic-reality test. A "trial" contractor who works your hours, on your roadmap, with your tools, may already be an employee. Keep it project-scoped and time-boxed, with an IP assignment in place from day one. When you convert, start fresh with full employee onboarding (W-4, G-4, I-9, PIIA). *(No official source addresses contract-to-hire specifically. This applies the IRS common-law test and Georgia's UI test.)*

**Decision checklist.** Each "yes" pushes toward an employee:
- [ ] Will you set their hours, location, or tools, or train them on your methods?
- [ ] Is the work ongoing with no defined end, rather than a scoped project?
- [ ] Is it core to your product, like building and maintaining your main codebase?
- [ ] Will they work only for you, with no other clients or business of their own?
- [ ] Will you pay by the hour or salary rather than per deliverable?
- [ ] Will you supply their laptop and software, and reimburse their expenses?
- [ ] Do you want them to manage others, take equity, or be the long-term "founding engineer"?

Two or more "yes" answers: treat this as an employee hire, or talk to a professional before using a 1099.

## Links
| Resource | URL | Why |
|----------|-----|-----|
| IRS: Contractor or employee | https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee | Common-law test, SS-8 |
| IRS Form SS-8 | https://www.irs.gov/forms-pubs/about-form-ss-8 | Official status ruling |
| IRS Pub 15 (2026) | https://www.irs.gov/pub/irs-pdf/p15.pdf | FICA, FUTA, section 3509, relief |
| 1099-MISC/NEC instructions | https://www.irs.gov/instructions/i1099mec | Threshold, deadline, e-file |
| IRS VCSP | https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program | Fixing past misclassification: eligibility, 10% payment, 120-day filing rule |
| DOL: FLSA misclassification | https://www.dol.gov/agencies/whd/flsa/misclassification | Federal wage-law test |
| 2026 DOL proposed rule | https://www.govinfo.gov/content/pkg/FR-2026-02-27/html/2026-03962.htm | Current FLSA status |
| GA DOL Employer Handbook | https://dol.georgia.gov/documents/employer-handbook | GA UI coverage test, penalties |
| GA DOL UI FAQ | https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance | New employer rate, wage base, DOL-1A |
| GA SBWC employer info | https://sbwc.georgia.gov/employer-information | Workers' comp threshold |
| Copyright Office Circ. 30 | https://www.copyright.gov/circs/circ30.pdf | Work made for hire, IP ownership |
| USCIS I-9 | https://www.uscis.gov/i-9 | Current edition, retention |

## Double-check before sending
| Item | Value as of last check | Where to verify | Last verified |
|------|------------------------|-----------------|---------------|
| Social Security rate / wage base | 6.2% each side / $184,500 (2026) | `p15.pdf` pp.1–2; IRS.gov/Pub15 | 2026-10-25 |
| 2027 Social Security wage base | $192,300 (announced by SSA Oct 14, 2026) | https://www.ssa.gov/oact/cola/cbb.html (returns 403 to automated checks; read from the Internet Archive capture of 2026-10-20) | 2026-10-26 |
| Medicare rate | 1.45% each side, no cap | `p15.pdf` p.2 | 2026-10-25 |
| FUTA | 6.0% on first $7,000; 0.6% after the full 5.4% credit | `p15.pdf` p.44; Form 940 instructions | 2026-10-25 |
| FUTA credit reduction states | Georgia is not a credit-reduction state (not on the final 2025 list or the 2026 potential list). The final 2026 list comes after Nov 10, 2026 | https://oui.doleta.gov/unemploy/futa_credit.asp | 2026-10-25 |
| GA SUTA new employer rate | 2.70% total | GA DOL FAQ; `dol224.pdf` p.72; employer's DOL-626 notice | 2026-10-25 |
| GA SUTA split (2.64% contribution + 0.06% admin assessment; assessment ends 12/31/2026) | Per SB 160 text (see GA_EMPLOYER_TAXES.md); GA DOL states a total of 2.70% | SB 160; GA DOL | 2026-10-25 |
| GA taxable wage base | $9,500 | GA DOL FAQ; `dol224.pdf` p.49. Note: one FAQ answer still says $8,500, which is outdated | 2026-10-25 |
| GA UI liability trigger | $1,500 payroll in a quarter, or 1 worker in 20 weeks | `dol224.pdf` p.49; GA DOL FAQ | 2026-10-25 |
| GA misclassification penalties | Late-report penalty + 1.5%/month interest; per-employee penalty under § 34-8-257 (amount not confirmed) | `dol224.pdf` p.146; GA DOL rules 300-2-3-.02 | 2026-10-25 (partial) |
| GA DOL rule amendments (06/15/2026 notice) | Adoption was scheduled for consideration 07/16/2026. Final status not confirmed | https://dol.georgia.gov/ (GDOL Rules) | Not verified |
| Workers' comp threshold | 3+ employees, part-time counts | https://sbwc.georgia.gov/employer-information | 2026-10-25 |
| 1099-NEC threshold | $2,000 (2026 payments); $600 (2025); may be indexed for inflation from 2027 | 1099-MISC/NEC instructions (rev. 12/2026) | 2026-10-25 |
| 1099-NEC deadline | January 31, to the contractor and the IRS | Same | 2026-10-25 |
| E-file threshold | 10 or more information returns in total | Same | 2026-10-25 |
| FLSA contractor rule | 2024 rule on the books; DOL not enforcing it since 05/01/2025; 02/27/2026 proposal not final | Federal Register; DOL WHD | 2026-10-25 |
| Form revisions | W-9 rev. 03/2024; G-4 rev. 06/03/26; I-9 edition 01/20/25; SS-8 rev. 12/2023 (inferred from file label) | IRS, GA DOR, USCIS form pages | 2026-10-25 |
| SS-8 processing time | "At least six months" | IRS contractor page | 2026-10-25 |
| VCSP terms | 10% of one year's employment tax liability at reduced § 3509(a) rates; Form 8952 at least 120 days before the reclassification date; 3 years of 1099s; no current IRS employment tax audit or DOL/state classification audit | https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program | 2026-10-26 |
| GA DOL Employer Portal URL | https://www.dol.state.ga.us/public/uitax/emplportal/login (linked from Online Services); https://eresponse.gdol.ga.gov/idp/sso/employer/login also loads | https://dol.georgia.gov/online-services | 2026-10-26 |
| Which 1099s go to GA DOR with the G-1003 | Only 1099s reporting GA withholding (or qualified overtime or cash tips); 1099-K and 1099-DA always | `2026 Employers_Tax_Guide.pdf` p.7, 20 | 2026-10-26 |

## When to bring in a professional
- **Employment attorney:** you're paying a 1099 developer who works full-time hours, only for you, on your core product. Also talk to one if a worker files an SS-8 or a UI claim, or if GA DOL opens an audit.
- **Corporate/IP attorney:** before any contractor writes code, to draft the IP assignment and the PIIA, and to clean up IP if early code was written without one. This matters before fundraising, because investors check IP chain of title. Also talk to one before offering equity to either type of hire.
- **CPA or payroll provider:** to set up payroll, check your GA rate notice, model the total cost of a hire, and decide about the VCSP or Section 530 relief if you've misclassified someone.
- **Out-of-state or overseas workers:** a different state's or country's rules may apply.

## Related packages
- `FIRST_HIRE_CHECKLIST.md`: the step-by-step hub
- `EXEMPT_VS_NONEXEMPT_PAY_RULES.md`: overtime, minimum wage, pay frequency
- `PAYING_FOUNDERS.md`: draws, salary, S-corp election
- `EQUITY_FOR_EARLY_HIRES.md`: options, profits interests, 83(b), 409A
- `GA_EMPLOYER_TAXES.md`: withholding, FICA, FUTA, GA UI, filing calendar
- `PAYROLL_PEO_AND_BENEFITS.md`: payroll provider vs. PEO, health and retirement benefits
- `REMOTE_AND_OUT_OF_STATE_HIRES.md`: employees in other states and abroad
- `FIRING_AND_OFFBOARDING_GA.md`: terminations, final pay, severance, equity on exit
- `HEADCOUNT_TRIGGERS_AND_COMPLIANCE_CALENDAR.md`: laws by headcount, plus annual deadlines
- `DELAWARE_ENTITY_IN_GEORGIA.md`: foreign registration and costs in both states
- `LOCAL_BUSINESS_LICENSES_METRO_ATLANTA.md`: city and county occupation tax certificates
