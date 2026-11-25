# Retos mixtos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../14-refactoring-challenges/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../16-timed-live-coding/README.es.md)
<!-- /chapter-navigation:top -->

Combina conceptos anteriores en vez de adivinar algoritmo nuevo. Reformula contrato, elige estructuras y desempate y rastrea ejemplo pequeño antes de programar.

Lee contrato y lecciones de requisitos previos enlazadas, predice resultados, intenta el inicial en archivo personal y comprueba límites. Abre pistas progresivamente; compara referencia solo tras intentar. No hay ejecutor en navegador.

### Conciliación como composición

Separa conciliación en agregación, claves únicas ordenadas y comparación. Por fila, desempaqueta etiqueta y cantidad; suma en diccionario específico de entrada. Mantén conjunto de vistos y lista ordenada mientras recorres expected antes de actual. Luego visita etiquetas en ese orden, obtén totales ausentes con get(label, 0) y emite fila de diferencia solo si difieren. Para expected [["a", 2], ["a", 3]] y actual [["a", 4]], esperado 5, real 4, delta -1. Comparar antes de agregar clasificaría duplicados mal. Flujo combina mapas de frecuencias, conservación de orden y acumuladores enseñados; sin ordenar ni datos externos.

## Retos disponibles

- [Longitud total de etiquetas cortas](../../exercises/problem-solving/total-short-lengths/README.es.md) · Fácil · 15 min
- [Etiqueta más frecuente](../../exercises/problem-solving/most-frequent-label/README.es.md) · Media · 25 min

- [Conciliar registros de inventario](../../exercises/problem-solving/inventory-reconciliation/README.es.md) · Difícil · 40 min

<!-- chapter-navigation:bottom -->
[← Anterior](../14-refactoring-challenges/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../16-timed-live-coding/README.es.md)
<!-- /chapter-navigation:bottom -->
