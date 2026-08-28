<div align="center">

# Controlando Contratos de Serialización y Decodificación JSON

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Biblioteca Estándar](../README.es.md) · [← Anterior: Trabajando con Fechas y Cálculos de Tiempo Usando `datetime`](../02-datetime/README.es.md)

La Phase 7 presentó JSON como formato de datos estructurados y enseñó la diferencia práctica entre `load()`, `loads()`, `dump()` y `dumps()`. Este capítulo profundiza una capa más.

El módulo `json` no sirve solamente para leer y escribir archivos `.json`. También es una herramienta de frontera. Sus opciones deciden qué valores de Python se aceptan, cómo se reconstruyen los números, si se toleran valores fuera del estándar, cómo se representan tipos personalizados, cómo se tratan nombres duplicados dentro de objetos y qué tan estable es la representación serializada.

El objetivo es convertir "JSON funciona" en una pregunta más precisa:

```text
¿Qué contrato JSON acepta y produce este programa?
```

**Tiempo estimado de estudio:** 120–160 minutos.

**Requisito de Python:** Python 3.10 o posterior para las APIs principales. El comando directo `python -m json` mostrado más adelante está disponible en Python 3.14; versiones soportadas anteriores pueden usar `python -m json.tool`.

**Base de documentación:** el comportamiento y los ejemplos fueron verificados con la documentación oficial de `json` de Python 3.14.

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- tratar la serialización JSON como un contrato de interfaz y no solamente como una operación de archivo;
- distinguir texto JSON de codificación en bytes;
- producir salida estable con `sort_keys` cuando un orden determinista sea útil;
- controlar espacios con `indent` y `separators`;
- explicar qué cambia `ensure_ascii` y qué no cambia;
- rechazar valores de punto flotante no finitos con `allow_nan=False`;
- rechazar constantes no estándar del decoder de Python con `parse_constant`;
- decodificar números JSON con funciones personalizadas como `decimal.Decimal`;
- reconocer límites de interoperabilidad relacionados con rango y precisión numérica;
- entender por qué los nombres de miembros de objetos JSON son strings;
- evitar descartar silenciosamente claves incompatibles con `skipkeys=True` cuando esa política no sea deliberada;
- serializar valores Python personalizados seleccionados con `default` o `JSONEncoder`;
- reconstruir representaciones seleccionadas con `object_hook`;
- inspeccionar pares nombre-valor ordenados con `object_pairs_hook`;
- detectar nombres duplicados en objetos JSON cuando la unicidad forme parte del contrato;
- mantener activada la detección de referencias circulares salvo una razón específica;
- usar detalles de `JSONDecodeError` para diagnósticos útiles;
- limitar entrada JSON no confiable según la frontera controlada;
- usar la interfaz de línea de comandos JSON de Python para validar y formatear;
- distinguir documentos JSON ordinarios de formatos JSON delimitados por líneas.

## 1. ¿Qué cambia respecto de la introducción a JSON de la Phase 7?

Ya conoces las cuatro operaciones principales:

```python
import json

text = json.dumps({"topic": "JSON"})
data = json.loads(text)
```

y las variantes orientadas a archivos:

```python
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

La Phase 7 se concentró en la frontera del formato:

```text
texto JSON
   ↓ parsing
valores Python
```

Este capítulo se concentra en la política alrededor de esa frontera:

```text
valores Python
   ↓ política de serialización
representación JSON
   ↓ transporte / almacenamiento
representación JSON
   ↓ política de decodificación
valores Python
```

Las APIs son conocidas. Los contratos son más profundos.

## 2. La serialización forma parte de un contrato de interfaz

Dos strings JSON pueden representar el mismo objeto lógico y aun así diferir en espacios o en el orden de los miembros:

```json
{"topic":"JSON","score":88}
```

```json
{
  "score": 88,
  "topic": "JSON"
}
```

Eso significa que el texto serializado puede tener al menos dos tipos de requisito:

- **requisitos semánticos**, como campos obligatorios y tipos de valores permitidos;
- **requisitos de representación**, como espacios, orden, escaping o sintaxis numérica estricta.

No asumas que uno implica el otro.

## 3. `dumps()` produce texto, no bytes

`json.dumps()` devuelve un `str` de Python:

```python
import json

text = json.dumps({"topic": "JSON"})
print(type(text).__name__)
```

Salida:

```text
str
```

Si un protocolo de red o una capa de almacenamiento necesita bytes, la codificación es un paso separado:

```python
payload = text.encode("utf-8")
```

Mantén las capas separadas:

```text
valores Python
   ↓ json.dumps()
texto Unicode
   ↓ .encode("utf-8")
bytes
```

El lado de encoding de `json` trabaja con texto: `json.dumps()` devuelve `str`, y `json.dump()` escribe texto en un objeto file-like compatible. El lado de decoding acepta un conjunto más amplio de entradas: `json.loads()` acepta `str`, `bytes` y `bytearray`, mientras que `json.load()` puede consumir un objeto file-like compatible cuyo `read()` devuelva una de esas formas soportadas. Si la aplicación controla una frontera de bytes de red o almacenamiento, una política explícita de encoding sigue haciendo que esa frontera sea más fácil de comprender.

## 4. Orden determinista de miembros con `sort_keys=True`

Los diccionarios de Python conservan el orden de inserción, pero ese orden no siempre es la política de representación deseada.

Para tests, snapshots, ejemplos o archivos de configuración generados, ordenar claves puede facilitar comparaciones:

```python
import json

record = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(record, sort_keys=True)

print(text)
```

`sort_keys=True` ordena las claves de los diccionarios en la salida serializada.

Esto puede mejorar el determinismo, pero **no** convierte JSON arbitrario en una forma canónica universal. Los estándares de canonicalización pueden definir reglas adicionales para números, Unicode, escaping y otros detalles de representación.

## 5. Salida legible para personas con `indent`

Usa `indent` cuando se espera que personas inspeccionen la salida:

```python
import json

record = {"topic": "JSON", "score": 88}
print(json.dumps(record, indent=2))
```

Pretty printing aumenta el espacio en blanco y normalmente aumenta el tamaño de la representación.

Elígelo porque la interfaz se beneficia de legibilidad, no porque JSON indentado sea más correcto.

## 6. Salida compacta con `separators`

Para una representación compacta, elimina espacios opcionales alrededor de separadores:

```python
import json

record = {"topic": "JSON", "score": 88}
text = json.dumps(record, separators=(",", ":"))

print(text)
```

Esto produce:

```text
{"topic":"JSON","score":88}
```

Una receta común para salida determinista orientada a máquinas es:

```python
import json

record = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(
    record,
    sort_keys=True,
    separators=(",", ":"),
)
```

De nuevo, una salida estable para tu aplicación no es automáticamente una representación JSON canónica definida por un estándar externo.

## 7. `ensure_ascii` controla escaping, no la codificación del texto

Por defecto, los caracteres no ASCII se escapan:

```python
import json

record = {"language": "Português"}
print(json.dumps(record))
```

Con `ensure_ascii=False`, esos caracteres pueden permanecer visibles directamente en el `str` devuelto:

```python
import json

record = {"language": "Português"}
print(json.dumps(record, ensure_ascii=False))
```

Esto **no** significa que el módulo JSON haya elegido bytes UTF-8. El resultado sigue siendo un `str` de Python.

Si lo escribes en un archivo de texto UTF-8, la decisión de encoding pertenece a la frontera del archivo:

```python
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(record, file, ensure_ascii=False)
```

## 8. Salida JSON estricta y floats no finitos

El encoder de Python permite deliberadamente estos valores de punto flotante por defecto:

- `NaN`;
- `Infinity`;
- `-Infinity`.

Esos tokens no son JSON válido según la especificación interoperable de JSON.

Cuando se exige salida compatible con el estándar, usa `allow_nan=False`:

```python
import json

record = {"value": float("nan")}

try:
    json.dumps(record, allow_nan=False)
except ValueError:
    print("Non-finite float rejected")
```

Esto es una decisión de contrato. Un `json.dumps()` por defecto que termina con éxito no demuestra que el texto generado evite la extensión numérica no estándar de Python.

## 9. Entrada JSON estricta y `parse_constant`

El decoder tiene la extensión equivalente. Por defecto, Python acepta `NaN`, `Infinity` y `-Infinity`.

Para rechazarlos, proporciona un callback mediante `parse_constant`:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


text = '{"value": NaN}'

try:
    json.loads(text, parse_constant=reject_nonstandard_constant)
except ValueError as error:
    print(error)
```

`JSONDecodeError` sigue representando errores normales de sintaxis JSON. El `ValueError` anterior proviene del callback que suministraste deliberadamente.

Una interfaz estricta suele necesitar ambas direcciones:

```text
encoding: allow_nan=False
decoding: parse_constant=callback que rechaza
```

## 10. Los números JSON no definen la política de precisión de la aplicación

JSON tiene una sintaxis de números, pero implementaciones diferentes pueden mapearlos a tipos numéricos y límites de precisión distintos.

Python normalmente decodifica:

- números JSON con forma de entero, sin fracción ni exponente, a `int`;
- números JSON que contienen fracción o exponente a `float`.

```python
import json

data = json.loads('{"count": 3, "ratio": 0.1}')

print(type(data["count"]).__name__)
print(type(data["ratio"]).__name__)
```

Para interfaces que intercambian enteros muy grandes o decimales de alta precisión, los límites del sistema receptor también importan. Un `int` de Python puede representar valores que otra implementación quizá no preserve exactamente.

La interoperabilidad es una propiedad de ambos extremos de la interfaz.

## 11. Decodifica números JSON de punto flotante con `parse_float`

El decoder puede entregar cada número JSON de punto flotante a una función que tú elijas. Eso incluye tokens con parte fraccionaria, como `19.90`, y formas exponenciales como `1e2`.

Por ejemplo, `decimal.Decimal` puede preservar exactamente el texto decimal:

```python
import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
```

Esto es útil cuando la aplicación necesita semántica decimal en lugar de semántica de punto flotante binario.

No significa que `Decimal` se convierta en un tipo JSON nativo. Es una decisión de decodificación dentro de Python.

## 12. `parse_int` también puede personalizar enteros

`parse_int` recibe el texto de cada entero JSON:

```python
import json


def tagged_integer(text: str):
    return ("integer", text)


data = json.loads('{"count": 42}', parse_int=tagged_integer)
print(data["count"])
```

Personalizar parsing de enteros es menos común en aplicaciones para principiantes, pero muestra un principio importante: decodificar es reconstrucción configurable, no una conversión mágica uno-a-uno.

Usa un hook numérico personalizado solamente cuando su comportamiento forme parte de un contrato documentado.

## 13. Los nombres de objetos JSON son strings

Los nombres de miembros de objetos JSON son strings.

El encoder de Python acepta algunas claves básicas que no son strings y las convierte, por lo que un round trip puede no preservar tipos de clave:

```python
import json

original = {1: "one", 2: "two"}
restored = json.loads(json.dumps(original))

print(original)
print(restored)
print(original == restored)
```

Las claves decodificadas son strings.

Si el tipo de la clave lleva significado en tu aplicación, representa ese significado explícitamente en lugar de depender de un round trip de claves de diccionario.

## 14. Prefiere fallos visibles a `skipkeys=True`

Por defecto, tipos de clave no soportados generan `TypeError`:

```python
import json

record = {(1, 2): "coordinate"}

try:
    json.dumps(record)
except TypeError:
    print("Unsupported key type")
```

`skipkeys=True` puede omitir silenciosamente claves no soportadas:

```python
text = json.dumps(record, skipkeys=True)
```

Eso solamente es apropiado cuando descartar esas entradas es una política explícita.

Para la mayoría de los contratos de datos, perder información silenciosamente es más peligroso que recibir una excepción que obliga a diseñar correctamente la representación.

## 15. Serialización personalizada con `default`

Objetos Python arbitrarios no son serializables a JSON por defecto.

Un callback `default` puede convertir objetos seleccionados no soportados en estructuras compatibles con JSON:

```python
import json
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def encode_custom(value):
    if isinstance(value, Point):
        return {"type": "point", "x": value.x, "y": value.y}
    raise TypeError(f"unsupported type: {type(value).__name__}")


text = json.dumps(Point(4, 7), default=encode_custom, sort_keys=True)
print(text)
```

Un buen callback maneja solamente los tipos que soporta deliberadamente y genera `TypeError` para los demás.

No conviertas `default` en una solución genérica que adivine cómo serializar cualquier objeto.

## 16. Las representaciones etiquetadas son tu schema, no el schema de JSON

Esta representación:

```json
{"type": "point", "x": 4, "y": 7}
```

es JSON normal. El significado de `"type": "point"` pertenece a tu aplicación.

Eso significa que tu contrato debe responder preguntas como:

- ¿`type` es obligatorio?
- ¿Qué nombres de tipo están permitidos?
- ¿`x` e `y` deben ser enteros obligatorios?
- ¿Qué ocurre con campos extra?
- ¿Qué versión del schema produjo el documento?

La sintaxis JSON no responde esas preguntas de negocio.

## 17. Un `JSONEncoder` personalizado puede centralizar el comportamiento

Para una política de encoding reutilizable, hereda de `json.JSONEncoder` y sobrescribe `default()`:

```python
import json
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class StudyEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, Point):
            return {"type": "point", "x": value.x, "y": value.y}
        return super().default(value)


text = json.dumps(Point(4, 7), cls=StudyEncoder)
print(text)
```

Usa un encoder personalizado cuando la aplicación realmente se beneficie de una política reutilizable. Para una conversión única, una transformación explícita o una función `default` suele ser más fácil de entender.

## 18. Reconstrucción personalizada con `object_hook`

`object_hook` se llama para cada objeto JSON decodificado después de que se convierte en un diccionario.

```python
import json


def decode_custom(record):
    if record.get("type") == "point":
        return (record["x"], record["y"])
    return record


text = '{"type": "point", "x": 4, "y": 7}'
data = json.loads(text, object_hook=decode_custom)

print(data)
```

El valor que devuelve el hook reemplaza ese diccionario en el resultado decodificado.

Esto es potente, así que mantén la política estrecha y explícita.

## 19. No permitas que tags no confiables elijan caminos arbitrarios de código

Un `object_hook` es código Python ejecutado durante la decodificación.

Evita diseños donde un string no confiable pueda seleccionar dinámicamente imports, clases, funciones o constructores arbitrarios.

Prefiere una allowlist fija de representaciones conocidas:

```text
tag de entrada
   ↓ validar contra valores conocidos
conversión conocida
```

JSON en sí mismo es un formato de datos. El riesgo aparece cuando la aplicación concede demasiada autoridad a datos no confiables sobre qué código ejecutar después.

## 20. Los nombres duplicados en objetos se aceptan por defecto

Considera este texto JSON:

```json
{"topic": "JSON", "topic": "CSV"}
```

El decoder por defecto de Python acepta nombres repetidos y conserva solamente el último valor:

```python
import json

text = '{"topic": "JSON", "topic": "CSV"}'
data = json.loads(text)

print(data)
```

Salida:

```text
{'topic': 'CSV'}
```

Si la unicidad importa para tu interfaz, la decodificación por defecto no alcanza para imponerla.

## 21. Inspecciona pares con `object_pairs_hook`

`object_pairs_hook` recibe los pares nombre-valor de cada objeto JSON en orden, antes de que se conviertan en un diccionario ordinario.

Eso permite detectar duplicados:

```python
import json


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


text = '{"topic": "JSON", "topic": "CSV"}'

try:
    json.loads(text, object_pairs_hook=reject_duplicate_keys)
except ValueError as error:
    print(error)
```

Este es otro ejemplo de convertir una suposición vaga en un contrato aplicado.

## 22. `object_pairs_hook` tiene prioridad sobre `object_hook`

Si se proporcionan ambos, `object_pairs_hook` tiene prioridad para la decodificación de objetos.

Evita combinar hooks de forma casual. Si una política necesita detección de duplicados y reconstrucción personalizada, diseña los pasos para que orden y responsabilidades sean evidentes.

Una política de decoder clara es más fácil de auditar que un conjunto de hooks que se superponen accidentalmente.

## 23. Mantén activada la detección de referencias circulares

Los containers de Python pueden contener ciclos:

```python
items = []
items.append(items)
```

JSON no puede representar directamente ese grafo de objetos.

El encoder verifica referencias circulares por defecto. Mantén `check_circular=True` salvo que exista una razón medida y bien comprendida para desactivarlo.

Desactivar la verificación no hace que los ciclos sean serializables. Elimina la protección que los detecta y puede llevar a un fallo de recursión.

## 24. Usa los detalles de `JSONDecodeError` para diagnóstico

`JSONDecodeError` incluye información útil de ubicación:

```python
import json

text = '{"topic": "JSON",}'

try:
    json.loads(text)
except json.JSONDecodeError as error:
    print(error.msg)
    print(error.lineno)
    print(error.colno)
```

Campos útiles incluyen:

- `msg` para el mensaje del decoder;
- `lineno` para el número de línea;
- `colno` para el número de columna;
- `pos` para la posición del carácter en el documento fuente.

Expón solamente el nivel de detalle apropiado para la interfaz. Los diagnósticos de una herramienta para desarrolladores y los diagnósticos devueltos por un servicio público no tienen por qué ser idénticos.

## 25. Hacer parsing de JSON válido sigue sin ser validar el schema

Esto es JSON válido:

```json
{"score": -500, "status": "banana"}
```

El trabajo del decoder es reconstruir valores. Tu programa todavía necesita validar reglas de dominio:

```python
import json

record = json.loads('{"score": -500}')

if not 0 <= record["score"] <= 100:
    raise ValueError("score must be between 0 and 100")
```

Mantén estas preguntas separadas:

```text
¿El texto es JSON válido?
        ↓
¿La forma decodificada coincide con el schema de la interfaz?
        ↓
¿Los valores satisfacen las reglas de la aplicación?
```

## 26. Limita la entrada no confiable

La documentación oficial de Python advierte que JSON malicioso puede consumir CPU y memoria considerables durante la decodificación.

El módulo `json` no es un sistema general de cuotas de recursos. En fronteras que controlas, considera límites como:

- tamaño máximo de request o archivo;
- profundidad máxima aceptada definida por la aplicación o gateway alrededor;
- timeouts en la capa de transporte o worker;
- límites de schema para tamaños de arrays y strings.

No aceptes un payload ilimitado solamente porque la sintaxis sea JSON.

## 27. La codificación de texto es una preocupación separada de transporte

JSON intercambiado como bytes necesita una codificación de caracteres acordada. UTF-8 es el estándar de interoperabilidad en sistemas modernos.

Cuando controlas I/O de archivos, deja la codificación explícita:

```python
import json

record = {"language": "Português"}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(record, file, ensure_ascii=False)
```

El serializer de Python no añade una byte-order mark a su salida JSON. Mantén las decisiones de encoding del transporte fuera del modelo lógico de datos siempre que sea posible.

## 28. El valor JSON de nivel superior no tiene que ser un objeto

Todos estos son valores JSON válidos en el nivel superior según especificaciones modernas:

```json
42
```

```json
"ready"
```

```json
true
```

```json
[1, 2, 3]
```

Tu API todavía puede exigir un objeto o un array. Eso sería un **contrato de la aplicación**, no una regla universal de sintaxis JSON.

Valida la forma de nivel superior que realmente esperas.

## 29. La interfaz de línea de comandos puede validar y formatear JSON

Python incluye una herramienta JSON de línea de comandos.

En Python 3.14, la forma directa preferida es:

```text
python -m json data.json
```

Para compatibilidad con versiones anteriores, esta forma sigue disponible:

```text
python -m json.tool data.json
```

El comando es útil para validación rápida y formato legible.

La interfaz de Python 3.14 también admite opciones como:

```text
--sort-keys
--no-ensure-ascii
--json-lines
--indent
--tab
--compact
```

Usa `python -m json --help` para consultar las opciones exactas del intérprete que estás ejecutando.

## 30. JSON Lines es otro contrato de framing

Un único documento JSON contiene un valor JSON de nivel superior.

Esto no es un único documento JSON ordinario:

```text
{"id": 1}
{"id": 2}
{"id": 3}
```

Sin embargo, puede ser un contrato válido de **JSON Lines / JSON delimitado por líneas** cuando cada línea se define de forma independiente como un valor JSON.

La CLI JSON de Python 3.14 tiene soporte para `--json-lines`, pero tu aplicación todavía debe declarar que consume un formato delimitado por líneas.

No confundas:

```text
un documento JSON que contiene un array
```

con:

```text
múltiples valores JSON delimitados por líneas
```

La regla de framing forma parte de la interfaz.

## 31. Llamadas repetidas a `dump()` todavía no crean framing

Esta sigue siendo una frontera importante de la Phase 7:

```python
json.dump(first, file)
json.dump(second, file)
```

Llamadas repetidas no añaden automáticamente un separador o container que convierta los valores en un documento JSON válido.

Elige una estructura explícita:

- un array que contenga múltiples valores;
- un objeto que contenga colecciones con nombre;
- un formato JSON delimitado por líneas documentado;
- otro protocolo que defina framing.

## 32. Salida estable no es canonicalización criptográfica

Una receta local útil como:

```python
json.dumps(
    data,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)
```

puede hacer estables snapshots y diffs en una aplicación Python controlada.

No uses automáticamente ese string para firmas, hashes compartidos entre implementaciones o protocolos de canonicalización entre lenguajes.

Esos casos requieren una especificación de canonicalización que defina todas las reglas relevantes de representación.

## 33. Una política práctica de decodificación estricta

Para una interfaz que quiera rechazar constantes numéricas no estándar de Python y nombres duplicados de objetos, combina hooks estrechos deliberadamente:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


def load_strict_json(text: str):
    return json.loads(
        text,
        parse_constant=reject_nonstandard_constant,
        object_pairs_hook=reject_duplicate_keys,
    )
```

Esto todavía no valida tu schema de negocio. Solamente endurece dos políticas de decodificación JSON.

## 34. Una política práctica de encoding determinista

Para snapshots independientes de lectura humana o artefactos generados donde una salida compacta y estable ayuda:

```python
import json


def dump_stable_json(data):
    return json.dumps(
        data,
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
```

La política ahora comunica varias decisiones explícitamente:

- rechazar floats no finitos;
- mantener caracteres Unicode legibles en el texto Python;
- ordenar claves de diccionario;
- eliminar espacios opcionales de los separadores.

Eso es mucho más fácil de revisar que depender de defaults no documentados dispersos por el código.

## 35. Errores comunes

### Error 1: tratar parsing exitoso como validación de schema

Sintaxis válida no demuestra que campos obligatorios, tipos, rangos o reglas de negocio sean correctos.

### Error 2: asumir que el JSON por defecto de Python es estricto en ambas direcciones

Por defecto, Python acepta y emite `NaN`, `Infinity` y `-Infinity`.

### Error 3: asumir que un round trip preserva cada tipo de Python

Las tuplas se convierten en arrays y regresan como listas; los nombres de objetos son strings; los objetos personalizados necesitan una representación explícita.

### Error 4: activar `skipkeys=True` para hacer desaparecer errores

Eso puede eliminar datos silenciosamente.

### Error 5: usar `default=str` sin definir un contrato

Convertir cada objeto no soportado en un string de presentación arbitrario puede hacer que la serialización tenga éxito mientras destruye el significado del tipo.

### Error 6: usar `sort_keys=True` y llamar al resultado JSON canónico

Ordenar claves resuelve solamente una dimensión de la representación.

### Error 7: decodificar entrada no confiable sin límites

Los parsers de sintaxis todavía pueden consumir CPU y memoria.

### Error 8: construir dinámicamente objetos Python arbitrarios a partir de tags no confiables

Mantén la reconstrucción personalizada en una allowlist explícita y valida campos antes de usarlos.

## 36. Ejemplo práctico: salida JSON determinista

```python
import json


data = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(
    data,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)

print(text)
```

Salida esperada:

```text
{"score":88,"status":"ready","topic":"JSON"}
```

Versión ejecutable: [`examples/deterministic_json.py`](examples/deterministic_json.py).

## 37. Ejemplo práctico: manejo estricto de números no finitos

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


try:
    json.dumps({"value": float("nan")}, allow_nan=False)
except ValueError:
    print("Encoding rejected non-finite float")

try:
    json.loads('{"value": NaN}', parse_constant=reject_nonstandard_constant)
except ValueError:
    print("Decoding rejected non-standard constant")
```

Versión ejecutable: [`examples/strict_numbers.py`](examples/strict_numbers.py).

## 38. Ejemplo práctico: decodificación decimal

```python
import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90, "quantity": 3}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
print(type(data["quantity"]).__name__)
```

Versión ejecutable: [`examples/decimal_decode.py`](examples/decimal_decode.py).

## 39. Ejemplo práctico: rechazar nombres duplicados de objetos

```python
import json


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


samples = [
    '{"topic": "JSON", "score": 88}',
    '{"topic": "JSON", "topic": "CSV"}',
]

for text in samples:
    try:
        data = json.loads(text, object_pairs_hook=reject_duplicate_keys)
    except ValueError as error:
        print(error)
    else:
        print(data)
```

Versión ejecutable: [`examples/reject_duplicate_keys.py`](examples/reject_duplicate_keys.py).

## 40. Ejercicio

Crea una función llamada `decode_settings(text)` para un contrato de configuración de aplicación.

Requisitos:

1. Analiza el string JSON.
2. Rechaza `NaN`, `Infinity` y `-Infinity`.
3. Rechaza nombres duplicados en objetos.
4. Exige que el valor de nivel superior sea un diccionario.
5. Exige exactamente estos campos: `theme`, `refresh_seconds` y `enabled`.
6. Exige que `theme` sea un string no vacío.
7. Exige que `refresh_seconds` sea un entero de 1 a 3600. Recuerda que `bool` es subclase de `int`, por lo que debes rechazar booleanos explícitamente si no son válidos aquí.
8. Exige que `enabled` sea un booleano.
9. Devuelve el diccionario validado.

Después crea una segunda función, `encode_settings(data)`, que:

1. serialice con `allow_nan=False`;
2. use `ensure_ascii=False`;
3. ordene claves;
4. use separadores compactos.

Prueba al menos estos casos:

```text
configuración válida
campo faltante
campo duplicado
valor NaN
tipo incorrecto en el nivel superior
refresh_seconds = true
refresh_seconds = 0
```

La parte importante no es solamente hacer funcionar la entrada válida. Haz cada frontera lo suficientemente explícita para que una futura persona pueda explicar **por qué** se rechaza una entrada inválida.

## 41. Referencia rápida

| Necesidad | Herramienta / política |
|---|---|
| Valor Python → texto JSON | `json.dumps()` |
| Texto JSON / bytes → valor Python | `json.loads()` |
| Leer JSON desde un objeto file-like compatible de texto o binario | `json.load()` |
| Escribir JSON a un objeto file-like de texto | `json.dump()` |
| Salida legible | `indent=2` u otro indent explícito |
| Salida compacta | `separators=(",", ":")` |
| Orden estable de claves | `sort_keys=True` |
| Mantener caracteres no ASCII visibles | `ensure_ascii=False` |
| Rechazar floats no finitos al serializar | `allow_nan=False` |
| Rechazar `NaN` / infinitos al decodificar | `parse_constant=...` |
| Decodificar números JSON de punto flotante de otra forma | `parse_float=...` |
| Decodificar enteros de otra forma | `parse_int=...` |
| Convertir valores personalizados no soportados | `default=...` |
| Encoder personalizado reutilizable | `cls=YourJSONEncoder` |
| Transformar objetos JSON decodificados | `object_hook=...` |
| Inspeccionar pares ordenados / duplicados | `object_pairs_hook=...` |
| Diagnóstico de sintaxis del decoder | `json.JSONDecodeError` |
| Validar / pretty-print desde CLI en Python 3.14 | `python -m json` |
| Forma de CLI compatible con versiones anteriores | `python -m json.tool` |

## 42. Checklist de diseño

Antes de publicar una interfaz JSON, pregunta:

```text
¿Qué forma de nivel superior se acepta?
¿Qué campos son obligatorios?
¿Se rechazan nombres duplicados?
¿Se rechazan NaN e infinitos?
¿Qué precisión numérica se necesita?
¿Qué tamaño máximo puede tener el documento?
¿Cómo se representan tipos personalizados?
¿El orden de claves es relevante solamente para presentación o para otro protocolo?
¿Qué encoding de caracteres transporta el texto JSON como bytes?
¿Es un único documento JSON o un formato delimitado por líneas?
```

Si esas respuestas son explícitas, la frontera JSON se vuelve mucho más fácil de probar y mantener.

## Referencias

- [Documentación Python 3.14: `json` — JSON encoder and decoder](https://docs.python.org/3.14/library/json.html)
- [Documentación Python 3.14: interfaz de línea de comandos JSON](https://docs.python.org/3.14/library/json.html#module-json.tool)
- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259)

## Próximo capítulo

Continúa con el [**Capítulo 04: `csv`**](../04-csv/README.es.md). Profundiza en dialectos, quoting, readers, writers, semántica null, entrada malformada y contratos de interfaces de texto tabular.

[Siguiente → Capítulo 04 · `csv`](../04-csv/README.es.md)
