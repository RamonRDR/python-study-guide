# ADR 0003: Browser execution and assessment

[🇺🇸 English](0003-browser-execution.md) · [🇧🇷 Português](0003-browser-execution.pt-BR.md) · [🇪🇸 Español](0003-browser-execution.es.md)

Status: proposed (direction approved 2026-11-25; pending PR review).

## Context

Interactive practice should require no new paid infrastructure. The guide includes both portable Python and platform-specific examples.

## Decision

Use Pyodide with a pinned runtime and Web Worker in the separate site project for verified compatible exercises only. Keep local execution supported. Use deterministic tests, objective quiz comparison, and self-assessment rubrics. Do not implement AI interviewers or semantic grading. Default progress storage to local browser storage.

## Alternatives

Remote Docker/Python execution (rejected for cost and operational burden); AI-based grading (out of scope); browser-only guide (rejected because platform-specific material must remain usable).

## Consequences

Browser runtime startup, package support, OS differences, isolation, interruption and output limits need validation by the site project. Workers are not sufficient alone for secure isolation. Public answers can be inspected and local progress may be lost. Costs remain contingent on existing hosting limits; no claim of unlimited capacity.
