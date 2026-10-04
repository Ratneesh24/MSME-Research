# 16. Contact database: what was built, what was not, and how to build the rest legally

> Brief section 17. The founders chose **"Design + public lists"**. Only company-level public information is used; no personal data is scraped or exposed.

## 16.1 Delivered in this study

| File | Contents | Records | Personal data? |
|---|---|---:|---|
| `data/channel_partners_public.csv` | National MSME bodies, chambers, **export promotion councils**, sector associations, **cluster/industrial-estate associations** and public facilitation bodies (SIDBI, NSIC, MSME-DFOs, DICs, BEE, ICAI, TReDS platforms). Each is mapped to the opportunities it can distribute | 95 | No. Organisation names, city, state, sector; official website only where confident |
| `data/clusters.csv` | 142 MSME clusters with state, district, sector, products, export relevance and linked opportunities | 142 | No |
| `data/district_msme.csv` | Districts with retrieved ASUSE 2025 / Udyam counts | 21 | No |
| `scripts/build_contact_lists.py` | Pipeline to generate **company-level** prospect lists from bulk public datasets | — | Drops email/phone/director/street-address fields by design |

**Why these first.** Chapter 8 shows that **CA firms and cluster associations are the cheapest acquisition channel**. One association relationship reaches hundreds of qualified MSMEs with consent and trust. That is worth more than a cold list of 500 firms.

## 16.2 Not delivered, and why

The brief asked for "Top 500" lists: potential customers, manufacturers, exporters, digitally immature but significant firms, and top clusters. These need bulk company-level data from public portals (MCA company master data on data.gov.in, NSE Emerge/BSE SME listings, India Post PIN directory). **The research environment's network policy blocked these downloads**, so the lists were **not generated**. No list was assembled from memory, because that would risk fabricated or outdated entries.

## 16.3 How to generate them (≈1 hour once inputs are downloaded)

1. Download inputs:
   - **MCA Company Master Data** (data.gov.in, state-wise CSVs): company name, CIN, status, class, paid-up capital, ROC, registered-office PIN.
   - **All India Pincode Directory** (data.gov.in): PIN → district.
   - **NSE Emerge** (731 companies, May-2026) and **BSE SME** (~580) listed-company files, optional (S60).
   - **EPC member directories**: compile manually from public EPC websites (EEPC, AEPC, CHEMEXCIL, PLEXCONCIL and others), optional.
2. Run:
   ```bash
   python3 scripts/build_contact_lists.py --mca-dir inputs/mca/ --pincode inputs/pincode.csv \
       --sme-listed inputs/sme_listed.csv --epc-members inputs/epc_members.csv --out data/prospects/
   ```
3. The NIC code is parsed from the CIN (characters 2–6). For example, `U72200KA1991PTC012483` → NIC 72200, Karnataka. Manufacturing = NIC 10–33; wholesale = 46.
4. Lists produced:
   - `top500_manufacturing.csv`
   - `top500_potential_customers_O1.csv`
   - `top500_exporters.csv`
   - `top500_digitally_immature.csv` (website status starts as "unknown"; check manually or via a search API, respecting terms)
   - `top_clusters.csv`
5. **Limits:**
   - Proprietorships and partnerships (most MSMEs) are **not** in MCA data. Reach them through associations and CAs.
   - Paid-up capital is only a rough size proxy, and turnover is not public.
   - GST/Udyam numbers should only be added when the business itself shares them.

## 16.4 Rules for outreach

- Use official business channels only: company landlines, generic business emails and association introductions.
- Comply with the **Digital Personal Data Protection Act, 2023**: purpose limitation, consent for follow-ups, and honouring opt-outs.
- Do not scrape lead platforms (IndiaMART, Justdial). Respect their terms. Contact listed sellers only through permitted means.
- Register outreach consent in the CRM and give an easy opt-out on WhatsApp ("STOP").
