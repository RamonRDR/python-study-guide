<div align="center">

# Contenedores Especializados y Contratos de Colecciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Standard Library](../README.es.md) · [← Capítulo anterior: Logging](../05-logging/README.es.md)

La Fase 3 presentó los cuatro modelos de colecciones de propósito general: `list`, `tuple`, `dict` y `set`. Este capítulo no reemplaza esos tipos integrados. Estudia el módulo `collections` como un conjunto de contenedores especializados para situaciones donde las **operaciones necesarias** son más específicas que el modelo de una colección general.

La pregunta central es:

```text
¿Qué comportamiento promete la estructura de datos,
y ese comportamiento coincide con las operaciones que mi programa realiza con mayor frecuencia?
```

Un contenedor especializado es útil cuando su semántica deja la intención más clara, reduce administración manual o proporciona un mejor contrato de rendimiento para un patrón de acceso específico.

**Tiempo estimado de estudio:** 150–190 minutos.

**Requisito de Python:** Python 3.10 o posterior para el contenido principal y los ejemplos ejecutables. Las notas sensibles a versión identifican cambios posteriores cuando son relevantes.

**Base de documentación:** los comportamientos y notas de versión se verificaron contra la documentación oficial de Python 3.14 para `collections`, `collections.abc` y `typing`.

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- explicar por qué `collections` complementa, en lugar de reemplazar, los contenedores integrados;
- usar `Counter` como abstracción de conteo y multiconjunto;
- razonar sobre conteos cero, negativos y ausentes en un `Counter`;
- usar `defaultdict` sin crear claves accidentalmente durante lecturas;
- elegir `deque` para operaciones eficientes en ambos extremos y ventanas de historial limitadas;
- explicar la diferencia entre acceso en los extremos de un deque e indexación en el medio;
- usar `namedtuple()` cuando son útiles tanto la compatibilidad con tuplas como los campos con nombre;
- distinguir casos de uso de `namedtuple()`, `typing.NamedTuple` y `dataclass`;
- usar `ChainMap` para capas de mappings sin copiarlas anticipadamente;
- entender por qué `ChainMap` lee a través de toda la cadena pero escribe solo en el primer mapping;
- explicar cuándo `OrderedDict` todavía ofrece comportamiento que un `dict` normal no expresa tan directamente;
- reconocer `UserDict`, `UserList` y `UserString` como bases de extensión orientadas a wrappers;
- usar `collections.abc` para razonar sobre interfaces de colección y no solo implementaciones concretas;
- elegir contenedores especializados por semántica y patrones de acceso en lugar de novedad.

## 1. Qué añade este capítulo después de la Fase 3

La Fase 3 enseñó las formas fundamentales:

```python
items = ["alpha", "beta"]
point = (10, 20)
settings = {"mode": "safe"}
tags = {"python", "study"}
```

Esas estructuras siguen siendo las opciones predeterminadas para la mayoría de programas.

El módulo `collections` se vuelve útil cuando el programa necesita un contrato más específico:

```text
contar valores repetidos                         -> Counter
crear valores ausentes mediante factory          -> defaultdict
agregar/quitar eficientemente en ambos extremos  -> deque
superponer mappings sin copiar                    -> ChainMap
mantener semántica de tuple con campos nombrados  -> namedtuple
reordenar claves de mapping deliberadamente      -> OrderedDict
extender colecciones mediante wrappers            -> UserDict/UserList/UserString
razonar sobre interfaces                          -> collections.abc
```

El objetivo no es memorizar nombres inusuales. Es reconocer el patrón de operaciones que hace que una estructura encaje mejor que otra.

## 2. Empieza por el contrato de operaciones

La elección de una estructura de datos debería responder preguntas como:

- ¿La búsqueda se realiza por clave o por posición?
- ¿Un valor ausente significa error, cero o crear un valor por defecto?
- ¿Las escrituras se concentran en un extremo, en ambos o en posiciones aleatorias?
- ¿La estructura es una copia estática o una vista viva sobre otros mappings?
- ¿El orden afecta la igualdad o solo la iteración?
- ¿El objeto debe conservar compatibilidad con tuple?

Si un tipo integrado ya comunica claramente el contrato deseado, prefiere el tipo integrado.

La especialización es útil cuando elimina ambigüedad.

## 3. Importa solo lo que haga el diseño más claro

Un estilo común es importar los nombres específicos usados por el módulo:

```python
from collections import ChainMap, Counter, defaultdict, deque, namedtuple
```

Para interfaces abstractas, importa desde el submódulo dedicado:

```python
from collections.abc import Iterable, Mapping, Sequence
```

`collections.abc` está relacionado con `collections`, pero sirve a otro propósito: interfaces y protocolos, no almacenamiento especializado concreto.

# Parte I: `Counter`

## 4. `Counter` modela conteos

`Counter` es una subclase de `dict` diseñada alrededor del conteo de objetos hashables.

```python
from collections import Counter

counts = Counter(["ok", "ok", "retry", "ok", "failed"])
print(counts)
```

Una representación típica es:

```text
Counter({'ok': 3, 'retry': 1, 'failed': 1})
```

Las claves son los elementos contados y los valores son sus conteos.

## 5. Construye un `Counter` desde elementos, mappings o argumentos nombrados

```python
from collections import Counter

from_elements = Counter("banana")
from_mapping = Counter({"red": 3, "blue": 1})
from_keywords = Counter(red=3, blue=1)
```

La primera forma cuenta ocurrencias. Las formas con mapping y argumentos nombrados interpretan los valores proporcionados como conteos.

## 6. Una clave ausente tiene conteo cero

A diferencia de una búsqueda en un diccionario normal, una clave ausente de `Counter` devuelve `0`:

```python
from collections import Counter

counts = Counter({"ready": 4})
print(counts["missing"])
```

Salida:

```text
0
```

Esto facilita el conteo incremental porque el código no necesita inicializar cada clave posible primero.

## 7. Un conteo cero no es lo mismo que una entrada ausente

Asignar cero no elimina una clave:

```python
from collections import Counter

counts = Counter(a=2)
counts["a"] = 0

print("a" in counts)
del counts["a"]
print("a" in counts)
```

Salida:

```text
True
False
```

Esta diferencia importa al inspeccionar claves o serializar el contador.

## 8. `total()` suma todos los conteos

Python 3.10 añadió `Counter.total()`:

```python
from collections import Counter

counts = Counter(success=8, retry=2, failed=1)
print(counts.total())
```

Salida:

```text
11
```

El total considera los conteos numéricos tal como están almacenados, incluidos valores negativos si existen.

## 9. `most_common()` conserva el orden de primera aparición en empates

```python
from collections import Counter

counts = Counter(["b", "a", "b", "a", "c"])
print(counts.most_common())
```

Los elementos con el mismo conteo mantienen el orden en que aparecieron por primera vez.

No trates silenciosamente los empates como orden alfabético a menos que tu programa los ordene explícitamente después.

## 10. `Counter.update()` suma conteos

`Counter.update()` no se comporta como `dict.update()`.

```python
from collections import Counter

counts = Counter(a=2)
counts.update(a=3, b=1)
print(counts)
```

El resultado contiene `a=5`, no `a=3`.

Esta es una operación de conteo, no semántica de reemplazo.

## 11. `subtract()` conserva resultados con signo

```python
from collections import Counter

balance = Counter(apples=5, pears=1)
balance.subtract(apples=2, pears=3)
print(balance)
```

`Counter` permite conteos cero y negativos. Eso resulta útil para deltas, balances y cálculos intermedios.

## 12. La aritmética de multiconjuntos filtra resultados no positivos

Los operadores aritméticos tienen un contrato de salida distinto de `subtract()`:

```python
from collections import Counter

required = Counter(a=4, b=2)
actual = Counter(a=1, b=5)

print(required - actual)
print(required + actual)
print(required & actual)
print(required | actual)
```

En estas operaciones de multiconjunto, el resultado excluye conteos iguales o menores que cero.

Eso hace conveniente la resta para preguntas como "¿qué falta todavía?".

## 13. `+` y `-` unarios normalizan counters con signo

```python
from collections import Counter

counts = Counter(a=3, b=0, c=-2)
print(+counts)
print(-counts)
```

El `+` unario conserva conteos positivos. El `-` unario conserva las magnitudes positivas de los conteos negativos.

Esto puede ser más claro que filtrar manualmente un counter con signo.

## 14. Las comparaciones de Counter tratan conteos ausentes como cero

Desde Python 3.10, las comparaciones ricas soportan igualdad y relaciones de inclusión de multiconjuntos.

```python
from collections import Counter

left = Counter(a=1)
right = Counter(a=1, b=0)

print(left == right)
```

Salida:

```text
True
```

Un elemento ausente se trata como si tuviera conteo cero en estas comparaciones.

## 15. Los valores de Counter no se limitan a enteros positivos

La clase en sí no impone únicamente conteos enteros positivos. Muchas operaciones aceptan otros valores numéricos.

Sin embargo, cada método tiene su propio contrato. Por ejemplo, `elements()` requiere conteos que puedan interpretarse como repeticiones e ignora conteos inferiores a uno.

No asumas que todos los métodos de `Counter` soportan tipos numéricos arbitrarios de la misma manera.

## 16. Usa un `dict` normal cuando no estés contando

Si el valor asociado a una clave es un estado, objeto, timestamp, configuración o registro arbitrario en lugar de un conteo, un diccionario normal suele comunicar mejor la intención.

`Counter` debería responder una pregunta de conteo o multiconjunto.

# Parte II: `defaultdict`

## 17. `defaultdict` modela creación de valores ausentes

`defaultdict` es una subclase de `dict` con una `default_factory`.

```python
from collections import defaultdict

groups = defaultdict(list)
groups["blue"].append("item-1")
print(groups)
```

Cuando `groups["blue"]` no existe, se llama a `list()`, se inserta la nueva lista y se devuelve esa lista.

## 18. La factory es un callable, no un valor ya creado

Correcto:

```python
from collections import defaultdict

rows = defaultdict(list)
counts = defaultdict(int)
```

La factory se llama cuando es necesaria.

Pasar `list()` en vez de `list` pasaría una lista ya creada, no el callable requerido como factory.

## 19. `__missing__()` es activado por `__getitem__()`

El comportamiento de valores ausentes está ligado a la búsqueda con corchetes:

```python
from collections import defaultdict

values = defaultdict(list)
values["new"].append(1)
```

La ruta de `dict.__getitem__()` invoca el método `__missing__()` de la subclase, que llama a la factory cuando corresponde.

## 20. `get()` no llama a la default factory

Este es uno de los contratos más importantes de `defaultdict`:

```python
from collections import defaultdict

values = defaultdict(list)

print(values.get("missing"))
print("missing" in values)
```

Salida:

```text
None
False
```

`get()` se comporta como `dict.get()` normal y no crea la clave.

## 21. Las pruebas de pertenencia no crean claves

```python
from collections import defaultdict

values = defaultdict(int)
print("x" in values)
print(values)
```

Una prueba de pertenencia es observacional. No invoca la factory.

## 22. Las lecturas con corchetes pueden modificar el mapping

Esta línea parece una lectura:

```python
value = values["missing"]
```

Con un `defaultdict`, también puede insertar `"missing"`.

Esta es una diferencia semántica frente a un diccionario normal y una fuente frecuente de claves accidentales.

Si solo quieres inspeccionar sin crear, usa pruebas de pertenencia o `get()` según corresponda.

## 23. `defaultdict(list)` es una herramienta natural de agrupación

```python
from collections import defaultdict

by_category = defaultdict(list)

for category, value in [("a", 1), ("b", 2), ("a", 3)]:
    by_category[category].append(value)

print(dict(by_category))
```

Esto evita repetir una rama de inicialización cuando la clave aún no existe.

## 24. `defaultdict(int)` es útil para conteos simples

```python
from collections import defaultdict

counts = defaultdict(int)

for word in ["red", "blue", "red"]:
    counts[word] += 1
```

Para frecuencia pura, `Counter` suele expresar el objetivo de manera más directa. `defaultdict(int)` sigue siendo útil cuando contar es solo una parte de un flujo de mapping más amplio.

## 25. Las factories pueden codificar defaults más ricos

```python
from collections import defaultdict


def new_state() -> dict[str, int]:
    return {"attempts": 0, "successes": 0}


state = defaultdict(new_state)
state["worker-a"]["attempts"] += 1
```

Usa una factory con nombre cuando la política de inicialización merezca un nombre o sea más compleja que un constructor integrado.

## 26. Los operadores de merge no significan "ejecutar la factory"

`defaultdict` soporta los operadores de merge de mappings introducidos para diccionarios.

El merge combina el contenido de los mappings. La creación de claves ausentes sigue ocurriendo solo mediante la ruta normal de `default_factory` / `__missing__()`.

No confundas comportamiento de merge con comportamiento de valor ausente.

# Parte III: `deque`

## 27. `deque` es una cola de doble extremo

Un `deque` soporta adiciones y extracciones eficientes en ambos extremos.

```python
from collections import deque

queue = deque(["a", "b"])
queue.append("c")
print(queue.popleft())
```

Es la estructura de la biblioteca estándar adecuada cuando ambos extremos forman parte activa del algoritmo.

## 28. Las operaciones de los extremos son aproximadamente O(1)

La documentación oficial describe las adiciones y extracciones en ambos lados como aproximadamente O(1).

En contraste, quitar el primer elemento de una lista con `pop(0)` requiere desplazar los elementos restantes y es O(n).

Para colas FIFO, prefiere:

```python
from collections import deque

queue = deque()
queue.append("job-1")
job = queue.popleft()
```

en lugar de usar repetidamente `list.pop(0)`.

## 29. `maxlen` crea una ventana de historial limitada

```python
from collections import deque

recent = deque(maxlen=3)

for value in [10, 20, 30, 40, 50]:
    recent.append(value)

print(list(recent))
```

Salida:

```text
[30, 40, 50]
```

Una vez lleno, agregar en un extremo descarta elementos del extremo opuesto.

## 30. La expulsión de `append()` en un deque limitado difiere de `insert()`

Un deque limitado y lleno acepta adiciones en los extremos descartando desde el lado opuesto.

Un `insert()` que haría crecer un deque limitado por encima de `maxlen` lanza `IndexError`.

Las dos operaciones tienen contratos diferentes deliberadamente.

## 31. `extendleft()` invierte el orden de entrada

```python
from collections import deque

values = deque([4])
values.extendleft([1, 2, 3])
print(list(values))
```

Salida:

```text
[3, 2, 1, 4]
```

Cada elemento se añade a la izquierda en secuencia, por lo que el iterable aparece en orden inverso.

## 32. `rotate()` mueve los extremos lógicos

```python
from collections import deque

values = deque([1, 2, 3, 4])
values.rotate(1)
print(list(values))
values.rotate(-2)
print(list(values))
```

Los valores positivos rotan hacia la derecha; los negativos, hacia la izquierda.

Esto es útil para planificación cíclica y algoritmos donde el frente actual cambia repetidamente.

## 33. La indexación de deque no lo convierte en reemplazo de list

El acceso indexado de deque es O(1) cerca de ambos extremos, pero se vuelve O(n) hacia el centro.

Si la operación dominante es acceso posicional aleatorio, una lista suele encajar mejor.

Usa deque por su comportamiento en los extremos, no solo porque admite `d[index]`.

## 34. Operaciones thread-safe en los extremos no forman un modelo completo de transacción

La documentación oficial describe las adiciones y extracciones de deque como thread-safe.

Eso no significa que una secuencia de varios pasos se convierta automáticamente en una transacción atómica de negocio.

Por ejemplo, un flujo de "comprobar, luego extraer, luego actualizar otra estructura" aún puede requerir sincronización explícita si varias threads deben observar toda la secuencia de forma consistente.

Usa la garantía limitada por lo que realmente dice, no como sustituto de diseño de concurrencia.

## 35. Extraer de un deque vacío lanza `IndexError`

```python
from collections import deque

queue = deque()

try:
    queue.popleft()
except IndexError:
    print("queue is empty")
```

Define en tu propio contrato de aplicación si una cola vacía es una rama esperada o una condición excepcional.

# Parte IV: `namedtuple()`

## 36. `namedtuple()` da nombres a las posiciones de una tupla

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
point = Point(10, 20)

print(point.x)
print(point[0])
```

El objeto sigue siendo similar a una tupla: indexable, iterable, desempaquetable e inmutable en el sentido de una tupla.

Los campos con nombre mejoran la legibilidad cuando las posiciones tienen significados estables.

## 37. La factory crea una nueva subclase de tuple

`namedtuple()` no crea un único registro. Crea una clase.

```python
from collections import namedtuple

Coordinate = namedtuple("Coordinate", "latitude longitude")
a = Coordinate(10.0, 20.0)
b = Coordinate(30.0, 40.0)
```

`Coordinate` es la subclase de tupla generada; `a` y `b` son instancias.

## 38. Los defaults se aplican a los campos más a la derecha

```python
from collections import namedtuple

Account = namedtuple("Account", ["name", "active"], defaults=[True])
print(Account("demo"))
```

Un campo con valor por defecto no puede preceder a un campo obligatorio en la firma generada.

## 39. `rename=True` repara nombres de campo inválidos o duplicados

```python
from collections import namedtuple

Row = namedtuple("Row", ["name", "class", "name"], rename=True)
print(Row._fields)
```

Usa esto cuando los nombres de campo provienen de un esquema externo que no controlas completamente.

Cuando controlas el esquema, nombres válidos explícitos suelen ser más claros que depender del renombrado automático.

## 40. Las named tuples son registros inmutables

No puedes asignar directamente a un campo:

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
point = Point(1, 2)

updated = point._replace(x=10)
print(updated)
```

`_replace()` devuelve una nueva instancia.

Desde Python 3.13, argumentos nombrados inválidos pasados a `_replace()` lanzan `TypeError` en lugar de `ValueError`.

## 41. `_asdict()` devuelve un diccionario normal

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
point = Point(1, 2)
print(point._asdict())
```

Desde Python 3.8, `_asdict()` devuelve un `dict` normal, no un `OrderedDict`.

## 42. `_fields` y `_field_defaults` permiten introspección

```python
from collections import namedtuple

Record = namedtuple("Record", "key enabled", defaults=[False])
print(Record._fields)
print(Record._field_defaults)
```

Los guiones bajos iniciales forman parte de la API de named tuples y existen para reducir colisiones con nombres de campos del usuario.

## 43. Vincula la clase generada al nombre del tipo cuando pickle sea importante

La documentación oficial recomienda asignar la clase generada a una variable que coincida con `typename` cuando importe el soporte de pickle:

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
```

La generación dinámica de clases puede interactuar con serialización e importabilidad. Para tipos de registro reutilizables, prefiere definiciones a nivel de módulo.

## 44. `typing.NamedTuple` es la alternativa tipada

Cuando las anotaciones estáticas de campos son centrales al diseño, `typing.NamedTuple` con sintaxis de clase suele ser más claro:

```python
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int
```

Conserva la semántica de tupla mientras expresa directamente los tipos de los campos.

## 45. Una dataclass no es simplemente una named tuple más nueva

Elige por semántica:

```text
necesita compatibilidad con tuple, indexación y unpacking -> namedtuple / NamedTuple
necesita una clase orientada a registros con métodos generados y semántica flexible -> dataclass
```

No migres automáticamente solo porque ambas herramientas crean objetos compactos parecidos a registros.

# Parte V: `ChainMap`

## 46. `ChainMap` crea una vista viva sobre mappings

```python
from collections import ChainMap

defaults = {"mode": "safe", "retries": 2}
overrides = {"mode": "fast"}

config = ChainMap(overrides, defaults)
print(config["mode"])
print(config["retries"])
```

Las búsquedas recorren los mappings del primero al último hasta encontrar una clave.

## 47. ChainMap mantiene los mappings por referencia

```python
from collections import ChainMap

base = {"region": "global"}
config = ChainMap({}, base)

base["region"] = "test"
print(config["region"])
```

Salida:

```text
test
```

Un `ChainMap` no es una copia aplanada anticipada. Los cambios en los mappings subyacentes siguen siendo visibles.

## 48. Escrituras y eliminaciones apuntan solo al primer mapping

```python
from collections import ChainMap

local = {}
defaults = {"retries": 3}
config = ChainMap(local, defaults)

config["retries"] = 1
print(local)
print(defaults)
```

Salida:

```text
{'retries': 1}
{'retries': 3}
```

La precedencia de lectura y el destino de escritura son asimétricos deliberadamente.

## 49. `new_child()` crea una nueva capa frontal escribible

```python
from collections import ChainMap

base = ChainMap({"mode": "safe"})
child = base.new_child({"mode": "fast"})

print(child["mode"])
print(base["mode"])
```

Esto modela naturalmente ámbitos anidados y capas temporales de override.

## 50. `parents` omite el primer mapping

`chain.parents` devuelve un nuevo `ChainMap` sobre todos los mappings excepto el primero.

Es útil cuando la primera capa representa el ámbito local actual y necesitas la vista envolvente.

## 51. El orden de iteración no es el orden de búsqueda

Las búsquedas recorren del primer mapping al último.

El orden de iteración se determina recorriendo los mappings del último al primero con semántica de sobrescritura de mapping.

Esto puede sorprender al código que asume que "primero buscado" también significa "primero iterado".

Prueba el contrato del que realmente depende tu programa.

## 52. Aplana explícitamente cuando necesites un snapshot

```python
from collections import ChainMap

config = ChainMap({"mode": "fast"}, {"mode": "safe", "retries": 2})
snapshot = dict(config)
```

El diccionario normal es independiente como snapshot de los valores resueltos en ese momento.

Usa `ChainMap` cuando la superposición viva sea la característica. Usa un diccionario combinado cuando la característica sea un snapshot resuelto independiente.

# Parte VI: `OrderedDict`

## 53. Los diccionarios normales ya preservan el orden de inserción

El orden de inserción está garantizado para diccionarios normales desde Python 3.7.

Por lo tanto, "necesito que las claves permanezcan en orden de inserción" normalmente **no** es razón suficiente para elegir `OrderedDict` hoy.

## 54. `OrderedDict` se especializa en reordenación

Todavía proporciona comportamiento diseñado para manipulación deliberada del orden:

```python
from collections import OrderedDict

items = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
items.move_to_end("a")
items.move_to_end("c", last=False)
print(list(items))
```

La reordenación frecuente de extremos es una de las razones restantes para considerarlo.

## 55. La igualdad de `OrderedDict` puede ser sensible al orden

Dos objetos `OrderedDict` comparan iguales solo cuando coinciden sus pares clave-valor y su orden.

La igualdad de diccionarios normales ignora el orden de inserción.

Esta diferencia semántica importa cuando el orden forma parte del contrato del valor y no solo de la presentación.

## 56. `popitem(last=False)` expresa eliminación FIFO directamente

`OrderedDict.popitem()` acepta `last=True` o `last=False`.

El `popitem()` de un dict normal elimina el elemento insertado más recientemente. `OrderedDict` tiene una API directa para elegir cualquiera de los extremos.

Si no necesitas estas semánticas especializadas de reordenación, prefiere un diccionario normal.

# Parte VII: Wrappers de extensión e interfaces de colección

## 57. `UserDict`, `UserList` y `UserString` envuelven tipos integrados

Estas clases ofrecen bases orientadas a wrappers cuyo contenido subyacente está disponible mediante `.data`.

```python
from collections import UserDict


class NormalizedKeys(UserDict):
    def __setitem__(self, key: str, value: object) -> None:
        super().__setitem__(key.strip().lower(), value)
```

Pueden ser más fáciles de extender de forma consistente que subclasificar directamente un tipo integrado cuando quieres interceptar muchas operaciones mediante una abstracción wrapper controlada.

## 58. Las bases wrapper son una elección de diseño, no una obligación

Python moderno permite subclasificar directamente `dict`, `list` y `str` en muchas situaciones.

Las clases `User*` siguen siendo útiles cuando el acceso al contenedor `.data` y su modelo de extensión hacen más sencilla la personalización.

Prefiere composición o una clase específica cuando tu objeto no sea conceptualmente una colección de propósito general.

## 59. `collections.abc` modela interfaces

```python
from collections.abc import Mapping, Sequence

print(isinstance({"a": 1}, Mapping))
print(isinstance([1, 2, 3], Sequence))
```

Las ABC permiten que el código pregunte "¿este objeto satisface una interfaz tipo mapping/sequence?" en lugar de "¿este objeto es exactamente un dict/list?".

Eso favorece APIs más flexibles.

## 60. Las pruebas con `Iterable` tienen una limitación importante

`isinstance(obj, Iterable)` reconoce iterables registrados y objetos con `__iter__()`.

No detecta de manera fiable todos los objetos heredados que pueden iterar mediante `__getitem__()`.

La documentación oficial indica que la única forma fiable de determinar si un objeto es iterable es llamar a `iter(obj)` y manejar el fallo.

## 61. Los mixins de ABC pueden tener consecuencias de rendimiento

Algunos métodos mixin de `Sequence` llaman repetidamente a `__getitem__()`.

Si una secuencia personalizada implementa `__getitem__()` en O(n), mixins heredados como iteración pueden llegar a O(n²).

Una interfaz puede proporcionar comportamiento correcto y aun así tener el contrato de rendimiento equivocado para una implementación concreta.

# Elegir y combinar las herramientas

## 62. Tabla de decisión

| Necesidad | Prefiere | Razón principal |
|---|---|---|
| Contar valores hashables | `Counter` | Semántica de conteo y multiconjunto |
| Agrupar/crear valores ausentes | `defaultdict` | Política de clave ausente basada en factory |
| Cola FIFO u operaciones en ambos extremos | `deque` | Operaciones eficientes en los extremos |
| Conservar solo los N valores más recientes | `deque(maxlen=N)` | Expulsión automática desde el extremo opuesto |
| Registro compatible con tuple y campos nombrados | `namedtuple` / `NamedTuple` | Campos nombrados más semántica de tupla |
| Superponer mappings con precedencia viva | `ChainMap` | Vista en lugar de merge anticipado |
| Reordenación frecuente de mapping | `OrderedDict` | API orientada a reordenación |
| Extender colección mediante wrapper | `UserDict` / `UserList` / `UserString` | `.data` subyacente controlado |
| Aceptar una interfaz, no un tipo concreto | `collections.abc` | Diseño orientado a protocolos |

## 63. Combina estructuras especializadas solo cuando cada una tenga un trabajo

Un programa puede usar legítimamente:

```text
Counter      -> resumir frecuencias
deque        -> conservar eventos recientes
ChainMap     -> resolver configuración por capas
```

Eso no significa que toda estructura de datos del programa deba venir de `collections`.

La especialización debe simplificar el modelo, no decorarlo con tipos poco familiares.

## 64. Errores comunes

### Usar `Counter` como diccionario genérico

Si los valores no son conteos, usa un mapping diseñado para valores arbitrarios.

### Asumir que `Counter.update()` reemplaza valores

Suma conteos.

### Asumir que un valor cero de `Counter` elimina la clave

Usa `del` si la clave debe desaparecer.

### Leer `defaultdict[key]` solo para comprobar si una clave existe

Eso puede crear la clave.

### Esperar que `defaultdict.get()` invoque la factory

No lo hace.

### Usar `list.pop(0)` para una cola FIFO duradera

Usa `deque.popleft()` cuando la cola crece y se reduce por el frente.

### Tratar el indexado intermedio de deque como O(1)

Usa listas para acceso posicional aleatorio rápido.

### Asumir que `extendleft()` conserva el orden del iterable

Invierte el orden visible.

### Esperar que las escrituras en `ChainMap` actualicen el mapping donde se encontró la clave

Las escrituras van solo al primer mapping.

### Usar `OrderedDict` solo porque los diccionarios deben conservar orden de inserción

Los diccionarios normales ya lo hacen.

## 65. Ejemplo práctico: reconciliación de capacidad con `Counter`

```python
from collections import Counter

required = Counter({"sensor": 4, "cable": 3, "case": 2})
packed = Counter({"sensor": 4, "cable": 1, "case": 3})

missing = required - packed
surplus = packed - required

print(f"required units: {required.total()}")
print(f"missing: {dict(missing)}")
print(f"surplus: {dict(surplus)}")
```

Salida esperada:

```text
required units: 9
missing: {'cable': 2}
surplus: {'case': 1}
```

El modelo de datos comunica que estos mappings representan cantidades, no estado arbitrario clave-valor.

## 66. Ejemplo práctico: agrupación con `defaultdict`

```python
from collections import defaultdict

records = [
    ("billing", "INV-101"),
    ("support", "REQ-203"),
    ("billing", "INV-102"),
]

by_team = defaultdict(list)

for team, reference in records:
    by_team[team].append(reference)
```

La factory elimina boilerplate de inicialización mientras mantiene visible la intención de agrupación.

## 67. Ejemplo práctico: historial reciente con deque limitado

```python
from collections import deque

recent = deque(maxlen=3)

for event in ["boot", "load-config", "connect", "ready"]:
    recent.append(event)

print(list(recent))
```

Salida esperada:

```text
['load-config', 'connect', 'ready']
```

No hace falta una rama explícita tipo "si está lleno, elimina el más antiguo".

## 68. Ejemplo práctico: precedencia de configuración con `ChainMap`

```python
from collections import ChainMap

defaults = {"mode": "safe", "retries": 2}
environment = {"retries": 4}
command_line = {"mode": "fast"}

config = ChainMap(command_line, environment, defaults)

print(config["mode"])
print(config["retries"])
```

Salida esperada:

```text
fast
4
```

La cadena conserva las capas originales mientras ofrece una sola vista de búsqueda.

## 69. Ejercicio

Construye una pequeña simulación de procesamiento de tareas con estos requisitos:

1. Deben contarse las categorías de tareas recibidas.
2. Las tareas pendientes de ejecución deben permitir eliminación FIFO desde la izquierda.
3. Solo deben conservarse los cinco IDs de tareas completadas más recientes.
4. La configuración debe resolverse desde los mappings `runtime`, luego `environment`, luego `defaults`, sin copiarlos en un único diccionario.
5. El programa debe imprimir:
   - total de tareas recibidas;
   - conteos por categoría;
   - orden en que se procesan las tareas;
   - historial de finalización conservado;
   - límite de reintentos resuelto.

Herramientas sugeridas:

```text
Counter
deque
ChainMap
```

No uses un contenedor especializado solo porque aparece en la lista. Explica en comentarios o notas por qué cada estructura elegida coincide con las operaciones requeridas.

## 70. Referencia rápida

```python
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple

Counter(iterable)
Counter(mapping)
counter.total()
counter.most_common(n)
counter.update(...)
counter.subtract(...)
+counter
-counter

defaultdict(list)
defaultdict(int)
mapping.default_factory

deque(iterable)
deque(iterable, maxlen=n)
d.append(value)
d.appendleft(value)
d.pop()
d.popleft()
d.extend(values)
d.extendleft(values)
d.rotate(n)

Record = namedtuple("Record", "field_a field_b")
record._asdict()
record._replace(field_a=value)
Record._fields
Record._field_defaults

ChainMap(front, fallback)
chain.maps
chain.new_child()
chain.parents

ordered.move_to_end(key, last=True)
ordered.popitem(last=False)
```

## 71. Checklist de diseño

Antes de elegir una colección especializada, pregunta:

- ¿Qué operación domina este flujo?
- ¿Qué debe significar un valor ausente?
- ¿La estructura puede mutar durante una lectura?
- ¿Es importante el rendimiento en los extremos?
- ¿El orden forma parte de la igualdad o solo de la iteración?
- ¿Necesito una vista viva o una copia estática?
- ¿Importa la compatibilidad con tuple?
- ¿Sería más simple un tipo integrado?
- ¿Dependo de comportamiento específico de versión?
- ¿He probado las semánticas importantes y no solo la salida del camino feliz?

## 72. Conexiones con otros conceptos de Python

`collections` se conecta directamente con temas ya estudiados:

- **Colecciones de la Fase 3:** los contenedores especializados se construyen sobre los modelos mentales de listas, tuplas, diccionarios y conjuntos.
- **Bucles:** `Counter`, agrupación, colas e historiales limitados suelen procesar iterables incrementalmente.
- **Funciones:** las factories pasadas a `defaultdict` son políticas invocables.
- **Type hints:** `typing.NamedTuple` e interfaces genéricas de colección hacen explícitos los contratos de datos.
- **Programación orientada a objetos:** wrappers `User*` y ABC muestran modelos distintos de extensión.
- **Algoritmos:** elegir entre operaciones al frente de una list y extremos de deque cambia la complejidad.
- **Diseño de configuración:** `ChainMap` modela precedencia sin aplanar las capas de origen.
- **Pruebas:** semánticas como creación de claves ausentes, igualdad sensible al orden y expulsión en estructuras limitadas merecen pruebas de comportamiento.

## Referencias

Referencias primarias usadas en este capítulo:

- [Documentación Python 3.14: `collections` — tipos de datos contenedor](https://docs.python.org/3.14/library/collections.html)
- [Documentación Python 3.14: `collections.abc` — clases base abstractas para contenedores](https://docs.python.org/3.14/library/collections.abc.html)
- [Documentación Python 3.14: `typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple)
- [Tutorial Python 3.14: estructuras de datos, incluida la orientación de deque para colas](https://docs.python.org/3.14/tutorial/datastructures.html#using-lists-as-queues)

## Próximo capítulo

Continúa con el **Capítulo 07: `itertools`** cuando esté disponible.

El próximo capítulo cambia de **contenedores** especializados a **pipelines de iteradores** especializados: componiendo transformaciones lazy, repetición, slicing, agrupación e iteración combinatoria sin crear colecciones intermedias innecesarias.
