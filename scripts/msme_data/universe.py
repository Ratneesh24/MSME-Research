"""MSME universe: funnel, size, sector, turnover, employment, digital adoption.

Units: counts are absolute numbers unless the column name says lakh/crore.
1 lakh = 100,000; 1 crore = 10,000,000.
"""

LAKH = 100_000
CRORE = 10_000_000

# ---------------------------------------------------------------------------
# 1. Funnel: Registered -> Potentially active -> Commercially active -> Digital
# ---------------------------------------------------------------------------
FUNNEL = [
    # stage, metric, value, ref_date, data_type, source_ids, notes
    dict(stage="1 Registered", metric="Udyam registrations, URP + UAP (cumulative)",
         value=9.16 * CRORE, ref_date="2026-07-31", data_type="observed", source_ids="S06",
         notes="Cumulative registrations since Jul-2020 (URP) and Jan-2023 (UAP). No mandatory annual "
               "re-validation, so closures are not netted out. 8.84 crore on 30-Jun-2026 (S05)."),
    dict(stage="1 Registered", metric="  of which Udyam Registration Portal (URP)",
         value=47_216_077, ref_date="2026-03-15", data_type="observed", source_ids="S03",
         notes="Self-declared, PAN/GST-linked registrations. Micro 4,66,38,889; small 4,91,075; medium 37,045."),
    dict(stage="1 Registered", metric="  of which Udyam Assist Platform (UAP), informal micro",
         value=32_071_728, ref_date="2026-03-15", data_type="observed", source_ids="S03;S63",
         notes="Created by banks/NBFCs/MFIs acting as designated agencies, typically at loan origination. "
               "These units have no GST/ITR. Treat as nano/household enterprises."),
    dict(stage="2 Potentially active", metric="Unincorporated non-agricultural establishments (ASUSE 2025)",
         value=7.92 * CRORE, ref_date="2025 (Jan-Dec)", data_type="observed", source_ids="S01",
         notes="Survey estimate of establishments operating in the reference period. Covers manufacturing, "
               "trade and other services and excludes construction, agriculture and incorporated companies. "
               "Own-account (no hired worker) 6.86 crore; hired-worker 1.06 crore."),
    dict(stage="2 Potentially active", metric="Active companies + LLPs (MCA)",
         value=2_552_715, ref_date="2026-02", data_type="observed", source_ids="S15",
         notes="All sizes. Most are small, but 'active' here means not struck off, not necessarily operating."),
    dict(stage="2 Potentially active", metric="Factories in ASI frame (registered manufacturing)",
         value=2.67 * LAKH, ref_date="FY2024-25", data_type="observed", source_ids="S16",
         notes="Overlaps with incorporated and unincorporated counts above."),
    dict(stage="2 Potentially active", metric="Estimated non-farm MSME universe, excluding construction",
         value=8.0 * CRORE, ref_date="2025-26", data_type="estimate", source_ids="S01;S15",
         notes="ASUSE 7.92 crore plus incorporated MSMEs, which are not in ASUSE; some MCA entities are "
               "dormant or large. Range 7.95-8.2 crore. Excludes construction and farm units."),
    dict(stage="3 Commercially active", metric="Active GST taxpayers (normal + composition)",
         value=16_714_646, ref_date="2026-06-30", data_type="observed", source_ids="S12",
         notes="Normal 1,48,70,332; composition 13,55,180; proprietorships 76.9%. GSTIN-level: one PAN can "
               "hold several GSTINs, and the count includes large firms."),
    dict(stage="3 Commercially active", metric="Hired-worker establishments (ASUSE 2025)",
         value=1.06 * CRORE, ref_date="2025", data_type="observed", source_ids="S01",
         notes="Unincorporated establishments employing at least one hired worker."),
    dict(stage="3 Commercially active", metric="Estimated GST-registered MSMEs filing regularly",
         value=1.38 * CRORE, ref_date="2026", data_type="estimate", source_ids="S12",
         notes="1.67 crore GSTINs x (1 - 8% multi-GSTIN duplication) x (1 - 10% irregular filers) minus "
               "about 0.1% large firms. Range 1.2-1.45 crore. The duplication and non-filing rates are our "
               "assumptions; the GSTR-3B on-time filing rate was reported at ~90% in earlier GSTN data."),
    dict(stage="3 Commercially active", metric="Estimated MSMEs with turnover >= Rs 5 crore (e-invoice generators)",
         value=8.56 * LAKH, ref_date="2026-06", data_type="observed", source_ids="S14",
         notes="GSTINs that generated e-invoices in Jun-2026; the e-invoice threshold is AATO > Rs 5 crore. "
               "Includes large companies (~16k GSTINs > Rs 500 cr). PAN-level count is lower, est. 6-7.5 lakh."),
    dict(stage="4 Digitally active", metric="Establishments using internet for business (ASUSE 2025: 39.4%)",
         value=round(0.394 * 7.92 * CRORE), ref_date="2025", data_type="derived", source_ids="S01",
         notes="39.4% x 7.92 crore. Up from 26.7% in ASUSE 2023-24."),
    dict(stage="4 Digitally active", metric="Estimated MSMEs using billing/accounting/GST software themselves",
         value=0.65 * CRORE, ref_date="2026", data_type="estimate", source_ids="S47;S12",
         notes="Range 0.5-0.8 crore, triangulated from vendor user claims (Tally, Vyapar 1m+, myBillBook "
               "1m+ MAU, Busy, Marg, Zoho), with heavy overlap, and the 1.49 crore normal GST filers, many "
               "of whom file through a CA without using software themselves. Low confidence."),
    dict(stage="4 Digitally active", metric="Estimated MSMEs with a website",
         value=27 * LAKH, ref_date="2025-26", data_type="estimate", source_ids="S55;S30",
         notes="Range 20-35 lakh. See website_presence.csv for the two-method triangulation."),
]

# ---------------------------------------------------------------------------
# 2. Enterprise size
# ---------------------------------------------------------------------------
SIZE_CRITERIA = [
    dict(category="Micro", investment_limit_cr=2.5, turnover_limit_cr=10, effective="2025-04-01",
         notes="Revised by Budget 2025-26 (earlier: Rs 1 cr investment / Rs 5 cr turnover)."),
    dict(category="Small", investment_limit_cr=25, turnover_limit_cr=100, effective="2025-04-01",
         notes="Earlier: Rs 10 cr / Rs 50 cr."),
    dict(category="Medium", investment_limit_cr=125, turnover_limit_cr=500, effective="2025-04-01",
         notes="Earlier: Rs 50 cr / Rs 250 cr. Classification uses both tests; exports are excluded from turnover."),
]

SIZE_DISTRIBUTION = [
    dict(dataset="Udyam URP", ref_date="2026-03-15", micro=46_638_889, small=491_075, medium=37_045, source_ids="S03"),
    dict(dataset="Udyam UAP", ref_date="2026-03-15", micro=32_071_728, small=0, medium=0, source_ids="S03"),
    dict(dataset="Udyam URP + UAP (classified)", ref_date="2026-03-15", micro=78_710_617, small=491_075, medium=37_045, source_ids="S03"),
    dict(dataset="Udyam URP (Bulletin VII)", ref_date="2021-09-30", micro=4_773_266, small=274_009, medium=31_742, source_ids="S10"),
    dict(dataset="NSS 73rd round (unincorporated)", ref_date="2015-16", micro=63_052_000, small=331_000, medium=5_000, source_ids="S11"),
]

# ---------------------------------------------------------------------------
# 3. Sector
# ---------------------------------------------------------------------------
SECTOR = [
    dict(sector="Trading", udyam_share_pct_feb2026=42.89, udyam_count_derived=round(0.4289 * 78_302_882),
         udyam_fy26_reported_employment_cr=2.98, nss73_enterprises_lakh=230.35, nss73_employment_lakh=387.18,
         asuse2025_gva_growth_pct=16.77, asuse2025_establishment_growth_pct=6.18,
         ability_to_pay="Low-Medium",
         notes="Largest count, working-capital heavy. SIDBI-Crisil credit gap highest at 33% for trading."),
    dict(sector="Services", udyam_share_pct_feb2026=36.22, udyam_count_derived=round(0.3622 * 78_302_882),
         udyam_fy26_reported_employment_cr=2.57, nss73_enterprises_lakh=206.85, nss73_employment_lakh=362.82,
         asuse2025_gva_growth_pct=7.36, asuse2025_establishment_growth_pct=10.29,
         ability_to_pay="Mixed",
         notes="Ranges from personal services (low) to IT, logistics and professional services (high)."),
    dict(sector="Manufacturing", udyam_share_pct_feb2026=20.89, udyam_count_derived=round(0.2089 * 78_302_882),
         udyam_fy26_reported_employment_cr=2.50, nss73_enterprises_lakh=196.65, nss73_employment_lakh=360.41,
         asuse2025_gva_growth_pct=8.52, asuse2025_establishment_growth_pct=6.48,
         ability_to_pay="Medium-High",
         notes="Smallest share by count but highest B2B intensity, capex and pain density (compliance, energy, quality)."),
]

# NIC sub-sector view: qualitative ranking of count vs ability to pay.
SUBSECTORS = [
    # name, nic, count_rank (1=most numerous), value_rank (1=highest ability to pay), evidence
    ("Retail trade (kirana, apparel, mobile, hardware)", "47", 1, 9, "Largest share of trading units; thin margins; B2C."),
    ("Food & beverage services (eateries, dhabas)", "56", 2, 10, "High count (Udyam bulletins); low B2B pay capacity."),
    ("Wholesale trade / distribution", "46", 3, 5, "Working-capital heavy; receivables-intensive; GST-registered."),
    ("Food products manufacturing", "10", 4, 6, "Most numerous manufacturing NIC in Udyam data; PMFME/ODOP focus."),
    ("Textiles & wearing apparel", "13-14", 5, 6, "Large clusters (Tiruppur, Surat, Ludhiana, Bhiwandi); export-linked."),
    ("Transport & logistics services", "49-52", 6, 7, "Fleet operators; fuel and receivables pain; ONDC/logistics."),
    ("Repair & personal services", "95-96", 7, 10, "High count, B2C, cash-heavy."),
    ("Fabricated metal products / engineering", "25,28", 8, 3, "B2B to OEMs; quality, energy and receivables pain."),
    ("Construction & specialised trades", "41-43", 9, 6, "Excluded from ASUSE; Udyam includes; project receivables."),
    ("IT & professional services", "62-63,69-74", 10, 2, "Higher margins and SaaS literacy; export services."),
    ("Chemicals & dyes", "20", 11, 2, "High GVA per unit; environmental compliance; CBAM-adjacent."),
    ("Pharmaceuticals", "21", 12, 1, "Regulated (GMP/Schedule M); quality-system spend; exports."),
    ("Auto components", "29-30", 13, 2, "Tier-2/3 suppliers; PPAP/quality; working capital to OEMs."),
    ("Electronics & electrical", "26-27", 14, 2, "PLI-linked growth; quality and component procurement."),
    ("Basic metals (re-rolling, castings, forging)", "24", 15, 3, "Energy-intensive; CBAM exposure for EU exporters."),
]

# ---------------------------------------------------------------------------
# 4. Turnover distribution (estimate) - see report chapter 03 for method
# ---------------------------------------------------------------------------
# Power-law fit for >= Rs 5 cr anchored on: N(>=5cr) ~ 7.0 lakh firms (PAN-level, from 8.56 lakh
# e-invoice GSTINs) and N(>=500cr) ~ 16,000 (0.10% of taxpayers, S13). Exponent a = ln(43.75)/ln(100).
import math

N5 = 7.0 * LAKH
N500 = 16_000
ALPHA = math.log(N5 / N500) / math.log(100)


def n_at_least(x_cr: float) -> float:
    """Firms with turnover >= x crore for x >= 5 (power-law interpolation)."""
    return N5 * (x_cr / 5.0) ** (-ALPHA)


def _bracket(lo, hi):
    hi_n = n_at_least(hi) if hi else 0
    return n_at_least(lo) - hi_n


_upper = [
    ("Rs 5-10 cr", 5, 10), ("Rs 10-25 cr", 10, 25), ("Rs 25-50 cr", 25, 50),
    ("Rs 50-100 cr", 50, 100), ("Rs 100-250 cr", 100, 250), ("Rs 250-500 cr", 250, 500),
]

TURNOVER = [
    dict(bracket="< Rs 10 lakh", est_low=5.4 * CRORE, est_high=6.4 * CRORE, confidence="Low",
         basis="ASUSE 2025 average GVA per establishment is only Rs 2.5 lakh (Rs 19.92 lakh cr / 7.92 cr), "
               "and 86.6% of establishments are own-account. Only ~1.49 crore units are normal GST filers "
               "against a Rs 20-40 lakh registration threshold, and 36.3% of GST registrants themselves report "
               "turnover <= Rs 5 lakh (S13)."),
    dict(bracket="Rs 10-25 lakh", est_low=0.8 * CRORE, est_high=1.4 * CRORE, confidence="Low",
         basis="Residual of the ASUSE universe after the GST-registered upper tail; partly below the GST threshold."),
    dict(bracket="Rs 25 lakh-1 cr", est_low=0.45 * CRORE, est_high=0.75 * CRORE, confidence="Low",
         basis="GST registrants between Rs 5 lakh and Rs 1.5 cr number ~67-75 lakh (80-85% below Rs 1.5 cr minus "
               "36.3% below Rs 5 lakh, S13); this band is a share of that."),
    dict(bracket="Rs 1-5 cr", est_low=0.20 * CRORE, est_high=0.30 * CRORE, confidence="Low-Medium",
         basis="GST registrants >= Rs 1.5 cr are 15-20% of ~1.53 crore (23-31 lakh) minus ~8.6 lakh >= Rs 5 cr; "
               "the Rs 1-1.5 cr band was added."),
]
for label, lo, hi in _upper:
    mid = _bracket(lo, hi)
    TURNOVER.append(dict(bracket=label, est_low=round(mid * 0.75), est_high=round(mid * 1.3), confidence="Medium",
                         basis=f"Power-law interpolation (alpha={ALPHA:.2f}) between e-invoice anchor (>= Rs 5 cr) "
                               f"and GST slab share >= Rs 500 cr; point estimate {round(mid):,}. +/-25-30% for "
                               "GSTIN vs PAN mismatch."))
TURNOVER.append(dict(bracket="Rs 500 cr+ (not MSME)", est_low=15_000, est_high=17_000, confidence="Medium",
                     basis="0.10% of active GST taxpayers (S13); they pay 50.3% of GST cash."))

ABILITY_TO_PAY = [
    dict(segment="Very small (turnover < Rs 40 lakh)", approx_units="6.5-7.0 crore", typical_monthly_software_budget="Rs 0-200",
         buying_behaviour="Free apps; pays via lending, payments or float; needs assisted onboarding",
         attractiveness="Low for SaaS; viable only for fintech/payments distribution models"),
    dict(segment="Formal small (Rs 40 lakh-1.5 cr)", approx_units="55-70 lakh", typical_monthly_software_budget="Rs 300-1,500",
         buying_behaviour="Pays CA Rs 1-3k/month; buys billing app (Rs 2-5k/yr); WhatsApp-native",
         attractiveness="Medium: large but churn-prone; sell through CAs and distributors"),
    dict(segment="Growing (Rs 1.5-10 cr)", approx_units="17-25 lakh", typical_monthly_software_budget="Rs 1,500-8,000",
         buying_behaviour="Accountant on payroll or CA; Tally; buys leads (IndiaMART/Justdial); owner decides",
         attractiveness="High: best balance of count, pain and ability to pay"),
    dict(segment="Established (Rs 10-500 cr)", approx_units="3.5-5 lakh", typical_monthly_software_budget="Rs 10,000-1,00,000+",
         buying_behaviour="Finance and sales staff; ERP or Tally+add-ons; evaluates ROI; some procurement process",
         attractiveness="High ACV, lower count; best for compliance, receivables, energy and quality"),
]

# ---------------------------------------------------------------------------
# 5. Employment
# ---------------------------------------------------------------------------
EMPLOYMENT = [
    dict(metric="Workers in unincorporated non-agri establishments (ASUSE 2025)", value=12.81 * CRORE,
         ref="2025", data_type="observed", source_ids="S01",
         notes="Added 74.52 lakh jobs (+6.18%) over ASUSE 2023-24. Excludes construction and incorporated firms."),
    dict(metric="Workers per establishment (ASUSE 2025)", value=round(12.81 / 7.92, 2), ref="2025",
         data_type="derived", source_ids="S01", notes="12.81 crore / 7.92 crore."),
    dict(metric="GVA per worker, Rs (ASUSE 2025)", value=156_539, ref="2025", data_type="observed", source_ids="S01",
         notes="+4.54% y/y. District range ~Rs 1.0 lakh (Murshidabad) to Rs 2.72 lakh (Rangareddy)."),
    dict(metric="Emolument per hired worker, Rs/year (ASUSE 2025)", value=146_550, ref="2025", data_type="observed",
         source_ids="S01;S02b", notes="+3.88% y/y; Dehradun ~Rs 4.64 lakh vs ~Rs 80k in parts of Bihar/Jharkhand."),
    dict(metric="Women-owned proprietary establishments (share)", value=0.27, ref="2025", data_type="observed",
         source_ids="S01", notes="Up from 26.2% in 2023-24."),
    dict(metric="MSME employment, NSS 73rd round", value=11.10 * CRORE, ref="2015-16", data_type="observed",
         source_ids="S11", notes="Manufacturing 3.60 cr, trade 3.87 cr, other services 3.63 cr."),
    dict(metric="Udyam: employment reported by registrations made in FY2025-26", value=8.04 * CRORE, ref="FY2025-26",
         data_type="observed", source_ids="S07",
         notes="Self-declared at registration. FY25: 6.91 cr; FY24: 5.45 cr. Trading 2.98 cr, services 2.57 cr, mfg 2.50 cr."),
    dict(metric="Udyam: cumulative employment claimed by all registrations", value=38 * CRORE, ref="Jul-2026",
         data_type="observed", source_ids="S08",
         notes="CONFLICT: ~3x ASUSE's 12.81 crore. Self-declared, cumulative, not de-duplicated, and includes "
               "construction/agri-allied units. Do NOT use as current employment."),
]

UDYAM_EMPLOYMENT_FY26_STATES = [
    ("Uttar Pradesh", 118.0), ("Maharashtra", 67.97), ("Tamil Nadu", 61.47), ("Telangana", 60.56),
    ("Bihar", 55.54), ("Karnataka", 50.87), ("Andhra Pradesh", 36.66),
]

# ---------------------------------------------------------------------------
# 6. Digital adoption indicators
# ---------------------------------------------------------------------------
DIGITAL = [
    dict(indicator="Establishments using internet for business", value_pct=39.4, universe="ASUSE 2025 (7.92 cr unincorporated)",
         ref="2025", source_ids="S01", confidence="High", notes="26.7% in ASUSE 2023-24."),
    dict(indicator="Maintain account with a financial institution", value_pct=82.5, universe="ASUSE 2025",
         ref="2025", source_ids="S01", confidence="High", notes="76.1% in ASUSE 2023-24."),
    dict(indicator="Registered under any Act/authority", value_pct=37.5, universe="ASUSE 2025",
         ref="2025", source_ids="S01", confidence="High", notes="37.2% previously; i.e. ~62% fully informal."),
    dict(indicator="Used computers for business: hired-worker establishments", value_pct=23.6, universe="ASUSE (earlier round)",
         ref="2023-24", source_ids="S01", confidence="Medium", notes="3% for own-account establishments."),
    dict(indicator="Adopted at least one digital tool", value_pct=53.8, universe="ISF survey, 7,835 MSMEs (registered-skewed)",
         ref="2024-25", source_ids="S30", confidence="Medium", notes="46.2% fully offline."),
    dict(indicator="Unaware of any government digitalisation scheme", value_pct=97.3, universe="ISF survey",
         ref="2024-25", source_ids="S30", confidence="Medium", notes=""),
    dict(indicator="Find it difficult to find the right digital tools", value_pct=52.6, universe="ISF survey",
         ref="2024-25", source_ids="S30", confidence="Medium", notes=""),
    dict(indicator="Accept digital payments", value_pct=90, universe="SIDBI-Crisil, 2,097 MSMEs",
         ref="2025", source_ids="S17", confidence="Medium", notes=""),
    dict(indicator="Used digital lending platforms", value_pct=18, universe="SIDBI-Crisil", ref="2025", source_ids="S17",
         confidence="Medium", notes=""),
    dict(indicator="Rely on traditional marketing", value_pct=70, universe="SIDBI-Crisil", ref="2025", source_ids="S17",
         confidence="Medium", notes=""),
    dict(indicator="Actively use digital marketing or e-commerce", value_pct=13, universe="ISF/SIDBI coverage", ref="2025",
         source_ids="S30;S17", confidence="Medium", notes=""),
    dict(indicator="Have a website or web page", value_pct=19, universe="Survey cited in ICRIER/ISF materials (registered MSMEs)",
         ref="2024-25", source_ids="S32;S30", confidence="Low", notes="A 2026 secondary source claims 35%; unverified."),
    dict(indicator="Share of procurement spend via digital channels", value_pct=35, universe="ISF, 27,000+ Udyam MSMEs",
         ref="2026", source_ids="S31", confidence="Medium", notes="Reported 30-40%."),
    dict(indicator="Integrated AI tools into operations", value_pct=25, universe="Vi Business study", ref="2026",
         source_ids="S33", confidence="Low", notes="D&B: 24% none, 35% experimenting, 37% automating tasks, 5% AI core."),
    dict(indicator="Lost time/money to a cyber incident in last 12 months", value_pct=47, universe="Small businesses survey",
         ref="2025", source_ids="S43", confidence="Low-Medium", notes="APAC average 37%."),
    dict(indicator="Have any insurance", value_pct=17, universe="IRDAI-cited study", ref="undated", source_ids="S42",
         confidence="Low", notes=""),
]

DIGITAL_LEVELS = [
    dict(level="L0 Offline", definition="No internet use for business; cash/UPI on personal phone at most",
         est_low=4.6 * CRORE, est_high=4.9 * CRORE, basis="(1-39.4%) x 7.92 cr ASUSE + few incorporated", confidence="Medium"),
    dict(level="L1 WhatsApp + digital payments", definition="Business WhatsApp/UPI QR, no accounting software",
         est_low=2.2 * CRORE, est_high=2.6 * CRORE, basis="Internet users (3.12 cr) minus L2+", confidence="Low-Medium"),
    dict(level="L2 Accounting/GST software", definition="Billing/accounting app or Tally used in-house",
         est_low=0.5 * CRORE, est_high=0.8 * CRORE, basis="Vendor user claims with overlap haircut; GST normal filers 1.49 cr as ceiling",
         confidence="Low"),
    dict(level="L3 Multiple SaaS tools", definition="Billing + CRM/WhatsApp API/HR/e-commerce/paid lead platforms",
         est_low=10 * LAKH, est_high=20 * LAKH,
         basis="IndiaMART 2.28 lakh payers; Justdial 6.3 lakh campaigns; AiSensy 2.1 lakh accounts; 8.56 lakh e-invoice GSTINs",
         confidence="Low"),
    dict(level="L4 Integrated ERP", definition="ERP integrating finance, inventory, production, sales",
         est_low=1 * LAKH, est_high=2.5 * LAKH, basis="Medium (37k) + upper-small Udyam units; ASI factories 2.67 lakh as ceiling",
         confidence="Low"),
    dict(level="L5 AI/data-driven", definition="AI or analytics core to operations",
         est_low=10_000, est_high=30_000, basis="~5% 'AI core' in D&B sample applied to L3-L4 base with downward bias correction",
         confidence="Very low"),
]

WEBSITE_PRESENCE = [
    dict(method="A. Domain supply side",
         steps=".IN ~4.2m domains (S55); assume .IN is 35-50% of Indian-registrant domains -> 8.4-12m; "
               "assume 30-40% host an active business site -> 2.5-4.8m; MSME share 85-90%",
         est_low=21 * LAKH, est_high=43 * LAKH, confidence="Low",
         key_assumptions=".IN share of Indian registrations; active-site share; MSME share"),
    dict(method="B. Survey side",
         steps="19% of surveyed (registered-skewed) MSMEs report a website (S32/S30); apply to 1.06 cr hired-worker "
               "establishments (20 lakh) and to 1.49 cr GST normal filers (28 lakh)",
         est_low=20 * LAKH, est_high=28 * LAKH, confidence="Low-Medium",
         key_assumptions="Survey sample representative of GST-registered MSMEs"),
    dict(method="Triangulated",
         steps="Overlap of A and B",
         est_low=20 * LAKH, est_high=35 * LAKH, confidence="Low-Medium",
         key_assumptions="~2.5-4.5% of 8 crore establishments; ~15-25% of GST-registered MSMEs"),
]
