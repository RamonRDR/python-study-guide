# Desafios de busca e ordenação

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../10-functions-and-recursion/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../12-algorithms-and-complexity/README.pt-BR.md)
<!-- /chapter-navigation:top -->

Revise busca linear, binária em entrada ordenada e insertion sort. Índice de inserção binária não precisa corresponder ao alvo; é primeira posição que aceita valor sem quebrar ordem.

Leia contrato e aulas de pré-requisitos vinculadas, preveja resultados, tente o inicial em arquivo pessoal e verifique limites. Abra dicas progressivamente; compare referência só após tentar. Não há executor no navegador.

### Duas fronteiras binárias

Em lista ordenada, busca semiaberta encontra primeiro valor pelo menos alvo (descarte até meio quando valor < alvo) ou primeiro estritamente maior (descarte quando valor <= alvo). Ambas podem retornar sentinela comprimento. Para [1, 4, 4, 4, 9] e alvo 4, fronteiras 1 e 4; último índice inclusivo 3. Se primeira fronteira fora da lista ou diferente, alvo ausente. Duas buscas logarítmicas continuam logarítmicas; sem ordenar ou varrer.

### Intercalar sequências ordenadas

Mantenha ponteiro para próximo item não consumido de cada entrada. Enquanto ambas têm itens, acrescente menor cabeça (qualquer em empate), avance só seu ponteiro e depois consuma restante de qualquer sequência. Para [1, 3] e [2, 3], cabeças produzem [1, 2, 3, 3]. Prefixo de saída fica ordenado e contém ocorrências consumidas. Cada ponteiro avança por item; lista retornada é espaço de saída, armazenamento auxiliar constante. É intercalação, não ordenação de listas arbitrárias.

## Desafios disponíveis

- [Primeiro índice correspondente](../../exercises/problem-solving/linear-first-index/README.pt-BR.md) · Fácil · 12 min
- [Índice de inserção binária](../../exercises/problem-solving/binary-insertion-index/README.pt-BR.md) · Média · 22 min
- [Insertion sort decrescente](../../exercises/problem-solving/descending-insertion-sort/README.pt-BR.md) · Média · 25 min

- [Intervalo do alvo por busca binária](../../exercises/problem-solving/binary-target-range/README.pt-BR.md) · Difícil · 32 min
- [Intercalar listas ordenadas](../../exercises/problem-solving/merge-sorted-lists/README.pt-BR.md) · Difícil · 30 min

<!-- chapter-navigation:bottom -->
[← Anterior](../10-functions-and-recursion/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../12-algorithms-and-complexity/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
