# Estrutura do Projeto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento descreve a estrutura atualmente versionada no repositório. Diretórios planejados não são apresentados como se já existissem.

## Mapa atual do repositório

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
│   └── 03-requests/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── get_with_query.py
│           ├── http_error_handling.py
│           ├── post_json.py
│           ├── session_defaults.py
│           └── stream_download.py
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

## Guia dos arquivos da raiz

- `AGENTS.md`: instruções gerais do repositório para colaboradores e agentes de IA.
- `AUTHORS.md`: registro canônico de autoria, manutenção e crédito das contribuições.
- `CODE_OF_CONDUCT.md`: política de conduta da comunidade e relatos privados reconhecida pelo GitHub.
- `CONTRIBUTING.md`: fluxo de contribuição e critérios de qualidade.
- `LICENSE`: Licença MIT aplicada ao repositório.
- `README.md`: porta de entrada canônica em inglês.
- `SECURITY.md`: escopo de segurança e política de relato privado de vulnerabilidades.
- `SUPPORT.md`: orientação sobre canais e limites do suporte.

## Guia de diretórios

- `.github/`: configuração de colaboração, formulários de issue, template de pull request e workflow do GitHub Actions.
- `assets/`: identidade visual original, arquivos exportados, composições editáveis, paleta, acessibilidade e regras de uso.
- `comments-and-documentation/`: trilha completa da Fase 6. Há capítulos revisados sobre comentários, docstrings, nomes significativos, marcadores de tarefas, comentários versus logging e PEP 8 e legibilidade, cada um em inglês, português brasileiro e espanhol, com exemplos executáveis seguros.
- `collections/`: trilha completa da Fase 3. Seus seis capítulos ensinam criação, leitura, mutação e métodos comuns de listas, cópia rasa, tuplas e imutabilidade, mapeamentos chave-valor e views de dicionários, unicidade e relações de conjuntos e como escolher entre listas, tuplas, dicionários e conjuntos de acordo com a intenção, em inglês, português brasileiro e espanhol, com exemplos executáveis seguros.
- `docs/`: trilhas completas de estudos, roadmaps, arquitetura do projeto, documentos localizados, políticas e guia de desenvolvimento responsável assistido por IA.
- `errors-files-and-modules/`: trilha completa da Fase 7. Os Capítulos 01–05 cobrem tratamento de exceções em runtime, levantamento deliberado e exceções personalizadas, I/O seguro de arquivos de texto com `open()` e `with`, parsing e escrita de TXT/CSV/JSON e organização do código por imports, módulos, pacotes regulares, contexto de execução e design de dependências, em inglês, português brasileiro e espanhol com exemplos executáveis determinísticos.
- `exercises/`: atividades práticas relacionadas aos capítulos.
- `external-libraries/`: trilha da Fase 9 para pacotes de terceiros. Atualmente contém capítulos multilíngues revisados de pandas 3.0.x, openpyxl 3.1.x e Requests 2.34.x com quinze exemplos executáveis determinísticos no total; `pytest` é o próximo planejado.
- `functions/`: trilha completa da Fase 5. Os Capítulos 01–09 cobrem definição e chamada de funções, entradas obrigatórias, valores retornados, escopo e busca de nomes, type hints para interfaces de funções, valores padrão incluindo avaliação no momento da definição e segurança com padrões mutáveis, coleta de argumentos posicionais e nomeados de quantidade variável com `*args` e `**kwargs`, composição por funções auxiliares e coordenadoras com dependências explícitas e grafos simples de chamadas e rastreamento explícito do fluxo de dados entre chamadas, incluindo vínculos de parâmetros, reatribuição versus mutação, `None`, resultados em tupla e passagens por `return`, em inglês, português brasileiro e espanhol com exemplos executáveis determinísticos.
- `fundamentals/`: trilha completa da Fase 1. Seus seis capítulos ensinam como o Python executa um programa, como usar `print()` e `input()`, como funcionam atribuição e nomes, como reconhecer e inspecionar tipos de dados embutidos comuns e como converter valores compatíveis de forma deliberada, com explicações multilíngues alinhadas e exemplos executáveis.
- `practical-projects/`: futuros projetos pequenos combinando diversos conceitos.
- `program-flow/`: trilha completa da Fase 4. Os Capítulos 01–08 ensinam condições, comparações, teste de valor de verdade, pertencimento, identidade, lógica booleana, ramificação condicional com `if`, `elif` e `else`, correspondência de padrões estruturais, repetição guiada por iteráveis com `for`, progressões numéricas com `range()`, iteração com posição usando `enumerate()`, iteração paralela com `zip()` incluindo validação explícita de comprimentos iguais com `strict=True`, repetição guiada por estado com `while`, controle deliberado de loops com `break`, `continue` e `else` de loop e como escolher e combinar ferramentas de fluxo do programa de acordo com a intenção, em inglês, português brasileiro e espanhol, com exemplos executáveis determinísticos.
- `scripts/`: ferramentas de manutenção sem dependências externas, utilizadas localmente e pelo GitHub Actions.
- `standard-library/`: trilha completa da Fase 8. Os Capítulos 01–09 cobrem fronteiras de filesystem com `pathlib`, modelagem de data/hora com `datetime`, contratos avançados de `json` e `csv`, `logging`, `collections` especializadas, `itertools`, `decimal` e contratos de `os`/`shutil` para estado do ambiente, travessia, metadados, cópia, movimentação, remoção recursiva, capacidades de plataforma e segurança de archives, em inglês, português do Brasil e espanhol com exemplos executáveis determinísticos.
- `strings-and-numbers/`: trilha completa da Fase 2. Seus quatro capítulos revisados cobrem criação e indexação de strings, métodos comuns, comportamento de inteiros, ponto flutuante e booleanos, precisão de ponto flutuante e `round()`, `abs()`, `min()`, `max()` e `sum()` em inglês, português brasileiro e espanhol, com exemplos executáveis seguros.
- `tests/`: testes de regressão das ferramentas de qualidade e, futuramente, do conteúdo educacional.

## Regra dos diretórios de capítulos

Cada capítulo de aprendizagem contém:

- `README.md` canônico em inglês;
- READMEs localizados em português brasileiro e espanhol;
- diretório `examples/` quando exemplos executáveis melhoram o tema;
- somente material completo e revisável, sem placeholders vazios.

## Convenções de nomes e idiomas

Diretórios, arquivos, variáveis, funções, classes e demais identificadores usam inglês. Os documentos explicativos são oferecidos em inglês, português brasileiro e espanhol.

O inglês utiliza arquivos canônicos reconhecidos automaticamente pelo GitHub. As versões em português brasileiro e espanhol dos documentos principais ficam em `docs/localized/`. Os capítulos mantêm os READMEs localizados junto da versão em inglês para navegação direta.

## Regra de manutenção

Um pull request que mover, criar ou remover caminhos importantes deve atualizar esta estrutura na mesma alteração. Novos exemplos executáveis também devem ser revisados para execução automática e registrados em `scripts/example_manifest.txt` quando aprovados para o CI.
