# Bacterial cellulose evidence atlas: working data (v0.2)

Status: work in progress (2026-10-26). Not for citation yet. Everything here is a working copy that a human has not yet fully checked.

## What this is

An open, cited, graded table of reported bacterial cellulose (BC) production results, built from the primary literature. Pass 1 covers production levers: medium (carbon, nitrogen, additives), organism and inoculum, culture format and conditions. Post-processing is pass 2. The table is meant to feed a later model and a site section; it is not a recommendation list.

Current contents: 5 studies, 58 records. Three studies are fully extracted (GHO22, PRU17, ZHA22), one is partial (AKI22) and one is abstract-level (ROD19). The screening queue has 70 entries (screening_log.csv).

## Rules (protocol v1.1)

1. Inclusion: primary experimental BC production data with numbers.
2. Vegan, per record: a record is dropped if its medium contains a known animal-derived input. Vegan records from the same study are kept. Unspecified origin (for example plain "peptone") is kept with a warning flag in `vegan_status` and `vegan_flag_inputs`. Dropped records are listed in `dropped_records.csv`.
3. West African availability: tagged per input (`inputs.csv`, `wa_tags`), including enzymes and other processing aids. The atlas keeps every study. The hard requirement applies only when something is recommended.
4. Units: the reported value and unit are kept as found. `yield_g_per_L_norm` is filled only for dry-weight values (or a plain unit change such as g per 100 mL to g/L, flagged). Wet weight is never converted without a measured ratio.
5. Grades: A = number in a primary paper's text or table (abstract-only records carry the flag `abstract_only`); B = digitised from a figure, with an overlay checked by a human; C = second-hand; D = analogy or assumption; own = a measurement from the owner's own jar runs.
6. Fields ending in `_derived` are computed by the extractor from reported values, with assumptions stated in the notes. They never overwrite reported fields.
7. Reliability flags (semicolon-separated) say why a number may mislead: n1, no_variance, no_control, basis_unconfirmed, denominator_unclear, mass_balance_exceeds, per_litre_inflated, outlier_check, abstract_only, and similar. See schema.md.

## Files

| File | What it holds |
|---|---|
| studies.csv | one row per study, with access, licence, extraction status and study-level flags |
| records.csv | one row per condition or outcome, with the fields defined in schema.md |
| inputs.csv | every input seen, with vegan status and a provisional West African availability tag |
| dropped_records.csv | what was dropped or excluded, and why |
| screening_log.csv | the pass-1 screening queue (70 entries, with decisions) |
| QA_brief.md | the brief for the second instance that re-extracts a sample |
| tools/qa_compare.py | first-pass comparer for the two extractions |

## Workflow

1. Instance 1 extracts studies into records.csv and studies.csv.
2. A second instance re-extracts a seeded random sample without seeing instance 1's values (QA_brief.md).
3. Differences are classified as transcription, interpretation or omission and resolved by a human. Agreement rates are recorded in studies.csv (`qa_status`).
4. Only reviewed releases are copied into `public/bc/data/`. Nothing in this folder is served by the site.

## Where it lives

`data/bc/` at the repository root. `wrangler.jsonc` serves only `./public`, so this folder is not deployed. The repository is public, so pushed files are readable on GitHub.

## Licence (provisional)

Compiled data: CC BY-NC-SA 4.0, matching the site's content licence. Extracted facts come from the cited papers, which keep their own licences, so cite them. Any scripts: AGPL-3.0-only. This is a proposal, not a decision.

## Known limits (v0.2)

- Only GHO22, PRU17 and ZHA22 were read in full text. Most screening-log numbers come from abstracts and snippets.
- Figure-only values are not extracted yet. Digitising needs the PDF inside the working environment.
- Some PDF text extraction lost digits (ZHA22 temperature and flask volume). Check the original PDF.
- Availability tags are provisional judgements, not production statistics.
