from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import main


def load_records(path: str) -> list[dict]:
    records: list[dict] = []
    for line_number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON at line {line_number}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"Line {line_number} is not an object")
        records.append(value)
    return records


def validate_sequence(records: list[dict]) -> list[dict]:
    issues: list[dict] = []
    identifiers = [record.get("shot_id") for record in records if isinstance(record.get("shot_id"), str)]
    counts = Counter(identifiers)
    known = set(identifiers)

    for position, record in enumerate(records, 1):
        shot_id = record.get("shot_id")
        for issue in main.validate(record):
            issues.append({"position": position, "shot_id": shot_id, **issue})
        if isinstance(shot_id, str) and counts[shot_id] > 1:
            issues.append({"position": position, "shot_id": shot_id, "field": "shot_id", "type": "duplicate_id"})
        continuity = record.get("continuity", {})
        if not isinstance(continuity, dict):
            continue
        for field in ("previous_id", "next_id"):
            reference = continuity.get(field)
            if isinstance(reference, str) and reference not in known:
                issues.append({
                    "position": position,
                    "shot_id": shot_id,
                    "field": f"continuity.{field}",
                    "type": "missing_reference",
                    "reference": reference,
                })

    by_id = {record.get("shot_id"): record for record in records if isinstance(record.get("shot_id"), str)}
    for position, record in enumerate(records, 1):
        shot_id = record.get("shot_id")
        continuity = record.get("continuity", {})
        if not isinstance(continuity, dict) or not isinstance(shot_id, str):
            continue
        next_id = continuity.get("next_id")
        if isinstance(next_id, str) and next_id in by_id:
            next_continuity = by_id[next_id].get("continuity", {})
            if isinstance(next_continuity, dict) and next_continuity.get("previous_id") not in (None, shot_id):
                issues.append({
                    "position": position,
                    "shot_id": shot_id,
                    "field": "continuity.next_id",
                    "type": "non_reciprocal_reference",
                    "reference": next_id,
                })
    return issues


def main_cli() -> None:
    parser = argparse.ArgumentParser(description="Validate an OpenShotSpec JSONL sequence.")
    parser.add_argument("sequence")
    parser.add_argument("-o", "--output", default="sequence-validation.json")
    args = parser.parse_args()
    records = load_records(args.sequence)
    issues = validate_sequence(records)
    report = {"records": len(records), "valid": not issues, "issue_count": len(issues), "issues": issues}
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("valid" if not issues else f"{len(issues)} issues")


if __name__ == "__main__":
    main_cli()
