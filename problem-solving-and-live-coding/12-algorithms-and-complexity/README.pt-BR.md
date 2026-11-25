# Desafios de algoritmos e complexidade

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../11-searching-and-sorting/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../13-debugging-challenges/README.pt-BR.md)
<!-- /chapter-navigation:top -->

Compare contagens de operações e armazenamento antes de escolher solução. Para n posições há n(n-1) pares ordenados de posições diferentes, o dobro da contagem não ordenada; use essa identidade aritmética. Para duplicados, compare varredura repetida com set. Testes funcionais não provam limites assintóticos.

Leia contrato e aulas de pré-requisitos vinculadas, preveja resultados, tente o inicial em arquivo pessoal e verifique limites. Abra dicas progressivamente; compare referência só após tentar. Não há executor no navegador.

### Contar multiplicidades, não apenas valores

Dois ponteiros anteriores detectam existência de par. Para contar cada par de índices em entrada ordenada, descarte fronteira se soma pequena ou grande. Em correspondência exata com extremos distintos, conte ocorrências consecutivas de cada valor pelo seu extremo e multiplique: dois 1 e três 3 formam seis pares somando 4. Consuma ambos grupos. Se extremos iguais, ordenação implica todos restantes iguais. Para k índices restantes, conte k(k-1)//2 e pare. Quatro 2 geram seis pares, não dois. Ponteiros avançam monotonicamente; trabalho total linear mesmo com loops internos de contagem. Sem cópia de entrada.

## Desafios disponíveis

- [Contar pares não ordenados](../../exercises/problem-solving/unordered-pair-count/README.pt-BR.md) · Fácil · 12 min
- [Detectar duplicado](../../exercises/problem-solving/has-duplicate/README.pt-BR.md) · Média · 18 min

- [Contar pares-alvo com duplicados](../../exercises/problem-solving/sorted-pair-multiplicity/README.pt-BR.md) · Difícil · 40 min

<!-- chapter-navigation:bottom -->
[← Anterior](../11-searching-and-sorting/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../13-debugging-challenges/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
