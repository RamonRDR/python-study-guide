# Pruebas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

Este directorio contiene pruebas de regresión de las herramientas de calidad del repositorio, incluido el contrato de evaluación. Instala `requirements-assessment.txt` en un entorno virtual antes de ejecutar la suite. GitHub Actions la ejecuta con:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Las pruebas protegen el procesamiento de enlaces Markdown y la validación de estructura, incluidos metadatos de recursos visuales, accesibilidad SVG y referencias locales seguras.

La documentación histórica preveía contenido educativo de pruebas, empezando por aserciones simples y después introduciendo `pytest` para ejemplos ejecutables y proyectos prácticos.

Las pruebas de regresión de navegación exigen el mismo orden de la ruta principal en los tres idiomas, enlaces exactos anterior/índice/siguiente al inicio y al final, transiciones entre módulos y cobertura de los README versionados de capítulos/proyectos. Ejecuta `python scripts/check_chapter_navigation.py` desde la raíz del repositorio para comprobar todo el currículo.

Las pruebas de fundamentos exigen asignación aprobada por lección/dificultad, cobertura exacta del índice y calificación determinista; ejecutan fixtures literales confiables, nunca código arbitrario cargado de los registros. Las regresiones del piloto siguen cubiertas.

La suite de expansión comprueba la matriz completa de 160 preguntas, 2.850 XP, 82 nuevos fixtures de respuestas, fixtures literales de código confiables, diversidad de tipos y los tres índices localizados. Las regresiones de fundamentos y piloto siguen activas; no se ejecuta código del alumno.

La suite de migración comprueba el índice completo de 30 registros, los 192 casos existentes, flags explícitos sin alias, enteros grandes exactos, modalidades, metadatos de tiempo y referencias/candidatos incorrectos confiables. El índice histórico de 29 entradas y su suite de regresión siguen intactos. El runtime del navegador y la aplicación de timeout no se prueban aquí.

Las pruebas consolidadas AC-07 verifican conjuntamente ambos índices canónicos, 190 IDs únicos, 160 fixtures independientes de respuestas correctas/incorrectas de cuestionario, inventario de código Python compartido y rechazo de registros inválidos en ambos cargadores. Las suites anteriores de discriminación de ejercicios confiables, fixtures y regresión permanecen activas. Consulta [evidencias AC-07](../docs/specs/learning-hub-foundation/acceptance-criteria.es.md).

Sprint 08A añade [test_curriculum_manifest.py](test_curriculum_manifest.py). Aceptación de Sprint 08A: esquema Draft 2020-12 y validación estructural/de rutas estricta con fixtures sintéticas positivas y negativas, incluidas versiones independientes de bancos, rutas localizadas, metadatos de ejecución y JSON inválido. Inventario y navegación (B), relaciones de bancos (C), consumidor fijado (D) y aceptación consolidada (E) siguen pendientes. El validador estructural por sí solo no certifica un snapshot publicado. CI y review en el head exacto son obligatorios; no se afirma un nuevo resultado de pruebas aquí.

Sprint 08B añade [test_curriculum_inventory.py](test_curriculum_inventory.py). Las pruebas comprueban inventario rastreado completo, IDs históricos, orden, navegación, títulos localizados, assets, recursos, metadatos de dependencias y rechazo de violaciones de asociaciones pendientes. CI también ejecuta CLI de inventario de autoría. No se afirma prueba de revisión del consumidor ni ejecución en navegador.

Sprint 08C añade [test_curriculum_relationships.py](test_curriculum_relationships.py). Pruebas exigen asociaciones canónicas completas, JSON estricto y versiones exactas; casos negativos cubren vínculos ausentes, duplicados, desplazados e inventados y orden de simulacros. Inventario pendiente permanece fixture histórica; gate de inventario publicado exige relaciones completas. Sin prueba de revisión del consumidor o runtime del navegador.

Sprint 08D añade [test_curriculum_consumer.py](test_curriculum_consumer.py). Ejecuta en checkout con historial completo: lock externo fija 08C; pruebas verifican identidad de bytes, snapshots pendientes o incompatibles, JSON estricto del lock, archivos ausentes/extras/mezclados, rutas no regulares, esquemas confiables, navegación independiente y actualización/rollback local sintéticos. Sin ejecutar código del snapshot, prueba de navegador ni release.

Sprint 08E añade [test_curriculum_acceptance.py](test_curriculum_acceptance.py). Equivalencia consolidada de autoría/dos pins, recuentos exactos y límite de enteros, y rechazo semántico de seis commits Git inválidos con identidad correspondiente. Usa repositorios temporales locales, historial completo y dependencia de validación existente; sin ejecutar código de alumnos ni validadores del snapshot. Regresiones anteriores quedan intactas.
