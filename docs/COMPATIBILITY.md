# Compatibility Guide

This guide defines how OpenShotSpec records, validators, and adapters should evolve without silently changing scene meaning.

## Version fields

A record may include:

```json
{
  "spec_version": "0.1"
}
```

Until a stable release is declared, consumers should treat minor versions as evolving and verify supported fields explicitly.

## Change categories

### Compatible additions

- New optional fields with documented defaults
- New extension namespaces
- Additional allowed enum values when old consumers can reject them clearly
- New descriptive metadata that does not alter core interpretation

### Migration-required changes

- Renaming a field
- Changing a field type
- Changing units
- Moving a field to another object
- Making an optional field required
- Changing the meaning of an existing value

### Breaking changes

- Removing a core field
- Reusing a field name for a different meaning
- Changing duration from seconds to another unit without a new version
- Allowing ambiguous identifiers
- Changing validation behavior without release notes

## Extension namespaces

Vendor-specific data should be isolated:

```json
{
  "extensions": {
    "vendor.example": {
      "model": "example-model",
      "seed": 12345
    }
  }
}
```

Extension data must not override `shot_id`, `duration`, `subject`, or `camera` semantics.

## Adapter declaration

Every adapter should publish metadata similar to:

```json
{
  "adapter": "storyboard-exporter",
  "adapter_version": "1.0.0",
  "supported_spec_versions": ["0.1"],
  "ignored_fields": ["continuity.previous_shot"],
  "vendor_extensions": ["vendor.example"]
}
```

## Migration checklist

- [ ] Record the source and target spec versions.
- [ ] Preserve the original input.
- [ ] Apply deterministic field mappings.
- [ ] Report dropped or transformed fields.
- [ ] Validate the migrated record.
- [ ] Compare readable descriptions before and after migration.
- [ ] Archive the migration-tool version.

## Consumer behavior

A consumer should:

1. Read `spec_version` before interpreting optional fields.
2. Reject unsupported required behavior with a clear message.
3. Ignore unknown optional metadata only when doing so is safe.
4. Never reinterpret an unknown enum value as a known one.
5. Report which fields were consumed, ignored, or transformed.

## Compatibility test fixture

A compatibility suite should include:

- a minimum valid record;
- a record with optional fields;
- a record with an unknown extension;
- a record with an unsupported version;
- a migration fixture with expected output;
- a record containing invalid duration and missing camera type.
