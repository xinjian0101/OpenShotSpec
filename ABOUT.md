# About OpenShotSpec

## Mission

OpenShotSpec defines a portable, structured scene-and-shot record for creative tools that need consistent subjects, cameras, lighting, continuity, and extension data.

## Intended users

- Creative-tool developers
- Previsualization and storyboard systems
- Prompt and scene planners
- Adapter authors integrating multiple media tools
- Teams that need continuity-aware scene records

## Core capabilities

- Single-record validation
- Structured scene description generation
- Continuity blocks and locked attributes
- JSON Schema definitions
- Multi-record sequence validation
- Extension namespaces
- Migration and adapter policies

## Boundaries

The format does not generate media, manage assets, choose artistic direction, or guarantee that every external tool can represent every shared field.

## Architecture

```text
Shared scene record -> validation -> adapter or description output
                    -> sequence validation -> continuity report
```

## Design priorities

1. Stable shared semantics
2. Portable identifiers
3. Explicit compatibility rules
4. Loss reporting in adapters
5. Extension namespaces for tool-specific data
6. Safe migrations that preserve original records

## Maturity

The project includes executable validators, schemas, examples, sequence checks, migration policy, adapter contracts, CI, and tests.

## Governance

New shared fields require cross-tool justification, valid and invalid fixtures, compatibility classification, and migration notes when required.
