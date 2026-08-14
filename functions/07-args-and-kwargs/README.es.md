<div align="center">

# `*args` y `**kwargs`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Anterior: Valores Predeterminados](../06-default-values/README.es.md)

Los capítulos anteriores dieron a las funciones parámetros obligatorios, valores de retorno, alcance, type hints y valores predeterminados seguros. Este capítulo añade una nueva opción de diseño: una función puede recoger una **cantidad variable de argumentos** cuando el número exacto es intencionalmente flexible.

```text
extra positional arguments → *args   → tuple
extra keyword arguments    → **kwargs → dictionary
```

**Tiempo estimado de estudio:** 75–100 minutos.

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- explicar qué recoge `*args`;
- explicar qué recoge `**kwargs`;
- identificar la tupla almacenada por `*args`;
- identificar el diccionario almacenado por `**kwargs`;
- usar cero, uno o muchos argumentos recogidos;
- combinar parámetros obligatorios con `*args` o `**kwargs`;
- usar `*args` y `**kwargs` juntos en una firma simple;
- añadir type hints a los valores recogidos;
- distinguir la recolección en la definición de una función del desempaquetado en el punto de llamada;
- reconocer cuándo una lista explícita de parámetros es más clara que una recolección flexible.

## 1. Por qué existen los argumentos de longitud variable

A veces una función acepta de forma natural una cantidad de valores que no está fijada de antemano.

Una función que suma puntuaciones puede recibir dos valores en una llamada y cinco en otra:

```python
def total_scores(*scores):
    return sum(scores)


print(total_scores(10, 20))
print(total_scores(10, 20, 30, 40, 50))
```

Salida:

```text
30
150
```

Sin un parámetro de longitud variable, tendrías que decidir una cantidad fija de parámetros de puntuación o exigir que el llamador construyera primero una colección.

Usa recolección flexible cuando la flexibilidad pertenezca al diseño de la función, no solamente para evitar decidir qué debería aceptar.

## 2. `*args` recoge argumentos posicionales extra

La sintaxis usa un `*` antes del nombre del parámetro:

```python
def show_values(*values):
    print(values)


show_values(4, 7, 9)
```

Salida:

```text
(4, 7, 9)
```

Dentro de la función, `values` es una tupla que contiene los argumentos posicionales recogidos por ese parámetro.

```text
call:       show_values(4, 7, 9)
                         ↓  ↓  ↓
*values collects:      (4, 7, 9)
```

## 3. `args` es una convención, no un nombre especial

A menudo verás esto:

```python
def show_values(*args):
    print(args)
```

Pero la parte especial es el `*`, no la palabra `args`.

Esto es igualmente válido y muchas veces más descriptivo:

```python
def show_scores(*scores):
    print(scores)
```

Prefiere un nombre significativo cuando los valores recogidos tengan un papel claro.

## 4. `*args` puede recoger cero argumentos

Un parámetro posicional de longitud variable no exige al menos un valor:

```python
def show_items(*items):
    print(items)


show_items()
show_items("pen")
show_items("pen", "book")
```

Salida:

```text
()
('pen',)
('pen', 'book')
```

La llamada vacía produce una tupla vacía.

## 5. Itera sobre la tupla recogida

Como el valor recogido es una tupla, la iteración normal con `for` funciona de forma natural:

```python
def print_names(*names):
    for name in names:
        print(name)


print_names("Ava", "Leo", "Mia")
```

Salida:

```text
Ava
Leo
Mia
```

Todo lo aprendido anteriormente sobre iteración de tuplas sigue siendo válido.

## 6. Los parámetros obligatorios pueden aparecer antes de `*args`

Una función puede exigir un valor antes de recoger argumentos posicionales adicionales. El parámetro ordinario antes de `*args` sigue siendo posicional-o-por-palabra-clave, a menos que la firma use una sintaxis separada de solo posición:

```python
def announce(prefix, *messages):
    for message in messages:
        print(prefix, message)


announce("INFO:", "Ready", "Running")
```

Salida:

```text
INFO: Ready
INFO: Running
```

En la llamada anterior, `"INFO:"` se asocia a `prefix` por posición. Los argumentos posicionales restantes se asocian a `messages`:

```text
"INFO:"             → prefix
"Ready", "Running" → messages → ("Ready", "Running")
```

`prefix` es obligatorio porque no tiene valor predeterminado, pero **obligatorio** no significa **solo posicional**. Si no se necesitan mensajes extra, el mismo parámetro puede asociarse por palabra clave:

```python
announce(prefix="INFO:")
```

Aquí `messages` se convierte en una tupla vacía. Con esta firma, los mensajes extra son posicionales, así que, cuando quieras proporcionarlos, la forma más simple es la llamada posicional mostrada arriba.

## 7. `**kwargs` recoge argumentos extra por palabra clave

La sintaxis usa dos caracteres `*` antes del nombre del parámetro:

```python
def show_details(**details):
    print(details)


show_details(color="blue", size="medium")
```

Salida:

```text
{'color': 'blue', 'size': 'medium'}
```

Dentro de la función, `details` es un diccionario.

```text
color="blue"   → key "color", value "blue"
size="medium"  → key "size", value "medium"
```

## 8. `kwargs` también es solo una convención

Esto es común:

```python
def show_details(**kwargs):
    print(kwargs)
```

Pero esto es igualmente válido:

```python
def show_settings(**settings):
    print(settings)
```

De nuevo, `**` controla la recolección. Tú eliges el nombre del parámetro.

## 9. `**kwargs` puede recoger cero argumentos por palabra clave

```python
def show_options(**options):
    print(options)


show_options()
show_options(theme="dark")
```

Salida:

```text
{}
{'theme': 'dark'}
```

Ningún argumento por palabra clave recogido significa un diccionario vacío.

## 10. Itera sobre nombres y valores de palabras clave

Iterar directamente sobre un diccionario produce las claves. Usa `.items()` cuando necesites claves y valores:

```python
def print_settings(**settings):
    for name, value in settings.items():
        print(name, value)


print_settings(language="Python", level="beginner")
```

Salida:

```text
language Python
level beginner
```

Este es comportamiento normal de diccionarios, no una regla especial de `**kwargs`.

## 11. Los parámetros obligatorios pueden aparecer antes de `**kwargs`

Una función puede exigir un dato nombrado y recoger información adicional por palabra clave:

```python
def build_profile(name, **details):
    print("Name:", name)

    for key, value in details.items():
        print(key, value)


build_profile("Ava", role="student", active=True)
```

Salida:

```text
Name: Ava
role student
active True
```

El argumento obligatorio se asocia a `name`. Los argumentos por palabra clave restantes se recogen en `details`.

## 12. Usa `*args` y `**kwargs` juntos

Una firma simple puede recoger ambas formas:

```python
def describe_group(name, *members, **details):
    print("Group:", name)
    print("Members:", members)
    print("Details:", details)


describe_group("Study", "Ava", "Leo", topic="Python", active=True)
```

Salida:

```text
Group: Study
Members: ('Ava', 'Leo')
Details: {'topic': 'Python', 'active': True}
```

El modelo mental es:

```text
required positional-or-keyword input → ordinary parameter
extra positional input               → *members → tuple
extra keyword input                  → **details → dictionary
```

Un parámetro ordinario como `name` es obligatorio aquí, pero puede recibir su valor tanto por posición como por palabra clave. Las dos llamadas siguientes son válidas, y ninguna añade un valor a `*members`:

```python
describe_group("Study", topic="Python")
describe_group(name="Study", topic="Python")
```

En la segunda llamada, `name="Study"` se asocia directamente al parámetro ordinario `name`. Solo `topic="Python"` queda disponible para ser recogido por `**details`.

## 13. El orden importa en la firma de la función

Para el patrón principiante de este capítulo, piensa en:

```python
def function(required, *args, **kwargs):
    pass
```

El parámetro obligatorio se asocia primero, `*args` recoge los argumentos posicionales restantes y `**kwargs` recoge los argumentos por palabra clave restantes.

Python admite otras características de ordenación de parámetros, incluidos parámetros solo por palabra clave y solo posicionales. Merecen tratamiento propio y quedan fuera del foco principal de este capítulo.

## 14. Los type hints describen cada valor recogido

Cuando anotas `*args`, la anotación describe cada valor posicional recogido:

```python
def total_scores(*scores: int) -> int:
    return sum(scores)
```

Conceptualmente, dentro de la función:

```text
scores → tuple of int values
```

Para `**kwargs`, la anotación describe cada valor recogido en el diccionario:

```python
def show_labels(**labels: str) -> None:
    for name, value in labels.items():
        print(name, value)
```

Conceptualmente:

```text
labels → dictionary with string keys and str values
```

Como se aprendió en el Capítulo 05, los type hints describen interfaces previstas, pero no imponen tipos automáticamente en runtime.

## 15. `*args` es una tupla, no una lista

Un error común es esperar métodos de lista:

```python
def collect(*items):
    print(type(items))


collect("a", "b")
```

Salida:

```text
<class 'tuple'>
```

Si la función realmente necesita una lista mutable, créala de forma deliberada:

```python
def collect(*items):
    result = list(items)
    result.append("done")
    return result
```

No trates mentalmente la tupla como una lista solo porque ambas son colecciones ordenadas.

## 16. `**kwargs` es un diccionario normal dentro de la función

Puedes usar operaciones conocidas de diccionarios:

```python
def get_mode(**options):
    return options.get("mode", "standard")


print(get_mode())
print(get_mode(mode="compact"))
```

Salida:

```text
standard
compact
```

El diccionario existe para la llamada actual de la función, igual que otros objetos locales creados durante esa llamada.

## 17. No uses flexibilidad cuando los parámetros explícitos sean más claros

Esta firma oculta la interfaz esperada:

```python
def create_user(**data):
    pass
```

Si la función realmente exige exactamente un nombre y un email, esto es más claro:

```python
def create_user(name, email):
    pass
```

Los parámetros explícitos mejoran la legibilidad, la ayuda del editor, la documentación y los mensajes de error cuando las entradas aceptadas son conocidas.

Usa `*args` y `**kwargs` porque la cantidad o los nombres de argumentos son intencionalmente variables, no solo porque acortan la firma.

## 18. Recolección en definiciones no es desempaquetado en llamadas

Este capítulo usa estrellas en definiciones de funciones:

```python
def show_values(*values):
    print(values)


def show_details(**details):
    print(details)
```

Aquí las estrellas **recogen** argumentos.

Python también puede usar `*` y `**` en llamadas para desempaquetar un iterable o mapping existente. Esa es la dirección opuesta del flujo de datos y se aplaza intencionalmente para que las dos ideas no se mezclen.

```text
definition side → collect
call side       → unpack (later topic)
```

## 19. Error común: esperar argumentos por palabra clave en `*args`

```python
def inspect(*values):
    print(values)


inspect(10, 20, 30)
```

Salida:

```text
(10, 20, 30)
```

`*values` recoge argumentos posicionales. Si necesitas argumentos flexibles por palabra clave, usa un parámetro con `**`.

## 20. Error común: iterar sobre `**kwargs` como si produjera pares

```python
def show(**details):
    for item in details:
        print(item)


show(color="blue", size="medium")
```

Salida:

```text
color
size
```

La iteración directa de diccionarios produce claves. Usa `details.items()` para pares clave-valor.

## 21. Error común: aceptar todo sin una razón

Una firma como:

```python
def process(*args, **kwargs):
    pass
```

es extremadamente flexible, pero poco informativa.

Antes de usarla, pregunta:

1. ¿Los valores posicionales son realmente variables en cantidad?
2. ¿Los nombres de argumentos por palabra clave son realmente abiertos?
3. ¿Una firma más explícita comunicaría mejor el contrato?
4. ¿La función validará o usará claramente los datos recogidos?

La flexibilidad es útil cuando modela el problema. La flexibilidad innecesaria hace que las APIs sean más difíciles de entender.

## 22. Ejemplos ejecutables

### Calcular un promedio con `*args`

Archivo: [`examples/calculate_average.py`](examples/calculate_average.py)

```python
def calculate_average(first_score: float, *scores: float) -> float:
    return (first_score + sum(scores)) / (1 + len(scores))


print(calculate_average(8.0, 9.0, 10.0))
```

Salida esperada:

```text
9.0
```

Un promedio requiere al menos un valor, por lo que `first_score` es obligatorio mientras `*scores` recoge cualquier puntuación adicional.

### Mostrar configuraciones con `**kwargs`

Archivo: [`examples/display_settings.py`](examples/display_settings.py)

```python
def display_settings(**settings: str) -> None:
    for name, value in settings.items():
        print(f"{name}: {value}")


display_settings(theme="dark", language="English")
```

Salida esperada:

```text
theme: dark
language: English
```

### Combinar entrada obligatoria, posicional y por palabra clave

Archivo: [`examples/describe_session.py`](examples/describe_session.py)

```python
def describe_session(title: str, *topics: str, **details: str) -> None:
    print(f"Title: {title}")
    print(f"Topics: {', '.join(topics)}")

    for name, value in details.items():
        print(f"{name}: {value}")


describe_session(
    "Python Study",
    "functions",
    "arguments",
    level="beginner",
    format="guided",
)
```

Salida esperada:

```text
Title: Python Study
Topics: functions, arguments
level: beginner
format: guided
```

## 23. Ejercicio: resumen flexible de pedido

Crea `summarize_order(order_id, *items, **details)`.

Requisitos:

1. imprime el ID del pedido;
2. imprime cada elemento en su propia línea;
3. imprime cada detalle como `name: value`;
4. llama la función con el ID `A-104`;
5. pasa `"notebook"` y `"pen"` como elementos posicionales;
6. pasa `priority="normal"` y `channel="online"` como detalles por palabra clave.

Salida esperada:

```text
Order: A-104
notebook
pen
priority: normal
channel: online
```

Mantén el ejercicio centrado en la recolección. No desempaquetes una lista o un diccionario existente en el punto de llamada.

## 24. Checklist de repaso

Antes de continuar, confirma que puedes:

- [ ] explicar que un `*` recoge argumentos posicionales extra;
- [ ] explicar que dos caracteres `*` recogen argumentos extra por palabra clave;
- [ ] identificar la tupla creada por un parámetro de estilo `*args`;
- [ ] identificar el diccionario creado por un parámetro de estilo `**kwargs`;
- [ ] manejar cero argumentos recogidos;
- [ ] iterar por valores posicionales recogidos;
- [ ] iterar por pares clave-valor con `.items()`;
- [ ] combinar un parámetro obligatorio con `*args` o `**kwargs`;
- [ ] usar ambas formas en una firma simple;
- [ ] añadir type hints básicos a los valores recogidos;
- [ ] explicar por qué `args` y `kwargs` son convenciones y no nombres mágicos;
- [ ] distinguir recolección en la definición de desempaquetado en la llamada;
- [ ] elegir parámetros explícitos cuando la interfaz sea fija.

## 25. Referencia rápida

| Necesidad | Forma | Dentro de la función |
|---|---|---|
| recoger argumentos posicionales extra | `def f(*values):` | `values` es una tupla |
| recoger argumentos extra por palabra clave | `def f(**options):` | `options` es un diccionario |
| exigir un valor y recoger más posicionales | `def f(first, *rest):` | `first` es normal; `rest` es una tupla |
| exigir un valor y recoger detalles por palabra clave | `def f(name, **details):` | `name` es normal; `details` es un diccionario |
| recoger ambas formas | `def f(name, *items, **details):` | tupla más diccionario |
| anotar valores posicionales | `def f(*values: int):` | cada valor recogido está previsto como `int` |
| anotar valores por palabra clave | `def f(**values: str):` | cada valor recogido está previsto como `str` |

## 26. Límite de alcance

Este capítulo aplaza intencionalmente:

- desempaquetar iterables con `*` en el punto de llamada;
- desempaquetar mappings con `**` en el punto de llamada;
- sintaxis solo posicional con `/`;
- diseño detallado de parámetros solo por palabra clave;
- reenviar argumentos arbitrarios mediante funciones wrapper;
- decoradores;
- tipado avanzado para firmas flexibles;
- introspección de firmas de funciones.

El objetivo aquí es construir un modelo mental estable de **recolección** antes de añadir la operación inversa de desempaquetado.

## 27. Qué viene después

Ahora puedes diseñar funciones con entradas fijas, valores predeterminados opcionales y cantidades intencionalmente variables de argumentos.

La siguiente pregunta es más amplia:

> ¿Cómo deberían varias funciones dividir el trabajo y llamarse entre sí sin convertirse en un enredo?

Eso lleva al **Capítulo 08: Funciones Trabajando Juntas**.

Vuelve a la [ruta de Funciones](../README.es.md) o a la [ruta completa](../../docs/learning-path.es.md).

## Referencias

Documentación primaria de Python:

- [Python 3.13 Tutorial: Arbitrary Argument Lists](https://docs.python.org/3.13/tutorial/controlflow.html#arbitrary-argument-lists)
- [Python 3.13 Tutorial: Keyword Arguments](https://docs.python.org/3.13/tutorial/controlflow.html#keyword-arguments)
- [Python 3.13 Language Reference: Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
