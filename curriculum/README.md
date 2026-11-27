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
