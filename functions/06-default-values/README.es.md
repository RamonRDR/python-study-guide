<div align="center">

# Valores Predeterminados

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Anterior: Type Hints](../05-type-hints/README.es.md)

Los capítulos anteriores mostraron cómo las funciones reciben argumentos, devuelven valores, resuelven nombres y describen tipos esperados. Este capítulo añade una decisión más de interfaz:

> ¿Qué entradas debe proporcionar siempre quien llama y cuáles pueden tener un valor alternativo razonable?

```text
required input
    +
defaulted input
        ↓
caller supplies only what needs to differ
```

**Tiempo estimado de estudio:** 75–100 minutos.

**Versión de Python:** los ejemplos usan **Python 3.10 o posterior**, igual que el capítulo de Type Hints.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- definir un valor predeterminado con `name=value`;
- combinar type hints y valores predeterminados con `name: type = value`;
- distinguir parámetros obligatorios de parámetros con valor predeterminado;
- reemplazar valores predeterminados con argumentos posicionales o por palabra clave;
- explicar la regla de orden para parámetros obligatorios y con valor predeterminado ordinarios;
- explicar cuándo se evalúan las expresiones predeterminadas;
- reconocer la trampa de argumentos predeterminados mutables;
- usar `None` antes de crear un objeto mutable nuevo;
- elegir valores predeterminados que aclaren la interfaz en vez de ocultar entradas obligatorias.

## 1. Un valor predeterminado permite omitir un argumento

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


print(greet("Avery"))
print(greet("Avery", "Welcome"))
```

Salida:

```text
Hello, Avery
Welcome, Avery
```

`name` no tiene valor predeterminado, así que quien llama debe proporcionarlo.

`greeting` tiene el valor `"Hello"`, por lo que su argumento puede omitirse.

```text
greet("Avery")
       ↓
name = "Avery"
greeting = "Hello"  ← default fills the missing slot
```

## 2. La sintaxis de definición y de llamada tiene funciones diferentes

La forma básica de la definición es:

```text
def function_name(required, optional=default_value):
    ...
```

Ejemplo:

```python
def build_label(topic, prefix="Topic"):
    return f"{prefix}: {topic}"


print(build_label("Functions"))
print(build_label("Functions", prefix="Chapter"))
```

Salida:

```text
Topic: Functions
Chapter: Functions
```

Mantén separados los dos usos de `=`:

```text
definition → prefix="Topic"     establishes a default
call       → prefix="Chapter"   supplies a keyword argument
```

## 3. Los parámetros obligatorios y predeterminados expresan decisiones de diseño

```python
def create_message(name, language="English"):
    return f"{name}: {language}"
```

`name` es obligatorio porque la función no debería inventarlo.

`language` tiene valor predeterminado porque `"English"` fue elegido como alternativa deliberada.

Pregunta:

> Si quien llama no dice nada sobre esta opción, ¿qué comportamiento es razonable y poco sorprendente?

No añadas valores predeterminados solo para hacer opcionales todos los argumentos.

## 4. Un argumento proporcionado reemplaza el valor predeterminado en esa llamada

```python
def format_score(score, suffix=" points"):
    return f"{score}{suffix}"


print(format_score(80))
print(format_score(80, " pts"))
```

Salida:

```text
80 points
80 pts
```

Python usa el valor predeterminado solo cuando el parámetro correspondiente todavía no recibió un valor.

Proporcionar otro valor en una llamada no modifica el valor predeterminado almacenado.

## 5. Varios valores predeterminados funcionan bien con reemplazos por palabra clave

```python
def create_badge(name, color="blue", size="medium"):
    return f"{name}: {color}, {size}"


print(create_badge("Python"))
print(create_badge("Python", size="large"))
print(create_badge("Python", color="green"))
```

Salida:

```text
Python: blue, medium
Python: blue, large
Python: green, medium
```

Los argumentos por palabra clave permiten cambiar una opción sin repetir las demás.

## 6. Los parámetros obligatorios normalmente vienen primero

Esto es válido:

```python
def register(name, active=True):
    return f"{name}: {active}"
```

Esto no lo es:

```python
# SyntaxError: non-default argument follows default argument
def register(active=True, name):
    return f"{name}: {active}"
```

Para parámetros ordinarios, usa esta regla inicial:

```text
required parameters first
defaulted parameters after them
```

Las categorías especiales de parámetros refinan esta regla más adelante.

## 7. Type hints y valores predeterminados pueden aparecer juntos

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(greet("Avery"))
```

Lee la firma así:

```text
name: str
├── expected type: str
└── no default → argument required

greeting: str = "Hello"
├── expected type: str
└── default: "Hello" → argument may be omitted

-> str
└── expected return type
```

Los type hints describen tipos esperados. Los valores predeterminados describen el comportamiento cuando se omite un argumento.

Ninguno sustituye la validación en runtime.

## 8. Mantén cuatro conceptos separados

```text
default    → fallback when an argument is omitted
type hint  → expected type information
validation → checks actual values or rules
conversion → explicitly transforms compatible data
```

Por ejemplo:

```python
def repeat_text(text: str, times: int = 2) -> str:
    return text * times
```

`times=2` es una alternativa. No valida todos los valores futuros.

## 9. Un valor predeterminado forma parte del comportamiento público

```python
def create_heading(title: str, level: int = 2) -> str:
    return f"h{level}: {title}"
```

La interfaz comunica:

> Si quien llama no elige un nivel, usa 2.

Cambiar el valor predeterminado después modifica todas las llamadas que omiten `level`.

Los valores predeterminados son pequeñas decisiones de interfaz, no solo sintaxis más corta.

## 10. No ocultes entradas realmente obligatorias

Este diseño puede ocultar datos faltantes:

```python
def create_student(name="", course=""):
    ...
```

Si ambas piezas son necesarias, exígelas:

```python
def create_student(name: str, course: str, active: bool = True):
    ...
```

Ahora solo `active` tiene una alternativa deliberada.

Una llamada más corta no es automáticamente una interfaz más clara.

## 11. Las expresiones predeterminadas se evalúan cuando se define la función

```python
level = "beginner"


def describe(topic, course_level=level):
    return f"{topic}: {course_level}"


level = "advanced"

print(describe("Functions"))
print(describe("Functions", level))
```

Salida:

```text
Functions: beginner
Functions: advanced
```

Cuando se ejecutó la sentencia `def`, `level` valía `"beginner"`.

Ese valor se convirtió en el valor predeterminado almacenado de `course_level`.

Cambiar la variable externa después no lo recalcula.

## 12. Los valores predeterminados se evalúan una vez, no una vez por llamada

Usa este modelo mental:

```text
execute def statement
    ↓
evaluate default expressions
    ↓
store their resulting values
    ↓
future calls reuse stored defaults when needed
```

Este detalle importa sobre todo cuando el objeto almacenado puede cambiar.

## 13. Los valores predeterminados inmutables suelen ser sencillos

Strings, números, booleanos y `None` son valores comunes:

```python
def describe_course(
    name: str,
    level: str = "beginner",
    lessons: int = 10,
    published: bool = False,
) -> str:
    return f"{name} | {level} | {lessons} | {published}"
```

Estos valores son inmutables, así que no crean el problema de mutación compartida que veremos a continuación.

Aun así, pregunta si cada alternativa tiene sentido.

## 14. Los valores predeterminados mutables pueden conservar cambios entre llamadas

```python
def add_topic(topic, topics=[]):
    topics.append(topic)
    return topics


print(add_topic("functions"))
print(add_topic("defaults"))
```

Salida:

```text
['functions']
['functions', 'defaults']
```

La misma lista se reutiliza porque fue creada cuando se ejecutó la definición de la función.

Esta es la **trampa del argumento predeterminado mutable**.

## 15. El problema es reutilizar el objeto predeterminado

Las listas son normales dentro del cuerpo de una función:

```python
def create_topics():
    topics = []
    topics.append("functions")
    return topics
```

Se crea una lista nueva cada vez que se ejecuta el cuerpo.

La forma arriesgada es específicamente:

```python
def add_topic(topic, topics=[]):
    ...
```

porque esa lista pertenece a los valores predeterminados almacenados y puede sobrevivir entre llamadas.

## 16. Usa `None` cuando la omisión deba crear un objeto nuevo

```python
def add_topic(topic: str, topics: list[str] | None = None) -> list[str]:
    if topics is None:
        topics = []

    topics.append(topic)
    return topics


print(add_topic("functions"))
print(add_topic("defaults"))
```

Salida:

```text
['functions']
['defaults']
```

Cada omisión de `topics` produce primero `None`; después el cuerpo crea una lista nueva.

## 17. `None` actúa como centinela en este patrón

Aquí, `None` significa:

> No se proporcionó ninguna lista, así que crea una ahora.

```text
topics supplied?
├── yes → use that object
└── no  → default gives None
            ↓
        create a fresh list
```

Esto funciona cuando `None` no es por sí mismo un dato significativo para el parámetro.

Los centinelas personalizados son un tema avanzado de diseño de interfaz y quedan fuera de este capítulo.

## 18. Un objeto mutable proporcionado todavía puede modificarse

```python
def add_topic(topic: str, topics: list[str] | None = None) -> list[str]:
    if topics is None:
        topics = []

    topics.append(topic)
    return topics


planned = ["scope"]
result = add_topic("defaults", planned)

print(planned)
print(result)
```

Salida:

```text
['scope', 'defaults']
['scope', 'defaults']
```

El patrón seguro no copia un objeto proporcionado explícitamente por quien llama.

El estado predeterminado compartido y la mutación deliberada de datos del llamador son preguntas distintas.

## 19. Los argumentos posicionales y por palabra clave pueden reemplazar valores predeterminados

```python
def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(5, 3))
print(power(5, exponent=3))
```

Salida:

```text
25
125
125
```

Para configuraciones opcionales, un argumento por palabra clave suele dejar más clara la intención.

## 20. Las palabras clave permiten saltar valores predeterminados anteriores

```python
def export_summary(name, format="text", include_title=True):
    return f"{name}: {format}, title={include_title}"


print(export_summary("study", include_title=False))
```

Salida:

```text
study: text, title=False
```

No existe un espacio posicional vacío para “mantén este valor predeterminado, pero cambia el siguiente”.

Los argumentos por palabra clave permiten reemplazos selectivos.

## 21. `None` no es automáticamente el mejor valor predeterminado

Un valor predeterminado puede ser cualquier valor adecuado:

```python
def format_name(name, separator=", "):
    ...
```

Usa `None` cuando represente correctamente el caso de argumento omitido, especialmente para crear un objeto mutable nuevo.

No reemplaces todos los valores predeterminados por `None` mecánicamente.

## 22. Errores comunes

### Objeto mutable como valor predeterminado

Evita:

```python
def collect_item(item, items=[]):
    items.append(item)
    return items
```

Prefiere:

```python
def collect_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items
```

### Parámetro obligatorio después de uno con valor predeterminado

Evita:

```python
# SyntaxError
def connect(timeout=30, host):
    return host, timeout
```

Prefiere:

```python
def connect(host, timeout=30):
    return host, timeout
```

### Alternativa engañosa

Si `topic` es realmente obligatorio, no ocultes esa decisión:

```python
def study(topic):
    return topic
```

## 23. Seguir una llamada completa

```python
def create_title(topic: str, prefix: str = "Chapter", number: int = 1) -> str:
    return f"{prefix} {number}: {topic}"


title = create_title("Defaults", number=6)
print(title)
```

Seguimiento:

```text
1. call create_title("Defaults", number=6)
2. topic = "Defaults"
3. number = 6
4. prefix is unfilled
5. prefix receives stored default "Chapter"
6. body returns "Chapter 6: Defaults"
7. title receives that returned string
```

Todo parámetro tiene un valor antes de ejecutar el cuerpo, proveniente de un argumento proporcionado o de un valor predeterminado.

## 24. Ejemplo ejecutable: opciones de saludo

```python
def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"


print(greet("Avery"))
print(greet("Avery", greeting="Welcome"))
print(greet("Avery", punctuation="."))
```

Salida:

```text
Hello, Avery!
Welcome, Avery!
Hello, Avery.
```

## 25. Ejemplo ejecutable: cotización de envío

```python
def calculate_shipping(weight: float, rate: float = 2.5, handling: float = 3.0) -> float:
    return weight * rate + handling


print(calculate_shipping(4.0))
print(calculate_shipping(4.0, rate=3.0))
print(calculate_shipping(4.0, handling=0.0))
```

Salida:

```text
13.0
15.0
10.0
```

## 26. Ejemplo ejecutable: valor seguro para lista

```python
def add_task(task: str, tasks: list[str] | None = None) -> list[str]:
    if tasks is None:
        tasks = []

    tasks.append(task)
    return tasks


print(add_task("study"))
print(add_task("practice"))
print(add_task("review", ["plan"]))
```

Salida:

```text
['study']
['practice']
['plan', 'review']
```

Las dos primeras llamadas crean listas independientes. La tercera modifica deliberadamente la lista proporcionada.

## 27. Conexión con capítulos anteriores

```text
definition and call
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
required vs optional caller input
```

Los valores predeterminados no sustituyen los argumentos. Definen cómo recibe un valor un parámetro cuando su argumento se omite.

## 28. Checklist de diseño

Antes de añadir un valor predeterminado, pregunta:

- ¿Esta entrada es realmente opcional?
- ¿La alternativa es poco sorprendente?
- ¿Cambiarla después modifica un comportamiento importante?
- ¿El valor predeterminado es mutable?
- Si es mutable, ¿`None` debería provocar un objeto nuevo?
- ¿`None` es por sí mismo un dato significativo?
- ¿Un argumento por palabra clave haría la llamada más clara?
- ¿El type hint incluye `None` cuando `None` está admitido?

## 29. Límite de alcance

Este capítulo trata valores predeterminados comunes para parámetros normales de función.

No requiere:

- parámetros solo posicionales con `/`;
- diseño solo por palabra clave con `*`;
- `*args` y `**kwargs`;
- objetos centinela personalizados;
- decoradores;
- recursos avanzados de tipado;
- dataclasses o constructores de clases.

El siguiente capítulo presenta `*args` y `**kwargs`.

## 30. Ejercicio

Crea `build_reminder`.

Requisitos:

- `task` es obligatorio;
- `priority` tiene `"normal"` como valor predeterminado;
- `done` tiene `False` como valor predeterminado;
- usa type hints;
- devuelve una string formateada;
- haz una llamada usando ambos valores predeterminados;
- haz otra reemplazando solo `priority` por palabra clave.

```python
print(build_reminder("Study Python"))
print(build_reminder("Review functions", priority="high"))
```

### Desafío extra

Crea otra función con una lista opcional:

- no uses `[]` directamente como valor predeterminado;
- usa `None`;
- crea una lista nueva dentro del cuerpo;
- demuestra que dos llamadas sin lista no comparten estado.

## 31. Preguntas de repaso

1. ¿Qué significa `language="English"` en una definición?
2. ¿Cuándo usa Python un valor predeterminado?
3. ¿Qué ocurre cuando quien llama proporciona ese argumento?
4. ¿Por qué los parámetros obligatorios ordinarios suelen aparecer primero?
5. ¿Cuándo se evalúan las expresiones predeterminadas?
6. ¿Por qué `items=[]` puede compartir estado entre llamadas?
7. ¿Cómo evita ese problema el patrón con `None`?
8. ¿Un valor predeterminado valida un argumento?
9. ¿En qué se diferencian los type hints y los valores predeterminados?
10. ¿Por qué un valor predeterminado debe representar comportamiento realmente opcional?

## Referencia rápida

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
```

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"
```

```python
greet("Avery", greeting="Welcome")
```

```python
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items
```

```text
default
→ used when the corresponding argument is omitted

default expression
→ evaluated when the function definition executes

mutable default object
→ can be shared between calls

None sentinel pattern
→ create a fresh mutable object inside the body
```

## Ejemplos ejecutables

```bash
python functions/06-default-values/examples/greet_with_style.py
python functions/06-default-values/examples/shipping_quote.py
python functions/06-default-values/examples/safe_list_default.py
```

## Referencias

- [Python 3.13 Tutorial — Default Argument Values](https://docs.python.org/3.13/tutorial/controlflow.html#default-argument-values)
- [Python 3.13 Language Reference — Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13 Language Reference — Calls](https://docs.python.org/3.13/reference/expressions.html#calls)

---

Siguiente: **07. `*args` y `**kwargs`**.
