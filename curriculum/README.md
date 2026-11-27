# Curriculum manifest

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

The versioned [manifest.json](manifest.json) contains the complete Sprint 08B inventory: 14 modules, 107 lessons, eight practical projects, 345 localized chapter/project paths, 42 localized module indexes, 243 shared chapter resources and six global images. It references existing files and preserves the approved stable IDs. Ordering, display titles and localized paths follow the three learning paths; the historical assessment matrix is used only for authoring baseline verification. No content is duplicated.

**Relationships complete, consumer revision acceptance pending:** `association_status` is `complete`. Quiz/exercise IDs identify ownership by chapter_id. Interview IDs are reverse links from documented prerequisite lessons, not ownership; a question may appear on multiple chapters. All three mocks are linked to the mock lesson and retain their indexed question/exercise references. Bank versions remain 1.0.0 for quiz/exercise and preliminary 0.1.0 for interview/mock. All 253 records are covered; no record bodies are duplicated. Chapters remain unverified except File Organizer (local_only with reason); external-library lessons reference the existing requirements file. No browser execution or exact minimum Python version is asserted.

Run the structural check or the stronger tracked authoring inventory and relationship check from the repository root after installing the existing assessment validation dependency. The latter validates all canonical records with strict JSON, compares exact association arrays, preserves inventory regressions and requires a Git checkout. Structural-only success is not full acceptance. `python scripts/curriculum_relationships.py` emits the deterministic association map from the existing banks without modifying files. Neither command verifies immutable consumer revision identity; that remains 08D, with final acceptance in 08E.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.md) · [Integration contract](../docs/specs/learning-hub-foundation/integration-contract.md)

```bash
python scripts/validate_curriculum.py
python scripts/validate_curriculum.py --inventory
```

## Pinned consumer fixture (Sprint 08D)

The external test-only [consumer lock](../tests/fixtures/learning-hub/consumer-lock.json) pins the reviewed 08C commit `ffb53c7b64a602f09f9943489ec7741d72843831` and exact supported versions. It is not a production release or a self-reference in the manifest. In a Git checkout with that commit available, run:

```bash
python scripts/curriculum_consumer.py
```

The trusted consumer code exports the pinned Git tree into isolated temporary staging, checks every regular file against its Git blob identity, rejects mixed revisions, missing/extra files and symlinks, compares the five schema files with trusted local copies, and validates exact versions, navigation and all assessment relationships using the consumer-side validators. Snapshot code is never executed; the authoring matrix and learning-path parsing are not required. The lock is outside the snapshot. A candidate must pass before selecting its pin; rollback means selecting and validating the prior approved pin. Synthetic update/rollback fixtures do not publish any revision. Trust in the local Git object database and trusted consumer code is assumed; this is not signature verification or a sandbox against concurrent filesystem mutation. Full Git history is obtained once by the Linux CI checkout; no visitor API requests, new dependencies, browser execution or site deployment. AC-08 remains open until 08E.

## Consolidated acceptance (Sprint 08E)

The consolidated acceptance suite checks authoring inventory against the original 08C pin and a temporary pin of the approved 08D revision. All manifest references and canonical record bytes must agree. Real local Git commits with invalid data must fail semantic acceptance even when byte identity passes. The external test lock remains unchanged; no production release, browser runtime or site. AC-08 closure is recorded after the final gates; Sprint 09 handles final QA and revision handoff. [Acceptance tests](../tests/test_curriculum_acceptance.py).
