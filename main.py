from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


REQUIRED = {
    "shot_id": str,
    "duration": (int, float),
    "subject": dict,
    "camera": dict,
}


def validate(shot: dict) -> list[dict]:
    issues: list[dict] = []
    if not isinstance(shot, dict):
        return [{"field": "$", "type": "invalid_type"}]
    for field, expected_type in REQUIRED.items():
        if field not in shot:
            issues.append({"field": field, "type": "missing"})
        elif not isinstance(shot[field], expected_type) or isinstance(shot[field], bool):
            issues.append({"field": field, "type": "invalid_type"})

    schema_version = shot.get("schema_version")
    if schema_version is not None and (not isinstance(schema_version, int) or isinstance(schema_version, bool) or schema_version < 1):
        issues.append({"field": "schema_version", "type": "invalid_version"})

    shot_id = shot.get("shot_id")
    if isinstance(shot_id, str) and not shot_id.strip():
        issues.append({"field": "shot_id", "type": "empty"})

    duration = shot.get("duration")
    if isinstance(duration, (int, float)) and not isinstance(duration, bool):
        if not math.isfinite(float(duration)):
            issues.append({"field": "duration", "type": "must_be_finite"})
        elif duration <= 0:
            issues.append({"field": "duration", "type": "must_be_positive"})

    camera = shot.get("camera")
    if isinstance(camera, dict):
        shot_type = camera.get("shot_type")
        if not isinstance(shot_type, str) or not shot_type.strip():
            issues.append({"field": "camera.shot_type", "type": "missing"})

    continuity = shot.get("continuity")
    if continuity is not None and not isinstance(continuity, dict):
        issues.append({"field": "continuity", "type": "invalid_type"})
    elif isinstance(continuity, dict):
        for field in ("previous_id", "next_id"):
            value = continuity.get(field)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                issues.append({"field": f"continuity.{field}", "type": "invalid_type"})
            if isinstance(shot_id, str) and value == shot_id:
                issues.append({"field": f"continuity.{field}", "type": "self_reference"})
        locked = continuity.get("locked_attributes", [])
        if not isinstance(locked, list) or any(not isinstance(item, str) or not item.strip() for item in locked):
            issues.append({"field": "continuity.locked_attributes", "type": "invalid_type"})
        elif len(locked) != len(set(locked)):
            issues.append({"field": "continuity.locked_attributes", "type": "duplicate_value"})

    extensions = shot.get("extensions")
    if extensions is not None and not isinstance(extensions, dict):
        issues.append({"field": "extensions", "type": "invalid_type"})
    return issues


def describe(shot: dict) -> str:
    subject = shot.get("subject", {})
    scene = shot.get("scene", {})
    camera = shot.get("camera", {})
    lighting = shot.get("lighting", {})
    parts = [
        str(subject.get("description", "")).strip(),
        str(subject.get("action", "")).strip(),
        str(scene.get("description", "")).strip(),
        str(camera.get("shot_type", "medium shot")).strip(),
        str(camera.get("movement", "static camera")).strip(),
        str(camera.get("lens", "50mm lens")).strip(),
        str(lighting.get("description", "natural practical lighting")).strip(),
        "realistic photography",
        "natural skin texture",
        "correct anatomy and perspective",
        "no text or watermark",
    ]
    return ", ".join(part for part in parts if part)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate an OpenShotSpec JSON file.")
    parser.add_argument("shot")
    parser.add_argument("--describe", action="store_true")
    parser.add_argument("-o", "--output", default="shot-validation.json")
    args = parser.parse_args()

    shot = json.loads(Path(args.shot).read_text(encoding="utf-8"))
    if args.describe:
        print(describe(shot))
        return
    issues = validate(shot)
    report = {"valid": not issues, "issues": issues}
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("valid" if not issues else f"{len(issues)} issues")


if __name__ == "__main__":
    main()
