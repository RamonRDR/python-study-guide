<div align="center">

# Parámetros y Argumentos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Anterior: Definir y Llamar Funciones](../01-defining-and-calling-functions/README.es.md)

El Capítulo 01 dio un nombre al comportamiento. El Capítulo 02 hace que ese comportamiento **trabaje con diferentes valores de entrada**.

La distinción central es:

```text
parameter = name in the function definition
argument  = value supplied by a function call
```

Este capítulo se centra en parámetros obligatorios y llamadas comunes. Los valores de retorno, valores predeterminados, type hints, `*args`, `**kwargs` y las reglas detalladas de alcance vienen después.

**Tiempo estimado de estudio:** 90–120 minutos.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- distinguir un parámetro de un argumento;
- definir una función con uno o más parámetros obligatorios;
- llamar a la misma función con argumentos diferentes;
- pasar literales, variables, expresiones y colecciones como argumentos;
- explicar cómo los argumentos posicionales se vinculan por posición;
- usar argumentos por palabra clave básicos;
- mezclar argumentos posicionales y por palabra clave en un orden válido;
- elegir nombres significativos para parámetros;
- usar parámetros con la lógica ya conocida de `if`, `for` y `range()`;
- reconocer argumentos faltantes, extra, duplicados e inesperados como errores de llamada;
- seguir los datos de entrada desde el llamador hasta el cuerpo de la función.

## 1. De comportamiento fijo a comportamiento configurable

Una función sin parámetros repite un comportamiento fijo:

```python
def greet():
    print("Hello, Maya!")


greet()
greet()
```

Cada llamada imprime el mismo nombre.

Un parámetro crea un lugar para que el llamador proporcione datos:

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Maya")
greet("Leo")
```

Ahora el comportamiento permanece igual mientras cambia la entrada.

## 2. Parámetro versus argumento

En la definición:

```python
def greet(name):
    print(f"Hello, {name}!")
```

`name` es un **parámetro**.

En la llamada:

```python
greet("Maya")
```

`"Maya"` es un **argumento**.

Mantén este modelo mental:

```text
definition → parameter
call       → argument
```

## 3. Un parámetro obligatorio necesita un argumento

```python
def show_city(city):
    print(f"City: {city}")


show_city("Recife")
```

La llamada proporciona un argumento para un parámetro obligatorio.

Llamar a `show_city()` sin argumento genera `TypeError` porque no se proporcionó la entrada obligatoria.

## 4. La lista de parámetros está dentro de los paréntesis

El Capítulo 01 usó una lista de parámetros vacía:

```python
def show_status():
    print("Ready")
```

El Capítulo 02 coloca nombres dentro de ella:

```python
def show_status(status):
    print(status)
```

Piensa:

```text
()             → no parameters
(status)       → one parameter
(title, year)  → two parameters
```

## 5. Una definición puede recibir muchos valores

```python
def show_language(language):
    print(f"Studying: {language}")


show_language("Python")
show_language("JavaScript")
show_language("SQL")
```

Salida:

```text
Studying: Python
Studying: JavaScript
Studying: SQL
```

La función se define una vez. Cada llamada proporciona un nuevo argumento.

## 6. Los argumentos pueden ser literales

```python
def show_quantity(quantity):
    print(f"Quantity: {quantity}")


show_quantity(3)
```

Aquí `3` es el argumento proporcionado a `quantity`.

## 7. Los argumentos pueden venir de variables

```python
def show_quantity(quantity):
    print(f"Quantity: {quantity}")


items_in_cart = 4
show_quantity(items_in_cart)
```

La variable del llamador y el parámetro no necesitan tener el mismo nombre.

```text
items_in_cart → name in caller code
quantity      → parameter name in function
```

## 8. Los argumentos pueden ser expresiones

Python evalúa una expresión usada como argumento antes de que el cuerpo use el valor resultante.

```python
def show_total(total):
    print(f"Total: {total}")


price = 12
quantity = 3
show_total(price * quantity)
```

Salida:

```text
Total: 36
```

La función recibe el resultado de `price * quantity`.

## 9. Varios parámetros crean varias entradas

Separa los parámetros con comas:

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book("Python Basics", 2026)
```

La definición tiene dos parámetros y la llamada proporciona dos argumentos.

## 10. Los argumentos posicionales se vinculan por posición

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")


show_route("Home", "Library")
```

Vinculación:

```text
origin      ← "Home"
destination ← "Library"
```

El primer argumento posicional va al primer parámetro compatible, el segundo al segundo y así sucesivamente.

## 11. El orden posicional puede cambiar el significado

```python
show_route("Library", "Home")
```

Esa llamada es válida, pero ahora la ruta apunta en la dirección opuesta.

Python sigue la posición. No intenta adivinar tu intención.

## 12. Los argumentos por palabra clave básicos indican el parámetro de destino

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book(title="Python Basics", year=2026)
```

Los argumentos por palabra clave hacen explícito qué parámetro recibe cada valor.

Para parámetros comunes, el orden también puede cambiar cuando todos los argumentos están nombrados:

```python
show_book(year=2026, title="Python Basics")
```

## 13. Las llamadas posicionales y por palabra clave pueden representar la misma entrada

Estas llamadas vinculan los mismos valores:

```python
show_book("Python Basics", 2026)
show_book(title="Python Basics", year=2026)
show_book("Python Basics", year=2026)
```

La tercera forma mezcla estilos: primero posicional, después por palabra clave.

Usa la forma que haga la llamada más fácil de leer.

## 14. Los argumentos posicionales van antes de los argumentos por palabra clave

Válido:

```python
show_book("Python Basics", year=2026)
```

Sintaxis inválida:

```python
show_book(title="Python Basics", 2026)
```

Una vez que aparece un argumento por palabra clave, un argumento posicional común no puede venir después en esa llamada.

## 15. No proporciones el mismo parámetro dos veces

```python
show_book("Python Basics", title="Another Title")
```

El argumento posicional ya vincula `title`, y el argumento por palabra clave intenta vincularlo de nuevo.

Python genera `TypeError`.

## 16. Los nombres de parámetros forman parte de la interfaz

Compara:

```python
def show_route(a, b):
    print(f"{a} -> {b}")
```

con:

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")
```

La segunda definición comunica el papel de cada entrada con más claridad.

Los buenos nombres de parámetros describen significado, no solo tipo de dato.

## 17. Un parámetro puede usarse más de una vez

```python
def show_name_box(name):
    print("---")
    print(name)
    print(name)
    print("---")


show_name_box("Maya")
```

Esto usa un parámetro dos veces. No crea dos parámetros.

## 18. Los parámetros funcionan con `if`

```python
def show_score_status(name, score):
    if score >= 70:
        print(f"{name}: ready")
    else:
        print(f"{name}: review")


show_score_status("Ana", 82)
show_score_status("Luis", 61)
```

Salida:

```text
Ana: ready
Luis: review
```

`if` mantiene su significado normal. La condición simplemente usa valores proporcionados por el llamador.

## 19. Los parámetros funcionan con bucles

```python
def repeat_message(message, times):
    for repetition in range(times):
        print(message)


repeat_message("Practice", 3)
```

Salida:

```text
Practice
Practice
Practice
```

El bucle sigue siendo responsable de la repetición. Los parámetros hacen configurable el comportamiento.

## 20. Las colecciones pueden ser argumentos

```python
def show_topics(topics):
    for topic in topics:
        print(topic)


study_topics = ["functions", "parameters", "arguments"]
show_topics(study_topics)
```

Salida:

```text
functions
parameters
arguments
```

Este capítulo solo lee la colección. La mutación y el comportamiento más profundo de objetos compartidos se aplazan intencionalmente.

## 21. Sigue el flujo de entrada

```python
def greet(name):
    print(f"Hello, {name}!")


person = "Maya"
greet(person)
```

Seguimiento:

```text
"Maya"
  ↓
person
  ↓
argument in greet(person)
  ↓
parameter name
  ↓
function body
```

Los nombres pueden ser diferentes. Sigue el valor.

## 22. La llamada debe satisfacer los parámetros obligatorios

Esta función requiere dos entradas:

```python
def show_book(title, year):
    print(f"{title} ({year})")
```

Muy pocos argumentos:

```python
show_book("Python Basics")
```

Demasiados argumentos:

```python
show_book("Python Basics", 2026, "Beginner")
```

Ambas llamadas generan `TypeError`.

Los capítulos posteriores introducirán entradas opcionales y flexibles.

## 23. Los nombres de argumentos por palabra clave deben coincidir con los parámetros

Válido:

```python
show_book(title="Python Basics", year=2026)
```

Argumento por palabra clave inesperado:

```python
show_book(name="Python Basics", year=2026)
```

La función no tiene un parámetro llamado `name`, por lo que Python genera `TypeError`.

## 24. Los parámetros y las variables externas tienen papeles diferentes

```python
def show_city(city):
    print(city)


home_city = "Curitiba"
show_city(home_city)
```

`home_city` pertenece al código llamador. `city` es el parámetro de la función.

Las reglas detalladas de nombres locales frente a globales pertenecen al Capítulo 04: Alcance.

## 25. Errores comunes

### Falta un argumento obligatorio

```python
def greet(name):
    print(f"Hello, {name}!")


greet()
```

### Proporcionar demasiados argumentos

```python
greet("Maya", "Leo")
```

### Intercambiar el significado posicional

```python
show_route("Library", "Home")
```

### Vincular el mismo parámetro dos veces

```python
show_book("Python Basics", title="Another Title")
```

### Colocar un argumento posicional después de uno por palabra clave

```python
show_book(title="Python Basics", 2026)
```

### Usar nombres vagos para parámetros

Prefiere:

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")
```

## 26. Ejemplo ejecutable: un parámetro, varias llamadas

Archivo: [`examples/greet_people.py`](examples/greet_people.py)

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Maya")
greet("Leo")
greet("Nina")
```

Salida esperada:

```text
Hello, Maya!
Hello, Leo!
Hello, Nina!
```

## 27. Ejemplo ejecutable: argumentos posicionales y por palabra clave

Archivo: [`examples/book_details.py`](examples/book_details.py)

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book("Python Basics", 2026)
show_book(year=2025, title="Study Notes")
```

Salida esperada:

```text
Python Basics (2026)
Study Notes (2025)
```

## 28. Ejemplo ejecutable: parámetros y flujo del programa

Archivo: [`examples/score_status.py`](examples/score_status.py)

```python
def show_score_status(name, score):
    if score >= 70:
        print(f"{name}: ready")
    else:
        print(f"{name}: review")


show_score_status("Ana", 82)
show_score_status("Luis", 61)
```

Salida esperada:

```text
Ana: ready
Luis: review
```

## 29. Ejercicio: tarjeta de estudio configurable

Crea `show_study_card` con dos parámetros obligatorios: `topic` y `minutes`.

Requisitos:

1. defínela con `def`;
2. usa ambos parámetros en el cuerpo;
3. imprime `Topic: ...` y `Minutes: ...`;
4. llámala una vez con argumentos posicionales para `"Python"` y `45`;
5. llámala otra vez con argumentos por palabra clave para `"SQL"` y `30`;
6. no uses valores predeterminados;
7. todavía no uses `return`.

Salida esperada:

```text
Topic: Python
Minutes: 45
Topic: SQL
Minutes: 30
```

## 30. Preguntas de repaso

- ¿Qué nombre es el parámetro en `def greet(name):`?
- ¿Qué valor es el argumento en `greet("Maya")`?
- ¿Un parámetro puede recibir argumentos diferentes en llamadas distintas?
- ¿Qué determina la vinculación posicional?
- ¿Por qué los argumentos por palabra clave pueden mejorar la legibilidad?
- ¿Puede un argumento posicional común venir después de uno por palabra clave?
- ¿Qué ocurre cuando falta un argumento obligatorio?
- ¿Qué ocurre cuando un parámetro recibe dos intentos de valor?
- ¿El nombre de la variable del llamador y el nombre del parámetro deben coincidir?
- ¿Se puede pasar una lista como argumento?

## 31. Checklist de repaso

Antes de continuar, confirma que puedes:

- [ ] explicar parámetro versus argumento;
- [ ] definir parámetros obligatorios;
- [ ] llamar a la misma función con valores diferentes;
- [ ] pasar literales, variables, expresiones y colecciones;
- [ ] vincular argumentos posicionales por orden;
- [ ] escribir argumentos por palabra clave básicos;
- [ ] mezclar correctamente argumentos posicionales y luego por palabra clave;
- [ ] evitar la vinculación duplicada de parámetros;
- [ ] elegir nombres significativos para parámetros;
- [ ] usar parámetros con `if` y bucles;
- [ ] reconocer argumentos faltantes, extra, duplicados e inesperados;
- [ ] seguir la entrada desde el llamador hasta el parámetro y el cuerpo.

## 32. Referencia rápida

| Necesidad | Forma | Significado |
|---|---|---|
| una entrada obligatoria | `def greet(name):` | `name` es un parámetro |
| proporcionar entrada | `greet("Maya")` | `"Maya"` es un argumento |
| varias entradas | `def show_book(title, year):` | dos parámetros |
| llamada posicional | `show_book("Python", 2026)` | vincula por posición |
| llamada por palabra clave | `show_book(title="Python", year=2026)` | vincula por nombre del parámetro |
| llamada mixta válida | `show_book("Python", year=2026)` | posicional primero, luego por palabra clave |
| entrada obligatoria faltante | pocos argumentos | `TypeError` |
| entrada extra | demasiados argumentos | `TypeError` |
| nombre inesperado | sin parámetro correspondiente | `TypeError` |
| vinculación duplicada | mismo parámetro dos veces | `TypeError` |

## 33. Límite de alcance

Este capítulo intencionalmente no enseña en profundidad:

- `return` y diseño de valores de retorno;
- reglas de alcance local y global;
- type hints y anotaciones;
- valores predeterminados de parámetros;
- problemas de valores predeterminados mutables;
- `*args` y `**kwargs`;
- parámetros solo posicionales con `/`;
- parámetros solo por palabra clave con `*`;
- desempaquetado de argumentos con `*` o `**`;
- semántica de mutación y objetos compartidos;
- funciones anidadas, lambdas, decoradores, generadores o recursión.

El objetivo aquí es un modelo fiable de **entradas obligatorias y llamadas comunes**.

## 34. Qué viene después

Ahora puedes proporcionar valores de entrada obligatorios a una función y vincular argumentos de llamadas comunes con parámetros.

La siguiente pregunta es:

> ¿Cómo puede una función enviar un resultado útil de vuelta al llamador?

Eso conduce al **Capítulo 03: Valores de Retorno**.

Vuelve a la [ruta de Funciones](../README.es.md) o a la [ruta completa](../../docs/learning-path.es.md).

## Referencias

Documentación primaria de Python:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Tutorial: More on Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Python 3.13 Tutorial: Keyword Arguments](https://docs.python.org/3.13/tutorial/controlflow.html#keyword-arguments)
- [Python 3.13 Language Reference: Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13 Language Reference: Calls](https://docs.python.org/3.13/reference/expressions.html#calls)
