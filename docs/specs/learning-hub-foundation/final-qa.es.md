# QA final y evidencias de aceptación (09A)

[EN](final-qa.md) · [PT-BR](final-qa.pt-BR.md) · [ES](final-qa.es.md)

Evidencias de la base, no aprobación final de AC-09. El mantenedor aprobó el plan de dos PR. La fuente es el commit exacto de main posterior a la fusión; el PR de QA exige nuevo CI, Codex, auditoría final, autorización explícita de squash y CI de push. 09B validará el commit de contenido resultante mediante lock externo y completará el handoff.

## Base verificada y gobernanza

`a8a264f9f36ec276f0ad8e35f10f2d76f82fe211`

[PR #112](https://github.com/RamonRDR/python-study-guide/pull/112) · [CI #46053604048](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048) · [Linux job](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048/job/140690676913) · [Windows job](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048/job/140690677260) · [AC-08](https://github.com/RamonRDR/python-study-guide/pull/112#issuecomment-7226219176)

Main coincidía con el árbol auditado `ef3b153ceae4eb98e97c124510e7962ff5969a90`, sin PR abiertos en la consulta inicial. Ruleset 20301083 activo, checks strict, PR y resolución de hilos obligatorios, historial lineal, solo squash, protección de eliminación/non-fast-forward, sin bypass. Sin mínimo de aprobaciones humanas exigido; aprobación del mantenedor y Codex siguen siendo gates operativos. Licencia MIT, autoría y política de contribución inspeccionadas. Árbol recursivo con 1.236 blobs, sin symlinks/submodules ni nombres de archivos que coincidan con patrones comunes de claves privadas/credenciales/.env; cribado de nombres no equivale a escaneo de secretos o auditoría integral de privacidad histórica. Sin certificación de seguridad.

## Resultados de CI (suites separadas)

| Suite | Aprobados | Omitidos |
| --- | ---: | ---: |
| Quality unittest | 180 | 0 |
| Engineering unittest | 7 | 0 |
| Practical pytest (Linux) | 406 | 1 |
| File Organizer pytest (Windows) | 63 | 17 |

La misma ejecución Linux completó 210 ejemplos autorizados, 9.273 enlaces internos en 580 documentos Markdown, estructura de idiomas, 345 documentos de navegación, compileall, estructura del repositorio, inventarios de evaluación y currículo y fixture histórica de consumidor fijada. La suite Windows es subconjunto de las pruebas prácticas Linux; no sumar recuentos. Disponibilidad de URL externas y ejecución de ejemplos fuera de la lista no comprobadas.

## Trazabilidad de aceptación

| Criterio | Evidencia integrada | Verificación de base / límite residual |
| --- | --- | --- |
| AC-00 | [PR #87](https://github.com/RamonRDR/python-study-guide/pull/87) | Constitución, especificaciones, ADR y workflow presentes; fusión histórica verificada. |
| AC-01 | [PR #88](https://github.com/RamonRDR/python-study-guide/pull/88) | Validador de navegación y pruebas negativas; 345 documentos localizados. |
| AC-02 | [PR #89](https://github.com/RamonRDR/python-study-guide/pull/89) | Seis lecciones de incorporación y alcance Git/entornos establecido; instalación/descarga/red no repetidas en cada SO. |
| AC-03 | [PR #90](https://github.com/RamonRDR/python-study-guide/pull/90) | Tres README y rutas maestras inspeccionados; insignias actualizadas en 09A, controles estructurales repetidos en PR. |
| AC-04 | [PR #91](https://github.com/RamonRDR/python-study-guide/pull/91) | Orientación de práctica manual y SDD/TDD; siete pruebas de ingeniería; introducción muestreada. |
| AC-05 | [PR #95](https://github.com/RamonRDR/python-study-guide/pull/95) | Mapa de requisitos previos, pruebas de retos y migración; 30 ejercicios canónicos, pruebas de referencias confiables y soluciones incorrectas. |
| AC-06 | [PR #101](https://github.com/RamonRDR/python-study-guide/pull/101) | Mapa de requisitos previos, validadores de preguntas/simulacros; 60 preguntas y tres simulacros, autoevaluación humana. |
| AC-07 | [PR #107](https://github.com/RamonRDR/python-study-guide/pull/107) | 160 cuestionarios y 30 ejercicios cubiertos por pruebas de validación/fixtures existentes; JSON/tipos estrictos, respuestas incorrectas e implementaciones de referencia/negativas. |
| AC-08 | [PR #112](https://github.com/RamonRDR/python-study-guide/pull/112) | Manifiesto/relaciones completos; evidencias fijadas 08C y temporales 08D, snapshots Git semánticamente inválidos y fixtures de rollback. |
| AC-09 | 09A / 09B | Evidencias y docs de 09A en revisión; handoff final 09B, validación del pin candidato y gates de HEAD exacto/post-merge pendientes. |

## Inventario curricular y de evaluación

Recuento directo del manifiesto y cuatro índices: 14 módulos, 115 entradas únicas (107 lecciones + ocho proyectos), 345 rutas de contenido localizado, 42 índices de módulos localizados, 243 recursos de capítulos y seis assets globales. Cuatro bancos: 160 cuestionarios, 30 ejercicios, 60 preguntas de entrevista y tres simulacros (253 registros distintos; 268 asociaciones: 160/30/75/3). Los 75 enlaces de entrevistas son referencias de requisitos previos, no 75 preguntas. Manifiesto completo, versión 1.0.0. Cuestionario/ejercicio 1.0.0; índices entrevista/simulacro preliminares 0.1.0; lock externo de fixture 1.0.0. Cinco esquemas Draft 2020-12. Pruebas existentes aprobadas verifican dificultad de cuestionarios 64/67/29 y 2.850 XP, ejercicios 12/12/6 y 192 casos, entrevistas 24/24/12 y simulacros 30/45/60 minutos. Estos últimos valores tienen evidencia de pruebas, no recuento manual de cada registro.

Revisados campos seleccionados de registros reales `quiz.absolute-distance-zero` (abs(-11) = 11, respuesta exacta `abs`), `problem-solving.ascii-digit-counter` (dígitos ASCII literales, no dígitos Unicode arbitrarios), `interview.allowed-tools` (respeto de reglas y declaración de herramientas), `mock.junior-30` (tiempos, preguntas/ejercicio y rúbrica manual). Los textos EN/PT-BR/ES revisados están conceptualmente alineados. Sin relectura semántica exhaustiva de los 253 registros.

## Revisión dirigida de idiomas

Consultada la primera entrada curricular de cada módulo en tres idiomas (42 documentos). Comparados conceptos introductorios, encabezados y bloques Python delimitados programáticamente; todos los bloques correspondientes son idénticos en bytes entre idiomas (314 por idioma, no todos los ejemplos del repositorio). Inspección dirigida asistida por IA, no revisión semántica integral ni humana de cada página; sin certificación de traducción. Cobertura estructural de 345 documentos proviene de CI. PR enfocados previos y mapas de requisitos previos son evidencias adicionales, no sustitutos de revisión independiente.

| Directorio de entrada (README.md, README.pt-BR.md, README.es.md) | Bloques Python por idioma |
| --- | ---: |
| `getting-started/01-install-python` | 0 |
| `fundamentals/01-how-python-runs-a-program` | 9 |
| `strings-and-numbers/01-string-creation-and-indexing` | 25 |
| `collections/01-list-creation-and-indexing` | 22 |
| `program-flow/01-conditions-comparisons-and-boolean-logic` | 46 |
| `functions/01-defining-and-calling-functions` | 30 |
| `comments-and-documentation/01-comments` | 46 |
| `errors-files-and-modules/01-try-except-else-finally` | 39 |
| `standard-library/01-pathlib` | 37 |
| `external-libraries/01-pandas` | 52 |
| `practical-projects/01-expense-tracker` | 7 |
| `manual-programming-practices/01-manual-coding-and-debugging` | 1 |
| `problem-solving-and-live-coding/01-problem-solving-fundamentals` | 0 |
| `technical-interview-preparation/01-understanding-technical-interviews` | 0 |

## Límites y siguiente gate

Sin ejecución local: acceso de red del contenedor local no resolvió GitHub; evidencia de ejecución de la base es GitHub Actions real. Sin Red aislado ni nuevo comportamiento de producción; sin pruebas artificiales para aumentar recuentos. Sin revisión independiente integral de prosa, código inline, enlaces externos, credenciales en contenido/historial o instalaciones en todas las plataformas. PR anteriores revisados siguen siendo evidencia; mantenedor debe evaluar riesgo residual de revisión semántica. Solo fixture de consumidor en Linux y File Organizer en Windows ejecutados. 114 entradas y 30 ejercicios no verificados en navegador; File Organizer local_only. Cuatro lecciones externas declaran requirements-external.txt; sin versión mínima Python inventada para capítulos. Web Worker no es frontera de seguridad; runtime, timeouts, cancelación, aislamiento de salida/red/almacenamiento/credenciales y despliegue real son trabajo del consumidor. Pruebas no demuestran complejidad/refactorización o mutación transitoria; identidad Git no equivale a firma. Base Git/validador confiables y staging aislado son supuestos, no protección concurrente del filesystem. Sin rollback atómico real en producción, sitio, release/tag ni cambios de enlaces entre guías. 09B debe validar el squash real aprobado de 09A; fixture histórica 08C no es pin de producción.
