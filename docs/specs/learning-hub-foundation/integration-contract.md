# Learning Hub integration contract

[🇺🇸 English](integration-contract.md) · [🇧🇷 Português](integration-contract.pt-BR.md) · [🇪🇸 Español](integration-contract.es.md)

Status: preliminary for the consumer manifest and integration fixtures in Sprint 08. The versioned assessment schemas and records follow the [assessment contract](assessment-contract.md). No runtime integration is implemented here.

## Version and transport

The public repository is authoritative. Consumer imports content at build time using an approved immutable Git commit SHA (a release tag may identify that SHA). The consumer records both revision and schema_version, rejects unsupported major versions, and fails the build on invalid data rather than silently mixing revisions. Use UTF-8 JSON and Markdown, no GitHub HTML scraping. No per-visitor GitHub API requests or paid services are required.

## Shared conventions

- Locales: en (default), pt-BR, es. Student-visible fields require all three translations; shared Python files and IDs remain English.
- IDs: stable, lowercase ASCII dotted/hyphenated strings; independent of display titles/order; never reuse an ID for a different item. Uniqueness per entity type, references explicitly typed by field.
- Paths: repository-relative POSIX paths; no absolute paths, traversal, backslashes, URL schemes or symlink escapes. Verify existence and confinement before import. Render Markdown/HTML safely, resolve links/assets within the same revision and sanitize untrusted content.
- Orders are explicit nonnegative integers, unique within siblings; previous/next follows curriculum order, not lexicographic directory order. Endpoints have null neighbors.
- Optional metadata has explicit documented defaults; unsupported capability must not be silently assumed.

## Preliminary record model

| Entity | Required fields for pilot |
| --- | --- |
| Curriculum | schema_version, default_locale, supported_locales, modules |
| Module | id, order, slug, title (locale map), index (locale path map), chapters |
| Chapter | id, order, slug, title, content (locale path map), assets, previous_id, next_id, exercise_ids, quiz_ids, interview_ids, execution |
| Quiz | id, chapter_id, difficulty, type, prompt (locale map), choices (stable choice IDs and translated text where applicable), answer, explanation, hints, xp |
| Exercise | id, chapter_id, difficulty, estimated_minutes, title, prompt, concepts, constraints, examples, starter_path or starter text, hints, solution_path, explanation, complexity (time/space where meaningful), tests, execution, allowed_dependencies |
| Interview question | id, topic, level, prompt, expected_answer, explanation, intent, common_errors, follow_ups, examples, rubric |
| Mock | id, level, duration_minutes (30/45/60), question_ids, exercise_ids, scoring rubric |

Localized fields include all learner-visible explanations, alternatives, examples that contain prose, hints, scoring descriptions and rubrics. Use IDs for internal concept references where possible. Quiz types: multiple_choice, true_false, error_identification, output_prediction, objective_code_completion. Difficulty: easy/medium/hard. Quiz answers use stable choice IDs, booleans or explicit accepted strings according to type. XP is a nonnegative integer and advisory, not certification.

## Example (illustrative only, not a published manifest)

```json
{
  "id": "fundamentals.print-and-input",
  "order": 2,
  "slug": "print-and-input",
  "content": {
    "en": "fundamentals/02-print-and-input/README.md",
    "pt-BR": "fundamentals/02-print-and-input/README.pt-BR.md",
    "es": "fundamentals/02-print-and-input/README.es.md"
  },
  "previous_id": "fundamentals.how-python-runs-a-program",
  "next_id": "fundamentals.variables-and-naming",
  "execution": "unverified"
}
```

This fragment omits other required metadata and is not a complete schema-valid record. Paths are existing files; IDs are proposed.

## Grading and execution

Quiz grading is deterministic. Compare exact canonical values by default; normalize line endings or whitespace only when the question explicitly permits it. Coding tests declare a function-call or stdin/stdout interface, JSON-compatible inputs/expected outputs, comparison rules (including tolerance only if specified), edge cases and execution bounds. Use reference solutions and representative incorrect solutions to validate test discrimination. Do not execute arbitrary learner code as part of repository CI.

Execution values: browser_compatible (verified against a pinned runtime), local_only (document reason), unverified (default; no automatic browser execution). Local Python and allowed dependency requirements must be explicit. Browser compatibility is per exercise, not inferred from all code in a chapter. Filesystem, network, external libraries and OS-dependent examples need individual assessment.

Consumer requirements: run learner code off the UI thread with a dedicated Web Worker; limit elapsed time and output, terminate/recreate on timeout or cancellation, avoid exposing privileged browser credentials, and isolate execution from the main application origin where necessary. A Worker alone is not a security boundary; assess network/storage access and sandbox design before deployment. No claim of hard memory isolation. Test runtime version and browser support in the site project. No server execution in this phase.

Public solutions and tests are inspectable; reveal hints/solutions only on demand in the UI, not as a security guarantee. Open interview questions use reference answers and rubric-based self-assessment, never automatic semantic grading.

## Ownership

Guide: Markdown, metadata, examples, reference solutions, tests, rubrics and schema validation. Site: safe renderer, editor, runtime, deterministic grading UI, local progress, accessibility, and deployment. Local browser storage is device-specific and may be cleared; no backend sync assumed.

## Remaining decisions

Finalize file layout, full schemas and versioning policy, exact scoring/comparison semantics, safe content rendering and browser runtime pin after pilots. Document compatibility and migration examples in the final handoff. See [ADR index](../../adr/README.md).

## Sprint 08A · Curriculum manifest 1.0.0

The manifest-specific decisions below supersede the preliminary manifest model above; bank contracts remain unchanged.

Publish `curriculum/manifest.json` with `schemas/curriculum-manifest.schema.json` (Draft 2020-12, manifest version 1.0.0). Reuse the existing jsonschema dependency and strict assessment JSON/path helpers. The manifest references source files, never duplicates lesson or assessment bodies. The 115 stable chapter IDs come from the assessment matrix; order and titles come from the three learning paths. Preserve the historical project foundation separately from curriculum order 00, educational phases 1–12 and the complementary module. Module and chapter orders are zero-based or greater, contiguous within siblings, and independent of IDs; previous/next spans the complete curriculum.

The manifest includes localized titles, index/content paths, chapter kind, resources and assets, execution metadata, typed assessment references and canonical bank descriptors. The four banks remain separately versioned: quiz/exercise 1.0.0, interview/mock 0.1.0. Interview references on chapters identify documented prerequisite relationships, not ownership; mock references identify the mock lesson. Quiz/exercise ownership uses existing chapter_id. No inferred pedagogical associations. Chapter execution is unverified or local_only with a localized reason; browser_compatible requires actual pinned-runtime evidence at exercise level. Optional local Python/dependency metadata means unspecified when absent, not unrestricted.

A manifest with association_status pending is a development artifact only; consumers require complete and full reference validation. A validates schema and confined files on synthetic fixtures; B publishes inventory with pending associations; C completes and validates associations; D proves pinned-revision consumption; E closes AC-08. All supported versions are explicit (initially exact versions); unsupported or unknown data fails closed. Preserve integer tokens, reject duplicate keys/nonfinite values, no JavaScript numeric rounding. Consumers store an approved full commit SHA and supported versions outside the snapshot; verify the checked-out commit and import only files from it. Never self-embed the SHA or fetch per learner. Related guides are optional and deferred until verified. No site or runtime implementation here.

[ADR 0004](../../adr/0004-curriculum-manifest.md).

## Sprint 08B · Curriculum inventory

08B publishes the first complete curriculum inventory: 14 modules, 107 lessons and eight practical projects, 115 stable chapter IDs and 345 localized content paths. Source ordering and titles must match the three master learning paths exactly (plain display text; remove inline code delimiters only). Module names come from the localized section headings, without phase/status prefixes. Preserve matrix IDs as the reviewed baseline, including the three historical problem-solving exceptions; the matrix is planning evidence, not a consumer input. Use contiguous zero-based module and chapter orders, explicit global previous/next, phase metadata distinct from curriculum order, and canonical localized module indexes. Verify all source paths and tracked chapter coverage. Inventory includes every tracked non-content file under each chapter as a resource, or as an asset for supported image extensions; root assets are tracked images under assets/. Resources are references, not an execution allowlist. Optional dependency paths are declared for the four external-library lessons using the existing shared requirements file; File Organizer is local_only because it exercises platform-specific filesystem behavior. All other chapters are unverified, with no browser compatibility claim. B requires pending association_status and empty typed association lists; C will populate those lists and validate relationships. CI verifies the actual checked-in manifest plus negative regression fixtures; use Git tracked files for authoring inventory, not untracked caches or a consumer's runtime API. No source duplication, new dependencies or site.
