# Complejidad algorítmica

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../02-constraints-and-edge-cases/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../04-recursion/README.es.md)
<!-- /chapter-navigation:top -->

**Requisitos previos:** [for](../../program-flow/04-for-loops-and-iteration/README.es.md) · [while](../../program-flow/06-while-loops-and-state-driven-repetition/README.es.md) · [Collections](../../collections/06-choosing-the-right-collection/README.es.md)

## Objetivo

Comparar cómo crecen el tiempo y el almacenamiento adicional con el tamaño de entrada (35–50 minutos).

## 1. Contar trabajo, no segundos

Sea n el número de elementos, suponiendo operaciones primitivas de coste constante sobre valores de tamaño fijo. Big O describe una cota superior asintótica de crecimiento, no segundos ni necesariamente una cota ajustada. Para estos ejemplos damos cotas ajustadas (también expresables con Theta). Constantes y términos de orden inferior no cambian la clase asintótica. Declara supuestos del peor, mejor y caso medio.

| Crecimiento | Ejemplo |
| --- | --- |
| O(1) | Acceder a un índice válido de lista |
| O(log n) | Reducir repetidamente a la mitad un tamaño positivo |
| O(n) | Visitar cada elemento una vez |
| O(n log n) | n operaciones en cada uno de logarítmicamente muchos niveles |
| O(n²) | Visitar cada par ordenado de n elementos |

Dos recorridos consecutivos cuestan O(n), no O(n²). Un bucle anidado no tiene por qué ser cuadrático: cuenta las iteraciones reales. Para tamaño 8, el bucle 8 → 4 → 2 → 1 tiene 3 pasos, un recorrido 8 y los pares ordenados 64. Consulta [conteo de operaciones](examples/operation_counts.py); duplicar n duplica el recorrido, cuadruplica los pares y añade aproximadamente un paso de reducción a la mitad.

## 2. Espacio y compromisos

El espacio auxiliar es almacenamiento adicional de trabajo, excluyendo entrada y, según la convención declarada aquí, salida requerida. Un acumulador usa O(1); copiar una lista de n valores usa O(n) extra. Las llamadas recursivas también usan pila. Una tabla hash puede reducir búsquedas repetidas a consultas de tiempo constante esperado bajo supuestos habituales de hashing, pero guarda entradas adicionales y la consulta en el peor caso puede ser lineal. La aritmética de enteros de tamaño arbitrario y las comparaciones de cadenas en Python pueden depender del tamaño de los operandos; declara el modelo simplificado en vez de afirmar que toda operación es constante.

## 3. Comparar adecuadamente

No elijas un algoritmo complejo para entradas pequeñas solo por crecimiento asintótico; considera claridad, restricciones reales, memoria y corrección. Las mediciones de tiempo varían con el hardware y no son demostraciones. Cuenta operaciones y razona sobre el crecimiento.

## Práctica

Para n = 4, 8, 16, predice los conteos de recorrido, pares y reducciones; ejecuta el ejemplo y explica por qué dos recorridos independientes siguen siendo O(n). Compara devolver un conteo con crear una lista de todos los valores que coinciden, distinguiendo espacio auxiliar y de salida.

**Referencia rápida:** define n y supuestos, cuenta iteraciones, identifica el peor caso y contabiliza el espacio auxiliar.

Ejecuta desde el directorio de la lección (Python 3.13 como base):

```bash
python examples/operation_counts.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../02-constraints-and-edge-cases/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../04-recursion/README.es.md)
<!-- /chapter-navigation:bottom -->
