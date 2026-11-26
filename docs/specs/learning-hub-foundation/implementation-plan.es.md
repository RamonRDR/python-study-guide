# Plan de implementación

[🇺🇸 English](implementation-plan.md) · [🇧🇷 Português](implementation-plan.pt-BR.md) · [🇪🇸 Español](implementation-plan.es.md)

Estado: propuesta para revisión. Ejecutar solo tras aprobación y fusión del PR de especificación.

## Secuencia de entrega

| Sprint | Rama propuesta | Entrega / dependencia |
| --- | --- | --- |
| 00 | docs/learning-hub-specification | Auditoría, constitución, especificación, plan, tareas, criterios, contratos preliminares y ADR. |
| 01 | feat/chapter-navigation | Inventariar idiomas de capítulos/proyectos, definir navegación ordenada, validar enlaces recíprocos y entre módulos; currículo existente primero. |
| 02 | feat/getting-started | Incorporación localizada y conexión con Fundamentals; ampliar pruebas de navegación e índices. Añadir lecciones de venv local al proyecto y gestión de pip/dependencias; documentar candidatos a ampliar bibliotecas por separado de la Fase 9 completada, con revisión de requisitos previos y futuros PR independientes. Añadir sexta lección de Git básico y registrar enlaces recíprocos futuros entre guías en el registro de integración; mantener Git avanzado y automatización específica de plataformas en la guía separada. |
| 03 | docs/readme-and-badges | Actualizar tres README, rutas, roadmap y estructura; badges solo con evidencias. |
| 04 | feat/manual-programming-practices | Enseñar práctica manual y SDD/TDD; referenciar orientación existente de mantenimiento asistido por IA. Aplicar flujo pequeño de rama/PR/prueba/revisión específico de Python, sin duplicar el curso independiente de Git. |
| 05 | feat/problem-solving-live-coding | Auditar requisitos previos de todos los temas FR-05; enseñar conceptos ausentes en los tres idiomas antes de la práctica correspondiente; después pilotar reto según contrato preliminar y ampliar por concepto/dificultad con pruebas. |
| 06A1 | feat/interview-foundations | Lecciones 01–08, mapa de requisitos previos, OOP |
| 06A2 | feat/interview-python-internals | Lecciones 09–14, internals y memoria |
| 06A3 | feat/interview-backend-and-databases | Lecciones 15–21, backend, SQL, ingeniería; control T06-01 |
| 06B | feat/technical-interview-pilot | Lección 22, nueve preguntas piloto y validación |
| 06C | feat/technical-interview-question-bank | 48 preguntas técnicas adicionales |
| 06D | feat/mock-and-international-interviews | Lecciones 23–24, tres preguntas conductuales/internacionales y tres simulaciones; AC-06 |
| 07A | feat/assessment-contract | Contratos versionados, matriz, validadores y pruebas; sincronizar cierre de Sprint 06. |
| 07B | feat/assessment-pilot | Diez quizzes y tres ejercicios existentes, con evidencia de requisitos previos. |
| 07C1 | feat/quiz-bank-foundations | Completar 78 quizzes de fundamentos. |
| 07C2 | feat/quiz-bank-advanced | Completar banco de 160 quizzes. |
| 07D | feat/exercise-contract-migration | Migrar los 27 ejercicios restantes. |
| 07E | feat/assessment-bank-acceptance | Verificación consolidada de AC-07 y cierre. |
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

Tras aprobar CI y Codex Review el head exacto, completa Final Pre-Merge Audit definida en AGENTS.md y registra evidencia en PR. Cualquier cambio de head invalida controles y auditoría; repite antes de aprobación del mantenedor.

[Registro de integración de guías relacionadas](related-guides.es.md)

Las herramientas de evaluación usan el validador gratuito `jsonschema==4.26.0` (Draft 2020-12) en `requirements-assessment.txt` para evitar implementar JSON Schema por nuestra cuenta. Ver [contrato de evaluación](assessment-contract.es.md).
