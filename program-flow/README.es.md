<div align="center">

# Flujo del Programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Ruta completa de aprendizaje](../docs/learning-path.es.md) · [Roadmap](../docs/roadmap.es.md)

Flujo del Programa es la Fase 4 de la secuencia principal de aprendizaje de Python Study Guide.

Las fases anteriores enseñaron cómo se crean, inspeccionan, transforman y organizan los valores. Esta fase enseña cómo esos valores empiezan a influir en **qué se ejecuta, cuántas veces se ejecuta y cuándo termina una repetición**.

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
| 07. `break`, `continue` y `else` de Bucles | Cambiar o interpretar la finalización normal de un bucle | Planificado |
| 08. Elegir y Combinar el Flujo del Programa | Seleccionar y combinar herramientas de flujo según la intención | Planificado |

Estudia los capítulos en orden al seguir la ruta completa para principiantes.

## Por qué las condiciones vienen antes de `if`

Una estructura de decisión solo es tan clara como la condición que la controla.

Por eso, esta fase comienza separando dos ideas:

```text
condition = a question Python can interpret for truth
decision = what the program does because of that condition
```

El Capítulo 01 se concentra en la primera idea. El Capítulo 02 añade la segunda usando esas condiciones para seleccionar qué bloque se ejecuta. El Capítulo 03 introduce después la coincidencia de patrones estructurales como otra forma de seleccionar comportamiento cuando la forma o el patrón de un valor es la pregunta importante. El Capítulo 04 cambia de la selección a la repetición al procesar elementos de un iterable uno por uno. El Capítulo 05 añade ayudas para progresiones numéricas, posiciones e iteración paralela. El Capítulo 06 añade repetición controlada por un estado cambiante y por una condición que se vuelve a evaluar antes de cada iteración.

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

El próximo capítulo planificado introduce `break`, `continue` y `else` de bucles.
