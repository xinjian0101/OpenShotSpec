# Support

## Start here

Review these documents before opening an issue:

- [README](README.md) for commands and current capabilities
- [About](ABOUT.md) for mission, maturity, and boundaries
- [Compatibility Guide](docs/COMPATIBILITY.md) for version expectations
- [Migration Policy](docs/MIGRATION_POLICY.md) for record changes
- [Adapter Contract](docs/ADAPTER_CONTRACT.md) for integration behavior
- [Format Extension Guide](docs/FORMAT_EXTENSION_GUIDE.md) for new fields

## Bug reports

Use the structured **Bug report** form for single-record validation, sequence validation, descriptions, schemas, continuity references, adapters, or migration defects.

Include:

- exact commit or specification version;
- minimal synthetic JSON or JSONL fixture;
- complete reproduction command;
- expected and actual validation result;
- adapter or migration version when relevant;
- unsupported or lost fields when conversion is involved.

## Feature requests

Use the **Feature request** form. Shared-field proposals should explain cross-tool value, exact semantics, validation rules, version impact, migration requirements, adapter behavior, and fixtures.

## Production-data rules

Do not upload private storyboards, unreleased scripts, asset paths, client identifiers, credentials, or proprietary prompts. Use synthetic records that reproduce only the relevant structure.

## Project boundaries

OpenShotSpec does not provide:

- image or video generation;
- automatic artistic decisions;
- universal lossless conversion across all tools;
- copyright or policy clearance;
- guarantees for undocumented vendor fields.

## Compatibility expectations

Required-field changes require versioning. Renamed fields require a migration path. Tool-specific fields belong in an extension namespace, and adapters should report unsupported or lossy mappings.

## Response expectations

Support is community-maintained and best effort. Small valid and invalid fixtures with explicit version information are the easiest to review.
