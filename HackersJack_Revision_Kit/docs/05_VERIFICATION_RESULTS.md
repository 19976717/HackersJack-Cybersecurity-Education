# Independent verification performed on the 12 supplied workbooks

**Audit completed:** 29 October 2026, using the twelve uploaded `(3).xlsx` copies and `scripts/pipeline.py` with `artifact_tool` for spreadsheet reading and SciPy for t distribution calculations. The original workbooks were not included in this ZIP.

| Outcome | N | Pre M (SD) | Post M (SD) | Gain | t(df) | dz | 95% CI gain |
|---|---:|---|---|---:|---|---:|---|
| Combined | 216 | 21.61 (2.45) | 28.67 (1.74) | 7.06 | 40.17 (215) | 2.73 | 6.71–7.41 |
| MCQ | 225 | 14.61 (1.95) | 19.09 (1.23) | 4.48 | 31.49 (224) | 2.10 | 4.20–4.77 |
| True/False | 231 | 7.04 (1.15) | 9.58 (0.91) | 2.53 | 28.50 (230) | 1.88 | 2.36–2.71 |
| Grade 5 combined | 107 | 22.44 (2.13) | 28.81 (1.07) | 6.37 | 28.46 (106) | 2.75 | 5.93–6.82 |
| Grade 6 combined | 109 | 20.79 (2.49) | 28.52 (2.21) | 7.73 | 30.33 (108) | 2.91 | 7.23–8.24 |

**Result:** Every checked main outcome statistic (N, pre mean, post mean, gain, paired t and dz) agrees with the manuscript at the precision reported. Two automated unit tests also passed. Full precision values are in `data/public_aggregates/statistical_results.csv`; check-by-check results in `docs/verification.csv`.

**Observed record completeness:** MCQ pre valid 257 / unavailable 32; MCQ post valid 251 / unavailable 38. TF pre valid 259 / unavailable 30; TF post valid 255 / unavailable 34. These are per-component records present in the sheets, **not** participant recruitment or attrition counts. Do not treat 289 as a confirmed recruitment denominator.

**Important qualifications:** This is an arithmetic/processing audit of the supplied workbooks, not an independent verification of school administration or item equivalence. The Grade 6 JK workbook has an internal sheet naming inconsistency (`6SH`), requiring source-owner confirmation. The script does not claim to have verified consent/assent, exact assessment items, instructional schedule or teacher roles. Full source file hashes were generated locally, not published in the package.

## How to report verification

“An independent computational audit of the 12 original class workbooks reproduced the reported matched sample sizes and the main descriptive and inferential statistics to the manuscript's displayed precision. The audit code, eligibility rules and summary outputs are supplied as supplementary materials. The analysis does not resolve the absence of a control group, potential repeated-testing effects, or uncertainty regarding longer-term knowledge retention.”
