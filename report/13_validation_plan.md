# 13. Primary research design and 30-day validation plan

> Brief sections 16 and 31. Instruments are in [`/instruments`](../instruments): interview guide, survey, qualification scorecard and response-coding template.
>
> **Status:** this study did **not** conduct interviews, and no responses are invented. Everything below is a ready-to-run plan.

## 13.1 Primary research design (50–100 MSMEs)

### Sample frame and quotas (target n = 80; minimum 50)

| Dimension | Quota |
|---|---|
| Sector | Engineering/auto components 20 · Textiles/apparel 12 · Food/agri-processing 10 · Chemicals/pharma 8 · Trading/distribution 15 · Services (B2B) 7 · Exporters (any sector, overlapping) ≥ 20 |
| Size (turnover) | < ₹1.5 cr: 15 · ₹1.5–10 cr: 35 · ₹10–100 cr: 25 · > ₹100 cr: 5 |
| Geography (≥ 4 states) | Gujarat (Rajkot/Ahmedabad/Surat) 20 · Punjab (Ludhiana/Mandi Gobindgarh) 15 · Tamil Nadu (Coimbatore/Tiruppur) 15 · Maharashtra (Pune) 15 · Uttar Pradesh/Delhi NCR 15 |
| Plus | **15 CA firms** (for O2) and **10 EU-exporting steel/aluminium firms** (for O6) |

**Recruitment (public, consent-based):**
- association meetings and introductions (`data/channel_partners_public.csv`);
- CA firms introducing clients (with the client's consent);
- publicly listed business contacts (company landlines/emails on official listings).

No scraping of personal data. Interviews are recorded only with consent. Comply with the Digital Personal Data Protection Act.

### Instruments
- **[Interview guide](../instruments/interview_guide.md)**: 45 minutes. Covers the brief's 20 questions plus problem-specific probes for O1/O2/O3/O6 and a past-behaviour focus ("tell me about the last time…").
- **[Survey](../instruments/survey_questionnaire.md)**: 12 minutes, WhatsApp/Google Form, in Hindi/Gujarati/Tamil/Punjabi/English. Quantifies pain frequency, time and money spent, current tools and willingness to pay at ₹500 / ₹2k / ₹5k / ₹10k / ₹25k a month.
- **[Qualification scorecard](../instruments/qualification_scorecard.md)**: decides who is a design partner.
- **[Coding template](../instruments/response_coding_template.csv)**: turns answers into scores for the problem database (`data/problem_scores.csv` columns WTP, severity, frequency, existing spend).

### Quantitative analysis plan
1. **Problem ranking.** Share of respondents naming each problem in their top 3 (unaided first, then aided). Report 95% confidence intervals; at n = 80 these are about ±10 points.
2. **Pain intensity.** Hours per week and ₹ per month per problem, with medians and inter-quartile ranges.
3. **Current spend.** Share already paying for any solution, and median monthly spend. This is the strongest WTP signal.
4. **WTP ladder.** Share willing at each price point. Discount stated WTP by ~50% (stated intent overstates payment).
5. **Segment cuts.** Size × sector × state. Test whether the "growing ₹1.5–10 cr" segment really has the highest pain × WTP.
6. **Update the scoring model.** Replace L-confidence scores with field data and re-run `scripts/build_datasets.py`.

## 13.2 30-day validation plan (for 2–3 opportunities: O1 + O2 together, O6, and optionally O3)

| Week | Goal | Activities | Output |
|---|---|---|---|
| **Week 1** | **Interview 20 MSMEs + 5 CA firms + 5 exporters** | Book via 3 associations and 3 CA firms. Run the interview guide. Daily debrief. Code the responses | First pain ranking; 10 candidate design partners; list of quotes |
| **Week 2** | **Interview another 30–50**; launch survey | Expand to 4 states. Survey to association WhatsApp groups (target 150+ responses). Landing pages live (one per opportunity, Hindi + English) | Quant pain/WTP data; landing-page conversion data; refined ICP |
| **Week 3** | **Build MVP prototypes for 2–3 opportunities** | O1: concierge collections (Tally export → WhatsApp reminders sent by the team, assisted by AI drafts) for 5 firms. O2: WhatsApp intake → draft Tally vouchers for 3 CA firms (AI + human). O6: manual CBAM calculation for 3 exporters using their bills. O3 (optional): agent on 1 firm's IndiaMART leads | Working prototypes; time/cost per customer to deliver |
| **Week 4** | **Acquire paying pilot customers** | Convert design partners to **paid** 60-day pilots (deposit or first-month fee). Run 2 acquisition experiments per opportunity | Paid pilots signed; CAC per channel; go/no-go per opportunity |

### MVPs (cheapest test of the riskiest assumption)

| Opp. | MVP | Riskiest assumption it tests |
|---|---|---|
| O1 | Concierge: we run their reminders for 30 days with AI drafts | Owners will let a third party message their debtors, and it **recovers cash** |
| O2 | Wizard-of-Oz: CA staff forward client docs to a WhatsApp number; we return Tally-ready vouchers within 24 h | CAs trust AI-drafted postings and will pay per client |
| O3 | Agent replies to one firm's live IndiaMART leads in 60 seconds, with owner approval for quotes | Faster vernacular reply **raises conversion** enough to pay ₹3–5k/month |
| O6 | Spreadsheet + expert: compute embedded emissions for 3 exporters' products; share with their EU importer | Exporters (or importers) pay ₹4–8 lakh/yr for verifier-ready data |

### Pricing experiments
1. **Van Westendorp** price-sensitivity questions in interviews (too cheap / cheap / expensive / too expensive).
2. **Real money**: offer three tiers on the pilot contract and record which tier is chosen. Require a **deposit or first-month payment** (₹2,000–25,000). A stated "yes" without payment does not count.
3. **Model test for O1:** SaaS-only vs SaaS + 2% success fee vs success-fee-only. Measure the uptake of each.
4. **Anchor test for O3:** price as a % of current IndiaMART/Justdial spend vs a flat fee.

### Landing-page experiment
One page per opportunity, Hindi + English, with WhatsApp click-to-chat as the CTA. Traffic comes from association broadcasts and ₹20–30k of targeted ads per page.
- **Metrics:** CTR, WhatsApp opt-in rate, demo bookings, pilot sign-ups.
- **Benchmark to beat:** ≥ 5% visitor → WhatsApp opt-in; ≥ 20% demo → pilot.

### Customer-acquisition experiments
| Channel | Experiment | Metric |
|---|---|---|
| CA firms | 2 ICAI/CPE-style sessions; referral offer | Pilots per session; CAC |
| Association | 1 member meeting per cluster with a live demo | Demo → pilot conversion |
| Outbound (O3) | 200 messages/calls to listed paid sellers in one category | Reply rate; pilot rate |
| EPC/importer (O6) | 1 workshop + 3 importer referrals | Pilots; willingness of importers to co-pay |

### Customer qualification criteria (design partner)
- **O1:** ≥ ₹5 cr turnover; ≥ 30 debtors; ≥ ₹50 lakh overdue > 60 days; uses Tally; owner reachable on WhatsApp.
- **O2:** CA firm with ≥ 5 staff and ≥ 100 GST clients; Tally-based.
- **O3:** pays for leads (any platform); ≥ 50 inbound leads/month; has a price list.
- **O6:** exports CBAM goods to the EU (directly or as a supplier); has electricity and fuel bills for 12 months.

The scorecard is in `/instruments/qualification_scorecard.md`.

### Success criteria (continue)
| Opp. | Day-30 bar |
|---|---|
| O1 | ≥ 5 paid pilots; pilot firms show ≥ 15% of targeted overdue recovered or a ≥ 10-day reduction in debtor days within 30 days; ≥ 40% of interviewees rate the pain ≥ 8/10 |
| O2 | ≥ 5 CA firms paying; ≥ 30% staff-time saving per client on measured tasks; ≥ 80% of AI-drafted vouchers accepted unchanged |
| O3 | ≥ 5 paid; first-response time < 2 min; ≥ 20% relative uplift in lead → quote conversion |
| O6 | ≥ 3 paid (or importer-paid) engagements at ≥ ₹2 lakh; a verifier confirms the methodology |

## 13.3 Kill criteria: evidence that should make us STOP an idea

| Opp. | Kill if… |
|---|---|
| **O1** | Fewer than 3 of 20 target firms will pay anything after seeing recovered-cash results. Or owners refuse third-party contact with debtors (relationship fear) in > 60% of cases. Or recovery uplift is indistinguishable from the owner's own follow-up |
| **O2** | CAs will not pay ≥ ₹3k/month after a 30-day pilot. Or AI posting accuracy stays < 85% after tuning. Or Tally integration is blocked |
| **O3** | Conversion uplift < 10% relative. Or monthly churn in pilots > 8%. Or IndiaMART announces an equivalent bundled feature at near-zero price |
| **O6** | EU importers accept supplier estimates without verification for 2026–27 (pain deferred). Or exporters will not pay ≥ ₹1 lakh/yr. Or verifiers reject MSME-grade data capture |
| **O4** | NBFC partner unavailable at ≤ 2.5% monthly loss-adjusted cost. Or gross margin < 2% after logistics in the pilot cluster |
| **O5** | No credit-enhancement partner. Or < 20% of interested units pass credit checks |
| **Any** | CAC in month 1–3 exceeds 12 months of gross profit per customer with no clear path to halve it |

## 13.4 The 3–5 assumptions that must be validated before starting the company

1. **Willingness to pay for outcomes, not software:** MSMEs (or their CAs) will pay a monthly fee or a success fee that maps to rupees recovered, orders won, hours saved or penalties avoided (O1, O2, O3, O6).
2. **Channel leverage:** CA firms and cluster associations can deliver customers at ≤ ₹50k CAC (≤ ₹1 lakh for O6) and will recommend a new vendor.
3. **Trust on WhatsApp:** owners will let an AI agent speak to *their* debtors and buyers under their brand, in their language, with owner approval only for exceptions.
4. **AI accuracy at MSME data quality:** extraction from poor phone photos and mixed-language chats reaches ≥ 85–90% accuracy with human review, at a cost that preserves ≥ 65% gross margin.
5. **(O6) Regulatory pull persists:** EU importers will demand verified supplier data, and default-value penalties will continue, through the 2026–2030 CBAM scope expansion.
