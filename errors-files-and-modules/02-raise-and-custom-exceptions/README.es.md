<div align="center">

# Lanzar Excepciones y Crear Excepciones Personalizadas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Errores, Archivos y Módulos](../README.es.md) · [← Capítulo anterior: Manejo de Excepciones](../01-try-except-else-finally/README.es.md)

El Capítulo 01 se concentró en **manejar excepciones que ya ocurren**. Este capítulo añade el otro lado del contrato: decidir cuándo tu propio código debe informar deliberadamente que una operación no puede continuar normalmente.

Python usa la instrucción `raise` para ese propósito. Una función puede validar sus entradas o su estado, lanzar una excepción apropiada cuando no puede cumplir su contrato y dejar que un llamador decida dónde corresponde la recuperación o la explicación.

El capítulo también introduce **clases de excepción personalizadas**. Esta es una introducción limitada a la herencia de clases específicamente para excepciones, no un capítulo completo de programación orientada a objetos.

**Tiempo estimado de estudio:** 90–120 minutos.

**Requisito de Python:** Python 3.10 o posterior. Los ejemplos reutilizan anotaciones modernas como `list[str]` y los conceptos de manejo de excepciones del Capítulo 01.

## Objetivos de aprendizaje

Al terminar este capítulo, deberías poder:

- explicar la diferencia entre manejar una excepción y lanzarla;
- usar `raise` para señalar deliberadamente un valor o estado inválido;
- elegir una excepción built-in adecuada para fallos comunes de validación;
- escribir mensajes de excepción útiles sin tratar el texto del mensaje como una API programática;
- explicar por qué lanzar una excepción interrumpe la ruta normal actual;
- dejar que las excepciones se propaguen hasta una capa que pueda manejarlas de forma significativa;
- volver a lanzar la excepción que se está manejando con un `raise` sin expresión;
- traducir una excepción en otra con `raise ... from ...`;
- explicar el propósito del encadenamiento explícito de excepciones;
- definir una clase de excepción personalizada simple;
- elegir cuándo una excepción personalizada añade significado útil al dominio;
- capturar una excepción personalizada sin ocultar fallos no relacionados;
- distinguir `raise` de `assert`;
- evitar diseños de excepción amplios, vagos o innecesarios.

## 1. Manejar y lanzar son responsabilidades diferentes

El Capítulo 01 usó `except` para responder a un fallo:

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

Este capítulo se concentra en el código que **crea deliberadamente la señal de fallo**:

```python
if score < 0:
    raise ValueError("score cannot be negative")
```

Las dos responsabilidades se conectan así:

```text
la función llamada detecta una condición que no puede aceptar
        ↓
la función llamada lanza una excepción
        ↓
la ejecución normal de esa llamada se interrumpe
        ↓
la excepción se propaga hacia afuera
        ↓
un llamador adecuado puede manejarla
```

Una función no necesita saber cómo se recuperará cada llamador. Necesita informar el fallo con suficiente precisión para que los llamadores puedan tomar esa decisión.

## 2. La sintaxis básica de `raise`

La forma más común para principiantes es:

```python
raise ValueError("score must be between 0 and 100")
```

`ValueError` es la clase de excepción. El texto que se le pasa se convierte en información de diagnóstico útil transportada por la instancia de excepción.

La sintaxis general también permite volver a lanzar y encadenar excepciones, temas que aparecen más adelante en este capítulo.

## 3. Lanzar una excepción interrumpe la ruta normal actual

Considera:

```python
def validate_score(score: int) -> int:
    if score > 100:
        raise ValueError("score cannot exceed 100")
    print("Validation finished")
    return score
```

Si `score` es `120`, la ejecución llega a `raise`. El `print()` y el `return` posteriores no se ejecutan en esa llamada, a menos que la excepción se maneje dentro de alguna estructura circundante antes de que el control la abandone.

Conceptualmente:

```text
score = 120
    ↓
la condición es verdadera
    ↓
raise ValueError(...)
    ↓
la ruta normal termina aquí
    ↓
buscar hacia afuera un handler coincidente
```

Este es el mismo modelo de propagación estudiado en el Capítulo 01, pero ahora tu propio código inicia deliberadamente la ruta excepcional.

## 4. Lanza una excepción cuando una función no pueda cumplir su contrato

Una forma útil de pensar en la validación es mediante el contrato de la función.

Supón que esta función promete aceptar solo porcentajes de 0 a 100:

```python
def normalize_percentage(value: int) -> int:
    if not 0 <= value <= 100:
        raise ValueError("value must be between 0 and 100")
    return value
```

Para `75`, la función puede cumplir su contrato y retorna normalmente.

Para `130`, retornar el valor como si todo fuera válido violaría el contrato. Lanzar `ValueError` hace explícito el estado inválido.

## 5. Las guard clauses mantienen las rutas inválidas cerca del inicio

La validación suele leerse con claridad cuando los casos inválidos se rechazan primero:

```python
def calculate_average(total: float, count: int) -> float:
    if count <= 0:
        raise ValueError("count must be greater than zero")
    return total / count
```

El primer `if` es una **guard clause**. Protege la ruta válida frente a una precondición inválida conocida.

Este patrón suele hacer más legible la operación principal:

```text
¿precondición inválida? → lanzar excepción
en caso contrario        → continuar el trabajo normal
```

Una guard clause es un patrón de diseño, no sintaxis especial de Python.

## 6. `ValueError` es apropiado para muchos valores inválidos

`ValueError` es útil cuando un argumento tiene una clase general de valor aceptable, pero su valor específico es inválido para la operación.

Ejemplos:

```python
def set_progress(progress: int) -> int:
    if not 0 <= progress <= 100:
        raise ValueError("progress must be between 0 and 100")
    return progress
```

y:

```python
def choose_level(level: str) -> str:
    if level not in {"beginner", "intermediate", "advanced"}:
        raise ValueError("unsupported level")
    return level
```

La pregunta importante no es solo "¿Python puede almacenar este valor?". La pregunta es "¿este valor es válido para el contrato de esta función?".

## 7. `TypeError` puede describir un tipo no soportado

Una API pública puede rechazar deliberadamente un argumento porque su tipo en runtime no está soportado:

```python
def repeat_label(label: str, times: int) -> str:
    if not isinstance(label, str):
        raise TypeError("label must be a string")
    if not isinstance(times, int):
        raise TypeError("times must be an integer")
    return label * times
```

Sin embargo, no añadas comprobaciones de tipo en runtime en todas partes solo porque existen type hints.

Los type hints comunican tipos esperados a lectores y herramientas, pero no los imponen automáticamente en runtime. Añade comprobaciones explícitas solo cuando la API realmente necesite validación en runtime.

## 8. Elige la excepción que mejor describa el contrato que falló

Algunas opciones útiles para principiantes:

| Situación | Excepción común |
|---|---|
| valor fuera de un rango aceptado | `ValueError` |
| tipo de argumento en runtime no soportado | `TypeError` |
| falta una clave requerida en una API que expone naturalmente esa consulta | `KeyError` |
| posición solicitada fuera del rango disponible de una secuencia | `IndexError` |
| el archivo solicitado no existe | `FileNotFoundError` |
| la operación no está implementada para el caso solicitado | `NotImplementedError` |

Esta tabla es una guía, no una regla que obligue a cada función a lanzar manualmente cada una de estas excepciones.

A menudo una operación built-in ya lanza naturalmente la excepción más apropiada. No dupliques comprobaciones solo para recrear la misma señal, a menos que tu función necesite un contrato o mensaje más claro.

## 9. No uses `Exception` cuando encaje una built-in más específica

Esto es válido:

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise Exception("invalid age")
    return age
```

Pero proporciona poca información al llamador sobre qué categoría de fallo ocurrió.

Prefiere:

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

Los tipos de excepción específicos permiten un manejo selectivo.

## 10. Los mensajes de excepción deben explicar la expectativa violada

Compara:

```python
raise ValueError("invalid")
```

con:

```python
raise ValueError("score must be between 0 and 100")
```

El segundo mensaje es más útil para una persona que lee un traceback o log.

Un mensaje práctico suele indicar:

- qué era inválido;
- cuál era la condición aceptada;
- suficiente contexto para diagnosticar el problema sin exponer secretos ni datos sensibles.

Evita incluir contraseñas, tokens de acceso, rutas privadas o payloads confidenciales en mensajes de excepción.

## 11. No hagas que la lógica dependa del texto exacto del mensaje

Los mensajes son principalmente texto de diagnóstico para personas.

Evita lógica como:

```python
try:
    validate_score(score)
except ValueError as error:
    if str(error) == "score must be between 0 and 100":
        print("Range problem")
```

Si los llamadores necesitan distinguir categorías de fallo de forma programática, usa **tipos** de excepción distintos, valores de retorno estructurados u otro contrato explícito de API.

## 12. `raise` puede recibir una instancia o una clase de excepción

Python permite:

```python
raise ValueError("invalid score")
```

y también:

```python
raise ValueError
```

Cuando recibe una clase de excepción, Python crea la instancia cuando es necesario, sin argumentos.

Para enseñanza y código de aplicación, lanzar una instancia con un mensaje útil suele ser más claro:

```python
raise ValueError("score must be between 0 and 100")
```

## 13. Las excepciones pueden propagarse por varias llamadas de función

Un helper puede lanzar una excepción sin manejarla:

```python
def validate_quantity(quantity: int) -> int:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return quantity


def build_order(quantity: int) -> str:
    valid_quantity = validate_quantity(quantity)
    return f"Order quantity: {valid_quantity}"
```

Si `validate_quantity()` lanza `ValueError`, `build_order()` también interrumpe su ruta normal a menos que maneje esa excepción.

La excepción continúa propagándose hacia afuera por la pila de llamadas.

## 14. Maneja la excepción en una capa que pueda responder de forma significativa

Un helper de validación de bajo nivel puede saber **qué está mal**, pero no **qué debe hacer el programa después**.

Por ejemplo:

```python
def validate_quantity(quantity: int) -> int:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return quantity


try:
    quantity = validate_quantity(0)
except ValueError as error:
    print(f"Could not continue: {error}")
```

El validador informa la violación del contrato. El llamador elige la respuesta orientada al usuario.

Una pregunta de diseño útil es:

```text
¿Esta capa sabe cómo recuperarse o explicar el fallo?
    sí → el manejo puede pertenecer aquí
    no → deja que la excepción se propague
```

## 15. No lances y captures inmediatamente sin una razón

Esto suele añadir ceremonia sin mejorar el diseño:

```python
def validate_score(score: int) -> int:
    try:
        if not 0 <= score <= 100:
            raise ValueError("invalid score")
    except ValueError:
        return 0
    return score
```

La función convierte una violación clara del contrato en un valor fallback no relacionado.

Si `0` es realmente el fallback documentado, retornarlo directamente puede ser más claro. Si la entrada inválida debe informarse, deja que `ValueError` se propague.

Lanza y maneja en la misma capa solo cuando esa capa realmente tenga una acción de recuperación significativa.

## 16. Un `raise` sin expresión vuelve a lanzar la excepción activa

Dentro de un bloque `except`, un `raise` sin expresión envía nuevamente hacia afuera la excepción que se está manejando:

```python
def parse_quantity(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        print("Could not parse quantity")
        raise
```

El handler realiza algún trabajo local y luego preserva el fallo en lugar de fingir que la operación tuvo éxito.

Conceptualmente:

```text
ocurre ValueError
    ↓
except ValueError se ejecuta
    ↓
logging o limpieza local
    ↓
raise sin expresión
    ↓
la misma excepción activa continúa hacia afuera
```

## 17. Prefiere `raise` sin expresión cuando el objetivo sea simplemente volver a lanzar

Dentro de un handler activo, esta es la forma directa:

```python
except ValueError:
    raise
```

Escribir `raise error` vuelve a lanzar ese objeto de excepción como una operación explícita de `raise` y puede alterar la presentación del traceback al añadir la ubicación actual del nuevo `raise`.

Cuando tu intención es "seguir propagando la excepción que estoy manejando ahora", un `raise` sin expresión comunica esa intención con más precisión.

## 18. Traducir excepciones puede mejorar un límite de abstracción

A veces una excepción de bajo nivel expone un detalle de implementación que los llamadores no deberían necesitar conocer.

Supón que un texto de configuración debe contener un entero:

```python
class ConfigurationError(Exception):
    pass


def parse_attempt_limit(text: str) -> int:
    try:
        return int(text)
    except ValueError as error:
        raise ConfigurationError("attempt limit must be an integer") from error
```

Ahora el llamador puede manejar `ConfigurationError` como parte de la API de configuración sin depender directamente del detalle interno de conversión.

## 19. `raise ... from ...` crea un encadenamiento explícito de excepciones

En:

```python
raise ConfigurationError("attempt limit must be an integer") from error
```

`ConfigurationError` es la nueva excepción y `error` se registra como su causa explícita.

Si la nueva excepción permanece sin manejar, la presentación del traceback de Python muestra la relación entre el fallo original y el fallo traducido.

Esto preserva el historial de diagnóstico y permite que la API de nivel superior exponga un tipo de excepción más significativo.

## 20. El encadenamiento explícito es especialmente útil al cambiar de nivel de abstracción

Una forma común es:

```text
una operación de bajo nivel falla
        ↓
la excepción de bajo nivel se captura
        ↓
se lanza una excepción de nivel superior a partir de la original
        ↓
el llamador ve el contrato de nivel superior
        ↓
el diagnóstico conserva la causa original
```

Ejemplos incluyen traducir errores de parsing en errores de configuración o errores de una biblioteca de almacenamiento en un error de persistencia específico de la aplicación.

No traduzcas toda excepción automáticamente. Hazlo cuando vuelva más claro el límite público.

## 21. `from None` suprime el contexto mostrado y debe ser deliberado

Python también permite:

```python
raise ValueError("invalid identifier") from None
```

Esto suprime la presentación automática del contexto de la excepción anterior en el traceback resultante.

Puede ser útil cuando el fallo de bajo nivel es irrelevante o confuso para usuarios, pero también elimina contexto de diagnóstico del traceback mostrado. Úsalo con moderación y de forma deliberada.

## 22. Las excepciones personalizadas son clases de excepción que tú defines

Una excepción personalizada permite que una aplicación dé a un fallo un tipo específico del dominio.

La forma útil más pequeña es:

```python
class EmptyStudyPlanError(Exception):
    pass
```

Esto crea una nueva clase de excepción llamada `EmptyStudyPlanError`, que hereda de `Exception` el comportamiento normal de las excepciones de aplicación.

La instrucción `pass` significa que la clase todavía no añade comportamiento adicional.

## 23. Esta es una introducción limitada a la herencia de clases

La sintaxis:

```python
class EmptyStudyPlanError(Exception):
    pass
```

significa, conceptualmente:

```text
Exception
    ↓
EmptyStudyPlanError
```

`EmptyStudyPlanError` es una clase más específica de `Exception`.

Esa relación importa porque:

```python
except EmptyStudyPlanError:
```

puede capturar solo esa categoría personalizada, mientras que:

```python
except Exception:
```

también puede capturarla porque la clase personalizada hereda de `Exception`.

No necesitas un modelo completo de programación orientada a objetos para usar este patrón simple con seguridad.

## 24. Las excepciones personalizadas de aplicación suelen heredar de `Exception`

Para fallos normales de aplicación, define excepciones personalizadas debajo de `Exception`, directamente o mediante otra excepción de aplicación apropiada.

Prefiere:

```python
class StudyPlanError(Exception):
    pass
```

a heredar directamente de `BaseException`.

`BaseException` también está por encima de excepciones de control como `KeyboardInterrupt` y `SystemExit`, que los handlers normales de una aplicación normalmente no deberían agrupar accidentalmente con fallos del dominio.

## 25. Los nombres de excepciones personalizadas suelen terminar en `Error`

Ejemplos:

```python
class EmptyStudyPlanError(Exception):
    pass
```

```python
class ConfigurationError(Exception):
    pass
```

El sufijo `Error` es una fuerte convención de Python para nombres de clases de excepción y hace visible inmediatamente su propósito.

## 26. Lanza una excepción personalizada igual que una built-in

```python
class EmptyStudyPlanError(Exception):
    pass


def summarize_plan(topics: list[str]) -> str:
    if not topics:
        raise EmptyStudyPlanError("study plan must contain at least one topic")
    return ", ".join(topics)
```

El tipo personalizado transporta significado del dominio. El mensaje transporta el detalle legible por personas.

## 27. Captura el tipo personalizado cuando sepas cómo responder

```python
try:
    summary = summarize_plan([])
except EmptyStudyPlanError as error:
    print(f"Plan error: {error}")
```

Este handler no captura accidentalmente excepciones no relacionadas, como un `TypeError` de programación en otra parte de la misma operación.

Los tipos personalizados específicos pueden hacer que una API sea más fácil de manejar correctamente.

## 28. No crees una excepción personalizada para cada pequeña regla de validación

Esto puede volverse ruidoso:

```text
NegativeScoreError
ScoreTooLargeError
EmptyScoreTextError
UnsupportedScoreFormatError
...
```

Si todas esas situaciones significan lo mismo para los llamadores, una built-in `ValueError` puede ser suficiente.

Crea una excepción personalizada cuando la **categoría en sí** sea significativa para llamadores, logging, tests o un límite de abstracción.

## 29. Una excepción personalizada puede heredar de una categoría built-in significativa

Si un error específico del dominio también es claramente una clase de error built-in, la herencia puede conservar ambos significados:

```python
class ScoreRangeError(ValueError):
    pass
```

Ahora los llamadores pueden elegir:

```python
except ScoreRangeError:
```

para el caso específico del dominio, o:

```python
except ValueError:
```

para una política más amplia de errores de valor.

Úsalo solo cuando la clase built-in padre describa correctamente el fallo personalizado.

## 30. Las excepciones personalizadas pueden transportar atributos estructurados

Una clase personalizada simple suele necesitar solo `pass`, pero una excepción también puede almacenar detalles estructurados:

```python
class ScoreRangeError(ValueError):
    def __init__(self, score: int) -> None:
        self.score = score
        super().__init__(f"score must be between 0 and 100: {score}")
```

Un llamador puede entonces inspeccionar `error.score` sin interpretar el texto del mensaje.

Este es un patrón de clase algo más avanzado. Prefiere la forma simple con `pass` hasta que los datos estructurados de la excepción aporten un beneficio real.

## 31. Ejemplo práctico: validar scores explícitamente

```python
def validate_score(score: int) -> int:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score


scores = [85, 120]

for score in scores:
    try:
        valid_score = validate_score(score)
    except ValueError as error:
        print(f"Rejected {score}: {error}")
    else:
        print(f"Accepted {valid_score}")
```

Salida:

```text
Accepted 85
Rejected 120: score must be between 0 and 100
```

Cada elemento se valida de forma independiente. El validador lanza la excepción; el bucle decide cómo continuar después de un elemento inválido.

Versión ejecutable: [`examples/validate_score.py`](examples/validate_score.py).

## 32. Ejemplo práctico: una excepción personalizada de dominio

```python
class EmptyStudyPlanError(Exception):
    pass


def summarize_plan(topics: list[str]) -> str:
    if not topics:
        raise EmptyStudyPlanError("study plan must contain at least one topic")
    return ", ".join(topics)


plans = [["Functions", "Exceptions"], []]

for topics in plans:
    try:
        print(summarize_plan(topics))
    except EmptyStudyPlanError as error:
        print(f"Plan error: {error}")
```

Salida:

```text
Functions, Exceptions
Plan error: study plan must contain at least one topic
```

Versión ejecutable: [`examples/custom_exception.py`](examples/custom_exception.py).

## 33. Ejemplo práctico: traducir y encadenar una excepción

```python
class ConfigurationError(Exception):
    pass


def parse_attempt_limit(text: str) -> int:
    try:
        limit = int(text)
    except ValueError as error:
        raise ConfigurationError("attempt limit must be an integer") from error

    if limit <= 0:
        raise ConfigurationError("attempt limit must be greater than zero")

    return limit


try:
    parse_attempt_limit("three")
except ConfigurationError as error:
    cause_name = type(error.__cause__).__name__ if error.__cause__ else "None"
    print(f"{type(error).__name__}: {error}")
    print(f"Cause: {cause_name}")
```

Salida:

```text
ConfigurationError: attempt limit must be an integer
Cause: ValueError
```

La causa explícita sigue disponible mediante `__cause__`, aunque el código de nivel superior maneje `ConfigurationError`.

Versión ejecutable: [`examples/exception_chaining.py`](examples/exception_chaining.py).

## 34. `raise` y `assert` no son intercambiables

Una assertion expresa una condición que el programador espera que sea verdadera durante depuración o comprobación de una invariante interna:

```python
assert total >= 0
```

Las assertions pueden deshabilitarse cuando Python se ejecuta con optimización activada.

Por eso, no uses `assert` para validación que debe ocurrir siempre, como comprobar entrada del usuario, contenido de archivos, datos de API o el contrato de una función pública.

Usa una excepción explícita:

```python
if total < 0:
    raise ValueError("total cannot be negative")
```

## 35. Lanza antes de modificar estado compartido cuando sea posible

Supón que datos inválidos no deben entrar en una lista:

```python
def add_score(scores: list[int], score: int) -> None:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    scores.append(score)
```

La validación ocurre antes de la mutación.

Ese orden reduce la posibilidad de dejar estado parcialmente actualizado después de un fallo.

Un flujo útil es:

```text
validar precondiciones
        ↓
lanzar excepción si son inválidas
        ↓
modificar estado solo después de que la validación tenga éxito
```

## 36. Error común: lanzar la categoría equivocada

Esto es engañoso:

```python
def validate_name(name: str) -> str:
    if not name:
        raise TypeError("name is empty")
    return name
```

Un string vacío sigue teniendo el tipo esperado `str`; el problema está en su valor.

`ValueError` comunica el fallo con más precisión:

```python
def validate_name(name: str) -> str:
    if not name:
        raise ValueError("name cannot be empty")
    return name
```

## 37. Error común: capturar tu base personalizada de forma demasiado amplia

Imagina:

```python
class ApplicationError(Exception):
    pass
```

Puede ser tentador envolver grandes secciones con:

```python
except ApplicationError:
    print("Something failed")
```

Pero una clase base amplia de aplicación todavía puede juntar varias categorías de fallo distintas en una respuesta vaga.

Captura el tipo más específico que la capa actual realmente pueda manejar de forma significativa.

## 38. Error común: convertir toda excepción en una personalizada

Esto no es automáticamente mejor:

```python
try:
    value = int(text)
except ValueError as error:
    raise ApplicationError("operation failed") from error
```

Si los llamadores ya entienden `ValueError` y la conversión forma parte del contrato público, la traducción puede no añadir ninguna abstracción útil.

Las excepciones personalizadas deben aclarar límites, no solo cambiar el nombre de fallos built-in.

## 39. Error común: ocultar historial de diagnóstico sin necesidad

Usar:

```python
raise ConfigurationError("invalid configuration") from None
```

puede producir un traceback más limpio para el usuario, pero suprime la presentación del contexto de la excepción anterior.

Si la causa de bajo nivel ayudaría a desarrolladores a diagnosticar el fallo, el encadenamiento explícito con `from error` suele ser más informativo.

## 40. Ejercicio

Construye un pequeño validador de sesiones de estudio que informe deliberadamente entradas inválidas.

Requisitos:

1. Crea una excepción personalizada llamada `StudySessionError` que herede de `Exception`.
2. Crea `validate_session(minutes: int, topic: str) -> tuple[int, str]`.
3. Lanza `ValueError` cuando `minutes` sea menor o igual que cero.
4. Lanza `StudySessionError` cuando `topic` esté vacío después de `strip()`.
5. Retorna la tupla validada `(minutes, topic)` cuando ambos valores sean válidos.
6. Crea al menos tres casos de prueba que incluyan una sesión válida y las dos categorías de fallo.
7. Maneja `ValueError` y `StudySessionError` por separado en el llamador.
8. Imprime mensajes deterministas para cada caso.
9. Añade un helper que reciba una versión textual de los minutos, la convierta con `int()` y lance `StudySessionError("minutes must be an integer") from error` cuando la conversión falle.
10. Antes de ejecutar el código, dibuja las rutas normal y excepcional para cada entrada.

Desafío adicional: decide si el helper de conversión debería exponer `ValueError` directamente o traducirlo a `StudySessionError`, y explica qué límite de API crea tu elección.

## 41. Lista de revisión

Ahora deberías poder responder:

- ¿Qué hace `raise` con la ruta normal de ejecución actual?
- ¿Cuándo `ValueError` encaja mejor que `TypeError`?
- ¿Por qué los mensajes de excepción no deberían convertirse en una API basada en comparar strings?
- ¿Qué ocurre cuando una excepción lanzada no tiene handler local?
- ¿Cuándo debería un helper de bajo nivel dejar que una excepción se propague?
- ¿Qué hace un `raise` sin expresión dentro de un bloque `except`?
- ¿Por qué un `raise` sin expresión suele ser preferible al simplemente volver a lanzar la excepción activa?
- ¿Qué relación registra `raise NewError(...) from error`?
- ¿Por qué el encadenamiento de excepciones puede mejorar un límite de abstracción?
- ¿Por qué `from None` debe usarse deliberadamente?
- ¿Qué significa `class CustomError(Exception): pass` a nivel inicial?
- ¿Por qué las excepciones personalizadas de aplicación suelen heredar de `Exception` en vez de directamente de `BaseException`?
- ¿Cuándo una excepción personalizada es más útil que una built-in?
- ¿Por qué `assert` no debe validar entrada externa obligatoria?
- ¿Por qué validar antes de modificar estado compartido suele ser más seguro?

## 42. Consulta rápida

| Necesidad | Enfoque útil |
|---|---|
| rechazar un valor inválido | `raise ValueError("...")` |
| rechazar un tipo en runtime no soportado | `raise TypeError("...")` cuando la comprobación en runtime realmente forme parte de la API |
| preservar la excepción que se está manejando | `raise` sin expresión |
| traducir una excepción conservando su causa | `raise NewError("...") from error` |
| suprimir deliberadamente el contexto anterior mostrado | `raise NewError("...") from None` |
| introducir una categoría de fallo específica del dominio | `class DomainError(Exception): pass` |
| conservar significado del dominio y de error de valor built-in | heredar de una built-in apropiada, como `ValueError` |
| distinguir fallos programáticamente | usa tipos de excepción o datos estructurados, no parsing del texto del mensaje |
| validar datos externos/del usuario de forma confiable | comprobaciones explícitas + `raise`, no `assert` |
| reducir cambios parciales de estado | valida antes de la mutación cuando sea práctico |

## 43. Límite de alcance

Este capítulo deliberadamente **no** enseña todavía en profundidad:

- programación orientada a objetos completa y diseño general de clases;
- herencia múltiple para clases de excepción;
- `ExceptionGroup` y `except*`;
- manipulación avanzada de tracebacks;
- políticas de retry;
- frameworks de logging;
- context managers y limpieza de archivos;
- pruebas de contratos de excepción con `pytest`.

Estos temas resultan más fáciles cuando el modelo básico de lanzar/propagar/manejar ya está firme.

## 44. Hacia dónde continúa la Fase 7

La progresión ahora es:

```text
manejar excepciones que ya ocurren
        ↓
lanzar excepciones deliberadamente
        ↓
elegir tipos built-in o personalizados
        ↓
propagar, volver a lanzar o encadenar deliberadamente
        ↓
siguiente: abrir y gestionar archivos de forma segura
        ↓
datos de texto estructurados
        ↓
módulos y paquetes
```

Próximo capítulo planificado: **`open()` y `with`**.

## Referencias oficiales

- [Python 3.14 Language Reference: The `raise` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-raise-statement)
- [Python 3.14 Tutorial: Raising Exceptions](https://docs.python.org/3.14/tutorial/errors.html#raising-exceptions)
- [Python 3.14 Tutorial: User-defined Exceptions](https://docs.python.org/3.14/tutorial/errors.html#user-defined-exceptions)
- [Python 3.14 Built-in Exceptions](https://docs.python.org/3.14/library/exceptions.html)
- [Python 3.14 Language Reference: The `assert` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-assert-statement)
