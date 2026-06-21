# Security Policy

## Supported versions

Security fixes are applied to the current `main` branch and current schema contracts. Older snapshots and unsupported forks may not receive updates.

## Reporting a vulnerability

Do not publish private production records, unreleased scripts, client identifiers, asset paths, credentials, or working exploit details in a public issue.

Use GitHub private vulnerability reporting when available. If unavailable, open a minimal public issue identifying the affected commit, schema version, and component without sensitive content.

Include:

- affected commit and schema version;
- minimal synthetic record or sequence;
- impact summary;
- validator, migration, or adapter path;
- expected and actual behavior.

## Security boundaries

OpenShotSpec validates and transforms structured records. Integrators remain responsible for protecting assets, limiting extension data, validating adapter outputs, controlling downstream tool access, and reviewing migration reports.

Schema validation does not sanitize arbitrary downstream prompts or vendor-specific extension payloads.

## Out of scope

- vulnerabilities in unrelated rendering tools;
- confidential content posted publicly by users;
- unsupported vendor extensions;
- copyright or policy clearance;
- unsupported local modifications.

## Disclosure

Allow maintainers reasonable time to reproduce, correct, test, and document a confirmed issue before public disclosure.
