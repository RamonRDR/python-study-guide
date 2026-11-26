# Identidad de objetos, referencias y copias

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../08-encapsulation-abstraction-and-solid/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../10-python-memory-management/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.es.md)
- [collections/02-modifying-lists-and-methods](../../collections/02-modifying-lists-and-methods/README.es.md)
- [program-flow/01-conditions-comparisons-and-boolean-logic](../../program-flow/01-conditions-comparisons-and-boolean-logic/README.es.md)

## Identidad, igualdad y enlace

Todo objeto tiene identidad, tipo y valor. `is` compara identidad; `==` usa la semántica de igualdad, que una clase puede personalizar. Usa `is None` para el singleton, no `is` para comparar cadenas o enteros. `id(obj)` identifica un objeto vivo, pero los IDs pueden reutilizarse después de su vida; específicamente en CPython es la dirección de memoria.

La asignación enlaza un nombre, no crea una copia. Los parámetros de función también se enlazan a objetos: reasignar un parámetro no reasigna el nombre del llamador, mientras mutar un objeto mutable compartido puede ser visible mediante ambos nombres.

```python
from copy import copy, deepcopy

original = {"steps": ["draft"]}
alias = original
shallow = copy(original)
deep = deepcopy(original)
shallow["steps"].append("review")
print(original == shallow, original is shallow)
print(alias is original, deep["steps"])
```

La salida es `True False`, luego `True ['draft']`. Una copia superficial crea otro diccionario externo pero comparte la lista interna. La copia profunda copia recursivamente componentes compatibles; su memo registra objetos ya copiados, incluidos ciclos y referencias repetidas. No garantiza un objeto nuevo por componente (los inmutables pueden compartirse), ni clona recursos externos. Las clases personalizadas pueden controlar la copia.

## Igualdad y hashing

Los objetos hashables deben tener hash estable y los objetos iguales deben tener hashes iguales. Objetos distintos pueden colisionar. Listas y diccionarios no son hashables; una tupla es hashable solo si sus elementos lo son. Si implementas igualdad por valor en una clase mutable, usarla como clave puede romper la búsqueda si cambia su hash. Python normalmente hace no hashable una clase cuando define `__eq__` sin `__hash__`.

## Práctica

Ejecuta el ejemplo compartido. Haz que dos claves referencien la misma lista y comprueba que la copia profunda conserva esa relación interna separándola del original. Prueba primero una copia superficial. Prefiere no copiar para compartir deliberadamente, copia superficial para estructura externa independiente y copia profunda solo cuando el contrato de propiedad anidada lo exige; copiar grafos grandes cuesta tiempo y memoria.

**Referencia rápida:** alias comparte; superficial copia contenedor; profunda copia grafo compatible; igualdad no es identidad.

## Ejemplo ejecutable compartido

[copy_plan.py](examples/copy_plan.py)

`python technical-interview-preparation/09-object-identity-references-and-copying/examples/copy_plan.py`

## Referencias oficiales (Python 3.13)

- [Python 3.13: reference/datamodel.html](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13: library/copy.html](https://docs.python.org/3.13/library/copy.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../08-encapsulation-abstraction-and-solid/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../10-python-memory-management/README.es.md)
<!-- /chapter-navigation:bottom -->
