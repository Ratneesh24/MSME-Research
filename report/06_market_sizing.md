# 6. TAM / SAM / SOM for every serious opportunity

> Brief section 20. Data: `data/tam_sam_som.csv`; inputs in `scripts/msme_data/opportunities.py`.

**Conventions.**

- All values are **annual revenue to the startup in ₹ crore**, not customer spend or GMV (except where stated for O4).
- **TAM bottom-up** = theoretical customers × ARPU. **TAM top-down** = an observed spend or value pool × a plausible capture share.
- **SAM** = the segment the specific product can serve in its first geography and form.
- **SOM** = realistic **year-5 ARR** range (customers × ARPU).
- Where the two TAM methods diverge by more than 2×, the **lower** figure should be used for planning.

| ID | Opportunity | TAM bottom-up | Inputs | TAM top-down (low–high) | SAM | SOM yr-5 (low–high) | SOM inputs |
|---|---|---|---|---|---|---|---|
| O1 | AI receivables & collections copilot (AR-OS) for B2B MSMEs | 5,400 | 900,000 customers x Rs 60,000/yr | 3,670–8,100 | 1,800 | 36.0–72.0 | 6,000-12,000 customers x Rs 60,000/yr |
| O2 | AI copilot for CA firms (WhatsApp intake -> Tally posting -> GST/TDS reconciliation) | 1,200 | 100,000 customers x Rs 120,000/yr | 1,000–1,500 | 480 | 45.0–75.0 | 3,000-5,000 customers x Rs 150,000/yr |
| O3 | AI B2B sales agent on WhatsApp/voice (lead response, qualification, quotes, follow-up) | 4,800 | 1,000,000 customers x Rs 48,000/yr | 1,050–2,500 | 1,920 | 48.0–96.0 | 10,000-20,000 customers x Rs 48,000/yr |
| O4 | Vertical, cluster-focused procurement + embedded credit (one input category) | – | n/a (top-down only) | 62,000–124,000 | 1,200 | 48.0–96.0 | 2,000-4,000 customers x Rs 240,000/yr |
| O5 | Energy-as-a-service for MSME clusters (rooftop solar RESCO + monitoring + retrofits) | 14,625 | 130,000 customers x Rs 1,125,000/yr | 10,000–19,000 | 1,125 | 112–225 | 1,500-3,000 customers x Rs 750,000/yr |
| O6 | CBAM & product-carbon-footprint compliance for MSME exporters and suppliers | – | n/a (top-down only) | 450–750 | 360 | 15.4–28.8 | 800-1,500 customers x Rs 192,000/yr |
| O7 | Incentive & scheme claims-as-a-service (success fee) | 450 | 150,000 customers x Rs 30,000/yr | 300–600 | 125 | 10.0–25.0 | 2,000-5,000 customers x Rs 50,000/yr |
| O8 | AI bid desk for GeM and public tenders | 750 | 250,000 customers x Rs 30,000/yr | 600–800 | 216 | 18.0–28.8 | 5,000-8,000 customers x Rs 36,000/yr |
| O9 | Export launchpad for export-capable non-exporters (managed service + buyer data + finance) | 6,000 | 300,000 customers x Rs 200,000/yr | 1,500–3,000 | 300 | 12.0–24.0 | 600-1,200 customers x Rs 200,000/yr |
| O10 | WhatsApp-native shop-floor digitisation for job shops (production tracking + clip-on machine sensors) | 900 | 150,000 customers x Rs 60,000/yr | 600–1,200 | 240 | 12.0–24.0 | 2,000-4,000 customers x Rs 60,000/yr |
| O11 | Supplier-quality and traceability SaaS for auto/engineering tier-2/3 | 585 | 65,000 customers x Rs 90,000/yr | 300–900 | 180 | 7.2–13.5 | 800-1,500 customers x Rs 90,000/yr |
| O12 | Labour-code payroll & compliance managed service (10-200 employees) | 3,840 | 800,000 customers x Rs 48,000/yr | 2,000–4,000 | 960 | 24.0–38.4 | 5,000-8,000 customers x Rs 48,000/yr |
| O13 | Embedded MSME insurance distribution (fire, stock, marine, group health) | 1,125 | 5,000,000 customers x Rs 2,250/yr | 800–1,500 | 225 | 6.8–13.5 | 30,000-60,000 customers x Rs 2,250/yr |
| O14 | AI digital storefront (website + Google profile + catalogue) for micro manufacturers | 6,000 | 10,000,000 customers x Rs 6,000/yr | 300–800 | 1,200 | 12.0–24.0 | 20,000-40,000 customers x Rs 6,000/yr |
| O15 | Credit-readiness + lender marketplace (CMA/DPR automation on AA/GST data) | 1,350 | 300,000 customers x Rs 45,000/yr | 1,000–1,800 | 405 | 22.5–40.5 | 5,000-9,000 customers x Rs 45,000/yr |
| O16 | Cluster skilled-worker staffing with ITI pipelines | 800 | 1,000,000 customers x Rs 8,000/yr | 500–1,000 | 160 | 5.6–12.0 | 7,000-15,000 customers x Rs 8,000/yr |
| O17 | Micro-merchant bookkeeping/ledger app | 1,500 | 50,000,000 customers x Rs 300/yr | 100–300 | – | – | n/a |
| O18 | Cross-border payments for MSME exporters | – | n/a (top-down only) | 1,200–2,500 | – | – | n/a |
| O19 | Standalone MSME cybersecurity | 1,500 | 5,000,000 customers x Rs 3,000/yr | 200–600 | – | – | n/a |

## 6.1 Method notes and sanity checks

- **O1 Receivables.** Bottom-up (9 lakh × ₹60k = ₹5,400 cr) sits inside the top-down range (0.5–1.0% of the ₹7.34–8.1 lakh cr overdue stock = ₹3,670–8,100 cr). The two methods agree. SOM assumes 2–4% penetration of a 3-lakh-firm SAM in five years.
- **O2 CA copilot.** Two independent views converge on ~₹1,000–1,500 cr: per-firm (1 lakh firms × ₹1.2 lakh) and per-client (1.49 cr GST filers × 70% professional-served × ₹100–150/month). The market is modest but highly reachable, and each firm is a channel to 50–500 MSMEs.
- **O3 AI sales agent.** Bottom-up (₹4,800 cr) is ~2–4× the top-down (₹1,050–2,500 cr, as 30–50% of today's lead spend). **Use ~₹2,000 cr as the planning TAM.** The gap is the unproven assumption that firms will pay for conversion on top of leads.
- **O4 Procurement.** The take-rate pool is enormous (₹62,000–1,24,000 cr on ₹124.9 lakh cr of procurement × 25% category share × 2–4%). The binding constraints are working capital and operations, not demand. SOM: 2,000–4,000 buyers × ₹60 lakh GMV × 4% = ₹48–96 cr net revenue (₹1,200–2,400 cr GMV).
- **O5 Energy.** The TAM is infrastructure-like PPA revenue (1.3 lakh units × 150 kW × ₹75 lakh/MW-yr). It is low confidence because the count of energy-intensive units is unmeasured. SOM of 150–300 MW (₹112–225 cr revenue) needs ₹600–1,200 cr of project capital.
- **O6 CBAM.** A small, segment-summed TAM (~₹450–750 cr). SOM is ₹15–29 cr ARR, but the international expansion (every non-EU exporter of CBAM goods) and adjacent regulations (UK CBAM, product passports) widen it.
- **D-category items (O14, O17, O18, O19)** show large theoretical TAMs that observed revenues contradict. Khatabook earned ~₹103 cr (FY24) and OkCredit ₹23 cr (FY25) from crores of users. **Theoretical TAM is not evidence.**

## 6.2 What would make these numbers wrong

1. **ARPU assumptions** (₹48k–1.5 lakh/yr) are anchored on adjacent spend (IndiaMART ₹69k, Justdial ₹19k, WhatsApp BSPs ₹18–42k, CA software). Direct WTP for the specific product is untested.
2. **Customer counts above ₹5 cr turnover** rest on e-invoice GSTIN counts. These are GSTIN-level, so PAN-level counts may be 15–30% lower.
3. **Penetration rates** (1–5% of SAM in five years) are typical of Indian SMB SaaS but are not guaranteed.
