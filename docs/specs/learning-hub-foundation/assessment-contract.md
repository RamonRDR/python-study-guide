# Assessment contract and delivery plan

[EN](assessment-contract.md) · [PT-BR](assessment-contract.pt-BR.md) · [ES](assessment-contract.es.md)

Sprints 07A–C2 merged and post-merge CI passed ([PR #102](https://github.com/RamonRDR/python-study-guide/pull/102), [PR #103](https://github.com/RamonRDR/python-study-guide/pull/103), [PR #104](https://github.com/RamonRDR/python-study-guide/pull/104), [PR #105](https://github.com/RamonRDR/python-study-guide/pull/105), [C2 CI](https://github.com/RamonRDR/python-study-guide/actions/runs/45901661393)). D completes the 30-exercise versioned index; AC-07 closure and browser runtime remain outside D.
 
## Scope and acceptance
- Inventory: 115 entries, 345 localized paths, 64 easy / 67 medium / 29 hard quizzes (2,850 XP at 10/20/30). The [allocation matrix](assessment-matrix.json) is engineering planning metadata, not a consumer manifest. Zero allocations preserve manual practice or avoid repeated assessment.
- Before authoring each question, inspect its source sections in all three locales and record exact headings in its prerequisites; teach missing concepts first. The matrix establishes chapter-level paths, not evidence of complete semantic translation review. Do not claim a quiz measures seniority.
- Use JSON Schema Draft 2020-12 plus Python relationship checks; schema version 1.0.0. Preserve existing exercise IDs, paths, solutions, constraints and tests. Unknown fields and unsupported versions fail closed. Existing interviews remain on their own preliminary contract.
- Quiz answers: stable choice ID for multiple_choice/error_identification; strict boolean for true_false; explicit accepted strings for output_prediction/objective_code_completion. Exact comparison unless output_prediction explicitly selects LF normalization; no eval or semantic grading.
- Exercise interface: function_call only in v1, JSON-compatible arguments/results, recursive exact type and value, unchanged input values, silence, declared new-container requirement where applicable. Functional tests cannot prove algorithm complexity or refactoring quality. Timeout is a declared bound, not enforced by the pure comparator. No arbitrary learner code runs in CI.
- JSON decoding must reject duplicate keys and nonfinite numbers. Python integers can exceed JavaScript safe integer range: keep canonical integer tokens, use lossless parsing or Python-side grading in the future consumer; never round or silently coerce. Browser compatibility remains unverified; actual runtime tests belong to the site.
- Validate indexes, ID uniqueness, locale maps, safe existing paths, teaching headings, examples/cases and assessment answers. Keep all code shared. Tests use fixtures, including malformed records; published records arrive in B–D. No new paid services.
 
## Delivery
A: contract, matrix and fixture validators; B: ten quizzes (two per type) and three existing exercises (vowel-counter, binary-insertion-index, inventory-reconciliation); C1: complete 78 foundation quizzes; C2: complete 160; D: remaining 27 exercises; E: AC-07 closure. The ten pilots count toward 160. No later PR until its predecessor is merged and CI passes.
 
## Evidence and limitations
Baseline: `bf56305f42d10ab7c5b31c2b70f6c38140353db4`. See [Sprint 06 closure](https://github.com/RamonRDR/python-study-guide/pull/101#issuecomment-7193467128). Existing 30 exercises have 192 cases and no declared external dependencies; all browser execution is unverified. The older vowel pilot lacked practice_mode and complexity assumptions; these were normalized in B. Preserve the legacy 29-entry expansion index until migration is approved. Review per-question teaching evidence and per-exercise solutions in the corresponding PR. All exact-head CI, Codex Review, Final Pre-Merge Audit and maintainer authorization gates remain mandatory.

## Pilot acceptance (07B)

- Publish exactly ten questions, two per quiz type, seven easy and three medium (130 XP), with three locale variants and exact prerequisite headings. Count them toward the approved matrix, never duplicate the Python code per locale.
- Migrate only vowel-counter, binary-insertion-index and inventory-reconciliation to 1.0.0, preserving all 24 canonical cases and existing implementations. Keep the other 27 legacy records and expansion index unchanged. A versioned partial exercise index identifies the three migrated records.
- Run both new indexes in CI, reject unindexed or unexpected versioned records, test allocation ceilings and verify the trusted solutions and representative wrong candidates. Reject contradictory expected results for equal typed inputs. When a new result container is required, reject aliases to nested mutable input containers as well as direct aliases. Mutation detection compares final input state, not every intermediate operation.
- Use no learner-code execution, new paid dependency or runtime claim. The remaining 150 quizzes and 27 migrations belong to C1/C2/D; AC-07 closes only in E.

## Foundations acceptance (07C1)

- Complete all approved allocations for modules 00–05, including the ten pilot questions: 78 total (37 easy, 30 medium, 11 hard; 1,300 XP). Add 68 records only. Keep the three versioned exercise records and legacy bank unchanged. C2 covers the remaining 82 quizzes.
- Read the teaching sections in EN/PT-BR/ES before drafting; retain exact localized heading references, stable IDs, original examples, single shared code and explicit accepted answers. Refine the two pilot output questions with precise newline prerequisites; retain their answers. Balance true/false answers across the expanded bank and vary choice positions.
- Preserve pilot regression checks while enforcing exact per-chapter difficulty allocation, index coverage, locale parity and deterministic grading. Test trusted literal examples, not arbitrary source read from question records. Review ambiguity, edge cases, difficulty, navigation and privacy before asking for merge approval.
- No runtime, paid dependency, exercise migration or AC-07 closure in C1. All exact-head gates remain mandatory.

## Expansion acceptance (07C2)

- Complete the remaining 82 quizzes per the approved chapter/difficulty matrix: 27 easy, 37 medium, 18 hard (1,550 XP). Preserve the 78 foundation records and their regressions. Final inventory: 160 quizzes, 64 easy/67 medium/29 hard, 2,850 XP. Zero allocations remain empty.
- Read the relevant teaching sections in all three locales before drafting; retain exact headings, original examples, stable IDs, localized prompts, explanations, hints and choices. Diversify formats, emphasizing scenario-based choices, error identification and constrained completion over excessive output prediction; balance true/false and vary choice positions. Avoid questions that claim to measure seniority.
- Require exact full-matrix and index coverage, correct/incorrect response fixtures for each new record, and trusted literal execution for executable shared code (no learner code, network or unsafe file operations). Preserve foundation and pilot regression tests. Maintain locale navigation and verify every link. Keep exercises, their indexes, interview bank, dependencies and runtime unchanged.
- C2 is not AC-07 closure; D migrates the remaining 27 exercises and E closes. Exact-head CI, Codex Review, Final Pre-Merge Audit, explicit approval and post-merge CI remain mandatory.

## Exercise migration acceptance (07D)

- Migrate exactly the remaining 27 records to schema 1.0.0 and complete the versioned index of 30 exercises (12 easy, 12 medium, 6 hard; 192 existing cases). Keep the 3 pilot records and all 160 quizzes unchanged. Preserve existing IDs, paths, original JSON numeric tokens, localized content, examples, cases, starters, references, wrong candidates, complexity, practice modes and timing metadata.
- Add only schema_version and tests.new_container to legacy records. Set the latter true for the eight migrated records returning a new list or dictionary, consistent with their contracts and the existing expansion test's no-alias rule; false for scalar results. The existing pilot inventory has one true flag. Preserve the legacy 29-entry expansion index as a compatibility view, not the canonical versioned index.
- Check all 30 canonical records against schema and relationship validation; use explicit repository-owned fixture paths to test every existing reference and representative wrong implementation, exact type/value, input preservation, silence and nested aliases. Preserve starter-mode checks and independent oracles. Verify large integer tokens with Python exact integer semantics. No learner source execution, new runtime, dependencies or exercise content expansion.
- All execution remains unverified for browsers, declared timeouts are not enforced here, and functional tests do not certify complexity or refactoring quality. AC-07 closes only in E after all exact-head gates and maintainer approval.

## Consolidated acceptance (07E)

- Confirm the complete canonical banks together: 160 quizzes (64 easy, 67 medium, 29 hard; 2,850 XP), 30 exercises (12 easy, 12 medium, 6 hard; 192 existing cases), all schema 1.0.0, five quiz types and function_call exercises. Check exact index coverage, globally distinct record IDs and a shared implementation per exercise.
- Consolidate positive and negative acceptance evidence for AC-07. Exercise both index validators with duplicate IDs and dangling references, reject missing locales, unsupported versions and invalid quiz answers. Use only existing trusted fixtures for deterministic grading and representative wrong implementations; preserve previous regression suites.
- Record D's merge and post-merge CI, mapping each AC-07 requirement to actual verification. Do not claim E is closed before exact-head CI, Codex Review, Final Pre-Merge Audit, explicit maintainer approval, squash merge and post-merge CI. No new learner content, runtime, dependencies or consumer manifest. Browser execution, timeout enforcement and manual complexity/refactoring review remain outside this acceptance.
