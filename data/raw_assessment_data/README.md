# HackersJack Cybersecurity Education — Assessment Dataset

## Dataset Overview

This directory contains the de-identified assessment datasets used in the study *Evaluating HackersJack Cybersecurity Education: A Pre-Post Study of Grade 5 and 6 Students in Australia*.

The dataset comprises 12 Excel workbooks representing six Grade 5 classes and six Grade 6 classes.

## Assessment Structure

The study used pre- and post-assessments consisting of:

* 20 multiple-choice questions.
* 10 True/False questions.
* A maximum combined score of 30 points.

Correct answers were assigned a score of 1, while incorrect answers were assigned a score of 0. Missing or unavailable observations were distinguished from incorrect responses during data preparation.

## Analytical Sample

The matched analytical samples were:

| Assessment                 | Matched students |
| -------------------------- | ---------------: |
| Combined assessment        |              216 |
| Multiple-choice assessment |              225 |
| True/False assessment      |              231 |

The different sample sizes reflect the availability of matched assessment records for each component.

## Data Processing

The analysis workflow documents:

1. Reading the original Excel workbooks.
2. Identifying grade and class information.
3. Matching pre- and post-assessment records.
4. Applying assessment scoring rules.
5. Identifying missing and incomplete observations.
6. Calculating descriptive statistics.
7. Conducting paired-samples statistical tests.
8. Comparing calculated results with the manuscript.

## Reproducibility

The Python scripts and automated tests are available in the repository's `scripts/` and `tests/` directories.

## Data Availability

These datasets are intended to support independent verification of the reported analyses. Public availability is subject to confirmation that the released files comply with the study's research ethics approval, applicable institutional requirements, and relevant data-sharing permissions.

## Research Limitations

The study used a single-group pre-post design without an untreated comparison group.

The results demonstrate changes in measured cybersecurity knowledge but do not independently establish causal effects, long-term knowledge retention, or changes in real-world cybersecurity behaviour.

