#!/usr/bin/env python3
"""Build company-level prospect lists from PUBLIC, bulk-downloadable sources.

Not executed in the research sandbox: the network policy blocked data.gov.in,
nseindia.com and bseindia.com. Download the inputs manually, then run:

    python3 scripts/build_contact_lists.py \
        --mca-dir inputs/mca_company_master/   # data.gov.in "Company Master Data" state CSVs
        --pincode inputs/pincode_directory.csv  # data.gov.in "All India Pincode Directory"
        [--sme-listed inputs/sme_listed.csv]   # NSE Emerge / BSE SME company lists (optional)
        [--epc-members inputs/epc_members.csv] # manually compiled from public EPC directories (optional)
        --out data/prospects/

Privacy and ethics rules (enforced in code):
  * Only company-level public fields are kept: name, CIN, status, NIC (from CIN),
    state, ROC, paid-up capital, PIN, district.
  * Email, phone, director names and full street address are DROPPED even if present.
  * Outreach must use official business channels and comply with the DPDP Act 2023
    and the platform terms of any listing used.

Outputs (CSV):
  top500_manufacturing.csv          NIC 10-33, active, paid-up Rs 25 lakh-50 cr, cluster districts first
  top500_potential_customers_O1.csv Manufacturing + wholesale (NIC 46), paid-up Rs 50 lakh-25 cr, target districts
  top500_exporters.csv              Join with EPC member list / SME-listed exporters (needs --epc-members or --sme-listed)
  top500_digitally_immature.csv     Paid-up >= Rs 1 cr with no website found ('website_status' = unknown until checked)
  top_clusters.csv                  Companies per cluster district (counts only)
"""
import argparse
import csv
import glob
import os
import re
from collections import Counter, defaultdict

DROP_FIELDS = {"EMAIL_ADDR", "EMAIL", "PHONE", "MOBILE", "DIRECTOR", "DIRECTORS", "REGISTERED_OFFICE_ADDRESS"}
CIN_RE = re.compile(r"^([LU])(\d{5})([A-Z]{2})(\d{4})([A-Z]{3})(\d{6})$")

# Cluster districts (from data/clusters.csv), normalised to lower case
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def cluster_districts():
    out = set()
    path = os.path.join(ROOT, "data", "clusters.csv")
    if os.path.exists(path):
        for r in csv.DictReader(open(path, encoding="utf-8")):
            for d in re.split(r"[/,]", r["district"]):
                out.add(d.strip().lower())
    return out


def parse_cin(cin):
    m = CIN_RE.match((cin or "").strip().upper())
    if not m:
        return None
    listed, nic, state, year, ownership, _ = m.groups()
    return dict(listed=listed == "L", nic5=nic, nic2=int(nic[:2]), state_code=state, year=int(year), ownership=ownership)


def money(x):
    try:
        return float(str(x).replace(",", "").strip() or 0)
    except ValueError:
        return 0.0


def load_pincodes(path):
    pin_to_district = {}
    if not path or not os.path.exists(path):
        return pin_to_district
    for r in csv.DictReader(open(path, encoding="utf-8", errors="ignore")):
        pin = (r.get("pincode") or r.get("Pincode") or "").strip()
        dist = (r.get("districtname") or r.get("District") or r.get("Districtname") or "").strip()
        if pin and dist:
            pin_to_district.setdefault(pin, dist)
    return pin_to_district


def load_mca(mca_dir, pin_to_district):
    rows = []
    for path in glob.glob(os.path.join(mca_dir, "*.csv")):
        for r in csv.DictReader(open(path, encoding="utf-8", errors="ignore")):
            r = {k.strip().upper(): v for k, v in r.items() if k}
            for f in list(r):
                if f in DROP_FIELDS:
                    r.pop(f)
            cin = r.get("CORPORATE_IDENTIFICATION_NUMBER") or r.get("CIN")
            meta = parse_cin(cin)
            if not meta:
                continue
            status = (r.get("COMPANY_STATUS") or "").strip().upper()
            if status and status not in ("ACTIVE", "ACTV"):
                continue
            pin = (re.findall(r"\b(\d{6})\b", r.get("REGISTERED_OFFICE_PIN", "") or "") or [""])[-1]
            rows.append(dict(
                company=(r.get("COMPANY_NAME") or "").strip(), cin=cin.strip().upper(), status=status or "ACTIVE",
                nic5=meta["nic5"], nic2=meta["nic2"], listed=meta["listed"], state=(r.get("REGISTERED_STATE") or meta["state_code"]).strip(),
                roc=(r.get("REGISTRAR_OF_COMPANIES") or "").strip(), paidup_rs=money(r.get("PAIDUP_CAPITAL")),
                pin=pin, district=pin_to_district.get(pin, ""), source=os.path.basename(path)))
    return rows


def size_band(paidup):
    # Paid-up capital is only a rough proxy for size; MSME status depends on investment AND turnover.
    for lim, label in ((25e5, "<25L"), (1e7, "25L-1cr"), (5e7, "1-5cr"), (25e7, "5-25cr"), (125e7, "25-125cr")):
        if paidup < lim:
            return label
    return ">=125cr"


def write(path, rows, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {path} ({len(rows)} rows)")


FIELDS = ["company", "cin", "nic5", "state", "district", "pin", "roc", "paidup_rs", "size_band_paidup", "turnover",
          "website", "website_status", "source"]


def rank(rows, clusters, n=500):
    for r in rows:
        r["size_band_paidup"] = size_band(r["paidup_rs"])
        r.setdefault("turnover", "not public")
        r.setdefault("website", "")
        r.setdefault("website_status", "unknown")
        r["in_cluster"] = r["district"].lower() in clusters
    return sorted(rows, key=lambda r: (not r["in_cluster"], -r["paidup_rs"]))[:n]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mca-dir", required=True)
    ap.add_argument("--pincode")
    ap.add_argument("--sme-listed")
    ap.add_argument("--epc-members")
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "prospects"))
    a = ap.parse_args(argv)

    clusters = cluster_districts()
    pins = load_pincodes(a.pincode)
    cos = load_mca(a.mca_dir, pins)
    print(f"loaded {len(cos):,} active companies")

    mfg = [r for r in cos if 10 <= r["nic2"] <= 33 and 25e5 <= r["paidup_rs"] <= 50e7]
    write(os.path.join(a.out, "top500_manufacturing.csv"), rank(mfg, clusters), FIELDS)

    o1 = [r for r in cos if (10 <= r["nic2"] <= 33 or r["nic2"] == 46) and 50e5 <= r["paidup_rs"] <= 25e7]
    write(os.path.join(a.out, "top500_potential_customers_O1.csv"), rank(o1, clusters), FIELDS)

    exporters = []
    names = set()
    for p in (a.epc_members, a.sme_listed):
        if p and os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8", errors="ignore")):
                names.add((r.get("company") or r.get("NAME OF COMPANY") or "").strip().upper())
    if names:
        exporters = [r for r in cos if r["company"].upper() in names]
    write(os.path.join(a.out, "top500_exporters.csv"), rank(exporters, clusters), FIELDS)

    immature = [r for r in cos if r["paidup_rs"] >= 1e7 and 10 <= r["nic2"] <= 46]
    write(os.path.join(a.out, "top500_digitally_immature.csv"), rank(immature, clusters), FIELDS)

    cnt = Counter(r["district"] for r in cos if r["district"].lower() in clusters)
    write(os.path.join(a.out, "top_clusters.csv"),
          [dict(district=d, active_companies=n) for d, n in cnt.most_common()], ["district", "active_companies"])


if __name__ == "__main__":
    main()
