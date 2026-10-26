---
id: remote-and-out-of-state-hires
title: "Remote, Out-of-State, and International Hires for a Georgia Startup"
questions: ["Can I hire a developer who lives in another state?", "What do I have to do to hire someone remote in Texas, California, or New York?", "Can I hire a developer in another country?", "Do I withhold Georgia tax for a remote employee who lives in another state?", "Which state's unemployment tax applies to a remote employee?", "How do I do the I-9 for a remote hire I never meet in person?", "Should I use an Employer of Record (EOR) or pay an overseas developer as a contractor?", "Can I hire someone on OPT or sponsor an H-1B?"]
tags: [remote-work, multi-state-payroll, state-withholding, state-unemployment-insurance, nexus, pay-transparency, form-i-9, e-verify, employer-of-record, international-contractors, form-w-8ben, ofac, export-controls, work-visas]
jurisdiction: [US-federal, GA, US-other-states, international]
audience: [pre-revenue, funded-2-10]
related: [employee-vs-contractor, first-hire-checklist, ga-employer-taxes, exempt-vs-nonexempt-pay-rules, delaware-entity-in-georgia, headcount-triggers-and-compliance-calendar, equity-for-early-hires]
last_verified: 2026-10-25
status: active
---

# Remote, Out-of-State, and International Hires for a Georgia Startup

> General information for founders, not legal or tax advice. Confirm specifics with a CPA or attorney before acting.

## Short answer
Yes. A Georgia startup can hire a remote employee in another state, but the company then becomes an employer in **that** state too. You register there for withholding (if the state has an income tax) and unemployment insurance (UI), follow its wage, leave, and notice laws, and extend workers' comp to it. The hire may also mean registering the company there and filing state income or franchise tax. A multi-state payroll provider or PEO handles most of the registrations. For someone living and working abroad, you either pay them as a contractor (collect a W-8BEN; no 1099) or hire them through an Employer of Record (EOR). A foreign national working **in** the US needs work authorization, so talk to an immigration attorney.

## By stage
- **Pre-revenue founders:**
  - **Texas is the lightest of the common asks.** It has no personal income tax ([Tex. Const. art. 8, § 24-a](https://statutes.capitol.texas.gov/docviewer/?docName=CN.8.24-a.htm)), and workers' comp is optional for most private employers ([TDI](https://www.tdi.texas.gov/wc/employer/index.html)). You still register for Texas UI ([TWC](https://www.twc.texas.gov/programs/unemployment-tax/determine-tax-account)).
  - **One remote hire means a second state** of registrations, UI tax, and insurance. Price it in.
  - **Overseas developers:** at minimum, a contract with an IP assignment, a W-8BEN, and an OFAC screen.
  - **Can wait:** an EOR, until the overseas person is effectively full-time and long-term.
- **Funded teams hiring 2–10:**
  - Use a payroll provider that registers and files in each new state.
  - Post salary ranges on remote job ads by default. New York's pay-transparency law applies at 4 employees ([NY DOL](https://dol.ny.gov/pay-transparency)), and California's and Washington's at 15 ([Cal. Lab. Code § 432.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=432.3.); [WA L&I](https://lni.wa.gov/workers-rights/wages/equal-pay-opportunities-act/equal-pay-and-opportunities-act-qa)).
  - Consider enrolling in E-Verify. It unlocks the remote I-9 video check ([USCIS](https://www.uscis.gov/i-9-central/remote-examination-of-documents)), and it is required to hire STEM OPT graduates ([USCIS](https://www.uscis.gov/working-in-the-united-states/students-and-exchange-visitors/optional-practical-training-extension-for-stem-students-stem-opt)).
  - Count remote staff toward headcount thresholds (`headcount-triggers-and-compliance-calendar`). Other states add their own thresholds.

## What you need to know

**1. Withholding for a GA employer's remote employee follows the work state.** Georgia requires withholding from nonresidents only "for services performed in Georgia" (`REFERENCE/INFO/first-hire/2026 Employers_Tax_Guide.pdf` p.9). A nonresident who never works in Georgia gets no GA withholding. You withhold for their work state instead, if it has an income tax. **Visits count:** GA withholding applies to a nonresident once more than 5% of their wages, or more than $5,000, is attributable to Georgia (same guide p.10, p.15).
- **Reciprocity:** the GA DOR guide mentions no reciprocal agreements, and a secondary payroll source says Georgia has none ([Paylocity, secondary](https://www.paylocity.com/resources/tax-compliance/tax-facts/georgia/)). This is **not confirmed on an official source.**
- **"Convenience of the employer":** a few states tax work-from-home days as if they were worked at the employee's assigned office in that state. New York does this unless the home office is a "bona fide employer office" ([NY IT-203 instructions](https://www.tax.ny.gov/forms/current-forms/it/it203i.htm)). Secondary sources add DE, NE, and PA, with CT and NJ applying the rule only in limited cases ([NJ Treasury](https://nj.gov/treasury/taxation/conveniencerulefaq.shtml); [SmartAsset, secondary](https://smartasset.com/taxes/convenience-of-the-employer-rule)). It matters once you have an office in one of those states.

**2. A remote employee can create company-level tax and registration duties.** The Multistate Tax Commission says a regularly telecommuting employee isn't protected by the federal P.L. 86-272 safe harbor, which covers only soliciting orders for tangible goods ([MTC Statement](https://www.mtc.gov/wp-content/uploads/2023/04/025-MTC-Statement-on-PL-86-272.pdf)). A SaaS or services startup should expect state income or franchise tax filings. Texas franchise tax, for example, reaches entities "doing business in Texas," with a $2,650,000 no-tax-due threshold for 2026–2027 reports ([Texas Comptroller](https://comptroller.texas.gov/taxes/franchise/)). Each state also sets its own foreign-entity registration test. Georgia's test is in `delaware-entity-in-georgia`; we did not verify other states' tests.

**3. Unemployment insurance uses a four-factor test.** Georgia applies four tests, in this order (`REFERENCE/INFO/first-hire/dol224.pdf` p.53):
1. **Localization:** the state where all the work is done, ignoring incidental work elsewhere.
2. **Base of operations.**
3. **Place of direction and control.**
4. **Residence.**

A developer working entirely from home in Texas is localized in Texas, so you pay Texas UI on their wages, not Georgia UI. FUTA works the same in every state (`ga-employer-taxes`).

**4. The work state's employment laws apply.** The FLSA doesn't override a state's higher minimum wage or stricter overtime rules (29 U.S.C. § 218(a); `exempt-vs-nonexempt-pay-rules`). The employee's state also sets its own paid sick leave, pay frequency, final-pay deadline, notices, and posters. Federal law sets no final-pay deadline, but "some states... may require immediate payment" ([DOL](https://www.dol.gov/general/topic/wages/lastpaycheck)).
- **Pay transparency:** several states require a pay range in job postings, including remote postings. Colorado's law covers any employer with one Colorado employee, even if the posting excludes Coloradans. An out-of-state employer with fewer than 15 fully remote Colorado employees gets a carve-out until July 1, 2029 ([CDLE INFO #9A](https://cdle.colorado.gov/sites/cdle/files/INFO%20%239A%20Transparency%20in%20Pay%20and%20Job%20Opportunities%20The%20Colorado%20EPEWA%20Part%202%205.29.24%20%5Baccessible%5D.pdf)). NY (4+), CA (15+), WA (15+), and other states and cities also have these laws.

**5. Workers' comp must cover the other state.** A Georgia policy doesn't automatically satisfy another state's law. New York requires a full NY policy, with NY listed in "Item 3A," for an out-of-state employer whose employee works in NY more than briefly ([NY WCB](https://www.wcb.ny.gov/content/main/coverage-required-wc.jsp)). NY also requires disability and Paid Family Leave coverage once a worker is localized in NY on 30 days in a calendar year ([NY PFL](https://paidfamilyleave.ny.gov/out-state-employers)). In Texas, workers' comp is optional, but an employer without it must report that to the state ([TDI](https://www.tdi.texas.gov/wc/employer/index.html)).

**6. You can do the I-9 for a remote hire in one of two ways.**
- **Authorized representative:** anyone you designate (a notary can serve, acting as your agent rather than as a notary) examines the documents in person and completes Section 2. You stay liable for their errors (`REFERENCE/INFO/first-hire/i-9instr.pdf` p.1, p.4; [USCIS](https://www.uscis.gov/i-9-central/completing-form-i-9/completing-section-2-employer-review-and-attestation)).
- **DHS alternative procedure:** available only to employers enrolled in E-Verify and in good standing. The employee sends copies, then shows the same documents on a live video call. You keep the copies and check the "alternative procedure" box. Offer it consistently at a hiring site; limiting it to remote hires is allowed if not discriminatory ([USCIS](https://www.uscis.gov/i-9-central/remote-examination-of-documents), updated 09/26/2025).

**7. Payroll providers, PEOs, and new-hire reports.** A multi-state payroll provider registers you and files in each state. A PEO also becomes your co-employer and often supplies workers' comp and benefits. You still owe any tax they fail to pay (`ga-employer-taxes`). Exception: for wages paid by an IRS-certified PEO (CPEO), the CPEO is solely liable for federal employment taxes (`p15.pdf` p.4; see `payroll-peo-and-benefits`). New-hire reports go to the employee's work state. A multistate employer can instead register with HHS and send all reports to one state ([ACF](https://acf.gov/css/employers/employer-responsibilities/new-hire-reporting)).

**8. Contractors in other states face stricter tests in some states.** California's ABC test (AB5) treats a worker as an employee unless (A) they are free from your control, (B) the work is outside the usual course of your business, **and** (C) they run an independent business ([CA Labor Agency](https://www.labor.ca.gov/employmentstatus/abctest/)). Prong B rules out most contract developers who build your core product. The federal and GA tests are in `employee-vs-contractor`.

**9. International hires: contractor or Employer of Record.**
- **Contractor:** simple and cheap, but local law decides whether the person is really an employee ([GOV.UK example](https://www.gov.uk/employment-status)).
- **EOR:** a provider with a local entity employs the person, runs local payroll and benefits, and bills you. Examples (not endorsements): Deel, Remote, Oyster, Velocity Global.
- **Permanent establishment (PE):** under treaties based on the OECD Model, a person who habitually concludes contracts for you abroad can create a taxable presence there ([OECD Model, Art. 5](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/06/model-tax-convention-on-income-and-on-capital-2025-full-version_4fd97b89/db32e18b-en.pdf)). Sales roles carry more PE risk than engineering roles.
- **IP assignment:** some countries limit how inventions can be assigned or keep "moral rights" with the author, so have local counsel review the clause. This is **general practice, not verified against any country's law.**
- **US tax forms:** collect **Form W-8BEN** from an individual, or W-8BEN-E from an entity. The payee gives it to you, and you keep it on file; it doesn't go to the IRS ([IRS](https://www.irs.gov/forms-pubs/about-form-w-8-ben)). Pay is sourced where the work is done. Pay to a nonresident alien for services outside the US is "not subject to withholding," and a W-8BEN can establish exemption from Form 1099 reporting ([IRS Pub 515](https://www.irs.gov/publications/p515)). Our reading: a non-US person working entirely abroad gets no 1099-NEC and no 1042-S. Work done on US visits is US-source.

**10. Run sanctions and export checks.** All US persons, including US companies, must comply with OFAC sanctions ([OFAC FAQs](https://ofac.treasury.gov/faqs/all-faqs)). Screen each foreign contractor with [Sanctions List Search](https://sanctionssearch.ofac.treas.gov/), and check that their country isn't sanctioned. Sharing controlled technology or source code with a foreign person, even inside the US, can be a "deemed export" ([BIS](https://www.bis.gov/learn-support/deemed-exports/what-deemed-export)). Check this if your product involves encryption or is defense-adjacent.

**11. Foreign nationals working in the US need their own work authorization.**
- **H-1B:** 65,000 visas a year, plus 20,000 for holders of US master's degrees, with registration in March ([USCIS](https://www.uscis.gov/working-in-the-united-states/h-1b-specialty-occupations)). Selection has been wage-weighted since FY 2027 ([USCIS](https://www.uscis.gov/newsroom/news-releases/dhs-changes-process-for-awarding-h-1b-work-visas-to-better-protect-american-workers)). The $100,000 payment for certain petitions is in litigation ([USCIS](https://www.uscis.gov/newsroom/alerts/presidential-proclamation-on-restriction-on-entry-of-certain-nonimmigrant-workers)).
- **O-1:** for extraordinary ability, filed by a US employer or agent ([USCIS](https://www.uscis.gov/working-in-the-united-states/temporary-workers/o-1-visa-individuals-with-extraordinary-ability-or-achievement)).
- **OPT and STEM OPT:** STEM OPT is a 24-month extension for F-1 graduates in STEM fields. The employer must be enrolled in E-Verify and must sign Form I-983 ([USCIS](https://www.uscis.gov/working-in-the-united-states/students-and-exchange-visitors/optional-practical-training-extension-for-stem-students-stem-opt)).

For any of these, use an immigration attorney.

## Steps
1. **Confirm the worker is an employee** under `employee-vs-contractor` and the state's own test, then work through the state-by-state lookup checklist in this section.
2. **Register in the work state before its first payroll**, for withholding (if it has an income tax) and UI. California: EDD within 15 days of paying more than $100 in a quarter ([EDD](https://edd.ca.gov/en/payroll_Taxes/Am_I_Required_to_Register_as_an_Employer)). Texas: TWC within 10 days of becoming liable ([TWC](https://www.twc.texas.gov/programs/unemployment-tax/determine-tax-account)). New York: review the [NY withholding rules](https://www.tax.ny.gov/bus/wt/whtax_require.htm) with a CPA. *You get:* state account numbers.
3. **Ask a CPA about nexus**, Secretary of State registration, and franchise or income tax in that state.
4. **Add the state to workers' comp.** In NY, also get disability and PFL coverage. *You get:* a policy that names the state.
5. **Complete the I-9 within 3 business days** of the start date, using a representative or the E-Verify video procedure.
6. **File the new-hire report** in the work state, or in your designated state.
7. **Abroad:** screen the person with OFAC, collect a W-8BEN, and sign a contract with a locally reviewed IP assignment. Or get EOR quotes.

### State-by-state lookup checklist
- [ ] Income tax withholding registration and any local income tax (Texas has none)
- [ ] UI registration trigger, wage base, and new-employer rate
- [ ] State disability or paid family leave programs
- [ ] Foreign-entity registration and income or franchise tax nexus
- [ ] Workers' comp rules for out-of-state employers
- [ ] Minimum wage ([DOL table](https://www.dol.gov/agencies/whd/minimum-wage/state)) and overtime
- [ ] Paid sick leave and other leave, at state and city level
- [ ] Pay frequency ([DOL table](https://www.dol.gov/agencies/whd/state/payday)) and final-pay deadline
- [ ] Hiring notices, pay-stub contents, and posters (including electronic delivery)
- [ ] Pay transparency and salary-history bans
- [ ] Contractor test (ABC or other)
- [ ] Non-compete rules
- [ ] New-hire reporting agency
- [ ] Headcount thresholds for state laws

Start with the [DOL list of state labor offices](https://www.dol.gov/agencies/whd/state/contacts).

## Links
| Resource | URL | Why |
|----------|-----|-----|
| GA DOR Employer's Tax Guide 2026 | https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-june-2026/download | Nonresident withholding (pp.9–10, 15–16) |
| GA DOL Employer Handbook | https://dol.georgia.gov/documents/employer-handbook | Four-factor UI test (p.53) |
| NY IT-203 instructions | https://www.tax.ny.gov/forms/current-forms/it/it203i.htm | Convenience of the employer, bona fide employer office |
| NY DTF withholding requirements | https://www.tax.ny.gov/bus/wt/whtax_require.htm | Who must withhold NY tax |
| MTC Statement on P.L. 86-272 | https://www.mtc.gov/wp-content/uploads/2023/04/025-MTC-Statement-on-PL-86-272.pdf | Remote employees and income tax nexus |
| USCIS remote examination | https://www.uscis.gov/i-9-central/remote-examination-of-documents | Alternative I-9 procedure |
| E-Verify | https://www.e-verify.gov/ | Enrollment (founder portal) |
| ACF new-hire reporting | https://acf.gov/css/employers/employer-responsibilities/new-hire-reporting | Multistate employer option |
| DOL state labor offices | https://www.dol.gov/agencies/whd/state/contacts | Starting point for the state checklist |
| CA ABC test | https://www.labor.ca.gov/employmentstatus/abctest/ | California contractor test |
| CA EDD registration | https://edd.ca.gov/en/payroll_Taxes/Am_I_Required_to_Register_as_an_Employer | CA employer registration |
| TWC UI account | https://www.twc.texas.gov/programs/unemployment-tax/determine-tax-account | TX UI liability |
| TDI workers' comp | https://www.tdi.texas.gov/wc/employer/index.html | TX optional coverage |
| NY WCB coverage | https://www.wcb.ny.gov/content/main/coverage-required-wc.jsp | NY workers' comp for out-of-state employers |
| NY PFL out-of-state employers | https://paidfamilyleave.ny.gov/out-state-employers | NY disability and PFL |
| CDLE INFO #9A | https://cdle.colorado.gov/sites/cdle/files/INFO%20%239A%20Transparency%20in%20Pay%20and%20Job%20Opportunities%20The%20Colorado%20EPEWA%20Part%202%205.29.24%20%5Baccessible%5D.pdf | Colorado pay transparency, remote jobs |
| IRS Pub 515 | https://www.irs.gov/publications/p515 | Foreign payees, sourcing, W-8 |
| IRS Form W-8BEN | https://www.irs.gov/forms-pubs/about-form-w-8-ben | Foreign contractor certificate |
| OFAC Sanctions List Search | https://sanctionssearch.ofac.treas.gov/ | Screening |
| BIS deemed exports | https://www.bis.gov/learn-support/deemed-exports/what-deemed-export | Export controls on tech and source code |
| USCIS H-1B | https://www.uscis.gov/working-in-the-united-states/h-1b-specialty-occupations | H-1B basics, $100,000 payment status |

## Double-check before sending
| Item | Value as of last check | Where to verify | Last verified |
|------|------------------------|-----------------|---------------|
| GA nonresident withholding trigger | More than 5% of wages or more than $5,000 attributable to GA | 2026 DOR guide pp.10, 15 | 2026-10-25 |
| GA reciprocal agreements | None found. The DOR guide mentions none; a secondary source says none | GA DOR; [Paylocity, secondary](https://www.paylocity.com/resources/tax-compliance/tax-facts/georgia/) | **Not verified on an official source** |
| Convenience-of-the-employer states | NY confirmed. DE, NE, and PA, plus CT and NJ in limited cases, per secondary sources (they conflict on AR, MA, AL, OR) | Each state's revenue department; NJ Treasury FAQ | 2026-10-25 (NY only) |
| GA four-factor UI test | Localization, base of operations, direction and control, residence | `dol224.pdf` p.53 (R-11-24) | 2026-10-25 |
| Remote I-9 alternative procedure | Open to E-Verify employers in good standing; USCIS page updated 09/26/2025 | https://www.uscis.gov/i-9-central/remote-examination-of-documents | 2026-10-25 |
| I-9 edition | 01/20/25 | https://www.uscis.gov/i-9 (per `first-hire-checklist`) | 2026-10-25 |
| W-8BEN revision | October 2021 | https://www.irs.gov/forms-pubs/about-form-w-8-ben | 2026-10-25 |
| No 1099-NEC or 1042-S for a non-US person working fully abroad | Our reading of Pub 515 (2026; page reviewed 30-Apr-2026). The IRS doesn't say it in one sentence | https://www.irs.gov/publications/p515 | 2026-10-25 |
| 1099-NEC threshold (US contractors) | $2,000 (2026 payments) | `employee-vs-contractor`; i1099mec (rev. 12/2026) | 2026-10-25 |
| Pay transparency coverage | CO: 1+ CO employee (remote carve-out under 15 until 2029-07-01). NY: 4+. CA: 15+. WA: 15+ | CDLE INFO #9A (5.29.24); NY DOL; Cal. Lab. Code § 432.3; WA L&I | 2026-10-25 (CO and WA from official pages via search excerpts, not fetched in full) |
| CA EDD registration | Within 15 days after paying more than $100 in a quarter | EDD | 2026-10-25 |
| TX UI liability and registration | $1,500 in a quarter or 1 employee in 20 weeks; register within 10 days | TWC | 2026-10-25 |
| TX franchise no-tax-due threshold | $2,650,000 (2026–2027 reports) | Texas Comptroller | 2026-10-25 |
| TX workers' comp | Optional for most private employers; nonsubscribers report to DWC | TDI (page updated 6/8/2026) | 2026-10-25 |
| NY workers' comp for out-of-state employers | Full NY policy (Item 3A) if, among other triggers, employees work in NY 40+ hours a week for more than 2 straight weeks, or 25+ employee-days in the prior year; Item 3C for brief visits | NY WCB | 2026-10-25 |
| NY disability and PFL trigger | A worker localized in NY on 30 days in a calendar year | NY PFL | 2026-10-25 |
| GA pay frequency | Semimonthly | DOL payday table (revised 2023-01-01) | 2026-10-25 |
| H-1B $100,000 payment | Guidance vacated June 8, 2026; stay denied July 24, 2026; DHS says it will collect if the order is lifted. A Sept 2026 White House fact sheet says the proclamation was renewed | USCIS alert (page dated 06/15/2026); whitehouse.gov | 2026-10-25 (renewal seen in search excerpt only; fluid) |
| H-1B cap and selection | 65,000 + 20,000; wage-weighted from FY 2027 | USCIS H-1B page (09/21/2026); USCIS release (12/23/2025) | 2026-10-25 |
| STEM OPT | 24 months; E-Verify and Form I-983 required | USCIS (page updated 01/30/2026) | 2026-10-25 |
| EOR provider names | Examples only | Provider sites | Not verified (not endorsements) |
| IP assignment rules abroad | Vary by country | Local counsel | **Not verified** |

## When to bring in a professional
- **CPA or multi-state payroll provider:** before the first payroll in any new state, especially NY, CA, or a convenience-of-the-employer state. Also to decide nexus and franchise tax.
- **Employment attorney licensed in the work state:** offer letters, state notices, leave policies, non-competes, and ABC-test contractors.
- **Insurance agent:** adding states to workers' comp, plus NY disability and PFL.
- **International counsel or an EOR:** before engaging anyone full-time abroad, for PE risk, local classification, and IP assignment.
- **Immigration attorney:** any H-1B, O-1, OPT, or STEM OPT hire.
- **Export-control counsel:** encryption, defense-adjacent, or dual-use technology shared with foreign persons.

## Related packages
- `FIRST_HIRE_CHECKLIST.md`: the step-by-step hub
- `EMPLOYEE_VS_CONTRACTOR.md`: classifying the worker
- `EXEMPT_VS_NONEXEMPT_PAY_RULES.md`: overtime, minimum wage, pay frequency
- `PAYING_FOUNDERS.md`: draws, salary, S-corp election
- `EQUITY_FOR_EARLY_HIRES.md`: options, profits interests, 83(b), 409A
- `GA_EMPLOYER_TAXES.md`: withholding, FICA, FUTA, GA UI, filing calendar
- `PAYROLL_PEO_AND_BENEFITS.md`: payroll provider vs. PEO, health and retirement benefits
- `FIRING_AND_OFFBOARDING_GA.md`: terminations, final pay, severance, equity on exit
- `HEADCOUNT_TRIGGERS_AND_COMPLIANCE_CALENDAR.md`: laws by headcount, plus annual deadlines
- `DELAWARE_ENTITY_IN_GEORGIA.md`: foreign registration and costs in both states
- `LOCAL_BUSINESS_LICENSES_METRO_ATLANTA.md`: city and county occupation tax certificates
