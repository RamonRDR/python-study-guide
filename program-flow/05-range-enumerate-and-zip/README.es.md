<div align="center">

# `range()`, `enumerate()` y `zip()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Flujo del Programa](../README.es.md) · [← Anterior: Bucles `for` e Iteración](../04-for-loops-and-iteration/README.es.md)

Un bucle `for` simple suele ser suficiente cuando solo necesitas cada elemento. A veces, sin embargo, el bucle también necesita **números, posiciones o elementos de más de un iterable**.

Este capítulo presenta tres funciones incorporadas que hacen explícitas esas intenciones: `range()`, `enumerate()` y `zip()`.

**Tiempo estimado de estudio:** 105–130 minutos.

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- explicar cuándo la iteración directa es más clara que usar una ayuda de iteración;
- crear progresiones numéricas con `range()`;
- explicar por qué el valor `stop` de `range()` queda excluido;
- usar `start`, `stop` y `step` deliberadamente;
- crear rangos descendentes con un paso negativo;
- reconocer rangos vacíos y el caso inválido de paso cero;
- explicar por qué un objeto `range` no es una lista materializada;
- usar `enumerate()` cuando se necesitan posición y elemento;
- elegir un valor `start` apropiado para `enumerate()`;
- desempaquetar directamente en el bucle `for` los pares producidos por `enumerate()`;
- usar `zip()` para recorrer varios iterables en paralelo;
- explicar el comportamiento predeterminado de `zip()` con el iterable más corto;
- usar `strict=True` cuando longitudes iguales forman parte de la expectativa del programa;
- reconocer que `zip(strict=True)` se añadió en Python 3.10;
- distinguir la secuencia reutilizable `range` de los iteradores devueltos por `enumerate()` y `zip()`;
- combinar ayudas de iteración sin ocultar la intención del bucle;
- elegir entre iteración directa, `range()`, `enumerate()` y `zip()` según la información que realmente necesita el bucle.

## 1. Por qué existen las ayudas de iteración

El capítulo anterior estableció el patrón básico:

```python
for item in iterable:
    statement
```

Esta sigue siendo la forma preferida cuando el cuerpo solo necesita cada elemento.

Pero algunos bucles necesitan información adicional:

- una progresión numérica → `range()`;
- posición + elemento → `enumerate()`;
- elementos paralelos → `zip()`.

Estas herramientas no reemplazan `for`. Proporcionan un iterable más adecuado para que el bucle `for` lo consuma.

## 2. Empieza con la herramienta más simple que coincida con la intención

Supón que solo necesitas los nombres de los temas:

```python
topics = ["conditions", "loops", "helpers"]

for topic in topics:
    print(topic)
```

No añadas índices solo porque existan.

Una regla útil para este capítulo es:

**Pregunta qué información necesita el cuerpo del bucle y luego elige el iterable que proporcione exactamente esa información.**

## 3. Qué es `range()`

`range()` representa una secuencia inmutable de enteros que siguen una progresión regular.

La forma más simple es:

```python
range(stop)
```

Por ejemplo:

```python
for number in range(5):
    print(number)
```

Salida:

```text
0
1
2
3
4
```

La progresión comienza en `0` de forma predeterminada.

## 4. El valor `stop` queda excluido

En:

```python
range(5)
```

`5` es el límite de parada, no un elemento incluido.

Los valores representados son:

```text
0, 1, 2, 3, 4
```

Este diseño de intervalo semiabierto se conecta naturalmente con la indexación desde cero. Una secuencia con cinco elementos tiene índices válidos de `0` a `4`.

## 5. `range(start, stop)`

Puedes proporcionar un valor inicial distinto:

```python
for number in range(2, 7):
    print(number)
```

Salida:

```text
2
3
4
5
6
```

El inicio se incluye cuando pertenece a la progresión. El límite de parada sigue excluido.

## 6. `range(start, stop, step)`

El tercer argumento controla el paso entre valores:

```python
for number in range(0, 10, 3):
    print(number)
```

Salida:

```text
0
3
6
9
```

El paso predeterminado es `1`.

## 7. Un paso negativo crea una progresión descendente

Para avanzar hacia abajo, el paso debe ser negativo:

```python
for number in range(5, 0, -1):
    print(number)
```

Salida:

```text
5
4
3
2
1
```

De nuevo, el límite `0` queda excluido.

## 8. La dirección y el paso deben concordar

Un paso positivo avanza hacia arriba. Un paso negativo avanza hacia abajo.

Con un paso positivo, el rango queda vacío cuando `start >= stop`. Con un paso negativo, el rango queda vacío cuando `start <= stop`. La progresión no necesita caer exactamente en `stop`; ese límite sigue excluido.

```python
print(list(range(5, 0)))
print(list(range(0, 5, -1)))
```

Salida:

```text
[]
[]
```

Este es un comportamiento normal, no un error.

## 9. Un paso cero es inválido

Un paso de cero nunca podría avanzar hacia un límite, por lo que Python lo rechaza:

```python
range(0, 5, 0)
```

Esto lanza `ValueError`.

El manejo de excepciones se enseña más adelante en la guía. Por ahora, recuerda la regla:

**`step` puede ser positivo o negativo, pero no cero.**

## 10. `range()` espera argumentos semejantes a enteros

Para código de principiantes, trata `start`, `stop` y `step` como valores enteros.

Esto es válido:

```python
range(0, 10, 2)
```

Esto no es una herramienta para progresiones de punto flotante:

```python
range(0, 1, 0.1)
```

Pasar valores `float` normales de esta manera lanza `TypeError`.

## 11. Un objeto `range` no es una lista

Imprimir un range directamente lo deja visible:

```python
numbers = range(5)

print(numbers)
print(type(numbers))
```

Salida:

```text
range(0, 5)
<class 'range'>
```

`range()` no construye por adelantado una lista con todos los enteros.

## 12. `range` es una secuencia inmutable y un iterable

Un objeto `range` puede usarse directamente en `for` porque es iterable:

```python
for number in range(3):
    print(number)
```

También se comporta como una secuencia de formas útiles:

```python
numbers = range(10, 20, 2)

print(len(numbers))
print(numbers[0])
print(numbers[-1])
print(14 in numbers)
```

Salida:

```text
5
10
18
True
```

No necesitas convertir un range en una lista solo para iterar sobre él.

## 13. Convierte a lista cuando realmente necesitas una lista

La conversión puede ser útil para inspección o cuando el código posterior necesita realmente una lista mutable:

```python
numbers = list(range(1, 6))
print(numbers)
```

Salida:

```text
[1, 2, 3, 4, 5]
```

No materialices una lista automáticamente cuando el propio objeto `range` ya expresa la progresión que necesitas.

## 14. Usa `range()` cuando los números mismos importen

Un buen caso de uso es una progresión fija de números de intento:

```python
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
```

Salida:

```text
Attempt 1
Attempt 2
Attempt 3
```

Aquí los números son una parte significativa de la salida, por lo que `range()` comunica bien la intención.

## 15. La iteración directa es más clara cuando solo importan los valores

Supón que tienes:

```python
topics = ["conditions", "loops", "helpers"]
```

Esto es directo y claro:

```python
for topic in topics:
    print(topic)
```

Esta versión añade una indirección innecesaria cuando el índice no se usa para nada más:

```python
for index in range(len(topics)):
    print(topics[index])
```

Ambas pueden funcionar, pero la primera expresa de forma más directa lo que significa el programa: procesar cada tema.

## 16. `range(len(sequence))` todavía tiene usos legítimos

A veces el índice en sí es necesario, como al asignar de nuevo a una posición específica:

```python
scores = [70, 80, 90]

for index in range(len(scores)):
    scores[index] = scores[index] + 5

print(scores)
```

Salida:

```text
[75, 85, 95]
```

La pregunta importante no es si `range(len(...))` está prohibido. Es si el índice realmente forma parte de la tarea.

## 17. Qué es `enumerate()`

Cuando necesitas tanto la posición como el elemento, `enumerate()` suele expresar esa intención de forma más directa.

```python
topics = ["conditions", "loops", "helpers"]

for index, topic in enumerate(topics):
    print(index, topic)
```

Salida:

```text
0 conditions
1 loops
2 helpers
```

`enumerate()` produce pares que contienen una cuenta y un elemento.

## 18. `enumerate()` empieza en cero de forma predeterminada

La cuenta predeterminada sigue la convención familiar de base cero:

```python
letters = ["A", "B", "C"]

for index, letter in enumerate(letters):
    print(index, letter)
```

Salida:

```text
0 A
1 B
2 C
```

Usa ese valor predeterminado cuando la cuenta represente índices normales de Python.

## 19. Usa `start=` cuando la numeración mostrada tenga otro significado

La numeración orientada a personas suele comenzar en uno:

```python
topics = ["conditions", "loops", "helpers"]

for position, topic in enumerate(topics, start=1):
    print(f"{position}. {topic}")
```

Salida:

```text
1. conditions
2. loops
3. helpers
```

Los elementos no cambiaron de posición dentro de la lista. Solo el contador producido por `enumerate()` comienza en `1`.

## 20. `enumerate()` funciona con iterables, no solo listas

También se puede enumerar una string:

```python
for position, letter in enumerate("loop", start=1):
    print(position, letter)
```

Salida:

```text
1 l
2 o
3 o
4 p
```

La misma idea se aplica a muchos otros iterables.

## 21. Los pares de `enumerate()` son desempaquetados por el objetivo del bucle

Este bucle:

```python
for index, topic in enumerate(["conditions", "loops"]):
    print(index, topic)
```

usa el comportamiento de desempaquetado que ya aprendiste.

Cada elemento producido tiene dos componentes: `(cuenta, elemento)`.

El objetivo del bucle asigna el primer componente a `index` y el segundo a `topic`.

## 22. Prefiere `enumerate()` a un contador manual cuando coincide con la tarea

Un contador manual puede funcionar:

```python
position = 1

for topic in ["conditions", "loops", "helpers"]:
    print(position, topic)
    position = position + 1
```

Pero cuando el objetivo es simplemente asociar cada elemento con una cuenta, esto es más directo:

```python
for position, topic in enumerate(
    ["conditions", "loops", "helpers"],
    start=1,
):
    print(position, topic)
```

`enumerate()` mantiene la responsabilidad de contar dentro de la herramienta de iteración en lugar de dispersarla por el cuerpo del bucle.

## 23. Qué es `zip()`

`zip()` combina elementos de varios iterables en paralelo.

```python
topics = ["conditions", "loops", "helpers"]
minutes = [25, 40, 30]

for topic, duration in zip(topics, minutes):
    print(topic, duration)
```

Salida:

```text
conditions 25
loops 40
helpers 30
```

El primer tema se empareja con la primera duración, el segundo con la segunda y así sucesivamente.

## 24. `zip()` produce tuplas

Puedes inspeccionar los elementos emparejados convirtiendo el resultado en una lista:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

print(list(zip(names, scores)))
```

Salida:

```text
[('Ari', 82), ('Mina', 91)]
```

Cada elemento producido por `zip()` es una tupla.

Por eso un bucle puede desempaquetarlo de forma natural:

```python
for name, score in zip(names, scores):
    print(name, score)
```

## 25. `zip()` acepta más de dos iterables

La iteración paralela no está limitada a pares:

```python
names = ["Ari", "Mina"]
scores = [82, 91]
levels = ["review", "advance"]

for name, score, level in zip(names, scores, levels):
    print(name, score, level)
```

Salida:

```text
Ari 82 review
Mina 91 advance
```

Usa tantas fuentes paralelas como la tarea realmente necesite, pero recuerda que muchas listas paralelas pueden volverse difíciles de mantener. Un diccionario o un registro estructurado puede modelar los datos con más claridad en algunos casos.

## 26. Por defecto, `zip()` se detiene en el iterable más corto

Este comportamiento es importante:

```python
names = ["Ari", "Mina", "Leo"]
scores = [82, 91]

print(list(zip(names, scores)))
```

Salida:

```text
[('Ari', 82), ('Mina', 91)]
```

`"Leo"` no se incluye porque el iterable de puntuaciones terminó primero.

El truncamiento predeterminado puede ser intencional, pero también puede ocultar un error de alineación de datos.

## 27. Usa `strict=True` cuando se requieran longitudes iguales

Si el programa espera que todos los iterables de entrada tengan longitudes iguales, haz explícita esa expectativa:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

for name, score in zip(names, scores, strict=True):
    print(name, score)
```

Salida:

```text
Ari 82
Mina 91
```

Si un iterable termina antes que otro, `zip(..., strict=True)` lanza `ValueError` en lugar de truncar silenciosamente.

El argumento `strict` se añadió en Python 3.10.

## 28. Este capítulo no requiere manejo de excepciones

Debes comprender qué garantiza `strict=True` sin necesidad de capturar el error todavía.

Por ahora, usa esta orientación:

- una diferencia de longitud es aceptable → el `zip()` predeterminado puede ser intencional;
- las longitudes deben coincidir → prefiere `zip(..., strict=True)`.

Fases posteriores enseñan `try` y `except` para programas que necesiten recuperarse de excepciones de forma deliberada.

## 29. `zip()` funciona con iterables en general

Los argumentos no tienen que ser listas:

```python
letters = "ABC"
numbers = range(1, 4)

for letter, number in zip(letters, numbers, strict=True):
    print(letter, number)
```

Salida:

```text
A 1
B 2
C 3
```

Esto funciona porque tanto `str` como `range` son iterables.

## 30. `range` es reutilizable; `enumerate()` y `zip()` devuelven iteradores

Esta es una conexión importante con el capítulo anterior.

Un objeto `range` es una secuencia, por lo que iterar sobre él no consume el objeto de forma permanente:

```python
numbers = range(3)

print(list(numbers))
print(list(numbers))
```

Salida:

```text
[0, 1, 2]
[0, 1, 2]
```

En cambio, los objetos devueltos por `enumerate()` y `zip()` son iteradores. Una vez agotados, el mismo iterador no se reinicia automáticamente:

```python
pairs = zip(["A", "B"], [1, 2])

print(list(pairs))
print(list(pairs))
```

Salida:

```text
[('A', 1), ('B', 2)]
[]
```

Si necesitas otra pasada, crea un nuevo objeto `enumerate()` o `zip()` a partir de los iterables originales.

## 31. Combina ayudas cuando la intención combinada siga siendo clara

A veces necesitas tanto una posición mostrada como datos alineados de varios iterables:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

for position, (name, score) in enumerate(
    zip(names, scores, strict=True),
    start=1,
):
    print(position, name, score)
```

Salida:

```text
1 Ari 82
2 Mina 91
```

Esto funciona porque:

1. `zip()` produce tuplas `(name, score)`;
2. `enumerate()` empareja cada tupla con una cuenta;
3. el objetivo del bucle desempaqueta ambas capas.

Usa combinaciones así solo cuando sigan siendo legibles para el público previsto.

## 32. Elige la ayuda según la intención

| Necesidad | Prefiere |
|---|---|
| Solo cada valor | `for item in iterable` directo |
| Progresión numérica | `range()` |
| Posición y valor | `enumerate()` |
| Valores paralelos | `zip()` |
| Valores paralelos que deben alinearse exactamente | `zip(..., strict=True)` |

Estas son orientaciones de claridad, no restricciones del lenguaje Python.

## 33. Errores comunes

### Error 1: esperar que `stop` se incluya

```python
print(list(range(1, 5)))
```

Salida:

```text
[1, 2, 3, 4]
```

### Error 2: usar un paso con la dirección incorrecta

```python
print(list(range(5, 0, 1)))
```

Salida:

```text
[]
```

### Error 3: usar `range(len(...))` cuando el índice es innecesario

```python
for index in range(len(topics)):
    print(topics[index])
```

Si el cuerpo solo necesita cada tema, la iteración directa es más clara.

### Error 4: confundir `enumerate(start=1)` con cambiar los índices de la lista

El contador puede empezar en `1`, pero la lista subyacente sigue utilizando sus índices normales desde cero.

### Error 5: asumir que `zip()` predeterminado valida longitudes iguales

No lo hace. `zip()` predeterminado se detiene en el iterable más corto.

### Error 6: reutilizar un iterador `zip()` o `enumerate()` ya agotado

Crea un nuevo objeto auxiliar cuando necesites otra pasada completa.

## 34. Ejemplo desarrollado: `range_progressions.py`

```python
print(list(range(5)))
print(list(range(2, 7)))
print(list(range(0, 10, 3)))
print(list(range(5, 0, -1)))
```

Salida:

```text
[0, 1, 2, 3, 4]
[2, 3, 4, 5, 6]
[0, 3, 6, 9]
[5, 4, 3, 2, 1]
```

Ejemplo del repositorio: [`examples/range_progressions.py`](examples/range_progressions.py)

## 35. Ejemplo desarrollado: `enumerate_positions.py`

```python
topics = ["conditions", "loops", "helpers"]

for position, topic in enumerate(topics, start=1):
    print(f"{position}. {topic}")
```

Salida:

```text
1. conditions
2. loops
3. helpers
```

Ejemplo del repositorio: [`examples/enumerate_positions.py`](examples/enumerate_positions.py)

## 36. Ejemplo desarrollado: `zip_parallel_iteration.py`

```python
topics = ["conditions", "loops", "helpers"]
minutes = [25, 40, 30]

for topic, duration in zip(topics, minutes, strict=True):
    print(f"{topic}: {duration} min")
```

Salida:

```text
conditions: 25 min
loops: 40 min
helpers: 30 min
```

Ejemplo del repositorio: [`examples/zip_parallel_iteration.py`](examples/zip_parallel_iteration.py)

## 37. Ejercicio

Crea una pequeña agenda de estudio con estas dos listas alineadas:

```python
topics = ["strings", "collections", "flow"]
minutes = [20, 35, 30]
```

Tu programa debe:

1. usar `zip(..., strict=True)` para mantener cada tema alineado con su duración;
2. usar `enumerate(..., start=1)` para numerar las filas desde uno;
3. imprimir una línea para cada bloque de estudio con esta forma:

```text
1. strings - 20 min
2. collections - 35 min
3. flow - 30 min
```

Luego crea por separado una cuenta regresiva con `range()` que imprima:

```text
3
2
1
Start
```

No uses `while`, `break`, `continue` ni una comprehension.

## 38. Lista de revisión

Antes de continuar, confirma que puedes explicar cada afirmación sin ejecutar el código:

- [ ] `range(stop)` comienza en cero por defecto.
- [ ] el límite `stop` queda excluido.
- [ ] `range(start, stop, step)` admite pasos positivos y negativos.
- [ ] un paso cero lanza `ValueError`.
- [ ] `range` representa una secuencia inmutable en lugar de una lista preconstruida.
- [ ] la iteración directa es más clara cuando solo se necesita el valor del elemento.
- [ ] `enumerate()` proporciona una cuenta junto con cada elemento.
- [ ] `enumerate(..., start=1)` cambia el contador, no los índices de la colección subyacente.
- [ ] `zip()` combina elementos de iterables en paralelo.
- [ ] `zip()` predeterminado se detiene cuando se agota el iterable más corto.
- [ ] `zip(..., strict=True)` lanza `ValueError` cuando las longitudes difieren.
- [ ] el argumento `strict` existe en Python 3.10 y posteriores.
- [ ] `range` es reutilizable como secuencia.
- [ ] `enumerate()` y `zip()` devuelven iteradores que pueden agotarse.
- [ ] las ayudas de iteración pueden combinarse cuando el resultado siga siendo legible.

## 39. Referencia rápida

| Necesidad | Forma típica |
|---|---|
| Contar desde cero hasta antes de `stop` | `range(stop)` |
| Elegir inicio y fin | `range(start, stop)` |
| Elegir un paso | `range(start, stop, step)` |
| Contar hacia abajo | `range(start, stop, -1)` u otro paso negativo |
| Posición y elemento | `enumerate(iterable)` |
| Numeración orientada a personas | `enumerate(iterable, start=1)` |
| Iteración paralela | `zip(first, second)` |
| Exigir longitudes iguales | `zip(first, second, strict=True)` |
| Solo cada elemento | `for item in iterable` directo |

Recuerda la progresión:

**iteración de elementos → progresión numérica → posición + elemento → elementos paralelos → regla explícita de alineación**

## Siguiente paso

El siguiente capítulo es **Bucles `while` y Repetición Guiada por Estado**.

Ahora sabes repetir trabajo para elementos y dar forma a la iteración cuando el bucle necesita números, posiciones o valores alineados. A continuación, la guía presenta repetición controlada por una **condición Booleana**, en lugar de por el agotamiento de un iterable.

## Referencias oficiales

- [Tutorial de Python 3.13: La función `range()`](https://docs.python.org/3.13/tutorial/controlflow.html#the-range-function)
- [Tutorial de Python 3.13: Técnicas de iteración](https://docs.python.org/3.13/tutorial/datastructures.html#looping-techniques)
- [Funciones incorporadas de Python 3.13: `enumerate()` y `zip()`](https://docs.python.org/3.13/library/functions.html)
- [Tipos incorporados de Python 3.13: Ranges](https://docs.python.org/3.13/library/stdtypes.html#typesseq-range)
