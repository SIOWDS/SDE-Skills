# Case Study: A Three-Arm Blind Test for SDE Intelligence Training

## 案例：SDE提智内功三臂盲评实验

This case converts the desktop prototype **SDE提智对照·简化版 2.3** into a reproducible evaluation protocol.

The original package implements the experiment workflow but contains no completed run dataset. Therefore, this page documents a **testable protocol**, not proof that SDE Intelligence Training has already produced a universal or statistically significant gain.

## Research question

For the same question, under an equal response-length limit:

> Does SDE Intelligence Training produce answers that independent judges rate as more original, mechanistic, rigorous and useful than a bare model response or an ordinary user prompt?

## Three arms

| Arm | Input | Purpose |
|---|---|---|
| A — Bare | Question only | Baseline model performance |
| B — User prompt | Ordinary user instruction + question | Prompt-engineering control |
| C — SDE training | SDE Intelligence Training prior + question | Treatment arm |

All arms must use:

- the same answering model and version;
- the same temperature and token/character budget;
- the same question;
- the same system safety conditions;
- the same number of repeated runs.

## Blinded judging

1. Remove labels A, B and C from answers.
2. Randomize answer order for each judging pass.
3. Ask one or more judge models to score without knowing the treatment.
4. Repeat judging several times.
5. Store every raw score and rationale.
6. Decode labels only after aggregation.

The SDE-trained answer should use field-native language. A judge must not be able to identify it merely from SDE terminology.

## Evaluation dimensions

Use a fixed rubric rather than an undefined “intelligence” impression.

| Dimension | Weight |
|---|---:|
| Explanatory fracture | 15 |
| Conceptual originality | 20 |
| Mechanism | 20 |
| Evidence discipline | 15 |
| Falsifiability | 10 |
| Generative reach | 10 |
| Field-native clarity | 5 |
| Self-application | 5 |
| **Total** | **100** |

The original desktop prototype also supports a 160-point “innovation IQ” display. For public reproducibility, report the 100-point rubric as the primary outcome and treat any IQ-style number as a communication metaphor, not a psychometric measurement.

## Primary outcomes

For each question (q):

[
Delta_{CA,q} = ar{C}_q - ar{A}_q
]

[
Delta_{CB,q} = ar{C}_q - ar{B}_q
]

Where:

- (ar{A}_q) is the mean blinded score of the bare arm;
- (ar{B}_q) is the mean score of the user-prompt arm;
- (ar{C}_q) is the mean score of the SDE-training arm.

The more important comparison is usually **C−B**, because it tests whether SDE training adds value beyond an ordinary instruction to “think deeply”.

## Recommended experiment

- At least 30 questions
- Multiple domains and difficulty levels
- At least 3 independent answering runs per arm
- At least 3 judging passes per answer
- At least 2 different judge models
- Pre-registered rubric and aggregation rules
- Human expert review on a stratified sample

Report:

- mean and median gain;
- standard deviation;
- confidence interval;
- win/tie/loss rate;
- domain-level differences;
- answer-length and latency differences;
- judge-model disagreement.

## Question set design

Include:

1. ordinary factual synthesis;
2. theoretical conflict;
3. causal-mechanism analysis;
4. interdisciplinary translation;
5. research design;
6. adversarial or misleading premises;
7. questions where SDE should not provide an advantage.

The seventh group is essential. A credible method must identify its boundary, not only its successes.

## Threats to validity

### Judge bias

A judge model may prefer complexity, confidence or polished prose. Control for this by enforcing equal length, random order, explicit evidence criteria and human review.

### Model contamination

A judge may recognize repeated SDE language. The treatment answer must pass the field-native translation test.

### Prompt-length advantage

The SDE arm receives more instructions. Add a length-matched generic-reasoning control in a stronger future design.

### Non-independence

Repeated calls to the same model family are not independent human observations. Report model and version details.

### Score inflation

Do not treat one high score or one question as evidence. Publish raw answers and scoring rationales.

### Moving models

Provider models change over time. Record evaluation date, exact model identifiers and relevant parameters.

## Reproducible record format

Store one JSON record per run:

```json
{
  "experiment_id": "sde-ab-001",
  "question_id": "q01",
  "question": "...",
  "answer_model": "...",
  "judge_model": "...",
  "arm": "A|B|C",
  "answer": "...",
  "scores": {
    "fracture": 0,
    "originality": 0,
    "mechanism": 0,
    "evidence": 0,
    "falsifiability": 0,
    "generative_reach": 0,
    "field_translation": 0,
    "self_application": 0
  },
  "judge_rationale": "...",
  "parameters": {},
  "timestamp": "..."
}
```

Never store API keys in experiment records or commit local configuration files.

## What would count as support?

Support requires:

- positive C−B gains across a varied question set;
- gains concentrated in mechanism, falsifiability and generative reach rather than verbosity;
- consistency across judge models;
- partial confirmation by relevant human experts;
- disclosed failures and negative cases.

## What would falsify or weaken the claim?

- C performs no better than B after length matching;
- gains disappear under human expert review;
- judges reward style while factual accuracy declines;
- the method helps only questions already phrased in SDE-like terms;
- performance collapses outside philosophy or conceptual analysis;
- answers become harder to verify or less field-native.

## Source

Adapted from the user-supplied desktop prototype **SDE提智对照·简化版 2.3**. The prototype uses equal-length answer generation, a bare/user-prompt/SDE three-arm design, randomized blinded judging, repeated scoring and report export.

The public repository intentionally documents the experimental logic before publishing outcome claims. Future datasets should be added under a dated, immutable release with model versions and raw records.
