# Proposed benchmark protocol — not implemented

## Intended scope

The **planning target** is 1,500–3,000 passages, at least 30% hard-negative examples, three independent reviewers per item, evidence-span annotations, a frozen held-out evaluation set and explicit abstention-aware metrics.

**None of these planned collection or annotation targets is currently reported as completed.**

## Prospective procedure

1. Define permitted constructs with measurement, language and model-evaluation specialists; exclude diagnosis and sensitive attributes.
2. Determine lawful passage sources: original constructed, appropriately licensed, or consented material; do not scrape private communication.
3. Pair each passage with a candidate claim and record provenance.
4. Create hard negatives that sound plausible but lack sufficient supporting evidence, not merely examples relying on stereotypes.
5. Pilot an annotation codebook with independent reviewers; examine disagreement before freezing rules.
6. Keep raw labels and evidence spans even when an adjudicated final label is produced.
7. Freeze data splits, exclusion rules, measures and prompts before held-out model evaluation. Prevent source and near-duplicate leakage.
8. Evaluate predetermined baselines and models; preserve settings, model versions, refusals and formatting failures.
9. Report all outcomes, including inconclusive and negative results, uncertainty and known limitations.

## Unresolved design decisions

- Precisely which interpretive claims are safe and meaningful to study?
- How should multilingual, quoted, ironic or indirect descriptions be treated?
- What source and item balance avoids shortcuts?
- Which reliability measures best represent reviewer disagreement?
- Which dataset split and adjudication process are justified?
- Should the final study avoid mental-state labels altogether and instead measure **textual evidentiary sufficiency**?

### Synthetic test records

The four hand-written items in `examples/` test schema structure only. They **are not** human-annotated benchmark records, a held-out dataset, or measured model outputs.
