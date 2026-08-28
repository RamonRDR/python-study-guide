# Trabajar con Fechas y Cálculos de Tiempo Usando `datetime`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

El módulo `datetime` de Python proporciona objetos explícitos para fechas, horas, valores combinados de fecha y hora, duraciones, desplazamientos fijos respecto de UTC, parsing, formato, comparación y aritmética.

Strings como `"2026-08-27"` son útiles para almacenamiento y comunicación, pero no saben automáticamente cuántos días separan dos fechas, si un año es bisiesto o cómo sumar una duración correctamente. El módulo `datetime` da tipos y reglas propios a esos conceptos.

Para la mayor parte del trabajo principiante e intermedio, los imports centrales son:

```python
from datetime import date, datetime, time, timedelta, timezone
```

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- distinguir `date`, `time`, `datetime` y `timedelta`;
- construir objetos de fecha y hora explícitamente;
- inspeccionar componentes de año, mes, día, hora, minuto y segundo;
- usar `date.today()` y `datetime.now()` deliberadamente;
- hacer aritmética con `timedelta`;
- entender la diferencia entre `timedelta.seconds` y `timedelta.total_seconds()`;
- hacer parsing con `strptime()` y formato con `strftime()`;
- usar helpers ISO como `fromisoformat()` e `isoformat()`;
- distinguir objetos `datetime` naive y timezone-aware;
- representar UTC y offsets fijos con `timezone`;
- convertir datetimes aware con `astimezone()`;
- entender por qué asignar `tzinfo` no equivale a convertir una hora;
- evitar tratar duraciones fijas como reglas de meses del calendario;
- reconocer cuándo las zonas horarias reales requieren el módulo complementario `zoneinfo`.

## 1. ¿Por qué usar tipos dedicados para fecha y hora?

Considera dos strings:

```python
start = "2026-08-27"
end = "2026-09-03"
```

Una persona ve que parecen fechas, pero Python todavía ve strings comunes.

Con `date`, el significado queda explícito:

```python
from datetime import date

start = date(2026, 8, 27)
end = date(2026, 9, 3)

print(end - start)
```

La resta produce un `timedelta`, porque Python ahora sabe que los valores representan fechas de calendario.

La idea de diseño es:

```text
texto para representación
        !=
objetos para comportamiento de fecha/hora
```

## 2. Las clases centrales

Las clases más usadas son:

| Clase | Representa |
|---|---|
| `date` | fecha de calendario: año, mes y día |
| `time` | hora de reloj sin una fecha |
| `datetime` | fecha y hora juntas |
| `timedelta` | duración entre puntos en el tiempo |
| `timezone` | offset fijo respecto de UTC |

Resuelven problemas relacionados, pero no son intercambiables.

## 3. Crear un `date`

Construye una fecha con año, mes y día:

```python
from datetime import date

release_date = date(2026, 8, 27)

print(release_date.year)
print(release_date.month)
print(release_date.day)
```

Valores imposibles fallan inmediatamente:

```python
from datetime import date

try:
    impossible = date(2026, 2, 30)
except ValueError:
    print("Invalid calendar date")
```

Esta validación es una ventaja de usar un tipo de fecha en lugar de transportar texto sin validar por el programa.

## 4. Crear un `time`

Un `time` representa una hora de reloj:

```python
from datetime import time

meeting_time = time(14, 30, 15)

print(meeting_time.hour)
print(meeting_time.minute)
print(meeting_time.second)
```

Un objeto `time` no contiene año, mes ni día. Es útil cuando la hora importa independientemente de la fecha.

No esperes sumar un `timedelta` directamente a un `time` simple. La aritmética de horas normalmente necesita un `datetime` o reglas de la aplicación sobre qué fecha usar.

## 5. Crear un `datetime`

Un `datetime` combina ambos conceptos:

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 14, 30, 15)

print(moment.date())
print(moment.time())
print(moment.year)
print(moment.hour)
```

Esto es útil para eventos, timestamps, plazos, logs, citas y otros valores donde importan fecha y hora.

## 6. Fecha y hora actuales

`date.today()` devuelve la fecha local actual:

```python
from datetime import date

today = date.today()
print(today)
```

`datetime.now()` devuelve la fecha y hora locales actuales como `datetime` naive por defecto:

```python
from datetime import datetime

now = datetime.now()
print(now)
```

Para un `datetime` UTC aware, prefiere:

```python
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc)
```

Evita llamadas al reloj real cuando una prueba o ejemplo determinista pueda usar un valor fijo.

### Evita `datetime.utcnow()` en código nuevo

`datetime.utcnow()` devuelve un objeto naive aunque represente UTC y está deprecated en Python moderno. Prefiere `datetime.now(timezone.utc)` para que la relación con UTC quede explícita en el propio objeto.

## 7. ¿Qué es un `timedelta`?

Un `timedelta` representa una duración.

```python
from datetime import timedelta

review_window = timedelta(days=7, hours=3)
print(review_window)
```

Puede sumarse o restarse de fechas y datetimes:

```python
from datetime import date, timedelta

start = date(2026, 8, 27)
end = start + timedelta(days=10)

print(end)
```

Restar fechas o datetimes compatibles produce un `timedelta`:

```python
from datetime import date

start = date(2026, 8, 27)
end = date(2026, 9, 3)

difference = end - start
print(difference.days)
```

## 8. `timedelta.seconds` no son los segundos totales

Este es un error clásico.

```python
from datetime import timedelta

duration = timedelta(days=1, seconds=90)

print(duration.days)
print(duration.seconds)
print(duration.total_seconds())
```

`duration.seconds` es solo la parte normalizada de segundos dentro del día. No incluye días completos.

Usa `total_seconds()` cuando necesites la duración completa expresada en segundos.

En el ejemplo anterior:

```text
componente de segundos = 90
duración total = 86490 segundos
```

## 9. Las duraciones no son meses de calendario

Un `timedelta` modela duraciones fijas en días, segundos y microsegundos. No tiene un concepto incorporado de "un mes de calendario".

Esto:

```python
from datetime import date, timedelta

start = date(2026, 1, 31)
approximate = start + timedelta(days=30)

print(approximate)
```

significa exactamente "sumar 30 días". No significa "moverse al mismo día del mes siguiente".

Reglas de cierre de mes, feriados, calendarios comerciales y vencimientos son políticas de la aplicación y deben modelarse explícitamente.

## 10. Comparar fechas y datetimes

Objetos compatibles del mismo tipo pueden compararse:

```python
from datetime import date

deadline = date(2026, 9, 10)
today = date(2026, 9, 3)

if today <= deadline:
    print("Still on time")
```

No compares strings formateados solo porque parecen fechas. Algunos formatos ordenan cronológicamente y otros no, y comparar strings no aporta semántica de calendario.

## 11. Hacer parsing con `strptime()`

Los datos externos suelen llegar como texto.

Usa `datetime.strptime()` cuando la entrada siga un formato conocido:

```python
from datetime import datetime

text = "27/08/2026 18:45"
moment = datetime.strptime(text, "%d/%m/%Y %H:%M")

print(moment)
```

La string de formato es un contrato entre tu código y la entrada.

Directivas comunes:

| Directiva | Significado |
|---|---|
| `%Y` | año de cuatro dígitos |
| `%m` | número de mes |
| `%d` | día del mes |
| `%H` | hora de 00 a 23 |
| `%M` | minuto |
| `%S` | segundo |
| `%f` | microsegundos |
| `%z` | offset UTC |

Si el texto no coincide con el formato esperado, el parsing genera `ValueError`.

```python
from datetime import datetime

try:
    moment = datetime.strptime("2026/08/27", "%Y-%m-%d")
except ValueError:
    print("Unexpected date format")
```

## 12. Formatear con `strftime()`

`strftime()` hace el camino contrario: objeto a texto.

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 18, 45)

print(moment.strftime("%Y-%m-%d"))
print(moment.strftime("%d/%m/%Y %H:%M"))
```

Mantén clara la diferencia:

```text
strptime: texto -> datetime
strftime: datetime/date/time -> texto
```

## 13. Helpers orientados a ISO

Para representaciones de estilo ISO, los métodos dedicados suelen ser más claros que formatos personalizados.

```python
from datetime import date, datetime

calendar_date = date.fromisoformat("2026-08-27")
moment = datetime.fromisoformat("2026-08-27T18:45:00+00:00")

print(calendar_date.isoformat())
print(moment.isoformat())
```

`fromisoformat()` e `isoformat()` son convenientes cuando el contrato coincide con las formas compatibles con el parser y formateador orientados a ISO de Python.

No asumas que toda string descrita informalmente como "ISO 8601" será aceptada por cualquier parser. La forma exacta admitida forma parte del contrato de interfaz.

## 14. Controlar la precisión de salida ISO

`datetime.isoformat()` puede controlar la precisión mostrada:

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 18, 45, 12, 345678)

print(moment.isoformat(timespec="minutes"))
print(moment.isoformat(timespec="seconds"))
print(moment.isoformat(timespec="microseconds"))
```

Esto es útil cuando un formato externo exige una precisión específica.

## 15. Datetimes naive y aware

Un `datetime` puede ser **naive** o **aware**.

Un datetime naive no contiene suficiente información de zona horaria para ubicarse de forma inequívoca frente a otros instantes del mundo.

```python
from datetime import datetime

naive = datetime(2026, 8, 27, 18, 30)
print(naive.tzinfo)
```

Un datetime aware posee información de timezone capaz de proporcionar un offset respecto de UTC:

```python
from datetime import datetime, timezone

aware = datetime(2026, 8, 27, 18, 30, tzinfo=timezone.utc)
print(aware.tzinfo)
print(aware.utcoffset())
```

La diferencia importa en APIs, logs, sistemas distribuidos y tareas programadas que cruzan zonas horarias.

## 16. Representar UTC

Usa `timezone.utc` para UTC:

```python
from datetime import datetime, timezone

moment = datetime(2026, 8, 27, 21, 30, tzinfo=timezone.utc)

print(moment.isoformat())
```

El resultado incluye el offset UTC:

```text
2026-08-27T21:30:00+00:00
```

## 17. Offsets UTC fijos

`timezone` puede representar offsets fijos:

```python
from datetime import datetime, timedelta, timezone

brt = timezone(timedelta(hours=-3))
moment = datetime(2026, 8, 27, 18, 30, tzinfo=brt)

print(moment.isoformat())
```

Un offset fijo como `-03:00` no equivale a una zona geográfica real. Las zonas geográficas pueden cambiar de offset por reglas históricas, horario de verano y cambios legales.

## 18. Convertir con `astimezone()`

Para un datetime aware, usa `astimezone()` para representar el mismo instante en otra zona:

```python
from datetime import datetime, timedelta, timezone

brt = timezone(timedelta(hours=-3))
local = datetime(2026, 8, 27, 18, 30, tzinfo=brt)
utc = local.astimezone(timezone.utc)

print(local.isoformat())
print(utc.isoformat())
```

La hora de reloj cambia, pero ambos objetos representan el mismo instante.

## 19. Asignar `tzinfo` no es convertir timezone

Este código cambia metadatos sin convertir la lectura del reloj:

```python
from datetime import datetime, timezone

naive = datetime(2026, 8, 27, 18, 30)
labeled = naive.replace(tzinfo=timezone.utc)

print(labeled.isoformat())
```

`replace(tzinfo=...)` no pregunta "¿qué hora es 18:30 en otra zona?". Crea un nuevo objeto con campos reemplazados.

Úsalo solo cuando ya sepas qué timezone representa el valor naive y adjuntar esa información sea la operación deseada.

Para convertir un datetime ya aware entre zonas, usa `astimezone()`.

## 20. No mezcles aritmética naive y aware sin una política

Restar un datetime aware de uno naive no tiene significado sin una relación explícita de timezone.

```python
from datetime import datetime, timezone

naive = datetime(2026, 8, 27, 18, 30)
aware = datetime(2026, 8, 27, 18, 30, tzinfo=timezone.utc)

try:
    difference = aware - naive
except TypeError:
    print("Cannot mix naive and aware datetimes")
```

Elige y documenta una política de timezone en las fronteras del sistema.

## 21. Zonas geográficas reales y `zoneinfo`

La biblioteca estándar incluye el módulo complementario `zoneinfo` para reglas IANA como `America/Sao_Paulo` o `Europe/London`.

Conceptualmente:

```python
from datetime import datetime
from zoneinfo import ZoneInfo

moment = datetime(2026, 8, 27, 18, 30, tzinfo=ZoneInfo("America/Sao_Paulo"))
print(moment.isoformat())
```

A diferencia de `timezone(timedelta(...))`, `ZoneInfo` puede modelar reglas históricas y futuras proporcionadas por la base de datos de zonas disponible.

La disponibilidad de esa base depende del entorno. Algunos sistemas la incluyen directamente; otros pueden necesitar el paquete `tzdata`. Por eso los ejemplos ejecutables de este capítulo usan offsets fijos.

## 22. Unix timestamps

Un Unix timestamp representa segundos transcurridos desde la convención de epoch Unix de la plataforma.

Crea un datetime UTC aware proporcionando timezone:

```python
from datetime import datetime, timezone

moment = datetime.fromtimestamp(0, tz=timezone.utc)
print(moment.isoformat())
```

Convierte un datetime aware de vuelta con `.timestamp()`:

```python
from datetime import datetime, timezone

moment = datetime(1970, 1, 1, tzinfo=timezone.utc)
print(moment.timestamp())
```

Los timestamps son útiles como valores de intercambio, pero legibilidad, rango soportado, precisión y comportamiento de plataforma siguen importando. No los uses como sustitutos de comprender y definir una política de timezone.

## 23. Reemplazar campos

`replace()` devuelve un nuevo objeto con campos seleccionados modificados:

```python
from datetime import datetime

original = datetime(2026, 8, 27, 18, 30)
updated = original.replace(hour=9, minute=0)

print(original)
print(updated)
```

No modifica el objeto original.

Esto es reemplazo de campos, no aritmética de calendario comercial. Cambiar `month=2` en una fecha cuyo día no existe en febrero puede generar `ValueError`.

## 24. Combinar una fecha y una hora

`datetime.combine()` es útil cuando valores separados deben convertirse en un solo datetime:

```python
from datetime import date, datetime, time

calendar_date = date(2026, 8, 27)
clock_time = time(18, 30)
moment = datetime.combine(calendar_date, clock_time)

print(moment)
```

El resultado es naive salvo que la información de timezone se aporte mediante un diseño explícito.

## 25. Errores comunes

### Error 1: guardar todo como strings

Los strings son apropiados en las fronteras, pero los cálculos normalmente deben usar objetos de fecha/hora.

### Error 2: tratar `timedelta.seconds` como la duración completa

Usa `total_seconds()` cuando necesites incluir también los días.

### Error 3: usar `timedelta(days=30)` como "un mes"

Eso significa 30 días, no un mes de calendario.

### Error 4: hacer parsing sin contrato explícito

Si la entrada tiene un formato definido, codifícalo deliberadamente y maneja `ValueError` cuando pueda ser inválida.

### Error 5: mezclar datetimes naive y aware

Define si tu sistema usa hora local, UTC o zonas explícitas en cada frontera.

### Error 6: usar `replace(tzinfo=...)` como conversión

Reemplazo de campo y conversión de timezone son operaciones distintas.

### Error 7: usar un offset fijo como si fuera una zona geográfica

Las reglas reales pueden cambiar. Usa `zoneinfo` cuando importen las reglas geográficas.

### Error 8: usar el reloj real en pruebas deterministas

Inyecta o construye datetimes fijos cuando importe la reproducibilidad.

## 26. Ejemplo práctico

Imagina un informe que recibe un timestamp UTC como texto, lo parsea, aplica un offset local fijo para presentación y calcula un plazo de revisión.

```python
from datetime import datetime, timedelta, timezone

source = "2026-08-27T21:30:00+00:00"
created_utc = datetime.fromisoformat(source)

local_zone = timezone(timedelta(hours=-3))
created_local = created_utc.astimezone(local_zone)
deadline = created_local + timedelta(days=5)

print(created_local.isoformat())
print(deadline.isoformat())
```

El flujo queda explícito:

```text
contrato de texto
    ↓
datetime aware
    ↓
conversión de timezone
    ↓
aritmética de duración
    ↓
salida formateada
```

## 27. Ejercicio

Crea un programa que:

1. haga parsing de `"2026-10-15 09:30"` usando `strptime()`;
2. trate ese valor como hora de pared con offset fijo `-03:00`;
3. sume 2 días y 4 horas con `timedelta`;
4. convierta el resultado a UTC con `astimezone()`;
5. muestre los valores local y UTC con `isoformat()`;
6. muestre la duración completa en segundos;
7. formatee el resultado UTC como `YYYY-MM-DD HH:MM`.

Después responde:

- ¿Qué objetos son naive y cuáles son aware?
- ¿Por qué `replace(tzinfo=...)` es aceptable para adjuntar aquí el offset conocido del origen, pero no para convertir entre zonas?
- ¿Por qué debe usarse `total_seconds()` en vez de `.seconds` para la duración completa?
- ¿Por qué un offset fijo `-03:00` no equivale automáticamente a todas las reglas históricas o futuras de `America/Sao_Paulo`?

## 28. Lista de revisión

Antes de avanzar, asegúrate de poder explicar:

- `date`, `time`, `datetime`, `timedelta` y `timezone`;
- construcción y validación de valores de calendario;
- `date.today()` y `datetime.now()`;
- por qué UTC aware debe usar `datetime.now(timezone.utc)`;
- aritmética de fechas y datetimes;
- `.days`, `.seconds` y `.total_seconds()`;
- por qué las duraciones fijas no son meses de calendario;
- `strptime()` frente a `strftime()`;
- `fromisoformat()` e `isoformat()`;
- datetimes naive frente a aware;
- UTC y offsets fijos;
- `astimezone()` frente a `replace(tzinfo=...)`;
- por qué las reglas de zonas geográficas pertenecen a `zoneinfo`;
- timestamps como valores de intercambio;
- cómo mantener pruebas deterministas.

## Referencia rápida

```python
from datetime import date, datetime, time, timedelta, timezone

calendar_date = date(2026, 8, 27)
clock_time = time(18, 30)
moment = datetime(2026, 8, 27, 18, 30)
duration = timedelta(days=2, hours=4)

calendar_date + timedelta(days=1)
moment + duration

datetime.strptime("2026-08-27 18:30", "%Y-%m-%d %H:%M")
moment.strftime("%d/%m/%Y %H:%M")

date.fromisoformat("2026-08-27")
datetime.fromisoformat("2026-08-27T18:30:00+00:00")
moment.isoformat()

aware_utc = datetime(2026, 8, 27, 21, 30, tzinfo=timezone.utc)
fixed_offset = timezone(timedelta(hours=-3))
aware_utc.astimezone(fixed_offset)

duration.total_seconds()
```

## Ejemplos ejecutables

- [`examples/date_arithmetic.py`](examples/date_arithmetic.py)
- [`examples/parse_and_format.py`](examples/parse_and_format.py)
- [`examples/utc_conversion.py`](examples/utc_conversion.py)
- [`examples/duration_seconds.py`](examples/duration_seconds.py)

Los ejemplos son deterministas y no dependen del reloj actual ni de una base externa de zonas horarias.

## Próximo capítulo

Continúa con el [**Capítulo 03: Controlando Contratos de Serialización y Decodificación JSON**](../03-json/README.es.md), donde la biblioteca estándar revisita JSON con control más profundo de rigor, hooks numéricos, representaciones personalizadas, nombres duplicados y salida determinista.

## Referencias oficiales

- [Python 3.14 `datetime` - tipos básicos de fecha y hora](https://docs.python.org/3.14/library/datetime.html)
- [Python 3.14 códigos de formato de `strftime()` y `strptime()`](https://docs.python.org/3.14/library/datetime.html#strftime-and-strptime-format-codes)
- [Python 3.14 `zoneinfo` - soporte para zonas IANA](https://docs.python.org/3.14/library/zoneinfo.html)
