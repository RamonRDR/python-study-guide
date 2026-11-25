# Repaso de estructuras de datos y algoritmos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../03-python-fundamentals-review/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../05-classes-and-objects/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [collections/01-list-creation-and-indexing](../../collections/01-list-creation-and-indexing/README.es.md)
- [collections/03-tuples-and-immutability](../../collections/03-tuples-and-immutability/README.es.md)
- [collections/04-dictionaries-keys-and-values](../../collections/04-dictionaries-keys-and-values/README.es.md)
- [collections/05-sets-and-unique-values](../../collections/05-sets-and-unique-values/README.es.md)
- [collections/06-choosing-the-right-collection](../../collections/06-choosing-the-right-collection/README.es.md)
- [problem-solving-and-live-coding/03-algorithmic-complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [problem-solving-and-live-coding/04-recursion](../../problem-solving-and-live-coding/04-recursion/README.es.md)
- [problem-solving-and-live-coding/05-searching-algorithms](../../problem-solving-and-live-coding/05-searching-algorithms/README.es.md)
- [problem-solving-and-live-coding/06-sorting-algorithms](../../problem-solving-and-live-coding/06-sorting-algorithms/README.es.md)
- [problem-solving-and-live-coding/07-problem-solving-patterns](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)
- [problem-solving-and-live-coding/08-strings-and-numbers](../../problem-solving-and-live-coding/08-strings-and-numbers/README.es.md)

## Elige según el contrato

Una lista representa orden y repetición; una tupla fija sus posiciones; un diccionario asocia claves hashables a valores; un conjunto representa miembros únicos hashables. Una tupla puede contener objetos mutables y no siempre es hashable. Elige la estructura según su comportamiento, no por una clasificación memorizada.

Para detectar duplicados, un conjunto de valores hashables vistos evita un recorrido anidado. Bajo supuestos habituales de hashing en el caso promedio, un recorrido cuesta O(n) tiempo y hasta O(n) espacio auxiliar. No prometas acceso constante en el peor caso a diccionarios/conjuntos. La búsqueda lineal funciona con entrada desordenada; la binaria requiere datos ordenados e invariante válido. La recursión necesita caso base y progreso hacia él; incluye el espacio de pila de llamadas. Explica compromisos de ordenación usando las lecciones de la Fase 11, no solo el nombre del algoritmo.

## Práctica con retos existentes

Usa el banco original de la Fase 11: `has-duplicate` para pertenencia, `binary-target-range` para límites y `longest-distinct-substring` para ventanas variables. Estudia primero la instrucción correspondiente. Para cada uno, declara restricciones, elige estructura, explica tiempo/espacio con supuestos, prueba casos límite y compara con la referencia.

**Referencia rápida:** contrato → representación → algoritmo → complejidad → pruebas.

Retos existentes: [has-duplicate](../../exercises/problem-solving/has-duplicate/README.es.md) · [binary-target-range](../../exercises/problem-solving/binary-target-range/README.es.md) · [longest-distinct-substring](../../exercises/problem-solving/longest-distinct-substring/README.es.md)

<!-- chapter-navigation:bottom -->
[← Anterior](../03-python-fundamentals-review/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../05-classes-and-objects/README.es.md)
<!-- /chapter-navigation:bottom -->
