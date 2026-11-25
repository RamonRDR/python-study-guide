# Complexidade algorítmica

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../02-constraints-and-edge-cases/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../04-recursion/README.pt-BR.md)
<!-- /chapter-navigation:top -->

**Pré-requisitos:** [for](../../program-flow/04-for-loops-and-iteration/README.pt-BR.md) · [while](../../program-flow/06-while-loops-and-state-driven-repetition/README.pt-BR.md) · [Coleções](../../collections/06-choosing-the-right-collection/README.pt-BR.md)

## Objetivo

Comparar como tempo e armazenamento extra crescem com o tamanho da entrada (35–50 minutos).

## 1. Contar trabalho, não segundos

Seja n o número de elementos, supondo operações primitivas de custo constante sobre valores de tamanho fixo. Big O descreve um limite superior assintótico de crescimento, não segundos nem necessariamente um limite justo. Para estes exemplos damos limites justos de crescimento (também expressáveis com Theta). Constantes e termos de ordem inferior não alteram a classe assintótica. Declare hipóteses de pior, melhor e caso médio.

| Crescimento | Exemplo |
| --- | --- |
| O(1) | Acessar um índice válido de lista |
| O(log n) | Dividir repetidamente um tamanho positivo pela metade |
| O(n) | Visitar cada elemento uma vez |
| O(n log n) | n operações em cada um de logaritmicamente muitos níveis |
| O(n²) | Visitar todo par ordenado de n elementos |

Duas varreduras consecutivas custam O(n), não O(n²). Loop aninhado não precisa ser quadrático: conte iterações reais. Para tamanho 8, o loop 8 → 4 → 2 → 1 tem 3 passos, uma varredura 8 e pares ordenados 64. Veja [contagem de operações](examples/operation_counts.py); dobrar n dobra a varredura, quadruplica os pares e adiciona cerca de um passo à divisão pela metade.

## 2. Espaço e trade-offs

Espaço auxiliar é armazenamento de trabalho adicional, excluindo entrada e, pela convenção declarada aqui, saída exigida. Um acumulador usa O(1); uma cópia de lista com n valores usa O(n) de espaço extra. Chamadas recursivas também usam pilha. Uma tabela hash pode reduzir buscas repetidas a consultas de tempo constante esperado sob hipóteses comuns de hashing, mas armazena entradas adicionais e a consulta no pior caso pode ser linear. Aritmética de inteiros de tamanho arbitrário e comparações de strings em Python podem depender do tamanho dos operandos; declare o modelo simplificado em vez de afirmar que toda operação é constante.

## 3. Comparar adequadamente

Não escolha algoritmo complexo para entrada pequena só pelo crescimento assintótico; considere clareza, restrições reais, memória e correção. Medições de tempo variam com hardware e não são provas. Conte operações e raciocine sobre crescimento.

## Prática

Para n = 4, 8, 16, preveja contagens de varredura, pares e divisões; execute o exemplo e explique por que duas varreduras independentes continuam O(n). Compare retornar uma contagem com criar lista de todos os valores correspondentes, distinguindo espaço auxiliar e da saída.

**Referência rápida:** defina n e hipóteses, conte iterações, identifique pior caso e contabilize espaço auxiliar.

Execute a partir do diretório da aula (Python 3.13 como base):

```bash
python examples/operation_counts.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../02-constraints-and-edge-cases/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../04-recursion/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
