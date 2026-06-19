# Maintenance Record

## Current release line

Version 0.1 provides a small structured record, a validator, a readable description command, and a JSON Schema.

## Added during the current maintenance cycle

- Required field checks.
- Positive duration checks.
- Camera type checks.
- Versioned schema document.
- Optional extension format guide.
- Command-line validation output.

## Known limits

- The Python validator covers the required MVP fields rather than every JSON Schema keyword.
- Migration commands are not included yet.
- References between multiple records are not validated yet.

## Rules for future changes

- Shared field changes require a schema version review.
- Format changes require valid and invalid examples.
- Unknown optional data should be preserved when practical.
- Incompatible changes require migration notes.

## Initial release

`0.1.0` was created on 2026-06-19.
