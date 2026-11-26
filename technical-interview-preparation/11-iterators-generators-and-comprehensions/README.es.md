# Iteradores, generadores y comprensiones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../10-python-memory-management/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../12-closures-and-decorators/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [program-flow/04-for-loops-and-iteration](../../program-flow/04-for-loops-and-iteration/README.es.md)
- [standard-library/07-itertools](../../standard-library/07-itertools/README.es.md)

## Protocolo de iteración

Un iterable suministra iterador mediante `iter()`. Un iterador se devuelve a sí mismo mediante `iter()`, produce valores con `next()` y señala agotamiento mediante `StopIteration`. Una lista puede proporcionar nuevos iteradores; un iterador individual se consume. Una función generadora contiene `yield`; llamarla crea un generador sin ejecutar el cuerpo. Cada avance reanuda hasta un yield o finalización. Conserva estado de ejecución entre avances. No lances StopIteration explícitamente en el cuerpo para terminar; usa return o llega al final.

```python
values = [1, 2, 3]
squares = [value ** 2 for value in values]
stream = (value ** 2 for value in values)
print(squares, next(stream), list(stream), list(stream))
```

Salida: `[1, 4, 9] 1 [4, 9] []`. Comprensiones de lista, conjunto y diccionario construyen contenedores inmediatamente: `[x for x in values if x > 1]`, `{x for x in values}`, `{x: x ** 2 for x in values}`. Una expresión generadora difiere el cálculo de resultados (la expresión iterable más a la izquierda se evalúa inmediatamente). Las comprensiones admiten filtros y bucles anidados, pero la lógica compleja queda más clara en funciones nombradas o bucles normales.

## Cuándo usar streaming

El ejemplo compartido filtra filas sin materializar toda la entrada. Usa estado adicional constante excluyendo entrada, salida y almacenamiento del llamador; llamar list materializa resultados. La evaluación perezosa puede reducir almacenamiento máximo y permitir terminar pronto, pero no garantiza menor tiempo total o memoria en todo pipeline. Evita consumo repetido cuando necesites colección reutilizable; no consumas silenciosamente un iterador solo para inspeccionarlo.

## Práctica

Usa fuente generadora registrando cada elemento consumido, llama next una vez y consume el resto. Prueba entrada vacía y agotamiento. Compara comprensión inmediata con generador para flujo grande; explica cuándo se justifica materializar.

**Referencia rápida:** iterable suministra; iterador avanza; generador suspende; comprensión construye; expresión generadora transmite.

## Ejemplo ejecutable compartido

[eligible_rows.py](examples/eligible_rows.py)

`python technical-interview-preparation/11-iterators-generators-and-comprehensions/examples/eligible_rows.py`

## Referencias oficiales (Python 3.13)

- [Python 3.13: tutorial/classes.html#iterators](https://docs.python.org/3.13/tutorial/classes.html#iterators)
- [Python 3.13: tutorial/classes.html#generators](https://docs.python.org/3.13/tutorial/classes.html#generators)
- [Python 3.13: tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions)
- [Python 3.13: reference/expressions.html#generator-expressions](https://docs.python.org/3.13/reference/expressions.html#generator-expressions)

<!-- chapter-navigation:bottom -->
[← Anterior](../10-python-memory-management/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../12-closures-and-decorators/README.es.md)
<!-- /chapter-navigation:bottom -->
