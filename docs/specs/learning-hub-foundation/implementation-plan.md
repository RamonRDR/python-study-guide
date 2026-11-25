# Implementation plan

[🇺🇸 English](implementation-plan.md) · [🇧🇷 Português](implementation-plan.pt-BR.md) · [🇪🇸 Español](implementation-plan.es.md)

Status: proposed for review. Execute only after specification PR approval and merge.

## Delivery sequence

| Sprint | Proposed branch | Deliverable / dependency |
| --- | --- | --- |
| 00 | docs/learning-hub-specification | Audit, constitution, specification, plan, tasks, acceptance criteria, preliminary contracts and ADRs. |
| 01 | feat/chapter-navigation | Inventory all chapter/project language files; define ordered navigation, validate reciprocal and cross-module links; existing curriculum first. |
| 02 | feat/getting-started | Add localized onboarding and connect to Fundamentals; extend navigation tests and existing indexes. |
| 03 | docs/readme-and-badges | Update three READMEs, paths, roadmap and structure; badge evidence only. |
| 04 | feat/manual-programming-practices | Teach manual practice and SDD/TDD; reference existing AI-assisted maintenance guidance. |
| 05 | feat/problem-solving-live-coding | Audit prerequisites for all FR-05 topics; teach missing concepts in all three languages before the corresponding practice; then pilot one challenge against the preliminary contract and expand by concept/difficulty with tests. |
| 06 | feat/technical-interview-preparation | Audit and teach remaining interview-specific prerequisites not covered in Sprint 05, then questions and timed mock sets; include rubrics and locale alignment. |
| 07 | feat/quiz-and-exercise-bank | Materialize versioned records and schemas; validate IDs, translations, scoring, solutions and representative incorrect implementations. |
| 08 | feat/learning-hub-content-contract | Finalize curriculum manifest, consumer validation, reference fixtures, versioning and compatibility metadata. |
| 09 | docs/learning-hub-handoff | Full QA, final review, evidence and approved revision handoff. |

Split large sprints into focused PRs with descriptive suffixes. Each branch starts from current main after dependencies merge. Do not merge without maintainer approval. Use squash merging per AGENTS.md.

## Validation strategy

Reuse scripts/check_internal_links.py, scripts/validate_repository_structure.py, scripts/run_examples.py, scripts/example_manifest.txt, tests/ and the quality-checks workflow. The example manifest remains an execution allowlist, not a curriculum source. Add deterministic tests for navigation, schema constraints, ID uniqueness, reference integrity and grading in the sprint that introduces each behavior. Use standard-library validation where sufficient; decide whether a free schema validator is justified when implementing schemas. Keep starter snippets syntactically valid or store incomplete snippets as data rather than breaking compileall.

Use existing Linux and Windows CI jobs; do not broaden OS-specific or network-dependent examples into unconditional browser execution. Browser compatibility is a consumer-side test obligation; define explicit local-only and unverified states.

## Integration strategy

Use a revision-pinned content snapshot at site build time, with normalized repository-relative paths and safe Markdown rendering. No runtime GitHub API dependency per student. The site will own Pyodide/worker lifecycle, UI, progress storage and resource limits; this repository owns content and deterministic test definitions. See [integration contract](integration-contract.md) and [ADR index](../../adr/README.md).

## Change control

For every PR: consult specs, record scope, review diffs, run applicable checks, disclose omissions, request Codex review, address findings, revalidate and obtain explicit approval. Update task status in the same reviewed PR where practical; merge status is evidenced by Git history. Maintain the educational roadmap separately. All public documentation must have EN, PT-BR and ES versions in the same PR; check structural parity and perform human equivalence review.
