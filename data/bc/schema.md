# Schema

## records.csv

| Field | Meaning |
|---|---|
| record_id | study id + running number, e.g. GHO22-R12 |
| study_id | key into studies.csv |
| record_type | observation / model_prediction / property / text_endpoint |
| condition_label | the paper's own label where it has one |
| lever_family | medium (carbon, nitrogen, additive), organism and inoculum, culture format and conditions, culture geometry |
| strain | species and strain id as reported |
| culture_format | static surface, agitated (rpm), reactor, vessel type |
| volume_mL, surface_area_cm2, depth_cm | geometry as reported; blank if not stated |
| temperature_C, pH_start, pH_end, duration_d | conditions as reported |
| inoculum | amount and basis as reported |
| medium_summary, carbon_sources, nitrogen_sources, additives | composition with concentrations as reported |
| yield_reported_value, yield_reported_unit | the value and unit exactly as printed |
| yield_basis | dry or wet, drying conditions, anything affecting comparability |
| yield_g_per_L_norm | normalised dry-weight yield, g/L (see rule 4) |
| productivity_g_per_L_day | as reported |
| yield_total_g_derived | total BC per vessel = g/L x volume (derived) |
| yield_mg_per_cm2_derived | BC per unit surface area = total / area (derived; only when area is stated) |
| yield_on_substrate_reported | yield coefficient or conversion ratio as reported, with its denominator |
| carbon_declared_g_per_L_derived | declared fermentable carbon sources summed (derived; assumptions in notes) |
| bc_to_declared_carbon_ratio_derived | yield_g_per_L_norm / carbon_declared (derived; above about 0.6 is flagged) |
| replicates_n, variance_reported | replication and spread as reported |
| vegan_status | clear / flag-unspecified / dropped (see dropped_records.csv) |
| vegan_flag_inputs | the inputs behind a flag |
| wa_tags | provisional West African availability per essential input |
| grade | A / B / C / D / own |
| reliability_flags | see below |
| source_location | table, figure or section |
| notes | anything a reader needs |

## Reliability flags

n1 (single run, no replicates) / no_variance / no_control (no control isolating the tested input) / basis_unconfirmed (dry or wet not stated) / denominator_unclear / mass_balance_exceeds (BC larger than a plausible conversion of the declared carbon) / per_litre_inflated (small volume inflates g/L) / outlier_check / abstract_only / volume_inconsistent / contradiction_in_text / pasteurised_not_sterilised / carbon_labelled_glucose_vs_sugar / film_state_hydrated_or_dried_not_stated / pass2_field / temperature_and_volume_lost_in_text_extraction / prediction_not_observation.

## studies.csv, inputs.csv, dropped_records.csv, screening_log.csv

Column names are self-explanatory; see the first row of each file. `qa_status` in studies.csv records whether a study was in the QA sample and the agreement found.
