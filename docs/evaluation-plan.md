# Evaluation plan — prospective, without measured results

## Intended evaluation dimensions

1. **Support-label performance:** per-label precision/recall, macro-F1, confusion matrix and uncertainty intervals.
2. **Evidence justification:** overlap of identified spans with independently annotated evidence, plus readability and irrelevant-span audits.
3. **Abstention:** coverage, selective risk among answered cases, and error rates for unsupported or ambiguous examples.
4. **Calibration:** agreement between expressed confidence and observed correctness, with one pre-specified confidence-elicitation method.
5. **Disagreement awareness:** compare high-consensus and contested records rather than disguising disagreement as ground truth.
6. **Robustness:** perturb irrelevant surface wording or contextual distractions while preserving the evidence.
7. **Language/context audits:** where collected data ethically and statistically support comparison.

## Definitions for preregistration

- **Coverage:** `answered_items / all_eligible_items`.
- **Selective risk:** `incorrect_answered_items / answered_items`, undefined at zero coverage.
- **Macro-F1:** average across prespecified class-level F1 scores.
- **Evidence overlap:** prespecified token-level or character-level intersection-over-union, defining how empty spans are evaluated.

## Proposed baselines — not executed

- Always-answer baseline.
- Always-abstain baseline (zero coverage; undefined selective risk).
- Evidence-first rule.
- Prompted language-model comparator under matched output constraints.

## Controls against leakage

Split by source/provenance and near-duplicate cluster rather than random rows alone. Freeze prompts, thresholds, evaluation splits, seeds and models in advance.

No performance results, model rankings, sample-derived effect sizes or completed annotations are reported in this repository. The included tool checks **input shape only**, not psychological construct validity.
