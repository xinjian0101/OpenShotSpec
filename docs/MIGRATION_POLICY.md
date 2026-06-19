# Migration Policy

OpenShotSpec uses an integer `schema_version` to identify shared-format changes.

## Compatible changes

The following changes normally remain compatible within one schema version:

- adding optional fields;
- adding optional extension data;
- clarifying documentation without changing field meaning;
- adding new recommended values while keeping previous values valid.

## Version-increment changes

A schema-version increment is required when a change:

- adds a required field;
- removes or renames a shared field;
- changes a field type;
- changes the unit or meaning of an existing value;
- makes previously valid records invalid;
- changes reference semantics.

## Migration requirements

Every migration should declare:

- source version;
- target version;
- reversible or irreversible status;
- fields added, removed, renamed, or transformed;
- default values and how they were selected;
- warnings and information loss;
- input and output checksums.

## Safe migration behavior

- Keep the original document unchanged by default.
- Write migrated output to a new file.
- Preserve unknown optional fields and extension blocks where possible.
- Stop when required data cannot be inferred safely.
- Never invent subject, scene, camera, or continuity information.

## Verification

Migration fixtures should cover the minimum valid record, a complete record, unknown extension data, missing optional fields, invalid source data, and repeated migration attempts.

## Deprecation

Deprecated fields should remain documented for at least one supported migration period. Documentation must identify the replacement field and the last version that accepts the deprecated form.
