# India MSME Ecosystem: Problems & Startup Opportunities (Oct 2026)

A data-backed study of which problems faced by Indian MSMEs are **large, frequent, painful, underserved and monetisable** enough to build a startup on. It takes the question from ecosystem → measurable problems → affected customers → existing spending → competition → market size → business model → MVP → validation → decision.

**Start here → [Executive summary](report/00_executive_summary.md)**

## Headline findings

| | |
|---|---|
| Udyam registrations | **9.16 crore** (Jul-2026). These are registrations, not active businesses |
| Operating non-farm establishments | **7.92 crore** (ASUSE 2025); 86.6% are one-person units with ~₹2.5 lakh GVA a year |
| Commercially active (GST-filing) | **~1.2–1.45 crore**; turnover ≥ ₹5 cr: **~6–7.5 lakh** |
| Realistic B2B customer base | **~8–12 lakh** B2B manufacturers and distributors with ₹2–100 cr turnover, in ~30 industrial districts |
| Largest measured pains | Delayed payments ₹7.34–8.1 lakh cr (73-day average); credit gap ₹30 lakh cr; compliance ₹13–17 lakh/yr per manufacturing MSME; small-firm logistics 16.9% vs 7.6% of output; CBAM default-value penalties since Jan-2026 |
| Strongest willingness-to-pay evidence | IndiaMART ₹1,569 cr (2.28 lakh payers); Justdial ₹1,214 cr; OfBusiness ₹22,241 cr; Tally ₹500–1,000 cr |
| **Category A opportunities** | O1 AI receivables copilot · O2 AI copilot for CA firms · O3 AI B2B sales agent · O4 vertical procurement + credit (hard) · O6 CBAM/carbon compliance (niche) |

## Repository map

| Path | What |
|---|---|
| [`report/`](report) | 17 chapters covering brief sections 1–35 (index below) |
| [`data/`](data) | 25 CSV datasets + `summary.json` (dashboard feed) |
| [`instruments/`](instruments) | Interview guide, survey, qualification scorecard, response-coding template |
| [`scripts/`](scripts) | `build_datasets.py` (all CSVs from `msme_data/`), `render_report_tables.py` (data-driven chapters), `build_contact_lists.py` (public prospect-list pipeline) |
| [`dashboard/index.html`](dashboard/index.html) | Interactive dashboard (also published as a private Artifact) |

### Report chapters

| # | Chapter | Brief sections |
|---|---|---|
| 00 | [Executive summary](report/00_executive_summary.md) | 34 |
| 01 | [MSME universe and active-MSME funnel](report/01_msme_universe.md) | 1–2 |
| 02 | [States, districts, clusters](report/02_geography.md) | 3–4 |
| 03 | [Turnover, ability to pay, employment](report/03_turnover_employment.md) | 5–6 |
| 04 | [Problem areas: finance, compliance, digital, website, sales, procurement, manufacturing, exports, schemes](report/04_problem_areas.md) | 7–15 |
| 05 | [Problem database (42) and scoring model](report/05_problem_database_and_scoring.md) | 18–19 |
| 06 | [TAM / SAM / SOM](report/06_market_sizing.md) | 20 |
| 07 | [Competitors, global analogs, white space, India-specific dynamics](report/07_competitors_white_space.md) | 21, 22, 26 |
| 08 | [Business models, unit economics, first 100 customers](report/08_business_models_gtm.md) | 23–24 |
| 09 | [Trends 2026–2035](report/09_trends_2026_2035.md) | 25 |
| 10 | [Opportunity shortlist (19) and final matrix](report/10_opportunities.md) | 27–28 |
| 11 | [Top-5 deep dives](report/11_top5_deep_dives.md) | 29 |
| 12 | ["Could AgriKhet build this?"](report/12_agrikhet.md) | 30 |
| 13 | [Primary research design + 30-day validation plan + kill criteria](report/13_validation_plan.md) | 16, 31 |
| 14 | ["Should we build this?"](report/14_should_we_build.md) | 35 |
| 15 | [Sources and data-quality log](report/15_sources.md) | 32–33 |
| 16 | [Contact database approach](report/16_contact_database.md) | 17 |

### Datasets (`data/`)

`msme_universe_funnel` · `msme_size_criteria` · `msme_size_distribution` · `sector_msme` · `subsector_count_vs_ability_to_pay` · `state_msme` (all 36 States/UTs; blanks where not retrieved) · `district_msme` · `clusters` (142) · `turnover_distribution` · `ability_to_pay_segments` · `employment` · `udyam_employment_fy26_by_state` · `digital_adoption` · `digital_maturity_levels` · `website_presence` · `problems` (42) · `problem_scores` · `scoring_criteria` · `competitors` (74) · `opportunities` (19) · `tam_sam_som` · `opportunity_matrix` · `unit_economics` · `channel_partners_public` (95) · `sources` (69)

## Rebuild

```bash
python3 scripts/build_datasets.py        # regenerates data/*.csv and data/summary.json (stdlib only)
python3 scripts/render_report_tables.py  # regenerates chapters 05, 06, 10 from the CSVs
```
Edit numbers only in `scripts/msme_data/*.py`, then rebuild. Report, CSVs and dashboard stay consistent.

## Read before using any number

- **Compiled 4-Oct-2026 under a network policy that blocked direct downloads from government portals.** Figures were captured from search-engine extracts of the cited pages. **Verify against the primary URL** in `data/sources.csv` before external use, especially "secondary"-tier sources.
- **No primary interviews were conducted, and none were invented.** WTP is inferred from observed spending and flagged where unproven.
- Every row is labelled **observed / derived / estimate / assumption**. Gaps say **"data unavailable"**.
- Company-level "Top 500" prospect lists were **not** generated (inputs could not be downloaded). `scripts/build_contact_lists.py` generates them from public MCA/NSE/BSE/PIN data, keeping company-level fields only and dropping personal data.
