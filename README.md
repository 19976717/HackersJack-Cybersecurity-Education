# HackersJack: Major Revision and Reproducibility Kit

**Manuscript:** Evaluating HackersJack Cybersecurity Education: A Pre-Post Study of Grade 5 and 6 Students in Australia  
**Reviewer report supplied:** `CHBR-D-26-02126-reviews.pdf`, comments from Reviewer 1 and Reviewer 3, October 2026.  
**Status:** Analysis reproducibility independently checked against 12 supplied class workbooks; all checked primary statistics agree with manuscript rounding. **This is not an assertion that every reviewer concern is resolved.**

## Read first

1. Read `docs/01_ACTION_PLAN.md` for the exact order of work.
2. Read `docs/02_SOURCE_DATA_AND_METHODS.md` to understand the actual Excel layout and matching.
3. Read `docs/03_REVIEWER_RESPONSE_DRAFT.md` and fill all `[CONFIRM]` fields before submission.
4. Read `docs/04_PRIVACY_AND_GITHUB.md` before any publication or sharing.
5. Read `docs/05_VERIFICATION_RESULTS.md` for the audit results already obtained.
6. Use `docs/06_SUBMISSION_CHECKLIST.md` before resubmitting.

## What this package contains

- Working Python pipeline (`scripts/pipeline.py`) that reads the original two-sheet class workbooks, matches records, computes statistics, and compares rounded outputs with the manuscript.
- Unit tests (`tests/test_pipeline.py`) and a GitHub Actions configuration that runs tests **without** private data.
- Data dictionary, reviewer-by-reviewer response drafts, ethical data-sharing decision tree, detailed implementation guide, reproducibility audit, and submission checklist.
- Aggregated statistical results only. **No original student-level spreadsheets are included.**

## Quick start (on a computer authorised to handle the student records)

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
```

Place exactly the 12 original, approved workbooks in `data/private_original/` (not their multiple uploaded duplicate versions), then:

```bash
python scripts/pipeline.py --input data/private_original --output outputs
```

Exit code `0` means all **selected reported values** match at displayed precision; exit code `2` means at least one discrepancy. A matching result does **not** verify the original answer keys, assessment administration, ethics procedures, or causal inference.

### Source workbooks used for the independent audit

Six Grade 5 classes: JD, KB, KS, OM, RS, SH.  
Six Grade 6 classes: GS, JK, JT, KH, KW, SH.

The audit used the 12 uploaded copies whose filenames end with `(3).xlsx`, and the copies were kept outside this package. The workbooks are **not** included in the ZIP for child-data protection.

### Privacy warning

The source workbooks contain student codes with alphabetic prefixes and numbers. They are **pseudonymised, not guaranteed anonymous**. Do not publish or upload the original workbooks, individual responses, student-code mappings, or unreviewed small-cell tables. A GitHub private repository is not automatically sufficient authorisation to upload restricted child data.

### Scope and accuracy

The script implements the matching and complete-score eligibility evident in the source workbooks. It does not infer unavailable study details such as actual question wording, pre/post equivalence, dates, consent/assent, teacher count, instructional dosage, or whether a delayed test was conducted. Those must be confirmed from records or acknowledged as unavailable.
