#!/usr/bin/env python3
"""First-pass comparer for two extractions of the same study.
Usage: python3 qa_compare.py records_instance1.csv records_instance2.csv STUDY_ID
Matches records by the printed yield value (reported value as a string), then compares key fields.
Prints agreement rates and every difference for a human to classify (transcription, interpretation, omission).
Licence: AGPL-3.0-only.
"""
import csv, sys
FIELDS = ["condition_label","strain","culture_format","volume_mL","temperature_C","pH_start","duration_d","inoculum",
          "yield_reported_unit","yield_basis","yield_g_per_L_norm","yield_total_g_derived","yield_on_substrate_reported",
          "replicates_n","vegan_status","grade"]
def load(p, sid):
    with open(p, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r["study_id"] == sid]
def norm(v): return (v or "").strip().lower()
a_rows, b_rows = load(sys.argv[1], sys.argv[3]), load(sys.argv[2], sys.argv[3])
print(f"instance 1: {len(a_rows)} records; instance 2: {len(b_rows)} records")
b_by = {}
for r in b_rows: b_by.setdefault(norm(r["yield_reported_value"]), []).append(r)
matched = 0; diffs = []; total = 0; agree = 0
for a in a_rows:
    k = norm(a["yield_reported_value"]); cand = b_by.get(k, [])
    if not cand: diffs.append((a["record_id"], "omission in instance 2", k)); continue
    b = cand.pop(0); matched += 1
    for fld in FIELDS:
        total += 1
        if norm(a[fld]) == norm(b[fld]): agree += 1
        else: diffs.append((a["record_id"], fld, f"1={a[fld]!r} | 2={b[fld]!r}"))
for k, rest in b_by.items():
    for b in rest: diffs.append((b["record_id"], "extra in instance 2", k))
print(f"matched by yield value: {matched}; field agreement: {agree}/{total} = {agree/total:.1%}" if total else "nothing matched")
for d in diffs: print(" -", *d)
