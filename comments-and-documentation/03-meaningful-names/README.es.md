<div align="center">

# Nombres Significativos y Código Autoexplicativo

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Docstrings](../02-docstrings/README.es.md)

Un nombre es una de las decisiones de diseño más pequeñas de un programa, pero puede leerse cientos de veces. Los buenos nombres reducen la cantidad de contexto que una persona debe reconstruir y ayudan al código a comunicar intención antes de que sea necesario un comentario o una docstring.

> **Principio orientador:** Nombra un concepto de acuerdo con lo que significa en el programa, no solamente de acuerdo con el valor almacenado en él en ese momento.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Requisitos previos | Se recomienda una familiaridad básica con variables y funciones |
| Tiempo estimado de estudio | 50 a 70 minutos |
| Conceptos principales | nombres que revelan intención, `snake_case`, `PascalCase`, constantes, booleanos, unidades, colecciones, alcance, vocabulario, built-ins, refactorización |

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías ser capaz de:

- elegir nombres que revelen propósito, significado del dominio, estado y unidades;
- seguir convenciones comunes de nombres en Python sin tratarlas como reglas de sintaxis;
- distinguir brevedad útil de vaguedad perjudicial;
- nombrar valores booleanos como preguntas o condiciones;
- utilizar nombres plurales para colecciones y singulares para elementos individuales;
- evitar ocultar nombres built-in y palabras reservadas;
- utilizar un vocabulario coherente para el mismo concepto;
- reconocer cuándo una pequeña función o variable puede revelar intención;
- comprender dónde los comentarios y las docstrings siguen siendo necesarios;
- renombrar código de forma segura considerando interfaces públicas.

## 1. Por qué importan los nombres

Python ejecuta identificadores sin importar si son expresivos:

```python
x = 30
y = 0.10
z = x - (x * y)
```

Una persona debe inferir qué significa cada valor. El mismo cálculo puede comunicar mucho más:

```python
subtotal = 30
discount_rate = 0.10
discounted_total = subtotal - (subtotal * discount_rate)
```

La segunda versión no cambia el algoritmo. Cambia el esfuerzo de quien lee.

Los nombres significativos ayudan a responder:

- ¿Qué representa este valor?
- ¿Qué unidad utiliza?
- ¿Es un elemento o una colección?
- ¿El booleano representa estado, capacidad o decisión?
- ¿Qué acción realiza esta función?
- ¿Qué concepto modela esta clase?

## 2. Sintaxis y convenciones de nombres en Python

En la convención ASCII más común, un identificador comienza con una letra o guion bajo y continúa con letras, dígitos o guiones bajos. La gramática léxica completa de Python es más amplia: acepta muchos caracteres Unicode de acuerdo con las reglas `XID_Start` y `XID_Continue`, y los identificadores distinguen mayúsculas de minúsculas. Consulta la [referencia léxica oficial](https://docs.python.org/es/3/reference/lexical_analysis.html#identificadores).

Este proyecto utiliza identificadores ASCII en inglés para favorecer la portabilidad, la búsqueda y la coherencia entre herramientas y documentación internacionales.

Válidos:

```python
customer_name = "Mina"
invoice2_total = 125
_internal_cache = {}
```

Inválidos:

```python
2nd_invoice = 125
customer-name = "Mina"
```

Las palabras reservadas de Python no pueden utilizarse como identificadores comunes:

```python
class = "premium"
```

Cuando un concepto externo entra en conflicto con una palabra reservada, un guion bajo final es una opción común:

```python
class_ = "premium"
```

### Convenciones de estilo comunes

| Tipo de nombre | Convención común | Ejemplo |
|---|---|---|
| Variable | `snake_case` | `invoice_total` |
| Función | `snake_case` | `calculate_invoice_total()` |
| Clase | `PascalCase` | `InvoiceCalculator` |
| Constante | `UPPER_SNAKE_CASE` | `MAX_RETRY_ATTEMPTS` |
| Nombre de uso interno | guion bajo inicial | `_load_cached_value()` |

Estas convenciones facilitan el reconocimiento, pero Python normalmente no las impone. Un proyecto puede añadir linters o verificaciones de estilo.

## 3. Revela intención, no solamente contenido

Los nombres débiles suelen describir el contenedor, no el concepto:

```python
data = ["Ana", "Diego", "Mina"]
value = 30
result = value * 60
```

Más claro:

```python
customer_names = ["Ana", "Diego", "Mina"]
duration_minutes = 30
duration_seconds = duration_minutes * 60
```

`data`, `value`, `item` y `result` no siempre son incorrectos. Se vuelven perjudiciales cuando el contexto cercano no deja evidente su significado.

Una pregunta útil al nombrar es:

> ¿Qué necesitaría saber una persona para utilizar este valor correctamente?

## 4. Incluye unidades y representación cuando importen

Un número sin unidad puede crear errores silenciosos:

```python
timeout = 30
total = 12_750
```

No se puede saber si `timeout` está en segundos o milisegundos, ni si `total` representa unidades monetarias o centavos.

Más claro:

```python
timeout_seconds = 30
invoice_total_cents = 12_750
```

Los detalles útiles de representación pueden incluir:

- `_seconds`, `_minutes` o `_milliseconds`;
- `_bytes` o `_megabytes`;
- `_cents` cuando se evita moneda en punto flotante;
- `_percentage` para valores de 0 a 100;
- `_rate` para valores fraccionarios como `0.15`;
- `_text`, `_path`, `_date` o `_datetime` cuando distintas formas podrían confundirse.

No agregues cada tipo a cada nombre. Agrega información que evite una confusión realista.

## 5. Nombra booleanos como preguntas o condiciones

Un nombre booleano debe hacer legibles `True` y `False`.

Débil:

```python
active = True
retry = False
```

Más claro:

```python
is_active = True
should_retry = False
```

Los prefijos comunes incluyen:

- `is_` para estado o clasificación;
- `has_` para posesión o presencia;
- `can_` para capacidad o permiso;
- `should_` para una decisión;
- `needs_` para una acción necesaria.

Ejemplo:

```python
RETRYABLE_STATUS_CODES = {502, 503, 504}

is_status_configured_for_retry = (
    response_status_code in RETRYABLE_STATUS_CODES
)
has_retry_attempts_remaining = attempt_number < MAX_RETRY_ATTEMPTS
should_retry_request = (
    is_status_configured_for_retry and has_retry_attempts_remaining
)
```

Evita nombres negativos cuando producen una doble negación:

```python
if not is_not_ready:
    ...
```

Prefiere un concepto positivo:

```python
if is_ready:
    ...
```

## 6. Colecciones y elementos individuales

Los nombres plurales ayudan a reconocer colecciones:

```python
customer_names = ["Ana", "Diego", "Mina"]

for customer_name in customer_names:
    print(customer_name)
```

Las formas plural y singular muestran la relación inmediatamente.

Para mapeos, nombra ambos lados cuando sea útil:

```python
country_code_by_name = {
    "Brazil": "BR",
    "Spain": "ES",
}
```

Otros patrones legibles incluyen:

```python
users_by_id = {}
price_by_product_code = {}
errors_by_file_path = {}
```

Nombres como `mapping`, `dictionary` y `list_data` revelan el tipo del contenedor, pero con frecuencia ocultan la relación del dominio.

## 7. Funciones, clases y constantes

### Las funciones normalmente describen acciones

Los nombres de funciones suelen comenzar con verbos:

```python
calculate_total()
load_configuration()
normalize_account_code()
is_supported_account()
```

El verbo debe corresponder al comportamiento. Una función llamada `get_report()` no debería eliminar archivos o enviar correos inesperadamente.

### Las clases normalmente describen entidades o responsabilidades

Los nombres de clases suelen utilizar sustantivos:

```python
Invoice
ReportGenerator
ValidationResult
```

Evita sufijos vacíos como `Manager`, `Helper` o `Processor` cuando no aclaran la responsabilidad. A veces esas palabras son correctas, pero no deberían convertirse en máquinas de niebla.

### Las constantes describen configuración o política estable

```python
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
SUPPORTED_FILE_EXTENSIONS = {".csv", ".json"}
```

Las mayúsculas comunican que el valor pretende permanecer estable por convención. No vuelven al objeto técnicamente inmutable.

## 8. El alcance determina cuánto detalle necesita un nombre

Un nombre corto puede ser claro dentro de un alcance local muy pequeño:

```python
for row in rows:
    print(row)
```

El mismo nombre puede ser demasiado vago en una función o módulo grande.

Un índice de bucle suele ser comprensible como `index` o incluso `i` en un bucle matemático muy pequeño:

```python
for i in range(3):
    print(i)
```

Un alcance mayor suele merecer más contexto:

```python
for retry_attempt_index in range(MAX_RETRY_ATTEMPTS):
    ...
```

Los nombres largos no son automáticamente buenos. Un nombre debe aportar suficiente información para su alcance sin convertirse en un párrafo vestido con guiones bajos.

## 9. Abreviaturas, siglas y vocabulario del proyecto

Utiliza una abreviatura cuando sea más conocida que su forma desarrollada o cuando el proyecto la haya definido claramente:

```python
url = "https://example.com"
user_id = 42
csv_file_path = "report.csv"
```

Evita acertijos privados:

```python
usr_cfg_tmp = {}
```

Un vocabulario coherente es más importante que encontrar un sinónimo nuevo en cada línea.

Confuso:

```python
customer_id = 42
client_name = "Ana"
consumer_status = "active"
```

Cuando esos nombres representan la misma entidad del dominio, elige un término:

```python
customer_id = 42
customer_name = "Ana"
customer_status = "active"
```

Un glosario del proyecto puede evitar la deriva de vocabulario en sistemas mayores.

## 10. Evita ocultar built-ins y nombres importantes

Python ofrece built-ins como `list`, `str`, `sum`, `id`, `input` y `type`.

Evita:

```python
list = ["Ana", "Diego"]
sum = 100
```

Después de esas asignaciones, llamar `list()` o `sum()` en el mismo alcance deja de referirse al built-in.

Prefiere:

```python
customer_names = ["Ana", "Diego"]
invoice_total = 100
```

También puede ocultarse un módulo o una función importada:

```python
import logging

logging = True
```

La asignación oculta el módulo importado. Elige un nombre distinto, como `is_logging_enabled`.

## 11. No codifiques información de tipo innecesaria

Nombres como estos suelen envejecer mal:

```python
customer_name_string = "Ana"
invoice_items_list = []
settings_dictionary = {}
```

Los type hints y las operaciones alrededor del valor ya comunican buena parte de su estructura:

```python
customer_name: str = "Ana"
invoice_items: list[str] = []
settings: dict[str, str] = {}
```

Incluye la representación en el nombre solamente cuando evite ambigüedad, como `invoice_total_cents` o `created_at_text`.

## 12. Las pequeñas abstracciones pueden revelar intención

Una expresión complicada puede recibir un nombre:

```python
is_priority_customer = (
    customer_status == "active"
    and annual_purchase_total >= 10_000
    and not has_overdue_invoice
)
```

Una operación reutilizable puede convertirse en una función:

```python
def is_priority_customer(
    customer_status,
    annual_purchase_total,
    has_overdue_invoice,
):
    return (
        customer_status == "active"
        and annual_purchase_total >= 10_000
        and not has_overdue_invoice
    )
```

El nombre crea un punto de apoyo conceptual. No debe ocultar complejidad arbitraria detrás de una etiqueta engañosa.

Los buenos nombres de abstracciones explican **qué** significa la operación. La implementación explica **cómo** funciona.

## 13. El código autoexplicativo no elimina la documentación

Los nombres claros reducen comentarios que solo traducen la sintaxis:

```python
# Check whether the account is supported.
if account_code in supported_account_codes:
    ...
```

El comentario aporta poco porque los nombres ya explican la condición.

Los comentarios siguen siendo útiles para motivos y restricciones:

```python
# Keep the legacy code for compatibility with exports created before 2024.
supported_account_codes.add("LEGACY")
```

Las docstrings siguen siendo útiles para contratos públicos, excepciones, efectos secundarios y expectativas de uso.

El código legible, los comentarios, las docstrings, los type hints, las pruebas y la documentación externa resuelven problemas diferentes.

## 14. Renombrar de forma segura

Renombrar es una refactorización: el comportamiento debe permanecer igual mientras el código se vuelve más fácil de comprender.

Un flujo seguro es:

1. identificar el concepto representado por el nombre;
2. buscar todas las referencias;
3. utilizar herramientas de refactorización del editor cuando estén disponibles;
4. actualizar pruebas, ejemplos, docstrings y documentación;
5. ejecutar las verificaciones del proyecto;
6. revisar la compatibilidad pública.

Renombrar una variable local suele tener poco riesgo. Renombrar una función pública, clase, módulo, opción de línea de comandos, clave de configuración, campo de base de datos o atributo serializado puede romper a quienes lo utilizan.

Los cambios públicos de nombre pueden requerir:

- un período de deprecación;
- un alias;
- instrucciones de migración;
- una versión de lanzamiento;
- coordinación con sistemas externos.

## 15. Ejemplos en este repositorio

| Archivo | Finalidad |
|---|---|
| [`vague_and_clear_names.py`](examples/vague_and_clear_names.py) | Compara identificadores vagos con nombres que comunican la intención del cálculo |
| [`booleans_and_units.py`](examples/booleans_and_units.py) | Demuestra booleanos, unidades, colecciones y constantes |
| [`refactor_for_intent.py`](examples/refactor_for_intent.py) | Muestra pequeñas operaciones nombradas que revelan un flujo |

Ejecuta un ejemplo desde la raíz del repositorio:

```bash
python comments-and-documentation/03-meaningful-names/examples/vague_and_clear_names.py
```

En sistemas donde el comando se llama `python3`:

```bash
python3 comments-and-documentation/03-meaningful-names/examples/vague_and_clear_names.py
```

## 16. Ejemplo práctico

Antes:

```python
def f(p, d):
    t = sum(p)
    return t - (t * d)
```

Después:

```python
def calculate_discounted_total(
    prices: list[float],
    discount_rate: float,
) -> float:
    subtotal = sum(prices)
    discount_amount = subtotal * discount_rate
    return subtotal - discount_amount
```

La segunda versión comunica:

- la acción de la función;
- qué contiene la colección;
- que el descuento es una tasa fraccionaria;
- qué representan los valores intermedios;
- el significado del valor devuelto.

Consulta la comparación completa en [`examples/vague_and_clear_names.py`](examples/vague_and_clear_names.py).

## 17. Errores comunes

### Elegir un nombre largo sin agregar significado

```python
the_value_that_we_are_currently_using = 10
```

Largo no significa preciso. Prefiere el concepto del dominio:

```python
retry_delay_seconds = 10
```

### Utilizar un nombre para varios significados

Reutilizar `result` para pasos no relacionados dificulta la depuración y la revisión.

### Nombrar por la implementación en lugar de la responsabilidad

`json_dictionary` puede quedar obsoleto si la implementación cambia. `report_payload` puede describir mejor su función.

### Utilizar verbos engañosos

Una función llamada `check_permissions()` que modifica permisos viola las expectativas de quien lee.

### Mezclar singular y plural

```python
customer = ["Ana", "Diego"]
```

Utiliza `customers` o `customer_names`.

### Ocultar un built-in

```python
type = "premium"
```

Utiliza `customer_type` u otro nombre específico del dominio.

### Mantener nombres obsoletos después de cambios de comportamiento

Una variable llamada `discount_percentage` es engañosa si el código ahora almacena `0.15` como tasa.

## 18. Ejercicio

Refactoriza este código sin cambiar su resultado:

```python
def p(x, y, z):
    a = x * y
    if z:
        a = a * 1.15
    return a
```

Supón que:

- `x` es una tarifa por hora en centavos;
- `y` es una cantidad de horas trabajadas;
- `z` indica si se aplica un adicional ficticio;
- `1.15` representa un multiplicador ficticio de adicional.

Una posible respuesta:

```python
PREMIUM_PAY_MULTIPLIER = 1.15


def calculate_pay_cents(
    hourly_rate_cents,
    worked_hours,
    has_premium_pay,
):
    base_pay_cents = hourly_rate_cents * worked_hours

    if has_premium_pay:
        return base_pay_cents * PREMIUM_PAY_MULTIPLIER

    return base_pay_cents
```

Preguntas de revisión:

1. ¿Cada nombre revela un concepto y no solamente un tipo?
2. ¿Las unidades son explícitas cuando podría haber confusión?
3. ¿El booleano se lee naturalmente dentro de una condición?
4. ¿La constante explica el número antes inexplicado?
5. ¿La refactorización conservó el comportamiento?

## 19. Lista de revisión de nombres

Antes de aceptar un nombre, pregunta:

- ¿Una persona puede explicar el concepto sin recorrer varias líneas?
- ¿El nombre distingue un elemento de una colección?
- ¿Las unidades o representaciones son explícitas cuando es necesario?
- ¿Un booleano se lee naturalmente como verdadero o falso?
- ¿El nombre de la función coincide con sus efectos?
- ¿Se utiliza el mismo término del dominio de forma coherente?
- ¿El nombre evita ocultar un built-in o una importación?
- ¿La cantidad de detalle es adecuada para el alcance?
- ¿Un cambio de comportamiento volvería falso al nombre?
- ¿La compatibilidad pública requiere un plan de migración?

## 20. Resumen de consulta rápida

| Situación | Prefiere |
|---|---|
| Variable o función | `snake_case` |
| Clase | `PascalCase` |
| Constante | `UPPER_SNAKE_CASE` |
| Estado booleano | `is_active`, `has_access`, `should_retry` |
| Colección | sustantivo plural como `customer_names` |
| Elemento individual | sustantivo singular como `customer_name` |
| Unidad numérica | `timeout_seconds`, `total_cents` |
| Relación de mapeo | `users_by_id`, `code_by_name` |
| Comportamiento de función | verbo claro como `calculate`, `load`, `normalize` |
| Conflicto con palabra reservada | guion bajo final como `class_` |
| Nombre built-in | alternativa específica del dominio |
| Condición compleja repetida | variable o función que revele intención |

## Conclusión

Los nombres significativos son documentación ejecutable entretejida directamente en el código. No sustituyen el diseño, los comentarios, las docstrings, las pruebas o las guías, pero hacen que todas esas herramientas sean más fáciles de utilizar.

Elige nombres que sigan siendo verdaderos, revelen el vocabulario del programa y reduzcan la cantidad de suposiciones que debe hacer quien lee.

[← Capítulo anterior: Docstrings](../02-docstrings/README.es.md) · [Volver al índice de la sección](../README.es.md) · Próximo capítulo: Marcadores de tareas
