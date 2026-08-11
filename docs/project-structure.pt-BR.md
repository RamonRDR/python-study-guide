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
- `exercises/`: atividades práticas relacionadas aos capítulos.
- `external-libraries/`: futuros guias sobre pacotes de terceiros.
- `functions/`: futura trilha sobre funções, parâmetros, retornos, escopo e type hints.
- `fundamentals/`: trilha completa da Fase 1. Seus seis capítulos ensinam como o Python executa um programa, como usar `print()` e `input()`, como funcionam atribuição e nomes, como reconhecer e inspecionar tipos de dados embutidos comuns e como converter valores compatíveis de forma deliberada, com explicações multilíngues alinhadas e exemplos executáveis.
- `practical-projects/`: futuros projetos pequenos combinando diversos conceitos.
- `program-flow/`: trilha da Fase 4 em andamento. Os Capítulos 01–06 ensinam condições, comparações, teste de valor de verdade, pertencimento, identidade, lógica booleana, ramificação condicional com `if`, `elif` e `else`, correspondência de padrões estruturais, iteração item por item com `for`, progressões numéricas com `range()`, iteração com posição usando `enumerate()`, iteração paralela com `zip()` incluindo validação explícita de comprimentos iguais com `strict=True`, e repetição guiada por estado com `while`, incluindo reavaliação da condição e raciocínio sobre término, em inglês, português brasileiro e espanhol, com exemplos executáveis determinísticos.
- `scripts/`: ferramentas de manutenção sem dependências externas, utilizadas localmente e pelo GitHub Actions.
- `standard-library/`: futuros guias sobre módulos distribuídos com o Python.
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
