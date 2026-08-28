<div align="center">

# Diseñando Contratos de Precisión y Redondeo Decimal

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Biblioteca Estándar](../README.es.md) · [← Anterior: `itertools`](../07-itertools/README.es.md)

El `float` integrado de Python es la herramienta correcta para una gran cantidad de trabajo numérico, pero modela números con punto flotante binario. El Capítulo 03 de Strings y Números ya mostró por qué un valor como `0.1` puede no tener una representación binaria exacta.

El módulo `decimal` resuelve un problema diferente. Proporciona aritmética decimal de punto flotante con control explícito sobre representación, precisión, redondeo, condiciones excepcionales y validación.

Este capítulo no trata de reemplazar cada `float` por `Decimal`. Trata de elegir deliberadamente un contrato numérico cuando los propios dígitos decimales forman parte del significado de los datos.

**Tiempo estimado de estudio:** 180–240 minutos.

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- explicar qué resuelve `Decimal` y qué no resuelve;
- construir valores decimales sin importar accidentalmente aproximación de punto flotante binario;
- distinguir representación decimal exacta de aritmética con precisión ilimitada;
- explicar signo, dígitos del coeficiente, exponente y conservación de ceros finales;
- inspeccionar representación con `as_tuple()` y distinguir igualdad de valor de ordenación por representación;
- explicar por qué la precisión del contexto cuenta dígitos significativos y no posiciones decimales;
- inspeccionar y reemplazar temporalmente el contexto aritmético activo;
- elegir reglas de redondeo explícitamente en lugar de depender de un valor predeterminado accidental;
- usar `quantize()` para imponer un exponente objetivo o una escala decimal fija;
- distinguir las señales `Rounded` e `Inexact`;
- usar flags para monitorización y traps para imponer reglas;
- validar una escala decimal atrapando `Inexact`;
- manejar `Infinity`, `NaN`, NaN señalizante y cero con signo deliberadamente;
- reconocer cuándo la aritmética entre `Decimal` y `float` se rechaza intencionalmente;
- usar `FloatOperation` para detectar rutas de conversión implícita desde float;
- explicar el propósito de `BasicContext`, `ExtendedContext` y objetos `Context` explícitos;
- usar `fma()` cuando una sola etapa de redondeo importa más que redondear un producto intermedio;
- elegir fronteras seguras para JSON, texto, bases de datos, APIs y entrada del usuario;
- reconocer trade-offs de rendimiento, interoperabilidad y mantenimiento;
- probar políticas decimales como comportamiento y no solo como salida formateada.

## 1. El problema no es que `float` esté roto

El punto flotante binario es un modelo de representación deliberado. Es rápido, ampliamente soportado por hardware y apropiado para cargas científicas, gráficas, estadísticas y muchos usos numéricos generales.

La incompatibilidad aparece cuando la **representación decimal en sí forma parte del contrato**.

```python
print(0.1 + 0.1 + 0.1 == 0.3)
```

```text
False
```

Ese resultado proviene del error de representación binaria, no de que Python haya olvidado aritmética.

## 2. `Decimal` usa representación decimal

```python
from decimal import Decimal


result = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")
print(result)
print(result == Decimal("0.3"))
```

```text
0.3
True
```

Las cadenas decimales pueden representarse exactamente como números decimales.

## 3. Representación exacta no significa que todo resultado sea exacto para siempre

Una distinción crucial:

```text
exact decimal input
        ↓
Decimal representation
        ↓
arithmetic under a finite context precision
        ↓
possibly rounded result
```

Por ejemplo, `1 / 7` tiene una expansión decimal infinita.

```python
from decimal import Decimal, localcontext


with localcontext(prec=8):
    print(Decimal(1) / Decimal(7))
```

```text
0.14285714
```

`Decimal` elimina el error de representación binaria para entradas decimales. No hace desaparecer la precisión finita.

## 4. Importa los nombres que tu código realmente usa

Para ejemplos didácticos, los imports explícitos mantienen visibles las dependencias:

```python
from decimal import Decimal, ROUND_HALF_EVEN
```

El módulo expone muchos contextos, señales y constantes de redondeo. Evita `from decimal import *` en código de aplicación normal cuando nombres explícitos hacen la política numérica más fácil de auditar.

## 5. Prefiere strings cuando el valor de origen es texto decimal

```python
from decimal import Decimal


price = Decimal("19.90")
rate = Decimal("0.075")

print(price)
print(rate)
```

Un constructor desde string expresa directamente los dígitos decimales.

## 6. Los enteros se convierten exactamente

```python
from decimal import Decimal


quantity = Decimal(7)
print(quantity)
```

```text
7
```

La conversión de entero a Decimal es exacta.

## 7. Pasar un `float` conserva exactamente el valor binario del float

Esta es una de las fronteras más importantes del módulo:

```python
from decimal import Decimal


print(Decimal(0.1))
```

El resultado contiene muchos dígitos porque Python convierte el `float` binario ya existente **exactamente** a su equivalente decimal.

Eso es diferente de:

```python
from decimal import Decimal


print(Decimal("0.1"))
```

La segunda forma representa directamente el valor decimal un décimo.

## 8. `Decimal.from_float()` hace explícita esa frontera

```python
from decimal import Decimal


converted = Decimal.from_float(0.1)
print(converted)
```

Úsalo cuando conservar exactamente el valor de un `float` existente sea la intención real.

No es un atajo para recuperar texto decimal que existía antes de crear el float.

## 9. `Decimal.from_number()` es una incorporación de Python 3.14

Python 3.14 añade un constructor alternativo que acepta `int`, `float` o `Decimal`, pero no strings ni tuplas:

```python
from decimal import Decimal


value = Decimal.from_number(314)
print(value)
```

Cuando importa la compatibilidad con versiones anteriores a Python 3.14, usa los constructores más antiguos apropiados para el tipo de origen.

## 10. Decide dónde comienza el contrato decimal

Una frontera robusta suele verse así:

```text
text / database decimal / validated API text
                    ↓
              Decimal(...)
                    ↓
          Decimal-only calculation
                    ↓
      explicit rounding / quantization
                    ↓
         output or persistence boundary
```

Convertir a `Decimal` solo después de varios cálculos en float binario no elimina aproximaciones ya introducidas antes.

## 11. `Decimal` y `float` generalmente no se mezclan en aritmética

```python
from decimal import Decimal


amount = Decimal("1.25")
# amount + 0.5  # TypeError
```

Este rechazo es útil. Evita que un pipeline mezcle silenciosamente dos modelos numéricos distintos.

Las comparaciones tienen reglas separadas, pero la aritmética normal debería mantenerse dentro de una representación numérica elegida deliberadamente.

## 12. Un Decimal tiene signo, dígitos de coeficiente y exponente

Conceptualmente:

```text
Decimal("12.340")

sign        = positive
coefficient = 1, 2, 3, 4, 0
exponent    = -3
```

El exponente describe la escala decimal respecto al coeficiente.

## 13. Los ceros finales pueden conservar significancia

```python
from decimal import Decimal


print(Decimal("1.20"))
print(Decimal("1.2000"))
```

```text
1.20
1.2000
```

Los valores son numéricamente iguales, pero sus representaciones almacenadas conservan información distinta de ceros finales.

## 14. Inspecciona la representación con `as_tuple()`

```python
from decimal import Decimal


value = Decimal("12.340")
print(value.as_tuple())
```

El resultado expone signo, dígitos del coeficiente y exponente como una named tuple.

## 15. La igualdad numérica ignora diferencias de representación

```python
from decimal import Decimal


print(Decimal("12.0") == Decimal("12.00"))
```

```text
True
```

Los números tienen el mismo valor numérico.

## 16. `compare_total()` puede distinguir representaciones

Cuando importa la representación en sí, `compare_total()` proporciona un orden total basado en la representación abstracta de Decimal:

```python
from decimal import Decimal


left = Decimal("12.0")
right = Decimal("12")
print(left.compare_total(right))
```

No uses comparación sensible a la representación cuando el requisito real sea igualdad numérica ordinaria.

## 17. Los objetos Decimal son inmutables

La aritmética crea nuevos valores en lugar de modificar objetos Decimal existentes.

```python
from decimal import Decimal


amount = Decimal("10.00")
updated = amount + Decimal("2.50")

print(amount)
print(updated)
```

```text
10.00
12.50
```

Este comportamiento encaja naturalmente con funciones, claves de diccionario, sets y cálculos repetibles.

## 18. La aritmética ocurre bajo un contexto

El contexto aritmético controla propiedades como:

- precisión;
- modo de redondeo;
- límites de exponente;
- flags de señales;
- habilitadores de traps.

Piensa en el contexto como la **política de ejecución numérica** que rodea las operaciones Decimal.

## 19. Inspecciona el contexto activo con `getcontext()`

```python
from decimal import getcontext


context = getcontext()
print(context.prec)
print(context.rounding)
```

La precisión predeterminada estándar es de 28 dígitos y el modo de redondeo predeterminado es `ROUND_HALF_EVEN`, salvo que el contexto activo se haya modificado.

## 20. Precisión significa dígitos significativos, no posiciones decimales

Esta distinción es esencial.

```python
from decimal import Decimal, localcontext


with localcontext(prec=4):
    print(Decimal("12345") + Decimal("1"))
    print(Decimal("1.2345") + Decimal("0"))
```

La precisión del contexto limita los dígitos significativos de los resultados aritméticos. No significa "mantener siempre cuatro dígitos después del punto decimal".

Usa `quantize()` cuando se requiera un exponente o escala fija.

## 21. Construir desde string no redondea a la precisión del contexto

```python
from decimal import Decimal, localcontext


with localcontext(prec=4):
    value = Decimal("3.1415926535")
    print(value)
```

El constructor conserva los dígitos suministrados por la string. La precisión del contexto se vuelve relevante cuando se realiza aritmética.

## 22. La aritmética aplica el contexto

```python
from decimal import Decimal, localcontext


with localcontext(prec=6):
    result = Decimal("3.1415926535") + Decimal("2.7182818285")
    print(result)
```

```text
5.85987
```

Los operandos exactos tienen más dígitos de los que permite la precisión del resultado, por lo que ocurre redondeo.

## 23. Evita cambiar casualmente la política aritmética global

Esto funciona:

```python
from decimal import getcontext


getcontext().prec = 50
```

Pero modificar el contexto activo dentro de código reutilizable de biblioteca puede sorprender a llamadores cuyos cálculos comparten ese contexto.

Prefiere un alcance local cuando la precisión o regla de redondeo pertenezca solo a una operación.

## 24. `localcontext()` delimita una política temporal

```python
from decimal import Decimal, getcontext, localcontext


original_precision = getcontext().prec

with localcontext(prec=8):
    result = Decimal(1) / Decimal(7)

print(result)
print(getcontext().prec == original_precision)
```

El contexto anterior se restaura después del bloque `with`.

Los argumentos nombrados para establecer atributos directamente en `localcontext()` están disponibles desde Python 3.11.

## 25. Objetos `Context` explícitos hacen portable la política

```python
from decimal import Context, Decimal, ROUND_HALF_UP


policy = Context(prec=12, rounding=ROUND_HALF_UP)
result = policy.divide(Decimal(1), Decimal(7))
print(result)
```

Un contexto explícito puede pasarse o reutilizarse como objeto de política en lugar de depender de estado ambiente.

## 26. `Context.create_decimal()` aplica el contexto durante la conversión

El constructor normal `Decimal` no reduce los dígitos de entrada según la precisión del contexto.

`Context.create_decimal()` es diferente: aplica precisión, redondeo, flags y traps del contexto durante la conversión.

```python
from decimal import Context, ROUND_DOWN


policy = Context(prec=5, rounding=ROUND_DOWN)
value = policy.create_decimal("3.1415926")
print(value)
```

```text
3.1415
```

Úsalo cuando normalizar la entrada forme intencionalmente parte de la política del contexto.

## 27. El redondeo es una regla de dominio o numérica, no decoración

El formato controla presentación. El redondeo cambia el valor numérico.

Son decisiones separadas:

```text
calculation precision
        ≠
quantization policy
        ≠
display formatting
```

Haz cada una explícita cuando la corrección dependa de ella.

## 28. `ROUND_HALF_EVEN` es el modo predeterminado del contexto

Half-even redondea al resultado más cercano y resuelve un empate exacto hacia el candidato cuyo último dígito conservado sea par.

```python
from decimal import Decimal, ROUND_HALF_EVEN


whole = Decimal("1")
print(Decimal("2.5").quantize(whole, rounding=ROUND_HALF_EVEN))
print(Decimal("3.5").quantize(whole, rounding=ROUND_HALF_EVEN))
```

```text
2
4
```

No describas esto como "redondear hacia abajo en .5". El desempate depende de cuál resultado vecino es par.

## 29. `ROUND_HALF_UP` resuelve empates alejándose de cero

```python
from decimal import Decimal, ROUND_HALF_UP


whole = Decimal("1")
print(Decimal("2.5").quantize(whole, rounding=ROUND_HALF_UP))
print(Decimal("-2.5").quantize(whole, rounding=ROUND_HALF_UP))
```

```text
3
-3
```

Elige un modo de redondeo porque el dominio lo requiere, no porque el nombre parezca familiar.

## 30. Los modos de redondeo direccionales tienen contratos distintos

El módulo también incluye:

```text
ROUND_CEILING  -> toward +Infinity
ROUND_FLOOR    -> toward -Infinity
ROUND_DOWN     -> toward zero
ROUND_UP       -> away from zero
ROUND_HALF_DOWN
ROUND_05UP
```

El comportamiento para números negativos es la razón por la cual "up" y "ceiling" no deben tratarse como sinónimos.

## 31. `quantize()` impone el exponente de otro Decimal

```python
from decimal import Decimal


value = Decimal("1.41421356")
rounded = value.quantize(Decimal("1.000"))
print(rounded)
```

```text
1.414
```

El operando derecho actúa como plantilla de exponente.

## 32. Usa un quantum con nombre para trabajo repetido de escala fija

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")
amount = Decimal("12.345")

print(amount.quantize(CENT, rounding=ROUND_HALF_UP))
```

```text
12.35
```

Un quantum con nombre hace visible y reutilizable el contrato de escala.

## 33. Cuantiza después de operaciones que pueden cambiar la escala

La multiplicación y división pueden producir más posiciones decimales de las que permite un dominio de escala fija.

```python
from decimal import Decimal, ROUND_HALF_EVEN


CENT = Decimal("0.01")
amount = Decimal("10.00")
rate = Decimal("0.0375")
raw_result = amount * rate
final_result = raw_result.quantize(CENT, rounding=ROUND_HALF_EVEN)

print(raw_result)
print(final_result)
```

El lugar correcto para cuantizar depende de la regla del dominio. No insertes redondeo automáticamente después de cada operación.

## 34. La cuantización también puede validar escala

Un validador de escala debe definir tanto la escala permitida como la magnitud soportada. `quantize()` puede señalar `InvalidOperation` cuando el coeficiente del resultado cuantizado excedería la precisión del contexto. El validador siguiente atrapa ambas condiciones y limita explícitamente los dígitos de coeficiente aceptados:

```python
from decimal import Context, Decimal, Inexact, InvalidOperation


TWO_PLACES = Decimal("0.01")
MAX_COEFFICIENT_DIGITS = 28
validator = Context(
    prec=MAX_COEFFICIENT_DIGITS,
    traps=[Inexact, InvalidOperation],
)

value = Decimal("3.21")

if not value.is_finite() or len(value.as_tuple().digits) > MAX_COEFFICIENT_DIGITS:
    raise ValueError("unsupported decimal value")

print(value.quantize(TWO_PLACES, context=validator))
```

Un valor como `Decimal("3.214")` genera `Inexact`. Los valores demasiado grandes o no finitos se rechazan antes de que puedan pasar como un `NaN` aceptado, mientras `InvalidOperation` también se atrapa como protección defensiva.

## 35. `quantize()` tiene una regla especial de Underflow

A diferencia de otras operaciones, `quantize()` nunca señala `Underflow`, incluso cuando el resultado es subnormal e inexacto.

Es un contrato avanzado, pero importa cuando la monitorización de señales forma parte de un diseño de validación o control numérico.

## 36. `round()` y el contexto Decimal interactúan de forma distinta según los argumentos

```python
from decimal import Decimal


value = Decimal("2.675")
print(round(value, 2))
```

Con un `ndigits` entero, el redondeo de Decimal respeta el modo de redondeo del contexto y equivale a cuantizar a la potencia de diez correspondiente.

En cambio, `round(decimal_value)` sin `ndigits` devuelve un `int`, resuelve empates hacia el par e ignora el modo de redondeo del contexto Decimal.

## 37. `to_integral_value()` redondea sin señalar `Inexact` ni `Rounded`

```python
from decimal import Decimal, ROUND_HALF_UP


value = Decimal("7.8")
print(value.to_integral_value(rounding=ROUND_HALF_UP))
```

Úsalo cuando necesites un resultado Decimal integral sin esas señales de redondeo.

## 38. `to_integral_exact()` informa condiciones de redondeo

```python
from decimal import Decimal, Inexact, Rounded, localcontext


with localcontext() as context:
    context.clear_flags()
    result = Decimal("7.8").to_integral_exact()
    print(result)
    print(context.flags[Rounded])
    print(context.flags[Inexact])
```

La variante `exact` es útil cuando quieres monitorizar si se descartó información.

## 39. Las señales forman parte del contrato Decimal

Las señales describen condiciones encontradas durante aritmética decimal.

Ejemplos importantes incluyen:

- `Clamped`;
- `DivisionByZero`;
- `InvalidOperation`;
- `Inexact`;
- `Rounded`;
- `Subnormal`;
- `Overflow`;
- `Underflow`;
- `FloatOperation`.

Una señal puede establecer una flag, lanzar mediante un trap o hacer ambas cosas en esa secuencia.

## 40. Las flags son sticky

Una vez que una flag de señal se vuelve verdadera, permanece marcada hasta que se limpia.

```python
from decimal import Decimal, Inexact, localcontext


with localcontext(prec=5) as context:
    context.clear_flags()
    Decimal(1) / Decimal(7)
    print(context.flags[Inexact])
```

```text
True
```

Limpia siempre las flags antes de un cálculo que pretendas monitorizar de forma independiente.

## 41. `Rounded` e `Inexact` no son la misma condición

`Rounded` significa que se descartaron dígitos.

`Inexact` significa que los dígitos descartados contenían información no nula, por lo que el resultado difiere del resultado matemático exacto.

Por ejemplo, reducir `5.00` a `5.0` puede señalar `Rounded` aunque no se haya perdido información no nula.

## 42. Los traps convierten señales seleccionadas en excepciones

```python
from decimal import Decimal, DivisionByZero, localcontext


with localcontext() as context:
    context.traps[DivisionByZero] = True
    # Decimal(1) / Decimal(0)  # raises DivisionByZero
```

Un trap es una regla de imposición. Una flag es un registro de observación.

## 43. Elige traps según el contrato

Políticas posibles incluyen:

```text
monitor and continue -> inspect flags
reject inexact input -> trap Inexact
reject divide by zero -> trap DivisionByZero
reject accidental float conversion -> trap FloatOperation
```

No habilites todos los traps solo porque las excepciones parezcan más seguras. La semántica deseada depende de la aplicación.

## 44. `FloatOperation` puede exponer fronteras implícitas con float

```python
from decimal import Decimal, FloatOperation, localcontext


with localcontext() as context:
    context.traps[FloatOperation] = True
    # Decimal(3.14)  # raises FloatOperation
```

La conversión explícita mediante `Decimal.from_float()` no señala `FloatOperation`, porque la intención de conversión ya es visible.

## 45. La comparación de igualdad con float tiene una excepción especial

La aritmética entre Decimal y float se rechaza en general, pero las reglas de comparación son más matizadas.

Cuando `FloatOperation` está atrapada, comparaciones de orden como `<` pueden lanzar, mientras las comparaciones de igualdad siguen permitidas.

No construyas un pipeline numérico alrededor de peculiaridades de comparación entre tipos. Normaliza deliberadamente las fronteras numéricas.

## 46. `BasicContext` es útil para depuración

`BasicContext` tiene precisión 9, usa `ROUND_HALF_UP` y habilita muchos traps.

Eso hace visibles rápidamente condiciones inesperadas durante depuración.

```python
from decimal import BasicContext


print(BasicContext.prec)
print(BasicContext.rounding)
```

## 47. `ExtendedContext` prefiere valores de resultado antes que excepciones

`ExtendedContext` tiene precisión 9, usa `ROUND_HALF_EVEN` y no tiene traps habilitados.

Una operación como división por cero puede, por tanto, producir `Infinity` mientras registra la señal en vez de lanzar inmediatamente.

Usa ese comportamiento solo cuando valores numéricos especiales formen parte intencional del algoritmo.

## 48. El contexto predeterminado no es lo mismo que `BasicContext`

El contexto predeterminado ordinario usa precisión 28 y `ROUND_HALF_EVEN`, con traps habilitados para `Overflow`, `InvalidOperation` y `DivisionByZero`.

No deduzcas el comportamiento predeterminado a partir de la configuración de los contextos estándar con nombre.

## 49. `IEEEContext()` es nuevo en Python 3.14

Python 3.14 añade `decimal.IEEEContext(bits)` para crear un contexto configurado para uno de los formatos de intercambio IEEE soportados.

```python
from decimal import IEEEContext


context = IEEEContext(128)
print(context.prec)
```

El código que debe funcionar en versiones anteriores no debería depender de esta API sin una estrategia de compatibilidad.

## 50. Decimal soporta valores especiales

```python
from decimal import Decimal


values = [
    Decimal("Infinity"),
    Decimal("-Infinity"),
    Decimal("NaN"),
    Decimal("sNaN"),
    Decimal("-0"),
]

for value in values:
    print(value)
```

Estos son valores aritméticos con semántica Decimal definida, no strings ordinarias de error.

## 51. Clasifica valores especiales antes del procesamiento normal cuando sea necesario

```python
from decimal import Decimal


value = Decimal("Infinity")
print(value.is_finite())
print(value.is_infinite())
print(value.is_nan())
```

Las fronteras de validación a menudo necesitan rechazar valores no finitos antes de persistencia o cálculos posteriores.

## 52. NaN no se comporta como un número ordinario

Un NaN representa un resultado numérico indefinido o no representable.

No dependas de lógica de ordenación normal para valores NaN. Detecta explícitamente con `is_nan()` cuando el dominio no los permite.

Los NaN señalizantes (`sNaN`) están diseñados para señalar `InvalidOperation` cuando se usan en la mayoría de operaciones.

## 53. El cero con signo puede conservar información direccional

Decimal distingue representaciones de cero positivo y negativo:

```python
from decimal import Decimal


positive_zero = Decimal("0")
negative_zero = Decimal("-0")

print(positive_zero == negative_zero)
print(negative_zero.is_signed())
```

Los valores comparan iguales numéricamente aunque la información de signo permanezca en la representación.

## 54. La precisión finita todavía puede causar pérdida de significancia

La aritmética Decimal puede redondear siempre que un resultado exceda la precisión del contexto.

```python
from decimal import Decimal, localcontext


with localcontext(prec=5):
    large = Decimal("10000")
    small = Decimal("0.12345")
    result = large + small
    print(result)
```

El modelo decimal evita error de representación binaria, pero una precisión baja aún puede descartar dígitos decimales significativos.

## 55. Aumentar la precisión puede formar parte de una estrategia numérica

Para cálculos intermedios puede ser apropiado usar más precisión de la que necesita la salida final y redondear solo en la frontera requerida.

```python
from decimal import Decimal, localcontext


with localcontext(prec=30):
    ratio = Decimal(1) / Decimal(7)

print(ratio)
```

La precisión de trabajo necesaria es propiedad del algoritmo y del dominio, no un número mágico universal.

## 56. `fma()` evita redondear el producto intermedio

Fused multiply-add calcula:

```text
self * other + third
```

sin redondear el resultado intermedio de la multiplicación.

```python
from decimal import Decimal


value = Decimal("2").fma(Decimal("3"), Decimal("5"))
print(value)
```

```text
11
```

Esto puede importar en fórmulas sensibles a precisión donde un redondeo intermedio alteraría el resultado final.

## 57. `normalize()` simplifica la representación conservando el valor

```python
from decimal import Decimal


print(Decimal("32.1000").normalize())
```

```text
32.1
```

Usa normalización cuando la significancia codificada por ceros finales no sea necesaria. No normalices automáticamente si la representación lleva significado de dominio.

## 58. El formato no sustituye a la cuantización

```python
from decimal import Decimal


value = Decimal("2.675")
print(f"{value:.2f}")
print(value)
```

Formatear produce texto para presentación. El objeto Decimal original sigue sin cambios.

Si cálculos posteriores requieren un valor a escala fija, crea ese valor numérico explícitamente con la política de redondeo requerida.

## 59. Analiza números decimales JSON deliberadamente

El capítulo anterior de JSON introdujo esta frontera:

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

`parse_float=Decimal` permite que el decoder construya un Decimal desde la forma textual del número JSON en vez de convertir primero a `float` de Python.

## 60. La codificación JSON necesita su propia política explícita

El encoder estándar de `json` no serializa automáticamente objetos `Decimal` arbitrarios como números JSON.

Diseños posibles incluyen:

- convertir a string cuando el esquema externo define una string;
- usar una representación entera de unidades menores cuando ese esquema sea apropiado;
- implementar una frontera de encoding personalizada y deliberada;
- usar otra tecnología de serialización con un tipo decimal nativo.

No conviertas silenciosamente un Decimal a float solo para facilitar la serialización cuando importan las semánticas decimales exactas.

## 61. Conserva texto decimal en las fronteras de entrada

Supongamos que un formulario proporciona:

```text
19.90
```

Prefiere:

```python
from decimal import Decimal


raw_value = "19.90"
amount = Decimal(raw_value)
```

antes que convertir el texto a float primero y luego a Decimal.

## 62. Las fronteras de base de datos deben respetar el tipo numérico de la base

Cuando un driver de base de datos expone una columna numeric o decimal exacta como `Decimal`, mantener ese valor como Decimal evita un viaje innecesario por float.

El comportamiento varía entre drivers, así que inspecciona el contrato real del adaptador en vez de asumir que cada columna numérica llega con el mismo tipo de Python.

## 63. Los contratos de API deben declarar la representación

"Número" suele ser demasiado ambiguo para datos sensibles a precisión.

Preguntas útiles de contrato incluyen:

- ¿El valor es texto de número JSON o texto dentro de string JSON?
- ¿Cuántas posiciones decimales se permiten?
- ¿Qué modo de redondeo se aplica?
- ¿Los ceros finales tienen significado?
- ¿Se permiten valores no finitos?
- ¿Quién realiza la cuantización final?

La corrección numérica empieza en la frontera, no en la expresión aritmética final.

## 64. Mantén la política de redondeo cerca de la regla de dominio

Un helper puede hacer explícita la política:

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")


def to_cents(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)
```

El nombre del helper y sus pruebas deberían explicar por qué ese modo de redondeo es correcto para el dominio que lo usa.

## 65. Evita mutación oculta del contexto dentro de helpers

Un helper arriesgado cambia estado ambiente:

```python
from decimal import getcontext


def calculate_something():
    getcontext().prec = 6
    # calculation continues
```

Un diseño más seguro:

- usa `localcontext()`;
- acepta un `Context` explícito;
- documenta que mutar el contexto forma parte de la API pública.

La política local es más fácil de razonar que efectos secundarios globales invisibles.

## 66. Los contextos Decimal y la concurrencia merecen diseño deliberado

El contexto decimal activo se gestiona independientemente para contextos de ejecución según el build de Python y el soporte de gestión de contexto.

La regla práctica es más simple: no uses mutación descontrolada del contexto ambiente como mecanismo de comunicación entre tareas concurrentes.

Pasa la política explícitamente o delimita los cambios con `localcontext()` cuando importe el aislamiento.

## 67. Decimal suele ser más lento que el punto flotante binario

La aritmética Decimal ofrece semántica decimal más rica, contexto controlado por software y manejo de señales. Esas capacidades tienen coste.

No elijas Decimal para toda carga numérica solo porque suene "más preciso".

Elígelo cuando representación decimal, control de redondeo, auditabilidad o fronteras decimales exactas justifiquen el trade-off.

## 68. Decimal no es lo mismo que aritmética racional

`Decimal("0.1")` puede representarse exactamente, pero un valor periódico como un tercio todavía necesita precisión finita durante división.

Para algoritmos cuyo contrato son razones exactas como `1/3`, el tipo `fractions.Fraction` de la biblioteca estándar modela una forma distinta de exactitud.

La selección del tipo numérico debe seguir el modelo matemático que necesita el programa.

## 69. Un cálculo práctico de escala fija

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")

unit_price = Decimal("19.95")
quantity = 3
discount = Decimal("2.50")

subtotal = unit_price * quantity
final_amount = (subtotal - discount).quantize(
    CENT,
    rounding=ROUND_HALF_UP,
)

print(f"subtotal: {subtotal}")
print(f"final: {final_amount}")
```

```text
subtotal: 59.85
final: 57.35
```

Lo importante no es que este ejemplo use dinero. Lo importante es que representación de entrada, aritmética, escala final y política de redondeo estén visibles.

## 70. Un cálculo práctico de precisión local

```python
from decimal import Decimal, getcontext, localcontext


default_precision = getcontext().prec

with localcontext(prec=8):
    result = Decimal(1) / Decimal(7)

print(f"default precision: {default_precision}")
print(f"local result: {result}")
print(f"restored precision: {getcontext().prec}")
```

Con el contexto predeterminado estándar, la salida visible es:

```text
default precision: 28
local result: 0.14285714
restored precision: 28
```

## 71. Un validador práctico de escala

```python
from decimal import Context, Decimal, Inexact, InvalidOperation


TWO_PLACES = Decimal("0.01")
MAX_COEFFICIENT_DIGITS = 28
validator = Context(
    prec=MAX_COEFFICIENT_DIGITS,
    traps=[Inexact, InvalidOperation],
)


def normalize_two_places(raw_value: str) -> Decimal:
    value = Decimal(raw_value)

    if (
        not value.is_finite()
        or len(value.as_tuple().digits) > MAX_COEFFICIENT_DIGITS
    ):
        raise ValueError("unsupported decimal value")

    normalized = value.quantize(TWO_PLACES, context=validator)

    if not normalized.is_finite():
        raise ValueError("quantization produced a non-finite result")

    return normalized


for raw_value in [
    "12.50",
    "7.00",
    "3.141",
    "12345678901234567890123456789.00",
    "NaN",
]:
    try:
        normalized = normalize_two_places(raw_value)
    except (Inexact, InvalidOperation, ValueError):
        print(f"rejected: {raw_value}")
    else:
        print(f"accepted: {normalized}")
```

```text
accepted: 12.50
accepted: 7.00
rejected: 3.141
rejected: 12345678901234567890123456789.00
rejected: NaN
```

Este validador tiene dos políticas explícitas: como máximo 28 dígitos de coeficiente y un resultado de dos posiciones que no descarte dígitos no nulos. También rechaza valores no finitos y atrapa `InvalidOperation`, por lo que una cuantización inválida no puede aceptarse como `NaN`.

## 72. Un monitor práctico de señales

```python
from decimal import Decimal, Inexact, Rounded, localcontext


with localcontext(prec=5) as context:
    context.clear_flags()
    result = Decimal(1) / Decimal(7)

    print(f"result: {result}")
    print(f"rounded: {context.flags[Rounded]}")
    print(f"inexact: {context.flags[Inexact]}")
```

```text
result: 0.14286
rounded: True
inexact: True
```

## 73. Errores comunes

### Error: construir desde float cuando la fuente original es texto decimal

```python
from decimal import Decimal


bad_boundary = Decimal(0.1)
good_boundary = Decimal("0.1")
```

Los dos constructores conservan valores de origen distintos.

### Error: tratar precisión como posiciones decimales

```python
from decimal import localcontext


with localcontext(prec=2):
    pass
```

`prec=2` significa dos dígitos significativos para aritmética, no dos dígitos después del punto decimal.

### Error: formatear en lugar de definir una política numérica de redondeo

```python
from decimal import Decimal


value = Decimal("12.345")
print(f"{value:.2f}")
```

Eso es presentación. No transforma `value` en un Decimal de dos posiciones.

### Error: leer flags antiguas

Si una operación anterior marcó `Inexact`, una comprobación posterior puede engañar si las flags no se limpiaron antes del cálculo monitorizado.

### Error: usar un contexto ambiente como estado compartido oculto

Una función que cambia silenciosamente la precisión puede modificar cálculos no relacionados más tarde en el mismo contexto de ejecución.

### Error: convertir a float en la frontera final de integración sin revisar el contrato

Una conversión a float puede ser aceptable para una API de visualización o inaceptable para un valor persistido exacto. El contrato del destino decide.

## 74. Tabla de decisión

| Requisito | Prefiere |
|---|---|
| aritmética binaria general y rápida | `float` |
| representación exacta de entrada decimal | `Decimal` desde texto o fuente decimal exacta |
| escala decimal fija explícita | `Decimal.quantize()` |
| precisión temporal de trabajo | `localcontext()` |
| política numérica explícita reutilizable | `Context` |
| observar redondeo sin lanzar | flags de señales |
| rechazar una condición aritmética concreta | traps |
| conservar exactamente un float existente | `Decimal.from_float()` |
| detectar conversión accidental de float | `FloatOperation` |
| razones racionales exactas | considera `fractions.Fraction` |
| formato decimal solo para visualización | especificación de formato / f-string |

## 75. Referencia rápida

```text
Decimal("1.25")
Decimal(7)
Decimal.from_float(0.1)
Decimal.from_number(value)        # Python 3.14+

getcontext()
setcontext(context)
localcontext()
localcontext(prec=40)             # keyword attributes: Python 3.11+
Context(prec=28, rounding=...)
Context.create_decimal(value)

value.quantize(Decimal("0.01"))
value.to_integral_value()
value.to_integral_exact()
value.normalize()
value.as_tuple()
value.compare_total(other)
value.fma(other, third)

context.clear_flags()
context.flags[Inexact]
context.flags[Rounded]
context.traps[Inexact] = True
context.traps[FloatOperation] = True

BasicContext
ExtendedContext
DefaultContext
IEEEContext(bits)                 # Python 3.14+
```

## 76. Checklist de diseño

Antes de elegir o configurar Decimal, pregunta:

- ¿De dónde se origina el valor?
- ¿La fuente ya existe como float binario?
- ¿Se requiere representación decimal exacta?
- ¿Cuántos dígitos significativos necesita el cálculo?
- ¿El dominio requiere un número fijo de posiciones decimales?
- ¿Qué regla de redondeo se aplica y en qué paso?
- ¿El redondeo es una transformación aceptada o un fallo de validación?
- ¿Necesito monitorizar `Rounded` o `Inexact`?
- ¿Alguna señal debe convertirse en excepción mediante trap?
- ¿`NaN` e infinitos son valores válidos del dominio?
- ¿Los ceros finales llevan significado?
- ¿Otra biblioteca o API convertirá el valor a float?
- ¿Es segura la mutación del contexto ambiente aquí?
- ¿Un `Context` explícito haría la política más clara?
- ¿He probado valores de empate, negativos, cero y límites de escala?
- ¿Dependo de una API específica de versión?

## 77. Ejercicio

Construye una calculadora ficticia de precios por medición con estos requisitos:

1. Lee precio unitario, cantidad y tasa de ajuste desde strings.
2. Convierte texto decimal directamente a `Decimal`.
3. Realiza aritmética intermedia con al menos 20 dígitos significativos de precisión local.
4. Cuantiza el importe final a dos posiciones decimales usando una regla de redondeo elegida explícitamente.
5. Rechaza un precio unitario de entrada que contenga más de dos posiciones decimales no nulas atrapando `Inexact` durante validación.
6. Limpia e inspecciona flags alrededor del cálculo principal.
7. Muestra si el cálculo principal produjo una señal `Inexact` o `Rounded` antes de la cuantización final.
8. Mantén sin cambios el contexto activo original después de que la función termine.

Desafíos de extensión:

- rechazar valores no finitos;
- añadir una prueba para un caso de redondeo exactamente en el punto medio;
- aceptar un `Context` explícito como argumento de función;
- serializar el valor final bajo un contrato de representación externo documentado.

## 78. Conexiones con otros conceptos de Python

`decimal` se conecta directamente con temas ya estudiados:

- **`float`:** el modelo anterior de representación binaria explica por qué existe Decimal.
- **Strings:** el texto decimal suele ser la frontera de entrada exacta más segura.
- **Funciones:** helpers de redondeo y contextos explícitos convierten política numérica en interfaces reutilizables.
- **Excepciones:** señales atrapadas se convierten en excepciones y pueden participar en flujos normales de validación.
- **Context managers:** `localcontext()` delimita política numérica con `with`.
- **JSON:** `parse_float=Decimal` conserva texto de número JSON como Decimal sin un float de Python intermedio.
- **Logging:** flags y fallos de validación pueden registrarse como evidencia de runtime sin exponer datos sensibles.
- **Pruebas:** redondeo en punto medio, límites de precisión, flags de señal y restauración de contexto merecen assertions de comportamiento.
- **`itertools`:** pipelines de iteradores que agregan valores Decimal deberían conservar el modelo numérico elegido desde origen hasta destino.
- **Próximas utilidades de sistema:** valores decimales suelen cruzar fronteras de archivo, entorno o proceso externo donde importan contratos de conversión a texto.

## Referencias

Referencias primarias utilizadas para este capítulo:

- [Documentación Python 3.14: `decimal` — aritmética decimal de punto fijo y punto flotante](https://docs.python.org/3.14/library/decimal.html)
- [Tutorial Python 3.14: Aritmética de Punto Flotante — Problemas y Limitaciones](https://docs.python.org/3.14/tutorial/floatingpoint.html)
- [Tutorial Python 3.14: aritmética decimal de punto flotante](https://docs.python.org/3.14/tutorial/stdlib2.html#decimal-floating-point-arithmetic)
- [Documentación Python 3.14: módulos numéricos y matemáticos](https://docs.python.org/3.14/library/numeric.html)

## Próximo capítulo

Continúa con **Capítulo 09: `os` y `shutil`** cuando esté disponible.

El próximo capítulo pasa de contratos numéricos a **contratos de operaciones del sistema operativo y filesystem**: acceso al entorno, operaciones de rutas de menor nivel, copia, movimiento, árboles de directorios, metadatos, operaciones destructivas y la frontera entre `pathlib`, `os` y `shutil`.
