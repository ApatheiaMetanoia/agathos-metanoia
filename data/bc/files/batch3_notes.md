# Batch 3 notes (BC evidence atlas, pass 1)

Extractor: Claude instance 1 (first pass). Date: 2026-11-07. Text came from the PubMed Central text feed (through the PubMed connector), MDPI HTML pages and one PubMed abstract. Licences come from PubMed's licence record where it exists. Paper figures could not be read in this environment, so nothing here is digitised.

## 1. What is in this batch

| Study | Paper (screening ID) | Access, licence | Records | Status |
|---|---|---|---|---|
| AND18 | Andritsou 2018, ACS Omega (C2-06) | open, CC BY | 6 | partial: Fig. 1 time-courses are figure-only |
| LIN22 | Lin 2022, Foods (P-03) | open, CC BY 4.0 | 18 | partial: most yields are figure-only, relative gains printed |
| SAY25 | Sayah 2025, Foods (C3-01) | open, CC BY 4.0 | 19 | partial: Tables 1 and 4 not captured |
| TSE22 | Tseng 2022, J Food Sci Technol (C2-01) | NOT open access | 4 | abstract only |
| UGU24 | Ugurel and Ogut 2024, Fibers (P-07) | open, CC BY | 17 plus 27 time-series points | tables read in full |

Totals: 64 records, 27 time-series points, 13 new inputs (IN27 to IN39), 0 dropped records (no known animal-derived input found; unspecified-origin inputs are flagged). Vegan status counts: {'flag-production-medium': 45, 'clear': 12, 'flag-inoculum-only': 7}.

## 2. Conventions used here (apply the same to batches 1 and 2 at merge)

1. **Vegan split.** `clear` = no unspecified or animal-origin input. `flag-inoculum-only` = an unspecified-origin input (usually peptone) appears only in a starter or seed culture and reaches the production medium as carry-over. `flag-production-medium` = an unspecified-origin input is an ingredient of the production medium itself. `flag-unspecified` is retired.
2. **Numeric columns hold numbers only.** Qualifiers go in `notes` or in flags (`no_replicate_n`, `n1`, `area_not_stated`, and so on).
3. **Flags come from a controlled list only**, no free text. New tokens are defined in section 6.
4. **Time series live in `timecourse_batch3.csv`** (long format: one row per series point; `record_id` points to an anchor record that carries the culture conditions; `method` is table, text, derived_from_text or, later, digitised; `overlay_checked` is n/a, pending or yes). Single-endpoint cultures stay in `records.csv`.
5. **`tools/lint_batch.py`** checks every batch the same way (header, IDs, vocabularies, numeric columns, derived arithmetic, flags, n_records, line endings). Batch 3 passes with 0 errors and 2 warnings (TSE22: reported numbers without a normalised value, because the dry or wet basis is not stated). In `--legacy` mode it reports 135 findings on batch 1 and 79 on batch 2, almost all text inside numeric columns (batch 1: {'pH_start': 27, 'replicates_n': 51, 'surface_area_cm2': 7, 'depth_cm': 7, 'temperature_C': 4, 'volume_mL': 2, 'duration_d': 9, 'productivity_g_per_L_day': 2}; batch 2: {'pH_start': 30, 'replicates_n': 37, 'duration_d': 11, 'temperature_C': 1}) plus undefined flag tokens.

## 3. Judgment calls to confirm or reverse

1. **Amino acids marked `clear`** (IN35, LIN22): supplier and route are not stated; fermentation or synthesis is the usual route for these eight. Mark them `flag-production-medium` if you prefer the strict reading.
2. **LIN22 yeast pre-fermented media and the SC7 co-culture are `flag-inoculum-only`**: the only unspecified-origin input is peptone in the YEPD starter of the yeast, at most about 0.2 g/L in the final medium (2% starter into coconut water, then 50% of that in the medium; extractor arithmetic).
3. **AND18 is `flag-production-medium`** although the paper does not itemise the nitrogen supplement: it says the nutrients were adjusted according to HS, and HS contains peptone.
4. **TSE22 is not open access.** Only the freely visible abstract was used (as with ROD19 in batch 1). Keep it abstract-only, drop it, or swap in C3-02 (Sci Rep, open, in PubMed Central as PMC7044201).
5. **Strain names restored from the screening log or section headings** where the text feed dropped italics (AND18 strain species; LIN22 species). LIN22 yeast genera are unavailable.
6. **UGU24 time series include derived points** (7 d and 15 to 28 d at 8 log, and 7 d at 10.5 log), computed from printed percent changes against the 9.1 g/L anchor. They are flagged `derived_from_percent_changes` and are meant to be replaced by digitised values (W02, W03).
7. **SAY25 factorial corners are placeholders** (yield in Table 1, not captured). The fitted values from the printed uncoded equation are in their notes only; the equation reproduces the printed predicted optimum 6.48 exactly, which is why I read it as uncoded.
8. **LIN22 grouped records** (flag `grouped_conditions`) stand for several conditions that share one statement; digitising should split them.
9. **UGU24-S01 is anchored to R17** although the temperature and pH of the extended runs are not stated.

## 4. Findings worth a second look

**UGU24 (the paper contradicts itself).** Mean of the Table 3 run averages by level: temperature 26/28/30/32 C = 5.59/2.71/3.71/2.96; pH 4/4.5/5/5.5 = 3.45/2.98/4.66/3.88; inoculum 6/8 log = 5.87/1.61; time 7/14 d = 3.71/3.78 g/L. The stated optimum (32 C, pH 5.5, 8 log, 14 d) therefore picks the worse inoculum level by 3.6-fold and a middling temperature, and the text says 26 C gave the lowest yield when Table 3 shows the highest. The best of the 16 runs is run 3 (26 C, pH 5, 6 log, 7 d) at 9.10 g/L, the same number as the headline 9.1 g/L. The printed S/N column equals 20*log10(mean) to within 0.02 dB, not the per-replicate formula printed as Eq. 1. Table 7 at 4 d gives 0.656 g/L (8 log) and 0.4 g/L (10.5 log), a decrease, where the text reports +275%. Methods list 18 to 20 d runs that are not reported; Table 7's 2 to 4 d times are not in the Methods; Fig. 5 values are printed as "g" not "g/L".

**SAY25.** 6.25 g/L (validation) against 6.59 g/L (abstract, discussion, conclusions) at the same optimum. The interaction text gives 2.2 to 5.5 g/L for extract at 2% ethanol; the printed equation gives about 4.4 to 5.4, and the other marginal numbers in that paragraph match the equation to within about 0.25 g/L, so 2.2 is probably a typo. The same 1.8 g/L is the IS22 value in 5 mL tubes at 15 d (Table 2) and the standard medium in the 10 d comparison, and HS is called the lowest medium although the extracts alone are said to be lower.

**AND18.** Peel extracts supply about 92, 81 and 24% of the sugar (orange, grapefruit, lemon; Table 5 arithmetic, assuming undiluted extracts) and the rest is commercial sugar, so the lemon-peel result mostly reflects added sugar. 2.9 g/L at 13 d is 0.22 g/L/day against a quoted "above 0.25". The sampling day of three of the five yields is not stated, nor which dry-weight method (oven or freeze-dried) was used for which sample.

**LIN22.** Controls differ between experiments (1.99 g/L in the low-dose methionine test). The two big gains (+165% SC7-PCW, +207.9% for 3.0% methionine) have no printed absolute value. Methionine is non-monotonic: 0.02% and 0.05% lowered yield, 3.0% raised it.

## 5. Suggested QA sample (blind instance, numeric rows so the comparer can pair them)

UGU24-R03, UGU24-R10, UGU24-R17, AND18-R02, AND18-R03, LIN22-R02, SAY25-R17 and the derived point UGU24-T23. Note: the QA instance should read the papers, not this folder.

## 6. New flag tokens (add to schema.md)

- `names_lost_in_text_extraction`: names, symbols, subscripts or exponents were dropped by the text feed; restored from another source or left unknown.
- `duration_not_stated`: the harvest day of the value is not given.
- `carbon_partly_commercial_sugar`: part of the carbon is added commercial sugar, not the substrate under test.
- `ph_not_stated`, `volume_not_stated`: as named.
- `grouped_conditions`: one record stands for several conditions that share a statement.
- `derived_from_percent_changes`: value computed by the extractor from printed percent changes against an anchor value.
- `no_replicate_n`, `area_not_stated`: used in batches 1 and 2 without a definition. Meaning: replicate number not stated; culture surface area (and depth) not stated.

## 7. Merge (do batch 2 first; files are CRLF, header row first, so `tail -n +2 >>` is safe)

```
cd data/bc
tail -n +2 "batch 2/records_batch2.csv" >> records.csv
tail -n +2 "batch 2/studies_batch2.csv" >> studies.csv
tail -n +2 "batch 2/inputs_batch2.csv" >> inputs.csv
tail -n +2 batch3/records_batch3.csv >> records.csv
tail -n +2 batch3/studies_batch3.csv >> studies.csv
tail -n +2 batch3/inputs_batch3.csv >> inputs.csv
cp batch3/timecourse_batch3.csv timecourse.csv
```
Then: (a) apply the batch 2 notes' own updates (seen_in, schema.md flags, screening-log status) plus these `seen_in` additions to existing inputs:
- IN01: add UGU24;SAY25;LIN22;TSE22
- IN04: add SAY25
- IN05: add SAY25
- IN06: add UGU24;SAY25;LIN22
- IN08: add UGU24;SAY25;LIN22
- IN10: add LIN22
- IN12: add UGU24;SAY25;LIN22
- IN13: add UGU24;SAY25;LIN22
- IN26: add LIN22
(b) remap `flag-unspecified` in batches 1 and 2 with a first-pass script (inoculum, preculture, seed, starter or carry-over only in `vegan_flag_inputs` -> `flag-inoculum-only`, otherwise `flag-production-medium`), then review the list by eye; (c) tidy numeric columns (keep the leading number, move the parenthetical to `notes`, blank plus `no_replicate_n` where none was reported) and replace the undefined or free-text flag tokens; (d) run `python3 tools/lint_batch.py records.csv --studies studies.csv` until it reports 0 errors in strict mode; (e) update README (15 studies, 159 records, 27 time-series points, v0.3) and set the screening-log extraction status for the 15 studies.

**Comparer v2 spec** (for the merge or QA chat): pair rows by normalised `condition_label` token overlap plus identical numeric fields, never by printed yield string; compare all 38 columns except free text; report flag sets as overlap; pair text endpoints by label; print a per-field agreement table.

**Housekeeping:** delete `data/.~lock.BC_atlas_pass1_screening_log_v0.1.xlsx#` and add `.~lock.*#` to a new `.gitignore`; `QA_brief_second_instance.md` is a byte-identical copy of `QA_brief.md`; keep one source of truth for the screening log (the csv) and archive the two xlsx versions; consider renaming `batch 2` to `batch2`.

## 8. Digitising worklist

`digitise_worklist_batch3.csv` lists 10 items (figures to upload and two tables to paste). Highest value: AND18 Fig. 1, UGU24 Figs. 4 to 6, LIN22 yeast and amino-acid figures, SAY25 Tables 1 and 4. Digitised values enter as grade B with `method=digitised` and `overlay_checked=yes` only after you have checked the overlay.
