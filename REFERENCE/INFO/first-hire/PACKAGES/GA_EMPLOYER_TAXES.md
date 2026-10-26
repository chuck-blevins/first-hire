---
id: ga-employer-taxes
title: "Employer Payroll Taxes and Filings in Georgia"
questions: ["What taxes do I need to collect and pay if active in GA?", "What payroll taxes do I owe when I hire my first employee in Georgia?", "Which forms do I file for payroll, and when?", "Do I need to register with the Georgia DOR and DOL before running payroll?", "What is Georgia's unemployment tax rate for a new employer?"]
tags: [payroll-taxes, withholding, fica, futa, ga-unemployment-insurance, new-hire-reporting, workers-comp, workplace-posters, filing-calendar]
jurisdiction: [US-federal, GA]
audience: [pre-revenue, funded-2-10]
related: [first-hire-checklist, paying-founders, employee-vs-contractor, equity-for-early-hires, exempt-vs-nonexempt-pay-rules, headcount-triggers-and-compliance-calendar, delaware-entity-in-georgia, payroll-peo-and-benefits, remote-and-out-of-state-hires, local-business-licenses-metro-atlanta]
last_verified: 2026-10-25
status: active
---

# Employer Payroll Taxes and Filings in Georgia

> General information for founders, not legal or tax advice. Confirm specifics with a CPA or attorney before acting.

## Short answer
Once you pay a W-2 employee in Georgia, you have three agencies to deal with. **IRS:** you withhold federal income tax and the employee's share of FICA, pay a matching employer share, deposit both through EFTPS, file Form 941 each quarter, and pay FUTA on Form 940 once a year. **GA Department of Revenue (DOR):** you register in the Georgia Tax Center, withhold GA income tax based on Form G-4, file G-7 returns, and file G-1003 with W-2s by January 31. **GA Department of Labor (DOL):** you register for state unemployment insurance (UI) and pay it quarterly on Form DOL-4N, at 2.70% of the first $9,500 per employee as a new employer. You also report each new hire within 10 days, buy workers' comp once you regularly have 3 or more employees, and put up the required posters. You can do all of this yourself in the agency portals, or a payroll provider can do it for you. Either way, you are the one legally responsible. Exception: for wages paid by an IRS-certified PEO (CPEO), the CPEO is solely liable for federal employment taxes (`p15.pdf` p.4; see `payroll-peo-and-benefits`).

## By stage
- **Pre-revenue founders:**
  - Georgia employer payroll obligations start when you pay a W-2 employee. Founders can be that employee: founders who work in a C-corp are W-2 employees, while LLC owners take draws and aren't on payroll (PAYING_FOUNDERS.md). A corporate officer who performs services counts for GA UI (`REFERENCE/INFO/first-hire/dol4e.pdf` p.2, per HEADCOUNT_TRIGGERS_AND_COMPLIANCE_CALENDAR.md).
  - **Now:** get an EIN, and enroll in EFTPS early. Enrollment takes about a week because the PIN arrives by mail ([eftps.gov](https://www.eftps.gov)).
  - **Very small payrolls:** an employer whose annual FICA plus withheld income tax is $1,000 or less can ask the IRS for written approval to file one Form 944 instead of four Forms 941 (`REFERENCE/INFO/first-hire/p15.pdf` p.5). An employer withholding $800 or less a year in GA can file one annual G-7, if it requests annual status in GTC before the first quarterly due date (`REFERENCE/INFO/first-hire/2026 Employers_Tax_Guide.pdf` p.7–8).
- **Funded teams hiring 2–10:**
  - In your first calendar year you deposit federal taxes monthly. You switch to semiweekly only if taxes in the lookback period were over $50,000 (`p15.pdf` p.33–34).
  - Workers' comp is required once you regularly employ 3 or more people, and corporate officers and LLC members count toward the 3 ([SBWC Employer Information](https://sbwc.georgia.gov/employer-information)).
  - For every new hire: collect a W-4, G-4 and I-9, and file the GA new-hire report within 10 days (`REFERENCE/INFO/first-hire/dol224.pdf` p.24).
  - Electronic filing of the GA DOL-4N becomes required at 25 or more employees (`dol224.pdf` p.78).
  - If you use a payroll provider, ask in writing which filings it submits. You still owe any tax the provider fails to pay.
  - Employees who live or work outside Georgia need professional help (`remote-and-out-of-state-hires`).

## What you need to know

**Federal income tax withholding (W-4).** Get a signed 2026 Form W-4 from each new hire and apply it from the first paycheck. If they don't turn one in, withhold as if they checked Single/Married filing separately and left everything else blank. The withholding tables are in Pub. 15-T. Sources: `REFERENCE/INFO/first-hire/p15.pdf` p.26; [IRS: About Form W-4](https://www.irs.gov/forms-pubs/about-form-w-4).

**FICA (Social Security + Medicare).** For 2026, Social Security is 6.2% from the employee plus 6.2% from you, on wages up to **$184,500**. Medicare is 1.45% plus 1.45% with no wage cap. Sources: `p15.pdf` p.1–2; [IRS Topic 751](https://www.irs.gov/taxtopics/tc751).

**Additional Medicare tax.** Once an employee's wages for the year pass $200,000, withhold an extra 0.9% from them starting in that pay period. You don't match it. Sources: `p15.pdf` p.29–30; [IRS Topic 751](https://www.irs.gov/taxtopics/tc751).

**FUTA (federal unemployment).** Only the employer pays it, never the employee. The rate is 6.0% on the first $7,000 per employee. If you pay your GA unemployment tax in full and on time, you get a credit of up to 5.4%, so you effectively pay **0.6%** (max $42 per employee per year). A deposit is due for any quarter where the running total owed is over $500. Georgia is **not** a credit-reduction state. It isn't on the final 2025 list (only California and the U.S. Virgin Islands are) or on DOL's list of *potential* 2026 reductions. DOL announces the final 2026 list after November 10, 2026. Sources: `p15.pdf` p.11–12, 43–44; [DOL FUTA credit reductions](https://oui.doleta.gov/unemploy/futa_credit.asp) (spreadsheets checked 2026-10-25); [IRS: FUTA credit reduction](https://www.irs.gov/businesses/small-businesses-self-employed/futa-credit-reduction).

**Federal deposit schedule.** All federal deposits must be made electronically, usually through EFTPS. In your first calendar year you are a **monthly** depositor: taxes for a month's paydays are due by the 15th of the next month. In later years, if your taxes in the lookback period (the 12 months ending June 30 of the year before last) were over $50,000, you switch to **semiweekly**: Wed–Fri paydays are due the next Wednesday, and Sat–Tue paydays are due the next Friday. Under either schedule, if you ever owe $100,000 or more in a single day, it's due the next business day. Sources: `p15.pdf` p.6, 33–34; [IRS employment tax due dates](https://www.irs.gov/businesses/small-businesses-self-employed/employment-tax-due-dates).

**Form 944 instead of 941.** Very small employers, whose total FICA plus withheld income tax for the year is $1,000 or less, can file one annual Form 944 instead of four Forms 941. You have to ask the IRS during the first quarter and get written approval before you can use it. Sources: `p15.pdf` p.5; [IRS: About Form 944](https://www.irs.gov/forms-pubs/about-form-944).

**Georgia income tax withholding (G-4).** Each employee fills out Form G-4 (Rev. 06/03/26), choosing a filing status (letter A–D) and claiming allowances. If they don't turn one in, you can use their federal W-4 election if it gives you enough information. Otherwise withhold as Single with zero allowances. As of the 2026 guide, Georgia has a **flat 4.99%** rate. Employers could start using it on May 11, 2026, and before that date the rate was 5.19%. You can use the wage-bracket tables (guide pp.31–50) or the percentage method (pp.51–54): subtract the standard deduction and the dependent allowance ($5,000 per year each), then multiply by 4.99%. Sources: `2026 Employers_Tax_Guide.pdf` (Rev. Sept 2026) p.3, 14–15, 51; `TSD_Employees_Withholding_Allowance_Certificate_G-4.pdf` p.1.
- *Discrepancy:* as of 2026-10-25, the live [DOR withholding page](https://dor.georgia.gov/taxes/withholding-tax-employers) still says withholding is a "graduated scale" and links to a 2014 guide. The 2026 guide, which is the same file as the live download, says the rate is flat. Go with the 2026 guide.

**GA filing frequency.** DOR assigns your filing frequency when you register, usually within 15 minutes. The frequency depends on how much you withhold:
- Annual: $800 or less per year
- Quarterly: $200 or less per month
- Monthly: more than $200 per month. Payment is due by the 15th of the next month.
- Semiweekly: more than $50,000 in the lookback period

Most filers file a quarterly **G-7** by the last day of the month after the quarter ends, even if they withheld nothing. The exception is employers withholding $800 or less a year. They can file one G-7 by January 31 of the following year, but only if they request annual status in GTC before the first quarterly due date (p.7–8). Once a G-7 shows more than $500 withheld, you must pay by EFT and file electronically from then on. The yearly reconciliation is **G-1003**, filed with your W-2s by January 31. Sources: `2026 Employers_Tax_Guide.pdf` p.6, 8–9, 15, 19.

**GA unemployment insurance (SUTA).** You become liable once you pay $1,500 in wages in any calendar quarter, or have at least one worker in 20 different weeks of a year (`dol4e.pdf` p.2).
- **Taxable wage base:** $9,500 per employee per year (`dol224.pdf` p.68; [GA DOL: file reports](https://dol.georgia.gov/file-tax-and-wage-reports-and-make-payments)).
- **New-employer rate:** 2.70% total. For 2024–2026 that total is a 2.64% contribution rate plus a 0.06% administrative assessment. Your actual rate is on your DOL-626 rate notice in the Employer Portal. You can't take this tax out of employees' paychecks. Sources: SB 160 (2023) §§1, 3 ([text](https://gov.georgia.gov/document/2023-signed-legislation/sb-160/download) p.2–4); `dol224.pdf` p.68, 72; [GA DOL UI FAQ](https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance); `dol810.pdf`.
- **Quarterly report:** File a DOL-4N tax and wage report and pay by April 30, July 31, October 31 and January 31, or the next business day if that date falls on a weekend or holiday. Electronic filing is **required at 25 or more employees**. DOL's portal is the preferred route at any size, and as of 2026-10-25 UI tax services are offered only through the Employer Portal. Sources: `dol224.pdf` p.78; `dol4606.pdf` p.2; [GA DOL: file reports](https://dol.georgia.gov/file-tax-and-wage-reports-and-make-payments).
- *Discrepancies:* `dol4e.pdf` (R-9/16, still the live version as of 2026-10-25) says new employers pay 2.70% and requires electronic filing only above 100 employees. The newer handbook and DOL-4606 say 25. Go with 25. The live FAQ also mentions an outdated $8,500 wage base in one answer. The current base is $9,500.

**New-hire reporting.** Within **10 days** of hire, report every new or rehired employee who lives or works in Georgia. Report even someone who worked only one day. The report covers the employee's name, address, SSN, date of birth, start date, state of hire and whether medical insurance is available, plus your FEIN, name and address. File online, by upload, or by mail at [ga-newhire.com](https://www.ga-newhire.com/), which redirects to newhire-reporting.com. Sources: `dol224.pdf` p.24; [GA New Hire FAQ](https://newhire-reporting.com/GA-Newhire/FAQ.aspx).

**Workers' compensation.** It's required once you regularly employ **3 or more** people, part-time or full-time. Corporate officers and LLC members count toward the 3 even if they waive their own coverage on Form WC-10. It's administered by the State Board of Workers' Compensation (SBWC). If you're required to carry it and don't, the Board can fine you $500–$5,000 per occurrence, and willfully going without it is a misdemeanor. Sources: `dol224.pdf` p.30; [SBWC Employer Information](https://sbwc.georgia.gov/employer-information).

**Posters.** GA DOL requires these posters (English and Spanish versions are available):
- DOL-810, Unemployment Insurance for Employees
- DOL-154, Employer Vacation
- DOL-4107, Equal Pay

SBWC requires its Bill of Rights (WC-BOR), a Panel of Physicians (WC-P1 or WC-P3), a notice that you have coverage, and your insurer's name. Federal posters are separate; use the [elaws Poster Advisor](https://webapps.dol.gov/elaws/posters.htm) to see which apply. Sources: [GDOL required posters](https://dol.georgia.gov/laws-and-rules/gdol-required-workplace-posters); `dol224.pdf` p.33; [SBWC Employer Information](https://sbwc.georgia.gov/employer-information).
- *Discrepancy:* the handbook also lists DOL-4244, which is for public employers, and calls WC-P1 the "Workers' Compensation Notice." The live page lists WC-P1 as the Panel of Physicians. Go with the live page. `dol1693.pdf` (Equal Opportunity Is the Law) is GA DOL's own WIOA notice and is not on the employer poster list.

**Local payroll taxes.** No GA source I checked mentions a city or county income or payroll tax withheld from wages. The DOR guide covers state withholding only. Some cities and counties charge business *occupation taxes*, but that's a business license fee, not a paycheck deduction. O.C.G.A. § 48-13-5 confirms the occupation tax is levied on the business entity "for engaging in an occupation" (FindLaw copy, current as of 2024-03-28; see `local-business-licenses-metro-atlanta`). No GA source checked mentions a local tax withheld from wages. Check the local business license office for your city or county.

## Steps
1. **Get an EIN** (prerequisite). You get it from the [IRS](https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number).
2. **Enroll in EFTPS** at [eftps.gov](https://www.eftps.gov). Enrollment takes about a week because the PIN arrives by mail. You get the login you'll use for federal deposits.
3. **Register for GA withholding** in the [Georgia Tax Center](https://gtc.dor.ga.gov/_/), under "Register a New Georgia Business." You get a withholding number and your filing frequency within about 15 minutes ([DOR](https://dor.georgia.gov/taxes/register-new-business-georgia)).
4. **Register for a GA UI tax account** using GA DOL's online registration at [dol.georgia.gov/online-services](https://dol.georgia.gov/online-services). DOL's FAQ says to do this right after your first GA payroll. You get an account number right away. Then set up the [Employer Portal](https://eresponse.gdol.ga.gov/idp/sso/employer/login), where you'll file DOL-4N, make payments and see your rate notice.
5. **Collect a W-4, G-4 and I-9** from each new hire before their first paycheck.
6. **Report the hire** at [ga-newhire.com](https://www.ga-newhire.com/) within 10 days.
7. **Buy workers' comp** from a licensed insurer before you reach 3 employees. Many founders buy it from day one. You get a policy, and the coverage shows up in the [SBWC verification lookup](https://sbwc.georgia.gov/online-employers-workers-compensation-coverage-verification).
8. **Put up the posters**: GA DOL, SBWC and federal.
9. **Run payroll and follow the 2026 payment calendar at the end of these steps.** If you use a payroll provider, ask in writing which filings it submits for you. You still have to complete the registrations yourself, and you still owe any tax the provider fails to pay.

### Who you pay, what, when (2026 dates; weekends roll to the next business day)
| Agency | What | How often | Due |
|---|---|---|---|
| IRS (EFTPS) | Withheld federal income tax + both shares of FICA | Monthly (year 1) | 15th of the next month |
| IRS | Form 941 | Quarterly | Apr 30, Jul 31, Nov 2 (Oct 31 is a Saturday), Feb 1, 2027 |
| IRS (EFTPS) | FUTA deposit, if more than $500 has built up | Quarterly | Same dates as Form 941 |
| IRS | Form 940 (FUTA annual) | Annual | Feb 1, 2027 (Feb 10 if all deposits were on time) |
| SSA / employees | W-2s + W-3 | Annual | Feb 1, 2027 (Jan 31 is a Sunday) |
| GA DOR (GTC) | Withholding payment | Monthly filers | 15th of the next month |
| GA DOR (GTC) | Form G-7 | Quarterly | Apr 30, Jul 31, Nov 2, 2026; Feb 1, 2027 |
| GA DOR (GTC) | G-1003 + W-2s | Annual | Feb 1, 2027 |
| GA DOL (Portal) | DOL-4N report + UI tax | Quarterly | Apr 30, Jul 31, Nov 2 (Oct 31 is a Saturday), Feb 1, 2027 (Jan 31 is a Sunday) |
| GA New Hire | New-hire report | Per hire | Within 10 days of hire |

Sources: `p15.pdf` p.11–12, 33; `2026 Employers_Tax_Guide.pdf` p.6; `dol224.pdf` p.78; [IRS due dates](https://www.irs.gov/businesses/small-businesses-self-employed/employment-tax-due-dates).

## Links
| Resource | URL | Why |
|----------|-----|-----|
| IRS Pub 15 (2026) | https://www.irs.gov/pub/irs-pdf/p15.pdf | Federal rules on withholding, FICA, deposits and FUTA |
| IRS employment tax due dates | https://www.irs.gov/businesses/small-businesses-self-employed/employment-tax-due-dates | Federal calendar |
| EFTPS | https://www.eftps.gov | Federal deposits (founder logs in) |
| DOL FUTA credit reductions | https://oui.doleta.gov/unemploy/futa_credit.asp | Credit-reduction state list |
| Georgia Tax Center | https://gtc.dor.ga.gov/_/ | GA withholding registration, G-7, G-1003 (founder logs in) |
| GA DOR withholding | https://dor.georgia.gov/taxes/withholding-tax-employers | Forms and guide |
| GA DOR 2026 Employer's Tax Guide | https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-june-2026/download | Tables and percentage method (Rev. Sept 2026) |
| GA DOL online services | https://dol.georgia.gov/online-services | UI account registration |
| GA DOL Employer Portal | https://eresponse.gdol.ga.gov/idp/sso/employer/login | DOL-4N filing, payments, rate notice (founder logs in) |
| GA DOL file reports/payments | https://dol.georgia.gov/file-tax-and-wage-reports-and-make-payments | Due dates and wage base |
| GA New Hire Reporting | https://www.ga-newhire.com/ | 10-day new-hire reports |
| SBWC employer info | https://sbwc.georgia.gov/employer-information | Workers' comp rules and posters |
| GDOL required posters | https://dol.georgia.gov/laws-and-rules/gdol-required-workplace-posters | Poster downloads |

## Double-check before sending
| Item | Value as of last check | Where to verify | Last verified |
|------|------------------------|-----------------|---------------|
| Social Security rate / 2026 wage base | 6.2% + 6.2%; $184,500 | IRS Topic 751; Pub 15 p.1–2 (ssa.gov returned 403) | 2026-10-25 |
| Medicare rate | 1.45% + 1.45%, no cap | IRS Topic 751 | 2026-10-25 |
| Additional Medicare threshold/rate | 0.9% over $200,000, employee only | IRS Topic 751 | 2026-10-25 |
| FUTA rate / wage base / max credit | 6.0% / $7,000 / 5.4% (net 0.6%) | Pub 15 p.43–44 | 2026-10-25 |
| GA FUTA credit reduction | None (not on the 2025 final list or the 2026 potential list); final 2026 list comes after Nov 10, 2026 | DOL futa_credit.asp | 2026-10-25 |
| Federal deposit lookback threshold | $50,000; $100,000 next-day rule | Pub 15 p.33–34 | 2026-10-25 |
| FUTA deposit threshold | More than $500 | Pub 15 p.12 | 2026-10-25 |
| Form 944 eligibility | $1,000 or less in annual liability; written IRS approval needed | IRS About Form 944; Pub 15 p.5 | 2026-10-25 |
| 941/940/W-2 deadlines | Last day of the month after each quarter; Jan 31 (940 Feb 10 if all deposits on time) | IRS due-dates page | 2026-10-25 |
| W-4 revision | 2026 | IRS About Form W-4 | 2026-10-25 (per SOURCES.md) |
| GA withholding rate | Flat 4.99% (from May 11, 2026; 5.19% before) | 2026 DOR guide p.3 (live DOR page still says "graduated") | 2026-10-25 |
| GA standard deduction / dependent | $15,000 single, $30,000 MFJ / $5,000 | 2026 DOR guide p.3, 51 | 2026-10-25 |
| G-4 revision | Rev. 06/03/26 | DOR G-4 page | 2026-10-25 (local PDF only) |
| GA filing-frequency thresholds | $800/yr, $200/mo, $50,000 lookback; EFT if more than $500 | 2026 DOR guide p.8 | 2026-10-25 |
| G-7 / G-1003 due dates | See calendar; G-1003 + W-2s Jan 31 | 2026 DOR guide p.6, 19 | 2026-10-25 |
| GA UI wage base | $9,500 | GA DOL file-reports page | 2026-10-25 |
| GA new-employer total rate | 2.70% (2.64% + 0.06% admin. assessment, 2024–2026) | SB 160; GA DOL UI FAQ; DOL-626 in Portal | 2026-10-25 |
| GA UI liability trigger | $1,500 in a quarter or 1 worker in 20 weeks | dol4e.pdf p.2 | 2026-10-25 |
| DOL-4N due dates | Apr 30 / Jul 31 / Oct 31 / Jan 31 (rolls to the next business day: Nov 2, 2026; Feb 1, 2027) | GA DOL file-reports page | 2026-10-25 |
| DOL electronic filing threshold | 25 or more employees | dol224 p.78; dol4606 p.2 (live page gives no number) | 2026-10-25 |
| New-hire deadline | 10 days | GA New Hire FAQ | 2026-10-25 |
| Workers' comp threshold | 3 or more regular employees | SBWC Employer Information | 2026-10-25 |
| Required GA posters | DOL-810, DOL-154, DOL-4107; WC-BOR, WC-P1/P3 | GDOL posters page; SBWC | 2026-10-25 |
| Local payroll taxes | None found; **not confirmed** | City/county business license office | Not verified |
| 2027 UI rate after SB 160 sunset | Unknown; SB 160 text has the 2.64% rate and the assessment ending after Dec 31, 2026 | GA DOL; 2027 DOL-626 | Not verified |

## When to bring in a professional
- Employees who live or work outside Georgia, or remote hires in other states.
- Paying yourself as an S-corp owner, or deciding whether an owner counts as an employee for UI or workers' comp.
- Missed deposits or filings, penalty notices, or a payroll provider that failed to pay.
- Deciding whether a worker is a contractor or an employee.
- Buying or merging with a business that already has employees (UI rate transfer, DOL-1N).
- Equity compensation, bonuses, or anyone paid more than $200,000.

## Related packages
- `FIRST_HIRE_CHECKLIST.md`: the step-by-step hub
- `EMPLOYEE_VS_CONTRACTOR.md`: classifying the worker
- `EXEMPT_VS_NONEXEMPT_PAY_RULES.md`: overtime, minimum wage, pay frequency
- `PAYING_FOUNDERS.md`: draws, salary, S-corp election
- `EQUITY_FOR_EARLY_HIRES.md`: options, profits interests, 83(b), 409A
- `PAYROLL_PEO_AND_BENEFITS.md`: payroll provider vs. PEO, health and retirement benefits
- `REMOTE_AND_OUT_OF_STATE_HIRES.md`: employees in other states and abroad
- `FIRING_AND_OFFBOARDING_GA.md`: terminations, final pay, severance, equity on exit
- `HEADCOUNT_TRIGGERS_AND_COMPLIANCE_CALENDAR.md`: laws by headcount, plus annual deadlines
- `DELAWARE_ENTITY_IN_GEORGIA.md`: foreign registration and costs in both states
- `LOCAL_BUSINESS_LICENSES_METRO_ATLANTA.md`: city and county occupation tax certificates
