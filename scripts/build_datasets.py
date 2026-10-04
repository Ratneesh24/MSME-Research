#!/usr/bin/env python3
"""Build every CSV in ../data (and data/summary.json for the dashboard).

Usage:  python3 scripts/build_datasets.py
Only the Python standard library is needed.
"""
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from msme_data.sources import SOURCES
from msme_data import universe as U
from msme_data import geography as G
from msme_data.clusters import CLUSTERS
from msme_data import problems as P
from msme_data.competitors import COMPETITORS
from msme_data import opportunities as O
from msme_data.partners import PARTNERS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data")
os.makedirs(DATA, exist_ok=True)

LAKH, CRORE = 1e5, 1e7


def write(name, rows, fields=None):
    rows = list(rows)
    fields = fields or list(rows[0].keys())
    path = os.path.join(DATA, name)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in fields})
    print(f"wrote {name:40s} {len(rows):4d} rows")
    return rows


def r0(x):
    return None if x is None else int(round(x))


# ---------------------------------------------------------------- sources
write("sources.csv", SOURCES, ["id", "tier", "publisher", "title", "period", "url"])

# ---------------------------------------------------------------- universe
funnel = [dict(r, value=r0(r["value"]), value_crore=round(r["value"] / CRORE, 3)) for r in U.FUNNEL]
write("msme_universe_funnel.csv", funnel,
      ["stage", "metric", "value", "value_crore", "ref_date", "data_type", "source_ids", "notes"])

write("msme_size_criteria.csv", U.SIZE_CRITERIA)
size_rows = []
for r in U.SIZE_DISTRIBUTION:
    tot = r["micro"] + r["small"] + r["medium"]
    size_rows.append(dict(r, total=tot, micro_pct=round(100 * r["micro"] / tot, 2),
                          small_pct=round(100 * r["small"] / tot, 2), medium_pct=round(100 * r["medium"] / tot, 3)))
write("msme_size_distribution.csv", size_rows,
      ["dataset", "ref_date", "micro", "small", "medium", "total", "micro_pct", "small_pct", "medium_pct", "source_ids"])

write("sector_msme.csv", U.SECTOR)
write("subsector_count_vs_ability_to_pay.csv",
      [dict(subsector=a, nic=b, count_rank=c, ability_to_pay_rank=d, evidence=e) for a, b, c, d, e in U.SUBSECTORS])

turn = [dict(r, est_low=r0(r["est_low"]), est_high=r0(r["est_high"]),
             est_mid=r0((r["est_low"] + r["est_high"]) / 2)) for r in U.TURNOVER]
write("turnover_distribution.csv", turn, ["bracket", "est_low", "est_mid", "est_high", "confidence", "basis"])
write("ability_to_pay_segments.csv", U.ABILITY_TO_PAY)

write("employment.csv", [dict(r, value=(round(r["value"], 2) if r["value"] < 100 else r0(r["value"]))) for r in U.EMPLOYMENT],
      ["metric", "value", "ref", "data_type", "source_ids", "notes"])
write("udyam_employment_fy26_by_state.csv",
      [dict(state=s, reported_employment_lakh=v, source_ids="S07") for s, v in U.UDYAM_EMPLOYMENT_FY26_STATES])

write("digital_adoption.csv", U.DIGITAL)
write("digital_maturity_levels.csv",
      [dict(r, est_low=r0(r["est_low"]), est_high=r0(r["est_high"])) for r in U.DIGITAL_LEVELS])
write("website_presence.csv", [dict(r, est_low=r0(r["est_low"]), est_high=r0(r["est_high"])) for r in U.WEBSITE_PRESENCE])

# ---------------------------------------------------------------- states
state_rows = []
for (name, region, urp, feb26, other, emp, nss, asuse, pop, exp) in G.STATES:
    total = feb26 or other
    total_src = "S04 (28-Feb-2026)" if feb26 else ("secondary 2026 (verify)" if other else "")
    row = dict(state=name, region=region, udyam_urp=urp, udyam_urp_uap_total=total, total_source=total_src,
               udyam_reported_employment_fy26_lakh=emp, nss73_msme_lakh_2015_16=nss,
               asuse_2023_24_establishments_lakh=asuse, population_2026_crore=pop,
               merchandise_exports_fy25_usd_bn=exp)
    row["urp_per_lakh_pop"] = r0(urp / (pop * 100)) if (urp and pop) else None
    row["total_per_lakh_pop"] = r0(total / (pop * 100)) if (total and pop) else None
    # Formalisation proxy: URP registrations relative to the informal-survey base (different dates - indicative only)
    base = asuse or nss
    row["urp_to_survey_base_ratio"] = round(urp / (base * LAKH), 2) if (urp and base) else None
    row["survey_base_used"] = ("ASUSE 2023-24" if asuse else ("NSS 2015-16" if nss else ""))
    row["notes"] = G.STATE_NOTES.get(name, "")
    state_rows.append(row)
write("state_msme.csv", state_rows)

write("district_msme.csv",
      [dict(state=s, district=d, asuse2025_establishments_lakh=e, asuse2025_workers_lakh=w, gva_per_worker_rs=g,
            udyam_urp=u, source_ids=src, note=n) for s, d, e, w, g, u, src, n in G.DISTRICT_METRICS])

# ---------------------------------------------------------------- clusters
write("clusters.csv",
      [dict(state=s, district=d, cluster=c, sector=sec, major_products=prod, cluster_type=t, export_relevance=x,
            msme_count="data unavailable", digital_maturity="data unavailable", linked_opportunities=o)
       for s, d, c, sec, prod, t, x, o in CLUSTERS])

# ---------------------------------------------------------------- problems + scoring
write("scoring_criteria.csv", [dict(key=k, criterion=l, weight_pct=w, anchors=a) for k, l, w, a in P.CRITERIA])
prob_rows, score_rows = [], []
for (pid, name, cat, who, affected, freq, sev, impact, cur, spend, digi, comp, opp, src, conf, scores) in P.PROBLEMS:
    assert len(scores) == 14, pid
    ws = P.weighted_score(scores)
    prob_rows.append(dict(id=pid, problem=name, category=cat, who_is_affected=who, msmes_affected=affected, frequency=freq,
                          severity=sev, financial_impact_evidence=impact, current_solution=cur, current_spending=spend,
                          digital_readiness=digi, competition=comp, startup_opportunity=opp, evidence_confidence=conf,
                          weighted_score=ws, source_ids=src))
    sr = dict(id=pid, problem=name, category=cat)
    sr.update({k: v for k, v in zip(P.KEYS, scores)})
    sr.update(weighted_score=ws, equal_weight_score=round(sum(scores) / 14, 2), evidence_confidence=conf)
    score_rows.append(sr)
# Sensitivity: rank under equal weights, to show the ranking is not an artefact of the weights.
for i, r in enumerate(sorted(score_rows, key=lambda r: -r["equal_weight_score"]), 1):
    r["equal_weight_rank"] = i
score_rows.sort(key=lambda r: -r["weighted_score"])
for i, r in enumerate(score_rows, 1):
    r["rank"] = i
write("problems.csv", prob_rows)
write("problem_scores.csv", score_rows, ["rank", "id", "problem", "category"] + P.KEYS + ["weighted_score", "equal_weight_score", "equal_weight_rank", "evidence_confidence"])

# ---------------------------------------------------------------- competitors
write("competitors.csv",
      [dict(company=a, country=b, problem_or_opportunity=c, target_customer=d, product=e, pricing=f, scale_or_funding=g,
            business_model=h, strength=i, weakness=j, india_opportunity=k) for a, b, c, d, e, f, g, h, i, j, k in COMPETITORS])

# ---------------------------------------------------------------- opportunities, TAM/SAM/SOM
opp_rows, tam_rows, matrix_rows = [], [], []
for o in O.OPPORTUNITIES:
    tam_bu = (o["tam_customers"] * o["arpu"] / CRORE) if (o.get("tam_customers") and o.get("arpu")) else None
    td_mid = (o["topdown_low_cr"] + o["topdown_high_cr"]) / 2
    if o.get("sam_customers") and o.get("sam_arpu"):
        sam = o["sam_customers"] * o["sam_arpu"] / CRORE
    elif o.get("sam_fraction"):
        sam = o["sam_fraction"] * (tam_bu or td_mid)
    else:
        sam = None
    som_lo = o["som_customers"][0] * o["som_arpu"] / CRORE if o["som_arpu"] else None
    som_hi = o["som_customers"][1] * o["som_arpu"] / CRORE if o["som_arpu"] else None
    tam_rows.append(dict(
        id=o["id"], opportunity=o["name"],
        tam_bottom_up_cr=round(tam_bu) if tam_bu else None,
        tam_bottom_up_inputs=(f"{o['tam_customers']:,} customers x Rs {o['arpu']:,.0f}/yr" if tam_bu else "n/a (top-down only)"),
        tam_top_down_low_cr=o["topdown_low_cr"], tam_top_down_high_cr=o["topdown_high_cr"], tam_top_down_method=o["topdown_method"],
        sam_cr=round(sam) if sam else None, sam_basis=o["sam_basis"],
        som_year5_low_cr=round(som_lo, 1) if som_lo else None, som_year5_high_cr=round(som_hi, 1) if som_hi else None,
        som_inputs=(f"{o['som_customers'][0]:,}-{o['som_customers'][1]:,} customers x Rs {o['som_arpu']:,.0f}/yr" if som_lo else "n/a"),
        customers_basis=o["customers_basis"]))
    opp_rows.append(dict(
        id=o["id"], opportunity=o["name"], category=o["category"], problems=o["problems"], target_customer=o["target"],
        potential_customers=(f"{o['tam_customers']:,}" if o.get("tam_customers") else o["customers_basis"]), pain_level=o["pain"],
        existing_alternatives=o["alternatives"], why_insufficient=o["why_insufficient"], proposed_solution=o["solution"],
        business_model=o["model"], pricing=o["pricing"], competition=o["competition"], acquisition=o["acquisition"],
        mvp_complexity=o["mvp_complexity"], time_to_mvp=o["time_to_mvp"], capital=o["capital"], gross_margin=o["gross_margin"],
        regulatory_risk=o["regulatory_risk"], technology_risk=o["tech_risk"], expansion=o["expansion"],
        international=o["international"], evidence_strength=o["evidence"]))
    m = o["matrix"]
    matrix_rows.append(dict(id=o["id"], opportunity=o["name"], category=o["category"], market_size=m["market"],
                            problem_severity=m["severity"], willingness_to_pay=m["wtp"], competition=m["competition"],
                            cac_difficulty=m["cac"], mvp_difficulty=m["mvp"], scalability=m["scalability"],
                            potential_5_10yr=m["potential"], evidence_confidence=m["confidence"]))
write("opportunities.csv", opp_rows)
write("tam_sam_som.csv", tam_rows)
write("opportunity_matrix.csv", matrix_rows)

ue_rows = []
for (oid, arpu, gm, cac_lo, cac_hi, churn, note) in O.UNIT_ECONOMICS:
    ltv = arpu * gm / churn
    gm_month = arpu * gm / 12
    ue_rows.append(dict(id=oid, arpu_rs_per_year=arpu, gross_margin=gm, cac_low_rs=cac_lo, cac_high_rs=cac_hi,
                        annual_churn=churn, ltv_rs=r0(ltv), ltv_to_cac_low=round(ltv / cac_hi, 1),
                        ltv_to_cac_high=round(ltv / cac_lo, 1), payback_months_low=round(cac_lo / gm_month, 1),
                        payback_months_high=round(cac_hi / gm_month, 1), notes=note))
write("unit_economics.csv", ue_rows)

write("channel_partners_public.csv",
      [dict(organisation=a, type=b, city=c, state=d, sector_focus=e, relevant_opportunities=f, website=g,
            source="Public organisation; verify before outreach") for a, b, c, d, e, f, g in PARTNERS])

# ---------------------------------------------------------------- dashboard summary
summary = dict(
    generated_for="India MSME opportunity study (Oct 2026)",
    funnel=[dict(stage=r["stage"], metric=r["metric"].strip(), value=r["value"], ref=r["ref_date"],
                 type=r["data_type"], src=r["source_ids"]) for r in funnel],
    states=[{k: v for k, v in r.items() if k != "notes"} for r in state_rows if r["udyam_urp"]],
    districts=[dict(state=s, district=d, est=e, workers=w, gva=g, urp=u) for s, d, e, w, g, u, *_ in G.DISTRICT_METRICS],
    turnover=turn, digital_levels=[dict(r, est_low=r0(r["est_low"]), est_high=r0(r["est_high"])) for r in U.DIGITAL_LEVELS],
    digital=U.DIGITAL, problems=score_rows, criteria=[dict(key=k, label=l, weight=w) for k, l, w, _ in P.CRITERIA],
    opportunities=[dict(o, **t, **{k: v for k, v in m.items() if k not in ("id", "opportunity")})
                   for o, t, m in zip(opp_rows, tam_rows, matrix_rows)],
    unit_economics=ue_rows,
    clusters=[dict(state=s, district=d, cluster=c, sector=sec, products=prod, type=t, export=x, opp=o)
              for s, d, c, sec, prod, t, x, o in CLUSTERS],
    competitors=[dict(company=a, country=b, area=c, scale=g, opp=k) for a, b, c, d, e, f, g, h, i, j, k in COMPETITORS],
)
with open(os.path.join(DATA, "summary.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=1)
print("wrote summary.json")
