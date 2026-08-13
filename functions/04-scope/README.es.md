<div align="center">

# Alcance

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Anterior: Valores de Retorno](../03-return-values/README.es.md)

El Capítulo 01 dio nombre al comportamiento. El Capítulo 02 movió datos hacia una función. El Capítulo 03 envió resultados de vuelta al llamador. Este capítulo responde la siguiente pregunta:

> ¿Dónde existe cada nombre y dónde puede encontrarlo Python?

El modelo mental para principiantes pasa a ser:

```text
caller → arguments → function local scope → return value → caller
```

**Tiempo estimado de estudio:** 80–105 minutos.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar la diferencia inicial entre **alcance** y **namespace**;
- identificar nombres globales a nivel de módulo y nombres locales de funciones;
- explicar que los parámetros son nombres locales;
- explicar que cada llamada de función recibe su propio namespace local;
- leer un nombre del nivel del módulo desde dentro de una función;
- predecir cuándo una asignación crea una vinculación local;
- reconocer sombreado cuando la misma grafía está vinculada en alcances diferentes;
- explicar que sentencias comunes `if`, `for` y `while` no crean un nuevo alcance local de función;
- reconocer `NameError` y el caso común de `UnboundLocalError` relacionado con alcance;
- explicar qué cambia `global` y por qué el flujo con parámetros y retorno suele ser más claro;
- seguir el camino inicial de búsqueda de nombres desde el alcance local hasta nombres globales e incorporados.

## 1. El alcance responde dónde un nombre es visible

Un **alcance** es una región del código donde un nombre puede accederse directamente.

```python
course = "Python"


def show_course():
    message = "Studying"
    print(course)
    print(message)


show_course()
print(course)
```

Salida:

```text
Python
Studying
Python
```

`course` está vinculado a nivel de módulo, por lo que la función puede leerlo. `message` se crea dentro de la función y es local a esa llamada.

La grafía de un nombre es solo parte de la historia. **Importa dónde está vinculado el nombre.**

## 2. Namespace y alcance están relacionados, pero son diferentes

Un **namespace** asocia nombres con objetos. Un **alcance** describe dónde esos nombres son directamente visibles.

```text
namespace → which names are bound to which objects
scope     → where those names are directly visible
```

Por ejemplo:

```python
course = "Python"
chapter = 4

print(course)
print(chapter)
```

Salida:

```text
Python
4
```

El namespace del módulo contiene vinculaciones para `course` y `chapter`.

## 3. Los nombres a nivel de módulo son globales para ese módulo

Un nombre vinculado en el nivel superior de un archivo Python pertenece al namespace global de ese módulo.

```python
course = "Python"
chapter = 4

print(course)
print(chapter)
```

Ambos son nombres globales en este módulo.

En código para principiantes, “global” aquí significa global al módulo actual, no compartido mágicamente con todos los programas Python.

## 4. Una llamada de función crea un namespace local

Cuando se llama una función, Python crea un namespace local para esa llamada.

```python
def show_message():
    message = "Ready"
    print(message)


show_message()
```

Salida:

```text
Ready
```

`message` es un nombre local creado durante esta llamada. Una llamada posterior recibe otro namespace local.

## 5. Los parámetros son nombres locales

Los parámetros de una función participan en su namespace local.

```python
def greet(name):
    message = f"Hello, {name}"
    print(message)


greet("Avery")
```

Salida:

```text
Hello, Avery
```

Durante la llamada:

```text
argument "Avery"
↓
local parameter name → "Avery"
↓
local message is created
```

El argumento proporciona un objeto. El parámetro es el nombre local que usa la función.

## 6. Los nombres locales no escapan automáticamente de la función

```python
def create_message():
    message = "Ready"


create_message()
print(message)
```

La llamada funciona, pero la última línea produce `NameError`. No existe una vinculación visible llamada `message` a nivel de módulo.

```text
inside function  → message is local
outside function → that local name is not directly visible
```

Si el llamador necesita el valor, retórnalo.

## 7. Cada llamada recibe su propio namespace local

```python
def build_label(topic):
    label = f"Learning {topic}"
    print(label)


build_label("scope")
build_label("functions")
```

Salida:

```text
Learning scope
Learning functions
```

Piensa en las llamadas como espacios de trabajo separados:

```text
call 1 → topic and label for "scope"
call 2 → topic and label for "functions"
```

Los nombres del código fuente se reutilizan, pero cada invocación tiene su propio namespace local.

## 8. Una función puede leer un nombre global

Una función puede leer un nombre a nivel de módulo sin declararlo `global` cuando solo lee ese nombre.

```python
course = "Python"


def show_course():
    print(course)


show_course()
```

Salida:

```text
Python
```

Python no encuentra una vinculación local llamada `course`, así que la búsqueda continúa hacia afuera y encuentra la vinculación a nivel de módulo.

Leer un nombre global y **revincular** un nombre global son operaciones diferentes.

## 9. Las constantes de módulo pueden ser entradas compartidas razonables

```python
TAX_RATE = 0.10


def calculate_tax(amount):
    return amount * TAX_RATE


print(calculate_tax(200))
```

Salida:

```text
20.0
```

Los nombres en mayúsculas como `TAX_RATE` son una convención de estilo para constantes. Python no impone inmutabilidad porque un nombre esté en mayúsculas.

Leer una constante de módulo claramente nombrada puede ser comprensible. El estado global mutable oculto es otro problema de diseño y queda para más adelante.

## 10. Una asignación dentro de una función normalmente crea una vinculación local

Sin `global` o `nonlocal`, asignar a un nombre dentro de una función normalmente vincula ese nombre localmente.

```python
status = "module"


def show_status():
    status = "function"
    print(status)


show_status()
print(status)
```

Salida:

```text
function
module
```

La asignación dentro de `show_status()` no reemplaza la vinculación a nivel de módulo. Crea una vinculación local con la misma grafía.

## 11. El sombreado usa la misma grafía para vinculaciones diferentes

El ejemplo anterior contiene **sombreado**:

```text
inside show_status → status = "function"
module level       → status = "module"
```

El sombreado es válido. El sombreado innecesario puede hacer que un programa sea más difícil de seguir, así que prefiere nombres distintos cuando los significados sean realmente diferentes.

## 12. Búsqueda de nombres para principiantes: LEGB

Considera:

```python
topic = "scope"


def show_topic():
    message = "ready"
    print(message)
    print(topic)
    print(len(topic))


show_topic()
```

Salida:

```text
ready
scope
5
```

El mnemónico tradicional de búsqueda es:

```text
Local → Enclosing → Global → Built-in
```

- **Local:** nombres de la llamada actual de la función;
- **Enclosing:** nombres de funciones externas cuando las funciones están anidadas;
- **Global:** nombres del módulo actual;
- **Built-in:** nombres como `len`, `print` y `abs`.

Este capítulo usa Local, Global y Built-in directamente. Las funciones anidadas y `nonlocal` se posponen, así que Enclosing se presenta solo como parte del mapa de búsqueda.

## 13. Evita sombrear nombres incorporados

Evita revincular nombres incorporados conocidos:

```python
len = 10

print(len("scope"))
```

Ahora `len` se refiere al entero `10` en el alcance actual, por lo que la función incorporada queda sombreada y la llamada falla.

Nombres como `list`, `str`, `type`, `sum`, `min`, `max`, `input` y `print` merecen la misma cautela.

## 14. `if` no crea un nuevo alcance local de función

```python
def classify_score(score):
    if score >= 60:
        result = "passing"
    else:
        result = "review"

    print(result)


classify_score(75)
```

Salida:

```text
passing
```

`result` pertenece al alcance local de la función que lo rodea. Ambas ramas vinculan el nombre, así que la lectura posterior es segura.

## 15. `for` no crea un nuevo alcance local de función

```python
def show_last_number():
    for number in [1, 2, 3]:
        print(number)

    print("Last:", number)


show_last_number()
```

Salida:

```text
1
2
3
Last: 3
```

El objetivo del bucle `number` pertenece al alcance de la función que lo rodea. Las sentencias comunes `while` siguen la misma idea de alcance circundante.

No generalices esto a toda construcción de Python. Funciones, clases, comprehensions y otras construcciones tienen reglas propias.

## 16. Pregunta si el nombre quedó definitivamente vinculado antes del uso

El alcance y el flujo del programa trabajan juntos.

Una pregunta útil es:

> En el camino que realmente se ejecutó, ¿este nombre quedó vinculado antes de que Python intentara leerlo?

Esto importa en ramas y bucles porque algunos caminos pueden no ejecutar una asignación.

## 17. Un nombre visible ausente produce `NameError`

Vuelve a este ejemplo:

```python
def create_message():
    message = "Ready"


create_message()
print(message)
```

La última línea no puede resolver `message` a nivel de módulo y produce `NameError`.

Una lista útil de depuración es:

1. ¿La grafía es correcta?
2. ¿El nombre estaba vinculado antes de este uso?
3. ¿Estaba vinculado en un alcance visible desde aquí?
4. ¿Esperaba que un valor local saliera de una función sin retornarlo?

## 18. Una asignación en cualquier punto de la función puede hacer local al nombre

Esta regla es sutil e importante:

```python
count = 10


def show_count():
    print(count)
    count = 20


show_count()
```

Llamar `show_count()` produce `UnboundLocalError`.

¿Por qué? La asignación `count = 20` convierte `count` en un nombre local para el bloque de la función. El `print(count)` anterior intenta leer ese nombre local antes de que la vinculación local reciba un valor.

```text
function contains local binding for count
↓
print(count) runs before local count receives a value
↓
UnboundLocalError
```

`UnboundLocalError` es una subclase de `NameError`. El manejo de excepciones viene después; aquí el objetivo es comprender por qué falla la búsqueda.

## 19. Prefiere flujo explícito de entrada y retorno cuando sea posible

En lugar de revincular silenciosamente estado global compartido, pasa el valor a la función y retorna el nuevo valor.

```python
count = 10


def increase(value):
    return value + 1


count = increase(count)
print(count)
```

Salida:

```text
11
```

El movimiento es explícito:

```text
module count
↓ argument
local parameter value
↓ return
new module count
```

Esto se apoya directamente en los Capítulos 02 y 03.

## 20. Leer un nombre global no requiere `global`

```python
mode = "study"


def show_mode():
    print(mode)


show_mode()
```

Salida:

```text
study
```

No hace falta una sentencia `global`. `global` trata de vincular un nombre a nivel de módulo, no de conceder permiso para leerlo.

## 21. `global` permite revinculación explícita a nivel de módulo

```python
mode = "study"


def enable_practice_mode():
    global mode
    mode = "practice"


enable_practice_mode()
print(mode)
```

Salida:

```text
practice
```

Dentro de esa función, `global mode` dirige usos y asignaciones de `mode` a la vinculación a nivel de módulo.

La declaración `global` debe aparecer antes de usos o asignaciones de ese nombre en el mismo alcance.

## 22. Usa `global` con cautela

Compara:

```text
global rebinding
function → hidden change to module state

parameter/return flow
caller → explicit input → function → explicit output → caller
```

El segundo modelo suele ser más fácil de probar, reutilizar y comprender.

Usa `global` cuando el estado compartido a nivel de módulo sea realmente el diseño previsto y se entienda el costo. Prefiere parámetros y valores de retorno cuando hagan más claro el flujo de datos.

Esto es una recomendación de diseño, no una prohibición de Python.

## 23. Alcance y valores de retorno trabajan juntos

```python
course = "Python"


def build_message(topic):
    label = f"{course}: {topic}"
    return label


message = build_message("scope")
print(message)
```

Salida:

```text
Python: scope
```

`topic` y `label` son locales. El llamador recibe el objeto útil mediante `return` y lo vincula a `message`.

El alcance crea la frontera. `return` ofrece un camino explícito a través de ella.

## 24. Sigue el recorrido completo

Para el ejemplo anterior:

```text
module binds course → "Python"
↓
caller passes "scope"
↓
local parameter topic is bound
↓
local label is bound
↓
course is found in module global scope
↓
function returns "Python: scope"
↓
caller binds message to returned value
```

Esto combina los modelos mentales de los Capítulos 02, 03 y 04.

## 25. Ejemplos ejecutables

### Nombres locales y globales

Archivo: [`examples/local_and_global_names.py`](examples/local_and_global_names.py)

```python
course = "Python"


def show_course():
    message = "Studying"
    print(course)
    print(message)


show_course()
print(course)
```

Salida esperada:

```text
Python
Studying
Python
```

### Namespaces locales separados por llamada

Archivo: [`examples/separate_function_calls.py`](examples/separate_function_calls.py)

```python
def build_label(topic):
    label = f"Learning {topic}"
    print(label)


build_label("scope")
build_label("functions")
```

Salida esperada:

```text
Learning scope
Learning functions
```

### Sombreado sin cambiar la vinculación global

Archivo: [`examples/shadowing_names.py`](examples/shadowing_names.py)

```python
status = "module"


def show_status():
    status = "function"
    print(status)


show_status()
print(status)
```

Salida esperada:

```text
function
module
```

## 26. Ejercicio: sigue nombres globales y locales

Estudia este programa:

```python
language = "Python"


def describe_topic(topic):
    label = f"{language}: {topic}"
    return label


result = describe_topic("scope")
print(result)
```

Salida esperada:

```text
Python: scope
```

Antes de ejecutarlo, responde:

1. ¿Qué nombres están a nivel de módulo?
2. ¿Qué nombres son locales a `describe_topic()`?
3. ¿Por qué la función puede leer `language` sin `global`?
4. ¿Por qué el llamador puede usar el valor retornado pero no el nombre local `label` directamente?
5. ¿Qué cambia si la función asigna a `language` sin declararlo `global`?

Después ejecuta el programa y verifica tu explicación.

## 27. Lista de revisión

Antes de continuar, confirma que puedes:

- [ ] explicar alcance y namespace a nivel principiante;
- [ ] identificar nombres globales del módulo y nombres locales de funciones;
- [ ] explicar que los parámetros son nombres locales;
- [ ] explicar que cada llamada recibe su propio namespace local;
- [ ] leer un nombre global desde una función sin `global`;
- [ ] reconocer sombreado local y de nombres incorporados;
- [ ] explicar Local → Enclosing → Global → Built-in;
- [ ] explicar el comportamiento de alcance de `if`, `for` y `while` comunes;
- [ ] reconocer `NameError` causado por un nombre visible ausente;
- [ ] explicar el `UnboundLocalError` común causado por leer antes de la vinculación local;
- [ ] explicar qué cambia `global`;
- [ ] preferir parámetros y retorno cuando hagan más claro el flujo de datos.

## 28. Referencia rápida

| Necesidad | Regla para principiantes |
|---|---|
| nombre a nivel de módulo | nombre global para ese módulo |
| parámetro de función | nombre local |
| asignación en una función | normalmente vincula un nombre local |
| leer global desde la función | no requiere `global` |
| revincular global desde la función | declararlo con `global` |
| misma grafía local y global | la vinculación local sombrea la global |
| `if` / `for` / `while` comunes | no crean nuevo alcance local de función |
| nombre no encontrado | `NameError` |
| nombre local leído antes de la vinculación local | `UnboundLocalError` |
| enviar resultado local al llamador | usar `return` |
| cambio de estado más claro | frecuentemente parámetros + retorno |

## 29. Límite de alcance

Este capítulo pospone intencionalmente:

- funciones anidadas como técnica de programación;
- `nonlocal`;
- closures;
- funciones lambda;
- alcances de clases y detalles de búsqueda específicos de métodos;
- detalles de alcance de comprehensions;
- mutación y aliasing de objetos globales compartidos;
- importación de módulos como tema principal;
- manejo de excepciones;
- decoradores y generadores.

Estos temas aparecen después en la ruta o necesitan su propio contexto.

## 30. Qué viene después

Ahora puedes seguir:

```text
caller
↓
arguments
↓
local parameter names
↓
local function work
↓
name lookup across visible scopes
↓
return value
↓
caller
```

La siguiente pregunta es:

> ¿Cómo puede una función comunicar los tipos de entradas y salidas que espera?

Eso conduce al **Capítulo 05: Type Hints**.

Vuelve a la [ruta de Funciones](../README.es.md) o a la [ruta completa de aprendizaje](../../docs/learning-path.es.md).

## Referencias

Documentación primaria de Python:

- [Python 3.13 Language Reference: Execution model](https://docs.python.org/es/3.13/reference/executionmodel.html)
- [Python 3.13 Tutorial: Python Scopes and Namespaces](https://docs.python.org/es/3.13/tutorial/classes.html#python-scopes-and-namespaces)
- [Python 3.13 Language Reference: The `global` statement](https://docs.python.org/es/3.13/reference/simple_stmts.html#the-global-statement)
