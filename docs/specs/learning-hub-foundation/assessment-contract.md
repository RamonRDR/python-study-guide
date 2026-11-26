# Assessment contract and delivery plan

[EN](assessment-contract.md) · [PT-BR](assessment-contract.pt-BR.md) · [ES](assessment-contract.es.md)

Sprint 07A: foundation only. The maintainer approved the 160-question allocation and pilot. This PR does not publish questions, migrate exercises, implement browser execution or finalize the curriculum manifest.
 
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
Baseline: `bf56305f42d10ab7c5b31c2b70f6c38140353db4`. See [Sprint 06 closure](https://github.com/RamonRDR/python-study-guide/pull/101#issuecomment-7193467128). Existing 30 exercises have 192 cases and no declared external dependencies; all browser execution is unverified. The older vowel pilot lacks practice_mode and complexity assumptions; normalize these explicitly during migration. Preserve the legacy 29-entry expansion index until migration is approved. Review per-question teaching evidence and per-exercise solutions in the corresponding PR. All exact-head CI, Codex Review, Final Pre-Merge Audit and maintainer authorization gates remain mandatory.
