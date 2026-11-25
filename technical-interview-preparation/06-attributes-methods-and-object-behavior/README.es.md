# Atributos, métodos y comportamiento de objetos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../05-classes-and-objects/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../07-inheritance-polymorphism-and-composition/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [Clases y objetos](../05-classes-and-objects/README.es.md)
- [functions/06-default-values](../../functions/06-default-values/README.es.md)
- [collections/02-modifying-lists-and-methods](../../collections/02-modifying-lists-and-methods/README.es.md)

## Atributos y enlace

Un atributo de instancia almacena datos por objeto; uno de clase normalmente ofrece datos compartidos accesibles desde las instancias. Asignar un atributo de instancia con el mismo nombre suele ocultar el atributo de clase. Un atributo mutable de clase, como una lista, es un error común de compartición accidental; inicializa listas independientes en `__init__`.

| Tipo de método | Recibe implícitamente | Propósito |
| --- | --- | --- |
| Instancia | self | Leer o cambiar estado de la instancia |
| Clase | cls | Constructores alternativos o comportamiento de la clase |
| Estático | Ninguno | Utilidad relacionada sin estado implícito |

Los marcadores incorporados `@classmethod` y `@staticmethod` cambian el enlace; el mecanismo general de decoradores se enseña después. En el ejemplo, `from_label` llama a cls para poder construir una subclase; `valid_label` no necesita instancia. Un método estático no es automáticamente puro.

## Métodos especiales

Nombres como `__len__`, `__str__` y `__repr__` integran objetos con operaciones de Python. `len(group)` usa el protocolo de longitud; `str(group)` se orienta al usuario; repr ayuda a depurar y no necesita ser Python ejecutable. Respeta contratos documentados (la longitud debe ser un entero no negativo). Igualdad y hashing requieren semánticas compatibles; sus contratos avanzados se tratan en la lección de identidad. Evita inventar nombres dunder.

## Práctica

Ejecuta el ejemplo compartido de grupo de estudio. Crea dos grupos, añade un miembro solo a uno y comprueba ambas longitudes. Explica por qué la lista members es por instancia y category es compartido. Añade una prueba de etiqueta vacía. Compara str y repr.

**Referencia rápida:** self = instancia; cls = clase; estático = sin argumento implícito; métodos especiales implementan protocolos.

[Ejemplo ejecutable compartido](examples/study_group.py)

`python technical-interview-preparation/06-attributes-methods-and-object-behavior/examples/study_group.py`

## Referencias oficiales (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../05-classes-and-objects/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../07-inheritance-polymorphism-and-composition/README.es.md)
<!-- /chapter-navigation:bottom -->
