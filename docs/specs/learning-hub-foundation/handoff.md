# Learning Hub handoff

[🇺🇸 English](handoff.md) · [🇧🇷 Português](handoff.pt-BR.md) · [🇪🇸 Español](handoff.es.md)

Status: 09B in review; implementation reference, not final AC-09 approval or production deployment. The 09A content revision is merged and CI-approved; exact candidate validation, 09B review and maintainer approval must precede final handoff closure.

## 1. Source and immutable revision

Repository: [RamonRDR/python-study-guide](https://github.com/RamonRDR/python-study-guide), public and MIT licensed. Retain attribution and license. Content candidate (full immutable Git SHA): `03e91ff9952f2b02293f16a11260d166eb00ea8a`, tree `f1cbf0689a8bf1f26539ed1b330b5c51ce7ce4e6`. This is the 09A squash, not the 09B documentation commit, a branch name or a release tag. No tag/release was created. The handoff itself is reviewed in a later commit; do not attempt to place its own SHA inside itself. The approved consumer pin may be selected only after successful validation and maintainer approval.

[PR #113](https://github.com/RamonRDR/python-study-guide/pull/113) · [CI #46059023528](https://github.com/RamonRDR/python-study-guide/actions/runs/46059023528) · [Codex](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226444778) · [Final Pre-Merge Audit](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226469107) · [09A closure](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226902203)

## 2. Architecture and ownership

The guide is the single source of truth; the external site consumes one validated commit at build time, never scraped HTML or per-learner GitHub API calls. Keep independent GitHub/local learning working. Markdown and shared Python stay canonical; structured JSON drives the UI. No paid service, server-side Python execution, AI grading or AI interviewer in scope. Local browser progress is device-specific, not account sync. Accepted ADRs: 0001 source of truth, 0002 content contract, 0003 proposed browser runtime direction (implementation unverified), 0004 manifest. See the ADR index and integration contract for authoritative details.

[ADR](../../adr/README.md) · [Integration contract](integration-contract.md) · [Assessment contract](assessment-contract.md)

## 3. Canonical contract and inventory

| Canonical entry | Version | Schema / validator | Count |
| --- | --- | --- | --- |
| `curriculum/manifest.json` | 1.0.0 | `schemas/curriculum-manifest.schema.json` | 14 / 115 |
| `quizzes/quiz-index.json` | 1.0.0 | `schemas/quiz-index.schema.json`, `schemas/quiz.schema.json` | 160 |
| `exercises/problem-solving/exercise-index.json` | 1.0.0 | `schemas/exercise-index.schema.json`, `schemas/exercise.schema.json` | 30 |
| `interviews/interview-index.json` | 0.1.0 | `scripts/validate_interviews.py` | 60 |
| `interviews/mocks/mock-index.json` | 0.1.0 | `scripts/validate_interviews.py` | 3 |

All five JSON schemas use Draft 2020-12; interview/mock records remain preliminary and use trusted Python validators, not invented JSON schemas. Manifest association_status must be complete. Inventory: 107 lessons + eight projects = 115 entries, 345 localized content paths, 42 module indexes, 243 chapter resources, six global assets. 253 canonical records; 268 associations (160 quiz, 30 exercise, 75 interview prerequisite links, three mock links). Quiz difficulty easy/medium/hard: 64/67/29, 2,850 XP; exercise difficulty 12/12/6, 192 cases; interview junior/mid/senior 24/24/12; mocks 30/45/60 minutes. Existing tests support the counts; see QA report.

## 4. Navigation, localization and resources

Use manifest module/chapter arrays and explicit zero-based order, global previous_id/next_id (null at endpoints), stable IDs and locale-specific index/content/title maps. Default en; supported en, pt-BR, es. Do not use display titles, paths or directory order as identity. Phase metadata is not engineering sprint numbering. Quiz/exercise chapter_id is ownership, interview_ids are reverse prerequisite references, mock_ids belong to the mock lesson. Follow each bank index and typed references; do not parse authoring matrix or master learning paths. Resolve links/assets inside the same verified revision, sanitize Markdown and HTML, preserve locale switching and accessible fallback/error states. Resources are not an execution allowlist; only scripts/example_manifest.txt lists approved repository examples. Optional chapter dependencies absent means unspecified; four external library chapters declare requirements-external.txt.

## 5. Real record examples

- Chapter `getting-started.install-python`: order 0, previous_id null, next_id `getting-started.configure-vscode`, quiz `quiz.interpreter-purpose`, execution unverified.
- Quiz `quiz.absolute-distance-zero`: `quizzes/questions/quiz.absolute-distance-zero.json`, exact accepted string `abs`, `magnitude = ____(-11)`, 10 XP. The solution returns 11.
- Exercise `problem-solving.ascii-digit-counter`: `exercises/problem-solving/ascii-digit-counter/exercise.json`; starter.py and solution.py referenced in record; input `a12-3` returns integer 3; Unicode digits outside ASCII ignored.
- Interview `interview.allowed-tools`: `interviews/questions/interview.allowed-tools.json`; expected answer, explanation, follow-ups and rubric; respect restrictions on AI/tools.
- Mock `mock.junior-30`: `interviews/mocks/mock.junior-30.json`; 30 minutes, four indexed questions, `problem-solving.label-counts`, 100-point self-assessment rubric.

## 6. Deterministic grading

Use trusted scripts/assessment_grading.py as a behavioral reference, not snapshot code. Quiz multiple_choice/error_identification accepts known choice ID string; true_false accepts actual boolean; output_prediction/objective_code_completion accepts string from explicit accepted values. Comparison exact or normalize_lf (CRLF/CR to LF only), no implicit trim/case folding, no eval. Invalid response types/unknown IDs raise a validation error; distinguish invalid from wrong. XP is advisory. Exercises call the declared function with independent deep-copied JSON args and compare return recursively by exact type/value (bool vs int vs float distinct, dictionary keys strings); preserve final inputs, reject output to stdout/stderr and exceptions, forbid nested input-container alias when new_container true. No automatic evaluation of complexity/refactoring or transient mutation; timeout metadata is not enforced by this trusted-fixture grader. Use a lossless strict JSON parser that retains integer and float distinction (e.g. 9007199254740993 and 2432902008176640000), rejects duplicate keys/nonfinite numbers and does not round through JavaScript Number. Open interviews/mocks use reference answers and learner rubrics; no semantic auto-grading. Public tests/solutions are inspectable; UI reveal-on-demand is not secrecy.

## 7. Execution and browser compatibility

All 30 exercises are unverified for browser execution, and allow no external dependencies; local_python 3.13. 114 chapters unverified, File Organizer local_only with localized reason. Do not promote execution status or run unverified/local_only content automatically. ADR 0003 selects pinned Pyodide + Web Worker as future site direction, not a verified implementation. Before enabling an individual exercise, test runtime version, compatibility, deterministic grading, elapsed-time/output limits, cancellation and worker recreation; assess memory, filesystem, storage, network and credential exposure with origin isolation as needed. Worker alone is not a security boundary. Keep local instructions available. Browser/OS/platform/network behaviors not proven by Linux fixtures or Windows File Organizer tests.

## 8. Import, candidate validation and rollback

Use a trusted Git object database (full history, no replacement objects), independently trusted tooling checkout and its five schemas outside the staged snapshot. Install the trusted requirements-assessment.txt (jsonschema 4.26.0 in this revision). Fetch the approved commit once at build time and verify full SHA. Copy the following strict JSON to a lock outside the snapshot. The identical reference file tests/fixtures/learning-hub/handoff-lock.json belongs to 09B tooling, not the 09A snapshot or active site configuration; consumer must independently approve/store its lock. Historical tests/fixtures/learning-hub/consumer-lock.json pins 08C and remains unchanged.

```json
{
  "lock_version": "1.0.0",
  "revision": "03e91ff9952f2b02293f16a11260d166eb00ea8a",
  "versions": {
    "manifest": "1.0.0",
    "quizzes": "1.0.0",
    "exercises": "1.0.0",
    "interviews": "0.1.0",
    "mocks": "0.1.0"
  }
}
```

```bash
# From the independently trusted tooling checkout (Python 3.13).
python -m pip install -r requirements-assessment.txt
python scripts/curriculum_consumer.py --repository /path/to/trusted-source-git --lock /path/to/external/handoff-lock.json
```

The command is the reference validator (uses Git archive and isolated temporary staging; no persistent deployment). Paths are placeholders to replace, not literal working directories. Do not run scripts from the exported content. The validator checks every tracked regular file and directory, path confinement, exact Git blob/tree coverage, trusted schema bytes, versions, strict JSON, unique IDs/navigation and full bank relationships. Reject missing/extra/modified files, symlinks/submodules, unknown or abbreviated SHA, unsupported versions and incomplete associations. The new test_ac09_handoff_content_pin in tests/test_curriculum_acceptance.py copies the lock outside the snapshot, validates exact 09A, compares canonical manifest/paths/bytes against the historical approved fixture and reports evidence in CI. It is pending execution on the PR at authoring time. Git identity is not a signature; trusted local Git database and isolated staging are assumptions, not concurrent filesystem protection. Only after validation succeeds select candidate as active; on failure retain previous approved pin and content, log reason and fail build without partial publication. Rollback: reselect previous known-good full SHA + exact versions, repeat validation/build and publish using consumer-controlled atomic deployment. Synthetic local rollback proven earlier; production atomic deployment/rollback not tested.

## 9. Evidence, acceptance and limits

09A exact push CI passed both required jobs: 180 quality unittest, seven engineering unittest, 406 practical passed/one skipped, Windows 63 passed/17 skipped, 210 approved examples, 9,282 internal links across 583 Markdown, 345 navigation documents. Windows overlaps Linux; do not add counts. Codex on 09A found no issues, final audit recorded. 09B requires fresh exact-head CI including the new pin test, Codex without unresolved findings, distinct final audit, explicit squash approval, then exact push CI. No AC-09 completion before these gates. QA report maps AC-00–09, prior PR evidence and review limits. Sampled 42 locale documents, 314 Python blocks per locale and four record samples, not exhaustive semantic/human audit. Local execution unavailable due to GitHub access from container; no complete external-link, secret-content/history, platform install or browser/security certification. No new paid infrastructure, code runtime or external site implementation. Related guide publication/linking remains separate approval.

[Final QA](final-qa.md) · [AC](acceptance-criteria.md) · [Tasks](tasks.md)

## 10. Consumer implementation checklist

- [ ] Verify approved exact SHA, lock versions, independent validator and schema trust; fail closed before rendering.
- [ ] Import only manifest/index-directed canonical data from the validated snapshot; preserve locale, stable IDs, links, assets and accessibility.
- [ ] Implement deterministic quiz/coding UI without numeric loss or implicit coercion; keep interviews/mocks self-assessed.
- [ ] Keep unverified/local_only execution disabled until per-exercise runtime and isolation checks; preserve manual/local practice.
- [ ] Store progress locally by stable ID and version/revision, handle migration/reset explicitly; no account sync assumption.
- [ ] Validate updates before switching active content, retain prior lock and prove rollback in deployment environment; never fetch per visitor.
- [ ] Review safe renderer, license/attribution, dependency/runtime pin, tests, browser support and operational limitations in the separate site project.
- [ ] Obtain final PR review/maintainer approval and post-merge CI; record handoff document revision separately from content pin.
