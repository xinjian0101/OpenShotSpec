# Format Extension Guide

OpenShotSpec keeps a small shared record and stores optional tool data inside an `extensions` object.

## Shared fields

- `schema_version`
- `shot_id`
- `duration`
- `subject`
- `scene`
- `camera`
- `lighting`
- `continuity`

## Extension example

```json
{
  "extensions": {
    "example.tool": {
      "quality_target": "preview",
      "format_version": 1
    }
  }
}
```

## Rules

- An extension must not change the meaning of required shared fields.
- Readers may ignore an unknown extension.
- Writers should keep unknown extension data when possible.
- Each extension should declare its own version.
- Portable records should not contain credentials or machine-specific absolute paths.

## Compatibility

A shared format change increments `schema_version`. Migration tools should record source and target versions and avoid destructive changes by default.
