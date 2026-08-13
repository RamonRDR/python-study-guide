# Estrutura do Projeto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento descreve a estrutura atualmente versionada no repositório. Diretórios planejados não são apresentados como seções educacionais concluídas.

## Mapa atual do repositório

```text
python-study-guide/
├── .github/
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
├── collections/
├── docs/
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
│   └── 03-return-values/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── calculate_total.py
│           ├── classify_score.py
│           └── find_first_even.py
├── fundamentals/
├── practical-projects/
├── program-flow/
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
├── strings-and-numbers/
└── tests/
```

As seções educacionais concluídas possuem seus próprios índices de capítulos e diretórios de exemplos. A árvore de Funções aparece detalhada porque a Fase 5 está sendo desenvolvida capítulo a capítulo.

## Guia de diretórios

- `.github/`: configuração de colaboração e GitHub Actions.
- `assets/`: identidade visual do projeto e orientações de uso.
- `comments-and-documentation/`: trilha completa da Fase 6.
- `collections/`: trilha completa da Fase 3.
- `docs/`: trilhas de estudo, roadmaps, documentação de estrutura, documentos localizados e orientações de desenvolvimento responsável.
- `exercises/`: atividades práticas focadas.
- `external-libraries/`: futuros guias de pacotes de terceiros.
- `functions/`: Fase 5 em andamento. Os Capítulos 01–03 cobrem definição e chamada de funções, parâmetros e argumentos, valores de retorno, `None`, retornos por ramificação e antecipados, resultados em tupla, `print()` versus `return` e rastreamento completo de entrada e saída.
- `fundamentals/`: trilha completa da Fase 1.
- `practical-projects/`: futuros projetos integrados.
- `program-flow/`: trilha completa da Fase 4.
- `scripts/`: ferramentas de qualidade do repositório sem dependências externas.
- `standard-library/`: futuros guias da biblioteca padrão.
- `strings-and-numbers/`: trilha completa da Fase 2.
- `tests/`: testes de regressão das ferramentas de qualidade e, futuramente, do código educacional.

## Regra dos diretórios de capítulos

Cada capítulo contém `README.md` canônico em inglês, READMEs localizados em português brasileiro e espanhol e um diretório `examples/` quando exemplos executáveis melhoram o tema.

## Convenções de nomes e idiomas

Caminhos do repositório e identificadores de código usam inglês. As explicações são oferecidas em inglês, português brasileiro e espanhol.

## Regra de manutenção

Um pull request que criar, mover ou remover caminhos importantes deve atualizar estes documentos de estrutura na mesma alteração. Exemplos aprovados para execução automática também devem ser registrados em `scripts/example_manifest.txt`.
