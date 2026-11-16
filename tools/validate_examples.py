"""Validate *synthetic demonstration* records, not research/clinical validity.

Use: python tools/validate_examples.py examples/synthetic_examples.jsonl
No external dependencies required.
"""
import json
import sys
from pathlib import Path

LABELS = {"supported", "not_established", "contradicted", "ambiguous"}
ACTIONS = {"answer", "abstain", "reject_claim"}
REQUIRED = {
    "example_id", "passage", "candidate_claim", "support_status",
    "evidence_spans", "recommended_action", "hard_negative", "origin", "split"
}
OPTIONAL = {"notes"}


def validate_record(row):
    """Return error messages; checks data structure only, never true meaning."""
    errors = []
    if not isinstance(row, dict):
        return ["record must be a JSON object"]
    missing = REQUIRED - row.keys()
    if missing:
        errors.append(f"missing fields: {', '.join(sorted(missing))}")
    extras = row.keys() - REQUIRED - OPTIONAL
    if extras:
        errors.append(f"unknown fields: {', '.join(sorted(extras))}")
    if missing:
        return errors
    if not isinstance(row["example_id"], str) or not row["example_id"].startswith("SYN-"):
        errors.append("example_id must use SYN- prefix")
    for key in ("passage", "candidate_claim"):
        if not isinstance(row[key], str) or not row[key].strip():
            errors.append(f"{key} must be non-empty text")
    if row["support_status"] not in LABELS:
        errors.append("invalid support_status")
    if row["recommended_action"] not in ACTIONS:
        errors.append("invalid recommended_action")
    if not isinstance(row["hard_negative"], bool):
        errors.append("hard_negative must be boolean")
    if row["origin"] != "synthetic_constructed" or row["split"] != "demo_only":
        errors.append("synthetic examples must have synthetic_constructed/demo_only tags")
    spans = row["evidence_spans"]
    passage = row["passage"]
    if not isinstance(spans, list):
        errors.append("evidence_spans must be a list")
    elif isinstance(passage, str):
        for i, span in enumerate(spans):
            if not isinstance(span, dict) or set(span) != {"start", "end", "text"}:
                errors.append(f"span {i}: expected start/end/text only")
                continue
            st, en, txt = span["start"], span["end"], span["text"]
            if type(st) is not int or type(en) is not int or not (0 <= st < en <= len(passage)):
                errors.append(f"span {i}: offsets out of bounds")
            elif not isinstance(txt, str) or passage[st:en] != txt:
                errors.append(f"span {i}: excerpt mismatches passage offsets")
    if row["support_status"] == "supported" and row["recommended_action"] != "answer":
        errors.append("supported synthetic record requires action=answer")
    if row["support_status"] == "not_established" and row["recommended_action"] != "abstain":
        errors.append("not_established synthetic record requires action=abstain")
    if row["support_status"] == "ambiguous" and row["recommended_action"] != "abstain":
        errors.append("ambiguous synthetic record requires action=abstain")
    if row["support_status"] == "contradicted" and row["recommended_action"] != "reject_claim":
        errors.append("contradicted synthetic record requires action=reject_claim")
    if row["support_status"] == "supported" and isinstance(spans,list) and len(spans) == 0:
        errors.append("supported synthetic record requires an evidence span")
    return errors


def validate_file(path):
    errors, seen, count = [], set(), 0
    for line_no, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        count += 1
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_no}: invalid JSON: {exc}")
            continue
        for err in validate_record(row):
            errors.append(f"line {line_no}: {err}")
        if isinstance(row, dict) and row.get("example_id"):
            if row["example_id"] in seen:
                errors.append(f"line {line_no}: duplicate example_id")
            seen.add(row["example_id"])
    if count == 0:
        errors.append("example file is empty")
    return count, errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python tools/validate_examples.py FILE.jsonl")
    count, errors = validate_file(sys.argv[1])
    if errors:
        for e in errors:
            print("ERROR:", e)
        sys.exit(1)
    print(f"PASS: {count} constructed examples have valid data shape (not benchmark/annotation validation).")
