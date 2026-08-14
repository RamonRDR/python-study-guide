<div align="center">

# Flujo de Datos Entre Funciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Anterior: Funciones Trabajando Juntas](../08-functions-working-together/README.es.md) · [Siguiente fase: Comentarios y Documentación →](../../comments-and-documentation/README.es.md)

Cuando las funciones trabajan juntas, los valores recorren el programa. Un argumento entra en una función, un parámetro lo recibe, los nombres locales pueden transformarlo y un valor retornado puede llevar un resultado de vuelta al llamador o hacia otra función.

Este capítulo hace explícito ese movimiento. También introduce una distinción importante: **reasignar un nombre de parámetro no es lo mismo que mutar un objeto mutable compartido**.

**Tiempo estimado de estudio:** 90–120 minutos.

**Requisito de Python:** Python 3.10 o posterior. Este capítulo usa sintaxis moderna de anotaciones, como `int | None`, y anotaciones de colecciones incorporadas, como `list[int]`.

## Objetivos de aprendizaje

Al terminar este capítulo, deberías poder:

- seguir un valor desde el llamador hasta un parámetro y de vuelta mediante `return`;
- explicar que los parámetros son nombres locales creados para cada llamada de función;
- distinguir el nombre de variable del llamador del nombre de parámetro de la función;
- explicar por qué reasignar un parámetro no reasigna la variable del llamador;
- reconocer cuándo la mutación de una lista o diccionario compartido es visible fuera de la función;
- elegir entre retornar un valor transformado y mutar deliberadamente un objeto;
- usar variables intermedias como puntos de control en un pipeline de datos;
- seguir datos a través de condiciones, bucles y varias llamadas de función;
- usar retornos en tupla cuando una función produce naturalmente varios resultados relacionados;
- manejar `None` deliberadamente cuando una función puede no tener un resultado útil;
- usar type hints para describir el flujo de datos esperado sin tratarlos como enforcement en runtime;
- evitar flujo de datos oculto mediante estado global innecesario;
- distinguir un grafo de llamadas de un seguimiento de flujo de datos;
- cerrar la Fase 5 con un modelo mental completo de entradas, trabajo local y salidas de funciones.

## 1. El ciclo básico del flujo de datos

Una llamada de función suele seguir este patrón:

```text
valor del llamador
    ↓
expresión de argumento
    ↓
parámetro
    ↓
trabajo local
    ↓
valor retornado
    ↓
el llamador recibe el resultado
```

Por ejemplo:

```python
def double(number: int) -> int:
    result = number * 2
    return result


original = 6
doubled = double(original)
print(original)
print(doubled)
```

Salida:

```text
6
12
```

`original` y `number` son nombres distintos. Durante la llamada, `number` es un nombre de parámetro local vinculado al valor proporcionado por el llamador.

## 2. Los nombres de argumentos y parámetros no tienen que coincidir

El llamador puede usar cualquier nombre de variable adecuado:

```python
def format_name(name: str) -> str:
    return name.strip().title()


raw_text = "  ava stone  "
clean_text = format_name(raw_text)
print(clean_text)
```

Salida:

```text
Ava Stone
```

La relación se crea por la llamada de función, no por nombres iguales:

```text
raw_text ──argument──> name
```

Dentro de `format_name()`, la función trabaja con su parámetro local `name`.

## 3. Cada llamada obtiene sus propios vínculos locales de parámetros

Llamar a la misma función dos veces no hace que ambas llamadas compartan un único parámetro local.

```python
def add_one(number: int) -> int:
    number = number + 1
    return number


first = add_one(4)
second = add_one(10)
print(first, second)
```

Salida:

```text
5 11
```

Cada llamada tiene su propio vínculo local para `number`.

Esto conecta directamente con el capítulo anterior sobre alcance: los nombres locales pertenecen a una llamada concreta de la función.

## 4. Reasignar un parámetro no reasigna la variable del llamador

Considera un entero:

```python
def add_five(number: int) -> int:
    number += 5
    return number


score = 70
updated_score = add_five(score)
print(score)
print(updated_score)
```

Salida:

```text
70
75
```

Dentro de la función, `number += 5` hace que el nombre local `number` pase a referirse al resultado `75`.

Eso **no** hace que el nombre `score` del llamador pase a referirse a `75`.

El llamador solo cambia si asigna explícitamente el valor retornado:

```python
score = add_five(score)
```

## 5. Un valor retornado no reemplaza automáticamente el valor original

Esta llamada calcula y retorna un resultado:

```python
updated_score = add_five(score)
```

El resultado se almacena en `updated_score` porque el llamador eligió ese destino de asignación.

Esta llamada descarta el valor retornado:

```python
add_five(score)
```

Python sigue ejecutando la función, pero ningún nombre del llamador conserva el entero retornado.

Un modelo mental útil es:

```text
return proporciona un valor
assignment decide dónde lo almacena el llamador
```

## 6. Los valores inmutables hacen más visible la reasignación

Enteros, strings y tuplas son inmutables. Una función no puede cambiar un objeto entero o string existente en el lugar.

Por ejemplo:

```python
def add_prefix(text: str) -> str:
    text = "INFO: " + text
    return text


message = "Ready"
formatted = add_prefix(message)
print(message)
print(formatted)
```

Salida:

```text
Ready
INFO: Ready
```

El parámetro local se reasigna al nuevo resultado string. El nombre original del llamador sigue refiriéndose al string original.

## 7. Los objetos mutables agregan una segunda posibilidad importante

Las listas y los diccionarios son mutables. Si el llamador y la función se refieren al mismo objeto mutable, la función puede mutar ese objeto.

```python
def add_topic(topics: list[str], topic: str) -> None:
    topics.append(topic)


topics = ["Functions"]
add_topic(topics, "Data flow")
print(topics)
```

Salida:

```text
['Functions', 'Data flow']
```

La función no reasignó la variable del llamador. Mutó el propio objeto lista al que ambos nombres se referían durante la llamada.

## 8. Reasignar un parámetro lista es distinto de mutar la lista

Compara estas funciones:

```python
def replace_topics(topics: list[str]) -> None:
    topics = ["New topic"]


def append_topic(topics: list[str]) -> None:
    topics.append("New topic")


first = ["Functions"]
second = ["Functions"]

replace_topics(first)
append_topic(second)

print(first)
print(second)
```

Salida:

```text
['Functions']
['Functions', 'New topic']
```

`replace_topics()` solo reasigna su nombre de parámetro local.

`append_topic()` modifica el propio objeto lista compartido.

Esta distinción es central para razonar sobre el flujo de datos en Python.

## 9. La mutación no es automáticamente incorrecta

Una función que actualiza deliberadamente una lista puede tener una interfaz clara:

```python
def record_score(scores: list[int], score: int) -> None:
    scores.append(score)
```

La pregunta importante es si la mutación es esperada y comprensible.

La mutación se vuelve difícil cuando quien llama supone que la función solo lee datos, pero en realidad cambia el objeto silenciosamente.

Haz que los efectos secundarios sean deliberados y fáciles de descubrir mediante nombres, documentación y comportamiento pequeño y enfocado.

## 10. Retornar un nuevo resultado puede facilitar el seguimiento de transformaciones

En lugar de mutar una colección de entrada, una función puede construir y retornar una nueva colección.

```python
def clamp_scores(scores: list[int]) -> list[int]:
    result = []

    for score in scores:
        if score < 0:
            result.append(0)
        elif score > 100:
            result.append(100)
        else:
            result.append(score)

    return result


raw_scores = [105, 80, -4]
clean_scores = clamp_scores(raw_scores)
print(raw_scores)
print(clean_scores)
```

Salida:

```text
[105, 80, -4]
[100, 80, 0]
```

Este diseño conserva la entrada original y hace explícita la transformación mediante el valor retornado.

## 11. Elige mutación o transformación retornada según la intención

No existe una regla de Python que diga que toda función debe evitar la mutación.

Una pregunta útil es:

```text
¿Esta función debe actualizar este objeto existente?
    sí → una mutación deliberada puede encajar
    no → retorna un nuevo resultado
```

Sea cual sea el diseño elegido, hazlo predecible para el llamador.

## 12. Las variables intermedias son puntos de control del flujo de datos

El Capítulo 08 mostró que varias funciones pueden formar un pipeline. Los nombres intermedios hacen visible cada etapa.

```python
def clamp_score(score: int) -> int:
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score


def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


raw_score = 108
clean_score = clamp_score(raw_score)
status = classify_score(clean_score)

print(raw_score, clean_score, status)
```

Salida:

```text
108 100 excellent
```

Los nombres `raw_score`, `clean_score` y `status` funcionan como puntos de control etiquetados.

## 13. Sigue el pipeline una transformación a la vez

El ejemplo anterior puede dibujarse así:

```text
108
 ↓ clamp_score()
100
 ↓ classify_score()
"excellent"
```

Esto es un **seguimiento de flujo de datos**. Destaca los valores que se mueven entre etapas.

Es distinto de un grafo de llamadas:

```text
main code
├── clamp_score()
└── classify_score()
```

Un grafo de llamadas destaca quién llama a quién. Un seguimiento de flujo de datos destaca qué datos se mueven y cambian.

## 14. Una función coordinadora puede hacer explícito el flujo

El mismo pipeline puede vivir dentro de una coordinadora:

```python
def clamp_score(score: int) -> int:
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score


def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def build_score_summary(score: int) -> str:
    clean_score = clamp_score(score)
    status = classify_score(clean_score)
    return f"{clean_score}: {status}"


print(build_score_summary(108))
```

Salida:

```text
100: excellent
```

La coordinadora es dueña de la secuencia. Las auxiliares son dueñas de las transformaciones individuales.

## 15. Los datos pueden ramificarse mediante condiciones

Una función no necesita retornar el mismo valor interno en todas las etapas, pero su comportamiento público debe seguir siendo comprensible.

```python
def find_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

La entrada `score` llega a uno de dos `return`.

Un seguimiento sencillo es:

```text
score
  ↓ condition
  ├─ true  → "ready"
  └─ false → "review"
```

## 16. Los retornos anticipados pueden detener el flujo deliberadamente

A veces una función detecta que no existe un resultado útil con el que continuar.

```python
def find_first_positive(values: list[int]) -> int | None:
    for value in values:
        if value > 0:
            return value
    return None


result = find_first_positive([-4, -2, 7, 9])
print(result)
```

Salida:

```text
7
```

La función retorna en cuanto encuentra el primer valor adecuado.

## 17. `None` puede representar la ausencia de un resultado útil

Cuando `None` forma parte de la interfaz, el llamador debe manejarlo intencionalmente.

```python
def find_first_positive(values: list[int]) -> int | None:
    for value in values:
        if value > 0:
            return value
    return None


result = find_first_positive([-4, -2])

if result is None:
    print("No positive value")
else:
    print(result)
```

Salida:

```text
No positive value
```

El llamador verifica el resultado antes de enviarlo a otro cálculo.

## 18. No continúes accidentalmente un pipeline con `None`

Supón que otra función espera un entero:

```python
def double(number: int) -> int:
    return number * 2
```

Pasar un posible `None` sin verificarlo antes crea un flujo inseguro.

El type hint `int | None` es útil porque informa a lectores y herramientas de análisis estático que existe el caso de ausencia.

Los type hints describen la interfaz prevista. Python no los aplica automáticamente en runtime.

## 19. Varios resultados relacionados pueden viajar en una tupla

Una función puede producir naturalmente más de un resultado relacionado.

```python
def summarize(values: list[int]) -> tuple[int, int]:
    total = sum(values)
    count = len(values)
    return total, count


total, count = summarize([10, 20, 30])
print(total)
print(count)
```

Salida:

```text
60
3
```

Python crea una tupla con los valores retornados y el llamador desempaqueta esa tupla en dos nombres.

## 20. Los retornos en tupla hacen visibles las dependencias posteriores

Un cálculo posterior puede usar uno o ambos valores retornados:

```python
def summarize(values: list[int]) -> tuple[int, int]:
    return sum(values), len(values)


def calculate_average(total: int, count: int) -> float:
    if count == 0:
        return 0.0
    return total / count


total, count = summarize([10, 20, 30])
average = calculate_average(total, count)
print(average)
```

Salida:

```text
20.0
```

La dependencia es explícita: `calculate_average()` necesita `total` y `count`.

## 21. Los bucles pueden mover muchos valores por el mismo helper

Un bucle puede enviar un elemento cada vez a una función:

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


names = [" ava ", "LEO", " mia"]
clean_names = []

for name in names:
    clean_names.append(normalize_name(name))

print(clean_names)
```

Salida:

```text
['Ava', 'Leo', 'Mia']
```

Cada iteración crea otra llamada y otro vínculo local de parámetro.

## 22. Las colecciones pueden pasar por varias etapas

Una colección puede ser transformada, resumida y formateada por funciones distintas.

```python
def keep_positive(values: list[int]) -> list[int]:
    result = []

    for value in values:
        if value > 0:
            result.append(value)

    return result


def calculate_total(values: list[int]) -> int:
    return sum(values)


def format_total(total: int) -> str:
    return f"Total: {total}"


raw_values = [-3, 5, 8, -1]
positive_values = keep_positive(raw_values)
total = calculate_total(positive_values)
message = format_total(total)
print(message)
```

Salida:

```text
Total: 13
```

El tipo de dato cambia a lo largo del recorrido:

```text
list[int] → list[int] → int → str
```

## 23. Los type hints pueden documentar la forma de cada etapa

El pipeline anterior expone sus transiciones esperadas directamente en las firmas:

```text
keep_positive(list[int]) -> list[int]
calculate_total(list[int]) -> int
format_total(int) -> str
```

Esto puede facilitar la inspección de un diseño con varias funciones.

Recuerda: los type hints comunican intención y ayudan a las herramientas. No validan ni convierten valores automáticamente en runtime.

## 24. Los globales ocultos dificultan ver el flujo de datos

Compara esta dependencia escondida:

```python
tax_rate = 0.10


def add_tax(amount: float) -> float:
    return amount * (1 + tax_rate)
```

con una dependencia explícita:

```python
def add_tax(amount: float, tax_rate: float) -> float:
    return amount * (1 + tax_rate)
```

La segunda firma muestra exactamente qué datos necesita la función.

Una constante a nivel de módulo puede ser apropiada en algunos diseños. El problema es usar estado global para ocultar entradas cambiantes normales que deberían ser visibles en la interfaz.

## 25. Evita que una función lea variables locales de otra función

Un nombre local dentro de una función no está disponible directamente dentro de otra función no relacionada.

```python
def first() -> int:
    value = 10
    return value


def second() -> int:
    value = first()
    return value * 2
```

`second()` recibe los datos mediante el valor retornado por `first()`. No entra en el namespace local de `first()`.

Ese traspaso explícito es una frontera saludable.

## 26. Ejemplo práctico: construir un informe de aprendizaje

Este ejemplo combina varias ideas de toda la fase de Funciones:

```python
def summarize_sessions(sessions: list[int]) -> tuple[int, float]:
    total = sum(sessions)
    if not sessions:
        return total, 0.0
    return total, total / len(sessions)


def classify_total(total: int) -> str:
    if total >= 120:
        return "deep"
    if total >= 60:
        return "steady"
    return "light"


def build_learning_report(subject: str, sessions: list[int]) -> str:
    total, average = summarize_sessions(sessions)
    workload = classify_total(total)
    return (
        f"{subject}: {total} minutes, "
        f"average {average:.1f}, workload {workload}"
    )


print(build_learning_report("Python", [30, 45, 60]))
```

Salida:

```text
Python: 135 minutes, average 45.0, workload deep
```

Seguimiento:

```text
subject = "Python"
sessions = [30, 45, 60]
        ↓ summarize_sessions()
total = 135, average = 45.0
        ↓ classify_total(total)
workload = "deep"
        ↓ formatting
final str returned to caller
```

## 27. El comportamiento con entrada vacía forma parte del diseño del flujo de datos

`summarize_sessions()` maneja explícitamente una lista vacía:

```python
if not sessions:
    return total, 0.0
```

Sin esa rama, dividir por `len(sessions)` fallaría cuando la lista estuviera vacía.

Pensar en flujo de datos incluye preguntar:

- ¿Qué valores pueden entrar en esta función?
- ¿Qué valores pueden salir de ella?
- ¿Qué ocurre en casos límite?
- ¿Puede la siguiente función consumir con seguridad todos los resultados posibles?

## 28. Error común: asumir que reasignar un parámetro cambia el llamador

Expectativa incorrecta:

```python
def reset_score(score: int) -> None:
    score = 0


score = 80
reset_score(score)
print(score)
```

Salida:

```text
80
```

Si el llamador debe recibir `0`, retorna el valor y asigna el resultado:

```python
def reset_score(score: int) -> int:
    return 0


score = reset_score(score)
```

## 29. Error común: mutar la entrada accidentalmente

Esta función cambia la lista del llamador:

```python
def prepare_names(names: list[str]) -> None:
    names.sort()
```

Eso puede ser correcto si la mutación es el contrato previsto.

Si el llamador espera que el orden original permanezca intacto, construye y retorna un resultado separado.

La lección importante no es “nunca mutes”. Es “no ocultes la mutación”.

## 30. Error común: confundir datos retornados con salida impresa

Una función puede imprimir un mensaje útil y aun así retornar `None`:

```python
def show_total(values: list[int]) -> None:
    print(sum(values))
```

Si la siguiente función necesita el total numérico, imprimir no es suficiente. Retorna el número.

Esta distinción ha aparecido durante toda la Fase 5 porque es una de las fronteras más importantes del flujo de datos entre funciones.

## 31. Error común: pasar la etapa equivocada a la siguiente función

Considera este pipeline:

```text
raw score → clamp → classify
```

Si la regla de clasificación debe usar el score limitado, esto es incorrecto:

```python
clean_score = clamp_score(raw_score)
status = classify_score(raw_score)
```

El código se ejecuta, pero el recorrido de los datos no es el previsto.

Los nombres de variables intermedias hacen que este tipo de error sea más fácil de detectar.

## 32. Error común: ocultar demasiadas etapas en una expresión profundamente anidada

Esto puede ser técnicamente válido:

```python
message = format_total(calculate_total(keep_positive(raw_values)))
```

Pero al aprender, depurar o inspeccionar varias etapas, los checkpoints explícitos suelen ser más claros:

```python
positive_values = keep_positive(raw_values)
total = calculate_total(positive_values)
message = format_total(total)
```

Prefiere legibilidad a concursos de cantidad de líneas.

## 33. Ejercicio

Construye un pequeño pipeline para temperaturas.

Requisitos:

1. Crea `clamp_temperature(temperature: int) -> int` que limite valores inferiores a `-50` a `-50` y superiores a `50` a `50`.
2. Crea `classify_temperature(temperature: int) -> str` que retorne `"hot"` para valores de al menos `30`, `"cold"` para valores inferiores a `10` y `"mild"` en los demás casos.
3. Crea `build_temperature_report(city: str, temperature: int) -> str`.
4. Dentro de la coordinadora, envía primero la temperatura original a la función de límite.
5. Pasa el resultado limitado a la función de clasificación.
6. Retorna un string final con ciudad, temperatura limitada y categoría.
7. Prueba la coordinadora con al menos una temperatura fuera del rango aceptado.

Antes de programar, dibuja el flujo de datos con flechas.

## 34. Lista de revisión

Ahora deberías poder responder:

- ¿Cuál es la diferencia entre una variable del llamador y un nombre de parámetro?
- ¿Reasignar un parámetro reasigna automáticamente la variable del llamador?
- ¿Por qué la mutación de una lista puede seguir siendo visible para el llamador?
- ¿Cuándo retornar un nuevo valor es más claro que mutar una entrada?
- ¿Qué proporciona `return` al llamador?
- ¿Qué papel tiene la asignación después de que una función retorna?
- ¿Cómo puede `None` interrumpir un pipeline?
- ¿Cómo pueden los type hints hacer más fácil entender el movimiento entre etapas?
- ¿Cuál es la diferencia entre un grafo de llamadas y un seguimiento de flujo de datos?
- ¿Por qué las dependencias globales ocultas son más difíciles de razonar?

## 35. Resumen de consulta rápida

| Situación | Modelo útil |
|---|---|
| El llamador envía un valor | la expresión de argumento se vincula a un parámetro en esa llamada |
| La función reasigna un parámetro | el vínculo de la variable del llamador no cambia |
| La función muta una lista/dict compartido | la mutación puede ser visible para el llamador |
| La función produce un valor transformado | retórnalo y deja que el llamador lo asigne |
| La función puede no producir resultado útil | retorna y maneja `None` deliberadamente |
| La función produce resultados relacionados | retorna una tupla y desempaquétala |
| Cooperan varias etapas | usa nombres intermedios para exponer el pipeline |
| Dependencias ocultas en globales | prefiere parámetros/retornos explícitos cuando corresponda |
| Necesitas una vista estructural | dibuja un grafo de llamadas |
| Necesitas una vista del movimiento de valores | dibuja un seguimiento de flujo de datos |

## 36. Fase 5 completada

Ahora puedes conectar toda la secuencia de Funciones:

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

La fase comenzó con un solo `def` y termina con un modelo para componer funciones mientras sigues exactamente cómo los datos entran, cambian y salen de cada llamada.

Siguiente paso en la secuencia recomendada: [Comentarios, Documentación y Código Limpio](../../comments-and-documentation/README.es.md).

## Referencias oficiales

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Tutorial: More on Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Python 3.13 Language Reference: `return` statement](https://docs.python.org/3.13/reference/simple_stmts.html#the-return-statement)
- [Python 3.13 Data Model](https://docs.python.org/3.13/reference/datamodel.html)
