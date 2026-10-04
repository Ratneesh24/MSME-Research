#!/usr/bin/env python3
"""Render the data-heavy report chapters (05, 06, 10-matrix) from data/*.csv.

Run after build_datasets.py:  python3 scripts/render_report_tables.py
Keeps every number in the Markdown identical to the CSVs.
"""
import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
D = lambda n: list(csv.DictReader(open(os.path.join(ROOT, "data", n), encoding="utf-8")))
OUT = lambda n: os.path.join(ROOT, "report", n)


def fmt_cr(x):
    if x in ("", None):
        return "–"
    v = float(x)
    return f"{v:,.0f}" if v >= 100 else (f"{v:,.1f}" if v >= 10 else f"{v:,.1f}")


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


# ---------------------------------------------------------------- chapter 05
crit = D("scoring_criteria.csv")
scores = D("problem_scores.csv")
probs = {p["id"]: p for p in D("problems.csv")}
short = {"customers": "Cust", "severity": "Sev", "frequency": "Freq", "financial_impact": "₹Imp", "wtp": "WTP",
         "existing_spend": "Spend", "competitive_white_space": "WhSp", "acquisition_ease": "CAC-ease",
         "tech_feasibility": "Tech", "scalability": "Scale", "gross_margin": "GM", "regulatory_ease": "Reg-ease",
         "retention": "Ret", "expansion": "Exp"}
keys = [c["key"] for c in crit]

ch5 = ["# 5. Problem database (42 problems) and scoring model",
       "",
       "> Brief sections 18–19. Data: `data/problems.csv` (descriptive fields + evidence), `data/problem_scores.csv` "
       "(scores), `data/scoring_criteria.csv`. Logic: `scripts/msme_data/problems.py`.",
       "",
       "## 5.1 Scoring model",
       "",
       "Each problem is scored 0–10 on 14 criteria. **Higher is always better for a startup**, so competitive intensity "
       "and regulatory complexity are inverted into *white space* and *regulatory ease*. The weights follow the brief's priorities: "
       "willingness to pay over number of users, and distribution feasibility over attractive ideas.",
       "",
       table(["Criterion", "Weight", "Scoring anchors"], [[c["criterion"], f"{c['weight_pct']}%", c["anchors"]] for c in crit]),
       "",
       "**Evidence confidence** (per problem): **H** = measured by official or large-sample data *and* observable spend; "
       "**M** = some measured data, WTP inferred; **L** = mostly reasoned. Treat L-confidence scores as hypotheses for interviews.",
       "",
       "**Sensitivity check.** Re-ranking with *equal* weights leaves the top five unchanged in membership (P09, P05, P10, P01, P30). "
       "Credit (P02) and logistics (P16) fall several places, because their scores rely on spend and financial impact rather than "
       "white space. The ranking is therefore not an artefact of the weights.",
       "",
       "## 5.2 Ranked scores",
       "",
       table(["#", "ID", "Problem"] + [short[k] for k in keys] + ["**Score**", "EW #", "Conf."],
             [[s["rank"], s["id"], s["problem"]] + [s[k] for k in keys] + [f"**{s['weighted_score']}**", s["equal_weight_rank"],
                                                                          s["evidence_confidence"]] for s in scores]),
       "",
       "EW # = rank under equal weights.",
       "",
       "## 5.3 Problem database (evidence, current solutions, spending)",
       "",
       "Full text in `data/problems.csv`. Condensed view:",
       "",
       table(["ID", "Problem", "MSMEs affected", "Frequency", "Financial impact (evidence)", "Current solution", "Current spending",
              "Competition", "Startup opportunity"],
             [[p["id"], p["problem"], p["msmes_affected"], p["frequency"], p["financial_impact_evidence"], p["current_solution"],
               p["current_spending"], p["competition"], p["startup_opportunity"]] for p in
              sorted(probs.values(), key=lambda p: p["id"])]),
       "",
       "## 5.4 Reading the results: problem ≠ business",
       "",
       "- **Highest-scoring problems are about money moving**: getting customers (P09/P10), getting paid (P01/P41), "
       "getting compliant cheaply via the CA (P05), and getting credit (P02). These have **observable spend**, measured by IndiaMART, "
       "Justdial, TReDS, CA fees and Tally, plus **new regulatory or technology triggers**: the MSMED Amendment Act 2026, CBAM, "
       "the labour codes and LLM agents.",
       "- **Big but weakly monetisable**: websites (P11), digital marketing (P12), training (P24), AI advice (P39), "
       "cybersecurity (P35), scheme discovery (P32). Many firms have these problems, but there is little evidence they pay to solve them.",
       "- **High score but hard for a new entrant**: lead generation itself (P09; incumbents), credit (P02; capital + "
       "regulation), procurement (P15; ops + working capital). The opportunity is an *adjacent wedge*: conversion (O3), "
       "credit-readiness/embedded finance (O1, O15), or a vertical procurement desk (O4).",
       "- **Small but urgent**: CBAM (P30). It affects few firms, but the pain is severe and buyers are concentrated and identifiable. "
       "It is a classic niche-to-platform entry.",
       ]
open(OUT("05_problem_database_and_scoring.md"), "w", encoding="utf-8").write("\n".join(ch5) + "\n")

# ---------------------------------------------------------------- chapter 06
tam = D("tam_sam_som.csv")
opps = {o["id"]: o for o in D("opportunities.csv")}
ch6 = ["# 6. TAM / SAM / SOM for every serious opportunity",
       "",
       "> Brief section 20. Data: `data/tam_sam_som.csv`; inputs in `scripts/msme_data/opportunities.py`.",
       "",
       "**Conventions.**",
       "",
       "- All values are **annual revenue to the startup in ₹ crore**, not customer spend or GMV (except where stated for O4).",
       "- **TAM bottom-up** = theoretical customers × ARPU. **TAM top-down** = an observed spend or value pool × a plausible capture share.",
       "- **SAM** = the segment the specific product can serve in its first geography and form.",
       "- **SOM** = realistic **year-5 ARR** range (customers × ARPU).",
       "- Where the two TAM methods diverge by more than 2×, the **lower** figure should be used for planning.",
       "",
       table(["ID", "Opportunity", "TAM bottom-up", "Inputs", "TAM top-down (low–high)", "SAM", "SOM yr-5 (low–high)", "SOM inputs"],
             [[t["id"], t["opportunity"], fmt_cr(t["tam_bottom_up_cr"]), t["tam_bottom_up_inputs"],
               f"{fmt_cr(t['tam_top_down_low_cr'])}–{fmt_cr(t['tam_top_down_high_cr'])}", fmt_cr(t["sam_cr"]),
               (f"{fmt_cr(t['som_year5_low_cr'])}–{fmt_cr(t['som_year5_high_cr'])}" if t["som_year5_low_cr"] else "–"),
               t["som_inputs"]] for t in tam]),
       "",
       "## 6.1 Method notes and sanity checks",
       "",
       "- **O1 Receivables.** Bottom-up (9 lakh × ₹60k = ₹5,400 cr) sits inside the top-down range (0.5–1.0% of the ₹7.34–8.1 "
       "lakh cr overdue stock = ₹3,670–8,100 cr). The two methods agree. SOM assumes 2–4% penetration of a 3-lakh-firm SAM in five years.",
       "- **O2 CA copilot.** Two independent views converge on ~₹1,000–1,500 cr: per-firm (1 lakh firms × ₹1.2 lakh) and "
       "per-client (1.49 cr GST filers × 70% professional-served × ₹100–150/month). The market is modest but highly reachable, "
       "and each firm is a channel to 50–500 MSMEs.",
       "- **O3 AI sales agent.** Bottom-up (₹4,800 cr) is ~2–4× the top-down (₹1,050–2,500 cr, as 30–50% of today's lead spend). "
       "**Use ~₹2,000 cr as the planning TAM.** The gap is the unproven assumption that firms will pay for conversion on top of leads.",
       "- **O4 Procurement.** The take-rate pool is enormous (₹62,000–1,24,000 cr on ₹124.9 lakh cr of procurement × 25% "
       "category share × 2–4%). The binding constraints are working capital and operations, not demand. SOM: 2,000–4,000 buyers "
       "× ₹60 lakh GMV × 4% = ₹48–96 cr net revenue (₹1,200–2,400 cr GMV).",
       "- **O5 Energy.** The TAM is infrastructure-like PPA revenue (1.3 lakh units × 150 kW × ₹75 lakh/MW-yr). It is low "
       "confidence because the count of energy-intensive units is unmeasured. SOM of 150–300 MW (₹112–225 cr revenue) needs "
       "₹600–1,200 cr of project capital.",
       "- **O6 CBAM.** A small, segment-summed TAM (~₹450–750 cr). SOM is ₹15–29 cr ARR, but the international expansion "
       "(every non-EU exporter of CBAM goods) and adjacent regulations (UK CBAM, product passports) widen it.",
       "- **D-category items (O14, O17, O18, O19)** show large theoretical TAMs that observed revenues contradict. "
       "Khatabook earned ~₹103 cr (FY24) and OkCredit ₹23 cr (FY25) from crores of users. **Theoretical TAM is not evidence.**",
       "",
       "## 6.2 What would make these numbers wrong",
       "",
       "1. **ARPU assumptions** (₹48k–1.5 lakh/yr) are anchored on adjacent spend (IndiaMART ₹69k, Justdial ₹19k, WhatsApp "
       "BSPs ₹18–42k, CA software). Direct WTP for the specific product is untested.",
       "2. **Customer counts above ₹5 cr turnover** rest on e-invoice GSTIN counts. These are GSTIN-level, so PAN-level counts may be "
       "15–30% lower.",
       "3. **Penetration rates** (1–5% of SAM in five years) are typical of Indian SMB SaaS but are not guaranteed.",
       ]
open(OUT("06_market_sizing.md"), "w", encoding="utf-8").write("\n".join(ch6) + "\n")

# ---------------------------------------------------------------- matrix snippet for chapter 10
mx = D("opportunity_matrix.csv")
snippet = table(["ID", "Opportunity", "Cat.", "Market size", "Severity", "WTP", "Competition", "CAC difficulty", "MVP difficulty",
                 "Scalability", "5–10 yr potential", "Evidence"],
                [[m["id"], m["opportunity"], f"**{m['category']}**", m["market_size"], m["problem_severity"], m["willingness_to_pay"],
                  m["competition"], m["cac_difficulty"], m["mvp_difficulty"], m["scalability"], m["potential_5_10yr"],
                  m["evidence_confidence"]] for m in mx])
open(OUT("_matrix_snippet.md"), "w", encoding="utf-8").write(snippet + "\n")

ue = D("unit_economics.csv")
ue_snip = table(["ID", "ARPU ₹/yr", "Gross margin", "CAC ₹ (low–high)", "Annual churn", "LTV ₹", "LTV/CAC", "Payback (months)", "Notes"],
                [[u["id"], f"{int(u['arpu_rs_per_year']):,}", f"{float(u['gross_margin']):.0%}",
                  f"{int(u['cac_low_rs']):,}–{int(u['cac_high_rs']):,}", f"{float(u['annual_churn']):.0%}", f"{int(u['ltv_rs']):,}",
                  f"{u['ltv_to_cac_low']}–{u['ltv_to_cac_high']}", f"{u['payback_months_low']}–{u['payback_months_high']}", u["notes"]]
                 for u in ue])
open(OUT("_unit_economics_snippet.md"), "w", encoding="utf-8").write(ue_snip + "\n")
print("rendered chapters 05, 06 and snippets")

# ---------------------------------------------------------------- chapter 10 (opportunity cards + matrix)
opp_rows = D("opportunities.csv")
tam_by = {t["id"]: t for t in tam}
cards = []
for o in opp_rows:
    t = tam_by[o["id"]]
    som = (f"₹{fmt_cr(t['som_year5_low_cr'])}–{fmt_cr(t['som_year5_high_cr'])} cr ARR (yr 5)" if t["som_year5_low_cr"] else "–")
    tam_txt = (f"₹{fmt_cr(t['tam_bottom_up_cr'])} cr bottom-up; " if t["tam_bottom_up_cr"] else "") + \
              f"₹{fmt_cr(t['tam_top_down_low_cr'])}–{fmt_cr(t['tam_top_down_high_cr'])} cr top-down"
    if o["category"].startswith("D"):
        continue
    cards.append("\n".join([
        f"### {o['id']} · {o['opportunity']}  —  Category **{o['category']}**",
        "",
        table(["Field", "Assessment"], [
            ["Problem(s)", o["problems"]],
            ["Target customer", o["target_customer"]],
            ["Potential customers", o["potential_customers"]],
            ["Pain level", o["pain_level"]],
            ["Existing alternatives", o["existing_alternatives"]],
            ["Why alternatives are insufficient", o["why_insufficient"]],
            ["Proposed solution", o["proposed_solution"]],
            ["Business model", o["business_model"]],
            ["Estimated pricing", o["pricing"]],
            ["TAM", tam_txt],
            ["SAM", f"₹{fmt_cr(t['sam_cr'])} cr ({t['sam_basis']})"],
            ["SOM", som],
            ["Competitive intensity", o["competition"]],
            ["Customer acquisition", o["acquisition"]],
            ["MVP complexity / time to MVP", f"{o['mvp_complexity']} / {o['time_to_mvp']}"],
            ["Capital requirement", o["capital"]],
            ["Gross-margin potential", o["gross_margin"]],
            ["Regulatory risk", o["regulatory_risk"]],
            ["Technology risk", o["technology_risk"]],
            ["Expansion", o["expansion"]],
            ["International potential", o["international"]],
            ["Evidence strength", o["evidence_strength"]],
        ]),
        ""]))

d_rows = [[o["id"], o["opportunity"], o["existing_alternatives"], o["evidence_strength"]] for o in opp_rows if o["category"].startswith("D")]
cat = {}
for o in opp_rows:
    cat.setdefault(o["category"][0], []).append(f"{o['id']} {o['opportunity']}")

ch10 = ["# 10. Startup opportunity shortlist and final opportunity matrix",
        "",
        "> Brief sections 27–28. Data: `data/opportunities.csv`, `data/tam_sam_som.csv`, `data/opportunity_matrix.csv`. "
        "Nineteen opportunities were assessed. Fifteen get full cards below, and four are listed as **Category D: avoid for now**.",
        "",
        "## 10.1 Final opportunity matrix",
        "",
        open(OUT("_matrix_snippet.md"), encoding="utf-8").read(),
        "",
        "## 10.2 Categories (not a single 'best idea')",
        "",
        "**Category A: strong evidence** (large or urgent problem + demonstrated spending + identifiable customers)",
        "",
        "\n".join(f"- {x}" for x in cat.get("A", [])),
        "",
        "  - *O4 is \"A (hard)\"*: the evidence is excellent (OfBusiness ₹22,241 cr revenue), but it needs heavy working capital and operations, against well-funded incumbents.",
        "  - *O6 is \"A (niche)\"*: severe, regulation-driven pain with identifiable buyers, but a small domestic TAM. Its international and regulatory expansion is the upside.",
        "",
        "**Category B: promising, needs willingness-to-pay validation**",
        "",
        "\n".join(f"- {x}" for x in cat.get("B", [])),
        "",
        "**Category C: interesting but weak evidence or monetisation**",
        "",
        "\n".join(f"- {x}" for x in cat.get("C", [])),
        "",
        "**Category D: avoid for now** (low WTP, saturated, tiny, or hard distribution)",
        "",
        table(["ID", "Opportunity", "Who already serves it", "Why avoid"], d_rows),
        "",
        "## 10.3 How the A-category opportunities relate",
        "",
        "```",
        "                 ┌──────────── CA firm (trusted channel) ────────────┐",
        "                 │                                                   │",
        "   O2 CA copilot ──► books + GST + bank data ──► O1 receivables ──► O15 credit / TReDS",
        "                                                   ▲",
        "   O3 sales agent ──► more orders ──► more invoices┘",
        "",
        "   O6 CBAM/carbon ◄── plant energy data ──► O5 energy-as-a-service",
        "```",
        "",
        "There are two coherent theses:",
        "",
        "1. **MSME finance back-office (O2 → O1 → O15).** Win CA firms with a copilot, then use the client data and trust to sell "
        "receivables automation and credit access to their MSME clients.",
        "2. **MSME climate-compliance stack (O6 ↔ O5).** Win exporters with CBAM compliance, then sell the energy and abatement "
        "projects that reduce the very emissions being reported. Chapter 12 shows this also fits AgriKhet's name and positioning.",
        "",
        "O3 (sales agent) stands alone. It has the broadest market and the most fragile retention.",
        "",
        "## 10.4 Opportunity cards (A, B and C)",
        "",
        "\n".join(cards),
        ]
open(OUT("10_opportunities.md"), "w", encoding="utf-8").write("\n".join(ch10) + "\n")
print("rendered chapter 10")
