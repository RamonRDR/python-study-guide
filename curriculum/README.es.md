# Manifiesto curricular

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

Este directorio se reserva para manifest.json. No hay manifiesto publicado en Sprint 08A.

Aceptación de Sprint 08A: esquema Draft 2020-12 y validación estructural/de rutas estricta con fixtures sintéticas positivas y negativas, incluidas versiones independientes de bancos, rutas localizadas, metadatos de ejecución y JSON inválido. Inventario y navegación (B), relaciones de bancos (C), consumidor fijado (D) y aceptación consolidada (E) siguen pendientes. El validador estructural por sí solo no certifica un snapshot publicado. CI y review en el head exacto son obligatorios; no se afirma un nuevo resultado de pruebas aquí.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.es.md) · [Contrato de integración](../docs/specs/learning-hub-foundation/integration-contract.es.md)

Ejecuta comprobaciones estructurales en un snapshot existente (no validación integral del consumidor):

```bash
python scripts/validate_curriculum.py --root . --manifest curriculum/manifest.json
```

El comando requiere el manifiesto introducido en B. A usa fixtures unitarias sintéticas y el workflow de calidad existente.
