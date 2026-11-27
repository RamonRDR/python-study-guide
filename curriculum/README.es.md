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

## Fixture de consumidor fijada (Sprint 08D)

El [lock del consumidor](../tests/fixtures/learning-hub/consumer-lock.json) externo, solo para pruebas, fija el commit revisado de 08C `ffb53c7b64a602f09f9943489ec7741d72843831` y versiones exactas admitidas. No es release de producción ni autorreferencia en manifiesto. En checkout Git con ese commit disponible, ejecuta:

```bash
python scripts/curriculum_consumer.py
```

Código confiable del consumidor exporta árbol Git fijado a staging temporal aislado, comprueba cada archivo regular con identidad de blob Git, rechaza revisiones mezcladas, archivos ausentes/extras y symlinks, compara cinco esquemas con copias locales confiables y valida versiones exactas, navegación y todas las relaciones de evaluaciones mediante validadores del consumidor. Nunca ejecuta código del snapshot; matriz de autoría y parsing de rutas no son necesarios. Lock queda fuera del snapshot. Candidato debe pasar antes de seleccionar su pin; rollback significa seleccionar y validar pin aprobado anterior. Fixtures sintéticas de actualización/rollback no publican revisiones. Se supone confianza en base de objetos Git local y código confiable del consumidor; no es verificación de firma ni sandbox contra mutación concurrente del filesystem. Historial Git completo se obtiene una vez en checkout Linux de CI; sin solicitudes por visitante, nuevas dependencias, ejecución en navegador ni despliegue del sitio. AC-08 sigue abierto hasta 08E.

## Aceptación consolidada (Sprint 08E)

La suite de aceptación consolidada compara inventario de autoría con pin original 08C y pin temporal de revisión 08D aprobada. Todas las referencias del manifiesto y bytes de registros canónicos deben coincidir. Commits Git reales locales con datos inválidos deben fallar aceptación semántica incluso con identidad de bytes aprobada. Lock externo de prueba queda intacto; sin release de producción, runtime de navegador ni sitio. Cierre AC-08 se registra tras gates finales; Sprint 09 realiza QA final y handoff de revisión. [Pruebas de aceptación](../tests/test_curriculum_acceptance.py).
