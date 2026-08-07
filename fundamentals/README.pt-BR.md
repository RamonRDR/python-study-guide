<div align="center">

# Fundamentos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta seção inicia a sequência principal de aprendizagem do Python Study Guide. Ela não pressupõe experiência anterior com programação e constrói o modelo mental necessário para escrever, salvar, executar, analisar e ampliar gradualmente programas Python.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. Como o Python executa um programa](01-how-python-runs-a-program/README.pt-BR.md) | Criar, executar, modificar e corrigir um primeiro arquivo Python | Iniciante absoluto | Disponível |
| [02. `print()` e `input()`](02-print-and-input/README.pt-BR.md) | Exibir informações e receber texto de uma pessoa usuária | Iniciante absoluto | Disponível |
| [03. Variáveis e nomes](03-variables-and-naming/README.pt-BR.md) | Armazenar valores e escolher identificadores compreensíveis | Iniciante | Disponível |
| [04. Tipos de dados embutidos](04-built-in-data-types/README.pt-BR.md) | Reconhecer categorias comuns de valores e sua notação no código-fonte | Iniciante | Disponível |
| [05. `type()` e `isinstance()`](05-type-and-isinstance/README.pt-BR.md) | Inspecionar tipos exatos e verificar famílias de tipos compatíveis | Iniciante | Disponível |
| [06. Conversão de tipos](06-type-conversion/README.pt-BR.md) | Converter valores compatíveis de forma deliberada | Iniciante | Disponível |

## Orientação de pré-requisitos

- **01. Como o Python executa um programa:** nenhuma experiência anterior com programação é necessária. O Python deve estar instalado, e a pessoa estudante precisa ter acesso a um editor de texto simples ou de código e a um terminal.
- **02. `print()` e `input()`:** conclua primeiro o Capítulo 01. A pessoa estudante deve conseguir criar, salvar e executar um arquivo `.py` pelo terminal.
- **03. Variáveis e nomes:** conclua primeiro o Capítulo 02. A pessoa estudante deve compreender `print()`, `input()` e por que o resultado de uma entrada precisa ser armazenado antes de ser reutilizado.
- **04. Tipos de dados embutidos:** conclua primeiro o Capítulo 03. A pessoa estudante deve compreender atribuição, reatribuição e como nomes de variáveis referenciam valores.
- **05. `type()` e `isinstance()`:** conclua primeiro o Capítulo 04. A pessoa estudante deve reconhecer valores `str`, `int`, `float`, `bool` e `None` e compreender que valores possuem tipos.
- **06. Conversão de tipos:** conclua primeiro o Capítulo 05. A pessoa estudante deve saber inspecionar valores com `type()` e `isinstance()` e reconhecer os tipos embutidos comuns apresentados anteriormente.

Estude os capítulos em ordem numérica ao seguir a trilha completa.

```text
01. Como o Python executa um programa
        ↓
02. print() e input()
        ↓
03. Variáveis e nomes
        ↓
04. Tipos de dados embutidos
        ↓
05. type() e isinstance()
        ↓
06. Conversão de tipos
```

## Objetivos da seção

Ao final desta trilha, você deverá ser capaz de:

- criar e executar arquivos de código-fonte Python;
- exibir informações e receber entradas básicas;
- armazenar valores usando nomes de variáveis significativos;
- reconhecer tipos de dados embutidos comuns;
- inspecionar valores com `type()` e `isinstance()`;
- converter valores compatíveis entre tipos básicos;
- ler saídas simples e mensagens básicas de erro.

## Capítulo atual

Continue com [Conversão de Tipos](06-type-conversion/README.pt-BR.md). O capítulo explica conversão deliberada com `int()`, `float()`, `str()` e `bool()`, conversões inválidas, comportamento de valor-verdade e conversão do texto retornado por `input()`.

## Estrutura do diretório

```text
fundamentals/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-how-python-runs-a-program/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       └── hello_world.py
├── 02-print-and-input/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── interactive_greeting.py
│       └── output_basics.py
├── 03-variables-and-naming/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── learning_profile.py
│       └── variable_basics.py
├── 04-built-in-data-types/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── same_looking_values.py
│       └── value_catalog.py
├── 05-type-and-isinstance/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── check_type_families.py
│       └── inspect_types.py
└── 06-type-conversion/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── conversion_basics.py
        └── conversion_surprises.py
```
