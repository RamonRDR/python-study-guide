<div align="center">

# Coleções

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta seção é a Fase 3 da sequência principal de aprendizagem do Python Study Guide. Ela parte de textos e números para ensinar como vários valores relacionados podem ser organizados em coleções antes que o fluxo do programa introduza iteração repetida e ramificações.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. Criação, indexação e fatiamento de listas](01-list-creation-and-indexing/README.pt-BR.md) | Criar coleções ordenadas e ler itens individuais e intervalos | Iniciante | Disponível |
| [02. Modificando listas e métodos comuns de listas](02-modifying-lists-and-methods/README.pt-BR.md) | Alterar o conteúdo de listas de forma deliberada e entender mutação | Iniciante | Disponível |
| 03. Tuplas e imutabilidade | Usar sequências imutáveis e compará-las com listas | Iniciante | Planejado |
| 04. Dicionários: chaves e valores | Organizar valores por chaves significativas em vez de posições | Iniciante | Planejado |
| 05. Conjuntos e valores únicos | Trabalhar com itens únicos e operações de pertencimento de conjuntos | Iniciante | Planejado |
| 06. Escolhendo a coleção certa | Comparar listas, tuplas, dicionários e conjuntos pela intenção | Iniciante | Planejado |

## Por que esta ordem?

A trilha desenvolve uma ideia de cada vez:

```text
one value
    ↓
ordered group of values
    ↓
changing an ordered group
    ↓
immutable ordered group
    ↓
key -> value relationships
    ↓
unique-value collections
    ↓
choose by intent
```

Listas vêm primeiro porque sua indexação e seu fatiamento reutilizam o modelo de sequência da Fase 2. A mutação fica separada em um segundo capítulo para que uma pessoa iniciante possa compreender a estrutura de uma lista antes de aprender todas as formas de alterá-la.

As tuplas tornam explícita a diferença entre mutabilidade e imutabilidade. Dicionários introduzem uma mudança conceitual maior, saindo de posições numéricas para chaves. Conjuntos aparecem depois porque são coleções cujo modelo principal não é indexação posicional. O capítulo final reúne as quatro escolhas.

## Orientação de pré-requisitos

- **01. Criação, indexação e fatiamento de listas:** conclua primeiro as Fases 1 e 2. Você deve compreender variáveis, tipos embutidos comuns, `len()`, índices inteiros, fatiamento de strings, valores booleanos e funções numéricas embutidas comuns.
- **02. Modificando listas e métodos comuns de listas:** conclua primeiro o Capítulo 01 para aprender mutação sobre um modelo de sequência já estável.
- **03. Tuplas e imutabilidade:** conclua os dois capítulos de listas para que o contraste entre sequências mutáveis e imutáveis tenha uma referência concreta.
- **04. Dicionários: chaves e valores:** conclua primeiro os capítulos de sequências. Este capítulo muda o modelo de busca de posições para chaves.
- **05. Conjuntos e valores únicos:** conclua primeiro o capítulo de dicionários. Conjuntos removem a busca posicional e se concentram em pertencimento e unicidade.
- **06. Escolhendo a coleção certa:** conclua os cinco capítulos anteriores para que a comparação use conceitos que você já praticou.

Ao seguir a trilha completa, estude os capítulos em ordem numérica.

## Objetivos da seção

Ao final da Fase 3, você deverá conseguir:

- criar e ler listas com confiança;
- modificar listas de forma deliberada e reconhecer alterações feitas no próprio objeto;
- explicar a diferença entre listas mutáveis e tuplas imutáveis;
- armazenar e recuperar valores com chaves de dicionário;
- usar conjuntos quando unicidade e pertencimento forem centrais;
- reconhecer quais tipos de coleção são posicionais e quais não são;
- escolher uma coleção de acordo com a relação entre os valores, e não apenas pela familiaridade com a sintaxe;
- entrar na Fase 4 preparado para usar loops e condicionais com coleções que já compreende.

## Limite de escopo

A Fase 3 se concentra na estrutura das coleções e em operações básicas.

Ela intencionalmente **não** ensina:

- loops `for` ou `while`;
- comprehensions de listas, dicionários ou conjuntos;
- `enumerate()` ou `zip()`;
- callbacks avançados de ordenação;
- classes de coleção personalizadas.

Essas ideias ficam mais fáceis depois que a pessoa entende primeiro o que as coleções contêm e como cada coleção organiza seus valores.

## Status da seção

A Fase 3 está **em andamento**. Os Capítulos 01 e 02 estão disponíveis em inglês, português brasileiro e espanhol. Os Capítulos 03 a 06 continuam planejados e serão adicionados como capítulos completos e revisáveis, sem placeholders vazios.

## Estrutura atual do diretório

```text
collections/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-list-creation-and-indexing/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── list_basics.py
│       └── list_slicing.py
└── 02-modifying-lists-and-methods/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── list_copying.py
        ├── list_methods.py
        └── list_mutation.py
```
