from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

import main


TARGET_VERSION = 1


def migrate_record(record: dict, target_version: int = TARGET_VERSION) -> tuple[dict, list[dict]]:
    if not isinstance(record, dict):
        raise ValueError("Record must be an object")
    if target_version != TARGET_VERSION:
        raise ValueError(f"Unsupported target version: {target_version}")

    migrated = copy.deepcopy(record)
    changes: list[dict] = []

    current_version = migrated.get("schema_version")
    if current_version not in (None, target_version):
        raise ValueError(f"Unsupported source version: {current_version}")
    if current_version is None:
        migrated["schema_version"] = target_version
        changes.append({"type": "add", "field": "schema_version", "value": target_version})

    camera = migrated.get("camera")
    if isinstance(camera, dict) and "shot_type" not in camera and isinstance(camera.get("type"), str):
        camera["shot_type"] = camera.pop("type")
        changes.append({"type": "rename", "from": "camera.type", "to": "camera.shot_type"})

    if "scene_description" in migrated:
        scene = migrated.setdefault("scene", {})
        if not isinstance(scene, dict):
            raise ValueError("scene must be an object before scene_description can be migrated")
        if "description" not in scene:
            scene["description"] = migrated.pop("scene_description")
            changes.append({"type": "move", "from": "scene_description", "to": "scene.description"})

    if "lighting_description" in migrated:
        lighting = migrated.setdefault("lighting", {})
        if not isinstance(lighting, dict):
            raise ValueError("lighting must be an object before lighting_description can be migrated")
        if "description" not in lighting:
            lighting["description"] = migrated.pop("lighting_description")
            changes.append({"type": "move", "from": "lighting_description", "to": "lighting.description"})

    continuity = migrated.get("continuity")
    if isinstance(continuity, dict) and isinstance(continuity.get("locked_attributes"), list):
        original = continuity["locked_attributes"]
        unique = list(dict.fromkeys(original))
        if unique != original:
            continuity["locked_attributes"] = unique
            changes.append({"type": "deduplicate", "field": "continuity.locked_attributes"})

    return migrated, changes


def migrate_document(value: object, target_version: int = TARGET_VERSION) -> tuple[object, list[dict]]:
    if isinstance(value, dict):
        record, changes = migrate_record(value, target_version)
        return record, [{"record": 0, **change} for change in changes]
    if isinstance(value, list):
        migrated_records = []
        all_changes: list[dict] = []
        for index, item in enumerate(value):
            record, changes = migrate_record(item, target_version)
            migrated_records.append(record)
            all_changes.extend({"record": index, **change} for change in changes)
        return migrated_records, all_changes
    raise ValueError("Input must be a JSON object or array")


def main_cli() -> None:
    parser = argparse.ArgumentParser(description="Migrate legacy OpenShotSpec JSON records.")
    parser.add_argument("input")
    parser.add_argument("-o", "--output", default="migrated-shot.json")
    parser.add_argument("--report", default="migration-report.json")
    parser.add_argument("--target-version", type=int, default=TARGET_VERSION)
    args = parser.parse_args()

    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    migrated, changes = migrate_document(source, args.target_version)

    records = migrated if isinstance(migrated, list) else [migrated]
    validation = [
        {"record": index, "issues": main.validate(record)}
        for index, record in enumerate(records)
        if main.validate(record)
    ]
    Path(args.output).write_text(json.dumps(migrated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    Path(args.report).write_text(
        json.dumps(
            {
                "target_version": args.target_version,
                "record_count": len(records),
                "change_count": len(changes),
                "changes": changes,
                "validation": validation,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Migrated {len(records)} record(s); applied {len(changes)} change(s)")


if __name__ == "__main__":
    main_cli()
