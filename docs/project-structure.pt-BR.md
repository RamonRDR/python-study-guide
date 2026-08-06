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
├── docs/
│   ├── ai-assisted-development/
│   ├── localized/
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
├── practical-projects/
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
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
- `docs/`: roadmaps, arquitetura do projeto, documentos localizados, políticas e guia de desenvolvimento responsável assistido por IA.
- `exercises/`: atividades práticas relacionadas aos capítulos.
- `external-libraries/`: futuros guias sobre pacotes de terceiros.
- `functions/`: futura trilha sobre funções, parâmetros, retornos, escopo e type hints.
- `fundamentals/`: futura trilha sobre variáveis, tipos, entrada, saída, textos, números, coleções e controle de fluxo.
- `practical-projects/`: futuros projetos pequenos combinando diversos conceitos.
- `scripts/`: ferramentas de manutenção sem dependências externas, utilizadas localmente e pelo GitHub Actions.
- `standard-library/`: futuros guias sobre módulos distribuídos com o Python.
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
