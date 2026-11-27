# Final QA and acceptance evidence (09A)

[EN](final-qa.md) · [PT-BR](final-qa.pt-BR.md) · [ES](final-qa.es.md)

Baseline evidence, not final AC-09 approval. Maintainer approved the two-PR plan. The source is the exact post-merge main commit below; the QA PR itself requires fresh CI, Codex, final audit, explicit squash authorization and push CI. 09B will validate the resulting content commit using an external lock and complete the handoff.

## Verified baseline and governance

`a8a264f9f36ec276f0ad8e35f10f2d76f82fe211`

[PR #112](https://github.com/RamonRDR/python-study-guide/pull/112) · [CI #46053604048](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048) · [Linux job](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048/job/140690676913) · [Windows job](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048/job/140690677260) · [AC-08](https://github.com/RamonRDR/python-study-guide/pull/112#issuecomment-7226219176)

Main matched the audited tree `ef3b153ceae4eb98e97c124510e7962ff5969a90`, no open PRs at the initial check. Ruleset 20301083 was active, strict checks, required PR and thread resolution, linear history, squash-only, deletion/non-fast-forward protection, no bypass. No required human approval count; maintainer approval and Codex remain operational gates. MIT license, creator attribution and contribution policy inspected. Recursive tree contained 1,236 blobs, no symlinks/submodules or filenames matching common private key/credential/.env patterns; filename screening is not a secret scan or full historical privacy audit. No security certification.

## CI results (separate suites)

| Suite | Passed | Skipped |
| --- | ---: | ---: |
| Quality unittest | 180 | 0 |
| Engineering unittest | 7 | 0 |
| Practical pytest (Linux) | 406 | 1 |
| File Organizer pytest (Windows) | 63 | 17 |

The same Linux run completed 210 allowlisted examples, 9,273 internal links across 580 Markdown files, language structure, 345 navigation documents, compileall, repository structure, assessment and curriculum inventories, and the historical pinned consumer fixture. The Windows suite is a subset of Linux practical tests; do not add counts. External URL availability and unlisted example execution are not proven.

## Acceptance traceability

| Criterion | Merged evidence | Baseline verification / residual limit |
| --- | --- | --- |
| AC-00 | [PR #87](https://github.com/RamonRDR/python-study-guide/pull/87) | Constitution, specifications, ADRs and workflow present; historical merge verified. |
| AC-01 | [PR #88](https://github.com/RamonRDR/python-study-guide/pull/88) | Navigation checker and negative tests; 345 localized documents. |
| AC-02 | [PR #89](https://github.com/RamonRDR/python-study-guide/pull/89) | Six onboarding lessons and established Git/environment scope; install/download/network instructions not rerun on each OS. |
| AC-03 | [PR #90](https://github.com/RamonRDR/python-study-guide/pull/90) | Three READMEs and master paths inspected; evidence badges refreshed in 09A, structural checks rerun in PR. |
| AC-04 | [PR #91](https://github.com/RamonRDR/python-study-guide/pull/91) | Manual practice and SDD/TDD guidance; seven engineering tests; sampled introduction. |
| AC-05 | [PR #95](https://github.com/RamonRDR/python-study-guide/pull/95) | Prerequisite map, challenge and migration tests; 30 canonical exercises, trusted reference and wrong-solution tests. |
| AC-06 | [PR #101](https://github.com/RamonRDR/python-study-guide/pull/101) | Prerequisite map, question/mocks validators; 60 questions and three mocks, human self-assessment. |
| AC-07 | [PR #107](https://github.com/RamonRDR/python-study-guide/pull/107) | All 160 quizzes and 30 exercise records covered by existing validator/fixture tests; strict JSON/types, wrong answers and reference/negative implementations. |
| AC-08 | [PR #112](https://github.com/RamonRDR/python-study-guide/pull/112) | Complete manifest/relationships; pinned 08C and temporary 08D evidence, semantic-negative Git snapshots and rollback fixtures. |
| AC-09 | 09A / 09B | 09A evidence and docs in review; final 09B handoff, candidate pin validation and exact-head/post-merge gates pending. |

## Curriculum and assessment inventory

Directly counted from the manifest and four indexes: 14 modules, 115 unique entries (107 lessons + eight projects), 345 localized content paths, 42 localized module indexes, 243 chapter resources and six global assets. Four banks: 160 quizzes, 30 exercises, 60 interview questions and three mocks (253 distinct records; 268 associations: 160/30/75/3). The 75 interview links are prerequisite references, not 75 questions. The manifest is complete, version 1.0.0. Quiz/exercise 1.0.0; interview/mock indexes preliminary 0.1.0; external fixture lock 1.0.0. All five schemas Draft 2020-12. Existing passing tests assert the 64/67/29 quiz difficulty distribution and 2,850 XP, 12/12/6 exercise distribution and 192 cases, 24/24/12 interview distribution and 30/45/60-minute mock durations. These latter values are test-backed, not a separate manual recount of every record.

Reviewed selected fields of the real records `quiz.absolute-distance-zero` (abs(-11) = 11, exact answer `abs`), `problem-solving.ascii-digit-counter` (literal ASCII digits, not arbitrary Unicode digits), `interview.allowed-tools` (respect tool rules and disclosure), `mock.junior-30` (timed slots, linked question/exercise and manual rubric). Their reviewed EN/PT-BR/ES text is conceptually aligned. No exhaustive semantic reread of the 253 records.

## Targeted locale review

Fetched the first curriculum entry of each module in all three locales (42 documents). Compared introductory concepts, headings and exact fenced Python blocks programmatically; all matching blocks were byte-equal across locales (314 per locale, not all repository examples). This is targeted AI-assisted inspection, not full semantic or human review of each page; no certification of translation quality. Structural coverage of all 345 documents comes from CI. Earlier focused PRs and prerequisite maps are additional evidence, not a substitute for independent review.

| Entry directory (README.md, README.pt-BR.md, README.es.md) | Python blocks per locale |
| --- | ---: |
| `getting-started/01-install-python` | 0 |
| `fundamentals/01-how-python-runs-a-program` | 9 |
| `strings-and-numbers/01-string-creation-and-indexing` | 25 |
| `collections/01-list-creation-and-indexing` | 22 |
| `program-flow/01-conditions-comparisons-and-boolean-logic` | 46 |
| `functions/01-defining-and-calling-functions` | 30 |
| `comments-and-documentation/01-comments` | 46 |
| `errors-files-and-modules/01-try-except-else-finally` | 39 |
| `standard-library/01-pathlib` | 37 |
| `external-libraries/01-pandas` | 52 |
| `practical-projects/01-expense-tracker` | 7 |
| `manual-programming-practices/01-manual-coding-and-debugging` | 1 |
| `problem-solving-and-live-coding/01-problem-solving-fundamentals` | 0 |
| `technical-interview-preparation/01-understanding-technical-interviews` | 0 |

## Limits and next gate

No local run: network access from the local execution container could not resolve GitHub; baseline execution evidence is the actual GitHub Actions run. No isolated Red or new production behavior; no added tests merely to increase counts. No full independent review of all prose, inline code, links outside the repository, credentials in file contents/history, or all platform installs. Earlier reviewed PRs remain evidence; maintainer must assess the residual semantic-review risk. Only the pinned consumer fixture on Linux and File Organizer tests on Windows were exercised. 114 curriculum entries and all 30 exercises are browser-unverified; File Organizer is local_only. Four external-library lessons declare requirements-external.txt; no chapter minimum Python version invented. Web Worker is not a security boundary; browser runtime, timeouts, cancellation, output/network/storage/credential isolation and actual deployment remain consumer work. Tests do not prove complexity/refactoring or transient mutation; snapshot identity is not signature verification. Git object store/trusted validator and isolated staging are assumptions, not concurrent filesystem protection. No production atomic rollback tested, no site, no release/tag or cross-guide link changes. 09B must validate the actual approved 09A squash revision; the historical 08C fixture is not a production pin.

## Sprint 09B · AC-09 handoff gate

09A closed after exact push CI on `03e91ff9952f2b02293f16a11260d166eb00ea8a`. [PR #113](https://github.com/RamonRDR/python-study-guide/pull/113) · [CI #46059023528](https://github.com/RamonRDR/python-study-guide/actions/runs/46059023528) · [closure](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226902203).

At 09B authoring time, 09A is closed. Its exact squash and post-merge evidence are recorded below; original baseline numbers above remain historical. The 09B pin test and final gates remain pending. [Handoff](handoff.md).
