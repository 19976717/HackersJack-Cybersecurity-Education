# Detailed, ordered major-revision action plan

## Phase A — Confirm the editorial scope (Day 1)

1. Read the actual editor decision letter separately from the reviewer PDF. The provided PDF contains reviewer comments, **not** a visible formal acceptance decision. Do not write “accepted pending major revision” in the response unless the editor's letter explicitly uses that status.
2. Confirm the journal/manuscript ID. The review filename begins `CHBR-D-26-02126`, whereas the provided LaTeX manuscript declares *Computers & Education Open*. **Verify these refer to the same submission before preparing the final cover response.**
3. Make a copy of the submitted manuscript and freeze a dated baseline. Record its file SHA-256. Keep original research files read-only.
4. Create a revision log with columns: reviewer, exact comment, manuscript change, supplement change, response, verified by, status.

## Phase B — Validate the source data (Day 1–2)

1. Use only one authoritative copy of each of the 12 workbooks; do not mix `(1)`, `(2)`, `(3)` copies. Confirm the chosen copies with the data custodian.
2. Store the 12 originals on an access-controlled local or institutional drive, outside the Git repository.
3. Generate SHA-256 hashes of the originals (the pipeline outputs `source_checksums.json` locally).
4. Inspect both worksheets in each workbook. There are 20 MCQ columns and 10 True/False columns. Sections are marked `Pre Assessment` and `Post Assessment`.
5. Check that scores use binary 0/1 and distinguish `absent`, blanks and other unavailable values from a genuine incorrect response.
6. Match records using **grade + class + student code + assessment component**. Never match a code globally across all classes.
7. Exclude incomplete occasions for the relevant outcome; combined requires both components at both occasions.
8. Run `python scripts/pipeline.py --input data/private_original --output outputs`.
9. Check `outputs/verification.csv`; compare the reported N, means, gains, t and dz. Document any discrepancy rather than altering the data or target values.
10. Keep an audit trail of who performed the verification and when. Do not circulate row-level data.

## Phase C — Validate instrument and study procedures (Day 2–4)

1. Obtain the actual pre- and post-assessment questionnaires and answer keys from the school/program team. Determine whether item text, ordering and answers were identical. Do not assume identity from identical Q1–Q20 / Q1–Q10 column labels.
2. If identical: explicitly acknowledge recall/repeated-testing as an alternative contributor to the gain; do not assert that all gain represents retained or transferable knowledge.
3. If different: document instrument equivalence, mapping and any evidence of comparable difficulty. If none exists, say so and qualify interpretation.
4. Confirm assessment dates, interval between tests, number of sessions, lesson duration, number of teachers, classroom roles, whether activities were assigned or self-selected, and whether any regular cyber lessons were concurrent. Only report records actually supported by logs, timetables, or school confirmation.
5. Verify ethics approval wording, parental permission and child assent procedures from the approved protocol and records. Do not infer either from an ethics approval statement.
6. Determine whether follow-up assessment or pupil-experience survey exists. If none, state not collected; do not invent retrospective data.
7. Verify whether a comparison group was feasible or approved. Explain why it was not included as an implementation fact if documented; otherwise state only that none was included.

## Phase D — Supplementary materials (Day 4–6)

Prepare S1: Dataset description + data dictionary + eligibility/missing-data rules.  
Prepare S2: Code and reproducibility instructions + software versions + source-file hash manifest (internal if filenames sensitive).  
Prepare S3: Aggregate statistics, component/grade tables, and optionally item-level summaries **only after disclosure review**.  
Prepare S4: Original instruments and administration protocol **only if available and release permitted**.

If raw records cannot be released, give a precise, truthful Data Availability statement. Consider controlled-access review through the institution if permitted. Do not promise raw data to reviewers without approval.

## Phase E — Manuscript revisions (Day 6–9)

1. Expand Methods with a compact, factual workflow: school(s), classes, roles, timing, intervention exposure, instrument administration, item identity/equivalence, matching and missingness.
2. Distinguish **observed gain** from **program-attributable causal effect** throughout title, abstract, results, discussion and conclusion.
3. Explain high post scores (28.67/30) as possible ceiling effects; do not interpret very large dz as proof of generalised behavioural change.
4. Explain Grade 6 lower baseline descriptively; avoid unsupported explanations about teacher administration or student composition.
5. Add limitations on test familiarity, absent control group, unmeasured engagement, no delayed retention and no behavioural outcomes.
6. Add a short, explicit answer to each RQ and an expanded practical implication for schools.
7. Put each RQ on a separate line, clarify HackersJack existed before the study if confirmed, and consider moving curriculum context earlier as Reviewer 3 suggests.
8. Cross-reference each supplementary file accurately. Do not state that code or data are public before they actually are.

## Phase F — Independent check and resubmission (Day 9–11)

1. Ask a coauthor or independent statistician to run the pipeline on an authorised machine and sign the audit log.
2. Run tests, compare output to paper and review changes for privacy.
3. Have the school/program owner verify procedural descriptions.
4. Have the ethics/data custodian approve any data release.
5. Complete the point-by-point response with page/line references from the revised manuscript.
6. Submit revised manuscript, tracked changes if requested, response letter and approved supplements through the journal portal before deadline.

## What **not** to do

- Do not change individual records or calculations merely to force agreement with reported values.
- Do not add fictitious delayed tests, surveys, control groups, teacher counts or hardware benchmarks.
- Do not publish identifiable or pseudonymised student-level records without permission and disclosure-risk assessment.
- Do not imply that GitHub or automated tests independently establish educational validity or causality.
