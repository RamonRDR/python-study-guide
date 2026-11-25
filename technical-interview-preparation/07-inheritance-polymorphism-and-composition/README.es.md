# Herencia, polimorfismo y composición

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../06-attributes-methods-and-object-behavior/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../08-encapsulation-abstraction-and-solid/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [Lección anterior de OOP](../06-attributes-methods-and-object-behavior/README.es.md)
- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.es.md)

## Herencia y sustitución

La herencia crea una subclase, escrita `class Child(Parent):`. Puede reutilizar o redefinir comportamiento heredado. Úsala cuando el subtipo respeta el contrato de la base, no solo porque dos implementaciones tienen líneas similares. En un ejemplo de herencia simple, `super().__init__(...)` puede inicializar la parte base; en general super sigue el orden de resolución de métodos, no simplemente un padre fijo.

## Polimorfismo y composición

El polimorfismo permite al llamador usar una operación común con implementaciones diferentes. Python suele permitir duck typing: un objeto puede cumplir un contrato de comportamiento sin compartir clase base. La composición almacena o recibe un colaborador en vez de heredar su implementación. En el ejemplo compartido, Notifier delega al método send del canal. El canal devuelve texto, no un mensaje real de red. Puede sustituirse por otro canal compatible o un doble de prueba. TextChannel y EmailChannel redefinen Channel.send, mientras el contrato base indica que las subclases deben proporcionar la operación. Una clase independiente con el mismo contrato también puede funcionar.

Evita jerarquías profundas elegidas solo para reutilizar código; no supongas que nombres iguales de métodos garantizan semántica igual. La composición añade una dependencia explícita, que puede ser más fácil de sustituir, pero puede añadir indirección.

## Práctica

Añade un canal ficticio de registro que devuelva `"log: Ready"` para el mensaje `"Ready"` sin cambiar Notifier. Prueba un doble y explica el contrato que todos los canales deben respetar. Explica un caso donde la herencia es apropiada y otro donde la composición es más simple.

**Referencia rápida:** herencia = relación de subtipo; polimorfismo = comportamiento intercambiable; composición = colaboración.

[Ejemplo ejecutable compartido](examples/notifications.py)

`python technical-interview-preparation/07-inheritance-polymorphism-and-composition/examples/notifications.py`

## Referencias oficiales (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../06-attributes-methods-and-object-behavior/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../08-encapsulation-abstraction-and-solid/README.es.md)
<!-- /chapter-navigation:bottom -->
