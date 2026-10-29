# Point-by-point response to reviewers — working draft

**Important:** Replace all `[CONFIRM]`, `[INSERT ...]` and conditional wording with verified facts before sending. Do not claim that supplements or GitHub URLs exist until actually submitted. The review PDF contains repeated Reviewer 1 passages on pages 1–3; answer each unique point once, not the duplicated OCR/layout fragments. This document is a draft, not a final submission-ready response.

## Introductory response to the editor

Dear Editor and Reviewers,

Thank you for your constructive assessment of our manuscript, *Evaluating HackersJack Cybersecurity Education: A Pre-Post Study of Grade 5 and 6 Students in Australia*. We have focused this revision on improving transparency of the original assessment data, reproducibility of the statistical analysis, documentation of the assessment and classroom procedures, and a more explicit discussion of the design's inferential boundaries. An independent computational audit of the twelve original class workbooks reproduced the principal reported statistics to the manuscript's stated rounding precision. We have not altered the original assessment records or the numerical findings. We recognise that computational reproducibility does not resolve the absence of a comparison group, potential repeated-testing effects, or the lack of delayed retention and behavioural measures. Below we describe the manuscript and supplementary-material changes point by point.

## Reviewer 1 — dataset not available (PDF p.1, lines 28–33; repeated p.2)

**Concern:** Dataset unavailable as supplement, limiting verification and reuse.

**Proposed response:** We agree that access to the analytical workflow is essential. We have prepared a reproducibility package describing the source data, a data dictionary, matching and exclusion rules, scoring, executable Python analysis code, and aggregate verification outputs. The original data comprise 12 class-specific workbooks (six per grade), each containing 20 MCQ and 10 True/False scored responses at pre- and post-assessment. The script independently reproduces the matched Ns (225 MCQ, 231 True/False, 216 combined) and the primary reported statistics to displayed precision. Because the data relate to minors and contain pseudonymous codes, individual-level release requires ethics/institutional/school authorisation. [CONFIRM: choose approved release option A/B/C in `04_PRIVACY_AND_GITHUB.md` and state exactly which materials were actually deposited.] The data availability statement has been clarified at [INSERT manuscript page/lines]. Supplementary materials are [INSERT exact names/links].

**Do not claim:** “Dataset publicly available” unless permission, anonymisation and release are complete.

## Reviewer 1 — limitations insufficiently addressed (PDF p.1, lines 34–40)

**Proposed response:** We have expanded the discussion to explain how each limitation affects interpretation of the current results. The absence of a control group prevents attribution of the entire 7.06-point mean gain to HackersJack; repeated assessment may contribute practice effects; the 28.67/30 post mean indicates a potential ceiling effect and reduced sensitivity to additional gains; differences in available component records produce distinct analysis denominators; and unmeasured classroom exposure and instructional fidelity prevent explanatory comparisons across classes. We have therefore restricted conclusions to within-cohort changes in assessed cybersecurity knowledge, not proven behavioural change or causal effectiveness. [INSERT revised page/lines].

## Reviewer 1 — delayed post-test (PDF p.1, lines 41–46)

**Proposed response:** We agree that a delayed assessment would help establish knowledge retention. [CONFIRM whether any delayed assessment exists.] The current study contains pre- and immediate/subsequent post-assessment records only; no delayed follow-up is present in the supplied analytical workbooks. We have made this measurement boundary explicit and identify delayed follow-up as a specific next-step design improvement. We do not infer retention from the current post-test results. [INSERT revised page/lines].

**Do not claim:** a delayed test was performed or long-term retention established.

## Reviewer 1 — student experience survey and real-world practices (PDF p.1, lines 47–54)

**Proposed response:** The approved evaluation and supplied analytical records focused on directly scored cybersecurity knowledge. [CONFIRM whether a survey was planned/collected and why it was not included.] The present data do not include validated measures of satisfaction, confidence, perceived usefulness, cyber-safe behaviour or transfer to daily situations. We now state this distinction explicitly and propose combining knowledge tests with learner feedback and behavioural/scenario measures in future studies. [INSERT revised page/lines].

## Reviewer 1 — same versus different pre/post questions and ceiling effects (PDF p.2, lines 62–67)

**Proposed response, conditional:** We thank the reviewer for identifying this important omission. Both occasions used the same *structure* (20 MCQ plus 10 True/False items), as demonstrated by the original scored workbooks. However, scored 0/1 response sheets alone do not establish whether question wording and answer keys were identical. [CONFIRM by inspecting original questionnaires.] If the same items were used, we will say: “The same items were used at pre and post. Familiarity and recall may therefore have contributed to the gain; without parallel forms or a comparison condition this contribution cannot be isolated.” If different items were used, we will document the item-to-item mapping and evidence of comparable difficulty; if such evidence is unavailable, we will state that as a limitation. We also discuss the post mean of 28.67/30 as a potential ceiling effect. [INSERT exact evidence and manuscript location].

## Reviewer 1 — control group, school/teacher roles and timing (PDF p.2–3, lines 68–73 and 131–145)

**Proposed response:** We agree that the absence of a comparison condition limits causal attribution. The study is a single-group matched pre/post evaluation, not a comparative effectiveness trial. The original analysis cannot isolate contributions from regular instruction, test familiarity, peer discussion or time-varying influences. We have clarified this interpretation. We have also expanded the study setting and administration section to report [CONFIRM: number of schools, number of teachers, who delivered activities, who administered tests, dates and interval, instructions and supervision] from contemporaneous records. Any unavailable procedural details are explicitly identified rather than inferred from item-score workbooks. A future comparison group receiving equivalent content through a different method would improve causal identification. [INSERT revised page/lines].

## Reviewer 3 — Introduction and aims (PDF p.3, lines 155–163)

**Proposed response:** We have expanded the background to discuss the challenges of maintaining up-to-date cybersecurity materials and implementing research in schools. We now clarify whether HackersJack was an existing platform prior to the study [CONFIRM project history], state the study aim and objectives explicitly, and place RQ4 on a separate line. [INSERT revised page/lines].

## Reviewer 3 — parental consent and child assent (PDF p.3, lines 165–170)

**Proposed response:** We agree that the ethics description should distinguish parental/guardian consent and child assent. We have checked the approved protocol and supporting records and clarified [CONFIRM exact consent and assent mechanisms, approvals and any exceptions]. We have retained participant confidentiality by describing the procedure without disclosing personal identifiers. [INSERT revised page/lines].

**Do not claim:** both were obtained without verifying the ethics documents.

## Reviewer 3 — participant and implementation detail (PDF p.4, lines 175–184)

**Proposed response:** We have added a more detailed description of the 12-class Grade 5/6 implementation, assessment administration and student-facing instructions, including [CONFIRM: activity assignment vs free choice, pacing, supervision, teacher roles, number of sessions, approximate exposure]. The supplied Excel workbooks establish scored pre/post observations, not how students navigated the platform; therefore these procedural details are reported only where supported by school/project documentation. We also provide the assessment questions or an authorised instrument description [CONFIRM rights and availability]. [INSERT revised page/lines].

## Reviewer 3 — Grade 6 lower baseline and validity (PDF p.4, lines 186–190)

**Proposed response:** The combined matched sample shows Grade 6's lower baseline mean (20.79 versus 22.44 for Grade 5), while both grades improved. We now make clear that this observational difference cannot establish why baseline performance differed. The available assessment data do not distinguish differences in student composition, prior learning or test administration. We report verified administration details where available and avoid attributing the difference to any unmeasured cause. [INSERT revised page/lines].

## Reviewer 3 — curriculum mapping, control group, explicit RQ answers and school takeaways (PDF p.4, lines 192–202)

**Proposed response:** We have reconsidered placement of the curriculum alignment material and [CONFIRM relocation or explain chosen structure]. We have expanded the explanation of why the current design cannot identify an added value over a traditional lesson and [CONFIRM documented rationale for the absence of a control group]. We now explicitly answer RQ1–RQ4 and expand practitioner recommendations on baseline diagnostics, item-level analysis, test design and cautious interpretation of short-term score gains. [INSERT revised page/lines].

## Reviewer 3 — overall execution and clarity (PDF p.4, lines 204–206)

**Proposed response:** We have reorganised the Methods to distinguish educational intervention, participant recruitment/ethics, assessment administration, source-data processing and statistical analysis. The reproducibility supplement provides additional operational detail. We agree that transparency about what was actually measured and what remains unknown is important for interpretation and replication.

## Final sign-off checklist for response letter

- Each comment paired with a verifiable change, not merely a promise.
- Every `[CONFIRM]` resolved from actual records or explicitly stated as unknown.
- Page/line citations updated against the **revised** manuscript.
- Data availability wording matches actual approved sharing arrangement.
- No invented instrument wording, teacher counts, dates, retention results or consent procedures.
- The editor's decision letter and journal identity verified.
