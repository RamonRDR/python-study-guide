<div align="center">

# Funciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Ruta completa](../docs/learning-path.es.md) · [Roadmap](../docs/roadmap.es.md)

Funciones es la Fase 5 de la secuencia principal de Python Study Guide.

Flujo del Programa enseñó cómo la ejecución decide y repite. Esta fase enseña a dar nombre al comportamiento, pasarle datos, devolver resultados, controlar el alcance, describir interfaces, combinar piezas pequeñas en programas más claros y seguir los datos a través de las fronteras entre funciones.

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
| [06. Valores Predeterminados](06-default-values/README.es.md) | Diseñar argumentos opcionales con seguridad, incluida la evaluación al definir y los valores mutables | Disponible |
| [07. `*args` y `**kwargs`](07-args-and-kwargs/README.es.md) | Recibir cantidades intencionalmente variables de argumentos posicionales y por palabra clave | Disponible |
| [08. Funciones Trabajando Juntas](08-functions-working-together/README.es.md) | Componer funciones auxiliares y coordinadoras manteniendo claras las responsabilidades y dependencias | Disponible |
| [09. Flujo de Datos Entre Funciones](09-data-flow-between-functions/README.es.md) | Seguir entradas del llamador, vínculos de parámetros, transformaciones, mutación, salidas retornadas y propiedad de los datos entre llamadas | Disponible |

Estudia los capítulos en orden al seguir la ruta completa para principiantes.

## Por qué definición y llamada vienen primero

Una función se entiende mejor cuando dos ideas están firmes:

```text
definition = describe and name behavior
call       = execute that behavior now
```

El Capítulo 01 separa esas ideas antes de añadir intercambio de datos. El Capítulo 02 añade entradas mediante parámetros y argumentos. El Capítulo 03 completa el primer recorrido de ida y vuelta con valores de retorno, `None`, retornos por rama y la diferencia entre retornar e imprimir. El Capítulo 04 añade alcance local y global, búsqueda de nombres, sombreado, comportamiento de alcance de sentencias ordinarias y uso cauteloso de `global`. El Capítulo 05 añade type hints de parámetros y retorno, anotaciones de colecciones, uniones con `None` y la diferencia fundamental entre información estática de tipos y enforcement en runtime. El Capítulo 06 añade valores predeterminados, reemplazos selectivos, evaluación al definir la función y el patrón seguro con `None` para crear objetos mutables nuevos. El Capítulo 07 añade recolección de cantidades variables de argumentos posicionales y por palabra clave con `*args` y `**kwargs`, sus modelos de tupla/diccionario, firmas mixtas simples y el límite entre recolección en la definición y desempaquetado posterior en la llamada. El Capítulo 08 conecta esas habilidades individuales componiendo funciones auxiliares y coordinadoras, pasando resultados retornados entre pasos, exponiendo dependencias mediante parámetros y leyendo grafos simples de llamadas. El Capítulo 09 cierra la fase siguiendo el flujo llamador-parámetro-retorno, los vínculos locales de parámetros, reasignación frente a mutación, resultados en tupla y `None`, pipelines explícitos y la diferencia entre grafos de llamadas y seguimientos de flujo de datos.

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

## Ruta completa

Comienza con [01. Definir y Llamar Funciones](01-defining-and-calling-functions/README.es.md), continúa con [02. Parámetros y Argumentos](02-parameters-and-arguments/README.es.md), luego estudia [03. Valores de Retorno](03-return-values/README.es.md), [04. Alcance](04-scope/README.es.md), [05. Type Hints](05-type-hints/README.es.md), [06. Valores Predeterminados](06-default-values/README.es.md), [07. `*args` y `**kwargs`](07-args-and-kwargs/README.es.md), [08. Funciones Trabajando Juntas](08-functions-working-together/README.es.md) y [09. Flujo de Datos Entre Funciones](09-data-flow-between-functions/README.es.md).

Después de completar los nueve capítulos, continúa con la ya publicada [Fase 6: Comentarios, Documentación y Código Limpio](../comments-and-documentation/README.es.md).

**La Fase 5 está completada con nueve capítulos revisados disponibles.**
