# 1. The Indian MSME universe: how many exist, and how many are really active

> Brief sections 1–2. Data: `data/msme_universe_funnel.csv`, `data/msme_size_distribution.csv`, `data/sector_msme.csv`, `data/subsector_count_vs_ability_to_pay.csv`. Source IDs (S01…) resolve in [15_sources.md](15_sources.md).

## 1.1 Why "India has X crore MSMEs" misleads

There are four official lenses on Indian MSMEs. Each counts something different:

| Lens | What it counts | Latest figure | Ref. date | Type | Source |
|---|---|---:|---|---|---|
| **Udyam Registration Portal (URP)** | Self-declared, PAN-linked registrations (all sizes, all sectors incl. construction and agri-allied) | 4.72 crore | 15-Mar-2026 | observed | S03 |
| **Udyam Assist Platform (UAP)** | Informal micro units registered by banks/NBFCs/MFIs ("designated agencies"); no GST/ITR | 3.21 crore | 15-Mar-2026 | observed | S03, S63 |
| **URP + UAP combined** | Cumulative registrations | **9.16 crore** | 31-Jul-2026 | observed (secondary report of official reply) | S06 |
| **ASUSE 2025 (NSO survey)** | *Operating* unincorporated non-agricultural establishments (manufacturing, trade, other services; **excludes construction and companies**) | **7.92 crore** | Jan–Dec 2025 | observed (survey estimate) | S01 |
| NSS 73rd round | Unincorporated non-agri MSMEs | 6.34 crore | 2015-16 | observed (outdated) | S11 |
| GST | Active GSTINs (all sizes) | 1.67 crore | 30-Jun-2026 | observed | S12 |
| MCA | Active companies + LLPs (all sizes) | 25.5 lakh | Feb-2026 | observed | S15 |
| ASI | Registered factories | 2.67 lakh | FY2024-25 | observed | S16 |

**Udyam growth is registration-driven, not business-formation-driven.** Cumulative registrations were 0.79 crore at end-FY22, 1.64 crore (FY23), 4.12 crore (FY24), 6.19 crore (FY25), 7.83 crore (28-Feb-2026) and 9.16 crore (31-Jul-2026) (S04, S06). That is roughly 18–19 lakh new registrations a month since April 2025. Business formation does not move that fast: ASUSE grew by 0.58 crore establishments over two survey rounds. The likely driver is UAP registrations made at loan origination (for example MUDRA, which ran 4.93 crore loan accounts in FY26, S26). Udyam has no mandatory annual re-validation, so closed units stay on the register.

**Conflict flagged: employment.** Udyam registrations collectively claim employment of **38+ crore** people (Jul-2026, S08). ASUSE 2025 counts **12.81 crore** workers in unincorporated non-farm establishments (S01). The Udyam figure is self-declared, cumulative, not de-duplicated, and includes construction and agri-allied units. **Treat it as a registration artefact, not employment.** This study uses ASUSE for employment.

## 1.2 Size composition

| Dataset (ref. date) | Micro | Small | Medium | Micro share |
|---|---:|---:|---:|---:|
| Udyam URP (15-Mar-2026) | 4,66,38,889 | 4,91,075 | 37,045 | 98.8% |
| Udyam UAP (15-Mar-2026) | 3,20,71,728 | – | – | 100% |
| **URP + UAP (15-Mar-2026)** | **7,87,10,617** | **4,91,075** | **37,045** | **99.33%** |
| Udyam URP, Bulletin VII (30-Sep-2021) | 47,73,266 | 2,74,009 | 31,742 | 93.98% |
| NSS 73rd round (2015-16) | 630.52 lakh | 3.31 lakh | 0.05 lakh | 99.47% |

Sources: S03, S10, S11. **Small + medium = 5.28 lakh enterprises**, about 0.7% of registrations. This group is the most commercially significant: it has the most employees, the highest B2B intensity and budgets. It is also small enough to identify and reach.

**Classification criteria (from 1-Apr-2025)**: micro ≤ ₹2.5 cr investment and ≤ ₹10 cr turnover; small ≤ ₹25 cr / ≤ ₹100 cr; medium ≤ ₹125 cr / ≤ ₹500 cr. Export turnover is excluded. These are *eligibility ceilings*, not observed sizes. Chapter 3 shows that the **observed** median micro establishment has turnover well below ₹10 lakh.

## 1.3 Active MSMEs: Registered → Potentially active → Commercially active → Digitally active

No official "active MSME" statistic exists. The estimate below is built from official counts that measure activity directly (survey operation, tax filing, e-invoicing). Every assumption is stated.

| Stage | Definition used | Count | Range | Type | Basis |
|---|---|---:|---|---|---|
| **1. Registered** | Udyam URP + UAP cumulative | **9.16 crore** | — | observed | S06 |
| **2. Potentially active** | Establishments operating during a reference year (non-farm, excl. construction) | **~8.0 crore** | 7.95–8.2 crore | estimate | ASUSE 7.92 crore (S01) + incorporated MSMEs, which ASUSE does not cover (subset of 25.5 lakh MCA entities, S15) |
| **3a. Commercially active – employing** | Has ≥1 hired worker | **1.06 crore** | — | observed | ASUSE hired-worker establishments (S01) |
| **3b. Commercially active – formal transacting** | GST-registered MSMEs filing regularly | **~1.38 crore** | 1.2–1.45 crore | estimate | 1.67 crore GSTINs (S12) × (1 – 8% multi-GSTIN duplication) × (1 – 10% irregular filers) – ~0.1% large firms. Duplication and non-filing rates are assumptions; GSTN earlier reported ~90% on-time GSTR-3B filing |
| **3c. Commercially significant** | Turnover ≥ ₹5 crore | **~6–7.5 lakh firms** | — | estimate | 8.56 lakh GSTINs generated e-invoices in Jun-2026 (S14); PAN-level is lower |
| **4a. Digitally connected** | Uses internet for business | **3.12 crore** | — | derived | 39.4% × 7.92 crore (S01) |
| **4b. Digitally operating** | Commercially active and runs billing/accounting software in-house | **~0.65 crore** | 0.5–0.8 crore | estimate (low confidence) | Vendor user claims (Tally, Vyapar 1m+, myBillBook 1m+ MAU, Busy, Marg, Zoho) with an overlap haircut. The 1.49 crore normal GST filers are a ceiling, and many of them file through a CA |
| 4c. Has a website | — | **~20–35 lakh** | — | estimate (low confidence) | Two-method triangulation, chapter 4 §10 |

```
Registered (Udyam)                 9.16 crore  ████████████████████████████████████████
Potentially active (operating)    ~8.0  crore  ███████████████████████████████████
Use internet for business          3.12 crore  █████████████▌
Commercially active (GST filing)  ~1.38 crore  ██████
  employ ≥1 hired worker           1.06 crore  ████▋
Digitally operating (software)    ~0.65 crore  ██▊
Turnover ≥ ₹5 crore             ~6–7.5 lakh    ▎
```

**Implication for a startup.** The practical B2B software and services market is not 9 crore. It is roughly:
- **~1.2–1.45 crore** GST-filing businesses, reachable mainly through CAs and billing apps;
- **~20–30 lakh** firms with ₹1.5 crore+ turnover that can pay for tools (chapter 3);
- **~6–7.5 lakh** firms above ₹5 crore that already transact digitally through e-invoicing. This last group is where most B2B SaaS revenue in India will come from in the next five years.

The 6.86 crore own-account establishments (86.6% of ASUSE units) have average GVA of only ₹2.5 lakh a year. For them, a product must be free or monetised indirectly (payments, credit), or delivered through someone else.

## 1.4 Sector structure: largest by count ≠ highest ability to pay

| Sector | Udyam share (27-Feb-2026) | Udyam count (derived on 7.83 cr) | Udyam FY26 reported jobs | NSS 2015-16 units | ASUSE 2025 GVA growth | Ability to pay |
|---|---:|---:|---:|---:|---:|---|
| Trading | 42.89% | 3.36 crore | 2.98 crore | 230.35 lakh (36%) | +16.77% | Low–Medium |
| Services | 36.22% | 2.84 crore | 2.57 crore | 206.85 lakh (33%) | +7.36% | Mixed |
| Manufacturing | 20.89% | 1.64 crore | 2.50 crore | 196.65 lakh (31%) | +8.52% | Medium–High |

Sources: S07 (shares and FY26 jobs), S11, S01. An older 2025 split (trading 3.19 crore, services 2.61 crore, manufacturing 1.54 crore on a 7.34 crore base) is consistent. ASUSE 2025 establishment growth was highest in other services (+10.29%), then manufacturing (+6.48%) and trade (+6.18%).

**Count vs ability to pay by NIC sub-sector.** Ranks are analyst judgement anchored on Udyam bulletins, ASUSE GVA per worker and observed software spend. Full table in `data/subsector_count_vs_ability_to_pay.csv`.

| Most numerous (count rank) | Highest ability to pay (value rank) |
|---|---|
| 1. Retail trade (NIC 47) | 1. Pharmaceuticals (21) |
| 2. Food & beverage services (56) | 2. Chemicals & dyes (20), auto components (29-30), electronics (26-27), IT & professional services |
| 3. Wholesale / distribution (46) | 3. Fabricated metals / engineering (25, 28), basic metals (24) |
| 4. Food products manufacturing (10), the most numerous manufacturing NIC | 5. Wholesale / distribution |
| 5. Textiles & apparel (13-14) | 6. Food products, textiles, transport, construction |

**Takeaway.** The sectors that dominate the count (retail, eateries, personal services) are mostly B2C, cash-heavy and low-margin. The sectors with ability to pay (engineering, chemicals, pharma, auto components, electronics, organised distribution) are a few lakh firms concentrated in identifiable clusters (chapter 2). **That concentration makes them reachable, so a B2B startup should target them first.**

## 1.5 Data gaps (explicit)

- No official count of *active* Udyam units, Udyam units with filed GST returns, or Udyam units with recent activity was retrieved. The Udyam–GST linkage exists administratively but is **not published**. → *data unavailable*.
- ASUSE excludes construction and incorporated firms, and Udyam includes both, so the two cannot be reconciled one-to-one.
- State-wise ASUSE 2025 tables and NIC-level Udyam counts exist on MoSPI and dashboard.msme.gov.in. They could not be downloaded from this environment (network policy) and should be pulled to refine chapter 2.
