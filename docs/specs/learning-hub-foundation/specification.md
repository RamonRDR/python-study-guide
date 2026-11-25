# Phase II: Learning Hub Foundation — specification

[🇺🇸 English](specification.md) · [🇧🇷 Português](specification.pt-BR.md) · [🇪🇸 Español](specification.es.md)

Status: proposed for review. Direction approved 2026-11-25. Baseline: main at 86f1c8517ef8e0e51d97e03388075a4d3fe41386.

## Purpose

Improve the independent Python Study Guide and make its content consumable by a future personal-site Learning Hub, without implementing the website here. Support manual practice, international technical interviews and independent study on GitHub.

## Baseline

The original foundation and educational phases 1–10 are complete according to the existing roadmap. The audit found 57 chapter directories plus 8 practical projects, each with EN/PT-BR/ES READMEs (195 files), 498 tracked files and 221 Python files. File presence is not proof of translation equivalence. Main's 2026-11-10 quality workflow succeeded (run 42921078332); no new test execution was performed during the audit. Historical README badge counts refer to run 34731456104 and must not be treated as live counts.

Existing assets, [learning path](../../learning-path.en.md), [roadmap](../../roadmap.en.md), [project structure](../../project-structure.en.md), [agent instructions](../../../AGENTS.md), [PR template](../../../.github/pull_request_template.md), and quality scripts remain authoritative within their existing scopes.

## Functional requirements

| ID | Requirement |
| --- | --- |
| FR-01 | Provide previous/index/next navigation at consistent locations, including cross-module transitions and first/last boundaries, in all three languages. |
| FR-02 | Add introductory Getting Started (curriculum order 00), before Fundamentals, without renumbering existing paths. Cover official Python and VS Code downloads, Windows/macOS/Linux, PATH where relevant, terminal verification, Python extension, interpreter selection, folders, .py files, integrated terminal, first manual execution and troubleshooting. VS Code is recommended, not required. Reuse Fundamentals for conceptual Hello World instruction. Teach creation, activation (or direct executable use), verification, VS Code selection, deactivation and recreation of project-local .venv on Windows/macOS/Linux; pip installation, inspection, dependency recording and restoration, Git exclusion and a library overview distinguishing existing chapters from future candidates. No mandatory Playwright or other new package dependencies in repository CI. |
| FR-03 | Update all three READMEs, learning paths, roadmap, structure and prerequisites as appropriate; preserve banner, slogan, authorship and relevant technical guidance. Badge numbers must come from identified successful validations. |
| FR-04 | Teach manual coding, error interpretation, official documentation, testing, independent attempts, requirements, specifications, plans, tasks, acceptance criteria, ADRs and review. Explain SDD and TDD complementarity; place content after checking overlaps. |
| FR-05 | Add curriculum phase 11, Problem Solving & Live Coding: reasoning, strings/numbers, collections, functions/recursion, search/sort, algorithms/complexity, debugging, refactoring, mixed challenges and timed practice. Easy/Medium/Hard; progressive hints, reference solutions, complexity and tests including edges. Before any affected challenge, map prerequisites to existing lessons and teach missing concepts (including recursion, search/sort and algorithm complexity) in all three languages; link the instruction before practice. |
| FR-06 | Add curriculum phase 12, Technical Interview Preparation: interview process, fundamentals, data structures, OOP, internals, memory, exceptions, testing/debugging, APIs/backend, databases/SQL, engineering practices, behavioral and take-home tasks, junior/mid/senior mock interviews, international interviews and technical English. Include expected answers, explanations, intent, common errors, follow-ups, examples, 30/45/60-minute mocks and objective self-assessment rubrics. |
| FR-07 | Provide machine-readable quizzes and exercise contracts, stable IDs, three locales, objective grading for supported types, original shared Python code and reference solutions tested against representative wrong answers. Preserve GitHub and local use. |
| FR-08 | Provide versioned curriculum manifest, schemas, relationships, translated titles, paths, resources, exercise/quiz/mock associations and browser compatibility. Consume a validated immutable revision rather than scraping GitHub HTML. |
| FR-09 | Validate all new and affected content and deliver a handoff containing approved revision, contracts, example records, results, limitations and remaining work. |

## Non-functional requirements

- NFR-01: no extra financial cost or new paid server/service/API; no web implementation in this repository.
- NFR-02: no unnecessary content duplication; shared code in English; all public documentation in three languages, including architecture and engineering. Private documentation stays outside the public repository, preferably in English.
- NFR-03: preserve existing paths and functionality; validate links, navigation, examples and tests.
- NFR-04: stable identifiers independent of order, relative paths confined to the repository, versioned schema and revision traceability.
- NFR-05: no AI grading; public answers are only visually concealed; open responses use reference answers and self-assessment.
- NFR-06: browser execution is opt-in per exercise, subject to runtime verification; local Python remains supported. No secrets or confidential examples.
- NFR-07: never report an unrun check as passed. Use existing CI and add gates incrementally.

## Scope boundaries

In scope: educational content, metadata, validation and handoff. Out of scope: site UI, authentication, cloud progress sync, server execution, payment, certification, production deployment and automated semantic evaluation.

OOP, SQL, algorithms and internals are not all taught as standalone modules today. Introduce missing prerequisites before evaluating them; do not silently assume mastery or renumber phases. Historical engineering Phase 0 remains Project Foundation; curriculum order 00 is Getting Started.

## References

- [Constitution](../constitution.md)
- [Implementation plan](implementation-plan.md)
- [Tasks](tasks.md)
- [Acceptance criteria](acceptance-criteria.md)
- [Integration contract](integration-contract.md)
- [Architecture decisions](../../adr/README.md)
- [Handoff](handoff.md)
