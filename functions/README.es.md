<div align="center">

# Funciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Ruta completa](../docs/learning-path.es.md) · [Roadmap](../docs/roadmap.es.md)

Funciones es la Fase 5 de la secuencia principal de Python Study Guide.

Flujo del Programa enseñó cómo la ejecución decide y repite. Esta fase enseña a dar nombre al comportamiento, pasarle datos, devolver resultados, controlar el alcance, describir interfaces y combinar piezas pequeñas en programas más claros.

## Prerrequisito

Completa primero la [Fase 4: Flujo del Programa](../program-flow/README.es.md).

Antes de continuar, deberías sentirte cómodo con variables y tipos integrados, strings, números, colecciones, condiciones booleanas, `if`, `elif`, `else`, `match`, `case`, `for`, `while`, `range()`, `enumerate()`, `zip()`, `break`, `continue`, `else` de bucles y con decidir qué herramientas de flujo usar juntas según el objetivo del programa.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Estado |
|---|---|---|
| [01. Definir y Llamar Funciones](01-defining-and-calling-functions/README.es.md) | Crear comportamiento con nombre usando `def`, llamarlo, reutilizarlo y seguir la ejecución | Disponible |
| [02. Parámetros y Argumentos](02-parameters-and-arguments/README.es.md) | Recibir entradas obligatorias con argumentos posicionales y por palabra clave básicos | Disponible |
| [03. Valores de Retorno](03-return-values/README.es.md) | Enviar resultados útiles al llamador y seguir el flujo completo de entrada y salida | Disponible |
| [04. Alcance](04-scope/README.es.md) | Entender nombres locales y globales, búsqueda, sombreado y revinculación global explícita | Disponible |
| [05. Type Hints](05-type-hints/README.es.md) | Describir entradas y salidas esperadas sin imponer tipos en runtime por sí solas | Disponible |
| 06. Valores Predeterminados | Diseñar argumentos opcionales de forma clara y segura | Planeado |
| 07. `*args` y `**kwargs` | Recibir cantidades variables de argumentos posicionales y por palabra clave | Planeado |
| 08. Funciones Trabajando Juntas | Componer funciones manteniendo responsabilidades claras | Planeado |
| 09. Flujo de Datos Entre Funciones | Seguir entradas, transformaciones, salidas y propiedad de los datos entre llamadas | Planeado |

Estudia los capítulos en orden al seguir la ruta completa para principiantes.

## Por qué definición y llamada vienen primero

Una función se entiende mejor cuando dos ideas están firmes:

```text
definition = describe and name behavior
call       = execute that behavior now
```

El Capítulo 01 separa esas ideas antes de añadir intercambio de datos. El Capítulo 02 añade entradas mediante parámetros y argumentos. El Capítulo 03 completa el primer recorrido de ida y vuelta con valores de retorno, `None`, retornos por rama y la diferencia entre retornar e imprimir. El Capítulo 04 añade alcance local y global, búsqueda de nombres, sombreado, comportamiento de alcance de sentencias ordinarias y uso cauteloso de `global`. El Capítulo 05 añade type hints de parámetros y retorno, anotaciones de colecciones, uniones con `None` y la diferencia fundamental entre información estática de tipos y enforcement en runtime. Los capítulos posteriores añaden valores predeterminados, recolección flexible de argumentos, composición y flujo explícito de datos sobre el mismo modelo.

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

La Fase 5 trata funciones normales definidas por el usuario y el movimiento de ejecución y datos alrededor de ellas. Manejo de errores, archivos, módulos, bibliotecas externas, decoradores, generadores y recursos avanzados de tipado como generics, protocols y overloads aparecen después o requieren tratamiento propio.

## Empieza aquí

Comienza con [01. Definir y Llamar Funciones](01-defining-and-calling-functions/README.es.md), continúa con [02. Parámetros y Argumentos](02-parameters-and-arguments/README.es.md), luego estudia [03. Valores de Retorno](03-return-values/README.es.md), [04. Alcance](04-scope/README.es.md) y [05. Type Hints](05-type-hints/README.es.md).

Después del Capítulo 05, el siguiente capítulo planeado es **06. Valores Predeterminados**.

La Fase 5 ahora está en progreso con cinco capítulos revisados disponibles.
