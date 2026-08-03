# Estrutura do Projeto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento descreve a estrutura atualmente versionada no repositório. Diretórios planejados não são apresentados como se já existissem.

## Mapa atual do repositório

```text
python-study-guide/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.yml
│   │   ├── config.yml
│   │   ├── content-suggestion.yml
│   │   └── translation-improvement.yml
│   └── pull_request_template.md
├── .gitignore
├── AGENTS.md
├── AUTHORS.md
├── AUTHORS.pt-BR.md
├── AUTHORS.es.md
├── CONTRIBUTING.md
├── CONTRIBUTING.pt-BR.md
├── CONTRIBUTING.es.md
├── LICENSE
├── README.md
├── README.pt-BR.md
├── README.es.md
├── assets/
│   └── README.md
├── comments-and-documentation/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── 01-comments/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── business_rule_comments.py
│           ├── unnecessary_comments.py
│           └── useful_comments.py
├── docs/
│   ├── ai-assisted-development/
│   │   ├── README.en.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── project-structure.en.md
│   ├── project-structure.pt-BR.md
│   ├── project-structure.es.md
│   ├── roadmap.en.md
│   ├── roadmap.pt-BR.md
│   └── roadmap.es.md
├── exercises/
│   └── README.md
├── external-libraries/
│   └── README.md
├── functions/
│   └── README.md
├── fundamentals/
│   └── README.md
├── practical-projects/
│   └── README.md
├── standard-library/
│   └── README.md
└── tests/
    └── README.md
```

## Guia dos arquivos da raiz

- `.gitignore`: impede que artefatos locais do Python e outros arquivos gerados sejam versionados.
- `AGENTS.md`: reúne instruções gerais do repositório para colaboradores e agentes de IA.
- `AUTHORS...`: registra, nos três idiomas, a autoria, a manutenção e o crédito das contribuições.
- `CONTRIBUTING...`: descreve o fluxo de contribuição e os critérios de qualidade nos três idiomas.
- `LICENSE`: contém a Licença MIT aplicada ao repositório.
- `README...`: funciona como porta de entrada multilíngue do projeto.

## Guia de diretórios

- `.github/`: configuração de colaboração do GitHub. O template de pull request solicita escopo, validação, alinhamento entre idiomas, declaração de assistência por IA, verificações de privacidade e observações para revisão. Os formulários de issue separam relatos de erros, sugestões de conteúdo e melhorias de tradução, enquanto `config.yml` desativa issues em branco sem estrutura para colaboradores e direciona ao guia de contribuição.
- `assets/`: política e futuro local de logos, banners, diagramas, capturas de tela e imagens de apresentação originais.
- `comments-and-documentation/`: trilha sobre comentários, docstrings, nomes, marcadores de tarefas, decisões de logging, PEP 8 e código legível. O primeiro capítulo está disponível em `01-comments/`.
- `docs/`: roadmaps, arquitetura do projeto, políticas e documentos multilíngues de referência. O diretório `ai-assisted-development/` explica o uso responsável de ChatGPT e Codex no fluxo do projeto.
- `exercises/`: futuras atividades práticas relacionadas aos capítulos.
- `external-libraries/`: futuros guias sobre pacotes de terceiros instalados separadamente.
- `functions/`: futura trilha sobre criação de funções, parâmetros, argumentos, retornos, escopo, type hints e colaboração entre funções.
- `fundamentals/`: futura trilha sobre variáveis, tipos de dados, entrada, saída, strings, números, coleções e controle de fluxo.
- `practical-projects/`: futuros projetos pequenos que combinarão vários conceitos.
- `standard-library/`: futuros guias sobre módulos distribuídos com o Python.
- `tests/`: testes automatizados dos exemplos executáveis e projetos à medida que forem adicionados.

## Convenções de nomes e idiomas

Os diretórios, nomes de arquivos, variáveis, funções, classes e demais identificadores do código usam inglês. Os documentos explicativos são oferecidos em inglês, português brasileiro e espanhol.

O inglês é representado pelo `README.md` padrão quando o documento é uma porta de entrada principal do GitHub. Documentos dentro de `docs/` podem utilizar os sufixos explícitos `.en.md`, `.pt-BR.md` e `.es.md`.

Os templates de colaboração do GitHub utilizam inglês como idioma padrão do repositório e permitem explicitamente que os envios sejam escritos em inglês, português brasileiro ou espanhol.

## Regra de manutenção

Um pull request que mover, criar ou remover caminhos importantes deverá atualizar esta estrutura na mesma alteração. Diretórios de capítulos planejados deverão ser adicionados somente quando contiverem material útil, e não como placeholders vazios.
