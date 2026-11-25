# Patrones de resolución de problemas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../06-sorting-algorithms/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../08-strings-and-numbers/README.es.md)
<!-- /chapter-navigation:top -->

**Requisitos previos:** [Diccionarios](../../collections/04-dictionaries-keys-and-values/README.es.md) · [Conjuntos](../../collections/05-sets-and-unique-values/README.es.md) · [Complejidad](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)

## Objetivo

Reconocer patrones reutilizables y elegirlos según el contrato (40–55 minutos).

## 1. Acumulador y mapa de frecuencias

Un acumulador resume valores procesados en una variable (por ejemplo una suma). Un mapa de frecuencias guarda conteos por clave distinta. Para ["a", "b", "a"], actualiza un diccionario con `counts.get(item, 0) + 1`; resultado {"a": 2, "b": 1}. Los conteos crecen al recorrer; lista vacía da diccionario vacío. Tiempo esperado O(n) bajo hashing normal y almacenamiento O(k) para k claves distintas (la salida requerida aquí). Para pertenencia solamente, puede bastar un set. No uses set para contar apariciones porque elimina duplicados.

## 2. Dos punteros

Para lista de enteros ordenada ascendente, decide si dos **índices diferentes** suman un objetivo. Inicia left en 0 y right en len(values)-1. Si la suma es pequeña, mueve left a la derecha; si es grande, mueve right a la izquierda; igualdad es éxito. Para cuando left >= right. El orden justifica descartar una frontera: si menor más mayor es pequeño, ese menor no puede formar par con ningún valor restante. [1, 3, 6, 8], objetivo 9, acierta con 1+8. [4], objetivo 8, falla. O(n) de tiempo y O(1) de espacio auxiliar, suponiendo orden sin validarlo.

## 3. Ventana deslizante fija

Para hallar la suma máxima de k enteros consecutivos (1 <= k <= len(values)), suma los primeros k una vez; en cada movimiento, resta el valor que sale y suma el que entra. Guarda la mejor suma. Para [4, -1, 3, 2], k=2, las sumas son 3, 2, 5; resultado 5. Inicia la mejor con la primera suma, no cero, porque todos los valores pueden ser negativos. La implementación compartida calcula la primera suma con un bucle, sin rebanada; O(n) de tiempo y O(1) de espacio auxiliar. El ejemplo exige k entero exacto y lanza TypeError para tipo incorrecto o ValueError para tamaño fuera del intervalo permitido. Una ventana fija no es un subconjunto arbitrario; tampoco se afirma que reglas de ventana variable funcionen con negativos.

## Práctica

Rastrea cada patrón con los ejemplos anteriores. Antes de abrir el [ejemplo compartido](examples/patterns.py), implementa un mapa de frecuencias para una lista de etiquetas; prueba duplicados y entrada vacía. Intenta un par ausente y un par de dos valores duplicados; prueba una ventana con todos negativos y k igual al tamaño. Explica por qué fuerza bruta puede ser referencia de corrección antes de optimizar.

**Referencia rápida:** acumulador para resúmenes; mapa para conteos; dos punteros cuando el orden permite eliminar; ventana fija para intervalos adyacentes.

Ejecuta desde el directorio de la lección (Python 3.13 como base):

```bash
python examples/patterns.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../06-sorting-algorithms/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../08-strings-and-numbers/README.es.md)
<!-- /chapter-navigation:bottom -->
