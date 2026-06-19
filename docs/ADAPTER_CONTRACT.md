# Adapter Contract

Adapters convert OpenShotSpec records to or from another tool format without changing shared semantics.

## Required adapter behavior

An adapter should:

- declare the OpenShotSpec schema versions it supports;
- validate required shared fields before conversion;
- preserve unknown optional fields when practical;
- keep extension data unless the user explicitly requests removal;
- report unsupported fields rather than silently discarding them;
- avoid embedding credentials or local machine paths;
- return deterministic output for the same input and configuration.

## Import result

An importer should produce:

```json
{
  "record": {},
  "warnings": [],
  "unsupported_fields": [],
  "source_format": "example",
  "source_version": "1"
}
```

## Export result

An exporter should produce:

```json
{
  "output": {},
  "warnings": [],
  "omitted_fields": [],
  "target_format": "example",
  "target_version": "1"
}
```

## Loss reporting

Lossy conversion must list every omitted or transformed field. A successful command must not imply lossless conversion unless no shared information was discarded.

## Identity and references

Adapters should preserve stable identifiers. External asset references should use portable identifiers or relative paths rather than absolute local paths.

## Testing requirements

Each adapter should include round-trip fixtures, minimum valid input, complete input, unknown extension input, invalid input, and expected warning output.
