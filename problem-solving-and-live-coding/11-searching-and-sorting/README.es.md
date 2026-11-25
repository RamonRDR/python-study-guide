# Retos de búsqueda y ordenación

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../10-functions-and-recursion/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../12-algorithms-and-complexity/README.es.md)
<!-- /chapter-navigation:top -->

Repasa búsqueda lineal, binaria en entrada ordenada e insertion sort. Índice de inserción binaria no tiene que coincidir con objetivo; es primera posición que acepta valor sin romper orden.

Lee contrato y lecciones de requisitos previos enlazadas, predice resultados, intenta el inicial en archivo personal y comprueba límites. Abre pistas progresivamente; compara referencia solo tras intentar. No hay ejecutor en navegador.

### Dos fronteras binarias

En lista ordenada, búsqueda semiabierta encuentra primer valor al menos objetivo (descarta hasta medio cuando valor < objetivo) o primero estrictamente mayor (descarta cuando valor <= objetivo). Ambas pueden devolver centinela longitud. Para [1, 4, 4, 4, 9] y objetivo 4, fronteras 1 y 4; último índice inclusivo 3. Si primera frontera fuera o distinta, objetivo ausente. Dos búsquedas logarítmicas siguen logarítmicas; sin ordenar ni recorrer.

### Fusionar secuencias ordenadas

Mantén puntero al siguiente elemento no consumido de cada entrada. Mientras ambas tengan elementos, añade menor cabeza (cualquiera en empate), avanza solo su puntero y luego consume resto de cualquier secuencia. Para [1, 3] y [2, 3], cabezas producen [1, 2, 3, 3]. Prefijo de salida queda ordenado y contiene apariciones consumidas. Cada puntero avanza por elemento; lista devuelta es espacio de salida, almacenamiento auxiliar constante. Es fusión, no ordenar listas arbitrarias.

## Retos disponibles

- [Primer índice coincidente](../../exercises/problem-solving/linear-first-index/README.es.md) · Fácil · 12 min
- [Índice de inserción binaria](../../exercises/problem-solving/binary-insertion-index/README.es.md) · Media · 22 min
- [Insertion sort descendente](../../exercises/problem-solving/descending-insertion-sort/README.es.md) · Media · 25 min

- [Intervalo del objetivo por búsqueda binaria](../../exercises/problem-solving/binary-target-range/README.es.md) · Difícil · 32 min
- [Fusionar listas ordenadas](../../exercises/problem-solving/merge-sorted-lists/README.es.md) · Difícil · 30 min

<!-- chapter-navigation:bottom -->
[← Anterior](../10-functions-and-recursion/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../12-algorithms-and-complexity/README.es.md)
<!-- /chapter-navigation:bottom -->
