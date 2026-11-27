# Manifiesto curricular

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

El [manifest.json](manifest.json) versionado contiene el inventario completo de Sprint 08B: 14 módulos, 107 lecciones, ocho proyectos prácticos, 345 rutas localizadas de capítulos/proyectos, 42 índices localizados de módulos, 243 recursos compartidos de capítulos y seis imágenes globales. Referencia archivos existentes y conserva IDs estables aprobados. Orden, títulos de visualización y rutas localizadas siguen las tres rutas; la matriz histórica de evaluación se usa solo para verificar el baseline de autoría. Sin duplicación de contenido.

**Relaciones completas, aceptación de revisión del consumidor pendiente:** `association_status` es `complete`. IDs de cuestionario/ejercicio identifican propiedad por chapter_id. IDs de entrevista son vínculos inversos de lecciones de prerrequisitos documentados, no propiedad; una pregunta puede aparecer en varios capítulos. Los tres simulacros están vinculados a la lección de simulacros y conservan referencias indexadas de preguntas/ejercicios. Versiones de bancos siguen 1.0.0 para cuestionario/ejercicio y 0.1.0 preliminar para entrevista/simulacro. Los 253 registros están cubiertos; sin duplicación de cuerpos. Capítulos siguen unverified excepto File Organizer (local_only con motivo); lecciones de bibliotecas externas referencian archivo de dependencias existente. Sin afirmar ejecución en navegador ni versión mínima exacta de Python.

Ejecuta comprobación estructural o la comprobación más fuerte de inventario rastreado y relaciones desde la raíz del repositorio tras instalar la dependencia de validación existente. La segunda valida todos los registros canónicos con JSON estricto, compara listas de asociaciones exactas, mantiene regresiones de inventario y requiere checkout Git. Éxito estructural solo no es aceptación integral. `python scripts/curriculum_relationships.py` emite mapa determinista de bancos existentes sin modificar archivos. Ningún comando verifica identidad inmutable de revisión del consumidor; queda en 08D, con aceptación final en 08E.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.es.md) · [Contrato de integración](../docs/specs/learning-hub-foundation/integration-contract.es.md)

```bash
python scripts/validate_curriculum.py
python scripts/validate_curriculum.py --inventory
```
