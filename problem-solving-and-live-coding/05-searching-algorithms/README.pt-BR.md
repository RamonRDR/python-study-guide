# Algoritmos de busca

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../04-recursion/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../06-sorting-algorithms/README.pt-BR.md)
<!-- /chapter-navigation:top -->

**Pré-requisitos:** [Listas](../../collections/01-list-creation-and-indexing/README.pt-BR.md) · [Controle de loops](../../program-flow/07-break-continue-and-loop-else/README.pt-BR.md) · [Complexidade](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)

## Objetivo

Selecionar e implementar busca linear e binária sob contratos explícitos (35–50 minutos).

## 1. Busca linear

Visite cada item da esquerda para a direita; retorne o índice da primeira ocorrência do alvo, ou -1 se ausente. Funciona com listas de inteiros não ordenadas e preserva entrada. Com [8, 4, 4, 9] e alvo 4, a resposta é 1. Entrada vazia retorna -1. Pior caso O(n) de tempo, O(1) de espaço auxiliar.

## 2. Busca binária

Busca binária precisa de sequência crescente ordenada com acesso aleatório. Mantenha intervalo semiaberto [left, right) contendo as posições ainda possíveis. Inicialmente left=0 e right=len(values). Calcule mid = (left + right) // 2. Se values[mid] for menor que o alvo, descarte até mid definindo left = mid + 1; caso contrário, defina right = mid. Quando os limites se igualam, left é a primeira posição possível de inserção. Verifique se está dentro da lista e é igual ao alvo, ou retorne -1. Essa variante encontra a **primeira** ocorrência mesmo com duplicidades.

Rastreie [2, 4, 4, 7, 9] para alvo 4: intervalo [0,5), mid 2 (4) → [0,2); mid 1 (4) → [0,1); mid 0 (2) → [1,1); índice 1. Cada iteração reduz o intervalo. Não acesse values[len(values)].

## 3. Comparar

O [exemplo](examples/search.py) assume listas de inteiros e entrada crescente ordenada para busca binária; não varre para validar ordenação, pois custaria O(n). No pior caso busca binária leva O(log n) comparações e O(1) de espaço auxiliar; ordenar entrada desordenada apenas para uma consulta pode custar mais que varrer. Recursos como `in` são úteis quando só importa pertinência.

## Prática

Rastreie alvo ausente menor que todos os valores e outro maior; teste listas vazias, unitárias e com duplicidades. Implemente ambas as funções sem ler o exemplo; depois compare. Explique por que busca binária em lista desordenada está fora do contrato.

**Referência rápida:** varredura linear para ordem arbitrária; busca binária apenas com dados ordenados e intervalo que diminui.

Execute a partir do diretório da aula (Python 3.13 como base):

```bash
python examples/search.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../04-recursion/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../06-sorting-algorithms/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
