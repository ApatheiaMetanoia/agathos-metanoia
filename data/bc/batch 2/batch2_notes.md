# BC atlas: batch 2 notes (1 Nov 2026)

Rules applied: README v0.2 and schema.md as pushed; open access only; figure digitising parked (no grade B used); vegan rule v1.1 per record.
Extractor: Claude instance 1. QA: not sampled yet. No records dropped under rule v1.1.

## Result
37 records across 5 studies: 20 observations with a dry-mass g/L value, 17 text endpoints (no usable mass yield). Vegan status: 11 clear, 26 flag-unspecified.

| study | screening ID | records | numeric yields | still needed |
|---|---|---|---|---|
| COS17 Costa 2017 | P-02 | 19 (13 observations, 6 no-growth endpoints) | 13 | nothing for pass 1 |
| NAR18 Narh 2018 | P-08 | 4 text endpoints | 0 | Fig. 4 digitising (parked) |
| MAC18 Machado 2018 | C1-02 | 7 (6 observations, F0 as text) | 6 | F0 from Fig. 1 (parked); DOI from the PDF header |
| SOU21 Souza 2021 | C1-01 | 6 (1 observation, 5 text) | 1 | Tables 1 and 2 from the PDF (not retrievable by the text tools) |
| IRH26 oil palm trunk sap | C3-04 | 1 text endpoint | 0 | nothing: the paper reports thickness, not mass |

## Judgment calls (each reversible)
1. C3-04 (oil palm trunk sap) is deep-B in the screening log; it was named in the request, so it was extracted. The deep-A oil palm item is C3-03 (frond juice), not extracted.
2. NAR18 keeps peptone in every medium (named 'bacto-peptone' in Methods, origin unstated). Kept with flag-unspecified rather than dropped; Bacto-brand peptone is generally animal-derived (general knowledge, verify), so this could be moved to dropped_records.csv.
3. MAC18 and SOU21: the production media list no peptone, but the pre-inoculum broth does (10% v/v). Flagged on every record; if inoculum carry-over should not count, 13 records become clear.
4. COS17 effluent media are flag-unspecified (composition not itemised). No-growth results are kept as text endpoints with no numeric yield.
5. Declared carbon follows batch 1: glucose, molasses sugars at the paper's stated fraction (MAC18: 69.5%), ethanol as stated. Corn steep liquor and coffee-ground carbon are not counted, which is why COS17-R15 shows 0.642 and carries mass_balance_exceeds.
6. g/L denominators: COS17 uses 100 mL; MAC18 uses 50 mL (45 mL medium + 5 mL inoculum; 45 mL would lower totals by 10%); SOU21-R05 uses 101 mL for the total.
7. Properties (FTIR, XRD, tensile, WHC, TGA) were not extracted for any paper (pass 2).

## New flags to add to schema.md
- composition_incomplete: some medium components are not stated.
- composition_inconsistent: amounts conflict between sections of the paper.
- control_yield_not_in_text: the control exists but its yield is not printed in the text.
- detection_limit_unstated: a dash or 'no BC' with no detection limit.
- error_exceeds_mean / error_term_undefined: the printed error is larger than the mean / is not defined as SD or SE.
- figure_only_yield: the yield is only in a figure (digitising parked).
- nitrogen_method_not_described, preparation_not_described, starter_not_described: a method or input is used but not described.
- no_mass_yield / qualitative_study: thickness or qualitative outcome only.
- ratio_claim_wet_basis: a headline ratio uses hydrated mass while dry mass tells a different story.
- table_not_captured: a table the record depends on could not be read.
- temperature_not_stated: incubation temperature missing.
- vessel_geometry_inconsistent: vessel volume or diameter differs between sections.
- yeast_extract_replacement_unclear: unclear whether yeast extract was actually replaced.

## Contradictions and oddities for the QA pass
- COS17: the '73% of HS' claim is hydrated mass; on dry mass Alt. 14 (9.63) beats HS (8.00 g/L). Vessel 250 mL (Methods) vs 500 mL (Results); diameter printed as 7.50 mm but 44.17 cm2 implies 7.50 cm. Citric acid 0.15% in text vs 1.5% in captions. Wet:dry ratio 25-118.
- NAR18: duration 7 d vs 9 d; steps labelled 0%, 100% and '150' while nitrogen indices are 1x, 2x, 3x; DSC sample B labelled S=3 but described as the 1:1 ratio.
- MAC18: F0 is similar to F2-F5 in the abstract but among the lowest in Section 3.3.
- SOU21: six media listed but 'three' stated; amounts conflict (list vs recipe); hydrolysis 67 C vs 68 C; production temperature missing.
- IRH26: thickness 2.5 cm vs 1-2.5 cm; printed mean 133.606 g/g vs 132.6 from the three values; XRD peaks differ between abstract and text.

## Suggested QA sample
COS17-R15 (best medium, mass-balance flag), COS17-R03 (error above mean), MAC18-R04 (F3), SOU21-R05 (11.08 g/L), NAR18-R04 (relative yield).

## Merge into data/bc (from that folder)
Check that records.csv ends with a newline (`tail -c 2 records.csv | xxd` should show 0d0a), then:
    tail -n +2 records_batch2.csv >> records.csv
    tail -n +2 studies_batch2.csv >> studies.csv
    tail -n +2 inputs_batch2.csv >> inputs.csv
Then update by hand:
- README: contents become 10 studies, 95 records; COS17 full, NAR18, MAC18 and SOU21 partial, IRH26 read in full with no mass yield.
- screening_log.csv extraction status: P-02 full; P-08, C1-02, C1-01 partial; C3-04 read, no mass yield.
- inputs.csv seen_in: IN01 +COS17;MAC18;IRH26 | IN03 +COS17;MAC18;SOU21 | IN04 +MAC18;SOU21 | IN05 +IRH26 | IN06 +COS17;NAR18 (inoculum carry-over in MAC18;SOU21) | IN08 +COS17;NAR18;MAC18 | IN10 +IRH26 | IN11 +COS17 | IN12 +COS17 | IN13 +COS17.
