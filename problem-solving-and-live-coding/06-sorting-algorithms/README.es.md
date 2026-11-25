# Algoritmos de ordenación

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../05-searching-algorithms/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../07-problem-solving-patterns/README.es.md)
<!-- /chapter-navigation:top -->

**Requisitos previos:** [List methods](../../collections/02-modifying-lists-and-methods/README.es.md) · [range](../../program-flow/05-range-enumerate-and-zip/README.es.md) · [Complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)

## Objetivo

Comprender tres algoritmos elementales de ordenación y sus compromisos (45–60 minutos).

## 1. Qué promete ordenar

Dada una lista de enteros, devuelve una nueva lista ascendente con exactamente los valores originales, incluidos duplicados. La lista del llamador debe quedar intacta. Ordenar no es eliminar duplicados. Copia la lista una vez antes de modificarla; la copia es la salida requerida.

## 2. Bubble sort

Compara valores adyacentes e intercambia si izquierda > derecha. Tras una pasada completa, el mayor valor restante queda en su posición final al extremo. Reduce la zona sin ordenar y termina pronto si no hay intercambios. [3, 1, 2] pasa a [1, 3, 2] y después [1, 2, 3]. Una ordenación estable mantiene el orden relativo de elementos con claves iguales; intercambiar solo inversiones estrictas hace estable esta variante.

## 3. Selection sort

En cada índice, busca el índice del mínimo en el sufijo restante e intercambia ese valor con la posición actual. El prefijo queda ordenado y definitivo. [3, 1, 2] → [1, 3, 2] → [1, 2, 3]. La variante habitual con intercambios no es estable: registros con claves iguales pueden cruzarse. Recorre cada sufijo incluso si ya está ordenado.

## 4. Insertion sort

Trata el primer elemento como prefijo ordenado. Guarda el siguiente valor, desplaza los elementos mayores del prefijo una posición a la derecha e inserta el valor guardado en el hueco. [3, 1, 2] → [1, 3, 2] → [1, 2, 3]. Desplaza solo valores estrictamente mayores para conservar estabilidad. Cada pasada amplía el prefijo ordenado.

| Variante | Mejor tiempo | Peor tiempo | Estable |
| --- | --- | --- | --- |
| Bubble (salida temprana) | O(n) | O(n²) | Sí |
| Selection | O(n²) | O(n²) | No |
| Insertion | O(n) | O(n²) | Sí |

Las tres usan O(1) de espacio auxiliar excluyendo la copia O(n) requerida como retorno. Contando la copia como asignación adicional, el almacenamiento extra total es O(n). Son algoritmos didácticos, no recomendaciones por defecto en producción. Python `sorted(values)` devuelve una lista nueva, mientras `values.sort()` modifica la lista; ambos son estables. Prefiere funciones incorporadas para ordenar en aplicaciones habituales.

## Práctica

Rastrea cada algoritmo a mano para [4, 2, 2, 1]. Predice comportamiento con entrada vacía, ordenada e inversa; implementa uno antes de abrir el [ejemplo compartido](examples/sort.py). Comprueba orden, multiplicidades y entrada intacta. Explica por qué probar solo el orden podría aceptar una solución que elimina duplicados.

**Referencia rápida:** bubble corrige inversiones adyacentes, selection elige un mínimo, insertion amplía el prefijo ordenado.

Ejecuta desde el directorio de la lección (Python 3.13 como base):

```bash
python examples/sort.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../05-searching-algorithms/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../07-problem-solving-patterns/README.es.md)
<!-- /chapter-navigation:bottom -->
