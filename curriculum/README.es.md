# Manifiesto curricular

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

El [manifest.json](manifest.json) versionado contiene el inventario completo de Sprint 08B: 14 módulos, 107 lecciones, ocho proyectos prácticos, 345 rutas localizadas de capítulos/proyectos, 42 índices localizados de módulos, 243 recursos compartidos de capítulos y seis imágenes globales. Referencia archivos existentes y conserva IDs estables aprobados. Orden, títulos de visualización y rutas localizadas siguen las tres rutas; la matriz histórica de evaluación se usa solo para verificar el baseline de autoría. Sin duplicación de contenido.

**Solo snapshot de desarrollo:** association_status es pending; todas las listas de referencias de cuestionario/ejercicio/entrevista/simulacro están vacías hasta 08C. Consumidores no deben importarlo como snapshot completo aprobado. Capítulos son unverified excepto File Organizer (local_only con motivo); lecciones de bibliotecas externas referencian el archivo compartido de dependencias existente. No se afirma ejecución en navegador ni versión mínima exacta de Python.

Ejecuta la comprobación estructural o la comprobación más fuerte del inventario rastreado abajo desde la raíz del repositorio, tras instalar la dependencia existente de validación de evaluaciones. La segunda compara el manifiesto con rutas fuente, IDs estables del baseline, recursos rastreados, assets y navegación global. Requiere checkout Git. Ningún comando verifica integridad de revisión del consumidor ni asociaciones completas de evaluaciones.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.es.md) · [Contrato de integración](../docs/specs/learning-hub-foundation/integration-contract.es.md)

```bash
python scripts/validate_curriculum.py
python scripts/validate_curriculum.py --inventory
```
