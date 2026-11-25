# Algoritmos de ordenação

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../05-searching-algorithms/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../07-problem-solving-patterns/README.pt-BR.md)
<!-- /chapter-navigation:top -->

**Pré-requisitos:** [Métodos de listas](../../collections/02-modifying-lists-and-methods/README.pt-BR.md) · [range](../../program-flow/05-range-enumerate-and-zip/README.pt-BR.md) · [Complexidade](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)

## Objetivo

Compreender três algoritmos elementares de ordenação e seus trade-offs (45–60 minutos).

## 1. O que ordenar promete

Dada uma lista de inteiros, retorne nova lista crescente com exatamente os valores originais, incluindo duplicidades. A lista do chamador deve permanecer inalterada. Ordenar não é remover duplicados. Copie a lista uma vez antes de modificá-la; a cópia é a saída exigida.

## 2. Bubble sort

Compare valores adjacentes e troque se esquerda > direita. Após passagem completa, o maior valor restante está em sua posição final no fim. Reduza a região não ordenada e pare cedo se não houver troca. [3, 1, 2] vira [1, 3, 2] e depois [1, 2, 3]. Uma ordenação estável preserva a ordem relativa de itens com chaves iguais; trocar apenas inversões estritas torna esta variante estável.

## 3. Selection sort

Em cada índice, procure o índice do mínimo no sufixo restante e troque esse valor para a posição atual. O prefixo fica ordenado e definitivo. [3, 1, 2] → [1, 3, 2] → [1, 2, 3]. A variante usual com trocas não é estável: registros de chaves iguais podem cruzar. Ela ainda varre cada sufixo mesmo se já ordenado.

## 4. Insertion sort

Trate o primeiro item como prefixo ordenado. Guarde o próximo valor, desloque itens maiores do prefixo uma posição à direita e insira o valor guardado na lacuna. [3, 1, 2] → [1, 3, 2] → [1, 2, 3]. Desloque apenas valores estritamente maiores para preservar estabilidade. Cada passagem amplia o prefixo ordenado.

| Variante | Melhor tempo | Pior tempo | Estável |
| --- | --- | --- | --- |
| Bubble (saída antecipada) | O(n) | O(n²) | Sim |
| Selection | O(n²) | O(n²) | Não |
| Insertion | O(n) | O(n²) | Sim |

As três usam O(1) de espaço auxiliar excluindo a cópia O(n) exigida como retorno. Contando a cópia como alocação adicional, armazenamento extra total é O(n). São algoritmos didáticos, não recomendações padrão para produção. Python `sorted(values)` retorna nova lista, enquanto `values.sort()` modifica a lista; ambos são estáveis. Prefira recursos nativos para ordenar em aplicações comuns.

## Prática

Rastreie cada algoritmo à mão para [4, 2, 2, 1]. Preveja comportamento em entrada vazia, ordenada e reversa; implemente um antes de abrir o [exemplo compartilhado](examples/sort.py). Verifique ordenação, multiplicidades e entrada inalterada. Explique por que testar apenas ordem pode aceitar solução que elimina duplicados.

**Referência rápida:** bubble corrige inversões adjacentes, selection escolhe mínimo, insertion amplia prefixo ordenado.

Execute a partir do diretório da aula (Python 3.13 como base):

```bash
python examples/sort.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../05-searching-algorithms/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../07-problem-solving-patterns/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
