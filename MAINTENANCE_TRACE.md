# Maintenance Trace

Batch: `content-enrichment-2026-06-19`

## Iteration 13

- Expanded the README with bilingual positioning, use cases, extended examples, design principles, workflow, compatibility rules, and limitations.
- Clearly separated the validated core from forward-compatible optional metadata.

## Iteration 14

- Added this visible maintenance trace.
- Defined versioning and adapter-maintenance expectations.

## Iteration 15

- Planned document: `docs/COMPATIBILITY.md`.
- Provides rules for format versions, extension namespaces, adapters, and migrations.

## Validation record

| Check | Result |
|---|---|
| Existing CLI retained | pass |
| Existing minimum record retained | pass |
| Extended fields marked as optional/future-facing | pass |
| Rendering capability not claimed | pass |
| Documentation links reviewed | pass after iteration 15 |

## Maintenance policy

1. Core required-field changes require a spec-version change.
2. New fields need type, meaning, default behavior, and example values.
3. Adapters must declare supported spec versions.
4. Vendor-specific data must not redefine core fields.
5. Migrations require before-and-after fixtures.
6. The validator and readable-description output must remain deterministic.

## Open items

- The core schema remains intentionally small.
- No official JSON Schema package is claimed in the current baseline.
- No renderer or vendor adapter is bundled as a universal reference implementation.
- Semantic equivalence across generation systems is not guaranteed.
