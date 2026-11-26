# Gestión de memoria en Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../09-object-identity-references-and-copying/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../11-iterators-generators-and-comprehensions/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [technical-interview-preparation/09-object-identity-references-and-copying](../../technical-interview-preparation/09-object-identity-references-and-copying/README.es.md)

## Vida y alcanzabilidad de objetos

La gestión de memoria es cómo una implementación asigna y recupera almacenamiento. Un objeto vivo puede ser alcanzable mediante nombres, contenedores, cierres u otros objetos. `del name` elimina un enlace; no necesariamente destruye el objeto. Python no promete finalización inmediata. En CPython 3.13 convencional, el conteo de referencias recupera muchos objetos cuando desaparecen referencias fuertes, complementado por un recolector de ciclos. Un ciclo puede mantener conteos por encima de cero incluso cuando resulta inalcanzable. Otras implementaciones y builds free-threaded pueden diferir; no dependas del instante exacto de recolección.

```python
first = []
second = first
del first
second.append("still alive")
print(second)
```

Una referencia débil no mantiene por sí misma vivo al objeto; `weakref.ref(obj)()` puede devolver el objeto o None tras destruirse. No todos los objetos admiten referencias débiles (las listas normales no). Úsalas solo cuando la relación no debe mantener vivo al objeto. Usa `with` para archivos y recursos similares; no dependas de la recolección para liberar recursos a tiempo.

## Retención y medición

Una caché alcanzable, colección global o cierre puede retener objetos indefinidamente sin defecto del recolector. Limita cachés por cantidad o presupuesto de recursos adecuado; elimina referencias innecesarias. El ejemplo compartido expulsa la clave insertada o actualizada hace más tiempo usando orden de inserción del diccionario. Leer una instantánea no renueva el orden: no es una caché LRU completa. Un límite de cantidad no limita bytes, y la instantánea superficial no aísla valores mutables.

`tracemalloc` permite comparar instantáneas de asignaciones Python; no mide toda la memoria del proceso ni asignaciones nativas. `gc.collect()` solicita recolección; no libera objetos alcanzables ni promete reducir RSS. Evita forzar recolección como solución predeterminada.

## Práctica

Ejecuta la caché, actualiza una clave antigua, inserta otra y comprueba la expulsión. Vacía la caché y explica por qué alias externos aún podrían retener valores. Esboza un ciclo entre dos contenedores y distingue ciclos inalcanzables de retención alcanzable.

**Referencia rápida:** alcanzabilidad y propiedad primero; el tiempo de recolección no es contrato de recursos; mide antes de optimizar.

## Ejemplo ejecutable compartido

[bounded_cache.py](examples/bounded_cache.py)

`python technical-interview-preparation/10-python-memory-management/examples/bounded_cache.py`

## Referencias oficiales (Python 3.13)

- [Python 3.13: reference/datamodel.html](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13: library/gc.html](https://docs.python.org/3.13/library/gc.html)
- [Python 3.13: library/weakref.html](https://docs.python.org/3.13/library/weakref.html)
- [Python 3.13: library/tracemalloc.html](https://docs.python.org/3.13/library/tracemalloc.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../09-object-identity-references-and-copying/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../11-iterators-generators-and-comprehensions/README.es.md)
<!-- /chapter-navigation:bottom -->
