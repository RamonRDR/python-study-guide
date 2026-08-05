<div align="center">

# Comentários, documentação e legibilidade

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta seção ensina como tornar o código Python mais fácil de entender, explicar, manter e observar. A sequência começa com comentários e avança por docstrings, nomes, marcadores de tarefas, decisões sobre logging e legibilidade segundo a PEP 8.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. Comentários](01-comments/README.pt-BR.md) | Explicar decisões e contextos não evidentes sem narrar o código | Iniciante | Disponível |
| [02. Docstrings](02-docstrings/README.pt-BR.md) | Documentar módulos, funções, classes e métodos | Iniciante | Disponível |
| 03. Nomes significativos | Fazer o código expressar intenção por meio de nomes claros e pequenas abstrações | Iniciante | Planejado |
| 04. Marcadores de tarefas | Utilizar `TODO`, `FIXME`, `NOTE` e convenções relacionadas com responsabilidade | Iniciante a intermediário | Planejado |
| 05. Comentários versus logging | Separar explicações no código-fonte da observação durante a execução | Intermediário | Planejado |
| 06. PEP 8 e legibilidade | Aplicar orientações de estilo compreendendo seus objetivos e limites | Iniciante a intermediário | Planejado |

## Orientação sobre pré-requisitos

- **01. Comentários:** não possui pré-requisito formal. Familiaridade básica com variáveis e condicionais ajuda, mas não é obrigatória.
- **02. Docstrings:** recomenda-se familiaridade básica com funções. Os exemplos de módulos, classes e métodos também podem ser compreendidos conceitualmente antes que esses temas sejam estudados em profundidade.
- **03. Nomes significativos:** conhecimentos básicos sobre variáveis e funções são recomendados.
- **04. Marcadores de tarefas:** recomenda-se concluir o capítulo de comentários. Familiaridade com issues e controle de versão ajuda.
- **05. Comentários versus logging:** recomenda-se concluir o capítulo de comentários. Conhecimentos básicos sobre execução de programas e exceções serão úteis.
- **06. PEP 8 e legibilidade:** recomenda-se conhecer a sintaxe básica do Python e concluir os capítulos de comentários e nomes significativos.

Os pré-requisitos planejados poderão ser refinados quando cada capítulo for escrito. O tempo estimado de estudo será publicado somente depois que o capítulo possuir conteúdo completo e revisável.

## Sequência recomendada

Estude os capítulos em ordem numérica. Depois de compreender seus pré-requisitos, cada capítulo também poderá ser consultado de maneira independente.

```text
01. Comentários
        ↓
02. Docstrings
        ↓
03. Nomes significativos
        ↓
04. Marcadores de tarefas
        ↓
05. Comentários versus logging
        ↓
06. PEP 8 e legibilidade
```

## Objetivos da seção

Ao concluir esta trilha, você deverá ser capaz de:

- diferenciar comentários, docstrings, documentação, type hints e logs;
- explicar decisões sem repetir código evidente;
- escolher nomes que revelem intenção, unidades, estado e responsabilidade;
- registrar tarefas técnicas com contexto suficiente para continuarem úteis;
- decidir quando informações de execução pertencem ao logging;
- aplicar recomendações da PEP 8 com discernimento, sem tratá-las como sintaxe do Python;
- revisar código considerando clareza, exatidão, privacidade e facilidade de manutenção.

## Capítulo atual

Depois de estudar [Comentários em Python](01-comments/README.pt-BR.md), continue com [Docstrings em Python](02-docstrings/README.pt-BR.md). Os dois capítulos incluem explicações multilíngues, exemplos executáveis, exercício e resumo para consulta rápida.

## Estrutura do diretório

```text
comments-and-documentation/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-comments/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── business_rule_comments.py
│       ├── unnecessary_comments.py
│       └── useful_comments.py
└── 02-docstrings/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── class_docstrings.py
        ├── function_docstrings.py
        └── inspect_docstrings.py
```

Os diretórios dos próximos capítulos serão adicionados quando seus conteúdos completos forem preparados. Evitamos placeholders vazios para que todo diretório de capítulo versionado contenha material útil.
