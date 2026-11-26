# Registro de tareas de Phase II

[🇺🇸 English](tasks.md) · [🇧🇷 Português](tasks.pt-BR.md) · [🇪🇸 Español](tasks.es.md)

Sprints 00–06 y 07A–C2 fusionados. D versiona los 30 ejercicios; el cierre requiere CI del head exacto, Codex Review, Final Pre-Merge Audit, aprobación del mantenedor y CI posterior.

| Tarea | Sprint | Dependencia | Estado |
| --- | --- | --- | --- |
| T00-01 Confirmar repositorio, base, ramas y CI | 00 | Ninguna | Hecho (auditoría de solo lectura) |
| T00-02 Auditar árbol y muestras de docs/scripts | 00 | T00-01 | Hecho (muestreo) |
| T00-03 Aprobar arquitectura y enfoque documental | 00 | T00-02 | Hecho (aprobación del mantenedor) |
| T00-04 Preparar SDD trilingüe y contrato preliminar | 00 | T00-03 | Hecho ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)) |
| T00-05 Verificar PR de especificación, CI y hallazgos Codex | 00 | T00-04 | Hecho ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)) |
| T00-06 Obtener aprobación y fusión | 00 | T00-05 | Hecho ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)) |
| T01-01 Inventariar e implementar navegación por idioma y pruebas | 01 | T00-06 | Hecho ([PR #88](https://github.com/RamonRDR/python-study-guide/pull/88)) |
| T02-01 Crear seis lecciones Getting Started, incluidos entornos por proyecto, gestión de dependencias y Git básico; conectar Fundamentals y mapear referencias futuras entre guías | 02 | T01-01 | Hecho ([PR #89](https://github.com/RamonRDR/python-study-guide/pull/89)) |
| T03-01 Alinear README, roadmap, ruta, estructura y badges | 03 | T02-01 | Hecho ([PR #90](https://github.com/RamonRDR/python-study-guide/pull/90)) |
| T04-01 Añadir práctica manual e ingeniería | 04 | T03-01 | Completado ([PR #91](https://github.com/RamonRDR/python-study-guide/pull/91)) |
| T05-00 Mapear todos los requisitos previos FR-05 a las lecciones existentes y enseñar conceptos ausentes en EN/PT-BR/ES antes de publicar retos | 05 | T04-01 | Completado ([PR #92](https://github.com/RamonRDR/python-study-guide/pull/92); [mapa](prerequisite-map.es.md)) |
| T05-01 Pilotar retos y pruebas de corrección | 05 | T05-00 | Completado ([PR #93](https://github.com/RamonRDR/python-study-guide/pull/93)) |
| T05-02 Ampliar retos por tema/dificultad | 05 | T05-01 | Hecho ([PR #94](https://github.com/RamonRDR/python-study-guide/pull/94), [PR #95](https://github.com/RamonRDR/python-study-guide/pull/95), `21c00c32b91a0116c8a50e89687b91f8efa04cb5`, [CI](https://github.com/RamonRDR/python-study-guide/actions/runs/45720384626)) |
| T06-01 Mapear carencias restantes específicas de entrevistas y enseñar conceptos necesarios no cubiertos en Sprint 05 | 06 | T05-02 | Completado: lecciones 01–21 fusionadas en #98; CI posterior aprobado ([#98](https://github.com/RamonRDR/python-study-guide/pull/98), [CI](https://github.com/RamonRDR/python-study-guide/actions/runs/45730226049)) |
| T06-02 Crear preguntas y simulaciones/rúbricas | 06 | T06-01 | Completado: 60 preguntas y tres simulaciones; [PR #101](https://github.com/RamonRDR/python-study-guide/pull/101), [CI posterior](https://github.com/RamonRDR/python-study-guide/actions/runs/45829816717) |
| T07-01 Finalizar y validar esquemas/registros de cuestionario/ejercicio | 07 | T06-02 | En curso: A y B fusionados ([PR #102](https://github.com/RamonRDR/python-study-guide/pull/102), [PR #103](https://github.com/RamonRDR/python-study-guide/pull/103)); C1 fusionado ([PR #104](https://github.com/RamonRDR/python-study-guide/pull/104)); C2 fusionado ([PR #105](https://github.com/RamonRDR/python-study-guide/pull/105)); D migra los 30 ejercicios; E pendiente |
| T08-01 Finalizar manifiesto y fixtures de integración | 08 | T07-01 | Pendiente |
| T09-01 Ejecutar QA y registrar evidencias reales | 09 | T08-01 | Pendiente |
| T09-02 Obtener revisión final y publicar handoff con revisión fijada | 09 | T09-01 | Pendiente |

Actualizar estados con enlaces de evidencia en PR enfocados posteriores. Hecho significa criterios satisfechos; completar sprint requiere revisión y aprobación. No inferir finalización a partir de este plan.
