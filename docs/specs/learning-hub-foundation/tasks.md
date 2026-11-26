# Phase II task register

[🇺🇸 English](tasks.md) · [🇧🇷 Português](tasks.pt-BR.md) · [🇪🇸 Español](tasks.es.md)

Sprints 00–06 and 07A–B merged. C1 implements 78 foundation quizzes; closure requires exact-head CI, Codex Review, Final Pre-Merge Audit, maintainer approval and post-merge CI.

| Task | Sprint | Dependency | Status |
| --- | --- | --- | --- |
| T00-01 Confirm repo, baseline, branches and CI | 00 | None | Done (read-only audit) |
| T00-02 Audit tree and representative docs/scripts | 00 | T00-01 | Done (sampled content) |
| T00-03 Approve architecture and documentation approach | 00 | T00-02 | Done (maintainer approval) |
| T00-04 Prepare trilingual SDD documents and preliminary contract | 00 | T00-03 | Done ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)) |
| T00-05 Verify specification PR, CI and Codex findings | 00 | T00-04 | Done ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)) |
| T00-06 Obtain approval and merge | 00 | T00-05 | Done ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)) |
| T01-01 Inventory navigation and implement locale-safe links/tests | 01 | T00-06 | Done ([PR #88](https://github.com/RamonRDR/python-study-guide/pull/88)) |
| T02-01 Author six Getting Started lessons, including project environments, dependency management and Git basics; link to Fundamentals and map future cross-guide references | 02 | T01-01 | Done ([PR #89](https://github.com/RamonRDR/python-study-guide/pull/89)) |
| T03-01 Align README, roadmap, learning path, structure and badges | 03 | T02-01 | Done ([PR #90](https://github.com/RamonRDR/python-study-guide/pull/90)) |
| T04-01 Add manual practice and engineering guidance | 04 | T03-01 | Done ([PR #91](https://github.com/RamonRDR/python-study-guide/pull/91)) |
| T05-00 Map all FR-05 prerequisites to existing lessons and teach missing concepts in EN/PT-BR/ES before challenge publication | 05 | T04-01 | Done ([PR #92](https://github.com/RamonRDR/python-study-guide/pull/92); [map](prerequisite-map.md)) |
| T05-01 Pilot challenge records and grading tests | 05 | T05-00 | Done ([PR #93](https://github.com/RamonRDR/python-study-guide/pull/93)) |
| T05-02 Expand challenges by topic/difficulty | 05 | T05-01 | Done ([PR #94](https://github.com/RamonRDR/python-study-guide/pull/94), [PR #95](https://github.com/RamonRDR/python-study-guide/pull/95), `21c00c32b91a0116c8a50e89687b91f8efa04cb5`, [CI](https://github.com/RamonRDR/python-study-guide/actions/runs/45720384626)) |
| T06-01 Map remaining interview-specific prerequisite gaps and teach necessary concepts not covered in Sprint 05 | 06 | T05-02 | Done: lessons 01–21 merged in #98; post-merge CI passed ([#98](https://github.com/RamonRDR/python-study-guide/pull/98), [CI](https://github.com/RamonRDR/python-study-guide/actions/runs/45730226049)) |
| T06-02 Author question bank and timed mocks/rubrics | 06 | T06-01 | Done: 60 questions and three timed mocks; [PR #101](https://github.com/RamonRDR/python-study-guide/pull/101), [post-merge CI](https://github.com/RamonRDR/python-study-guide/actions/runs/45829816717) |
| T07-01 Finalize and validate quiz/exercise schemas and records | 07 | T06-02 | In progress: A and B merged ([PR #102](https://github.com/RamonRDR/python-study-guide/pull/102), [PR #103](https://github.com/RamonRDR/python-study-guide/pull/103)); C1 implements 78 quizzes; C2–E pending |
| T08-01 Finalize curriculum manifest and integration fixtures | 08 | T07-01 | Pending |
| T09-01 Execute QA and record actual evidence | 09 | T08-01 | Pending |
| T09-02 Obtain final review and publish revision-pinned handoff | 09 | T09-01 | Pending |

Update statuses with evidence links in subsequent focused PRs. Done means the associated acceptance criteria are satisfied; sprint completion requires review and maintainer approval. Do not infer completion from this plan.
