# Project Structure

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

This document describes the structure currently tracked in the repository. Planned directories are not shown as if they already existed.

## Current repository map

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
├── requirements-external.txt
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
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── 01-pandas/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── csv_pipeline.py
│           ├── dataframe_basics.py
│           ├── filter_and_assign.py
│           ├── groupby_summary.py
│           └── merge_tables.py
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
│   ├── 08-decimal/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── exact_amounts.py
│   │       ├── local_context_precision.py
│   │       ├── monitor_rounding.py
│   │       └── validate_scale.py
│   └── 09-os-shutil/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── copy_tree_and_move.py
│           ├── environment_contract.py
│           ├── scan_directory.py
│           └── walk_with_pruning.py
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

## Root file guide

- `AGENTS.md`: repository-wide instructions for contributors and AI agents.
- `AUTHORS.md`: canonical authorship, maintenance, and contribution-credit record.
- `CODE_OF_CONDUCT.md`: community behavior and private-reporting policy recognized by GitHub.
- `CONTRIBUTING.md`: contribution workflow and quality expectations.
- `LICENSE`: MIT License applied to the repository.
- `README.md`: canonical English repository entry point.
- `SECURITY.md`: security scope and private vulnerability-reporting policy.
- `SUPPORT.md`: support routing and project-support boundaries.

## Directory guide

- `.github/`: collaboration configuration, issue forms, pull request template, and GitHub Actions workflow.
- `assets/`: original visual identity, exported assets, editable compositions, palette, accessibility guidance, and usage rules.
- `comments-and-documentation/`: complete Phase 6 learning path. Reviewed chapters are available for comments, docstrings, meaningful names, task markers, comments versus logging, and PEP 8 and readability, each in English, Brazilian Portuguese, and Spanish with safe executable examples.
- `collections/`: complete Phase 3 learning path. Its six chapters teach list creation, reading, mutation, common methods, shallow copying, tuples and immutability, dictionary key-value mappings and views, set uniqueness and relationships, and how to choose among lists, tuples, dictionaries, and sets by intent, in English, Brazilian Portuguese, and Spanish with safe executable examples.
- `docs/`: master learning paths, roadmaps, project architecture, localized project documents, policies, and responsible AI-assisted development guidance.
- `errors-files-and-modules/`: complete Phase 7 learning path. Chapters 01–05 cover runtime exception handling, deliberate raising and custom exceptions, safe text-file I/O with `open()` and `with`, TXT/CSV/JSON parsing and writing, and code organization through imports, modules, regular packages, execution context, and dependency design, in English, Brazilian Portuguese, and Spanish with deterministic executable examples.
- `exercises/`: focused practice activities connected to learning chapters.
- `external-libraries/`: Phase 9 learning path for third-party packages. It currently contains the multilingual pandas 3.0.x chapter and five deterministic executable examples, with `openpyxl`, `requests`, and `pytest` planned next.
- `functions/`: complete Phase 5 learning path. Chapters 01–09 cover defining and calling functions, required inputs, returned values, scope and name lookup, type hints for function interfaces, default values including definition-time evaluation and mutable-default safety, variable-length positional and keyword argument collection with `*args` and `**kwargs`, composition through helper and coordinating functions with explicit dependencies and simple call graphs, and explicit data-flow tracing across calls including parameter bindings, rebinding versus mutation, `None`, tuple results, and return-based handoffs, in English, Brazilian Portuguese, and Spanish with deterministic executable examples.
- `fundamentals/`: complete Phase 1 learning path. Its six chapters teach how Python runs a program, how to use `print()` and `input()`, how assignment and naming work, how to recognize and inspect common built-in data types, and how to convert compatible values deliberately, with aligned multilingual explanations and executable examples.
- `practical-projects/`: future small projects combining several concepts.
- `program-flow/`: complete Phase 4 learning path. Chapters 01–08 teach conditions, comparisons, truth-value testing, membership, identity, Boolean logic, conditional branching with `if`, `elif`, and `else`, structural pattern matching, iterable-driven repetition with `for`, numeric progressions with `range()`, position-aware iteration with `enumerate()`, parallel iteration with `zip()` including explicit equal-length validation with `strict=True`, state-driven repetition with `while`, deliberate loop control with `break`, `continue`, and loop `else`, and how to choose and combine program-flow tools according to intent, in English, Brazilian Portuguese, and Spanish with deterministic executable examples.
- `scripts/`: dependency-free maintenance tools used locally and by GitHub Actions.
- `standard-library/`: complete Phase 8 learning path. Chapters 01–09 cover `pathlib` filesystem boundaries, `datetime` date/time modeling, advanced `json` and `csv` contracts, `logging`, specialized `collections`, `itertools`, `decimal`, and `os`/`shutil` contracts for environment state, traversal, metadata, copy, move, recursive removal, platform capabilities, and archive safety, in English, Brazilian Portuguese, and Spanish with deterministic executable examples.
- `strings-and-numbers/`: complete Phase 2 learning path. Its four reviewed chapters cover string creation and indexing, common string methods, integer, floating-point, and Boolean behavior, floating-point precision, and `round()`, `abs()`, `min()`, `max()`, and `sum()` in English, Brazilian Portuguese, and Spanish with safe executable examples.
- `tests/`: regression tests for repository quality tools and later educational code.

## Chapter directory rule

Each learning chapter contains:

- a canonical English `README.md`;
- Brazilian Portuguese and Spanish localized README files;
- an `examples/` directory when executable examples improve the topic;
- only complete, reviewable material rather than empty placeholders.

## Naming and language conventions

Repository directories, file names, variables, functions, classes, and other code identifiers use English. Explanatory documents are offered in English, Brazilian Portuguese, and Spanish.

English uses canonical root files recognized automatically by GitHub. Brazilian Portuguese and Spanish versions of those documents are stored in `docs/localized/`. Learning chapters keep their localized README files beside the English version for direct navigation.

## Maintenance rule

A pull request that moves, creates, or removes significant paths must update this structure in the same change. New executable examples must also be reviewed for unattended execution and registered in `scripts/example_manifest.txt` when approved for CI.
