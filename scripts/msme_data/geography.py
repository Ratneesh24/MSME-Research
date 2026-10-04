"""State and district data.

Column provenance:
  udyam_urp            URP-only registrations (DataRankIndia compilation of Udyam portal, 2026)  [S09]
  udyam_urp_uap_feb26  URP + UAP as on 28-Feb-2026, PIB Annexure-I                              [S04]
  udyam_total_other    URP + UAP from other 2026 secondary reports - dates unclear, verify      [S09/S05]
  udyam_emp_fy26_lakh  Employment reported by FY2025-26 Udyam registrations                    [S07]
  nss73_lakh           Estimated MSMEs, NSS 73rd round 2015-16 (top-10 states only published)   [S11]
  asuse2324_lakh       ASUSE 2023-24 establishments (only 3 states retrieved)                   [S64]
  pop2026_cr           Projected population 1-Jul-2026                                          [S58]
  exports_fy25_usd_bn  Merchandise exports FY2024-25 (all firms, not MSME-only)                 [S70]
None = data not retrieved / unavailable (never imputed).
"""

STATES = [
    # name, region, urp, urp_uap_feb26, total_other, emp_fy26_lakh, nss73_lakh, asuse2324_lakh, pop2026_cr, exports_bn
    ("Maharashtra", "West", 7_336_363, 10_144_478, None, 67.97, 47.78, 60.97, 12.96, 65.9),
    ("Uttar Pradesh", "North", 4_977_996, 8_603_272, None, 118.0, 89.99, 93.83, 24.35, 22.0),
    ("Tamil Nadu", "South", 4_155_776, None, 6_240_000, 61.47, 49.48, None, 7.90, 52.1),
    ("Rajasthan", "North", 3_157_377, 4_446_338, None, None, 26.87, None, 8.39, None),
    ("Gujarat", "West", 3_028_267, 4_369_973, None, None, 33.16, None, 7.43, 116.3),
    ("Karnataka", "South", 2_605_682, 4_991_314, None, 50.87, 38.34, None, 7.08, 30.5),
    ("Madhya Pradesh", "Central", 2_403_832, 4_827_725, None, None, 26.74, None, 9.00, None),
    ("West Bengal", "East", 2_175_295, 5_310_326, None, None, 88.67, 92.68, 10.06, None),
    ("Andhra Pradesh", "South", 2_084_658, 3_928_602, None, 36.66, 33.87, None, 5.37, None),
    ("Bihar", "East", 2_031_067, 4_273_285, None, 55.54, 34.46, None, 13.29, None),
    ("Telangana", "South", 1_879_803, None, 4_917_109, 60.56, None, None, 3.87, None),
    ("Punjab", "North", 1_623_386, None, 2_562_060, None, None, None, 3.14, None),
    ("Haryana", "North", 1_424_265, None, 2_621_059, None, None, None, 3.14, None),
    ("Odisha", "East", 1_411_434, None, 3_101_315, None, None, None, 4.75, None),
    ("Kerala", "South", 1_104_301, 1_842_567, None, None, None, None, 3.62, None),
    ("Jharkhand", "East", None, None, None, None, None, None, 4.11, None),
    ("Assam", "North-East", None, None, None, None, None, None, 3.60, None),
    ("Chhattisgarh", "Central", None, None, None, None, None, None, 2.89, None),
    ("Delhi", "North", None, None, None, None, None, None, None, None),
    ("Uttarakhand", "North", None, None, None, None, None, None, None, None),
    ("Himachal Pradesh", "North", None, None, None, None, None, None, None, None),
    ("Jammu & Kashmir", "North", None, None, 964_000, None, None, None, None, None),
    ("Goa", "West", None, None, None, None, None, None, None, None),
    ("Tripura", "North-East", None, None, None, None, None, None, None, None),
    ("Meghalaya", "North-East", None, None, None, None, None, None, None, None),
    ("Manipur", "North-East", None, None, None, None, None, None, None, None),
    ("Nagaland", "North-East", None, None, None, None, None, None, None, None),
    ("Arunachal Pradesh", "North-East", None, None, None, None, None, None, None, None),
    ("Mizoram", "North-East", None, None, None, None, None, None, None, None),
    ("Sikkim", "North-East", None, None, None, None, None, None, None, None),
    ("Puducherry", "South", None, None, None, None, None, None, None, None),
    ("Chandigarh", "North", None, None, None, None, None, None, None, None),
    ("Dadra & Nagar Haveli and Daman & Diu", "West", None, None, None, None, None, None, None, None),
    ("Ladakh", "North", None, None, None, None, None, None, None, None),
    ("Andaman & Nicobar Islands", "East", None, None, None, None, None, None, None, None),
    ("Lakshadweep", "South", None, None, None, None, None, None, None, None),
]

STATE_NOTES = {
    "Tamil Nadu": "URP+UAP figure (~62.4 lakh) is from a secondary 2026 source; verify. TN tops ASI factory count (S16).",
    "Telangana": "URP+UAP 49.17 lakh reported with a URP component (24.2 lakh) that conflicts with the URP column (18.8 lakh); "
                 "the sources likely differ in date. Verify on dashboard.msme.gov.in.",
    "Punjab": "URP+UAP from secondary report; date unclear.",
    "Haryana": "URP+UAP from secondary report; date unclear.",
    "Odisha": "URP+UAP from secondary report; date unclear.",
    "Jammu & Kashmir": "~9.64 lakh registrations since 2020 (Kashmir Life, 2026); URP/UAP split unknown.",
    "West Bengal": "Second-largest informal base (ASUSE) but low Udyam URP: largest formalisation gap among big states.",
    "Uttar Pradesh": "Largest by ASUSE establishments and workers; leads FY26 Udyam reported employment.",
    "Maharashtra": "Largest by Udyam registrations; Pune alone ~15% of state URP (S66).",
    "Gujarat": "Largest exporter state (26.6% of FY25 merchandise exports, S70).",
}

# ---------------------------------------------------------------------------
# Districts with quantitative data retrieved (ASUSE 2025 district estimates; Udyam URP)
# ---------------------------------------------------------------------------
DISTRICT_METRICS = [
    # state, district, asuse_establishments_lakh, asuse_workers_lakh, gva_per_worker_rs, udyam_urp, source_ids, note
    ("West Bengal", "North 24 Parganas", 16.59, 21.3, None, None, "S02;S02b", "Rank 1 by establishments and workers (ASUSE 2025)"),
    ("West Bengal", "South 24 Parganas", 10.29, 12.4, None, None, "S02;S02b", "Rank 2"),
    ("Gujarat", "Surat", 8.51, None, None, 588_856, "S02b;S66", "Top-10; textiles and diamonds"),
    ("Gujarat", "Ahmedabad", 7.30, None, None, 603_761, "S02b;S66", "Top-10; Udyam URP leader in Gujarat (19.9% of state)"),
    ("Telangana", "Rangareddy", 6.93, None, 272_000, None, "S02b", "Top-10; among highest GVA/worker"),
    ("Uttar Pradesh", "Prayagraj", 6.32, None, None, None, "S02b", "Top-10; only UP district in top-10"),
    ("Maharashtra", "Pune", 6.01, None, 228_000, 1_100_000, "S02b;S66", "Udyam URP ~15% of Maharashtra (derived ~11 lakh)"),
    ("Karnataka", "Bengaluru Urban", 5.0, None, None, None, "S02b", "~5 lakh establishments"),
    ("West Bengal", "Murshidabad", None, None, 100_443, None, "S02b", "Low GVA/worker: top-3 activities = 50%+ of units, 30% of GVA"),
    ("Maharashtra", "Mumbai Suburban", None, None, None, None, "S02b", "Among major districts; count not retrieved"),
    ("Maharashtra", "Thane", None, None, None, None, "S02b", "Among major districts; count not retrieved"),
    ("Maharashtra", "Pimpri-Chinchwad (Pune)", None, None, None, None, "S02b", "Among highest GVA/worker"),
    ("Telangana", "Hyderabad", None, None, None, None, "S02b", "Among highest GVA/worker; emoluments Rs 2.14 lakh/hired worker"),
    ("Delhi", "Delhi", None, None, None, None, "S02b", "Among highest GVA/worker"),
    ("Rajasthan", "Jaipur", None, None, None, None, "S02b", "Highest avg emoluments per hired worker among big districts (Rs 2.33 lakh)"),
    ("Uttarakhand", "Dehradun", None, None, None, None, "S02b", "Emoluments ~Rs 4.64 lakh per hired worker"),
    ("Gujarat", "Rajkot", None, None, None, 280_662, "S66", "9.3% of Gujarat URP"),
    ("Gujarat", "Vadodara", None, None, None, 223_028, "S66", "7.4% of Gujarat URP"),
    ("Tamil Nadu", "Chennai", None, None, None, 451_575, "S66", "10.9% of TN URP"),
    ("Tamil Nadu", "Coimbatore", None, None, None, 311_048, "S66", "7.5% of TN URP"),
    ("Tamil Nadu", "Tiruppur", None, None, None, 202_160, "S66", "4.9% of TN URP"),
]

DISTRICT_FACTS = [
    "Top 10 districts hold ~10% of unincorporated establishments, workers and GVA; top 50 (across 12 states) hold ~one-third (S02).",
    "Only 16 districts exceed 5 lakh establishments: 8 in West Bengal, 3 Maharashtra, 2 Gujarat, 1 each Karnataka, Telangana, UP (S02b).",
    "280 districts exceed the national GVA/worker of Rs 1,56,539; 331 districts lie between Rs 1.0 and 1.5 lakh (S02b).",
    "Top-10 districts are spread over Gujarat, Telangana, Uttar Pradesh and West Bengal (6 in WB) (S02b).",
]
