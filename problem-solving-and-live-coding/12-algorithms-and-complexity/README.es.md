# Retos de algoritmos y complejidad

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../11-searching-and-sorting/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../13-debugging-challenges/README.es.md)
<!-- /chapter-navigation:top -->

Compara conteos de operaciones y almacenamiento antes de elegir solución. Para n posiciones hay n(n-1) pares ordenados de posiciones distintas, el doble del conteo no ordenado; usa esa identidad aritmética. Para duplicados, compara recorrido repetido con conjunto. Pruebas funcionales no demuestran cotas asintóticas.

Lee contrato y lecciones de requisitos previos enlazadas, predice resultados, intenta el inicial en archivo personal y comprueba límites. Abre pistas progresivamente; compara referencia solo tras intentar. No hay ejecutor en navegador.

### Contar multiplicidades, no solo valores

Dos punteros anteriores detectan existencia de par. Para contar cada par de índices en entrada ordenada, descarta frontera si suma pequeña o grande. En coincidencia exacta con extremos distintos, cuenta apariciones consecutivas de cada valor desde su extremo y multiplica: dos 1 y tres 3 forman seis pares que suman 4. Consume ambos grupos. Si extremos iguales, orden implica todos restantes iguales. Para k índices restantes cuenta k(k-1)//2 y termina. Cuatro 2 dan seis pares, no dos. Punteros avanzan monótonamente; trabajo total lineal incluso con bucles internos. Sin copia de entrada.

## Retos disponibles

- [Contar pares no ordenados](../../exercises/problem-solving/unordered-pair-count/README.es.md) · Fácil · 12 min
- [Detectar duplicado](../../exercises/problem-solving/has-duplicate/README.es.md) · Media · 18 min

- [Contar pares objetivo con duplicados](../../exercises/problem-solving/sorted-pair-multiplicity/README.es.md) · Difícil · 40 min

<!-- chapter-navigation:bottom -->
[← Anterior](../11-searching-and-sorting/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../13-debugging-challenges/README.es.md)
<!-- /chapter-navigation:bottom -->
