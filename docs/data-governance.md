# Data governance plan — no corpus released

There is **no released research dataset**. The four rows in `examples/synthetic_examples.jsonl` are constructed demonstrations excluded from the planned benchmark.

## Before collecting real data

- Confirm lawful source rights, permissions and licences; do not scrape private chats, diaries, therapy records, student files or confidential data.
- Decide whether consent, ethics committee review or other oversight is necessary.
- Minimise and protect personal information; do not release identifiable sensitive material.
- Specify data retention, deletion, access controls and incident response.
- Preserve provenance and source versions.
- Prevent test contamination, near-duplicate leakage, and unlicensed redistribution.
- Plan multilingual inclusion without suggesting demographic representativeness.

## Proposed data inventory

| Item | Purpose | Current status |
| --- | --- | --- |
| Provenance and rights | Establish rights to use/share text | Not established |
| Passage and candidate claim | Benchmark unit | Four synthetic examples only |
| Independent reviewer labels | Disagreement and reliability | Not collected |
| Evidence spans | Explainable support | Illustrative offsets only |
| Adjudication record | Review difficult cases | Not performed |
| Frozen split IDs | Independent evaluation | Not assigned |
| Model outputs and confidence | Evaluate candidate systems | Not generated |

**An annotation schema and constructed demonstrations are not a validated dataset.**
