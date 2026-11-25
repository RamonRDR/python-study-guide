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
├── scripts/
│   ├── check_chapter_navigation.py
│   ├── check_documentation_languages.py
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
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    ├── test_chapter_navigation.py
    ├── test_check_internal_links.py
    ├── test_documentation_languages.py
    ├── test_problem_solving_expansion.py
    ├── test_problem_solving_foundations.py
    ├── test_problem_solving_pilot.py
    └── test_validate_repository_structure.py
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
- `docs/adr/` and `docs/specs/`: trilingual architecture decisions, Phase II specifications, task register, acceptance criteria, integration contract and future related-guide references. The FR-05 prerequisite map is in the learning-hub-foundation directory.
- `errors-files-and-modules/`: complete Phase 7 learning path. Chapters 01–05 cover runtime exception handling, deliberate raising and custom exceptions, safe text-file I/O with `open()` and `with`, TXT/CSV/JSON parsing and writing, and code organization through imports, modules, regular packages, execution context, and dependency design, in English, Brazilian Portuguese, and Spanish with deterministic executable examples.
- `exercises/`: 30 focused exercises with localized instructions, preliminary JSON, shared starter and reference, and trusted tests. The expansion index lists 29 records; the original pilot remains separate.
- `external-libraries/`: complete Phase 9 learning path for third-party packages. It contains reviewed multilingual chapters for pandas 3.0.x, openpyxl 3.1.x, Requests 2.34.x, and pytest 9.1.x, with twenty deterministic executable examples in total. The phase covers tabular transformations, Excel workbook automation, HTTP/API clients, and automated-testing contracts; Phase 10 practical projects are also complete.
- `functions/`: complete Phase 5 learning path. Chapters 01–09 cover defining and calling functions, required inputs, returned values, scope and name lookup, type hints for function interfaces, default values including definition-time evaluation and mutable-default safety, variable-length positional and keyword argument collection with `*args` and `**kwargs`, composition through helper and coordinating functions with explicit dependencies and simple call graphs, and explicit data-flow tracing across calls including parameter bindings, rebinding versus mutation, `None`, tuple results, and return-based handoffs, in English, Brazilian Portuguese, and Spanish with deterministic executable examples.
- `getting-started/`: introductory curriculum order 00, with Python installation, editor setup, manual first-file execution, project-local virtual environments, dependency management and Git basics in all three languages. Historical Phase 0 remains Project Foundation.
- `fundamentals/`: complete Phase 1 learning path. Its six chapters teach how Python runs a program, how to use `print()` and `input()`, how assignment and naming work, how to recognize and inspect common built-in data types, and how to convert compatible values deliberately, with aligned multilingual explanations and executable examples.
- `manual-programming-practices/`: complementary four-lesson engineering module after Phase 10, with shared reading-progress implementation and tests; no new dependencies.
- `practical-projects/`: complete Phase 10 practical-project workspace. Projects 01–08 are complete, reviewed, and integrated. Project 07 adds immutable reconciliation models, exact integer-cent arithmetic, deterministic matching and ordering, duplicate rejection, explicit reconciliation statuses, validated report invariants, stable text rendering, and focused precision and safety regression tests. Project 08 closes the phase with immutable automation requests and results, a fixed `prepare → process → verify → finalize` execution plan, deterministic event logs, structured evidence, controlled failure injection, fail-fast propagation, post-processing verification, skipped-step semantics, stable rendering, and focused invariant regression tests without external integrations.
- `problem-solving-and-live-coding/`: Seven foundation lessons and nine challenge chapters provide 30 exercises (12 easy, 12 medium, six hard), including two timed attempts. Final Sprint 05 validation is pending.
- `program-flow/`: complete Phase 4 learning path. Chapters 01–08 teach conditions, comparisons, truth-value testing, membership, identity, Boolean logic, conditional branching with `if`, `elif`, and `else`, structural pattern matching, iterable-driven repetition with `for`, numeric progressions with `range()`, position-aware iteration with `enumerate()`, parallel iteration with `zip()` including explicit equal-length validation with `strict=True`, state-driven repetition with `while`, deliberate loop control with `break`, `continue`, and loop `else`, and how to choose and combine program-flow tools according to intent, in English, Brazilian Portuguese, and Spanish with deterministic executable examples.
- `scripts/`: dependency-free maintenance tools used locally and by GitHub Actions. The repository quality tools verify approved examples, internal links, language-family parity, chapter navigation and required paths. The Windows job covers File Organizer tests; the Linux job runs the complete practical-project suite.
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
