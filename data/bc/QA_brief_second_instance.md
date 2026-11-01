# QA brief: independent re-extraction of one study (BC evidence atlas)

You are the second Claude instance. Your job is to re-extract ONE study from scratch, without seeing the first instance's values, so the project can measure extraction accuracy. Do not open records.csv, studies.csv or any other file from the project's data folder before you finish. Work only from the paper and this brief.

## Assigned study (seeded random draw, seed 20261026, from the three fully extracted studies)

GHO22: Ghozali et al. 2022, "Influence of Glucose, Urea and Bacteria Concentration on Yield and Carbon Conversion of Nata De Cassava Prepared Using Liquid Tapioca Waste Medium", Jurnal Sains Materi Indonesia 24(1).
DOI: 10.17146/jsmi.2022.24.1.6669
Open PDF: https://jurnal.batan.go.id/index.php/jsmi/article/download/6669/pdf
(If the link fails, ask the project owner to upload the PDF.)

## Deliver

1. A CSV with exactly this header, one row per production condition or reported outcome in the paper:
record_id,study_id,record_type,condition_label,lever_family,strain,culture_format,volume_mL,surface_area_cm2,depth_cm,temperature_C,pH_start,pH_end,duration_d,inoculum,medium_summary,carbon_sources,nitrogen_sources,additives,yield_reported_value,yield_reported_unit,yield_basis,yield_g_per_L_norm,productivity_g_per_L_day,yield_total_g_derived,yield_mg_per_cm2_derived,yield_on_substrate_reported,carbon_declared_g_per_L_derived,bc_to_declared_carbon_ratio_derived,replicates_n,variance_reported,vegan_status,vegan_flag_inputs,wa_tags,grade,reliability_flags,source_location,notes
2. A short note listing anything ambiguous or contradictory in the paper, and any field you had to leave blank.

## Rules (protocol v1.1, summarised)

- Copy numbers exactly as printed. Do not round, correct or "fix" them. Record the unit exactly as printed.
- Leave a field blank if the paper does not state it. Do not guess.
- Check how every yield or ratio is DEFINED (numerator, denominator, weight basis, drying) and write that down in `yield_basis` and `yield_on_substrate_reported`.
- Fill `yield_g_per_L_norm` only for dry-weight values, or for a plain unit change (for example g per 100 mL to g/L), and flag the basis if it is not confirmed.
- `_derived` fields are computed from reported values; state any assumption in `notes`.
- Vegan status per record: clear, or flag-unspecified (origin not stated, e.g. plain "peptone"), or dropped (known animal-derived input). Tag each essential input for provisional West African availability in `wa_tags`.
- Grade: A for numbers printed in the text or tables. Do not digitise figures in this task.
- Reliability flags: use the tokens n1, no_variance, no_control, basis_unconfirmed, denominator_unclear, mass_balance_exceeds, per_litre_inflated, outlier_check and similar. Say what each flag rests on in `notes`.
- Check internal consistency between table columns and report any mismatch.

## What happens next

The project owner (or the first instance) compares your CSV with the first extraction using tools/qa_compare.py, classifies each difference as transcription, interpretation or omission, and records agreement rates. Disagreements are resolved by a human, not by either instance.
