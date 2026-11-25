# Acceptance criteria

Status: proposed for review. Criteria are requirements, not results.

| ID | Sprint | Acceptance condition |
| --- | --- | --- |
| AC-00 | 00 | Specification, constitution, plan, tasks, criteria, preliminary integration contract, ADRs and handoff placeholder exist; AGENTS references them; existing educational content and workflows unchanged; CI and review evidence recorded; maintainer approves before merge. |
| AC-01 | 01 | Every existing chapter/project locale has correct previous/index/next navigation, except missing neighbors at true endpoints; links resolve in the same locale, cross-module boundaries are reciprocal, and automated tests reject wrong targets and missing links. |
| AC-02 | 02 | Localized onboarding covers all FR-02 topics; official download links and OS-specific commands verified; a learner can install, select interpreter, create and run a file; no chapter renumbering; navigation includes new module. |
| AC-03 | 03 | All three READMEs and affected indexes/structure agree with actual paths and published statuses; banner/license preserved; every numerical badge identifies genuine evidence, without summing overlapping suites. |
| AC-04 | 04 | Three-language manual practice guidance and SDD/TDD explanations include original examples, explicit requirements/acceptance and independent practice; distinguish student workflow from maintenance AI use. |
| AC-05 | 05 | Challenges cover FR-05 topics at suitable difficulty; each has stable ID, localized prompt, time estimate, concepts, constraints, examples, starter, progressive hints, reference, explanation, complexity, tests and edge cases where relevant; local tests pass and detect representative incorrect solutions. |
| AC-06 | 06 | FR-06 topics are addressed with documented prerequisites; questions have expected answers, explanation, intent, common errors, follow-ups and examples; 30/45/60-minute mock sets have explicit scoring rubrics; no AI interviewer or claim of automatic semantic evaluation. |
| AC-07 | 07 | Valid quiz/exercise records exist for supported types; invalid schema, duplicate ID, missing locale, invalid answer or dangling reference fails validation; deterministic grading and representative wrong-solution tests pass; no duplicated language-specific Python implementations. |
| AC-08 | 08 | Manifest provides stable module/chapter ordering, paths, locales, titles, relationships, associations and compatibility; schema and cross-reference validators reject unsafe paths, missing content and unsupported versions; a consumer fixture resolves content from an immutable revision without HTML scraping. |
| AC-09 | 09 | All applicable checks pass for approved revision; translation parity reviewed; limitations and unrun checks disclosed; handoff includes contract, paths, schemas, examples, grading, ADRs, pendencies and evidence; final Codex review and maintainer approval obtained. |

## Global definition of done

Every affected locale is aligned; tests and links are checked; no known regressions or unresolved relevant findings; no credentials or private data; documentation and task register current; maintainer approves the merge. When validation cannot be run, record what was not run and why rather than marking it passed. Semantic translation review is a human check, not guaranteed by structural validation.
