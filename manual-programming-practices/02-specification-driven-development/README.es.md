# Desarrollo guiado por especificaciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../01-manual-coding-and-debugging/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../03-test-driven-development/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Tiempo estimado:** 40–60 minutos. Convierte una solicitud ambigua en un contrato pequeño y comprobable antes de implementar. Desarrollo guiado por especificaciones (SDD) se usa aquí como flujo ligero, no como herramienta universal ni formato obligatorio. La especificación describe comportamiento observable; la implementación es una forma de satisfacerla.

## 1. De solicitud a requisitos

Solicitud ficticia: "Mostrar cuántas páginas faltan en un libro." Pregunta: ¿qué pasa si hay cero páginas, todas están leídas o la entrada es inválida? Para este ejercicio elegimos explícitamente el contrato siguiente, no porque Python lo exija.

| ID | Requisito |
| --- | --- |
| R1 | Función `remaining_pages(total_pages, pages_read)` devuelve entero igual al total menos leídas. |
| R2 | Acepta solo valores del tipo int nativo (no bool ni subclases de int); si no, lanza TypeError. |
| R3 | Ambos enteros no negativos y pages_read no puede superar total_pages; si no, lanza ValueError. |
| R4 | Sin prompts, impresión, archivos ni red dentro de la función; quien llama se ocupa de mostrar. |

Fuera de alcance: base de datos, interfaz, porcentajes, progreso entre libros. Errores de tipo preceden a errores de valor si ocurren ambos. La restricción al tipo exacto es una elección deliberada del ejercicio: evita comportamiento sobrescrito por subclases. Sin convertir cadenas o floats.

## 2. Criterios de aceptación

| ID | Entrada | Esperado |
| --- | --- | --- |
| AC1 | (20, 7) | 13 |
| AC2 | (20, 0); (20, 20); (0, 0) | 20; 0; 0 |
| AC3 | (-1, 0); (20, -1); (20, 21) | ValueError |
| AC4 | ("20", 7); (20, 7.0); (True, 0); (20, False) | TypeError |
| AC5 | llamada válida | sin salida en stdout o stderr |

Los criterios conectan requisitos con evidencia observable. Las pruebas pueden codificarlos; por sí solas no demuestran todos los requisitos posibles.

## 3. Plan, tareas y decisión

Crea un `specification.md` en tu carpeta de práctica con contrato, ejemplos y exclusiones. Crea `plan.md`: validar tipos, validar rangos, calcular resultado, verificar pruebas. Divide en tareas con condiciones de finalización. No implementes todo de una vez; usa pruebas incrementales en la siguiente lección.

Una ADR (registro de decisión de arquitectura) registra contexto, decisión y consecuencias. Ejemplo: elegir función pura en lugar de script interactivo para reutilizar y probar el resultado sin E/S de terminal. Contrapartida: quien llama debe mostrar o recoger datos. Registra en `adr-0001.md`; proyectos mayores pueden usar un directorio. Las ADR registran decisiones significativas, no cada línea.

## 4. Control de cambios y práctica independiente

Imagina que piden aceptar la cadena "20". No cambies silenciosamente la implementación: aclara necesidad, actualiza contrato y criterios, revisa pruebas, implementa y revisa. Por ahora el contrato rechaza cadenas. Escribe tu especificación de otra función simple, con casos normales, límites e inválidos; intercámbiala con alguien o reléela como revisor. ¿Pueden implementar sin adivinar?

SDD responde **qué y por qué**. TDD ayuda a verificar **cómo se implementa el comportamiento** en pequeños pasos. Ninguno sustituye comprensión, diseño ni revisión humana. Consulta la [especificación](../../docs/specs/learning-hub-foundation/specification.es.md) y el [índice de ADR](../../docs/adr/README.es.md) del proyecto como ejemplo real mayor, no formato obligatorio para cada programa pequeño.

**Referencia rápida:** solicitud → aclarar → requisitos y exclusiones → criterios → plan/tareas → decisiones → pruebas e implementación → revisión.

<!-- chapter-navigation:bottom -->
[← Anterior](../01-manual-coding-and-debugging/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../03-test-driven-development/README.es.md)
<!-- /chapter-navigation:bottom -->
