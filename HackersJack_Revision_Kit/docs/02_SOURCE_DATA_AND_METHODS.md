# Actual source-data layout, data dictionary and analysis protocol

## Observed structure from the supplied Excel workbooks

Twelve original class-level workbooks: Grade 5 JD/KB/KS/OM/RS/SH; Grade 6 GS/JK/JT/KH/KW/SH. Each workbook contains exactly two worksheets, an MCQ sheet and a True/False sheet. Each sheet contains distinct `Pre Assessment` and `Post Assessment` sections, a Q1…Q20 or Q1…Q10 header row, student codes and 0/1 item values. Some cells contain `absent` or are blank. Extra score/total columns appear in some worksheets but are **not used** for scoring by the script. The code recomputes totals from item-level values.

**Observed anomaly:** The Grade 6 JK workbook's internal sheet names include `6SH`, inconsistent with its filename. The pipeline assigns class using the filename and records this discrepancy for manual confirmation. The same grade may contain a separate SH class, so this matters. Verify the class identity from school records before treating the matching as final.

## Data dictionary

| Field | Type | Meaning | Handling |
|---|---|---|---|
| `grade` | integer | Year level, 5 or 6 | From filename |
| `class` | string | Class identifier | From workbook filename; verify anomalous internal sheet names |
| `code` | string | Pseudonymous student code | Confidential; match only within grade and class |
| `kind` | category | `MCQ` or `TF` | From sheet type |
| `occasion` | category | `pre` or `post` | From section heading |
| `Q1`…`Q20` | 0/1 or missing | Correctness for MCQ items | Sum 20 valid item values |
| `Q1`…`Q10` | 0/1 or missing | Correctness for TF items | Sum 10 valid item values |
| `score` | integer or unavailable | Total correct answers | Derived from item-level 0/1 |
| `valid` | Boolean | All expected item values present and binary | Missing/absent invalidates component at that occasion |
| `paired gain` | integer | Post minus pre for matched component | Derived only for valid matched occasions |
| `combined score` | integer | MCQ + TF score | Requires both components pre and post |

## Matching and eligibility

A student is matched on `(grade, class, code, kind)`. A component pair is eligible only when both occasions have all required binary responses. Combined eligibility is the intersection of valid matched MCQ and TF pairs for the same `(grade, class, code)`. Missing and `absent` values are **not** treated as incorrect answers.

The resulting matched Ns independently reproduced from the supplied source workbooks are MCQ 225, TF 231, combined 216, Grade 5 combined 107, Grade 6 combined 109.

## Formulas

For student i and component c, `S_pre = sum(correct_pre_items)` and `S_post = sum(correct_post_items)`. Paired difference `D_i = S_post - S_pre`. `Mean gain = mean(D)`. Sample SD uses denominator `n-1`. Paired `t = mean(D) / (SD(D)/sqrt(n))`, df `n-1`; Cohen `dz = mean(D)/SD(D)`. 95% CI is `mean(D) ± t_critical(0.975, n-1) * SD(D)/sqrt(n)`. Two-sided p-values are from Student's t distribution.

## Key limitations of the available workbook metadata

The workbooks store **scored correctness** (0/1), not the actual question wording, answer options, answer keys, administration dates, teacher names/count, delivery logs, parental consent, child assent or instructional exposure. Identical Q numbers **do not prove** that identical item wording was used at pre and post. These facts must be sourced separately.

## Recommended reporting language

“The analysis used 12 class-specific workbooks containing item-level scored pre- and post-assessment records. Each assessment comprised 20 MCQ and 10 True/False items. Pre/post records were linked within grade and class using pseudonymous student codes. Responses coded 0 and 1 represented observed incorrect and correct answers; missing and absent responses were retained as unavailable. Eligibility was evaluated separately for each component and for the combined 30-item score, yielding matched samples of 225, 231 and 216 respectively. An executable analysis script and supplementary data dictionary document these rules.”

Use the final sentence only after actually including the supplement.
