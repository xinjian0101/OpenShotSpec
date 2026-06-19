from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = {
    "shot_id": str,
    "duration": (int, float),
    "subject": dict,
    "camera": dict,
}


def validate(shot: dict) -> list[dict]:
    issues: list[dict] = []
    for field, expected_type in REQUIRED.items():
        if field not in shot:
            issues.append({"field": field, "type": "missing"})
        elif not isinstance(shot[field], expected_type):
            issues.append({"field": field, "type": "invalid_type"})
    duration = shot.get("duration")
    if isinstance(duration, (int, float)) and duration <= 0:
        issues.append({"field": "duration", "type": "must_be_positive"})
    camera = shot.get("camera")
    if isinstance(camera, dict) and not camera.get("shot_type"):
        issues.append({"field": "camera.shot_type", "type": "missing"})
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
