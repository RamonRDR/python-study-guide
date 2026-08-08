<div align="center">

# Textos e Números

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta seção corresponde à Fase 2 da sequência principal de aprendizagem do Python Study Guide. Ela se apoia em Fundamentos para aprofundar valores de texto e numéricos do Python antes da introdução de coleções e fluxo do programa.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. Criação e indexação de strings](01-string-creation-and-indexing/README.pt-BR.md) | Criar strings e ler posições e intervalos com segurança | Iniciante | Disponível |
| [02. Métodos comuns de strings](02-common-string-methods/README.pt-BR.md) | Transformar, pesquisar, dividir e unir texto | Iniciante | Disponível |
| [03. `int`, `float` e `bool`](03-int-float-and-bool/README.pt-BR.md) | Aprofundar o comportamento de inteiros, ponto flutuante e booleanos | Iniciante | Disponível |
| 04. `round()`, `abs()`, `min()`, `max()` e `sum()` | Usar funções embutidas numéricas comuns | Iniciante | Planejado |

## Orientação de pré-requisitos

- **01. Criação e indexação de strings:** conclua a Fase 1 primeiro. Você deve entender variáveis, `str`, `int`, `type()`, conversão de tipos e execução básica de programas.
- **02. Métodos comuns de strings:** conclua o Capítulo 01 primeiro. Você deve entender imutabilidade de strings, indexação, slicing e a diferença entre a string original e um resultado do tipo string produzido sem modificá-la.
- **03. `int`, `float` e `bool`:** conclua primeiro o Capítulo 02. A Fase 1 já apresentou esses tipos; este capítulo aprofunda comportamento numérico, precisão de ponto flutuante e valores de verdade.
- **04. Funções numéricas embutidas:** conclua primeiro o capítulo sobre tipos numéricos para aprender essas funções dentro de um contexto, e não como uma lista isolada.

Estude os capítulos em ordem numérica ao seguir a trilha completa.

```text
01. String creation and indexing
        ↓
02. Common string methods
        ↓
03. int, float, and bool
        ↓
04. round(), abs(), min(), max(), and sum()
```

## Objetivos da seção

Ao final desta trilha de aprendizagem, você deverá conseguir:

- criar e inspecionar valores de texto com confiança;
- ler posições e intervalos de strings com indexação e slicing;
- usar operações comuns de strings respeitando sua imutabilidade;
- distinguir e usar tipos comuns de valores numéricos e lógicos;
- aplicar adequadamente funções numéricas embutidas frequentes;
- conectar entrada textual, conversão de tipos e cálculos numéricos;
- reconhecer quando uma operação textual ou numérica produz um valor de resultado sem modificar o valor original.

## Capítulo atual

Continue com [`int`, `float` e `bool`](03-int-float-and-bool/README.pt-BR.md). Ele aprofunda comportamento de inteiros e ponto flutuante, divisão verdadeira e pelo piso, restos, aproximação de ponto flutuante, valores de verdade e a relação entre `bool` e `int`.

## Estrutura do diretório

```text
strings-and-numbers/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-string-creation-and-indexing/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── fixed_position_text.py
│       └── string_basics.py
├── 02-common-string-methods/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── normalize_text.py
│       └── split_and_join.py
└── 03-int-float-and-bool/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── numeric_behavior.py
        └── truth_and_precision.py
```

A árvore representa arquivos que existem atualmente. Os capítulos planejados aparecem na trilha de aprendizagem, mas não são apresentados como diretórios até que seu conteúdo seja adicionado.
