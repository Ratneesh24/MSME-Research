# 5. Problem database (42 problems) and scoring model

> Brief sections 18–19. Data: `data/problems.csv` (descriptive fields + evidence), `data/problem_scores.csv` (scores), `data/scoring_criteria.csv`. Logic: `scripts/msme_data/problems.py`.

## 5.1 Scoring model

Each problem is scored 0–10 on 14 criteria. **Higher is always better for a startup**, so competitive intensity and regulatory complexity are inverted into *white space* and *regulatory ease*. The weights follow the brief's priorities: willingness to pay over number of users, and distribution feasibility over attractive ideas.

| Criterion | Weight | Scoring anchors |
|---|---|---|
| Number of customers affected | 6% | 10: >1 crore MSMEs; 8: 10 lakh-1 crore; 6: 2-10 lakh; 4: 50k-2 lakh; 2: <50k direct buyers |
| Pain severity | 8% | 10: existential/cash crisis; 5: notable cost; 2: annoyance |
| Frequency | 6% | 10: daily; 8: weekly; 6: monthly; 4: quarterly; 2: annual or one-off |
| Financial impact per affected firm | 8% | 10: >5% of revenue; 7: 2-5%; 5: 1-2%; 3: <1% |
| Willingness to pay (evidence) | 12% | 10: demonstrated large-scale payment for this outcome; 7: some paying segments; 4: stated interest only; 2: expects free |
| Existing spending pool | 10% | 10: Rs 1,000 cr+ observable revenue to incumbents; 7: Rs 100-1,000 cr; 4: <Rs 100 cr; 2: negligible |
| Competitive white space (inverse of intensity) | 7% | 10: few or no credible solutions; 5: several but clear gaps; 2: saturated, funded incumbents or free tools |
| Ease of customer acquisition | 10% | 10: concentrated buyers or channel with pull; 5: feasible via field/partners; 2: diffuse, high CAC |
| Technology feasibility | 5% | 10: buildable with current tech in <6 months; 5: needs hardware or deep integrations; 2: research-grade |
| Scalability | 7% | 10: software-only pan-India; 5: needs local ops; 2: heavy services or capex |
| Gross-margin potential | 6% | 10: >75%; 7: 50-75%; 4: 20-50%; 2: <20% |
| Regulatory ease (inverse of complexity) | 3% | 10: no licence; 6: data/consumer rules; 3: licensed activity (NBFC, insurance, payments) |
| Retention potential | 7% | 10: system of record or embedded workflow; 5: periodic; 2: one-off |
| Expansion opportunity | 5% | 10: clear cross-sell and international; 5: some; 2: narrow |

**Evidence confidence** (per problem): **H** = measured by official or large-sample data *and* observable spend; **M** = some measured data, WTP inferred; **L** = mostly reasoned. Treat L-confidence scores as hypotheses for interviews.

**Sensitivity check.** Re-ranking with *equal* weights leaves the top five unchanged in membership (P09, P05, P10, P01, P30). Credit (P02) and logistics (P16) fall several places, because their scores rely on spend and financial impact rather than white space. The ranking is therefore not an artefact of the weights.

## 5.2 Ranked scores

| # | ID | Problem | Cust | Sev | Freq | ₹Imp | WTP | Spend | WhSp | CAC-ease | Tech | Scale | GM | Reg-ease | Ret | Exp | **Score** | EW # | Conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P09 | Finding new customers (lead generation) | 9 | 8 | 9 | 7 | 9 | 9 | 3 | 6 | 8 | 9 | 7 | 9 | 6 | 8 | **7.61** | 1 | H |
| 2 | P05 | CA-firm productivity: client data collection, entry and reconciliation | 4 | 7 | 9 | 6 | 8 | 7 | 6 | 8 | 8 | 8 | 8 | 9 | 9 | 7 | **7.39** | 3 | M |
| 3 | P10 | Converting and following up leads (slow response, no CRM) | 8 | 7 | 10 | 6 | 7 | 6 | 6 | 7 | 8 | 9 | 7 | 8 | 8 | 8 | **7.33** | 2 | M |
| 4 | P01 | Delayed B2B payments and receivables collection | 8 | 9 | 8 | 8 | 6 | 6 | 7 | 6 | 8 | 8 | 7 | 7 | 7 | 8 | **7.21** | 4 | H |
| 5 | P30 | EU CBAM and product carbon-footprint compliance | 3 | 9 | 6 | 9 | 7 | 4 | 7 | 7 | 8 | 7 | 7 | 7 | 8 | 9 | **6.94** | 5 | M |
| 6 | P02 | Access to affordable working-capital credit | 9 | 9 | 6 | 8 | 8 | 10 | 3 | 5 | 7 | 7 | 5 | 3 | 5 | 7 | **6.86** | 11 | H |
| 7 | P22 | High energy cost and inefficiency | 6 | 7 | 9 | 8 | 7 | 7 | 6 | 6 | 8 | 5 | 4 | 7 | 9 | 6 | **6.79** | 10 | M |
| 8 | P15 | Procurement: supplier discovery, reliability and credit at purchase | 8 | 7 | 8 | 7 | 8 | 10 | 4 | 5 | 7 | 5 | 3 | 6 | 7 | 7 | **6.72** | 12 | H |
| 9 | P04 | Bookkeeping and GST return preparation (owner side) | 9 | 6 | 8 | 4 | 7 | 9 | 2 | 4 | 8 | 8 | 7 | 8 | 9 | 6 | **6.65** | 6 | H |
| 10 | P14 | Raw-material price volatility | 8 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 7 | 7 | 6 | 8 | 6 | 6 | **6.64** | 7 | M |
| 11 | P16 | Logistics cost penalty for small shippers | 8 | 6 | 8 | 8 | 7 | 9 | 4 | 5 | 7 | 6 | 3 | 7 | 6 | 6 | **6.48** | 17 | H |
| 12 | P17 | Inventory management (stock-outs, dead stock) | 8 | 5 | 9 | 5 | 5 | 6 | 3 | 5 | 9 | 9 | 8 | 10 | 8 | 5 | **6.4** | 8 | M |
| 13 | P19 | Production planning and job tracking in job shops | 5 | 6 | 10 | 6 | 5 | 4 | 7 | 5 | 7 | 7 | 7 | 10 | 9 | 7 | **6.39** | 9 | L |
| 14 | P21 | Quality rejections and OEM supplier-quality requirements | 4 | 7 | 8 | 6 | 6 | 5 | 6 | 6 | 7 | 6 | 7 | 9 | 8 | 6 | **6.32** | 15 | L |
| 15 | P06 | GST input-tax-credit mismatches and notices | 8 | 7 | 6 | 6 | 6 | 6 | 4 | 5 | 8 | 8 | 7 | 8 | 7 | 4 | **6.29** | 16 | M |
| 16 | P41 | Legal recovery of overdue dues (MSEFC/ODR) | 6 | 8 | 3 | 8 | 7 | 5 | 8 | 6 | 7 | 7 | 7 | 6 | 4 | 5 | **6.29** | 22 | M |
| 17 | P42 | Bank and UPI reconciliation | 8 | 5 | 10 | 3 | 5 | 5 | 4 | 5 | 8 | 9 | 8 | 9 | 8 | 5 | **6.19** | 13 | M |
| 18 | P29 | Trade finance for exporters | 5 | 7 | 6 | 7 | 8 | 7 | 4 | 5 | 6 | 7 | 5 | 3 | 6 | 7 | **6.17** | 29 | M |
| 19 | P28 | Cross-border payment cost and forex conversion | 5 | 5 | 8 | 5 | 8 | 7 | 2 | 6 | 6 | 9 | 6 | 3 | 7 | 6 | **6.15** | 28 | H |
| 20 | P37 | Loan documentation (CMA data, project reports) and credit readiness | 7 | 6 | 3 | 4 | 7 | 5 | 6 | 7 | 8 | 8 | 8 | 8 | 4 | 6 | **6.12** | 21 | M |
| 21 | P26 | Finding international buyers (export discovery) | 5 | 6 | 6 | 7 | 6 | 6 | 5 | 5 | 7 | 7 | 6 | 8 | 5 | 9 | **6.11** | 19 | M |
| 22 | P34 | Winning public procurement (GeM/tenders) | 6 | 5 | 7 | 6 | 6 | 5 | 4 | 6 | 8 | 8 | 7 | 9 | 6 | 4 | **6.03** | 20 | M |
| 23 | P03 | No cash-flow visibility or forecasting | 7 | 6 | 8 | 5 | 4 | 3 | 7 | 4 | 8 | 9 | 8 | 9 | 7 | 6 | **6.02** | 14 | L |
| 24 | P20 | Machine downtime and low OEE | 5 | 6 | 9 | 6 | 5 | 4 | 7 | 5 | 6 | 6 | 5 | 10 | 8 | 7 | **6.02** | 18 | L |
| 25 | P08 | Licences, renewals, factory and environment consents | 6 | 7 | 4 | 5 | 6 | 6 | 6 | 5 | 7 | 6 | 6 | 7 | 8 | 5 | **5.95** | 26 | M |
| 26 | P07 | Payroll, PF/ESI and new labour-code compliance | 6 | 6 | 6 | 4 | 6 | 6 | 4 | 5 | 8 | 7 | 6 | 7 | 8 | 5 | **5.89** | 25 | M |
| 27 | P23 | Hiring skilled workers | 8 | 7 | 5 | 5 | 5 | 6 | 4 | 5 | 8 | 7 | 6 | 9 | 4 | 6 | **5.82** | 24 | M |
| 28 | P31 | ESG/BRSR value-chain data requests from large buyers | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 7 | 8 | 8 | 7 | 8 | 7 | 8 | **5.76** | 27 | L |
| 29 | P27 | Export documentation and compliance | 5 | 5 | 7 | 4 | 6 | 6 | 4 | 5 | 7 | 7 | 6 | 7 | 7 | 6 | **5.74** | 30 | M |
| 30 | P25 | Attendance and wage payments for micro payroll | 8 | 4 | 10 | 3 | 4 | 4 | 3 | 5 | 9 | 9 | 7 | 9 | 7 | 4 | **5.69** | 23 | M |
| 31 | P33 | Claiming state and central investment incentives | 4 | 6 | 2 | 8 | 8 | 5 | 5 | 5 | 6 | 5 | 7 | 8 | 4 | 4 | **5.58** | 37 | L |
| 32 | P36 | Insurance protection gap | 9 | 6 | 2 | 5 | 4 | 6 | 5 | 5 | 7 | 8 | 6 | 3 | 6 | 6 | **5.55** | 35 | L |
| 33 | P12 | Digital marketing and social media content | 8 | 4 | 7 | 3 | 4 | 5 | 2 | 5 | 9 | 8 | 6 | 9 | 5 | 5 | **5.32** | 32 | M |
| 34 | P32 | Discovering and applying for government schemes | 9 | 5 | 2 | 6 | 5 | 4 | 6 | 5 | 7 | 6 | 6 | 8 | 3 | 5 | **5.29** | 36 | L |
| 35 | P38 | Owner dashboards / MIS | 7 | 4 | 6 | 3 | 3 | 3 | 5 | 4 | 8 | 9 | 8 | 10 | 6 | 6 | **5.28** | 31 | L |
| 36 | P40 | Obtaining quality certifications (ISO, BIS, ZED) | 5 | 6 | 2 | 5 | 7 | 5 | 4 | 6 | 6 | 5 | 5 | 6 | 4 | 5 | **5.18** | 42 | L |
| 37 | P39 | Knowing how to adopt AI | 8 | 4 | 5 | 4 | 4 | 3 | 5 | 4 | 8 | 7 | 6 | 9 | 5 | 7 | **5.17** | 33 | L |
| 38 | P35 | Cybersecurity and payment fraud | 8 | 6 | 3 | 4 | 3 | 3 | 5 | 3 | 7 | 8 | 6 | 9 | 6 | 6 | **5.03** | 38 | M |
| 39 | P18 | Demand forecasting | 6 | 4 | 6 | 4 | 3 | 2 | 6 | 3 | 7 | 8 | 8 | 10 | 6 | 5 | **5.0** | 34 | L |
| 40 | P11 | Creating and maintaining a website | 8 | 3 | 2 | 2 | 4 | 5 | 2 | 5 | 10 | 8 | 6 | 10 | 4 | 4 | **4.82** | 39 | M |
| 41 | P24 | Training and upskilling workers | 7 | 5 | 4 | 4 | 3 | 3 | 6 | 4 | 7 | 6 | 5 | 9 | 4 | 5 | **4.73** | 41 | L |
| 42 | P13 | Product catalogues and photography for marketplaces | 7 | 3 | 3 | 2 | 4 | 3 | 4 | 5 | 9 | 8 | 7 | 10 | 3 | 4 | **4.7** | 40 | L |

EW # = rank under equal weights.

## 5.3 Problem database (evidence, current solutions, spending)

Full text in `data/problems.csv`. Condensed view:

| ID | Problem | MSMEs affected | Frequency | Financial impact (evidence) | Current solution | Current spending | Competition | Startup opportunity |
|---|---|---|---|---|---|---|---|---|
| P01 | Delayed B2B payments and receivables collection | ~1-1.5 crore B2B sellers; most acute for 8-12 lakh firms of Rs 2-250 cr turnover | Continuous (weekly follow-ups) | Rs 7.34 lakh cr delayed (Mar-24, GAME 3.0) / ~Rs 8.1 lakh cr (Economic Survey 2025-26); avg payment 73 days vs 45-day law; 82.6% of invoices carry 0-30 day terms (Recordent 2026); only Rs 55,244 cr (~7%) ever filed on Samadhaan | Phone/WhatsApp follow-ups, lawyers, MSEFC, TReDS (Rs 3.47 lakh cr FY26), credit-bureau reporting (Recordent) | TReDS discount charges; legal/collection fees; no consolidated estimate | Low-Medium: TReDS platforms, KredX, Recordent, generic AR tools; no MSME-native AR copilot at scale | AI receivables copilot + legal escalation (ODR/MSEFC) + embedded invoice finance |
| P02 | Access to affordable working-capital credit | Credit gap Rs 30 lakh cr = 24% of demand; only 41% of MSME borrowers have active formal credit | Monthly | Gap highest for medium (29%), women-owned (35%), trading (33%) (SIDBI-Crisil 2025) | Banks, NBFCs, fintech lenders, CGTMSE, MUDRA (Rs 5.94 lakh cr FY26), PSB digital model (Rs 52,300 cr Apr-Dec 25) | Interest and fees on a very large loan book | High: banks, NBFCs (FlexiLoans, Lendingkart, Indifi, Oxyzo), DSAs | Credit-readiness + lender marketplace; cash-flow underwriting on AA/GST |
| P03 | No cash-flow visibility or forecasting | Most GST-registered MSMEs (no measured figure) | Weekly | Profitable firms still run out of cash (73-day cycle, S22); no direct measurement | Excel, CA, gut feel | Negligible standalone spend | Low in India; Agicap-type tools abroad | Cash-flow module inside AR/AP or banking product (not standalone) |
| P04 | Bookkeeping and GST return preparation (owner side) | ~1.6 crore GSTINs | Monthly/quarterly | CA fees typically Rs 1-5k/month (indicative); late fees and ITC loss on errors | CAs/accountants + Tally/Busy/Marg/Vyapar/myBillBook/Zoho Books | Large: Tally Rs 500-1,000 cr; Clear Rs 272 cr; CA fee pool | Very high (saturated, many free tiers) | Avoid head-on; serve via CA-firm tooling (P05) |
| P05 | CA-firm productivity: client data collection, entry and reconciliation | ~1 lakh firms serving most of the 1.49 crore GST filers | Daily, peaking at due dates | Staff shortage and manual data entry from WhatsApp photos, PDFs and bank statements; due-date crunch | Articled staff, Excel, Tally, practice-management tools, GST software | CAs already buy GST/ITR/Tally software (Rs 5-50k/yr typical, indicative) | Medium: Clear, Suvit, Tally add-ons, practice-management tools; AI layer immature | AI copilot for CA firms: WhatsApp document intake, auto-posting to Tally, GSTR-2B/IMS reconciliation, notices |
| P06 | GST input-tax-credit mismatches and notices | ~1.49 crore normal filers; acute for multi-vendor buyers | Monthly | ITC denial is a direct cash loss; growing data-driven notices | CA + reconciliation tools (Clear, others) | Part of GST software spend | Medium-High | Reconciliation + vendor-compliance nudges (bundle into P05) |
| P07 | Payroll, PF/ESI and new labour-code compliance | Est. 6-10 lakh establishments (low confidence) | Monthly | Four labour codes effective 21-Nov-2025 change wage definitions and registrations; mfg MSME compliance cost Rs 13-17 lakh/yr (all laws) | Consultants, payroll SaaS (greytHR, Keka, Zoho Payroll, RazorpayX), Excel | Payroll SaaS + consultant fees | High | Managed payroll + labour-code compliance for 10-200 staff firms |
| P08 | Licences, renewals, factory and environment consents | 2.67 lakh ASI factories + unregistered manufacturers | Quarterly/annual deadlines | 998 unique obligations, 1,456 compliances, 70+ approvals, 59 inspectors per single-state mfg MSME; Rs 13-17 lakh/yr (TeamLease 2025) | Consultants, in-house staff, enterprise compliance tools | Consultant fees; enterprise RegTech | Medium (enterprise-focused vendors) | Compliance calendar + done-for-you filings for mid-size factories |
| P09 | Finding new customers (lead generation) | Most MSMEs; 70% rely on traditional marketing | Daily | Revenue growth constrained; high competition is a top-3 challenge (SIDBI-Crisil 2025) | IndiaMART, Justdial, TradeIndia, referrals, distributors, trade fairs, Google Ads | IndiaMART FY26 revenue Rs 1,569 cr from 2.28 lakh payers (~Rs 69k/yr); Justdial Rs 1,214 cr, 6.3 lakh paid campaigns | High (entrenched marketplaces) | Do not build another marketplace; win on conversion (P10) |
| P10 | Converting and following up leads (slow response, no CRM) | ~4-6 lakh B2B MSMEs paying for leads; ~15 lakh broader | Daily | Paid leads wasted when response is slow or language mismatched (no measured India figure) | Owner's phone, WhatsApp Business app, Excel, IndiaMART lead manager, WhatsApp BSP tools | WhatsApp BSPs Rs 1.5-3.5k/month (AiSensy 2.1 lakh accounts); LeadSquared (enterprise) | Medium: tools exist, not done-for-you vernacular agents for B2B | AI sales agent on WhatsApp/voice: instant vernacular response, qualification, quotes, follow-ups |
| P11 | Creating and maintaining a website | ~7.7 crore establishments lack a site; ~20-35 lakh have one | One-off | Limited direct revenue impact for most micro firms | Freelancers, agencies, Wix/GoDaddy/Hostinger | Fragmented, low-ticket (Rs 3-15k one-time typical, indicative) | Very high, commoditised by AI | Bundle only (as a lead-capture asset in P10) |
| P12 | Digital marketing and social media content | Only ~13% use digital marketing/e-commerce actively | Weekly | Uncertain ROI | Agencies, freelancers, Meta/Google self-serve | Ad spend + agency retainers (fragmented) | Very high | Low priority standalone |
| P13 | Product catalogues and photography for marketplaces | Lakhs of marketplace sellers | Occasional | Lower conversion on poor listings | Photographers, marketplace services, AI image tools | Small | Medium; AI commoditising | Feature within sales agent / storefront |
| P14 | Raw-material price volatility | 55.7% of 27,000+ surveyed MSMEs cite it as top procurement challenge | Weekly | Margin erosion when input prices swing and output prices are fixed | Phone quotes, trader relationships, OfBusiness-type platforms | Bundled in procurement margins | Medium | Price intelligence + forward buying inside vertical procurement (O4) |
| P15 | Procurement: supplier discovery, reliability and credit at purchase | MSME procurement worth Rs 124.9 lakh cr; 30-40% digital; 75% spend Rs 10 lakh-1 cr/month (ISF sample) | Weekly | 37.6% struggle managing multiple suppliers; 33.4% lack dependable vendors; 35.6% face payment/credit constraints | Local traders, OfBusiness, Udaan, Moglix, Bizongo, Zetwerk, Infra.Market | OfBusiness FY25 revenue Rs 22,241 cr; Infra.Market Rs 18,472 cr; Zetwerk Rs 12,798 cr; Moglix FY24 Rs 4,964 cr | Medium-High (well-funded horizontals) | Vertical, cluster-specific procurement + embedded credit |
| P16 | Logistics cost penalty for small shippers | Manufacturers < Rs 5 cr turnover | Weekly | Logistics = 16.9% of output for firms < Rs 5 cr vs 7.6% for > Rs 250 cr (NCAER-DPIIT 2025) | Local transporters, aggregators (Shiprocket, Delhivery, Porter, BlackBuck) | Freight spend is large | Medium-High | Cluster freight pooling/aggregation; tied to procurement or export |
| P17 | Inventory management (stock-outs, dead stock) | Most stock-holding MSMEs | Daily | Working capital locked in slow stock (no India-wide measure) | Billing apps with inventory, Tally, Excel | Within billing/ERP spend | High | Feature, not company |
| P18 | Demand forecasting | Larger stock-holders | Monthly | Unmeasured | Experience, Excel | Negligible | Low | Feature inside procurement/inventory |
| P19 | Production planning and job tracking in job shops | Est. 1-2 lakh units with 10+ workers (low confidence) | Daily | Missed delivery dates, idle machines, WIP chaos (no India measurement) | Whiteboards, Excel, WhatsApp groups | Low; few buy MES | Low for MSME-grade products | WhatsApp-native production tracking (O10) |
| P20 | Machine downtime and low OEE | Subset of ~2.67 lakh ASI factories | Daily | Global benchmarks: typical discrete OEE ~60% vs 85% world-class (not India-measured) | Operator logs, OEM service | Low | Low (Indian IIoT vendors target large plants) | Low-cost clip-on sensors + WhatsApp alerts (O10) |
| P21 | Quality rejections and OEM supplier-quality requirements | Est. 50-80k component makers (low confidence) | Weekly | OEM debit notes and lost business (unmeasured) | Paper PPAP files, Excel, consultants | Consultants; some QMS software | Medium | Supplier-quality and traceability SaaS (O11) or module in O10 |
| P22 | High energy cost and inefficiency | Est. 1-1.6 lakh energy-intensive units (low confidence) | Continuous | Energy 15-40% of production cost in intensive clusters; 10-25% efficiency potential (BEE) | Discoms, diesel gensets, rooftop-solar EPCs, energy auditors | Large energy bills; C&I solar market | Medium (C&I solar players focus on larger customers) | Energy-as-a-service: rooftop solar (RESCO) + monitoring + retrofits financed from savings (O5) |
| P23 | Hiring skilled workers | ~25% of MSMEs cite lack of skilled manpower (SIDBI 2025) | Quarterly | Shortages of up to 35% in unskilled roles; costs +5-8% (industry reports) | Contractors, referrals, Apna, WorkIndia, ITIs | Job-posting and contractor fees | High | Cluster staffing with ITI pipelines (O16) |
| P24 | Training and upskilling workers | Broad | Occasional | Productivity loss (unmeasured) | Government-funded schemes, OEM programmes | Low (expects subsidy) | Medium | Weak standalone; buyer- or govt-funded |
| P25 | Attendance and wage payments for micro payroll | Large (part of 1.06 crore hired-worker establishments) | Daily | Small | Registers, PagarBook-type apps | Small | High | Avoid standalone |
| P26 | Finding international buyers (export discovery) | 1.73 lakh exporting MSMEs (FY25) + est. 1-2 lakh export-capable non-exporters | Monthly | MSME exports Rs 12.39 lakh cr (FY25); 45.8% share of exports | Trade fairs (EPC-subsidised), Alibaba.com, agents, Volza-type data | Fair costs, marketplace memberships, agent commissions | Medium | Managed export launchpad + buyer data + finance (O9) |
| P27 | Export documentation and compliance | 1.73 lakh exporting MSMEs | Per shipment | Delays, demurrage, missed incentives | CHAs, freight forwarders, in-house staff | Service fees | Medium-High | Bundle in O9 |
| P28 | Cross-border payment cost and forex conversion | 1.73 lakh MSME exporters + freelancers | Per invoice | Bank FX markups and fees | Banks, Skydo (40k+ exporters), BriskPe, Xflow, Wise, Payoneer | Large FX/fee pool | Very high (saturated) | Avoid |
| P29 | Trade finance for exporters | 1.73 lakh exporters | Per order | Pre/post-shipment finance gaps; EPM interest subvention 2.75% | Banks, Drip Capital, ECGC, EPM schemes | Interest and factoring fees | Medium | Partner, not build (lending licence) |
| P30 | EU CBAM and product carbon-footprint compliance | 3-4k direct + 25-30k indirect MSME exporters exposed (CleanCarbon est.) | Per shipment and annual declarations | Default values 30-80% above actual emissions; 15-22% price cuts needed (GTRI); orders cancelled | Consultants, global CBAM tools, buyers' templates | Emerging consulting and verification fees | Low-Medium (early) | CBAM/PCF data platform + managed verification for MSME exporters (O6) |
| P31 | ESG/BRSR value-chain data requests from large buyers | Est. 20-50k MSME suppliers in scope (low confidence) | Annual | Risk of delisting as supplier; voluntary FY26, assurance from FY27 | Buyer-provided questionnaires, consultants | Often buyer-paid | Medium (ESG SaaS targets the listed buyer) | Supplier ESG data module sold via buyers (O6) |
| P32 | Discovering and applying for government schemes | 97.3% unaware of digitalisation schemes (ISF); broad unawareness | Annual/one-off | Unclaimed subsidies and guarantees (unmeasured) | Consultants, bank staff, Haqdarshak, govt portals | Fragmented success fees | Medium | Scheme engine as a lead magnet; monetise via O7/O15 |
| P33 | Claiming state and central investment incentives | Unmeasured; PMEGP alone targets ~4 lakh projects over 5 years | One-off per project | Capital subsidy, SGST reimbursement, interest subvention often Rs 5 lakh-5 cr per claim (indicative) | Incentive consultants on success fee | Success fees (common practice; scale unmeasured) | Medium (fragmented consultants) | Incentive-claims-as-a-service (O7) |
| P34 | Winning public procurement (GeM/tenders) | 11 lakh+ MSEs registered on GeM | Weekly | MSMEs won 47% of GeM order value in FY26 (Rs 2.36 lakh cr) | Tender-info portals, consultants | Subscriptions and consultant fees | Medium-High | AI bid desk (O8) |
| P35 | Cybersecurity and payment fraud | ~3.1 crore internet-using establishments | Occasional | 47% of small businesses lost time/money to an incident (2025) | Antivirus, bank alerts | Low | Medium | Bundle with banking/insurance; weak standalone |
| P36 | Insurance protection gap | ~17% have any insurance (IRDAI-cited, low confidence) | Annual | Uninsured fire/stock/health losses | Agents, bank cross-sell | Premium pool (MSME share unmeasured) | Medium | Embedded distribution via SaaS partners (O13) |
| P37 | Loan documentation (CMA data, project reports) and credit readiness | Lakhs of applications/yr (PSB digital model: 3.96 lakh in 9 months) | Per application | Delays and rejections; CA fees per report (indicative Rs 5-25k) | CAs, DSAs, bank officers | CA/DSA fees | Medium | Automated CMA/DPR + lender matching (O15) |
| P38 | Owner dashboards / MIS | Broad | Weekly | Unmeasured | Tally reports, Excel | Low | Medium | Feature |
| P39 | Knowing how to adopt AI | 24% no AI use; 35% experimenting (D&B 2026) | Ongoing | Unmeasured | YouTube, vendors, consultants | Low | Medium | Deliver AI inside workflows (O1-O3), not as advice |
| P40 | Obtaining quality certifications (ISO, BIS, ZED) | Lakhs of manufacturers (unmeasured) | One-off with renewals | Needed to qualify as supplier | Certification consultants | Consultant fees | High (fragmented consultants) | Low priority |
| P41 | Legal recovery of overdue dues (MSEFC/ODR) | 2.57 lakh Samadhaan applications to Dec-2025; far more never file | Per dispute | Rs 55,244 cr filed; 52,744 applications (Rs 8,397 cr) not yet examined; new Act adds ODR and 90-day mediation | Lawyers, MSEFC filings | Legal fees | Low | Productised MSEFC/ODR filing (module of O1) |
| P42 | Bank and UPI reconciliation | ~1.5 crore GST filers | Daily | Unreconciled receipts cause GST and books errors | Accountants, Tally bank feeds | Within accounting spend | Medium-High | Feature of P05 |

## 5.4 Reading the results: problem ≠ business

- **Highest-scoring problems are about money moving**: getting customers (P09/P10), getting paid (P01/P41), getting compliant cheaply via the CA (P05), and getting credit (P02). These have **observable spend**, measured by IndiaMART, Justdial, TReDS, CA fees and Tally, plus **new regulatory or technology triggers**: the MSMED Amendment Act 2026, CBAM, the labour codes and LLM agents.
- **Big but weakly monetisable**: websites (P11), digital marketing (P12), training (P24), AI advice (P39), cybersecurity (P35), scheme discovery (P32). Many firms have these problems, but there is little evidence they pay to solve them.
- **High score but hard for a new entrant**: lead generation itself (P09; incumbents), credit (P02; capital + regulation), procurement (P15; ops + working capital). The opportunity is an *adjacent wedge*: conversion (O3), credit-readiness/embedded finance (O1, O15), or a vertical procurement desk (O4).
- **Small but urgent**: CBAM (P30). It affects few firms, but the pain is severe and buyers are concentrated and identifiable. It is a classic niche-to-platform entry.
