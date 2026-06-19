# OpenShotSpec

A portable JSON format and validator for structured video-scene descriptions. It is intended for shot planning, AI-video prompt pipelines, storyboard exchange, and tool-to-tool scene metadata transfer.

中文定位：用于描述镜头、主体、动作和摄影信息的可移植 JSON 规范与校验器。

> Current status: compact MVP and evolving interchange specification. The validator does not generate video and does not guarantee compatibility with every downstream tool.

## Use cases

- Exchange structured shot descriptions between creative tools
- Validate scene records before prompt generation or rendering
- Store shot plans in a machine-readable format
- Convert structured fields into readable production descriptions
- Build adapters for storyboard, editing, and generation systems

## Current capabilities

- Validate `shot_id`, `duration`, `subject`, and `camera`
- Require a positive duration
- Require a camera shot type
- Reject structurally invalid records
- Convert valid records into readable descriptions
- Run locally without a paid API

## Quick start

### Requirements

- Python 3.10 or newer

### Validate a scene

```bash
python main.py scene.json
```

### Generate a readable description

```bash
python main.py scene.json --describe
```

### Run checks

```bash
python checks.py
```

## Minimum record

```json
{
  "shot_id": "S1",
  "duration": 3,
  "subject": {},
  "camera": {
    "shot_type": "medium"
  }
}
```

## Recommended extended record

```json
{
  "spec_version": "0.1",
  "shot_id": "S1",
  "duration": 3.5,
  "subject": {
    "description": "a delivery rider entering a quiet apartment corridor",
    "action": "stops and looks toward a half-open door"
  },
  "camera": {
    "shot_type": "medium",
    "movement": "slow push-in",
    "angle": "eye level",
    "lens": "35mm"
  },
  "scene": {
    "location": "older residential building",
    "time": "night",
    "lighting": "single ceiling lamp with practical shadows"
  },
  "continuity": {
    "character_id": "rider-01",
    "costume_id": "uniform-blue-v1",
    "previous_shot": null
  },
  "notes": [
    "keep the doorway visible",
    "avoid readable private information"
  ]
}
```

Only fields supported by the current validator are guaranteed to affect validation or description output. Additional fields should be treated as forward-compatible metadata unless documented otherwise.

## Design principles

- **Portable**: records should not depend on one generation vendor.
- **Explicit**: camera, subject, duration, and identifiers are separate fields.
- **Versionable**: format changes should declare a specification version.
- **Extensible**: optional metadata can be added without redefining the core.
- **Reviewable**: a human should be able to inspect the JSON and its readable description.
- **Deterministic**: identical valid input should produce stable validation results.

## Recommended workflow

1. Author or export a scene record.
2. Validate the record with OpenShotSpec.
3. Review errors and unsupported fields.
4. Generate a readable production description.
5. Pass the validated record through a downstream adapter.
6. Archive the source record, spec version, and adapter version.

## Compatibility rules

- Unknown optional fields should not silently change core meaning.
- Required-field changes need a specification-version update.
- Renamed fields require a documented migration path.
- Adapters should declare the OpenShotSpec versions they support.
- Vendor-specific fields should live in a clearly named extension namespace.

## Known limitations

- The current validator covers a small core schema.
- It does not validate visual realism, prompt quality, copyright, or safety policy.
- It does not render images or video.
- It does not guarantee semantic equivalence between different generation systems.
- Extended example fields may require future validator support.

## Documentation

- [Compatibility Guide](docs/COMPATIBILITY.md)
- [Maintenance Trace](MAINTENANCE_TRACE.md)

## License

MIT