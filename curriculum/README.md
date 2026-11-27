# Curriculum manifest

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

This directory is reserved for manifest.json. No published manifest exists in Sprint 08A.

Sprint 08A acceptance: a Draft 2020-12 schema and strict structural/path validation with synthetic positive and negative fixtures, including independent bank versions, localized paths, execution metadata and invalid JSON. Inventory and navigation (B), bank relationships (C), pinned consumer (D) and consolidated acceptance (E) remain pending. The structural validator alone does not certify a published snapshot. Exact-head CI and review are required; no new test result is asserted here.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.md) · [Integration contract](../docs/specs/learning-hub-foundation/integration-contract.md)

Run structural checks on an existing snapshot (not full consumer validation):

```bash
python scripts/validate_curriculum.py --root . --manifest curriculum/manifest.json
```

The command requires the manifest introduced in B. A uses synthetic unit fixtures and the existing quality workflow.
