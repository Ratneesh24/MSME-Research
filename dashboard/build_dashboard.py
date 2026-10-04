#!/usr/bin/env python3
"""Inject data/summary.json (+ problem evidence) into dashboard/src.html -> dashboard/index.html."""
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

summary = json.load(open(os.path.join(ROOT, "data", "summary.json"), encoding="utf-8"))
summary.pop("competitors", None)
summary.pop("digital", None)
keep = ("msmes_affected", "financial_impact_evidence", "current_solution", "current_spending", "startup_opportunity", "source_ids")
summary["problem_evidence"] = {r["id"]: {k: r[k] for k in keep}
                               for r in csv.DictReader(open(os.path.join(ROOT, "data", "problems.csv"), encoding="utf-8"))}
blob = json.dumps(summary, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = open(os.path.join(HERE, "src.html"), encoding="utf-8").read().replace("__DATA__", blob)
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
print(f"wrote dashboard/index.html ({len(html)/1024:.0f} KB)")
