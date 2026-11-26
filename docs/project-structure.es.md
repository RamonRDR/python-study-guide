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
│   ├── pull_request_template.md
│   ├── pull_request_template.pt-BR.md
│   └── pull_request_template.es.md
├── .gitignore
├── AGENTS.md
├── AUTHORS.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements-assessment.txt
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
│   ├── adr/
│   ├── specs/
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
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── problem-solving/
│       ├── exercise-index.json
│       ├── expansion-index.json
│       ├── ascii-digit-counter/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── binary-insertion-index/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── binary-target-range/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── clamp-value/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── debug-negative-window/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── debug-positive-count/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── descending-insertion-sort/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── first-repeated-label/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── has-duplicate/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── inventory-reconciliation/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── label-counts/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── linear-first-index/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── literal-palindrome/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── longest-distinct-substring/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── merge-inventory/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── merge-sorted-lists/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── most-frequent-label/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── recursive-factorial/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── recursive-flatten/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── recursive-power/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── refactor-score-summary/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── refactor-shipping-fee/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── sorted-pair-multiplicity/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── sum-digits/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── timed-longest-streak/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── timed-threshold-count/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── total-short-lengths/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── unique-in-order/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       ├── unordered-pair-count/
│       │   ├── README.md
│       │   ├── README.pt-BR.md
│       │   ├── README.es.md
│       │   ├── exercise.json
│       │   ├── starter.py
│       │   ├── solution.py
│       │   └── test_solution.py
│       └── vowel-counter/
│           ├── README.md
│           ├── README.pt-BR.md
│           ├── README.es.md
│           ├── exercise.json
│           ├── starter.py
│           ├── solution.py
│           └── test_solution.py
├── external-libraries/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-pandas/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── csv_pipeline.py
│   │       ├── dataframe_basics.py
│   │       ├── filter_and_assign.py
│   │       ├── groupby_summary.py
│   │       └── merge_tables.py
│   ├── 02-openpyxl/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── load_and_iterate.py
│   │       ├── styled_report.py
│   │       ├── table_and_validation.py
│   │       ├── workbook_basics.py
│   │       └── write_only_export.py
│   ├── 03-requests/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── get_with_query.py
│   │       ├── http_error_handling.py
│   │       ├── post_json.py
│   │       ├── session_defaults.py
│   │       └── stream_download.py
│   └── 04-pytest/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── assertions_and_parametrize.py
│           ├── capture_output_and_logs.py
│           ├── exceptions_and_warnings.py
│           ├── fixtures_and_tmp_path.py
│           └── monkeypatch_environment.py
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
├── getting-started/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-install-python/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 02-configure-vscode/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 03-run-your-first-program/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── first_program.py
│   ├── 04-virtual-environments/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 05-packages-and-dependencies/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   └── 06-git-and-version-control/
│       ├── README.md
│       ├── README.pt-BR.md
│       └── README.es.md
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
├── interviews/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── interview-index.json
│   ├── questions/
│   └── mocks/
│       ├── mock-index.json
│       ├── mock.junior-30.json
│       ├── mock.mid-45.json
│       └── mock.senior-60.json
├── manual-programming-practices/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-manual-coding-and-debugging/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 02-specification-driven-development/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 03-test-driven-development/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── reading_progress.py
│   │       └── test_reading_progress.py
│   └── 04-professional-workflow/
│       ├── README.md
│       ├── README.pt-BR.md
│       └── README.es.md
├── practical-projects/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-expense-tracker/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── demo.py
│   │   ├── expense_tracker.py
│   │   └── tests/
│   │       ├── conftest.py
│   │       └── test_expense_tracker.py
│   ├── 02-grade-calculator/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── demo.py
│   │   ├── grade_calculator.py
│   │   └── tests/
│   │       ├── conftest.py
│   │       └── test_grade_calculator.py
│   ├── 03-user-registration/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── demo.py
│   │   ├── user_registration.py
│   │   └── tests/
│   │       ├── conftest.py
│   │       └── test_user_registration.py
│   ├── 04-csv-analyzer/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── csv_analyzer.py
│   │   ├── demo.py
│   │   └── tests/
│   │       ├── conftest.py
│   │       └── test_csv_analyzer.py
│   ├── 05-report-generator/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── demo.py
│   │   ├── report_generator.py
│   │   └── tests/
│   │       ├── conftest.py
│   │       └── test_report_generator.py
│   ├── 06-file-organizer/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── demo.py
│   │   ├── file_organizer.py
│   │   └── tests/
│   │       ├── conftest.py
│   │       ├── test_atomic_move.py
│   │       └── test_file_organizer.py
│   ├── 07-fictional-reconciliation-workflow/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── demo.py
│   │   ├── reconciliation.py
│   │   └── tests/
│   │       ├── conftest.py
│   │       ├── test_decimal_precision.py
│   │       ├── test_reconciliation.py
│   │       └── test_text_safety.py
│   └── 08-simulated-automation-flow/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       ├── automation_flow.py
│       ├── demo.py
│       └── tests/
│           ├── conftest.py
│           └── test_automation_flow.py
├── problem-solving-and-live-coding/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-problem-solving-fundamentals/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── study_minutes.py
│   ├── 02-constraints-and-edge-cases/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── capacity.py
│   ├── 03-algorithmic-complexity/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── operation_counts.py
│   ├── 04-recursion/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── recursive_sum.py
│   ├── 05-searching-algorithms/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── search.py
│   ├── 06-sorting-algorithms/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── sort.py
│   ├── 07-problem-solving-patterns/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── patterns.py
│   ├── 08-strings-and-numbers/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 09-collections/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 10-functions-and-recursion/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 11-searching-and-sorting/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 12-algorithms-and-complexity/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 13-debugging-challenges/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 14-refactoring-challenges/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 15-mixed-challenges/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   └── 16-timed-live-coding/
│       ├── README.md
│       ├── README.pt-BR.md
│       └── README.es.md
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
├── quizzes/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── quiz-index.json
│   └── questions/
│       ├── quiz.absolute-distance-zero.json
│       ├── quiz.acceptance-observable-evidence.json
│       ├── quiz.append-preserve-existing-file.json
│       ├── quiz.assignment-symbol.json
│       ├── quiz.authentication-not-object-authorization.json
│       ├── quiz.automation-failure-publication.json
│       ├── quiz.big-o-not-seconds.json
│       ├── quiz.binary-first-match-boundary.json
│       ├── quiz.binary-target-exclusive-end.json
│       ├── quiz.bool-int-exact-versus-compatible.json
│       ├── quiz.boolean-precedence.json
│       ├── quiz.capacity-inclusive-boundary.json
│       ├── quiz.catch-invalid-integer.json
│       ├── quiz.chain-one-level.json
│       ├── quiz.chained-comparison-boundary.json
│       ├── quiz.classmethod-subclass-factory.json
│       ├── quiz.closure-late-binding-snapshot.json
│       ├── quiz.collection-keyed-quantities.json
│       ├── quiz.collection-membership.json
│       ├── quiz.combined-classification-loop.json
│       ├── quiz.composition-replaceable-collaborator.json
│       ├── quiz.conditional-chain-one-branch.json
│       ├── quiz.context-exit-false-propagation.json
│       ├── quiz.counter-tally-purpose.json
│       ├── quiz.csv-convert-before-validation.json
│       ├── quiz.csv-quoted-comma.json
│       ├── quiz.csv-row-rejection-isolated.json
│       ├── quiz.dataframe-labeled-table.json
│       ├── quiz.decimal-exact-input-boundary.json
│       ├── quiz.decimal-float-arithmetic-error.json
│       ├── quiz.decimal-literal-type.json
│       ├── quiz.deepcopy-preserves-internal-alias.json
│       ├── quiz.default-argument-omission.json
│       ├── quiz.definition-body-delayed.json
│       ├── quiz.dictionary-fallback.json
│       ├── quiz.dictionary-membership-keys.json
│       ├── quiz.dictionary-none-versus-absent.json
│       ├── quiz.discarded-return-does-not-rebind.json
│       ├── quiz.distinct-window-monotonic.json
│       ├── quiz.division-zero-error.json
│       ├── quiz.docstring-first-statement.json
│       ├── quiz.docstring-runtime-attribute.json
│       ├── quiz.editor-replaces-interpreter.json
│       ├── quiz.empty-braces-not-set.json
│       ├── quiz.enumerate-default-start.json
│       ├── quiz.exact-type-function.json
│       ├── quiz.exhausted-generator-next.json
│       ├── quiz.expense-reject-zero.json
│       ├── quiz.extension-does-not-parse.json
│       ├── quiz.finally-propagates-unhandled.json
│       ├── quiz.flatten-shared-accumulator.json
│       ├── quiz.for-accumulator-initial-value.json
│       ├── quiz.for-item-driven.json
│       ├── quiz.function-result-pipeline.json
│       ├── quiz.gil-compound-invariant.json
│       ├── quiz.git-inspect-staged.json
│       ├── quiz.grade-weight-atomic-rejection.json
│       ├── quiz.green-ci-not-complete-proof.json
│       ├── quiz.hash-inside-string.json
│       ├── quiz.http-get-retrieval.json
│       ├── quiz.implicit-none-return.json
│       ├── quiz.import-alias-keyword.json
│       ├── quiz.import-initialization-side-effect.json
│       ├── quiz.input-digits-text.json
│       ├── quiz.insertion-stable-shift.json
│       ├── quiz.install-declared-requirements.json
│       ├── quiz.instance-initialization-role.json
│       ├── quiz.integer-text-conversion.json
│       ├── quiz.interpreter-purpose.json
│       ├── quiz.inventory-order-and-delta.json
│       ├── quiz.json-dumps-text-not-bytes.json
│       ├── quiz.left-join-zero-child-count.json
│       ├── quiz.list-add-one.json
│       ├── quiz.list-extend-not-nest.json
│       ├── quiz.list-pop-result.json
│       ├── quiz.list-slice-last-two.json
│       ├── quiz.list-stored-item-type.json
│       ├── quiz.local-before-assignment.json
│       ├── quiz.local-binding-shadow.json
│       ├── quiz.log-fallback-level.json
│       ├── quiz.logging-handler-threshold.json
│       ├── quiz.loop-else-break-versus-continue.json
│       ├── quiz.match-guard-fallthrough.json
│       ├── quiz.match-or-alternatives.json
│       ├── quiz.match-wildcard.json
│       ├── quiz.missing-required-argument.json
│       ├── quiz.mutable-default-reuse.json
│       ├── quiz.name-with-explicit-unit.json
│       ├── quiz.negative-floor-remainder.json
│       ├── quiz.negative-window-initialization.json
│       ├── quiz.none-check-preserve-zero.json
│       ├── quiz.nonempty-false-text.json
│       ├── quiz.open-returns-file.json
│       ├── quiz.openpyxl-formula-not-engine.json
│       ├── quiz.openpyxl-xlsx-format.json
│       ├── quiz.organizer-exact-name-atomic-boundary.json
│       ├── quiz.os-getcwd-process-state.json
│       ├── quiz.overlapping-threshold-order.json
│       ├── quiz.pair-duplicate-multiplicity.json
│       ├── quiz.pandas-label-selection.json
│       ├── quiz.pandas-merge-cardinality.json
│       ├── quiz.parameter-rebind-versus-mutation.json
│       ├── quiz.pep8-guidance-not-syntax.json
│       ├── quiz.positional-argument-binding.json
│       ├── quiz.positive-remainder.json
│       ├── quiz.predict-before-execution.json
│       ├── quiz.print-custom-separator.json
│       ├── quiz.print-literal.json
│       ├── quiz.pytest-collect-only.json
│       ├── quiz.python-source-module.json
│       ├── quiz.qualifying-minute-sum.json
│       ├── quiz.quoted-digits-type.json
│       ├── quiz.raise-keyword.json
│       ├── quiz.range-stop.json
│       ├── quiz.reachable-cache-retention.json
│       ├── quiz.reassignment-order.json
│       ├── quiz.reconciliation-duplicate-source.json
│       ├── quiz.recursive-sum-trace.json
│       ├── quiz.registration-canonical-uniqueness.json
│       ├── quiz.relative-path-working-directory.json
│       ├── quiz.repeated-lookup-tradeoff.json
│       ├── quiz.replace-does-not-mutate.json
│       ├── quiz.report-inclusive-boundaries.json
│       ├── quiz.requests-explicit-timeout.json
│       ├── quiz.requests-json-not-success.json
│       ├── quiz.return-keyword.json
│       ├── quiz.rolling-window-update.json
│       ├── quiz.round-ties-to-even.json
│       ├── quiz.sdd-exact-int-contract.json
│       ├── quiz.sdd-type-before-range.json
│       ├── quiz.set-directional-difference.json
│       ├── quiz.set-shared-members.json
│       ├── quiz.shallow-list-copy-nested.json
│       ├── quiz.short-circuit-operand-result.json
│       ├── quiz.singleton-tuple-comma.json
│       ├── quiz.source-file-extension.json
│       ├── quiz.split-preserves-empty-fields.json
│       ├── quiz.sql-check-null-constraint.json
│       ├── quiz.string-negative-index.json
│       ├── quiz.string-slice-exclusive-stop.json
│       ├── quiz.string-zero-index.json
│       ├── quiz.strip-surrounding-whitespace.json
│       ├── quiz.task-marker-no-runtime.json
│       ├── quiz.tdd-red-first.json
│       ├── quiz.tdd-refactor-preserve-behavior.json
│       ├── quiz.timedelta-duration.json
│       ├── quiz.traceback-diagnosis-first.json
│       ├── quiz.transaction-failed-credit-rollback.json
│       ├── quiz.true-division-integers.json
│       ├── quiz.try-else-success-only.json
│       ├── quiz.tuple-nested-mutability.json
│       ├── quiz.type-hints-runtime.json
│       ├── quiz.unclosed-print.json
│       ├── quiz.unsaved-source-edit.json
│       ├── quiz.value-error-contract.json
│       ├── quiz.variadic-collection-shapes.json
│       ├── quiz.venv-direct-executable.json
│       ├── quiz.venv-recreate.json
│       ├── quiz.while-initial-false.json
│       └── quiz.while-state-overshoot.json
├── schemas/
│   ├── exercise-index.schema.json
│   ├── exercise.schema.json
│   ├── quiz-index.schema.json
│   └── quiz.schema.json
├── scripts/
│   ├── assessment_grading.py
│   ├── assessment_records.py
│   ├── check_chapter_navigation.py
│   ├── check_documentation_languages.py
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── interview_records.py
│   ├── interview_mocks.py
│   ├── run_examples.py
│   ├── validate_assessments.py
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
├── technical-interview-preparation/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-understanding-technical-interviews/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 02-live-coding-and-take-home/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 03-python-fundamentals-review/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 04-data-structures-and-algorithms-review/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 05-classes-and-objects/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── reading_session.py
│   ├── 06-attributes-methods-and-object-behavior/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── study_group.py
│   ├── 07-inheritance-polymorphism-and-composition/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── notifications.py
│   ├── 08-encapsulation-abstraction-and-solid/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── stock.py
│   ├── 09-object-identity-references-and-copying/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── copy_plan.py
│   ├── 10-python-memory-management/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── bounded_cache.py
│   ├── 11-iterators-generators-and-comprehensions/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── eligible_rows.py
│   ├── 12-closures-and-decorators/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── call_counter.py
│   ├── 13-context-managers/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── managed_session.py
│   ├── 14-concurrency-parallelism-and-the-gil/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── safe_counter.py
│   ├── 15-exceptions-testing-and-debugging-review/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── parse_quantity.py
│   ├── 16-http-rest-and-backend-fundamentals/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── route_catalog.py
│   ├── 17-api-contracts-authentication-and-authorization/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── note_access.py
│   ├── 18-relational-databases-and-sql/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── lesson_catalog.py
│   ├── 19-joins-aggregations-and-data-relationships/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── group_progress.py
│   ├── 20-transactions-indexes-and-sql-safety/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── credit_transfer.py
│   ├── 21-software-engineering-and-technical-decisions/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── progress_report.py
│   ├── 22-technical-interview-question-bank/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── 23-behavioral-and-international-interviews/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   └── 24-mock-interviews-and-self-assessment/
│       ├── README.md
│       ├── README.pt-BR.md
│       └── README.es.md
└── tests/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    ├── assessment_expansion_fixtures.py
    ├── assessment_foundation_fixtures.py
    ├── test_assessment_contract.py
    ├── test_assessment_expansion.py
    ├── test_assessment_foundations.py
    ├── test_assessment_pilot.py
    ├── test_chapter_navigation.py
    ├── test_check_internal_links.py
    ├── test_documentation_languages.py
    ├── test_interview_oop_foundations.py
    ├── test_interview_python_internals.py
    ├── test_interview_backend_foundations.py
    ├── test_interview_records.py
    ├── test_interview_bank_distribution.py
    ├── test_interview_mocks.py
    ├── test_problem_solving_expansion.py
    ├── test_problem_solving_foundations.py
    ├── test_problem_solving_pilot.py
    └── test_validate_repository_structure.py
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
- `docs/adr/` y `docs/specs/`: decisiones de arquitectura trilingües, especificaciones de Phase II, registro de tareas, criterios de aceptación, contrato de integración y futuras referencias entre guías. El mapa de requisitos previos FR-05 está en el directorio learning-hub-foundation.
- `errors-files-and-modules/`: ruta completa de la Fase 7. Los Capítulos 01–05 cubren manejo de excepciones en runtime, lanzamiento deliberado y excepciones personalizadas, I/O seguro de archivos de texto con `open()` y `with`, parsing y escritura de TXT/CSV/JSON y organización del código mediante imports, módulos, paquetes regulares, contexto de ejecución y diseño de dependencias, en inglés, portugués de Brasil y español con ejemplos ejecutables deterministas.
- `exercises/`: 30 ejercicios con instrucciones localizadas, inicial y referencia compartidos y pruebas de confianza. Tres registros usan schema 1.0.0; 27 siguen legados. El índice de expansión mantiene 29 registros; el índice parcial versionado lista los tres ejercicios migrados.
- `quizzes/`: 160 preguntas localizadas e índice versionado. Las respuestas son públicas; ningún runtime implementado.
- `schemas/`: cuatro esquemas versionados de evaluación (Draft 2020-12).
- `external-libraries/`: ruta completa de la Fase 9 para paquetes de terceros. Contiene capítulos multilingües revisados de pandas 3.0.x, openpyxl 3.1.x, Requests 2.34.x y pytest 9.1.x, con veinte ejemplos ejecutables deterministas en total. La fase cubre transformaciones tabulares, automatización de libros de Excel, clientes HTTP/API y contratos de pruebas automatizadas; la Fase 10 de proyectos prácticos también está completada.
- `functions/`: ruta completa de la Fase 5. Los Capítulos 01–09 cubren definición y llamada de funciones, entradas obligatorias, valores retornados, alcance y búsqueda de nombres, type hints para interfaces de funciones, valores predeterminados incluida la evaluación al definir la función y la seguridad con valores mutables, recolección de argumentos posicionales y por palabra clave de cantidad variable con `*args` y `**kwargs`, composición mediante funciones auxiliares y coordinadoras con dependencias explícitas y grafos simples de llamadas, y seguimiento explícito del flujo de datos entre llamadas, incluidos vínculos de parámetros, reasignación frente a mutación, `None`, resultados en tupla y traspasos mediante `return`, en inglés, portugués de Brasil y español, con ejemplos ejecutables determinísticos.
- `getting-started/`: orden curricular introductorio 00, con instalación de Python, configuración del editor, primera ejecución manual de archivo, entornos virtuales por proyecto, gestión de dependencias y Git básico en los tres idiomas. La Fase 0 histórica sigue siendo Base del proyecto.
- `fundamentals/`: ruta completa de la Fase 1. Sus seis capítulos enseñan cómo Python ejecuta un programa, cómo usar `print()` e `input()`, cómo funcionan la asignación y los nombres, cómo reconocer e inspeccionar tipos de datos incorporados comunes y cómo convertir valores compatibles de forma deliberada, con explicaciones multilingües alineadas y ejemplos ejecutables.
- `manual-programming-practices/`: módulo complementario de ingeniería de cuatro lecciones tras la Fase 10, implementación y pruebas compartidas de progreso de lectura; sin nuevas dependencias.
- `practical-projects/`: espacio completo de Proyectos Prácticos de la Fase 10. Los Proyectos 01–08 están completados, revisados e integrados. El Proyecto 07 añade modelos inmutables de conciliación, aritmética exacta en centavos enteros, matching y orden deterministas, rechazo de duplicados, estados explícitos de conciliación, invariantes validadas del informe, renderizado de texto estable y pruebas de regresión enfocadas en precisión y seguridad. El Proyecto 08 cierra la fase con solicitudes y resultados inmutables de automatización, un plan fijo de ejecución `prepare → process → verify → finalize`, logs deterministas de eventos, evidencia estructurada, inyección controlada de fallos, propagación fail-fast, verificación posterior al procesamiento, semántica de pasos omitidos, renderizado estable y pruebas de regresión centradas en invariantes sin integraciones externas.
- `problem-solving-and-live-coding/`: Siete lecciones de fundamentos y nueve de retos ofrecen 30 ejercicios (12 fáciles, 12 medios, seis difíciles), incluidas dos prácticas cronometradas. Sprint 05 completado ([PR #95](https://github.com/RamonRDR/python-study-guide/pull/95)).
- `technical-interview-preparation/`: Todo el contenido previsto de la Fase 12 está implementado: 24 lecciones, 60 preguntas (24 Junior, 24 Mid-level, 12 Senior) y tres simulaciones de 30/45/60 minutos. Sprint 06 se completó en el [PR #101](https://github.com/RamonRDR/python-study-guide/pull/101) y su CI posterior.
- `program-flow/`: ruta completa de la Fase 4. Los Capítulos 01–08 enseñan condiciones, comparaciones, pruebas de valor de verdad, pertenencia, identidad, lógica booleana, ramificación condicional con `if`, `elif` y `else`, coincidencia de patrones estructurales, repetición guiada por iterables con `for`, progresiones numéricas con `range()`, iteración con posición usando `enumerate()`, iteración paralela con `zip()` incluida la validación explícita de longitudes iguales con `strict=True`, repetición guiada por estado con `while`, control deliberado de bucles con `break`, `continue` y `else` de bucle y cómo elegir y combinar herramientas de flujo del programa según la intención, en inglés, portugués de Brasil y español, con ejemplos ejecutables determinísticos.
- `scripts/`: herramientas de mantenimiento sin dependencias externas utilizadas localmente y por GitHub Actions. Las herramientas de calidad verifican ejemplos aprobados, enlaces internos, paridad de familias de idiomas, navegación de capítulos y rutas obligatorias. El job Windows cubre pruebas de File Organizer; el job Linux ejecuta la suite completa de proyectos prácticos.
- `standard-library/`: ruta completa de la Fase 8. Los Capítulos 01–09 cubren fronteras de filesystem con `pathlib`, modelado de fecha/hora con `datetime`, contratos avanzados de `json` y `csv`, `logging`, `collections` especializadas, `itertools`, `decimal` y contratos de `os`/`shutil` para estado del entorno, recorrido, metadatos, copia, movimiento, eliminación recursiva, capacidades de plataforma y seguridad de archives, en inglés, portugués de Brasil y español con ejemplos ejecutables deterministas.
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
