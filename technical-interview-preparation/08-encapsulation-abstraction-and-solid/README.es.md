# Encapsulación, abstracción y SOLID

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../07-inheritance-polymorphism-and-composition/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [Herencia y composición](../07-inheritance-polymorphism-and-composition/README.es.md)
- [manual-programming-practices/02-specification-driven-development](../../manual-programming-practices/02-specification-driven-development/README.es.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.es.md)
- [practical-projects/03-user-registration](../../practical-projects/03-user-registration/README.es.md)

## Encapsulación y abstracción

La encapsulación expone operaciones que preservan estado válido. En el ejemplo de inventario, remove valida antes de cambiar cantidad. Un guion bajo inicial señala un detalle no público por convención; dos guiones bajos iniciales activan name mangling, no seguridad. Una property puede exponer lectura sin setter normal; los llamadores aún pueden eludir convenciones, así que no es una frontera de control de acceso.

La abstracción define qué promete un colaborador sin obligar a los llamadores a saber cómo funciona. `ABC` y `@abstractmethod` de la biblioteca estándar expresan un contrato abstracto explícito: una subclase concreta debe implementar métodos abstractos antes de la instanciación normal. `StockReader` define available; un lector de memoria u otra fuente puede respetar el mismo contrato. Una anotación de tipo por sí sola no impone comportamiento en ejecución.

## SOLID como preguntas de diseño

| Principio | Pregunta práctica |
| --- | --- |
| Responsabilidad única (SRP) | ¿Este componente tiene una razón coherente para cambiar? |
| Abierto/cerrado (OCP) | ¿Una variación prevista puede soportarse mediante un punto de extensión estable sin modificar todos los llamadores? |
| Sustitución de Liskov (LSP) | ¿Puede un subtipo sustituir la base sin romper el comportamiento prometido? |
| Segregación de interfaces (ISP) | ¿El llamador depende solo de las operaciones necesarias? |
| Inversión de dependencias (DIP) | ¿La política de alto nivel puede depender de una abstracción útil en vez de un detalle concreto de infraestructura? |

El ejemplo de inventario separa reglas de estado de lectura; el lector expone solo available; remaining depende de ese contrato. Un lector doble facilita las pruebas. SOLID es un conjunto de heurísticas de diseño, no sintaxis Python ni requisito de cinco clases. Un cálculo puntual puede necesitar solo una función. Introduce abstracciones cuando reduzcan acoplamiento relevante o apoyen variación real.

## Práctica

Añade un lector doble que devuelva 7 y verifica remaining sin modificarlo. Intenta retirar más de lo que hay en el inventario; prueba que la cantidad no cambia. Explica qué dos principios SOLID se aplican y un coste de introducir una abstracción adicional.

**Referencia rápida:** protege invariantes, expón contratos pequeños, favorece sustitución útil, justifica complejidad.

[Ejemplo ejecutable compartido](examples/stock.py)

`python technical-interview-preparation/08-encapsulation-abstraction-and-solid/examples/stock.py`

## Referencias oficiales (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)
- [abc](https://docs.python.org/3.13/library/abc.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../07-inheritance-polymorphism-and-composition/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:bottom -->
