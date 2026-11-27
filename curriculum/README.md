# Curriculum manifest

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

The versioned [manifest.json](manifest.json) contains the complete Sprint 08B inventory: 14 modules, 107 lessons, eight practical projects, 345 localized chapter/project paths, 42 localized module indexes, 243 shared chapter resources and six global images. It references existing files and preserves the approved stable IDs. Ordering, display titles and localized paths follow the three learning paths; the historical assessment matrix is used only for authoring baseline verification. No content is duplicated.

**Development snapshot only:** association_status is pending; all quiz/exercise/interview/mock reference arrays are empty until 08C. Consumers must not import this as an approved complete snapshot. Chapters are unverified except File Organizer (local_only with a reason); external-library lessons reference the existing shared requirements file. No browser execution or exact minimum Python version is asserted.

Run the structural check or the stronger tracked authoring inventory check below from the repository root, after installing the existing assessment validation dependency. The latter compares the manifest with the source learning paths, baseline stable IDs, tracked resources, assets and global navigation. It requires a Git checkout. Neither command verifies consumer revision integrity or completed assessment associations.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.md) · [Integration contract](../docs/specs/learning-hub-foundation/integration-contract.md)

```bash
python scripts/validate_curriculum.py
python scripts/validate_curriculum.py --inventory
```
