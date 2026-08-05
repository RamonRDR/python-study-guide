<div align="center">

# Docstrings en Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Comentarios](../01-comments/README.es.md)

Una docstring explica la finalidad y el uso público de un módulo, función, clase o método de Python. A diferencia de un comentario común, la docstring se almacena como documentación del objeto y puede ser leída por personas, editores, generadores de documentación, `help()` y herramientas de introspección.

> **Principio orientador:** Escribe una docstring para la persona que necesita utilizar el objeto correctamente sin leer toda su implementación.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Requisitos previos | Se recomienda una familiaridad básica con funciones. Los ejemplos de módulos, clases y métodos pueden comprenderse de forma conceptual antes de estudiar esos temas en profundidad |
| Tiempo estimado de estudio | 45 a 65 minutos |
| Conceptos principales | docstring, `__doc__`, `help()`, `inspect.getdoc()`, módulos, funciones, clases, métodos, parámetros, valores de retorno, excepciones, PEP 257 |

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías ser capaz de:

- diferenciar una docstring de un comentario y de un literal de string sin función documental;
- colocar docstrings correctamente en módulos, funciones, clases y métodos;
- escribir docstrings útiles de una línea y de varias líneas;
- documentar comportamiento, parámetros, retornos, excepciones, efectos secundarios y restricciones cuando sean relevantes;
- acceder a la documentación mediante `__doc__`, `help()` e `inspect.getdoc()`;
- comprender la relación entre docstrings, type hints, archivos README y documentación externa;
- reconocer que PEP 257 define convenciones generales, pero no impone un único estilo universal de marcado;
- revisar docstrings considerando exactitud, claridad, privacidad y facilidad de mantenimiento.

## 1. Qué es una docstring

Una docstring es un literal de string que aparece como la primera instrucción dentro de un módulo, función, clase o método.

```python
def greet(name):
    """Return a greeting for the provided name."""
    return f"Hello, {name}!"
```

Como la string está en la posición correcta, Python la almacena en el atributo `__doc__` de la función:

```python
print(greet.__doc__)
```

Salida:

```text
Return a greeting for the provided name.
```

El mismo texto con comillas triples en otra posición es solamente una expresión de string:

```python
def greet(name):
    result = f"Hello, {name}!"
    """This is not the function docstring."""
    return result
```

En este caso, `greet.__doc__` es `None`, porque la string no es la primera instrucción.

### Las comillas triples no crean automáticamente una docstring

Las comillas triples crean un literal de string. La posición es lo que le da a esa string su función documental.

```python
message = """A regular multi-line string."""
```

Este es un valor normal asignado a `message`, no una docstring.

## 2. Por qué existen las docstrings

La firma y la implementación de una función pueden mostrar cómo funciona el código, pero quienes la utilizan todavía necesitan una explicación estable sobre cómo llamarla de forma segura.

Considera:

```python
def calculate_fee(amount, priority=False):
    ...
```

La firma no responde completamente:

- ¿Qué representa `amount`?
- ¿Qué unidad o moneda se espera?
- ¿Qué cambia cuando `priority` es `True`?
- ¿Qué se devuelve?
- ¿La función puede generar una excepción?
- ¿Modifica algún estado externo?

Una docstring puede describir ese contrato público sin obligar a cada persona a inspeccionar la implementación.

```python
def calculate_fee(amount_cents, priority=False):
    """Return the fictional service fee in cents.

    Args:
        amount_cents: Positive base amount expressed in cents.
        priority: Whether to apply the fictional priority rate.

    Returns:
        The calculated fee in cents.

    Raises:
        ValueError: If amount_cents is not positive.
    """
```

El código continúa siendo la fuente del comportamiento ejecutable. La docstring es el mapa legible del uso previsto de la interfaz.

## 3. Colocación correcta

### Docstrings de módulos

Una docstring de módulo normalmente aparece al comienzo de un archivo Python, después de un *shebang* o declaración de codificación cuando alguno exista, y antes de los imports.

```python
"""Utilities for the fictional reading-progress examples."""

from pathlib import Path
```

La docstring de módulo puede resumir la finalidad del archivo y sus principales objetos públicos.

### Docstrings de funciones

La docstring de una función es la primera instrucción después de la cabecera de la función.

```python
def convert_minutes_to_seconds(minutes):
    """Return the provided duration converted to seconds."""
    return minutes * 60
```

### Docstrings de clases

La docstring de una clase describe su responsabilidad, comportamiento importante y expectativas públicas.

```python
class ReadingProgress:
    """Track completed pages in a fictional reading session."""
```

### Docstrings de métodos

La docstring de un método explica lo que hace desde el punto de vista de quien lo llama.

```python
class ReadingProgress:
    """Track completed pages in a fictional reading session."""

    def record_pages(self, pages):
        """Add completed pages without exceeding the total page count."""
```

La docstring de la clase explica el objeto como un todo. Las docstrings de los métodos explican operaciones individuales.

## 4. Docstrings de una línea

Utiliza una docstring de una línea cuando la finalidad del objeto sea simple y pueda expresarse con exactitud en una frase breve.

```python
def is_even(value):
    """Return whether value is an even integer."""
    return value % 2 == 0
```

Convenciones útiles de PEP 257 incluyen:

- utilizar comillas dobles triples incluso para una sola línea;
- mantener las comillas de apertura y cierre en la misma línea;
- escribir una frase completa terminada en punto;
- describir el efecto o resultado en lugar de repetir la firma.

Evita:

```python
def is_even(value):
    """is_even(value) -> bool"""
```

La firma ya muestra el nombre del parámetro, y los type hints pueden mostrar los tipos esperados. La docstring debe añadir significado.

## 5. Docstrings de varias líneas

Utiliza una docstring de varias líneas cuando quienes usan el objeto necesiten más que un resumen.

```python
def calculate_average(values):
    """Return the arithmetic mean of a non-empty sequence.

    Args:
        values: Numeric values included in the calculation.

    Returns:
        The arithmetic mean.

    Raises:
        ValueError: If values is empty.
    """
```

Una estructura práctica es:

1. una línea breve de resumen;
2. una línea en blanco;
3. una explicación adicional;
4. secciones estructuradas cuando el proyecto las utilice.

El resumen debe seguir siendo útil por sí solo, porque editores y herramientas de documentación pueden mostrar únicamente esa primera línea.

## 6. Qué pertenece a una docstring útil

No todas las funciones necesitan todas las secciones posibles. Documenta lo que quien llama al objeto necesita saber.

### Finalidad y comportamiento

Indica lo que ofrece el objeto.

```python
def normalize_identifier(raw_value):
    """Normalize a fictional identifier for display."""
```

### Parámetros

Explica significado, unidades, formatos aceptados y restricciones importantes que los nombres y type hints no expresen completamente.

```python
def schedule_retry(delay_seconds):
    """Schedule a retry after a non-negative delay.

    Args:
        delay_seconds: Waiting time in seconds. Zero schedules an immediate retry.
    """
```

### Valor de retorno

Explica el significado del valor devuelto, especialmente cuando sean posibles `None`, valores centinela, unidades o resultados diferentes.

```python
def find_label(code):
    """Return the matching label, or None when the code is unknown."""
```

### Excepciones

Documenta excepciones que formen parte del contrato público y que quienes llaman puedan manejar razonablemente.

```python
def load_percentage(text):
    """Convert text to a percentage from 0 through 100.

    Raises:
        ValueError: If text is not numeric or is outside the accepted range.
    """
```

No prometas todas las excepciones internas que podrían escapar en cualquier situación. Concéntrate en el comportamiento intencional y relevante.

### Efectos secundarios

Menciona cambios importantes que ocurran además del valor devuelto.

```python
def save_report(path, content):
    """Write content to path, replacing an existing file."""
```

El comportamiento de reemplazo importa aunque la implementación sea simple.

### Restricciones y supuestos

Documenta requisitos que no puedan inferirse con seguridad.

```python
def compare_snapshots(left, right):
    """Compare snapshots created with the same schema version."""
```

## 7. Docstrings para diferentes objetos

| Objeto | Enfoque habitual de la documentación |
|---|---|
| Módulo | Finalidad, principales objetos públicos, notas importantes de uso o configuración |
| Función | Comportamiento, parámetros, retorno, excepciones, efectos secundarios y restricciones |
| Clase | Responsabilidad, expectativas de construcción, estado importante y comportamiento público |
| Método | Operación realizada, cambios de estado, resultado y excepciones |
| Propiedad | Significado del valor expuesto y restricciones relevantes |
| Script | Finalidad, uso desde la línea de comandos, entradas, salidas, entorno y comportamiento de salida cuando sea relevante |

Los objetos públicos normalmente necesitan documentación más sólida que pequeños auxiliares privados cuyos nombres y contexto ya sean claros. La política del proyecto determina el límite exacto.

## 8. Docstrings, comentarios, type hints y archivos README

Estos recursos cooperan en lugar de competir.

```python
def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers."""
```

- El **nombre** comunica la intención principal.
- Los **type hints** describen las formas de datos esperadas.
- La **docstring** explica el comportamiento y las expectativas públicas.
- Un **comentario** puede explicar una decisión de implementación no evidente.
- Un **README o guía** puede enseñar un flujo mayor que involucre varios objetos.

No dupliques la misma frase en todas partes. Coloca cada información donde su público la buscará de forma natural.

## 9. Acceso a docstrings durante la ejecución

### `__doc__`

Los objetos documentados exponen el texto mediante `__doc__`.

```python
print(calculate_average.__doc__)
```

Cuando no existe una docstring válida, `__doc__` normalmente será `None`.

### `help()`

El sistema de ayuda incorporado utiliza la documentación y los metadatos disponibles del objeto.

```python
help(calculate_average)
```

Esto resulta útil en una sesión interactiva de Python. La presentación completa puede variar según el entorno.

### `inspect.getdoc()`

`inspect.getdoc()` recupera y limpia el texto de documentación.

```python
from inspect import getdoc

print(getdoc(calculate_average))
```

La función elimina la indentación común y puede recuperar documentación heredada para algunas categorías de objetos cuando no se ha definido una docstring propia.

## 10. Estilos y herramientas de documentación

Python define qué es una docstring, pero no exige un único formato universal para secciones como parámetros y retornos.

Algunos ecosistemas comunes son:

- texto simple siguiendo PEP 257;
- secciones de estilo Google, como `Args`, `Returns` y `Raises`;
- encabezados de estilo NumPy;
- campos en reStructuredText utilizados por herramientas como Sphinx.

Estas son convenciones de documentación, no sintaxis diferentes de Python.

Esta guía utiliza una estructura compacta inspirada en el estilo Google en los ejemplos más extensos porque es accesible para principiantes. Un proyecto real debe elegir un estilo, registrar la decisión y aplicarla de forma coherente.

### PEP 257 y herramientas de formato

PEP 257 describe convenciones generales y la semántica de las docstrings. Linters y generadores de documentación pueden añadir reglas más estrictas y específicas del proyecto. Una advertencia de una herramienta debe entenderse dentro de la configuración de esa herramienta, no confundirse con un error de sintaxis de Python.

## 11. Cuándo una docstring es innecesaria o perjudicial

### No repitas el nombre

```python
def add(a, b):
    """Add a and b."""
    return a + b
```

Esto puede ser aceptable en un ejemplo didáctico deliberadamente pequeño, pero añade poco valor en documentación de producción.

Una docstring mejor agregaría un contrato no evidente, o la función podría quedar sin docstring si fuera un auxiliar privado y trivial según la política del proyecto.

### No documentes un comportamiento falso

```python
def retry():
    """Retry the operation three times."""
    max_attempts = 5
```

Una docstring desactualizada es una trampa bien pulida. Actualiza la documentación siempre que cambie el comportamiento.

### No copies la implementación en prosa

Evita narrar cada línea. Documenta la interfaz y las garantías no evidentes.

### No expongas información privada

Las docstrings forman parte del código fuente. Pueden aparecer en editores, sitios generados, paquetes, logs o repositorios públicos.

Nunca incluyas credenciales, URLs privadas, datos personales, reglas de negocio confidenciales ni detalles internos propietarios. Utiliza ejemplos originales y ficticios.

### No utilices una docstring como excusa para una interfaz confusa

Nombres mejores, funciones más pequeñas, type hints y un diseño más simple pueden resolver el problema antes de añadir documentación.

## 12. Ejemplo básico

```python
def format_name(first_name, last_name):
    """Return a display name with surrounding whitespace removed."""
    return f"{first_name.strip()} {last_name.strip()}"
```

La docstring añade una garantía útil: se eliminan los espacios externos. No narra la f-string.

## 13. Ejemplo práctico

```python
def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers.

    Args:
        values: Numbers included in the calculation.

    Returns:
        The arithmetic mean of the provided values.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)
```

La docstring comunica:

- la entrada no puede estar vacía;
- el resultado representa una media aritmética;
- quienes llaman pueden esperar un `ValueError` para una secuencia vacía.

Consulta el ejemplo ejecutable completo en [`examples/function_docstrings.py`](examples/function_docstrings.py).

## 14. Errores comunes

### Colocar la string después de código ejecutable

Solo la primera instrucción se convierte en la docstring del objeto.

### Confundir comentarios con docstrings

Un comentario no está disponible mediante la documentación normal del objeto:

```python
# Return the arithmetic mean.
def calculate_average(values):
    ...
```

### Repetir type hints sin añadir significado

Débil:

```python
def load_items(limit: int) -> list[str]:
    """limit is an int and returns a list of strings."""
```

Mejor:

```python
def load_items(limit: int) -> list[str]:
    """Return at most limit fictional item labels in display order."""
```

### Documentar detalles internos como garantías permanentes

Evita prometer un algoritmo interno específico a menos que quienes utilizan el objeto puedan depender de él.

### Mezclar estilos sin coherencia dentro del mismo proyecto

La consistencia ayuda a lectores y herramientas. Sigue la convención documentada en el repositorio.

### Olvidar constructores y métodos públicos

Una clase bien descrita, pero con requisitos de construcción sin explicar, sigue siendo difícil de utilizar.

## 15. Ejemplos en este repositorio

| Archivo | Objetivo |
|---|---|
| [`function_docstrings.py`](examples/function_docstrings.py) | Muestra docstrings de módulo y función, parámetros, retornos, excepciones y `__doc__` |
| [`class_docstrings.py`](examples/class_docstrings.py) | Muestra docstrings de clase, constructor y métodos |
| [`inspect_docstrings.py`](examples/inspect_docstrings.py) | Muestra el acceso limpio durante la ejecución con `inspect.getdoc()` |

Ejecuta un ejemplo desde la raíz del repositorio:

```bash
python comments-and-documentation/02-docstrings/examples/function_docstrings.py
```

En sistemas donde el comando se llama `python3`:

```bash
python3 comments-and-documentation/02-docstrings/examples/function_docstrings.py
```

## 16. Ejercicio

Revisa esta función:

```python
def reserve_seats(available, requested):
    if requested <= 0:
        raise ValueError("requested must be positive")
    if requested > available:
        return False
    return True
```

Escribe una docstring que explique:

1. la finalidad de la función;
2. qué representan `available` y `requested`;
3. qué significan `True` y `False`;
4. cuándo se genera `ValueError`;
5. ninguna regla ficticia más allá de lo que el código realmente garantiza.

Una posible respuesta:

```python
def reserve_seats(available, requested):
    """Return whether the requested number of fictional seats is available.

    Args:
        available: Number of seats currently available.
        requested: Positive number of seats requested.

    Returns:
        True when all requested seats are available; otherwise False.

    Raises:
        ValueError: If requested is not positive.
    """
    if requested <= 0:
        raise ValueError("requested must be positive")
    if requested > available:
        return False
    return True
```

Varias redacciones pueden ser correctas. La exactitud importa más que el detalle decorativo.

## 17. Lista de revisión de docstrings

Antes de aprobar una docstring, pregunta:

- ¿Está en la posición correcta?
- ¿El resumen explica la finalidad o el comportamiento?
- ¿La documentación coincide con el código actual?
- ¿Las unidades, rangos, valores centinela y restricciones importantes están claros?
- ¿Se documentaron retornos, excepciones y efectos secundarios relevantes?
- ¿Evita repetir la firma y la implementación evidente?
- ¿Sigue el estilo elegido por el proyecto?
- ¿Un nombre mejor o una interfaz más simple podría eliminar parte de la explicación?
- ¿Existe alguna información privada, propietaria, personal o identificable?
- ¿Una persona sabría utilizar el objeto correctamente sin leer todas las líneas?

## 18. Resumen de consulta rápida

| Situación | Enfoque preferido |
|---|---|
| Función pública simple con un contrato evidente | Utiliza una docstring breve de una línea |
| El comportamiento requiere explicar parámetros, retornos o excepciones | Utiliza una docstring de varias líneas |
| La información trata sobre una decisión de implementación | Utiliza un comentario |
| La información trata sobre tipos esperados | Utiliza type hints y aclara en la docstring cuando todavía falte significado |
| Un flujo abarca varios módulos o pasos de configuración | Utiliza un README o guía |
| La documentación debe consultarse de forma interactiva | Utiliza `help()`, `__doc__` o `inspect.getdoc()` |
| La docstring repite la firma | Sustituye la repetición por comportamiento y garantías |
| La implementación cambia | Revisa y actualiza la docstring en el mismo cambio |
| Un proyecto utiliza estilo Google, NumPy o reStructuredText | Sigue la convención elegida de forma coherente |

## Referencias oficiales

- [Modelo de datos de Python: atributos `__doc__`](https://docs.python.org/es/3/reference/datamodel.html)
- [Función incorporada de Python: `help()`](https://docs.python.org/es/3/library/functions.html#help)
- [Python `inspect.getdoc()`](https://docs.python.org/es/3/library/inspect.html#inspect.getdoc)
- [PEP 257: convenciones de docstrings](https://peps.python.org/pep-0257/)
- [PEP 8: strings de documentación](https://peps.python.org/pep-0008/#documentation-strings)

## Principio final

Una docstring útil describe el contrato que necesita quien lee. Debe revelar la finalidad y las garantías importantes sin convertir la implementación en una segunda copia frágil escrita en prosa.
