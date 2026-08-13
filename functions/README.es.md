<div align="center">

# Funciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Ruta completa](../docs/learning-path.es.md) · [Roadmap](../docs/roadmap.es.md)

Funciones es la Fase 5 de la secuencia principal de Python Study Guide.

Flujo del Programa enseñó cómo la ejecución decide y repite. Esta fase enseña cómo **dar nombre al comportamiento, pasarle datos, devolver resultados, controlar el alcance, describir interfaces y combinar piezas pequeñas en programas más claros**.

## Prerrequisito

Completa primero la [Fase 4: Flujo del Programa](../program-flow/README.es.md).

Ya deberías sentirte cómodo con:

- variables y tipos integrados;
- strings, números y colecciones;
- condiciones booleanas;
- `if`, `elif` y `else`;
- `match` y `case`;
- `for` y `while`;
- `range()`, `enumerate()` y `zip()`;
- `break`, `continue` y `else` de bucles;
- elegir y combinar herramientas de flujo según la intención.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Estado |
|---|---|---|
| [01. Definir y Llamar Funciones](01-defining-and-calling-functions/README.es.md) | Crear comportamiento con nombre usando `def`, llamarlo, reutilizarlo y seguir la ejecución | Disponible |
| [02. Parámetros y Argumentos](02-parameters-and-arguments/README.es.md) | Recibir entradas obligatorias con argumentos posicionales y por palabra clave básicos | Disponible |
| 03. Valores de Retorno | Enviar resultados útiles de vuelta al llamador | Planeado |
| 04. Alcance | Entender dónde son visibles los nombres y cómo funciona su búsqueda | Planeado |
| 05. Type Hints | Describir entradas y salidas esperadas sin cambiar por sí solos el comportamiento en runtime | Planeado |
| 06. Valores Predeterminados | Diseñar argumentos opcionales con claridad y seguridad | Planeado |
| 07. `*args` y `**kwargs` | Recibir cantidades variables de argumentos posicionales y por palabra clave | Planeado |
| 08. Funciones Trabajando Juntas | Componer funciones manteniendo responsabilidades claras | Planeado |
| 09. Flujo de Datos Entre Funciones | Seguir entradas, transformaciones, salidas y responsabilidad entre llamadas | Planeado |

Estudia los capítulos en orden al seguir la ruta completa para principiantes.

## Por qué definición y llamada vienen primero

Una función se entiende mucho mejor cuando dos ideas están firmes primero:

```text
definition = describe and name behavior
call       = execute that behavior now
```

El Capítulo 01 aísla esas ideas antes de añadir intercambio de datos.

El Capítulo 02 añade parámetros obligatorios, argumentos posicionales y argumentos por palabra clave básicos para que una función trabaje con entradas diferentes. El Capítulo 03 añadirá valores de retorno. Los capítulos posteriores construirán alcance, type hints, valores predeterminados, recolección flexible de argumentos, composición y flujo explícito de datos sobre el mismo modelo de definición/llamada.

## Progresión de la fase

```text
define and call
    ↓
parameters and arguments
    ↓
return values
    ↓
scope
    ↓
type hints
    ↓
default values
    ↓
*args and **kwargs
    ↓
functions working together
    ↓
data flow between functions
```

## Límite de alcance

La Fase 5 se centra en funciones normales definidas por el usuario y en el movimiento de ejecución y datos alrededor de ellas.

No requiere:

- manejo de excepciones con `try` y `except`;
- manejo de archivos;
- módulos y paquetes como tema principal;
- bibliotecas externas;
- decoradores;
- generadores;
- patrones avanzados de programación funcional.

Esos conceptos aparecen después o requieren tratamiento propio.

## Empieza aquí

Comienza con [01. Definir y Llamar Funciones](01-defining-and-calling-functions/README.es.md) y luego continúa con [02. Parámetros y Argumentos](02-parameters-and-arguments/README.es.md).

Después del Capítulo 02, el siguiente capítulo planeado es **03. Valores de Retorno**.

**La Fase 5 ahora está en progreso con dos capítulos revisados disponibles.**
