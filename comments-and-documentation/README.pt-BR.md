<div align="center">

# Comentários, Documentação e Legibilidade

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta seção ensina como tornar o código Python mais fácil de entender, explicar, manter e observar. Ela é a seção educacional-piloto concluída do Python Study Guide.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. Comentários](01-comments/README.pt-BR.md) | Explicar decisões e contextos não evidentes sem narrar o código | Iniciante | Disponível |
| [02. Docstrings](02-docstrings/README.pt-BR.md) | Documentar módulos, funções, classes e métodos | Iniciante | Disponível |
| [03. Nomes significativos](03-meaningful-names/README.pt-BR.md) | Expressar intenção por nomes claros e pequenas abstrações | Iniciante | Disponível |
| [04. Marcadores de tarefas](04-task-markers/README.pt-BR.md) | Utilizar `TODO`, `FIXME`, `NOTE` e convenções relacionadas com responsabilidade | Iniciante a intermediário | Disponível |
| [05. Comentários versus logging](05-comments-vs-logging/README.pt-BR.md) | Separar explicações no código-fonte da observação durante a execução | Intermediário | Disponível |
| [06. PEP 8 e legibilidade](06-pep8-and-readability/README.pt-BR.md) | Aplicar orientações de estilo compreendendo objetivos e limites | Iniciante a intermediário | Disponível |

## Orientação sobre pré-requisitos

- **01. Comentários:** não possui pré-requisito formal. Familiaridade básica com variáveis e condicionais ajuda, mas não é obrigatória.
- **02. Docstrings:** recomenda-se familiaridade básica com funções. Os exemplos de módulos, classes e métodos também podem ser compreendidos conceitualmente antes que esses temas sejam estudados em profundidade.
- **03. Nomes significativos:** recomenda-se familiaridade básica com variáveis e funções.
- **04. Marcadores de tarefas:** recomenda-se concluir o capítulo de comentários. Familiaridade com issues e controle de versão ajuda.
- **05. Comentários versus logging:** recomenda-se concluir o capítulo de comentários. Conhecimentos básicos sobre execução de programas e exceções serão úteis.
- **06. PEP 8 e legibilidade:** recomenda-se conhecer a sintaxe básica do Python e concluir os capítulos de comentários e nomes significativos.

Estude os capítulos em ordem numérica ao seguir a trilha completa. Cada capítulo também pode ser consultado de forma independente depois que seus pré-requisitos forem compreendidos.

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
- aplicar recomendações da PEP 8 com discernimento, sem tratá-las como sintaxe;
- revisar código considerando clareza, exatidão, privacidade e facilidade de manutenção.

## Capítulo atual

Conclua a trilha com [PEP 8 e Legibilidade em Python](06-pep8-and-readability/README.pt-BR.md). Todos os capítulos incluem explicações multilíngues, exemplos executáveis, exercício, checklist e resumo para consulta rápida.

## Estrutura do diretório

```text
comments-and-documentation/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-comments/
├── 02-docstrings/
├── 03-meaningful-names/
├── 04-task-markers/
├── 05-comments-vs-logging/
└── 06-pep8-and-readability/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── imports_and_names.py
        ├── readable_layout.py
        └── refactor_for_readability.py
```
