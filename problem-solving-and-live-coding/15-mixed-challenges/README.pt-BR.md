# Desafios mistos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../14-refactoring-challenges/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../16-timed-live-coding/README.pt-BR.md)
<!-- /chapter-navigation:top -->

Combine conceitos anteriores em vez de adivinhar algoritmo novo. Reformule contrato, escolha estruturas e desempate e rastreie exemplo pequeno antes de programar.

Leia contrato e aulas de pré-requisitos vinculadas, preveja resultados, tente o inicial em arquivo pessoal e verifique limites. Abra dicas progressivamente; compare referência só após tentar. Não há executor no navegador.

### Conciliação como composição

Separe conciliação em agregação, chaves únicas ordenadas e comparação. Para cada linha, desempacote rótulo e quantidade; some em dicionário específico de cada entrada. Mantenha set de vistos e lista ordenada enquanto percorre expected antes de actual. Depois visite rótulos nessa ordem, obtenha totais ausentes com get(label, 0) e emita linha de diferença só se totais diferirem. Para expected [["a", 2], ["a", 3]] e actual [["a", 4]], esperado 5, real 4, delta -1. Comparar antes de agregar classificaria duplicidades incorretamente. Pipeline combina mapas de frequência, preservação de ordem e acumuladores ensinados; sem ordenação ou dados externos.

## Desafios disponíveis

- [Comprimento total de rótulos curtos](../../exercises/problem-solving/total-short-lengths/README.pt-BR.md) · Fácil · 15 min
- [Rótulo mais frequente](../../exercises/problem-solving/most-frequent-label/README.pt-BR.md) · Média · 25 min

- [Conciliar registros de estoque](../../exercises/problem-solving/inventory-reconciliation/README.pt-BR.md) · Difícil · 40 min

<!-- chapter-navigation:bottom -->
[← Anterior](../14-refactoring-challenges/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../16-timed-live-coding/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
