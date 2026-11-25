# ADR 0002: Versioned content contract

Status: proposed (direction approved 2026-11-25; pending PR review).

## Context

Markdown provides a good human learning experience but is insufficient alone for reliable programmatic navigation, quiz grading and exercise association.

## Decision

Use JSON records and a versioned curriculum manifest referencing existing files, with stable identifiers independent of order, localized fields and validated references. Keep scripts/example_manifest.txt as the approved execution allowlist. Define preliminary records before authoring pilots; finalize schemas with real examples and tests in Sprints 07–08.

## Alternatives

Infer all metadata from filenames/Markdown (fragile); duplicate Python per locale (maintenance burden); replace Markdown with JSON-only content (degrades GitHub usability).

## Consequences

Validators must detect schema errors, dangling references, unsafe paths, duplicates and locale omissions. Student-facing content remains available in GitHub; structured records are canonical where applicable, with generated views or references preferred over manually maintained duplicate prose.
