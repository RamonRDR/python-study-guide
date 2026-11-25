# Plan de implementación

[🇺🇸 English](implementation-plan.md) · [🇧🇷 Português](implementation-plan.pt-BR.md) · [🇪🇸 Español](implementation-plan.es.md)

Estado: propuesta para revisión. Ejecutar solo tras aprobación y fusión del PR de especificación.

## Secuencia de entrega

| Sprint | Rama propuesta | Entrega / dependencia |
| --- | --- | --- |
| 00 | docs/learning-hub-specification | Auditoría, constitución, especificación, plan, tareas, criterios, contratos preliminares y ADR. |
| 01 | feat/chapter-navigation | Inventariar idiomas de capítulos/proyectos, definir navegación ordenada, validar enlaces recíprocos y entre módulos; currículo existente primero. |
| 02 | feat/getting-started | Incorporación localizada y conexión con Fundamentals; ampliar pruebas de navegación e índices. |
| 03 | docs/readme-and-badges | Actualizar tres README, rutas, roadmap y estructura; badges solo con evidencias. |
| 04 | feat/manual-programming-practices | Enseñar práctica manual y SDD/TDD; referenciar orientación existente de mantenimiento asistido por IA. |
| 05 | feat/problem-solving-live-coding | Auditar requisitos previos de todos los temas FR-05; enseñar conceptos ausentes en los tres idiomas antes de la práctica correspondiente; después pilotar reto según contrato preliminar y ampliar por concepto/dificultad con pruebas. |
| 06 | feat/technical-interview-preparation | Auditar y enseñar requisitos previos restantes específicos de entrevistas no cubiertos en Sprint 05; después preguntas y simulaciones cronometradas; rúbricas y paridad de idiomas. |
| 07 | feat/quiz-and-exercise-bank | Materializar registros y esquemas versionados; validar IDs, traducciones, puntuación, soluciones e implementaciones incorrectas representativas. |
| 08 | feat/learning-hub-content-contract | Finalizar manifiesto, validación del consumidor, fixtures, versionado y compatibilidad. |
| 09 | docs/learning-hub-handoff | QA completo, revisión final, evidencias y handoff de revisión aprobada. |

Dividir sprints grandes en PR enfocados con sufijos descriptivos. Crear cada rama desde main actual tras fusionar dependencias. No fusionar sin aprobación. Usar squash merge según AGENTS.md.

## Estrategia de validación

Reutilizar scripts/check_internal_links.py, scripts/validate_repository_structure.py, scripts/run_examples.py, scripts/example_manifest.txt, tests/ y workflow de calidad. El manifiesto de ejemplos sigue siendo lista de ejecución autorizada, no fuente curricular. Añadir pruebas deterministas de navegación, restricciones de esquema, unicidad, referencias y corrección en el sprint correspondiente. Usar biblioteca estándar cuando baste; evaluar un validador gratuito de esquema al implementar. Mantener código inicial sintácticamente válido o fragmentos incompletos como datos para no romper compileall.

Usar jobs Linux y Windows existentes; no convertir ejemplos dependientes de SO o red en ejecución incondicional de navegador. La compatibilidad de navegador es obligación de prueba del consumidor; estados explícitos local-only y unverified.

## Integración

Usar snapshot de contenido fijado por revisión al compilar el sitio, rutas relativas normalizadas y renderizado Markdown seguro. Sin dependencia de API GitHub por estudiante. El sitio controla ciclo de vida Pyodide/worker, interfaz, progreso y límites de recursos; la guía controla contenido y pruebas deterministas. Ver [contrato](integration-contract.es.md) y [ADR](../../adr/README.es.md).

## Control de cambios

Por cada PR: consultar especificaciones, registrar alcance, revisar diffs, ejecutar controles aplicables, informar omisiones, solicitar Codex Review, resolver hallazgos, revalidar y obtener aprobación explícita. Actualizar tareas en el mismo PR cuando sea posible; historial Git evidencia fusión. Mantener roadmap educativo separado. Toda documentación pública debe tener EN, PT-BR y ES en el mismo PR; verificar estructura y revisar equivalencia humana.
