#!/usr/bin/env python3
"""Lint a bacterial cellulose atlas records CSV against the atlas conventions.

Usage: python3 lint_batch.py records_batchN.csv [--studies studies_batchN.csv]
                             [--against other_records.csv ...] [--legacy]
--legacy  accept the pre-split vegan token (flag-unspecified) and report text inside
          numeric columns / undefined flag tokens as warnings (for batches 1 and 2).
Exit status is 1 when any ERROR is found.
Licence: AGPL-3.0-only
"""
import argparse, csv, re, sys

REC_COLS = ("record_id,study_id,record_type,condition_label,lever_family,strain,culture_format,volume_mL,surface_area_cm2,depth_cm,"
            "temperature_C,pH_start,pH_end,duration_d,inoculum,medium_summary,carbon_sources,nitrogen_sources,additives,yield_reported_value,"
            "yield_reported_unit,yield_basis,yield_g_per_L_norm,productivity_g_per_L_day,yield_total_g_derived,yield_mg_per_cm2_derived,"
            "yield_on_substrate_reported,carbon_declared_g_per_L_derived,bc_to_declared_carbon_ratio_derived,replicates_n,variance_reported,"
            "vegan_status,vegan_flag_inputs,wa_tags,grade,reliability_flags,source_location,notes").split(",")
NUMERIC = ("volume_mL,surface_area_cm2,depth_cm,temperature_C,pH_start,pH_end,duration_d,yield_g_per_L_norm,productivity_g_per_L_day,"
           "yield_total_g_derived,yield_mg_per_cm2_derived,carbon_declared_g_per_L_derived,bc_to_declared_carbon_ratio_derived,replicates_n").split(",")
RECORD_TYPES = {"observation", "model_prediction", "property", "text_endpoint"}
GRADES = {"A", "B", "C", "D", "own"}
VEGAN = {"clear", "flag-inoculum-only", "flag-production-medium"}
VEGAN_LEGACY = {"flag-unspecified"}
FLAGS = set("""n1 no_variance no_control basis_unconfirmed denominator_unclear mass_balance_exceeds per_litre_inflated outlier_check abstract_only
volume_inconsistent contradiction_in_text pasteurised_not_sterilised carbon_labelled_glucose_vs_sugar film_state_hydrated_or_dried_not_stated
pass2_field temperature_and_volume_lost_in_text_extraction prediction_not_observation
composition_incomplete composition_inconsistent control_yield_not_in_text detection_limit_unstated error_exceeds_mean error_term_undefined
figure_only_yield nitrogen_method_not_described preparation_not_described starter_not_described no_mass_yield qualitative_study
ratio_claim_wet_basis table_not_captured temperature_not_stated vessel_geometry_inconsistent yeast_extract_replacement_unclear
no_replicate_n area_not_stated
names_lost_in_text_extraction duration_not_stated carbon_partly_commercial_sugar ph_not_stated volume_not_stated grouped_conditions
derived_from_percent_changes""".split())

def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def num(x):
    try: return float(x)
    except Exception: return None

def close(a, b, tol=0.03): return abs(a - b) <= tol * max(abs(a), abs(b), 1e-9)

def lint(path, studies=None, others=(), legacy=False):
    out = []
    def err(m): out.append(("ERROR", m))
    def warn(m): out.append(("WARN", m))
    raw = open(path, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"): warn("file starts with a BOM")
    if raw.count(b"\n") != raw.count(b"\r\n"): warn("line endings are not all CRLF")
    if not raw.endswith(b"\n"): warn("file does not end with a newline")
    rows = load(path)
    with open(path, newline="", encoding="utf-8-sig") as f:
        header = next(csv.reader(f))
    if header != REC_COLS: err(f"header differs from the 38-column record header: {[h for h in header if h not in REC_COLS]} extra, {[h for h in REC_COLS if h not in header]} missing")
    seen = {}
    for r in rows:
        rid = r["record_id"]
        if rid in seen: err(f"{rid}: duplicate record_id")
        seen[rid] = 1
    for p in others:
        dup = {r["record_id"] for r in load(p)} & set(seen)
        if dup: err(f"record_ids already present in {p}: {sorted(dup)[:5]}")
    sids = {s["study_id"] for s in load(studies)} if studies else None
    for r in rows:
        rid = r["record_id"]
        if sids is not None and r["study_id"] not in sids: err(f"{rid}: study_id {r['study_id']} not in studies file")
        if r["record_type"] not in RECORD_TYPES: err(f"{rid}: record_type '{r['record_type']}'")
        if r["grade"] not in GRADES: err(f"{rid}: grade '{r['grade']}'")
        vv = VEGAN | (VEGAN_LEGACY if legacy else set())
        if r["vegan_status"] not in vv: err(f"{rid}: vegan_status '{r['vegan_status']}'")
        for c in NUMERIC:
            v = r[c].strip()
            if v and num(v) is None: (warn if legacy else err)(f"{rid}: {c} is not a plain number: '{v[:30]}'")
        n, V, T, A, M, C, R = (num(r[k]) for k in ("yield_g_per_L_norm", "volume_mL", "yield_total_g_derived", "surface_area_cm2", "yield_mg_per_cm2_derived", "carbon_declared_g_per_L_derived", "bc_to_declared_carbon_ratio_derived"))
        fl = [t for t in re.split(r"\s*;\s*", r["reliability_flags"].strip()) if t]
        if None not in (n, V, T) and not close(n * V / 1000, T): err(f"{rid}: yield_total {T} vs g/L x mL/1000 = {n*V/1000:.4g}")
        if None not in (T, A, M) and not close(T / A * 1000, M): err(f"{rid}: mg/cm2 {M} vs total/area x 1000 = {T/A*1000:.4g}")
        if None not in (n, C, R) and C and not close(n / C, R): err(f"{rid}: ratio {R} vs norm/carbon = {n/C:.4g}")
        if R is not None and R > 0.6 and "mass_balance_exceeds" not in fl: err(f"{rid}: ratio {R} above 0.6 without mass_balance_exceeds")
        if "mass_balance_exceeds" in fl and (R is None or R <= 0.6): err(f"{rid}: mass_balance_exceeds with ratio {R}")
        if n is not None and not re.search(r"dr(y|ied)", r["yield_basis"].lower()): err(f"{rid}: normalised g/L filled but yield_basis has no dry/dried")
        if r["record_type"] == "observation" and num(r["yield_reported_value"]) is not None and n is None: warn(f"{rid}: numeric reported value but no normalised g/L")
        for t in fl:
            if t not in FLAGS: (warn if legacy else err)(f"{rid}: flag token not in vocabulary: {t}")
            elif t != "n1" and (re.search(r"\d", t) or len(t) > 40): warn(f"{rid}: flag token looks like free text: {t}")
    if studies:
        cnt = {}
        for r in rows: cnt[r["study_id"]] = cnt.get(r["study_id"], 0) + 1
        for s in load(studies):
            if str(cnt.get(s["study_id"], 0)) != s["n_records"].strip(): err(f"{s['study_id']}: n_records {s['n_records']} vs actual {cnt.get(s['study_id'], 0)}")
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("records"); ap.add_argument("--studies"); ap.add_argument("--against", nargs="*", default=[]); ap.add_argument("--legacy", action="store_true")
    a = ap.parse_args()
    res = lint(a.records, a.studies, a.against, a.legacy)
    for sev, m in res: print(f"{sev}: {m}")
    e = sum(1 for s, _ in res if s == "ERROR"); w = len(res) - e
    print(f"{len(load(a.records))} records checked: {e} error(s), {w} warning(s)")
    sys.exit(1 if e else 0)
