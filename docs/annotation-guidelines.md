# Draft annotation guidelines — v0.1 (unvalidated)

## Annotation question

For a given passage and a candidate interpretive claim: **What does this passage establish about that specific claim?**

Do not infer the person's true internal state.

## Proposed support labels

| Label | Decision | Recommended action |
| --- | --- | --- |
| `supported` | The passage offers clear textual support without a relevant contradiction | Explain using exact quoted evidence |
| `not_established` | The claim is possible but insufficiently evidenced | Abstain from affirming it |
| `contradicted` | The passage clearly supplies contrary evidence | Reject or qualify using counterevidence |
| `ambiguous` | Several interpretations remain defensible | State uncertainty or abstain |

These are **provisional annotation labels**, not independently validated psychological categories.

## Evidence-span rule

The proposed data structure stores `start` and `end` offsets with the convention `[start, end)` over the Unicode string, plus the exact matching excerpt. Do not invent an excerpt or mark background assumptions as observed words. Empty evidence spans can be appropriate for `not_established`.

## Constructed demonstrations

**Passage:** "I prefer the library because it is quiet."

**Claim:** "The speaker says they prefer the library."

**Suggested label:** `supported` — the preference is explicitly reported.

**Passage:** "A student left the room after the bell."

**Claim:** "The student was upset."

**Suggested label:** `not_established` — no emotion is stated.

These illustrations are authored examples, not participant data.

## Planned independent annotation

Three reviewers would label items independently, identify support spans, record confidence/uncertainty and retain disagreement for adjudication. A consensus does not certify someone's private mental state.

**Safety boundary:** Do not infer diagnoses, dangerousness, sensitive identities or deception from short text. Future human data would require permission, privacy safeguards and appropriate ethics review.

**Versioning:** Record changes to rules and labels before freezing an evaluation set; do not revise labels retrospectively merely to improve scores.
