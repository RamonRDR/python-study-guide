# Algoritmos de búsqueda

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../04-recursion/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../06-sorting-algorithms/README.es.md)
<!-- /chapter-navigation:top -->

**Requisitos previos:** [Lists](../../collections/01-list-creation-and-indexing/README.es.md) · [Loop control](../../program-flow/07-break-continue-and-loop-else/README.es.md) · [Complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)

## Objetivo

Seleccionar e implementar búsqueda lineal y binaria con contratos explícitos (35–50 minutos).

## 1. Búsqueda lineal

Visita cada elemento de izquierda a derecha; devuelve el índice de la primera aparición del objetivo, o -1 si falta. Funciona con listas de enteros sin ordenar y conserva la entrada. Con [8, 4, 4, 9] y objetivo 4, la respuesta es 1. Una entrada vacía devuelve -1. Peor caso O(n) de tiempo, O(1) de espacio auxiliar.

## 2. Búsqueda binaria

La búsqueda binaria necesita una secuencia ordenada ascendente con acceso aleatorio. Mantén un intervalo semiabierto [left, right) con las posiciones aún posibles. Inicialmente left=0 y right=len(values). Calcula mid = (left + right) // 2. Si values[mid] es menor que el objetivo, descarta hasta mid poniendo left = mid + 1; en otro caso, pon right = mid. Cuando los límites coinciden, left es la primera posición posible de inserción. Comprueba que está dentro de la lista y que es igual al objetivo, o devuelve -1. Esta variante encuentra la **primera** coincidencia incluso con duplicados.

Rastrea [2, 4, 4, 7, 9] para objetivo 4: intervalo [0,5), mid 2 (4) → [0,2); mid 1 (4) → [0,1); mid 0 (2) → [1,1); índice 1. Cada iteración reduce el intervalo. No accedas a values[len(values)].

## 3. Comparar

El [ejemplo](examples/search.py) supone listas de enteros y entrada ordenada ascendente para búsqueda binaria; no recorre para validar el orden porque costaría O(n). En el peor caso la búsqueda binaria necesita O(log n) comparaciones y O(1) de espacio auxiliar; ordenar una entrada desordenada para una sola consulta puede costar más que recorrerla. Recursos como `in` son útiles si solo importa pertenencia.

## Práctica

Rastrea un objetivo ausente menor que todos los valores y otro mayor; prueba listas vacías, unitarias y con duplicados. Implementa ambas funciones sin leer el ejemplo; después compara. Explica por qué la búsqueda binaria en una lista desordenada está fuera del contrato.

**Referencia rápida:** recorrido lineal para orden arbitrario; búsqueda binaria solo con datos ordenados e intervalo decreciente.

Ejecuta desde el directorio de la lección (Python 3.13 como base):

```bash
python examples/search.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../04-recursion/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../06-sorting-algorithms/README.es.md)
<!-- /chapter-navigation:bottom -->
