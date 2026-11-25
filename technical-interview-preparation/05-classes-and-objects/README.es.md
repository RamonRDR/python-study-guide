# Clases y objetos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../04-data-structures-and-algorithms-review/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../06-attributes-methods-and-object-behavior/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [functions/01-defining-and-calling-functions](../../functions/01-defining-and-calling-functions/README.es.md)
- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.es.md)
- [comments-and-documentation/02-docstrings](../../comments-and-documentation/02-docstrings/README.es.md)

## Qué es y por qué

Una clase define un tipo y agrupa comportamientos relacionados; una instancia es un objeto de ese tipo con estado propio. Prefiere una clase cuando estado y operaciones comparten ciclo de vida o invariante. Una función pura puede ser más simple para un cálculo sin estado.

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

first = Counter()
second = Counter()
first.increment()
print(first.value, second.value)  # 1 0
```

La llamada a la clase normalmente crea e inicializa una instancia. `__init__` inicializa una instancia ya creada; no es el mecanismo de creación del objeto (`__new__`). No devuelvas un valor distinto de None desde `__init__`. `self` es el nombre convencional del parámetro de instancia; una llamada como `first.increment()` enlaza esa instancia automáticamente. Cada asignación a `self.value` almacena estado en la instancia.

## Ejemplo práctico y errores

El ejemplo compartido modela una sesión de lectura. Su método read valida la cantidad antes de actualizar el estado. Dos sesiones mantienen totales independientes. No uses un atributo mutable compartido de clase para estado por instancia; no añadas clases solo para envolver una función independiente.

## Práctica

Implementa una sesión que registre tareas completadas en vez de páginas. Crea dos instancias, prueba estado independiente y garantiza que cantidades inválidas no cambien el total. Explica clase, instancia, atributo y método con tus palabras.

**Referencia rápida:** clase define tipo; instancia guarda estado; método opera en la instancia; inicializa y valida deliberadamente.

[Ejemplo ejecutable compartido](examples/reading_session.py)

`python technical-interview-preparation/05-classes-and-objects/examples/reading_session.py`

## Referencias oficiales (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../04-data-structures-and-algorithms-review/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../06-attributes-methods-and-object-behavior/README.es.md)
<!-- /chapter-navigation:bottom -->
