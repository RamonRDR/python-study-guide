# Revisão de estruturas de dados e algoritmos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../03-python-fundamentals-review/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../05-classes-and-objects/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [collections/01-list-creation-and-indexing](../../collections/01-list-creation-and-indexing/README.pt-BR.md)
- [collections/03-tuples-and-immutability](../../collections/03-tuples-and-immutability/README.pt-BR.md)
- [collections/04-dictionaries-keys-and-values](../../collections/04-dictionaries-keys-and-values/README.pt-BR.md)
- [collections/05-sets-and-unique-values](../../collections/05-sets-and-unique-values/README.pt-BR.md)
- [collections/06-choosing-the-right-collection](../../collections/06-choosing-the-right-collection/README.pt-BR.md)
- [problem-solving-and-live-coding/03-algorithmic-complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)
- [problem-solving-and-live-coding/04-recursion](../../problem-solving-and-live-coding/04-recursion/README.pt-BR.md)
- [problem-solving-and-live-coding/05-searching-algorithms](../../problem-solving-and-live-coding/05-searching-algorithms/README.pt-BR.md)
- [problem-solving-and-live-coding/06-sorting-algorithms](../../problem-solving-and-live-coding/06-sorting-algorithms/README.pt-BR.md)
- [problem-solving-and-live-coding/07-problem-solving-patterns](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)
- [problem-solving-and-live-coding/08-strings-and-numbers](../../problem-solving-and-live-coding/08-strings-and-numbers/README.pt-BR.md)

## Escolha pelo contrato

Uma lista representa ordem e repetição; uma tupla fixa suas posições; um dicionário associa chaves hashable a valores; um conjunto representa membros únicos hashable. Uma tupla pode conter objetos mutáveis e nem sempre é hashable. Escolha a estrutura pelo comportamento, não por um ranking decorado.

Para detectar duplicados, um conjunto de valores hashable vistos evita uma varredura aninhada. Sob hipóteses usuais de hashing no caso médio, a varredura custa O(n) tempo e até O(n) espaço auxiliar. Não prometa acesso constante no pior caso a dicionários/conjuntos. Busca linear funciona com entrada desordenada; busca binária exige dados ordenados e invariante válido. Recursão precisa de caso base e progresso em sua direção; inclua espaço da pilha de chamadas. Explique trade-offs de ordenação usando as aulas da Fase 11, não apenas o nome do algoritmo.

## Prática com desafios existentes

Use o banco original da Fase 11: `has-duplicate` para pertinência, `binary-target-range` para limites e `longest-distinct-substring` para janelas variáveis. Estude primeiro a instrução correspondente. Para cada um, declare restrições, escolha estrutura, explique tempo/espaço com hipóteses, teste casos de borda e compare com a referência.

**Referência rápida:** contrato → representação → algoritmo → complexidade → testes.

Desafios existentes: [has-duplicate](../../exercises/problem-solving/has-duplicate/README.pt-BR.md) · [binary-target-range](../../exercises/problem-solving/binary-target-range/README.pt-BR.md) · [longest-distinct-substring](../../exercises/problem-solving/longest-distinct-substring/README.pt-BR.md)

<!-- chapter-navigation:bottom -->
[← Anterior](../03-python-fundamentals-review/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../05-classes-and-objects/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
