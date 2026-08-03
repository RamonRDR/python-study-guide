<div align="center">

# Comentários, documentação e legibilidade

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta seção ensina como tornar o código Python mais fácil de entender, explicar, manter e observar. A sequência começa com comentários e avança por docstrings, nomes, marcadores de tarefas, decisões sobre logging e legibilidade segundo a PEP 8.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. Comentários](01-comments/README.pt-BR.md) | Explicar decisões e contextos não evidentes sem narrar o código | Iniciante | Disponível |
| 02. Docstrings | Documentar módulos, funções, classes e métodos | Iniciante | Planejado |
| 03. Nomes significativos | Fazer o código expressar intenção por meio de nomes claros e pequenas abstrações | Iniciante | Planejado |
| 04. Marcadores de tarefas | Utilizar `TODO`, `FIXME`, `NOTE` e convenções relacionadas com responsabilidade | Iniciante a intermediário | Planejado |
| 05. Comentários versus logging | Separar explicações no código-fonte da observação durante a execução | Intermediário | Planejado |
| 06. PEP 8 e legibilidade | Aplicar orientações de estilo compreendendo seus objetivos e limites | Iniciante a intermediário | Planejado |

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

Comece por [Comentários em Python](01-comments/README.pt-BR.md). O capítulo inclui explicações multilíngues, exemplos executáveis, exercício e resumo para consulta rápida.

## Estrutura do diretório

```text
comments-and-documentation/
├── README.md
├── README.pt-BR.md
├── README.es.md
└── 01-comments/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── business_rule_comments.py
        ├── unnecessary_comments.py
        └── useful_comments.py
```

Os diretórios dos próximos capítulos serão adicionados quando seus conteúdos completos forem preparados. Evitamos placeholders vazios para que todo diretório de capítulo versionado contenha material útil.
