# Implementation plan

[🇺🇸 English](implementation-plan.md) · [🇧🇷 Português](implementation-plan.pt-BR.md) · [🇪🇸 Español](implementation-plan.es.md)

Status: proposed for review. Execute only after specification PR approval and merge.

## Delivery sequence

| Sprint | Proposed branch | Deliverable / dependency |
| --- | --- | --- |
| 00 | docs/learning-hub-specification | Audit, constitution, specification, plan, tasks, acceptance criteria, preliminary contracts and ADRs. |
| 01 | feat/chapter-navigation | Inventory all chapter/project language files; define ordered navigation, validate reciprocal and cross-module links; existing curriculum first. |
| 02 | feat/getting-started | Add localized onboarding and connect to Fundamentals; extend navigation tests and existing indexes. Add project-local venv and pip/dependency management lessons; document candidate library expansion separately from the completed Phase 9, with prerequisite review and separate future PRs. Add a sixth Git basics lesson and record future reciprocal cross-guide links in the integration register; keep advanced Git and platform-specific automation in the separate guide. |
| 03 | docs/readme-and-badges | Update three READMEs, paths, roadmap and structure; badge evidence only. |
| 04 | feat/manual-programming-practices | Teach manual practice and SDD/TDD; reference existing AI-assisted maintenance guidance. Apply a small Python-specific branch/PR/test/review workflow without duplicating the independent Git course. |
| 05 | feat/problem-solving-live-coding | Audit prerequisites for all FR-05 topics; teach missing concepts in all three languages before the corresponding practice; then pilot one challenge against the preliminary contract and expand by concept/difficulty with tests. |
| 06A1 | feat/interview-foundations | Lessons 01–08, prerequisite map, OOP |
| 06A2 | feat/interview-python-internals | Lessons 09–14, internals and memory |
| 06A3 | feat/interview-backend-and-databases | Lessons 15–21, backend, SQL, engineering; T06-01 gate |
| 06B | feat/technical-interview-pilot | Lesson 22, nine pilot questions and validation |
| 06C | feat/technical-interview-question-bank | 48 additional technical questions |
| 06D | feat/mock-and-international-interviews | Lessons 23–24, three behavioral/international questions and three mocks; AC-06 |
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

After CI and Codex Review pass on the exact head, complete the Final Pre-Merge Audit defined in AGENTS.md and record evidence in the PR. Any change to the head invalidates those checks and audit; repeat them before maintainer approval.

[Related guide integration register](related-guides.md)
