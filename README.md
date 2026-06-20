<div align="center">

# OpenShotSpec

**Portable, continuity-aware JSON records for scenes, shots, adapters, and creative tooling.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Format](https://img.shields.io/badge/Format-JSON-0969da)](schema/open-shot-spec.schema.json)
[![License](https://img.shields.io/badge/License-MIT-2ea44f)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Specification-f59e0b)](MAINTENANCE.md)

[Quick start](#quick-start) · [Record model](#record-model) · [Sequence validation](#sequence-validation) · [Migration](#legacy-migration) · [About](ABOUT.md)

</div>

---

OpenShotSpec defines a vendor-neutral scene and shot record for storyboard, previsualization, prompt planning, continuity tracking, and tool-to-tool metadata exchange. The repository includes single-record validation, sequence validation, readable descriptions, schemas, examples, migration utilities, and adapter policies.

> [!NOTE]
> OpenShotSpec describes creative intent and continuity metadata. It does not render media or guarantee semantic equivalence across every downstream tool.

## At a glance

| Area | Current support |
|---|---|
| Format | JSON and JSONL |
| Validation | Required fields, versions, duration, camera, continuity |
| Sequences | Duplicate IDs, missing references, reciprocal links |
| Description | Deterministic readable production text |
| Migration | Safe legacy-field migration with change report |
| Extensibility | Vendor-specific extension namespaces |
| Runtime | Python standard library |

## Quick start

Validate one record:

```bash
python main.py examples/scene.json
```

Generate a readable description:

```bash
python main.py examples/scene.json --describe
```

Validate a JSONL sequence:

```bash
python sequence.py examples/sequence.jsonl -o sequence-validation.json
```

Run tests:

```bash
python -m unittest -v
```

## Capability matrix

| Capability | Status | Notes |
|---|---:|---|
| Core scene validation | ✅ | Stable required fields |
| Continuity references | ✅ | Single-record and sequence checks |
| JSON Schema | ✅ | Draft 2020-12 documents |
| Legacy migration | ✅ | Non-destructive change tracking |
| Adapter contract | ✅ | Loss reporting and version declaration |
| Media generation | ❌ | Outside scope |
| Universal vendor mapping | ❌ | Adapters must report unsupported data |

## Minimum record

```json
{
  "schema_version": 1,
  "shot_id": "SCENE-001",
  "duration": 3.5,
  "subject": {
    "description": "A delivery rider in a dark blue jacket",
    "action": "stops beside a half-open door"
  },
  "camera": {
    "shot_type": "medium",
    "movement": "slow push-in",
    "lens": "35mm lens"
  }
}
```

## Record model

| Block | Purpose |
|---|---|
| `subject` | Identity, appearance, and action |
| `scene` | Location, time, environment, and context |
| `camera` | Shot type, movement, angle, and lens |
| `lighting` | Practical and artistic lighting intent |
| `continuity` | Previous/next references, locks, and assets |
| `extensions` | Tool-specific metadata outside the shared core |

## Sequence validation

`sequence.py` checks multiple records for:

- duplicate `shot_id` values;
- missing `previous_id` and `next_id` targets;
- self-references;
- non-reciprocal continuity links;
- invalid scene records inside the sequence.

Example result:

```json
{
  "records": 3,
  "valid": true,
  "issue_count": 0,
  "issues": []
}
```

## Legacy migration

```bash
python migrate.py legacy-shot.json \
  -o migrated-shot.json \
  --report migration-report.json
```

The migration utility can:

- add `schema_version`;
- rename `camera.type` to `camera.shot_type`;
- move legacy scene and lighting descriptions;
- deduplicate continuity locks;
- preserve the original input object;
- report every applied change.

## Recommended workflow

```text
scene authoring
      ↓
OpenShotSpec validation
      ↓
sequence continuity validation
      ↓
human creative review
      ↓
versioned adapter
      ↓
downstream storyboard / prompt / production tool
```

## Repository map

| Path | Purpose |
|---|---|
| `main.py` | Single-record validation and description output |
| `sequence.py` | Multi-record continuity validation |
| `migrate.py` | Safe legacy-record migration |
| `schema/` | Core and continuity schemas |
| `examples/` | Complete records and sequences |
| `docs/` | Compatibility, adapters, migration, and language policy |
| `test_*.py` / `checks.py` | Validation and migration tests |
| `ABOUT.md` | Mission, maturity, boundaries, and governance |

## Compatibility principles

- Required-field changes require a version increment.
- Renamed fields require a migration path.
- Unknown optional data must not silently alter core meaning.
- Adapters must declare supported versions and report losses.
- Tool-specific fields belong in a named extension namespace.

## Documentation

- [About the project](ABOUT.md)
- [Compatibility guide](docs/COMPATIBILITY.md)
- [Format extension guide](docs/FORMAT_EXTENSION_GUIDE.md)
- [Migration policy](docs/MIGRATION_POLICY.md)
- [Adapter contract](docs/ADAPTER_CONTRACT.md)
- [Language policy](docs/LANGUAGE_POLICY.md)
- [Maintenance trace](MAINTENANCE_TRACE.md)
- [Maintenance policy](MAINTENANCE.md)

## License

MIT
