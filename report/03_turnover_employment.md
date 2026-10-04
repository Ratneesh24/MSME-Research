# 3. Turnover distribution, ability to pay, and employment

> Brief sections 5–6. Data: `data/turnover_distribution.csv`, `data/ability_to_pay_segments.csv`, `data/employment.csv`.

## 3.1 Classification limits are not observed turnover

The MSME definition (micro ≤ ₹10 cr turnover, small ≤ ₹100 cr, medium ≤ ₹500 cr, from 1-Apr-2025) sets **ceilings**. Almost every "micro" enterprise is far below its ceiling. Three official anchors show this:

1. **ASUSE 2025** (S01): ₹19.92 lakh crore GVA across 7.92 crore establishments, an **average GVA of about ₹2.5 lakh per establishment per year**. 86.6% are own-account units with no hired worker.
2. **GST, FY2024-25** (S13): **36.3% of GST registrants report turnover ≤ ₹5 lakh**. **More than 80% are below ₹1.5 crore** and together contribute under 7% of GST collections. Taxpayers above ₹500 crore are **0.10%** of the base but pay **50.3%** of GST cash.
3. **e-invoicing** (S14): only **8.56 lakh GSTINs** generated e-invoices in June 2026. E-invoicing is mandatory above ₹5 crore AATO, so this is the best observable count of firms above ₹5 crore (GSTIN-level, including large companies).

Udyam Bulletin VII (S10) adds that 88% of URP registrants in 2021 reported turnover below ₹1 crore. That group is more formal than the overall universe.

## 3.2 Estimated turnover distribution (all non-farm MSME establishments, ~8.0 crore)

Method:
- **≥ ₹5 crore**: a power law N(≥x) = N₅ · (x/5)^-α fitted through two anchors. The first is ~7.0 lakh firms ≥ ₹5 cr (PAN-level haircut of 8.56 lakh e-invoice GSTINs). The second is ~16,000 firms ≥ ₹500 cr (0.10% of GST taxpayers). This gives α ≈ 0.82, with ±25–30% bands for the GSTIN-vs-PAN mismatch.
- **Below ₹5 crore**: residuals from the GST slab shares and the ASUSE universe.

**Confidence is low below ₹1 crore and medium above ₹5 crore.**

| Turnover bracket | Estimated enterprises | Share of ~8.0 crore | Confidence | Main basis |
|---|---:|---:|---|---|
| < ₹10 lakh | 5.4–6.4 crore | ~74% | Low | ASUSE average GVA ₹2.5 lakh; 86.6% own-account; 36.3% of even GST registrants ≤ ₹5 lakh |
| ₹10–25 lakh | 0.8–1.4 crore | ~14% | Low | Residual; partly below the GST threshold (₹20/40 lakh) |
| ₹25 lakh–₹1 crore | 45–75 lakh | ~7.5% | Low | ~67–75 lakh GST registrants between ₹5 lakh and ₹1.5 cr |
| ₹1–5 crore | 20–30 lakh | ~3% | Low–Med | GST registrants ≥ ₹1.5 cr (15–20% of base) minus ≥ ₹5 cr |
| ₹5–10 crore | 2.3–3.9 lakh | 0.39% | Medium | Power-law fit |
| ₹10–25 crore | 1.6–2.7 lakh | 0.27% | Medium | " |
| ₹25–50 crore | 0.61–1.05 lakh | 0.10% | Medium | " |
| ₹50–100 crore | 0.34–0.60 lakh | 0.06% | Medium | " |
| ₹100–250 crore | 0.24–0.41 lakh | 0.04% | Medium | " |
| ₹250–500 crore | 0.09–0.16 lakh | 0.02% | Medium | " |
| ₹500 crore+ (large, not MSME) | ~15,000–17,000 | 0.02% | Medium | 0.10% of GST taxpayers |

Cross-check: Udyam small + medium (turnover > ₹10 cr **or** investment > ₹2.5 cr) = 5.28 lakh (S03). Our estimate of firms ≥ ₹10 cr is ~4 lakh (range 3.0–5.2 lakh). The two are consistent once investment-qualified small units are added.

## 3.3 Who can pay for B2B software and services?

| Segment | Approx. units | Typical monthly software/services budget | Buying behaviour | Attractiveness |
|---|---:|---|---|---|
| **Very small** (< ₹40 lakh) | 6.5–7.0 crore | ₹0–200 | Free apps; monetised through payments, credit or float; needs assisted onboarding | **Low for SaaS.** Khatabook (₹102.7 cr FY24 revenue) and OkCredit (₹23.3 cr FY25, loss ₹23 cr) show how hard this is to monetise (S47) |
| **Formal small** (₹40 lakh–₹1.5 cr) | 55–70 lakh | ₹300–1,500 | Pays CA ₹1–3k/month; buys billing app; WhatsApp-native | Medium: large but churn-prone. Reach through CAs and distributors |
| **Growing** (₹1.5–10 cr) | 17–25 lakh | ₹1,500–8,000 | Accountant or CA; Tally; buys leads (IndiaMART's average payer spends ~₹69k a year); owner decides | **High: best balance of count, pain and ability to pay** |
| **Established** (₹10–500 cr) | 3.5–5 lakh | ₹10,000–1,00,000+ | Finance and sales staff; ERP or Tally plus add-ons; ROI-driven | High ACV, smaller count. Best for receivables, compliance, energy, quality and CBAM |

Budgets are indicative, anchored on observed prices (IndiaMART ₹1,569 cr ÷ 2.28 lakh payers ≈ ₹69k a year; Justdial ₹1,214 cr ÷ 6.32 lakh campaigns ≈ ₹19k; WhatsApp BSPs ₹1.5–3.5k a month; S44, S45, S49). They need primary validation.

**Most attractive customer segment:** **B2B manufacturers and distributors with ₹2–100 crore turnover, ≈ 8–12 lakh firms.** That is ~8–12 lakh firms at ₹2–5 cr plus ~6.5 lakh at ₹5–100 cr, times a 60–70% B2B share (assumption). They have:
- **acute pain**: receivables, procurement, compliance, energy;
- **observed spending**: leads, CAs, Tally, consultants;
- **digital rails already**: GST, e-invoice, banking, WhatsApp;
- **geographic concentration**: about 30 industrial districts.

The very small segment is better served as *end-users of a channel* (CAs, banks, distributors) than as direct SaaS buyers.

## 3.4 Employment

| Metric | Value | Ref. | Source | Note |
|---|---:|---|---|---|
| Workers in unincorporated non-agri establishments | **12.81 crore** | 2025 | S01 | +74.52 lakh (+6.18%) vs 2023-24; excludes construction and companies |
| Workers per establishment | **1.62** | 2025 | derived | Most units are one- or two-person |
| GVA per worker | ₹1,56,539 | 2025 | S01 | +4.54% y/y; district range ₹1.0–2.72 lakh |
| Emolument per hired worker | ₹1,46,550 / yr | 2025 | S01 | +3.88% y/y |
| Women-owned proprietary establishments | 27% | 2025 | S01 | up from 26.2% |
| MSME employment, NSS | 11.10 crore | 2015-16 | S11 | Mfg 3.60 cr, trade 3.87 cr, services 3.63 cr |
| Udyam: employment reported by FY26 registrations | 8.04 crore | FY26 | S07 | Trading 2.98 cr, services 2.57 cr, mfg 2.50 cr; UP 1.18 cr leads |
| Udyam: cumulative claimed employment | 38+ crore | Jul-2026 | S08 | **Conflicts with ASUSE; not usable** |

- **Formal vs informal.** ASUSE units are unincorporated, and only 37.5% are registered under any Act (S01). An MSME-specific formal/informal employment split (PF/ESI coverage) was **not retrieved**. PLFS and EPFO data would be needed → *data unavailable*.
- **Skilled vs unskilled.** No MSME-wide split was retrieved → *data unavailable*.
- **Workforce problems (evidence).** About **one-fourth** of surveyed MSMEs cite lack of skilled manpower as a major challenge (SIDBI 2025, S67). Industry reports cite shortages of up to 35% in unskilled roles and 10–15% in technical roles, raising operating costs 5–8% (secondary). Retention problems are widely reported but **not measured**.
- **Regulatory change.** The four Labour Codes took effect on **21-Nov-2025** (S52). They consolidate 29 laws and introduce single registration, licence and return. Wage definitions change, and so do PF/gratuity bases. This creates a 12–24-month transition-compliance window for firms with 10+ workers.

### Do workforce problems make good startups?

| Workforce problem | Pain | Willingness to pay | Verdict |
|---|---|---|---|
| Hiring skilled workers (P23) | High | Low–Medium: MSMEs pay contractors, not platforms. Apna and WorkIndia already exist | **C**: only as cluster staffing tied to payroll |
| Training/upskilling (P24) | Medium | Low: expectation of subsidy | **C/D** |
| Payroll + labour-code compliance (P07) | Medium | Medium: consultants are paid today | **B** (O12): crowded, but the regulatory change is a trigger |
| Attendance/wages for micro (P25) | Low | Low | **D** |

**Conclusion.** The labour pain is real, but MSMEs pay for compliance and outcomes (a filled role, a clean inspection), not for HR software. Workforce opportunities rank below the finance, sales and procurement problems.
