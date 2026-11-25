# Recursividad

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../03-algorithmic-complexity/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../05-searching-algorithms/README.es.md)
<!-- /chapter-navigation:top -->

**Requisitos previos:** [Valores de retorno](../../functions/03-return-values/README.es.md) · [Ámbito](../../functions/04-scope/README.es.md) · [Funciones](../../functions/08-functions-working-together/README.es.md) · [Complejidad](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)

## Objetivo

Entender autollamadas, caso base, progreso y pila de llamadas (35–45 minutos).

## 1. Una instancia menor del mismo problema

La recursividad resuelve un problema llamando a la misma función con una instancia menor. El caso base devuelve sin otra llamada; el paso recursivo debe acercarse a él. Para sumar enteros de 1 a n, usa sum(0) = 0 y sum(n) = n + sum(n - 1) para n positivo. Cada llamada tiene sus propias variables locales; las anteriores esperan los resultados posteriores.

Para n = 3: las llamadas descienden 3 → 2 → 1 → 0. Los retornos se deshacen 0 → 1 → 3 → 6. Sin caso base o llamando con n + 1 no termina para n positivo.

## 2. Implementación en Python

El [ejemplo](examples/recursive_sum.py) acepta enteros exactos de 0 a 100. Rechaza valores fuera del dominio antes de recurrir y usa una función auxiliar privada para no repetir validación. El límite es una restricción didáctica, no una garantía para cualquier configuración de pila Python. Python limita la profundidad y puede lanzar RecursionError; no aumentes el límite solo para resolver un problema lineal. Un acumulador iterativo evita el crecimiento de la pila.

Bajo el modelo de aritmética de coste fijo, ambas versiones tardan O(n); la recursiva usa O(n) de espacio auxiliar en la pila y la iterativa O(1). Una fórmula cerrada evita iterar, pero aquí el objetivo es entender la estructura recursiva.

## Práctica

Rastrea n = 4 en una tabla de llamadas pendientes y valores devueltos. Implementa una cuenta atrás recursiva que devuelva la cantidad de pasos hasta cero para n de 0 a 100. Prueba 0 y 1; compara con un bucle. Explica por qué el argumento decreciente demuestra progreso y por qué importa validar negativos.

**Referencia rápida:** caso base + entrada menor + combinar retornos; cuenta marcos de pila como espacio auxiliar.

Ejecuta desde el directorio de la lección (Python 3.13 como base):

```bash
python examples/recursive_sum.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../03-algorithmic-complexity/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../05-searching-algorithms/README.es.md)
<!-- /chapter-navigation:bottom -->
