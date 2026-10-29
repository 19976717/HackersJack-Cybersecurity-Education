# Privacy, GitHub and reproducibility publication protocol

## Before publishing anything

1. Consult the approved ethics protocol, institution data custodian, and school agreements.
2. Check whether research records may be disclosed to editors/reviewers and whether open public release is permitted.
3. Treat alphanumeric student codes as pseudonymous, **not** safely anonymous; they may contain patterns resembling initials.
4. Do not push raw workbooks to GitHub, including to a private repository, without explicit authorisation and appropriate access controls.
5. Review any aggregated outputs for small-group or item-response disclosure risks. Consider suppression or pooling where appropriate.
6. Keep original data in approved secure storage and access logs.

## Create repository safely

1. Create a new private GitHub repository named `hackersjack-prepost-reproducibility`.
2. Copy only this kit's code, documentation and approved aggregate outputs to the repository. The `.gitignore` excludes `data/private_original/` and `outputs/`.
3. Check `git status` and `git diff --cached --name-only` before committing. Also check for spreadsheets in the index: `git ls-files '*.xlsx' '*.xls' '*.csv'`.
4. Remove any non-approved aggregate files before making repository public.
5. Run unit tests on GitHub Actions; it uses synthetic data and does not require original child data.
6. Have an independent authorised analyst run the full pipeline **locally** using the original files.
7. Capture version, commit SHA, dependencies and test outcomes in the supplement.
8. If permitted, publish code and non-sensitive outputs, optionally archive a release with a permanent DOI (e.g. an institutional repository or Zenodo). Never claim a DOI until one exists.

## Terminal steps

```bash
git init
git add README.md LICENSE requirements.txt scripts tests docs data/public_aggregates .github .gitignore
git status
git commit -m "Add documented reproducibility pipeline and reviewer support materials"
# Create a private repository through the GitHub interface, then follow its exact remote instructions.
# git remote add origin <YOUR_ACTUAL_PRIVATE_REPOSITORY_URL>
# git branch -M main
# git push -u origin main
```

## Options for data availability (select only the true one)

**Option A — approved open release:** “An anonymised dataset and analysis code are available at [actual repository DOI/URL].” Only if approved, deposited and checked.

**Option B — controlled access:** “Individual-level assessment data are not publicly available because the study involved minors and is subject to ethics and school data-governance conditions. Requests for controlled access may be considered by the corresponding author and responsible data custodian, subject to applicable permissions. Analysis code, a data dictionary, and non-disclosive aggregate results are available at [actual link].” Use only if access requests genuinely can be considered.

**Option C — no individual access:** “Individual-level assessment records are not available for public release because they concern school-aged participants and are governed by the approved ethics protocol and institutional/school data-sharing restrictions. The accompanying supplementary materials provide the data dictionary, scoring and matching rules, analysis code and aggregate results.”

## What code can and cannot establish

Code plus source data can reproduce arithmetic, eligibility and statistical tests. Code cannot validate the original questionnaire content, rule out practice effects, prove consent was obtained, measure retention, or create a missing control group.
