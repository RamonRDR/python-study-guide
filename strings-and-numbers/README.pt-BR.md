<div align="center">

# Textos e Números

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta seção corresponde à Fase 2 da sequência principal de aprendizagem do Python Study Guide. Ela se apoia em Fundamentos para aprofundar valores de texto e numéricos do Python antes da introdução de coleções e fluxo do programa.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. Criação e indexação de strings](01-string-creation-and-indexing/README.pt-BR.md) | Criar strings e ler posições e intervalos com segurança | Iniciante | Disponível |
| 02. Métodos comuns de strings | Transformar, pesquisar, dividir e unir texto | Iniciante | Planejado |
| 03. `int`, `float` e `bool` | Trabalhar com mais profundidade com valores numéricos e lógicos | Iniciante | Planejado |
| 04. `round()`, `abs()`, `min()`, `max()` e `sum()` | Usar funções embutidas numéricas comuns | Iniciante | Planejado |

## Orientação de pré-requisitos

- **01. Criação e indexação de strings:** conclua a Fase 1 primeiro. Você deve entender variáveis, `str`, `int`, `type()`, conversão de tipos e execução básica de programas.
- **02. Métodos comuns de strings:** conclua o Capítulo 01 primeiro. Você deve entender imutabilidade de strings, indexação, slicing e a diferença entre a string original e um resultado do tipo string produzido sem modificá-la.
- **03. `int`, `float` e `bool`:** a Fase 1 já apresentou esses tipos. Este capítulo aprofundará seu comportamento depois que os capítulos de texto estabelecerem uma intuição mais forte sobre sequências.
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

Comece por [Criação e Indexação de Strings](01-string-creation-and-indexing/README.pt-BR.md). Ele apresenta literais de string, `len()`, índices positivos e negativos, slicing, limites de slices, `IndexError` e imutabilidade de strings.

## Estrutura do diretório

```text
strings-and-numbers/
├── README.md
├── README.pt-BR.md
├── README.es.md
└── 01-string-creation-and-indexing/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── fixed_position_text.py
        └── string_basics.py
```

A árvore representa arquivos que existem atualmente. Os capítulos planejados aparecem na trilha de aprendizagem, mas não são apresentados como diretórios até que seu conteúdo seja adicionado.
