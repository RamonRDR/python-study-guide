# ADR 0001: Content source of truth

[🇺🇸 English](0001-content-source-of-truth.md) · [🇧🇷 Português](0001-content-source-of-truth.pt-BR.md) · [🇪🇸 Español](0001-content-source-of-truth.es.md)

Status: accepted architecture direction ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)); browser execution remains unverified.

## Context

The existing guide is independently usable in three languages. A future website needs the same material without manually maintaining copies or coupling the guide to the site.

## Decision

Keep the GitHub repository authoritative for Markdown, Python and structured data. Import validated, immutable revisions during the site build. Preserve existing paths and GitHub/local usability. Keep site implementation outside this repository.

## Alternatives

Separate manually maintained site content (rejected: drift); runtime GitHub API requests for every learner (rejected as default: availability/rate-limit dependency); scrape GitHub HTML (rejected: fragile presentation coupling).

## Consequences

Consumer needs an explicit update/build process, revision tracking, safe rendering and validation. Content updates may not appear on the site until rebuilt. No new paid service is planned.
