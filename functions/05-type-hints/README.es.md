<div align="center">

# Type Hints

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Anterior: Alcance](../04-scope/README.es.md)

Los capítulos anteriores establecieron definición, entradas, retornos y alcance. Este capítulo añade la descripción de tipos en la interfaz:

> ¿Cómo puede una función describir los tipos de valores que espera recibir y devolver?

```text
function interface
├── parameter names
├── parameter type hints
└── return type hint
        ↓
function body still runs as ordinary Python
```

**Tiempo estimado de estudio:** 75–100 minutos.

**Versión de Python:** este capítulo requiere **Python 3.10 o posterior**.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué comunica una type hint;
- anotar parámetros con `name: type`;
- anotar retornos con `-> type`;
- explicar que Python no impone las type hints en runtime por sí mismo;
- distinguir hints de validación en runtime y conversión;
- usar `str`, `int`, `float`, `bool` y `None` en firmas simples;
- anotar el contenido de listas, diccionarios y tuplas;
- usar `str | None` para un resultado simple valor-o-`None`;
- leer una firma tipada como una interfaz compacta;
- mantener las hints alineadas con el comportamiento real de la función.

## 1. Las type hints describen tipos esperados

Una **type hint** es información añadida al código que describe el tipo que se espera que tenga un valor.

Una función tipada básica se ve así:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


message = greet("Avery")
print(message)
```

Salida:

```text
Hello, Avery
```

Lee la firma así:

```text
name: str → se espera que el parámetro reciba una string
-> str    → se espera que la función devuelva una string
```

Las hints hacen visible el flujo de datos previsto.

## 2. Las anotaciones de parámetros usan dos puntos

Una hint de parámetro aparece después del nombre del parámetro:

```text
parameter_name: type
```

Los dos puntos anotan el parámetro existente.

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


print(calculate_total(12.5, 4))
```

Salida:

```text
50.0
```

La firma comunica `price → float`, `quantity → int` y `return → float`.

## 3. Las anotaciones de retorno usan una flecha

Una hint de retorno aparece después de la lista de parámetros:

```text
def function_name(...) -> return_type:
```

La flecha describe el resultado esperado; no convierte valores.

```python
def is_passing(score: int) -> bool:
    return score >= 60


print(is_passing(72))
print(is_passing(45))
```

Salida:

```text
True
False
```

## 4. Las type hints no imponen tipos en runtime por sí solas

Esta es la regla más importante del capítulo.

Python no rechaza automáticamente una llamada solo porque un argumento no coincida con una type hint:

```python
def echo_text(value: str) -> str:
    return value


result = echo_text(42)

print(result)
print(type(result).__name__)
```

Salida:

```text
42
int
```

La ejecución normal todavía acepta `42` porque el cuerpo lo devuelve. Un IDE o verificador estático puede advertirlo, pero la anotación sola no valida en runtime.

## 5. Las type hints no convierten valores

Una hint describe un tipo esperado; no ejecuta conversores.

```python
def add_tax(amount: float) -> float:
    return amount * 1.1


print(add_tax(100.0))
```

Mantén los conceptos separados:

```text
type hint  → describe
conversion → transforma explícitamente un valor compatible
validation → comprueba un valor o una regla real
```

## 6. Type hints y validación en runtime resuelven problemas diferentes

El tipado estático razona sobre tipos declarados antes o mientras escribes código; la validación en runtime comprueba valores reales mientras el programa se ejecuta.

Este ejemplo contiene ambas ideas:

```python
def set_username(username: str) -> str:
    if not isinstance(username, str):
        raise TypeError("username must be a str")

    return username


print(set_username("Avery"))
```

`username: str` documenta el tipo previsto. `isinstance(username, str)` participa en la comprobación en runtime.

Usar `str` aquí mantiene el ejemplo enfocado. Una comprobación como `isinstance(value, int)` tiene un detalle adicional importante para principiantes: `bool` es una subclase de `int` en Python.

No añadas validación en todas partes solo porque una función tenga anotaciones. Valida donde las fronteras o reglas reales del programa lo requieran.

## 7. Los tipos incorporados suelen ser suficientes

Para firmas básicas suelen bastar `str`, `int`, `float` y `bool`, sin importar `typing`.

```python
def build_label(topic: str, chapter: int) -> str:
    return f"Chapter {chapter}: {topic}"


label = build_label("Type Hints", 5)
print(label)
```

Salida:

```text
Chapter 5: Type Hints
```

## 8. `-> None` describe ausencia de retorno útil

Usa `-> None` cuando una función no está diseñada para devolver un resultado útil a quien la llama:

```python
def show_status(status: str) -> None:
    print(f"Status: {status}")


show_status("ready")
```

Se conecta con el Capítulo 03: una función sin otro resultado útil produce `None`.

## 9. Las colecciones pueden describir tipos de elementos

Python moderno puede describir también el tipo esperado de los elementos:

```python
def first_topic(topics: list[str]) -> str:
    return topics[0]


print(first_topic(["scope", "type hints", "defaults"]))
```

Lee `list[str]` como “una lista cuyos elementos esperados son strings”.

## 10. Los diccionarios describen tipos de claves y valores

```python
def total_scores(scores: dict[str, int]) -> int:
    return sum(scores.values())


print(total_scores({"Avery": 8, "Jordan": 9}))
```

`dict[str, int]` comunica:

```text
keys   → expected str
values → expected int
```

La hint no inspecciona automáticamente cada elemento en runtime.

## 11. Las hints de tupla pueden describir múltiples resultados

```python
def min_and_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


print(min_and_max([4, 8, 2, 9]))
```

`tuple[int, int]` describe dos elementos enteros esperados y encaja con los retornos del Capítulo 03.

## 12. `str | None` describe un resultado valor-o-`None`

```python
def find_topic(topics: list[str], target: str) -> str | None:
    for topic in topics:
        if topic == target:
            return topic

    return None


print(find_topic(["scope", "type hints"], "type hints"))
print(find_topic(["scope", "type hints"], "files"))
```

Salida:

```text
type hints
None
```

`str | None` significa que el resultado esperado puede ser una string o `None`. La barra vertical expresa una unión de tipos permitidos.

El código más antiguo puede expresar la misma idea como `typing.Optional[str]`. Esta guía usa Python moderno, por lo que aquí se prefiere `str | None`. Por ahora solo necesitas reconocer la forma antigua cuando aparezca.

## 13. Las firmas tipadas etiquetan el flujo de datos que ya conoces

```python
def summarize_scores(scores: list[int]) -> tuple[int, int]:
    lowest = min(scores)
    highest = max(scores)
    return lowest, highest


result = summarize_scores([72, 88, 91])
print(result)
```

Sigue la interfaz:

```text
caller
↓
list[int]
↓
parameter
↓
function-local work
↓
tuple[int, int]
↓
caller
```

Las hints describen, no sustituyen, esas fronteras.

## 14. Las hints deben coincidir con el comportamiento real

```python
def format_score(score: int) -> str:
    return f"Score: {score}"


print(format_score(95))
```

`score: int -> str` coincide con la implementación. Una hint obsoleta crea confianza falsa.

## 15. También existen anotaciones de variables

```python
course: str = "Python"
chapter: int = 5

print(course)
print(chapter)
```

El foco son las interfaces. Anota variables locales solo cuando aporte claridad o soporte de herramientas.

## 16. Las anotaciones son metadatos de la función

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


print(greet.__annotations__)
```

En Python 3.13, las anotaciones de función están disponibles mediante el mapping `__annotations__` del objeto función.

La representación impresa exacta importa menos que la idea de que las herramientas pueden inspeccionar esos metadatos. El código para principiantes normalmente lee las hints en el código fuente en lugar de usar `__annotations__` directamente.

## 17. El análisis estático y el runtime están separados

Un verificador de tipos puede marcar esta llamada antes de ejecutarla:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


greet(42)
```

Python todavía puede ejecutarla si las operaciones del cuerpo aceptan el objeto.

```text
static analysis → reasons about declared types
runtime         → executes Python objects and operations
```

## 18. Los editores y herramientas pueden usar hints

Las herramientas con soporte de tipos pueden usar hints para advertencias, autocompletado, información al pasar el cursor, navegación y apoyo a refactorizaciones.

Las funciones exactas dependen de la herramienta y de su configuración. La característica del lenguaje sigue siendo la misma: las anotaciones describen la interfaz prevista.

## 19. Las fronteras de funciones son un lugar de alto valor para hints

Compara:

```python
def summarize(scores):
    ...
```

con:

```python
def summarize(scores: list[int]) -> str:
    ...
```

La segunda firma aclara qué pasar y qué esperar de vuelta.

## 20. No anotes todo solo porque puedes

Esto es válido:

```python
def double(number: int) -> int:
    result: int = number * 2
    return result
```

La anotación local puede aportar poco porque la expresión ya hace evidente `result`.

Prefiere hints que aclaren interfaces y valores no obvios. Evita convertir una función pequeña en un laberinto de etiquetas redundantes.

## 21. Una type hint no es una regla de dominio

`value: int` puede comunicar que se espera un entero. Por sí solo, no comunica ni impone un rango como:

```text
0 <= value <= 100
```

Tipos y reglas de dominio son distintos. Comprueba en runtime las reglas que deban cumplirse al ejecutar.

## 22. Errores comunes

### Error 1: esperar enforcement automático en runtime

```python
def echo(value: str) -> str:
    return value


echo(10)
```

La anotación por sí sola no es una guarda de runtime.

### Error 2: esperar conversión automática

```python
def parse_count(count: int) -> int:
    return count
```

Pasar `"5"` no crea automáticamente el entero `5`.

### Error 3: anotar el tipo de retorno incorrecto

```python
def label(score: int) -> int:
    return f"Score: {score}"
```

La implementación devuelve una string, así que `-> int` es engañoso.

### Error 4: asumir que las type hints prueban que el algoritmo es correcto

Una función perfectamente anotada todavía puede contener lógica incorrecta.

## 23. Un ejemplo práctico

```python
def progress_message(completed: int, total: int) -> str:
    percentage = completed / total * 100
    return f"{percentage:.0f}% complete"


print(progress_message(4, 5))
```

Salida:

```text
80% complete
```

La firma aclara `completed → int`, `total → int` y `return → str`; el cuerpo realiza el cálculo.

## Ejemplos ejecutables

El capítulo incluye tres ejemplos aprobados para ejecución automática:

### `annotated_greeting.py`

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


message = greet("Avery")

print(message)
```

```text
Hello, Avery
```

### `collection_summary.py`

```python
def summarize_topics(topics: list[str]) -> str:
    return f"{len(topics)} topics: {', '.join(topics)}"


print(summarize_topics(["scope", "type hints", "defaults"]))
```

```text
3 topics: scope, type hints, defaults
```

### `runtime_does_not_enforce.py`

```python
def echo_text(value: str) -> str:
    return value


result = echo_text(42)

print(result)
print(type(result).__name__)
```

```text
42
int
```

El último ejemplo pasa deliberadamente un `int` a un parámetro anotado como `str`. Python ejecuta la llamada porque las anotaciones no imponen el tipo por sí solas.

## 24. Ejercicio

Crea `build_summary`.

Requisitos:

1. Recibe `topic` como string.
2. Recibe `scores` como una lista de enteros.
3. Devuelve una string.
4. Añade hints a ambos parámetros y al retorno.
5. Produce este resultado para la llamada de ejemplo:

```python
print(build_summary("Python", [8, 9, 10]))
```

```text
Python: 3 scores
```

Antes de ejecutarlo, explica esas tres hints y si Python rechazaría automáticamente argumentos incompatibles en runtime.

## 25. Una posible solución

```python
def build_summary(topic: str, scores: list[int]) -> str:
    return f"{topic}: {len(scores)} scores"


print(build_summary("Python", [8, 9, 10]))
```

Salida:

```text
Python: 3 scores
```

## 26. Lista de revisión

Antes de continuar, asegúrate de poder explicar:

- [ ] qué comunica una type hint;
- [ ] la sintaxis de parámetro con `:`;
- [ ] la sintaxis de retorno con `->`;
- [ ] por qué las hints no imponen tipos en runtime por sí solas;
- [ ] por qué las hints no convierten valores;
- [ ] hints frente a validación en runtime;
- [ ] `-> None`;
- [ ] `list[str]`;
- [ ] `dict[str, int]`;
- [ ] `tuple[int, int]`;
- [ ] `str | None`;
- [ ] por qué las hints deben coincidir con el comportamiento real;
- [ ] por qué no toda variable local necesita una anotación.

## 27. Consulta rápida

| Objetivo | Sintaxis | Significado |
|---|---|---|
| Anotar parámetro | `name: str` | argumento string esperado |
| Anotar retorno | `-> int` | resultado entero esperado |
| Sin resultado útil | `-> None` | quien llama no debería esperar resultado útil |
| Lista de strings | `list[str]` | elementos string esperados |
| Diccionario | `dict[str, int]` | claves string, valores enteros |
| Tupla de dos enteros | `tuple[int, int]` | dos elementos enteros esperados |
| String o `None` | `str | None` | cualquiera de los resultados es esperado |
| Validación en runtime | código explícito | comprueba valores reales en ejecución |
| Conversión | `int(value)`, etc. | crea explícitamente un valor convertido |

## Límite de alcance

Este capítulo deja intencionalmente para más adelante:

- `TypeVar` y parámetros de tipo genéricos;
- `Protocol` y subtipado estructural;
- overloads;
- `Literal` y `TypedDict`;
- aliases de tipo avanzados;
- tipado de callables y funciones de orden superior;
- herramientas de estrechamiento de tipos como `TypeGuard` y `TypeIs`;
- configuración de verificadores estáticos específicos;
- bibliotecas de validación en runtime.

Estos temas son útiles, pero requieren más contexto que un primer capítulo sobre anotaciones de funciones.

## 28. Qué viene después

Ahora tienes este modelo de función:

```text
define behavior
↓
receive arguments through parameters
↓
work inside local scope
↓
return results
↓
describe the interface with type hints
```

El próximo capítulo añade **Valores Predeterminados**, haciendo opcionales algunos argumentos de llamada.

[← Anterior: Alcance](../04-scope/README.es.md) · [Volver a Funciones](../README.es.md)

## Referencias

Documentación primaria de Python:

- [Python 3.13 `typing` — Support for type hints](https://docs.python.org/3.13/library/typing.html)
- [Python 3.13 Data model — anotaciones de función y `__annotations__`](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13 Tipos incorporados — relación entre `bool` e `int`](https://docs.python.org/3.13/library/stdtypes.html)
