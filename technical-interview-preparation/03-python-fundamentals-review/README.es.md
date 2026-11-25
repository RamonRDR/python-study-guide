# Repaso de fundamentos de Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../02-live-coding-and-take-home/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../04-data-structures-and-algorithms-review/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [fundamentals/03-variables-and-naming](../../fundamentals/03-variables-and-naming/README.es.md)
- [fundamentals/04-built-in-data-types](../../fundamentals/04-built-in-data-types/README.es.md)
- [fundamentals/06-type-conversion](../../fundamentals/06-type-conversion/README.es.md)
- [strings-and-numbers/02-common-string-methods](../../strings-and-numbers/02-common-string-methods/README.es.md)
- [program-flow/01-conditions-comparisons-and-boolean-logic](../../program-flow/01-conditions-comparisons-and-boolean-logic/README.es.md)
- [program-flow/02-if-elif-and-else](../../program-flow/02-if-elif-and-else/README.es.md)
- [program-flow/04-for-loops-and-iteration](../../program-flow/04-for-loops-and-iteration/README.es.md)
- [functions/01-defining-and-calling-functions](../../functions/01-defining-and-calling-functions/README.es.md)
- [functions/02-parameters-and-arguments](../../functions/02-parameters-and-arguments/README.es.md)
- [functions/03-return-values](../../functions/03-return-values/README.es.md)
- [functions/04-scope](../../functions/04-scope/README.es.md)
- [functions/06-default-values](../../functions/06-default-values/README.es.md)
- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.es.md)

## Repaso mediante razonamiento

Usa las lecciones enlazadas en vez de reaprender aquí su sintaxis. Un nombre se enlaza a un objeto; su tipo determina las operaciones admitidas. Las conversiones pueden fallar: `int("12")` funciona, pero `int("twelve")` genera ValueError. Las cadenas son inmutables; los métodos devuelven resultados. Las condiciones seleccionan ejecución; los bucles repiten trabajo; las funciones tienen parámetros, retornos y enlaces locales. Explica una regla, muestra un ejemplo y describe un límite.

```python
def add_tag(tags, tag):
    tags.append(tag)
    return tags

original = ["python"]
result = add_tag(original, "testing")
print(original, result)
```

Ambos nombres hacen referencia a la lista modificada. Reasignar el parámetro a una lista nueva no reasignaría el nombre del llamador. Una lista predeterminada se evalúa al definir la función, no en cada llamada; usa None cuando omitir implica crear una lista nueva. Consulta las lecciones enlazadas sobre flujo de datos y valores predeterminados.

## Práctica independiente

Predice la salida antes de ejecutar. Modifica la función para devolver una lista nueva sin mutar la entrada. Prueba una lista vacía y etiquetas repetidas. Explica si el contrato elegido admite duplicados. Repasa LEGB, cortocircuito booleano, igualdad frente a identidad y por qué `is None` es adecuado. No deduzcas identidad por caché de enteros o cadenas.

**Referencia rápida:** tipos, conversión, enlace, mutación, condiciones, bucles, funciones, ámbito y retornos.

<!-- chapter-navigation:bottom -->
[← Anterior](../02-live-coding-and-take-home/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../04-data-structures-and-algorithms-review/README.es.md)
<!-- /chapter-navigation:bottom -->
