---
id: exempt-vs-nonexempt-pay-rules
title: "Exempt vs. Non-Exempt and Basic Pay Rules for Your First Technical Hire in Georgia"
questions: ["Do I have to pay my developer overtime?", "Can I pay a salary below X and still not pay overtime?", "Can I pay my first hire in equity instead of cash?", "Can I defer or accrue salary until we raise?", "Can I have unpaid interns or volunteers?", "How often do I have to run payroll in Georgia?", "When is a final paycheck due in Georgia?"]
jurisdiction: [US-federal, GA]
tags: [flsa, overtime, minimum-wage, pay-frequency, internships, wage-and-hour]
audience: [pre-revenue, funded-2-10]
related: [employee-vs-contractor, first-hire-checklist, equity-for-early-hires, remote-and-out-of-state-hires, firing-and-offboarding-ga]
last_verified: 2026-10-25
status: active
---

# Exempt vs. Non-Exempt and Basic Pay Rules for Your First Technical Hire in Georgia

> General information for founders, not legal or tax advice. Confirm specifics with a CPA or attorney before acting.

## Short answer
Every employee is owed overtime (time-and-a-half over 40 hours in a workweek) unless they pass **both** a pay test and a duties test. The job title doesn't decide it. For a salaried developer, the pay test is at least **$684/week ($35,568/year)** in salary. A computer employee paid hourly can be exempt at **$27.63/hour or more**. The developer's main job must also be real software or systems work: designing, building, testing, or analyzing. Junior trainees, help-desk staff, and hardware repair roles often fail the duties test. Georgia adds no overtime rules of its own. In practice, the minimum wage is the federal **$7.25/hour**. Equity can't replace cash wages, and "accrued" salary is still owed. Unpaid internships at a for-profit startup are allowed only in narrow cases, and unpaid "volunteering" for a for-profit isn't allowed at all. Pay at least semimonthly.

## By stage
- **Pre-revenue founders:**
  - Your pay rules come from the job and the cash you actually pay. Being pre-revenue doesn't change them.
  - The FLSA's $500,000 sales threshold covers only *enterprise* coverage. A remote developer who works over the internet with people in other states is very likely covered *individually* anyway ([WHD Fact Sheet #14](https://www.dol.gov/agencies/whd/fact-sheets/14-flsa-coverage)).
  - If you can't afford at least $684/week in salary, the hire is non-exempt. Track hours, and pay at least $7.25/hour plus overtime.
  - Don't pay in "sweat equity" alone, and don't let unpaid salary pile up.
  - Founders who own at least 20% and actively manage are exempt with no salary minimum (29 CFR 541.101). That rule doesn't extend to your first hire.
- **Funded teams hiring 2–10:**
  - Classify each role by its duties, and write the classification into the offer letter (FIRST_HIRE_CHECKLIST.md, step 9).
  - Expect non-exempt roles as you grow: QA testers working from scripts, IT and help desk, ops and office staff, and junior or trainee devs. Set up time tracking for them.
  - Adopt a written policy on salary deductions. It protects the exemption if a mistake slips through (29 CFR 541.603(d)).
  - Remote hires outside Georgia follow their own state's rules, which are often stricter (see "Remote workers" below).

## What you need to know

**1. Exempt means passing three tests: salary level, salary basis, and duties.**
Job titles never decide it (29 CFR 541.2; `REFERENCE/INFO/first-hire/dol224.pdf` p.19).
- **Salary level.** At least **$684/week**. That equals $1,368 biweekly, $1,482 semimonthly, or $2,964 monthly ([29 CFR 541.600](https://www.ecfr.gov/current/title-29/section-541.600)). Nondiscretionary bonuses and commissions paid at least annually can cover up to 10% of it (541.602(a)(3)).
- **Status of the higher thresholds.** The 2024 rule raised the threshold to $844 and then $1,128. Two federal courts vacated it in Nov 2024 (Texas v. DOL; Flint Avenue v. DOL). The Fifth Circuit dismissed the appeals on May 5 and 7, 2026. On May 15, 2026, DOL restored the 2019 text with a technical rule ([91 FR 27833](https://www.federalregister.gov/documents/2026/05/15/2026-09839/defining-and-delimiting-the-exemptions-for-executive-administrative-professional-outside-sales-and)). DOL's [salary-levels page](https://www.dol.gov/agencies/whd/overtime/salary-levels) lists $684/week. As of 2026-10-25, a Federal Register search found no new proposed rule on Part 541.
- **Outdated handbook figures.** The GA DOL Handbook (R-11-24) still shows the pre-2019 figures of $455/week and $100,000 HCE (`dol224.pdf` pp.15, 19–21). Don't quote them.

**2. The duties tests, in plain terms.** "Primary duty" means the main or most important duty. Spending more than 50% of time on exempt work is a guide, not a rule (541.700).
- **Executive:** manages the company or a department, regularly directs **2 or more** employees, and has real hire/fire input (541.100).
- **Administrative:** does office work tied to running the business, and exercises discretion and independent judgment on matters that matter (541.200).
- **Learned professional:** the work requires advanced knowledge in a field of science or learning, usually gained through a prolonged course of specialized instruction (541.300–.301). Many self-taught developers don't fit here, so use the computer exemption instead.

**3. The computer employee exemption (29 CFR 541.400).** It requires $684/week on salary, **or $27.63/hour or more** if paid hourly (FLSA §13(a)(17)). The primary duty must be one of these:
1. Systems analysis, including consulting with users to set hardware, software, or system specifications.
2. Designing, developing, documenting, analyzing, creating, testing, or modifying systems or programs based on user or system specifications.
3. The same kinds of work on operating-system programs.
4. A combination of these that requires the same skill level.

These are *not* exempt under 541.400:
- Hardware manufacture or repair, and people who merely *use* software heavily, such as CAD drafters (541.401).
- Trainees who aren't yet doing the exempt duties (541.705).
- *Inference, not stated in the regulation:* help-desk work, password resets, device setup, and QA that runs other people's test scripts usually don't look like "design, development... or testing of systems... based on specifications." Treat these roles as non-exempt unless counsel says otherwise. A lead developer who manages 2 or more developers can qualify as an executive (541.402).
- WHD Fact Sheet #17E summarizes the exemption ([FS17E](https://www.dol.gov/agencies/whd/fact-sheets/17e-overtime-computer), Aug 2024).

**4. Highly compensated employee (HCE).** Someone earning **$107,432 or more** in total annual compensation, including at least $684/week in salary, is exempt if they regularly perform *one* exempt duty (541.601). Pay for a partial year is prorated.

**5. Overtime and minimum wage.**
- **Overtime:** non-exempt employees get at least 1.5× their regular rate for hours over 40 in a fixed 168-hour workweek. No overtime is owed for weekends or holidays as such (`dol224.pdf` p.15). You can't average hours across two weeks ([DOL Overtime](https://www.dol.gov/agencies/whd/overtime)).
- **No Georgia overtime law.** We found no Georgia daily or weekly overtime statute. GA DOL applies the FLSA rules on hours (`dol224.pdf` p.15).
- **Minimum wage:** the federal rate is $7.25. Georgia's $5.15 (O.C.G.A. § 34-4-3) doesn't apply to employment covered by the FLSA, or to employers with 5 or fewer employees or $40,000 or less in sales ([DOL state table](https://www.dol.gov/agencies/whd/minimum-wage/state), updated July 1, 2026; [FindLaw § 34-4-3](https://codes.findlaw.com/ga/title-34-labor-and-industrial-relations/ga-code-sect-34-4-3/), secondary). GA DOL says employers that comply with federal law also comply with Georgia law (`dol224.pdf` p.14).

**6. Salary-basis rules: when you may dock an exempt salary.** Pay the full salary for any week the person does *any* work. You can't dock pay because work was slow (541.602(a)). Allowed deductions (541.602(b)): full-day personal absences; full-day sick absences under a bona fide sick-pay or disability plan; offsets for jury, witness, or military pay; penalties for major safety-rule violations; full-day disciplinary suspensions under a written policy; a prorated first or last week; and unpaid FMLA leave. Partial-day docking is *not* allowed. A pattern of improper deductions can cost the exemption for everyone in the same job under the same manager. A written policy with a complaint process, plus reimbursing any mistakes, preserves it (541.603).

**7. Recordkeeping.** For non-exempt staff, keep: name, SSN, address, birth date if under 19, sex, occupation; when the workweek starts; hours worked each day and week; pay basis and regular rate; straight-time and overtime earnings; additions and deductions; total wages, pay date, and period covered ([FS21](https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping); 29 CFR 516.2). Keep payroll records **3 years** and time cards **2 years** (516.5–.6). For exempt staff you need the same basics, minus the hours and overtime fields, plus the basis of pay (516.3).

**8. Georgia pay frequency, method, and final pay.**
- **Frequency.** O.C.G.A. § 34-7-2 covers "every person, firm, or corporation" employing wageworkers in "manual, mechanical, or clerical labor." It excludes farming, sawmill, and turpentine businesses, and officials or department heads employed by the month or year at stipulated salaries. It requires pay dates that split the month into at least two equal periods ([FindLaw, current as of 3/28/2024](https://codes.findlaw.com/ga/title-34-labor-and-industrial-relations/ga-code-sect-34-7-2/), secondary).
  - GA DOL says all other employees "must be paid on a semi-monthly or more frequent basis" (`dol224.pdf` p.15). It mis-cites the statute as "§ 7-234-7-2."
  - *Practical rule:* run payroll semimonthly, biweekly, or weekly. Don't pay a first developer monthly, because it isn't settled whether a non-manager developer falls under the salaried-head exclusion.
- **Method.** Pay by cash, check, or direct deposit with the employee's consent. Payroll cards are also allowed. Each payment must cover the full net wages for the period (`dol224.pdf` p.16; § 34-7-2).
- **Final pay.** Federal law doesn't require immediate final pay ([DOL](https://www.dol.gov/general/topic/wages/lastpaycheck)). We found no general Georgia final-paycheck statute. Pay on the next regular payday, which is the common practice (secondary sources only). You *must* give a Separation Notice (DOL-800) on the last day, or mail it within 3 days (`dol224.pdf` p.92).

**9. Equity, deferred pay, and accrued salary.**
- **Equity isn't wages.** Minimum wage and overtime must be paid "in cash or negotiable instrument payable at par" ([29 CFR 531.27](https://www.law.cornell.edu/cfr/text/29/531.27)), "free and clear" (531.35). Options and stock don't count toward the $7.25 minimum or toward overtime.
- *Inference:* equity also can't make up the $684/week salary. Salary basis means a predetermined amount paid each pay period (541.602), and only bonuses and commissions can count toward the level, up to 10% of it.
- **"We'll pay you when we raise" is risky.** Wages are due on the regular payday, and overtime by the next payday at the latest (29 CFR 778.106). Accrued salary is an unpaid wage claim from day one. If the salary isn't actually paid each period, the exemption fails, and minimum wage and overtime are owed for every hour.
- **Personal liability.** The FLSA "employer" includes any person acting in the employer's interest (29 U.S.C. § 203(d)), so founders can be named personally.
- **Tax rules for deferral.** Deferral arrangements can trigger the 409A rules on deferred compensation (see EQUITY_FOR_EARLY_HIRES.md).
- **Safe pattern:** pay at least the legal minimum in cash, then add equity on top.

**10. Unpaid interns and volunteers.**
- **Interns.** At a for-profit, an intern can go unpaid only if the *intern* is the "primary beneficiary" ([Fact Sheet #71](https://www.dol.gov/agencies/whd/fact-sheets/71-flsa-internships), Jan 2018). The seven factors: a clear understanding of no pay; school-like training; a tie to coursework or credit; fitting the academic calendar; a duration limited to real learning; work that complements rather than displaces paid staff; and no promised job at the end.
- **The handbook's intern test is outdated.** The GA DOL Handbook still prints the older six-factor test (`dol224.pdf` p.22). Use FS71 instead.
- **Volunteers.** DOL says: "employees may not volunteer services to for-profit private sector employers" ([DOL elaws](https://webapps.dol.gov/elaws/whd/flsa/docs/volunteers.asp)).
- *Rule of thumb:* an intern who ships production code is an employee. Pay at least minimum wage plus overtime.

**11. Remote workers in other states.** The FLSA doesn't excuse you from a state's higher minimum wage or shorter workweek (29 U.S.C. § 218(a)). Generally, the law of the state where the employee works applies. Many states have higher salary thresholds, daily overtime, or final-pay deadlines. A dedicated package is planned (★ in QUESTION_BANK.md). Until it exists, send these cases to counsel.

**12. Misclassification consequences.**
- **Back pay plus liquidated damages.** You owe unpaid minimum wage and overtime plus an **equal amount** as liquidated damages, along with the employee's attorney's fees (29 U.S.C. § 216(b)). A court may reduce the damages if you acted in good faith with reasonable grounds (§ 260).
- **Lookback.** Claims reach back **2 years**, or **3 years** for willful violations (§ 255(a)).
- **Civil penalties.** Repeated or willful violations carry penalties of up to **$2,515** per violation ([29 CFR 578.3](https://www.ecfr.gov/current/title-29/section-578.3)). The amount is adjusted for inflation each year.
- **Contractor misclassification** has its own tax penalties. See EMPLOYEE_VS_CONTRACTOR.md.

## Steps
1. **Confirm it's an employee, not a contractor** (EMPLOYEE_VS_CONTRACTOR.md).
2. **Write a short job description that lists the primary duties.** Compare it to the duties tests above ([29 CFR 541](https://www.ecfr.gov/current/title-29/part-541)). *You get:* a documented classification decision.
3. **Set the pay.** For an exempt role, pay a salary of at least $684/week, or $27.63/hour or more for a computer employee paid hourly. Otherwise, pay hourly or salary at $7.25 or more, with overtime. Put the exempt or non-exempt status in the offer letter (FIRST_HIRE_CHECKLIST.md, step 9).
4. **Pick the payroll schedule:** semimonthly, biweekly, or weekly. Get written consent for direct deposit. Set this up in your payroll provider.
5. **For non-exempt staff, turn on time tracking** in your payroll tool. Write a policy that unapproved overtime is still paid.
6. **For exempt staff, adopt a written policy on salary deductions** with a complaint process (541.603(d)). Put it in the offer packet or handbook.
7. **Keep records:** payroll 3 years, time cards 2 years ([FS21](https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping)).
8. **Interns:** pay them, or document all 7 FS71 factors with the school *before* the internship starts.
9. **At separation:** pay through the next regular payday, and give the DOL-800 ([GA DOL forms](https://dol.georgia.gov/employers)). The full offboarding steps are in `firing-and-offboarding-ga`.

**Pre-hire checklist**
- [ ] Is the worker an employee? (If not, see EMPLOYEE_VS_CONTRACTOR.md.)
- [ ] Is the primary duty real design, build, test, or analysis work, not support, repair, or training?
- [ ] Is the cash salary at least $684/week (or the hourly rate at least $27.63 for a computer employee)?
- [ ] Is every dollar of required pay in cash, with equity only on top?
- [ ] Are payroll runs at least semimonthly?
- [ ] Is time tracking set up (non-exempt) or a deduction policy in place (exempt)?
- [ ] Does the employee work outside Georgia? If so, check that state's rules.

**Decision flowchart (text)**
```
START: Is this person a W-2 employee? -- No/unsure --> EMPLOYEE_VS_CONTRACTOR.md
  | Yes
Unpaid intern or "volunteer"? -- Yes --> For-profit: volunteer = NOT allowed.
  |                                       Intern: pass FS71 primary-beneficiary test? No --> pay >= $7.25 + OT
  | No
Works outside GA? -- Yes --> that state's rules too (see `remote-and-out-of-state-hires`)
  | No
Total comp >= $107,432 incl. >= $684/wk salary AND regularly does 1+ exempt duty? -- Yes --> EXEMPT (HCE)
  | No
Primary duty = systems analysis / software design-build-test (541.400)?
  | Yes --> Paid salary >= $684/wk OR hourly >= $27.63? -- Yes --> EXEMPT (computer)
  |                                                       -- No  --> NON-EXEMPT
  | No
Manages dept + directs 2+ FTEs + hire/fire input, OR admin w/ discretion on matters of significance,
OR learned professional?  AND salary >= $684/wk paid on salary basis? -- Yes --> EXEMPT
  | No
NON-EXEMPT: track hours, pay >= $7.25/hr, 1.5x over 40/week, keep 516.2 records.
```

## Links
| Resource | URL | Why |
|----------|-----|-----|
| 29 CFR Part 541 (eCFR) | https://www.ecfr.gov/current/title-29/part-541 | Exemption tests, salary basis, computer, HCE |
| DOL salary levels | https://www.dol.gov/agencies/whd/overtime/salary-levels | Current $684 / $107,432 |
| May 15, 2026 technical rule | https://www.federalregister.gov/documents/2026/05/15/2026-09839/defining-and-delimiting-the-exemptions-for-executive-administrative-professional-outside-sales-and | 2024 rule vacatur and restored text |
| WHD Fact Sheet #17E | https://www.dol.gov/agencies/whd/fact-sheets/17e-overtime-computer | Computer exemption summary |
| WHD Fact Sheet #21 | https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping | Required records |
| WHD Fact Sheet #71 | https://www.dol.gov/agencies/whd/fact-sheets/71-flsa-internships | Intern primary-beneficiary test |
| WHD Fact Sheet #14 | https://www.dol.gov/agencies/whd/fact-sheets/14-flsa-coverage | Enterprise vs. individual coverage |
| DOL state minimum wage table | https://www.dol.gov/agencies/whd/minimum-wage/state | Federal $7.25; GA $5.15 scope |
| DOL state payday table | https://www.dol.gov/agencies/whd/state/payday | GA semimonthly (revised 1/1/2023) |
| DOL elaws: volunteers | https://webapps.dol.gov/elaws/whd/flsa/docs/volunteers.asp | No volunteering for for-profits |
| GA DOL Employer Handbook | https://dol.georgia.gov/documents/employer-handbook | Pay method, frequency, DOL-800 (some FLSA figures outdated) |
| O.C.G.A. § 34-7-2 (FindLaw, secondary) | https://codes.findlaw.com/ga/title-34-labor-and-industrial-relations/ga-code-sect-34-7-2/ | GA pay frequency and method |
| 29 U.S.C. §§ 216, 255, 260 | https://www.law.cornell.edu/uscode/text/29/216 | Damages and limitations |

## Double-check before sending
| Item | Value as of last check | Where to verify | Last verified |
|------|------------------------|-----------------|---------------|
| EAP standard salary level | $684/week ($35,568/yr) | eCFR 29 CFR 541.600; dol.gov/agencies/whd/overtime/salary-levels | 2026-10-25 |
| HCE total annual compensation | $107,432 (incl. ≥ $684/wk salary) | 29 CFR 541.601; DOL salary-levels page | 2026-10-25 |
| Computer employee hourly rate | $27.63/hour | 29 CFR 541.400(b); FS17E (Aug 2024) | 2026-10-25 |
| 2024 rule status | Vacated (E.D. Tex. and N.D. Tex., Nov 2024); 5th Cir. appeals dismissed May 5/7, 2026; CFR restored May 15, 2026 | 91 FR 27833 | 2026-10-25 |
| New Part 541 rulemaking | None found in Federal Register after 05/15/2026. Unified Agenda not checked | federalregister.gov (CFR 29 Part 541 filter); reginfo.gov agenda | 2026-10-25 (partial) |
| Federal minimum wage | $7.25/hour | DOL state table (updated 7/1/2026) | 2026-10-25 |
| GA minimum wage and scope | $5.15; not for FLSA-covered work, ≤5 employees, or ≤$40K sales | O.C.G.A. § 34-4-3 (FindLaw copy 3/28/2024, secondary); DOL state table | 2026-10-25 (official GA code not checked) |
| GA pay frequency | At least two equal periods per month (semimonthly); salaried heads excluded | O.C.G.A. § 34-7-2 (FindLaw, secondary); `dol224.pdf` p.15; DOL payday table (rev. 1/1/2023) | 2026-10-25 (official GA code not checked) |
| GA final paycheck rule | No general statute found; next regular payday is common practice | Secondary sources only; DOL final-pay page doesn't list states | Not verified on an official source |
| GA overtime law | None found; FLSA rules apply | `dol224.pdf` p.15 | 2026-10-25 (absence of a statute not confirmed in official code) |
| DOL-800 timing | Last day of work. If the employee isn't available, send it within 3 days by mail or email (amended rule) | `dol224.pdf` p.92 (R-11-24); Rule 300-2-7-.06 and GDOL post 2026-10-07 (see `firing-and-offboarding-ga`) | 2026-10-25 |
| FLSA civil money penalty (repeated/willful) | Up to $2,515 per violation (2025 adjustment; 2026 adjustment not in eCFR as of 10/22/2026) | 29 CFR 578.3 | 2026-10-25 |
| Statute of limitations | 2 years / 3 years willful | 29 U.S.C. § 255(a) | 2026-10-25 |
| Intern test guidance | FS71, updated Jan 2018 (7 factors) | dol.gov FS71 | 2026-10-25 |
| GA DOL Handbook FLSA figures | Outdated: shows $455/wk, $100K HCE, old 6-factor intern test | `dol224.pdf` pp.15, 19–22 | 2026-10-25 |

## When to bring in a professional
- **Employment attorney:**
  - The role mixes development with support, QA, or ops, or you have a junior or trainee developer you want to classify as exempt.
  - You've already been paying a non-exempt person as exempt.
  - You're considering deferred or accrued salary, or "equity instead of pay."
  - You're running an unpaid internship.
  - You're hiring outside Georgia, or paying monthly.
  - You've received a wage demand letter or a DOL investigation notice.
- **CPA or payroll provider:** regular-rate overtime math when there are bonuses, setting up time tracking, and any arrangement that defers pay (409A and when the pay becomes taxable).
- **Corporate attorney:** converting accrued salary into equity or notes, and how either shows up in diligence.

## Related packages
- `FIRST_HIRE_CHECKLIST.md`: the step-by-step hub
- `EMPLOYEE_VS_CONTRACTOR.md`: classifying the worker
- `PAYING_FOUNDERS.md`: draws, salary, S-corp election
- `EQUITY_FOR_EARLY_HIRES.md`: options, profits interests, 83(b), 409A
- `GA_EMPLOYER_TAXES.md`: withholding, FICA, FUTA, GA UI, filing calendar
- `PAYROLL_PEO_AND_BENEFITS.md`: payroll provider vs. PEO, health and retirement benefits
- `REMOTE_AND_OUT_OF_STATE_HIRES.md`: employees in other states and abroad
- `FIRING_AND_OFFBOARDING_GA.md`: terminations, final pay, severance, equity on exit
- `HEADCOUNT_TRIGGERS_AND_COMPLIANCE_CALENDAR.md`: laws by headcount, plus annual deadlines
- `DELAWARE_ENTITY_IN_GEORGIA.md`: foreign registration and costs in both states
- `LOCAL_BUSINESS_LICENSES_METRO_ATLANTA.md`: city and county occupation tax certificates
