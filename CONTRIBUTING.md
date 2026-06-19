# Contributing

OpenShotSpec contributions should improve portability without expanding the shared core unnecessarily.

## Before proposing a field

- Confirm that the information is needed by more than one adapter or workflow.
- Check whether the value belongs in an extension namespace.
- Define the field type, unit, default behavior, and compatibility impact.
- Provide valid and invalid examples.

## Schema changes

Every schema change should include:

1. Motivation.
2. Compatibility classification.
3. Updated schema document.
4. Minimum valid fixture.
5. Complete fixture.
6. Invalid fixture.
7. Migration note when required.

## Adapter contributions

Adapters must list supported source and target versions, preserve unknown optional data when possible, report omitted fields, and include round-trip fixtures.

## Continuity changes

Continuity rules should use stable identifiers and portable references. Do not place local credentials or machine-specific absolute paths into shared records.

## Commit style

Use `feat:`, `fix:`, `docs:`, `test:`, `schema:`, or `adapter:` prefixes.

## Review standard

A contribution is ready when another implementation can understand the format from the schema, examples, and documentation without relying on private context.
