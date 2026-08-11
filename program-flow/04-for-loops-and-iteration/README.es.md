<div align="center">

# Bucles `for` e Iteración

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Flujo del Programa](../README.es.md) · [← Anterior: `match` y `case`](../03-match-and-case/README.es.md)

Los capítulos anteriores enseñaron a Python a **elegir** qué debe ejecutarse. Un bucle `for` introduce un tipo diferente de control de flujo: **repetir un bloque una vez por cada elemento proporcionado por un iterable**.

Aquí las colecciones dejan de ser solamente valores que inspeccionas y empiezan a funcionar como flujos de trabajo que el programa puede procesar un elemento a la vez.

**Tiempo estimado de estudio:** 105–130 minutos.

## Objetivos de aprendizaje

Al terminar este capítulo, deberías poder:

- explicar la diferencia entre selección y repetición;
- explicar qué significa iteración;
- escribir un bucle `for` básico con sintaxis e indentación correctas;
- identificar el objetivo del bucle y el iterable en una sentencia `for`;
- explicar qué es un iterable a un nivel apropiado para principiantes;
- reconocer que Python crea y consume automáticamente un iterador para un bucle `for`;
- iterar sobre listas, tuplas, strings, diccionarios y conjuntos;
- explicar las garantías de orden, o la ausencia de ellas, de esos tipos iterables;
- iterar sobre claves, valores y pares clave-valor de diccionarios;
- desempaquetar elementos con varias partes directamente en el objetivo de un `for`;
- combinar `for` con una sentencia `if`;
- construir una nueva colección a partir de elementos seleccionados sin usar una comprehension;
- usar bucles anidados cuando una tarea repetida realmente pertenece dentro de otra;
- explicar qué sucede cuando un iterable está vacío;
- evitar depender del objetivo del bucle como variable de resultado después del bucle;
- evitar modificar la estructura de la misma colección mientras se itera sobre ella;
- reconocer cuándo `for` es apropiado y cuándo una herramienta de flujo posterior expresará mejor la intención.

## 1. De la selección a la repetición

Una sentencia `if` elige si un bloque se ejecuta. Una sentencia `match` elige un bloque según un patrón.

Un bucle `for` responde una pregunta diferente:

**¿Qué debe hacer Python para cada elemento?**

Supón que una lista contiene tres temas:

```python
topics = ["conditions", "patterns", "loops"]
```

Sin un bucle, podrías escribir:

```python
print(topics[0])
print(topics[1])
print(topics[2])
```

Eso funciona solamente porque ya conoces exactamente el tamaño y las posiciones.

Un bucle `for` expresa la relación directamente:

```python
for topic in topics:
    print(topic)
```

Salida:

```text
conditions
patterns
loops
```

El bucle dice: para cada elemento proporcionado por `topics`, llama temporalmente a ese elemento `topic` y ejecuta el bloque indentado.

## 2. Sintaxis básica

La forma para principiantes es:

```python
for item in iterable:
    statement
```

Tiene cuatro partes importantes:

1. `for` inicia el bucle;
2. `item` es el objetivo que recibe cada valor;
3. `in` conecta el objetivo con la fuente de elementos;
4. `iterable` es el objeto capaz de proporcionar elementos uno a la vez.

Los dos puntos cierran la cabecera del bucle. El bloque indentado es el cuerpo del bucle.

Un ejemplo real:

```python
colors = ["blue", "green", "orange"]

for color in colors:
    print(f"Color: {color}")
```

Salida:

```text
Color: blue
Color: green
Color: orange
```

## 3. Un bucle, paso a paso

Considera:

```python
levels = ["beginner", "intermediate", "advanced"]

for level in levels:
    print(level)
```

Un seguimiento mental útil es:

```text
first item  -> level = "beginner"     -> run the body
second item -> level = "intermediate" -> run the body
third item  -> level = "advanced"     -> run the body
no more items -> leave the loop
```

Python no ejecuta toda la colección de una vez. Cada iteración asigna un elemento al objetivo y luego ejecuta el cuerpo.

## 4. El `for` de Python está orientado por elementos

Un bucle `for` en Python trata fundamentalmente de **elementos provenientes de un iterable**.

Eso es diferente de la idea clásica de bucle al estilo C, cuya cabecera contiene manualmente:

- un contador inicial;
- una condición;
- una expresión de incremento.

En este capítulo, no pienses:

```text
repeat three times
```

Piensa:

```text
for each item supplied by this iterable
```

Cuando el objetivo real sea producir una progresión numérica o seguir posiciones explícitamente, el siguiente capítulo introducirá `range()` y `enumerate()`.

## 5. Qué es un iterable

Un **iterable** es un objeto capaz de proporcionar sus miembros uno a la vez.

Ya conoces varios tipos iterables:

- `list`;
- `tuple`;
- `str`;
- `dict`;
- `set`.

Eso significa que todos pueden aparecer después de `in` en un bucle `for`.

La palabra iterable **no** significa "lista". Una lista es solamente un tipo de iterable.

Esta distinción importa porque la misma sintaxis de `for` funciona con muchos tipos diferentes de objetos.

## 6. Iterable frente a iterador

La terminología de Python distingue un **iterable** de un **iterador**.

Para un principiante, un modelo mental práctico es:

```text
iterable = source that can provide items
iterator = object Python uses to obtain the next item from that source
```

Cuando comienza un bucle `for`, Python obtiene un iterador para el iterable y sigue pidiendo el siguiente elemento hasta que no quedan más.

Normalmente **no** necesitas llamar a `iter()` o `next()` por tu cuenta para escribir un bucle `for`. La sentencia maneja ese protocolo por ti.

Temas posteriores podrán explorar los iteradores directamente. Por ahora, entiende por qué la palabra **iterable** es más amplia que colección o secuencia.

## 7. El objetivo del bucle es un objetivo de asignación

En este bucle:

```python
scores = [72, 81, 90]

for score in scores:
    print(score)
```

`score` recibe un nuevo elemento en cada iteración.

Conceptualmente:

```text
score = 72
run body
score = 81
run body
score = 90
run body
```

Esto conecta los bucles con un concepto que ya conoces: la asignación.

El objetivo del bucle no es un placeholder mágico de solo lectura. Es un objetivo normal de asignación que Python actualiza a medida que avanza la iteración.

## 8. La indentación define el cuerpo del bucle

Como en `if` y `match`, la indentación forma parte de la sintaxis.

```python
names = ["Ana", "Mina"]

for name in names:
    print(f"Hello, {name}")
    print("Inside the loop")

print("After the loop")
```

Salida:

```text
Hello, Ana
Inside the loop
Hello, Mina
Inside the loop
After the loop
```

Las dos llamadas `print()` indentadas se ejecutan para cada nombre. El `print()` final se ejecuta una vez después de terminar la iteración.

La guía usa cuatro espacios por nivel de indentación, siguiendo PEP 8.

## 9. Iterar sobre una lista

Las listas son un primer caso de uso natural porque contienen una secuencia de elementos:

```python
topics = ["strings", "collections", "flow"]

for topic in topics:
    print(f"Review: {topic}")
```

Salida:

```text
Review: strings
Review: collections
Review: flow
```

La iteración de una lista sigue el orden de la lista.

No necesitas índices cuando el objetivo es simplemente procesar cada valor.

## 10. Iterar sobre una tupla

Las tuplas también son iterables:

```python
coordinates = (4, -2)

for coordinate in coordinates:
    print(coordinate)
```

Salida:

```text
4
-2
```

La inmutabilidad de una tupla no impide la iteración. Inmutabilidad significa que la estructura de la tupla no puede modificarse mediante asignación de elementos; no significa que sus elementos no puedan leerse uno a la vez.

La iteración de una tupla sigue el orden de la tupla.

## 11. Iterar sobre un string

Un string es una secuencia iterable de caracteres:

```python
word = "loop"

for letter in word:
    print(letter)
```

Salida:

```text
l
o
o
p
```

Los dos caracteres `o` aparecen porque la iteración procesa posiciones del string, no solamente valores distintos.

La iteración de un string sigue el orden de sus caracteres.

## 12. Los valores repetidos siguen siendo elementos repetidos

Un bucle no elimina duplicados automáticamente.

```python
scores = [80, 90, 80]

for score in scores:
    print(score)
```

Salida:

```text
80
90
80
```

El primer y el tercer elemento tienen valores iguales, pero siguen siendo elementos separados en la secuencia de la lista.

Si la unicidad es la relación importante, un conjunto puede ser una colección más apropiada. Esa es una decisión del modelo de datos, no un comportamiento especial de `for`.

## 13. Un iterable vacío ejecuta el cuerpo cero veces

Un bucle `for` no exige al menos una iteración.

```python
topics = []

for topic in topics:
    print(topic)

print("Finished")
```

Salida:

```text
Finished
```

No había elementos para asignar a `topic`, por lo que el cuerpo del bucle nunca se ejecutó.

Esta es una propiedad importante: **cero iteraciones es normal**.

## 14. Iterar sobre un diccionario proporciona claves por defecto

Un diccionario es iterable, pero su iteración predeterminada produce las claves:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic in lesson_minutes:
    print(topic)
```

Salida:

```text
conditions
patterns
loops
```

Esto es equivalente en intención a iterar sobre `lesson_minutes.keys()`.

En Python 3.7 y versiones posteriores, el orden de inserción de los diccionarios está garantizado por el lenguaje. Por eso, las claves anteriores aparecen en el orden en que se insertaron esas entradas.

## 15. Iterar sobre valores de un diccionario

Si no necesitas las claves, `.values()` proporciona los valores:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for minutes in lesson_minutes.values():
    print(minutes)
```

Salida:

```text
25
35
40
```

Elige el iterable según lo que necesite el cuerpo.

## 16. Iterar sobre pares clave-valor de un diccionario

`.items()` proporciona pares clave-valor:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic, minutes in lesson_minutes.items():
    print(f"{topic}: {minutes} min")
```

Salida:

```text
conditions: 25 min
patterns: 35 min
loops: 40 min
```

El objetivo del bucle tiene dos nombres porque cada elemento proporcionado por `.items()` es un par de dos elementos.

## 17. Un objetivo de `for` puede desempaquetar elementos

El ejemplo anterior se conecta directamente con el desempaquetado de tuplas y secuencias de la Fase 3.

```python
records = [
    ("conditions", 25),
    ("patterns", 35),
]

for topic, minutes in records:
    print(topic, minutes)
```

Salida:

```text
conditions 25
patterns 35
```

Para cada par, Python asigna el primer componente a `topic` y el segundo a `minutes`.

La cantidad y la estructura de los nombres del objetivo deben ser compatibles con los elementos que se van a desempaquetar.

## 18. Iterar sobre un conjunto

Los conjuntos son iterables:

```python
topics = {"strings", "collections", "flow"}

for topic in topics:
    print(topic)
```

Sin embargo, un conjunto no tiene un contrato de orden posicional en el que debas confiar.

No escribas código para principiantes que dependa de un orden específico de iteración de conjuntos.

Por eso, este capítulo no documenta un orden exacto de salida para ese ejemplo.

## 19. El iterable determina el orden significativo

`for` por sí mismo no promete una única regla universal de orden.

El iterable proporciona elementos según su propia semántica:

| Iterable | Orden en el que se puede confiar |
|---|---|
| `list` | orden de la secuencia de la lista |
| `tuple` | orden de la secuencia de la tupla |
| `str` | orden de la secuencia de caracteres |
| `dict` | orden de inserción de las claves en Python 3.7+ |
| `dict.values()` | orden de inserción correspondiente |
| `dict.items()` | orden de inserción correspondiente |
| `set` | sin contrato de orden posicional |

Una buena regla es:

**Pregunta qué orden define el iterable, no qué orden define `for`.**

## 20. Combinar `for` con `if`

Las herramientas de flujo de capítulos anteriores pueden trabajar dentro de un bucle:

```python
scores = [52, 81, 67, 90]

for score in scores:
    if score >= 70:
        print(f"Passing: {score}")
```

Salida:

```text
Passing: 81
Passing: 90
```

El bucle controla **qué elemento es el actual**. El `if` controla **qué sucede con ese elemento**.

Esta combinación es una de las bases más comunes del procesamiento de datos.

## 21. Construir una nueva lista durante la iteración

Ya conoces `list.append()`, así que puedes recopilar resultados seleccionados de forma explícita:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)

print(passing_scores)
```

Salida:

```text
[81, 90]
```

Este patrón tiene tres etapas claras:

```text
create destination
    ↓
iterate over source
    ↓
append selected result
```

Las list comprehensions pueden expresar algunas transformaciones de forma más compacta, pero se aplazan intencionalmente hasta que los bucles estén completamente comprendidos.

## 22. Acumular un resultado

Un bucle también puede actualizar un acumulador separado:

```python
minutes = [20, 35, 15]
total = 0

for value in minutes:
    total = total + value

print(total)
```

Salida:

```text
70
```

La distinción importante es:

- `value` es el elemento actual;
- `total` es un estado que sobrevive de una iteración a la siguiente.

Para una suma simple de valores numéricos, `sum()` suele ser más claro y ya lo aprendiste en la Fase 2. Este ejemplo manual existe para mostrar cómo el estado puede cambiar entre iteraciones, no para reemplazar `sum()`.

## 23. Bucles anidados

El cuerpo de un bucle puede contener otro bucle:

```python
groups = [
    ["A", "B"],
    ["C", "D"],
]

for group in groups:
    for item in group:
        print(item)
```

Salida:

```text
A
B
C
D
```

Para cada `group`, el bucle interno completa su iteración sobre ese grupo.

La indentación muestra la relación:

```text
outer item
    ↓
run the complete inner loop
    ↓
move to the next outer item
```

Los bucles anidados son útiles cuando los propios datos tienen estructura anidada. Evita anidar solo porque es posible; cada nivel aumenta la cantidad de flujo que el lector debe seguir.

## 24. Ten cuidado al modificar la colección que estás recorriendo

Cambiar la estructura de la misma colección mientras se itera sobre ella puede producir comportamientos confusos o errores, según la colección y el cambio.

Para código de principiantes, prefiere una de estas estrategias:

- iterar sobre la colección original y construir una nueva colección;
- cuando la mutación sea realmente necesaria, iterar sobre una copia apropiada.

Un patrón claro de filtrado es:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)
```

Aquí el bucle lee `scores`, mientras que las mutaciones ocurren solamente en `passing_scores`.

Esta separación es más fácil de razonar que eliminar o insertar elementos en `scores` mientras se está recorriendo.

## 25. El objetivo del bucle puede seguir existiendo después de un bucle no vacío

Python no elimina automáticamente el nombre del objetivo después de un bucle `for`.

```python
values = [10, 20, 30]

for value in values:
    print(value)

print(f"Last assigned value: {value}")
```

Salida:

```text
10
20
30
Last assigned value: 30
```

Este es un comportamiento real del lenguaje, pero depender del objetivo del bucle como resultado final del programa suele ser poco claro.

También hay un caso límite importante: si el iterable está vacío, el bucle no asignará el objetivo en absoluto.

Prefiere una variable de resultado separada e inicializada deliberadamente cuando el código posterior al bucle necesite un resultado.

## 26. Reasignar el objetivo dentro del cuerpo no controla la iteración

Como Python asigna el siguiente elemento al objetivo del bucle en cada iteración, cambiar ese nombre dentro del cuerpo no le dice al bucle cuál debería ser el siguiente elemento.

```python
values = [1, 2, 3]

for value in values:
    value = value * 10
    print(value)
```

Salida:

```text
10
20
30
```

El cuerpo cambia la asociación actual, pero la siguiente iteración vuelve a asignar a `value` el siguiente elemento de `values`.

Si necesitas un valor transformado, un nombre separado puede dejar la intención más clara:

```python
values = [1, 2, 3]

for value in values:
    transformed = value * 10
    print(transformed)
```

## 27. Cuándo `for` es una buena elección

Usa `for` cuando la idea central sea:

- procesar todos los elementos de una colección;
- inspeccionar caracteres de un texto;
- procesar claves, valores o pares de un diccionario;
- filtrar elementos con un `if` dentro del bucle;
- construir un nuevo resultado a partir de elementos existentes;
- recorrer estructuras iterables anidadas.

La señal más fuerte es que ya tienes, o puedes obtener naturalmente, un iterable cuyos elementos definen la repetición.

## 28. Cuándo otra herramienta puede expresar mejor la intención

No elijas `for` solamente porque haya repetición.

Los capítulos posteriores proporcionan herramientas para intenciones diferentes:

- `range()` para progresiones aritméticas e iteración orientada por conteo;
- `enumerate()` cuando se necesitan posición y elemento;
- `zip()` cuando varios iterables deben avanzar juntos;
- `while` cuando la repetición está controlada por una condición que cambia, no por agotar un iterable;
- `break` y `continue` cuando el flujo del bucle necesita salida anticipada o salto deliberado.

Esta separación mantiene limpio el primer modelo mental: **`for` consume elementos de un iterable**.

## 29. Elige nombres singulares para el objetivo cuando sea posible

Si el nombre de una colección está en plural, un objetivo singular suele hacer evidente la relación:

```python
topics = ["strings", "collections", "flow"]

for topic in topics:
    print(topic)
```

Del mismo modo:

```python
students = ["Ana", "Diego"]

for student in students:
    print(student)
```

Nombres como `x` o `item` son válidos, pero un nombre singular específico del dominio normalmente enseña mejor la intención del código.

## 30. Errores comunes

### Error 1: olvidar los dos puntos

Incorrecto:

```python
for topic in topics
    print(topic)
```

Correcto:

```python
for topic in topics:
    print(topic)
```

### Error 2: olvidar la indentación

Incorrecto:

```python
for topic in topics:
print(topic)
```

Correcto:

```python
for topic in topics:
    print(topic)
```

### Error 3: iterar sobre la parte incorrecta de un diccionario

Esto produce claves:

```python
for item in settings:
    print(item)
```

Si el cuerpo necesita tanto la clave como el valor, usa `.items()`:

```python
for key, value in settings.items():
    print(key, value)
```

### Error 4: asumir el orden de un conjunto

No dependas de que esto produzca un orden posicional elegido:

```python
for topic in {"strings", "collections", "flow"}:
    print(topic)
```

### Error 5: asumir que el cuerpo se ejecutará al menos una vez

Un iterable vacío produce cero ejecuciones del cuerpo.

### Error 6: cambiar la colección fuente mientras la recorres

Prefiere construir una nueva colección o iterar deliberadamente sobre una copia adecuada.

### Error 7: esperar que reasignar el objetivo controle el bucle

La siguiente iteración vuelve a asignar el siguiente elemento del iterador.

### Error 8: recurrir a índices cuando solo se necesitan valores

Si el cuerpo solo necesita cada valor, itera directamente sobre los valores. Las herramientas que manejan posiciones llegan en el siguiente capítulo.

## 31. Límite de alcance de este capítulo

Este capítulo se concentra en la iteración directa, elemento por elemento.

No requiere:

- `range()`;
- `enumerate()`;
- `zip()`;
- bucles `while`;
- `break`;
- `continue`;
- `else` de bucle;
- comprehensions;
- funciones definidas por el usuario;
- manejo de excepciones;
- bibliotecas externas.

La gramática de `for` de Python admite una cláusula `else` opcional, pero esta guía enseña intencionalmente el `else` de bucle junto con `break` más adelante, porque su significado queda más claro cuando se pueden comparar directamente la finalización normal del bucle y la terminación anticipada.

## 32. Ejemplo trabajado: iterar sobre colecciones

El archivo [`examples/collection_iteration.py`](examples/collection_iteration.py) contiene:

```python
topics = ["conditions", "patterns", "loops"]

for topic in topics:
    print(f"Study: {topic}")

coordinates = (4, -2)

for coordinate in coordinates:
    print(f"Coordinate: {coordinate}")

word = "loop"
letters = []

for letter in word:
    letters.append(letter.upper())

print("Letters:", letters)
```

Salida:

```text
Study: conditions
Study: patterns
Study: loops
Coordinate: 4
Coordinate: -2
Letters: ['L', 'O', 'O', 'P']
```

Este ejemplo conecta la iteración de lista, tupla y string con la mutación de listas ya aprendida en fases anteriores.

## 33. Ejemplo trabajado: iteración de diccionarios

El archivo [`examples/dictionary_iteration.py`](examples/dictionary_iteration.py) contiene:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic in lesson_minutes:
    print(f"Topic: {topic}")

for topic, minutes in lesson_minutes.items():
    print(f"{topic}: {minutes} min")
```

Salida:

```text
Topic: conditions
Topic: patterns
Topic: loops
conditions: 25 min
patterns: 35 min
loops: 40 min
```

El primer bucle usa las claves del diccionario. El segundo usa `.items()` y desempaquetado en el objetivo.

## 34. Ejemplo trabajado: filtrar y recopilar

El archivo [`examples/filter_and_collect.py`](examples/filter_and_collect.py) contiene:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)

print("Passing scores:", passing_scores)
print("Passing count:", len(passing_scores))
```

Salida:

```text
Passing scores: [81, 90]
Passing count: 2
```

Este ejemplo combina directamente las cuatro primeras fases:

```text
list of values
    ↓
for each value
    ↓
if the condition is true
    ↓
append the value to a result list
```

## 35. Ejercicio

Crea una lista llamada `study_minutes` que contenga:

```python
[25, 40, 15, 50]
```

Después:

1. crea una lista vacía llamada `long_sessions`;
2. itera sobre `study_minutes` con `for`;
3. si un valor es al menos `30`, añádelo a `long_sessions`;
4. después del bucle, imprime `long_sessions`;
5. imprime su longitud.

Valores finales esperados:

```text
[40, 50]
2
```

Luego explica con tus propias palabras:

- cuál es el iterable;
- cuál es el objetivo del bucle;
- cuántas iteraciones ocurren;
- por qué el bloque `if` se ejecuta menos veces de las que se entra al cuerpo del bucle.

### Práctica extra

Dado:

```python
course = {
    "title": "Python",
    "phase": 4,
    "chapter": 4,
}
```

Escribe un bucle que imprima solamente las claves y luego otro que imprima cada clave y su valor correspondiente usando `.items()`.

Todavía no uses `range()`, `enumerate()`, `zip()` ni una comprehension.

## 36. Lista de revisión

Antes de avanzar, confirma que puedes explicar cada afirmación sin ejecutar el código:

- [ ] `for` repite un bloque para los elementos proporcionados por un iterable.
- [ ] un iterable puede proporcionar elementos uno a la vez.
- [ ] Python administra automáticamente el iterador usado por un bucle `for` normal.
- [ ] el objetivo del bucle recibe un nuevo elemento en cada iteración.
- [ ] un iterable vacío provoca cero ejecuciones del cuerpo.
- [ ] listas, tuplas y strings iteran en el orden de la secuencia.
- [ ] la iteración de diccionarios produce claves por defecto.
- [ ] `.values()` proporciona valores del diccionario.
- [ ] `.items()` proporciona pares clave-valor que pueden desempaquetarse.
- [ ] la iteración de conjuntos no debe tratarse como orden posicional.
- [ ] un `if` dentro de un bucle puede tomar una decisión para cada elemento actual.
- [ ] una lista de destino separada puede recopilar resultados seleccionados de forma segura.
- [ ] los bucles anidados son apropiados cuando el trabajo repetido sigue una estructura de datos anidada.
- [ ] modificar la misma colección mientras se recorre suele ser una mala estrategia para principiantes.
- [ ] el objetivo del bucle puede seguir existiendo después de un bucle no vacío, pero no debe tratarse como una variable de resultado confiable.
- [ ] `range()`, `enumerate()` y `zip()` pertenecen al siguiente capítulo.

## 37. Referencia rápida

| Necesidad | Forma típica |
|---|---|
| Iterar sobre valores | `for item in iterable:` |
| Iterar sobre una lista | `for item in items:` |
| Iterar sobre caracteres de texto | `for character in text:` |
| Iterar sobre claves de diccionario | `for key in mapping:` |
| Iterar sobre valores de diccionario | `for value in mapping.values():` |
| Iterar sobre pares clave-valor | `for key, value in mapping.items():` |
| Decidir por elemento | `for item in items:` con un `if` interno |
| Construir una lista filtrada | inicializa `result = []` y usa `append()` para los elementos seleccionados |
| Recorrer colecciones anidadas | bucles `for` anidados |
| No hay elementos disponibles | el cuerpo del bucle se ejecuta cero veces |

Recuerda la progresión:

**iterable → next item → assign target → run body → repeat until exhausted**

## Siguiente paso

El siguiente capítulo es **`range()`, `enumerate()` y `zip()`**.

Ahora sabes procesar elementos directamente. A continuación, la guía añade herramientas para generar progresiones numéricas, mantener posiciones junto a los elementos y avanzar por varios iterables al mismo tiempo.

## Referencias oficiales

- [Python 3.13 tutorial: `for` Statements](https://docs.python.org/3.13/tutorial/controlflow.html#for-statements)
- [Python 3.13 language reference: The `for` statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-for-statement)
- [Python 3.13 glossary: iterable](https://docs.python.org/3.13/glossary.html#term-iterable)
- [Python 3.13 glossary: iterator](https://docs.python.org/3.13/glossary.html#term-iterator)
- [Python 3.13 tutorial: Looping Techniques](https://docs.python.org/3.13/tutorial/datastructures.html#looping-techniques)
- [PEP 8: Indentation](https://peps.python.org/pep-0008/#indentation)
