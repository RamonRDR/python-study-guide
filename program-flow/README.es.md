<div align="center">

# Flujo del Programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Ruta completa de aprendizaje](../docs/learning-path.es.md) · [Roadmap](../docs/roadmap.es.md)

Flujo del Programa es la Fase 4 de la secuencia principal de aprendizaje de Python Study Guide.

Las fases anteriores enseñaron cómo se crean, inspeccionan, transforman y organizan los valores. Esta fase enseña cómo esos valores influyen en **qué se ejecuta, cuántas veces se ejecuta, cuándo termina una repetición y cómo pueden combinarse deliberadamente las herramientas de flujo**.

## Prerrequisito

Completa primero la [Fase 3: Colecciones](../collections/README.es.md).

Ya deberías sentirte cómodo con:

- variables y tipos de datos incorporados;
- strings y expresiones numéricas;
- valores booleanos y comparaciones básicas;
- listas, tuplas, diccionarios y conjuntos;
- `in` y `not in` como pruebas de pertenencia;
- elección de una colección según la relación entre los valores.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Estado |
|---|---|---|
| [01. Condiciones, Comparaciones y Lógica Booleana](01-conditions-comparisons-and-boolean-logic/README.es.md) | Construir expresiones de verdad confiables antes de usarlas para controlar la ejecución | Disponible |
| [02. `if`, `elif` y `else`](02-if-elif-and-else/README.es.md) | Elegir qué bloque de código se ejecuta | Disponible |
| [03. `match` y `case`: Coincidencia de Patrones Estructurales](03-match-and-case/README.es.md) | Comparar valores y estructuras de datos con patrones | Disponible |
| [04. Bucles `for` e Iteración](04-for-loops-and-iteration/README.es.md) | Repetir trabajo para elementos de un iterable | Disponible |
| [05. `range()`, `enumerate()` y `zip()`](05-range-enumerate-and-zip/README.es.md) | Contar, seguir posiciones y coordinar iteraciones | Disponible |
| [06. Bucles `while` y Repetición Guiada por Estado](06-while-loops-and-state-driven-repetition/README.es.md) | Repetir mientras una condición permanezca verdadera y el estado evolucione | Disponible |
| [07. `break`, `continue` y `else` de Bucles](07-break-continue-and-loop-else/README.es.md) | Terminar antes, omitir una iteración y distinguir finalización normal de `break` | Disponible |
| [08. Elegir y Combinar el Flujo del Programa](08-choosing-and-combining-program-flow/README.es.md) | Seleccionar y combinar herramientas de flujo según la intención | Disponible |

Estudia los capítulos en orden al seguir la ruta completa para principiantes.

## Por qué las condiciones vienen antes de `if`

Una estructura de decisión solo es tan clara como la condición que la controla.

Por eso, esta fase comienza separando dos ideas:

```text
condition = a question Python can interpret for truth
decision = what the program does because of that condition
```

El Capítulo 01 se concentra en la primera idea. El Capítulo 02 usa esas condiciones para seleccionar qué bloque se ejecuta. El Capítulo 03 introduce coincidencia de patrones estructurales cuando la forma o el patrón de un valor es la pregunta importante. El Capítulo 04 avanza de la selección a la repetición guiada por iterable. El Capítulo 05 añade ayudas para progresiones numéricas, posiciones e iteración paralela. El Capítulo 06 añade repetición controlada por estado cambiante. El Capítulo 07 añade salida anticipada deliberada, salto de iteración y manejo de finalización de bucles. El Capítulo 08 cierra la fase eligiendo y combinando todas esas herramientas según la intención.

## Progresión de la fase

```text
conditions
    ↓
decisions
    ↓
pattern matching
    ↓
for each item
    ↓
iteration helpers
    ↓
while a condition holds
    ↓
loop control
    ↓
choose and combine flow
```

## Límite de alcance

La Fase 4 enseña flujo del programa sin convertir temas posteriores en prerrequisitos.

No requiere:

- funciones definidas por el usuario con `def`;
- manejo de excepciones con `try` y `except`;
- manejo de archivos;
- comprehensions como atajo para bucles;
- bibliotecas externas.

Esos conceptos aparecen más adelante en el roadmap.

## Empieza aquí

Empieza con [01. Condiciones, Comparaciones y Lógica Booleana](01-conditions-comparisons-and-boolean-logic/README.es.md).

Después del Capítulo 01, continúa con [02. `if`, `elif` y `else`](02-if-elif-and-else/README.es.md).

Después del Capítulo 02, continúa con [03. `match` y `case`: Coincidencia de Patrones Estructurales](03-match-and-case/README.es.md).

Después del Capítulo 03, continúa con [04. Bucles `for` e Iteración](04-for-loops-and-iteration/README.es.md).

Después del Capítulo 04, continúa con [05. `range()`, `enumerate()` y `zip()`](05-range-enumerate-and-zip/README.es.md).

Después del Capítulo 05, continúa con [06. Bucles `while` y Repetición Guiada por Estado](06-while-loops-and-state-driven-repetition/README.es.md).

Después del Capítulo 06, continúa con [07. `break`, `continue` y `else` de Bucles](07-break-continue-and-loop-else/README.es.md).

Después del Capítulo 07, termina la fase con [08. Elegir y Combinar el Flujo del Programa](08-choosing-and-combining-program-flow/README.es.md).

**La Fase 4 está completada con ocho capítulos revisados.** La siguiente fase de aprendizaje planificada es la Fase 5: Funciones.
