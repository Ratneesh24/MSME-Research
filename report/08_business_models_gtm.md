# 8. Business models, unit economics and customer acquisition

> Brief sections 23–24. Data: `data/unit_economics.csv`; inputs in `scripts/msme_data/opportunities.py`. All economics below are **assumption ranges to validate**. They are not observed results.

## 8.1 Recommended business model per opportunity

| ID | Primary model | Secondary revenue | Why this model |
|---|---|---|---|
| O1 Receivables | SaaS (₹2–6k/month) | Success fee 1–3% on recovered dues > 90 days; financing referral (TReDS/NBFC) | Aligns price with cash recovered; finance earns more than SaaS once invoices flow through |
| O2 CA copilot | Per-firm SaaS tiered by client count (₹3k–50k/month) | Per-client usage; partner revenue from O1/O15 cross-sell | CAs already budget for software; usage scales with clients |
| O3 Sales agent | SaaS + conversation usage (₹2.5–8k/month) | Performance tier (per qualified lead) | Directly comparable with existing lead spend |
| O4 Procurement | Trading margin (2–5% of GMV) | Credit spread/referral; logistics | Proven by OfBusiness; margin funds field operations |
| O5 Energy | PPA/lease (10–25 years) | Monitoring SaaS; shared savings; carbon credits | Infrastructure economics; MSME pays from savings |
| O6 CBAM/carbon | Annual subscription (₹0.6–8 lakh) | Verification coordination; abatement projects (O5) | Recurring regulatory obligation |
| O7 Incentive claims | Success fee 3–8% | Filing fees | Customers pay only on benefit received |
| O8 GeM bid desk | Subscription (₹2–5k/month) | Optional success fee 0.5% of awarded value | Bidders bid continuously |
| O9 Export launchpad | Retainer (₹1–3 lakh/yr) | Success commission 2–5% of first-year exports; finance/logistics referrals | Outcome uncertainty needs shared risk |
| O10 Shop-floor | Hardware at near-cost + SaaS per machine | Energy and quality modules | Analog: Guidewheel per-sensor pricing |
| O12 Payroll/compliance | Per-employee managed service | Insurance and hiring add-ons | Buyers want done-for-you |
| O15 Credit marketplace | Lender commission 0.75–1.5% | Report fees (₹5–15k) | DSA economics, with CA origination lowering CAC |

## 8.2 Unit economics (ranges)

LTV = ARPU × gross margin ÷ annual churn. Payback = CAC ÷ monthly gross profit per customer.

| ID | ARPU ₹/yr | Gross margin | CAC ₹ (low–high) | Annual churn | LTV ₹ | LTV/CAC | Payback (months) | Notes |
|---|---|---|---|---|---|---|---|---|
| O1 | 60,000 | 75% | 25,000–45,000 | 30% | 150,000 | 3.3–6.0 | 6.7–12.0 | Channel-led via CA firms/associations; success fees lift ARPU in year 1 |
| O2 | 150,000 | 80% | 40,000–80,000 | 18% | 666,667 | 8.3–16.7 | 4.0–8.0 | CA firms are sticky once client data lives in the tool |
| O3 | 48,000 | 62% | 20,000–35,000 | 40% | 74,400 | 2.1–3.7 | 8.1–14.1 | SMB SaaS churn; must prove conversion uplift monthly |
| O4 | 240,000 | 30% | 15,000–30,000 | 25% | 288,000 | 9.6–19.2 | 2.5–5.0 | ARPU = 4% take on Rs 60 lakh/yr buyer GMV; GM = contribution after logistics and credit cost |
| O5 | 750,000 | 45% | 150,000–300,000 | 4% | 8,437,500 | 28.1–56.2 | 5.3–10.7 | Per 100 kW site; 10-25 yr contracts; capex not in CAC |
| O6 | 192,000 | 68% | 50,000–150,000 | 12% | 1,088,000 | 7.3–21.8 | 4.6–13.8 | Regulatory recurrence keeps churn low |
| O7 | 50,000 | 55% | 10,000–25,000 | 80% | 34,375 | 1.4–3.4 | 4.4–10.9 | Mostly one-off claims; repeat only on new investments |
| O8 | 36,000 | 75% | 12,000–25,000 | 35% | 77,143 | 3.1–6.4 | 5.3–11.1 |  |
| O9 | 200,000 | 45% | 60,000–120,000 | 35% | 257,143 | 2.1–4.3 | 8.0–16.0 | Service-heavy |
| O10 | 60,000 | 58% | 40,000–80,000 | 20% | 174,000 | 2.2–4.3 | 13.8–27.6 | Hardware sold at near cost |
| O12 | 48,000 | 52% | 20,000–40,000 | 20% | 124,800 | 3.1–6.2 | 9.6–19.2 |  |
| O15 | 45,000 | 65% | 10,000–20,000 | 50% | 58,500 | 2.9–5.8 | 4.1–8.2 | Per disbursal; repeat via renewals/top-ups |

**How to read this:**
- **O2 and O6 have the strongest modelled economics:** low churn, high gross margin and a reachable buyer community.
- **O1** is healthy if churn stays near 30%/yr and success fees materialise.
- **O3** is the most fragile (LTV/CAC 2–4). It works only if the agent proves conversion uplift every month, because SMB SaaS churn in India is high.
- **O4 and O5** look excellent on LTV/CAC but are **capital businesses**. Working capital (O4) and project capex (O5) dominate, and CAC ratios hide that.
- **O7** (one-off claims) and **O10** (hardware-heavy payback of 14–28 months) are weak as standalone ventures.

## 8.3 Customer acquisition: how to win the first 100 customers

### Channels compared (cheapest realistic first)

| Channel | Reach | Cost | Trust | Best for | Notes |
|---|---|---|---|---|---|
| **CA firms** (98,967 firms, S51) | Each serves 50–500 MSMEs | Low (revenue share/referral) | **Very high** | O1, O2, O7, O12, O15 | Selling *to* CAs (O2) creates the channel for everything else |
| **Industry/cluster associations** (`data/channel_partners_public.csv`, 95 bodies) | Hundreds to thousands of members per cluster | Low–Medium (sponsor meetings, member pricing) | High | O1, O3, O4, O5, O6, O10 | Rajkot Engineering Association, CICU Ludhiana, CODISSIA, Morbi Ceramic, AIIFA, EEPC |
| **Lead-platform seller lists** (IndiaMART/Justdial paid sellers are publicly listed businesses) | 2–6 lakh lead buyers | Low (targeted outbound) | Medium | O3 | Contact via business listings only; respect platform terms and DPDP |
| **Export promotion councils** | Exporter members | Low | High | O6, O9 | EEPC for steel/engineering (CBAM); FIEO |
| **TReDS platforms / banks / NBFCs** | Sellers already onboarded | Medium (partnership) | High | O1, O15 | Integrate as finance rails; co-marketing |
| **Tally partner network** | Tally resellers/implementers across India | Medium (rev-share) | High with MSMEs | O2, O1 | Ships Tally connectors with the product |
| **WhatsApp communities / YouTube (vernacular)** | Large | Low | Medium | O2 (CA groups), O3 | Content-led demand; slow but compounding |
| **Field sales in clusters** | Dense | Medium–High | High | O4, O5, O10 | Needed for operations-heavy products |
| **LinkedIn / paid digital** | Mid-market only | High for MSMEs | Low | O6 (exporters), O2 | Supplementary |
| **Government agencies** (MSME-DFOs, DICs, BEE) | Broad | Low, but slow | High | O5, O6, O7, O9 | Workshops and demo days, not sales |

**Cheapest realistic channel overall: CA firms, plus one dense cluster association.** Both are trusted, concentrated and already in the MSME's money and compliance workflow.

### First 100 customers by opportunity

| Opp. | First 10 | 10 → 100 | Why it is cheap |
|---|---|---|---|
| **O1** | 10 engineering firms in Rajkot via the Rajkot Engineering Association + 3 local CA firms. Concierge pilot: run their collections for 30 days | Association endorsement + "₹X recovered" case studies; 10 CA partners each bringing 5–10 clients; integrate one TReDS platform | Pain is acute and measurable in rupees recovered |
| **O2** | 10 CA firms (5–20 staff) in Ahmedabad/Pune via ICAI branch CPE talks; free 30-day pilot on their 10 largest clients' data | CA WhatsApp/Telegram groups, referral credits, a Tally partner, 2–3 ICAI branch seminars a month | Tight professional community; word-of-mouth |
| **O3** | 10 IndiaMART-paying manufacturers in Ludhiana/Rajkot reached by outbound; agent switched on for their incoming leads in 48 hours | Category-specific case studies ("reply time 4 h → 60 s; conversion +X%"); IndiaMART/Justdial integration; reseller partners | Buyers already pay for leads and feel the leakage |
| **O6** | 10 steel/engineering exporters via EEPC/AIIFA workshops in Ludhiana and Mandi Gobindgarh | EU importer referrals; bank trade-finance desks; verifier partnerships | Regulation-driven urgency |
| **O4** | One cluster desk (e.g., yarn in Surat) serving 10 weavers at small tickets on 30-day credit via NBFC partner | Association MoU, trader-turned-agents, price-alert WhatsApp broadcasts | Volatility and credit pain are shared across the cluster |
| **O5** | 2–3 demonstration plants in Morbi or a foundry cluster with association co-branding | Pooled credit enhancement, discom data, bank partners | Visible savings sell themselves within a cluster |

**Kill-switch for acquisition.** If the first 100 customers cannot be won at ≤ ₹50k all-in CAC (≤ ₹1 lakh for O6, field-cost-based for O4/O5) within six months of MVP, the channel thesis is wrong (see chapter 13).
