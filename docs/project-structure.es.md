# Estructura del Proyecto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento describe la estructura actualmente versionada en el repositorio. Los directorios planificados no se muestran como si ya existieran.

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
├── errors-files-and-modules/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-try-except-else-finally/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── parse_integer.py
│   │       ├── safe_divide.py
│   │       └── trace_try_else_finally.py
│   ├── 02-raise-and-custom-exceptions/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── custom_exception.py
│   │       ├── exception_chaining.py
│   │       └── validate_score.py
│   ├── 03-open-and-with/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── append_text.py
│   │       ├── handle_missing_file.py
│   │       └── write_and_read_text.py
│   ├── 04-txt-csv-and-json/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── csv_records.py
│   │       ├── handle_invalid_json.py
│   │       ├── json_document.py
│   │       └── text_records.py
│   └── 05-imports-modules-and-packages/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── grade_tools.py
│           ├── import_standard_library.py
│           ├── main_guard.py
│           ├── module_demo.py
│           ├── package_demo.py
│           └── study_tools/
│               ├── __init__.py
│               └── formatting.py
├── exercises/
├── external-libraries/
├── functions/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-defining-and-calling-functions/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── define_and_call.py
│   │       ├── execution_order.py
│   │       └── repeated_calls.py
│   ├── 02-parameters-and-arguments/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── book_details.py
│   │       ├── greet_people.py
│   │       └── score_status.py
│   ├── 03-return-values/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── calculate_total.py
│   │       ├── classify_score.py
│   │       └── find_first_even.py
│   ├── 04-scope/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── local_and_global_names.py
│   │       ├── separate_function_calls.py
│   │       └── shadowing_names.py
│   ├── 05-type-hints/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── annotated_greeting.py
│   │       ├── collection_summary.py
│   │       └── runtime_does_not_enforce.py
│   ├── 06-default-values/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── greet_with_style.py
│   │       ├── safe_list_default.py
│   │       └── shipping_quote.py
│   ├── 07-args-and-kwargs/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── calculate_average.py
│   │       ├── describe_session.py
│   │       └── display_settings.py
│   ├── 08-functions-working-together/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── build_score_report.py
│   │       ├── build_study_summary.py
│   │       └── prepare_greeting.py
│   └── 09-data-flow-between-functions/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── build_learning_report.py
│           ├── rebinding_and_mutation.py
│           └── trace_score_pipeline.py
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
│   ├── 06-while-loops-and-state-driven-repetition/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── countdown_state.py
│   │       ├── doubling_until_limit.py
│   │       └── study_target.py
│   ├── 07-break-continue-and-loop-else/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── break_search.py
│   │       ├── continue_filtering.py
│   │       └── loop_else_search.py
│   └── 08-choosing-and-combining-program-flow/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── search_with_position.py
│           ├── select_and_classify.py
│           └── state_driven_workflow.py
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-pathlib/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── discover_python_files.py
│   │       ├── inspect_paths.py
│   │       ├── path_parts.py
│   │       └── text_workspace.py
│   ├── 02-datetime/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── date_arithmetic.py
│   │       ├── duration_seconds.py
│   │       ├── parse_and_format.py
│   │       └── utc_conversion.py
│   ├── 03-json/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── decimal_decode.py
│   │       ├── deterministic_json.py
│   │       ├── reject_duplicate_keys.py
│   │       └── strict_numbers.py
│   ├── 04-csv/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── dialect_round_trip.py
│   │       ├── quote_none_escape.py
│   │       ├── sniff_delimiter.py
│   │       └── validate_dict_rows.py
│   ├── 05-logging/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── context_filter.py
│   │       ├── dict_config_routing.py
│   │       ├── queue_listener.py
│   │       └── stacklevel_helper.py
│   ├── 06-collections/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── bounded_deque.py
│   │       ├── chainmap_config.py
│   │       ├── counter_inventory.py
│   │       └── defaultdict_grouping.py
│   ├── 07-itertools/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── combinatoric_options.py
│   │       ├── groupby_runs.py
│   │       ├── lazy_pipeline.py
│   │       └── pairwise_deltas.py
│   └── 08-decimal/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── exact_amounts.py
│           ├── local_context_precision.py
│           ├── monitor_rounding.py
│           └── validate_scale.py
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
- `errors-files-and-modules/`: ruta completa de la Fase 7. Los Capítulos 01–05 cubren manejo de excepciones en runtime, lanzamiento deliberado y excepciones personalizadas, I/O seguro de archivos de texto con `open()` y `with`, parsing y escritura de TXT/CSV/JSON y organización del código mediante imports, módulos, paquetes regulares, contexto de ejecución y diseño de dependencias, en inglés, portugués de Brasil y español con ejemplos ejecutables deterministas.
- `exercises/`: actividades prácticas relacionadas con los capítulos.
- `external-libraries/`: futuras guías sobre paquetes de terceros.
- `functions/`: ruta completa de la Fase 5. Los Capítulos 01–09 cubren definición y llamada de funciones, entradas obligatorias, valores retornados, alcance y búsqueda de nombres, type hints para interfaces de funciones, valores predeterminados incluida la evaluación al definir la función y la seguridad con valores mutables, recolección de argumentos posicionales y por palabra clave de cantidad variable con `*args` y `**kwargs`, composición mediante funciones auxiliares y coordinadoras con dependencias explícitas y grafos simples de llamadas, y seguimiento explícito del flujo de datos entre llamadas, incluidos vínculos de parámetros, reasignación frente a mutación, `None`, resultados en tupla y traspasos mediante `return`, en inglés, portugués de Brasil y español, con ejemplos ejecutables determinísticos.
- `fundamentals/`: ruta completa de la Fase 1. Sus seis capítulos enseñan cómo Python ejecuta un programa, cómo usar `print()` e `input()`, cómo funcionan la asignación y los nombres, cómo reconocer e inspeccionar tipos de datos incorporados comunes y cómo convertir valores compatibles de forma deliberada, con explicaciones multilingües alineadas y ejemplos ejecutables.
- `practical-projects/`: futuros proyectos pequeños que combinarán varios conceptos.
- `program-flow/`: ruta completa de la Fase 4. Los Capítulos 01–08 enseñan condiciones, comparaciones, pruebas de valor de verdad, pertenencia, identidad, lógica booleana, ramificación condicional con `if`, `elif` y `else`, coincidencia de patrones estructurales, repetición guiada por iterables con `for`, progresiones numéricas con `range()`, iteración con posición usando `enumerate()`, iteración paralela con `zip()` incluida la validación explícita de longitudes iguales con `strict=True`, repetición guiada por estado con `while`, control deliberado de bucles con `break`, `continue` y `else` de bucle y cómo elegir y combinar herramientas de flujo del programa según la intención, en inglés, portugués de Brasil y español, con ejemplos ejecutables determinísticos.
- `scripts/`: herramientas de mantenimiento sin dependencias externas utilizadas localmente y por GitHub Actions.
- `standard-library/`: ruta de aprendizaje de la Fase 8 en progreso. Los Capítulos 01–08 cubren límites de filesystem con `pathlib`, modelado de fecha/hora con `datetime`, contratos avanzados de serialización/decodificación `json`, contratos avanzados de texto tabular con `csv`, contratos avanzados de entrega de eventos con `logging`, contratos especializados de `collections`, composición lazy de iteradores con `itertools` y contratos de representación, precisión, redondeo, cuantización, contexts, señales, traps y validación con `decimal`, en inglés, portugués brasileño y español con ejemplos ejecutables deterministas. El Capítulo 09 sobre `os` y `shutil` es el próximo planificado.
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
