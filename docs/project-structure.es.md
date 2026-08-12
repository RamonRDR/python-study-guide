# Estructura del Proyecto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento describe la estructura actualmente versionada en el repositorio. Los directorios planificados no se presentan como si ya existieran.

## Mapa actual del repositorio

```text
python-study-guide/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   └── quality-checks.yml
│   └── pull_request_template.md
├── AGENTS.md
├── AUTHORS.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── assets/
├── comments-and-documentation/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-comments/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── business_rule_comments.py
│   │       ├── unnecessary_comments.py
│   │       └── useful_comments.py
│   ├── 02-docstrings/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── class_docstrings.py
│   │       ├── function_docstrings.py
│   │       └── inspect_docstrings.py
│   ├── 03-meaningful-names/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── booleans_and_units.py
│   │       ├── refactor_for_intent.py
│   │       └── vague_and_clear_names.py
│   ├── 04-task-markers/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── actionable_markers.py
│   │       ├── scan_markers.py
│   │       └── temporary_workaround.py
│   ├── 05-comments-vs-logging/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── application_and_library_logging.py
│   │       ├── comments_vs_logging.py
│   │       └── logging_levels.py
│   └── 06-pep8-and-readability/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── imports_and_names.py
│           ├── readable_layout.py
│           └── refactor_for_readability.py
├── collections/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-list-creation-and-indexing/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── list_basics.py
│   │       └── list_slicing.py
│   ├── 02-modifying-lists-and-methods/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── list_copying.py
│   │       ├── list_methods.py
│   │       └── list_mutation.py
│   ├── 03-tuples-and-immutability/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── tuple_basics.py
│   │       ├── tuple_mutable_item.py
│   │       └── tuple_unpacking.py
│   ├── 04-dictionaries-keys-and-values/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── dictionary_basics.py
│   │       ├── dictionary_mutation.py
│   │       └── dictionary_views.py
│   ├── 05-sets-and-unique-values/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── set_basics.py
│   │       ├── set_mutation.py
│   │       └── set_operations.py
│   └── 06-choosing-the-right-collection/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── collection_models.py
│           ├── collection_tradeoffs.py
│           └── study_workspace.py
├── docs/
│   ├── ai-assisted-development/
│   ├── localized/
│   ├── learning-path.en.md
│   ├── learning-path.pt-BR.md
│   ├── learning-path.es.md
│   ├── project-structure.en.md
│   ├── project-structure.pt-BR.md
│   ├── project-structure.es.md
│   ├── roadmap.en.md
│   ├── roadmap.pt-BR.md
│   └── roadmap.es.md
├── exercises/
├── external-libraries/
├── functions/
├── fundamentals/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-how-python-runs-a-program/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── hello_world.py
│   ├── 02-print-and-input/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── interactive_greeting.py
│   │       └── output_basics.py
│   ├── 03-variables-and-naming/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── learning_profile.py
│   │       └── variable_basics.py
│   ├── 04-built-in-data-types/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── same_looking_values.py
│   │       └── value_catalog.py
│   ├── 05-type-and-isinstance/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── check_type_families.py
│   │       └── inspect_types.py
│   └── 06-type-conversion/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── conversion_basics.py
│           └── conversion_surprises.py
├── practical-projects/
├── program-flow/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-conditions-comparisons-and-boolean-logic/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── boolean_logic.py
│   │       ├── comparison_results.py
│   │       └── truth_values.py
│   ├── 02-if-elif-and-else/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── basic_if.py
│   │       ├── if_elif_else.py
│   │       └── independent_conditions.py
│   ├── 03-match-and-case/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── literal_and_or_patterns.py
│   │       ├── mapping_patterns_and_guards.py
│   │       └── sequence_patterns.py
│   ├── 04-for-loops-and-iteration/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── collection_iteration.py
│   │       ├── dictionary_iteration.py
│   │       └── filter_and_collect.py
│   ├── 05-range-enumerate-and-zip/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── enumerate_positions.py
│   │       ├── range_progressions.py
│   │       └── zip_parallel_iteration.py
│   └── 06-while-loops-and-state-driven-repetition/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── countdown_state.py
│           ├── doubling_until_limit.py
│           └── study_target.py
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
├── strings-and-numbers/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-string-creation-and-indexing/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── fixed_position_text.py
│   │       └── string_basics.py
│   ├── 02-common-string-methods/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── normalize_text.py
│   │       └── split_and_join.py
│   ├── 03-int-float-and-bool/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── numeric_behavior.py
│   │       └── truth_and_precision.py
│   └── 04-numeric-builtins/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── numeric_summary.py
│           └── rounding_behavior.py
└── tests/
```

## Guía de los archivos raíz

- `AGENTS.md`: instrucciones generales del repositorio para colaboradores y agentes de IA.
- `AUTHORS.md`: registro canónico de autoría, mantenimiento y reconocimiento de contribuciones.
- `CODE_OF_CONDUCT.md`: política de conducta de la comunidad e informes privados reconocida por GitHub.
- `CONTRIBUTING.md`: flujo de contribución y expectativas de calidad.
- `LICENSE`: Licencia MIT aplicada al repositorio.
- `README.md`: punto de entrada canónico en inglés.
- `SECURITY.md`: alcance de seguridad y política de reporte privado de vulnerabilidades.
- `SUPPORT.md`: orientación sobre canales y límites del soporte.

## Guía de directorios

- `.github/`: configuración de colaboración, formularios de issue, plantilla de pull request y workflow de GitHub Actions.
- `assets/`: identidad visual original, recursos exportados, composiciones editables, paleta, accesibilidad y reglas de uso.
- `comments-and-documentation/`: ruta completa de la Fase 6. Hay capítulos revisados sobre comentarios, docstrings, nombres significativos, marcadores de tareas, comentarios frente a logging y PEP 8 y legibilidad, cada uno en inglés, portugués de Brasil y español, con ejemplos ejecutables seguros.
- `collections/`: ruta completa de la Fase 3. Sus seis capítulos enseñan creación, lectura, mutación y métodos comunes de listas, copia superficial, tuplas e inmutabilidad, mappings clave-valor y vistas de diccionarios, unicidad y relaciones de conjuntos y cómo elegir entre listas, tuplas, diccionarios y conjuntos según la intención, en inglés, portugués de Brasil y español, con ejemplos ejecutables seguros.
- `docs/`: rutas completas de aprendizaje, roadmaps, arquitectura del proyecto, documentos localizados, políticas y guía de desarrollo responsable asistido por IA.
- `exercises/`: actividades prácticas relacionadas con los capítulos.
- `external-libraries/`: futuras guías sobre paquetes de terceros.
- `functions/`: futura ruta sobre funciones, parámetros, retornos, alcance y type hints.
- `fundamentals/`: ruta completa de la Fase 1. Sus seis capítulos enseñan cómo Python ejecuta un programa, cómo usar `print()` e `input()`, cómo funcionan la asignación y los nombres, cómo reconocer e inspeccionar tipos de datos incorporados comunes y cómo convertir valores compatibles de forma deliberada, con explicaciones multilingües alineadas y ejemplos ejecutables.
- `practical-projects/`: futuros proyectos pequeños que combinarán varios conceptos.
- `program-flow/`: ruta de la Fase 4 en progreso. Los Capítulos 01–06 enseñan condiciones, comparaciones, pruebas de valor de verdad, pertenencia, identidad, lógica booleana, ramificación condicional con `if`, `elif` y `else`, coincidencia de patrones estructurales, iteración elemento por elemento con `for`, progresiones numéricas con `range()`, iteración con posición usando `enumerate()`, iteración paralela con `zip()` incluida la validación explícita de longitudes iguales con `strict=True`, y repetición guiada por estado con `while`, incluida la reevaluación de la condición y el razonamiento sobre la finalización, en inglés, portugués de Brasil y español, con ejemplos ejecutables determinísticos.
- `scripts/`: herramientas de mantenimiento sin dependencias externas utilizadas localmente y por GitHub Actions.
- `standard-library/`: futuras guías sobre módulos distribuidos con Python.
- `strings-and-numbers/`: ruta completa de la Fase 2. Sus cuatro capítulos revisados cubren creación e indexación de strings, métodos comunes, comportamiento de enteros, punto flotante y booleanos, precisión de punto flotante y `round()`, `abs()`, `min()`, `max()` y `sum()` en inglés, portugués de Brasil y español, con ejemplos ejecutables seguros.
- `tests/`: pruebas de regresión de las herramientas de calidad y, más adelante, del contenido educativo.

## Regla de los directorios de capítulos

Cada capítulo de aprendizaje contiene:

- un `README.md` canónico en inglés;
- READMEs localizados en portugués de Brasil y español;
- un directorio `examples/` cuando los ejemplos ejecutables mejoran el tema;
- solamente material completo y revisable, sin placeholders vacíos.

## Convenciones de nombres e idiomas

Los directorios, archivos, variables, funciones, clases y demás identificadores utilizan inglés. Los documentos explicativos se ofrecen en inglés, portugués de Brasil y español.

El inglés utiliza archivos canónicos reconocidos automáticamente por GitHub. Las versiones en portugués de Brasil y español de los documentos principales se almacenan en `docs/localized/`. Los capítulos mantienen los READMEs localizados junto a la versión en inglés para facilitar la navegación.

## Regla de mantenimiento

Un pull request que mueva, cree o elimine rutas importantes debe actualizar esta estructura en el mismo cambio. Los nuevos ejemplos ejecutables también deben revisarse para ejecución automática y registrarse en `scripts/example_manifest.txt` cuando se aprueben para CI.
