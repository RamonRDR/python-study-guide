<div align="center">

# `int`, `float` y `bool`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Python ya presentó estos tipos en la fase de Fundamentos. Este capítulo avanza un nivel al centrarse en cómo se comportan en expresiones, cómo difieren sus resultados y qué detalles importan al elegir entre ellos.

El objetivo no es memorizar reglas aisladas. El objetivo es construir un modelo mental confiable para números enteros, valores decimales aproximados y valores de verdad.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- elegir `int`, `float` o `bool` según el significado de un valor;
- explicar por qué los enteros de Python no están limitados a un rango fijo de 32 o 64 bits;
- predecir el tipo de resultado de expresiones numéricas mixtas comunes;
- distinguir `/` de `//` y `%`;
- comprender por qué la división por piso con números negativos puede sorprender a principiantes;
- reconocer los límites de aproximación de los valores binarios de punto flotante;
- explicar por qué `0.1 + 0.2 == 0.3` es `False`;
- usar `bool()` y valores de verdad sin confundir contenido textual con significado booleano;
- explicar la relación especial entre `bool` e `int`;
- evitar usar valores booleanos como cantidades numéricas cuando eso oculte la intención.

## 1. Tres tipos, tres funciones principales

Un primer modelo útil es:

| Tipo | Función principal | Ejemplo |
|---|---|---|
| `int` | valores enteros | `12`, `0`, `-4` |
| `float` | valores fraccionarios o reales aproximados | `7.5`, `-0.25` |
| `bool` | valores de verdad | `True`, `False` |

```python
item_count = 12
unit_price = 7.5
is_available = True

print(type(item_count))
print(type(unit_price))
print(type(is_available))
```

```text
<class 'int'>
<class 'float'>
<class 'bool'>
```

Estos tipos pueden interactuar, pero siguen comunicando significados diferentes.

## 2. `int` representa enteros

Usa `int` para valores que conceptualmente no tienen parte fraccionaria.

```python
students = 30
temperature_change = -4
balance_adjustment = 0

print(students)
print(temperature_change)
print(balance_adjustment)
```

```text
30
-4
0
```

Un entero puede ser positivo, negativo o cero.

## 3. Los enteros de Python tienen precisión arbitraria

En muchos lenguajes de programación, un tipo entero está vinculado a una cantidad fija de bits. El `int` incorporado de Python es diferente: los enteros tienen precisión arbitraria, limitada principalmente por la memoria disponible y por restricciones de implementación, no por un rango normal fijo de 32 o 64 bits.

```python
large_number = 10 ** 100

print(type(large_number))
print(len(str(large_number)))
```

```text
<class 'int'>
101
```

Esto no significa que los enteros extremadamente grandes sean gratuitos. Los valores mayores requieren más memoria y procesamiento. La idea importante para principiantes es simplemente que los valores `int` normales de Python no desbordan en un límite pequeño fijo como 2.147.483.647.

## 4. Los separadores numéricos mejoran la legibilidad

Python permite underscores dentro de literales numéricos para mejorar la lectura.

```python
annual_revenue = 1_250_000
binary_mask = 0b1010

print(annual_revenue)
print(binary_mask)
```

```text
1250000
10
```

Los underscores forman parte de la notación del código fuente, no del valor numérico almacenado.

El literal binario aparece solo para mostrar que la notación de enteros puede variar. Las bases numéricas no son el foco de este capítulo.

## 5. `float` representa valores de punto flotante

Usa `float` cuando un valor necesita una parte fraccionaria o cuando una operación produce naturalmente un resultado de punto flotante.

```python
unit_price = 19.90
exchange_rate = 5.42
temperature = -3.5

print(type(unit_price))
print(type(exchange_rate))
print(type(temperature))
```

```text
<class 'float'>
<class 'float'>
<class 'float'>
```

Un punto decimal en un literal numérico normalmente produce un `float`.

## 6. `int` y `float` pueden participar en la misma expresión

Python admite aritmética mixta entre estos tipos numéricos.

```python
whole_number = 4
decimal_number = 2.5

print(whole_number + decimal_number)
print(type(whole_number + decimal_number))
```

```text
6.5
<class 'float'>
```

Cuando un entero y un valor de punto flotante participan en una operación aritmética común, Python normalmente produce un resultado de punto flotante para conservar la capacidad fraccionaria.

Este es un ejemplo de conversión numérica implícita. No reemplaza los conceptos de conversión explícita aprendidos en Fundamentos.

## 7. `/` es división verdadera

El operador `/` realiza división verdadera.

```python
print(7 / 2)
print(type(7 / 2))
```

```text
3.5
<class 'float'>
```

Incluso cuando ambos operandos son enteros, `/` normalmente produce un resultado de punto flotante cuando el cociente puede representarse como `float`. Si el cociente entero es demasiado grande para representarse como `float`, la división verdadera genera `OverflowError`.

```python
print(8 / 4)
print(type(8 / 4))
```

```text
2.0
<class 'float'>
```

Cuando el cociente puede representarse como `float`, un cociente matemáticamente entero sigue teniendo tipo `float` cuando se usa `/`.

## 8. `//` es división por piso

El operador `//` realiza división por piso.

```python
print(7 // 2)
print(7.0 // 2)
```

```text
3
3.0
```

Con dos enteros, el resultado es entero. Si participa un operando de punto flotante, el resultado es un valor de punto flotante que representa el cociente redondeado hacia abajo.

La palabra **piso** importa. `//` no significa simplemente "eliminar la parte decimal".

## 9. `%` da el resto asociado con la división por piso

El operador `%` da el resto.

```python
print(7 % 2)
print(14 % 5)
```

```text
1
4
```

Para enteros, `//` y `%` se relacionan mediante esta igualdad:

```text
dividend == divisor * (dividend // divisor) + (dividend % divisor)
```

Ejemplo:

```python
value = 17
divisor = 5

quotient = value // divisor
remainder = value % divisor

print(quotient)
print(remainder)
print(divisor * quotient + remainder)
```

```text
3
2
17
```

Esta relación resulta especialmente útil al dividir valores en grupos y sobrantes.

## 10. La división por piso con números negativos puede sorprender

Un error común es esperar que la división por piso simplemente trunque hacia cero.

```python
print(-7 // 3)
print(-7 % 3)
```

```text
-3
2
```

¿Por qué `-3` en lugar de `-2`?

Porque la división por piso redondea el cociente hacia abajo, en dirección al infinito negativo. El cociente exacto es aproximadamente `-2.333...`, y su piso es `-3`.

El resto conserva entonces la identidad de la división:

```text
-7 == 3 * (-3) + 2
```

No necesitas memorizar cada caso negativo. Recuerda la regla: `//` significa división por piso, no truncamiento.

## 11. `**` realiza exponenciación

El operador de exponenciación es `**`.

```python
print(2 ** 5)
print(9 ** 0.5)
```

```text
32
3.0
```

El tipo del resultado depende de los valores y de la operación. Elevar `9` a `0.5` usa un exponente de punto flotante y produce un `float`.

## 12. Dividir entre cero es un error

Los tipos numéricos no hacen válida la división entre cero.

```python
print(10 / 0)
```

La operación genera:

```text
ZeroDivisionError: division by zero
```

El traceback completo contiene líneas adicionales e información del archivo. Lo importante aquí es el tipo de excepción.

El manejo de excepciones se estudia más adelante en el roadmap. Por ahora, reconoce que una operación aritmética inválida puede detener la ejecución del programa.

## 13. Los valores de punto flotante suelen ser aproximaciones

En la mayoría de los sistemas modernos, los números de punto flotante de Python usan aritmética binaria de punto flotante proporcionada por el hardware.

Muchas fracciones decimales sencillas no pueden representarse exactamente como fracciones binarias finitas. Eso significa que un valor como `0.1` se almacena como la aproximación binaria representable más cercana.

Esto no es un error específico de Python. Es una propiedad de la aritmética binaria de punto flotante usada por muchos lenguajes y procesadores.

## 14. El ejemplo clásico de `0.1 + 0.2`

```python
result = 0.1 + 0.2

print(result)
print(result == 0.3)
```

```text
0.30000000000000004
False
```

El resultado mostrado expone una pequeña diferencia de representación.

La lección importante no es que los floats sean poco confiables. La lección es que representan muchos valores decimales de forma aproximada, por lo que la igualdad decimal exacta puede ser inapropiada en algunas situaciones.

## 15. El texto decimal mostrado no cuenta toda la historia interna

Python normalmente muestra una representación decimal corta que vuelve al mismo valor de punto flotante almacenado.

Puedes inspeccionar una razón entera exacta para un float finito:

```python
value = 0.1

print(value)
print(value.as_integer_ratio())
```

```text
0.1
(3602879701896397, 36028797018963968)
```

La razón muestra el valor binario exacto de punto flotante que este `float` representa en implementaciones estándar de Python que usan aritmética IEEE 754 binary64.

Para un principiante, basta con este modelo mental: el texto `0.1` es una notación conveniente para un valor de punto flotante representable cercano.

## 16. No uses igualdad de floats sin considerar el contexto

Esto puede ser frágil:

```python
print(0.1 + 0.2 == 0.3)
```

```text
False
```

Que la igualdad exacta sea adecuada depende del dominio.

Para comparaciones numéricas aproximadas, la biblioteca estándar de Python ofrece herramientas como `math.isclose()`. Para aritmética decimal exacta en base 10, el módulo `decimal` suele ser más apropiado.

Estas herramientas pertenecen a fases posteriores del roadmap, así que este capítulo solo presenta la razón por la que existen.

## 17. Los valores monetarios merecen atención especial

Un patrón tentador para principiantes es:

```python
account_balance = 0.1 + 0.2
```

Un `float` puede ser perfectamente adecuado para muchas mediciones, cálculos gráficos, simulaciones y tareas numéricas comunes. Pero los dominios que requieren comportamiento decimal exacto, como muchos cálculos contables, a menudo necesitan una representación decimal diseñada para ese requisito.

No conviertas esto en la regla simplista "float es malo para dinero". La pregunta correcta es qué garantías de precisión, redondeo, almacenamiento y dominio necesita la aplicación.

## 18. `float.is_integer()` pregunta si un float tiene valor integral

Un `float` puede representar un valor sin parte fraccionaria.

```python
print((5.0).is_integer())
print((5.25).is_integer())
```

```text
True
False
```

`5.0` sigue siendo un `float`. `is_integer()` pregunta por su valor numérico, no por su tipo en tiempo de ejecución.

```python
value = 5.0

print(type(value))
print(value.is_integer())
```

```text
<class 'float'>
True
```

## 19. `bool` representa valores de verdad

El tipo booleano tiene dos valores:

```python
is_ready = True
has_error = False

print(type(is_ready))
print(type(has_error))
```

```text
<class 'bool'>
<class 'bool'>
```

Usa `bool` cuando el significado sea sí/no, verdadero/falso, habilitado/deshabilitado, disponible/no disponible u otra condición de dos estados.

## 20. Las comparaciones producen resultados booleanos

Las comparaciones responden preguntas sobre valores y normalmente producen `True` o `False`.

```python
temperature = 18

print(temperature > 20)
print(temperature == 18)
```

```text
False
True
```

El uso detallado de comparaciones dentro de `if`, `while` y otras estructuras de flujo llegará más adelante. Aquí, céntrate en el tipo del resultado.

## 21. Todo objeto puede participar en pruebas de valor de verdad

Python puede interpretar muchos valores como verdaderos o falsos en un contexto booleano.

```python
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(None))
print(bool(1))
print(bool(-3))
print(bool("Python"))
```

```text
False
False
False
False
True
True
True
```

Para los tipos ya presentados en esta guía:

- el cero numérico es falso;
- una string vacía es falsa;
- `None` es falso;
- los números distintos de cero son verdaderos;
- las strings no vacías son verdaderas.

Las colecciones añadirán más reglas de valor de verdad después.

## 22. El contenido textual no se interpreta como una palabra booleana

Esta es una trampa clásica para principiantes:

```python
print(bool("False"))
print(bool("0"))
```

```text
True
True
```

Las dos strings no están vacías, por lo que ambas son truthy.

`bool()` no lee palabras en inglés y decide su significado. Aplica las reglas de valor de verdad de Python al objeto.

## 23. `bool` es una subclase de `int`

Python tiene una relación histórica y técnica entre valores booleanos y enteros.

```python
print(isinstance(True, bool))
print(isinstance(True, int))
print(int(True))
print(int(False))
```

```text
True
True
1
0
```

Por eso el Capítulo 05 de Fundamentos mostró que `isinstance(True, int)` es `True`, aunque `type(True) is bool`.

La relación es real, pero no debe borrar el significado semántico.

## 24. La aritmética booleana funciona, pero a menudo comunica la idea equivocada

Como `bool` es una subclase de `int`, esto es Python válido:

```python
print(True + True)
print(False + 10)
```

```text
2
10
```

Eso no significa que la aritmética booleana deba ser tu diseño predeterminado.

Si una variable significa disponibilidad, validación, permiso u otra condición, conserva ese significado en lugar de tratar el valor como un `0` o `1` accidental.

## 25. Elige un tipo según el significado, no la apariencia

Considera este pequeño modelo:

```python
items_in_cart = 3
average_price = 14.75
is_checkout_open = True

print(type(items_in_cart))
print(type(average_price))
print(type(is_checkout_open))
```

```text
<class 'int'>
<class 'float'>
<class 'bool'>
```

Los tres valores podrían participar en comportamiento numérico en algunas circunstancias, pero sus significados de dominio son diferentes.

Buenas elecciones de tipo hacen que el código posterior sea más fácil de entender.

## 26. Evita flags enteras cuando un booleano expresa la intención

Menos claro:

```python
is_active = 1
```

Más claro:

```python
is_active = True
```

Una flag entera puede ser válida al comunicarse con un formato de archivo, base de datos, protocolo o API heredada que exija `0` y `1`. Dentro de la lógica Python normal, un `bool` suele comunicar la intención booleana con más claridad.

## 27. Evita añadir `.0` solo para que un valor parezca decimal

Esto no es automáticamente mejor:

```python
employee_count = 42.0
```

Si el valor representa una cantidad que no puede ser fraccionaria, `42` puede expresar mejor el dominio.

Del mismo modo, un valor como `5.0` puede necesitar legítimamente seguir siendo `float` cuando forma parte de una cadena de cálculos basada en mediciones u operaciones de punto flotante.

El significado va primero.

## 28. Los tipos de resultado numérico pueden aportar información

Compara:

```python
print(5 + 2)
print(5 + 2.0)
print(5 / 2)
print(5 // 2)
```

```text
7
7.0
2.5
2
```

Los operadores y los tipos de los operandos influyen tanto en el valor como en el tipo del resultado.

Al depurar código numérico, inspecciona ambos.

## 29. Ejemplo práctico: comportamiento numérico

El archivo [`examples/numeric_behavior.py`](examples/numeric_behavior.py) contiene:

```python
whole_number = 7
decimal_number = 2.5

print("Mixed addition:", whole_number + decimal_number)
print("True division:", 7 / 2)
print("Floor division:", 7 // 2)
print("Remainder:", 7 % 2)
print("Negative floor division:", -7 // 3)
print("Matching remainder:", -7 % 3)
```

Salida esperada:

```text
Mixed addition: 9.5
True division: 3.5
Floor division: 3
Remainder: 1
Negative floor division: -3
Matching remainder: 2
```

Este ejemplo mantiene varias reglas numéricas relacionadas en un mismo lugar.

## 30. Ejemplo práctico: verdad y precisión

El archivo [`examples/truth_and_precision.py`](examples/truth_and_precision.py) contiene:

```python
print("0.1 + 0.2:", 0.1 + 0.2)
print("Exactly 0.3:", 0.1 + 0.2 == 0.3)
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print('bool(""):', bool(""))
print('bool("False"):', bool("False"))
print("bool is int-compatible:", isinstance(True, int))
```

Salida esperada:

```text
0.1 + 0.2: 0.30000000000000004
Exactly 0.3: False
bool(0): False
bool(1): True
bool(""): False
bool("False"): True
bool is int-compatible: True
```

El ejemplo coloca deliberadamente dos sorpresas comunes juntas: aproximación de punto flotante y reglas de valor de verdad booleano.

## 31. Errores comunes

### Error 1: esperar que `/` conserve `int`

```python
print(type(8 / 4))
```

```text
<class 'float'>
```

### Error 2: interpretar `//` como truncamiento hacia cero

```python
print(-7 // 3)
```

```text
-3
```

### Error 3: esperar que la aritmética decimal con floats sea exacta

```python
print(0.1 + 0.2 == 0.3)
```

```text
False
```

### Error 4: suponer que el texto `"False"` es falso

```python
print(bool("False"))
```

```text
True
```

### Error 5: olvidar que `bool` es compatible con `int`

```python
print(isinstance(True, int))
```

```text
True
```

Compatibilidad no significa que los dos tipos expresen la misma intención.

## 32. Ejercicio: crea un perfil numérico

Crea un archivo llamado `numeric_profile.py`.

Usa estos valores iniciales:

```python
item_count = 12
unit_price = 7.5
is_available = True
```

Tu programa debe:

1. calcular `subtotal` multiplicando `item_count` por `unit_price`;
2. imprimir cada valor original;
3. imprimir el tipo de cada valor original;
4. imprimir `subtotal`;
5. imprimir el tipo de `subtotal`;
6. explicar, con tus propias palabras, por qué `subtotal` es un `float`.

Una implementación posible es:

```python
item_count = 12
unit_price = 7.5
is_available = True

subtotal = item_count * unit_price

print("Item count:", item_count)
print("Item count type:", type(item_count))
print("Unit price:", unit_price)
print("Unit price type:", type(unit_price))
print("Available:", is_available)
print("Available type:", type(is_available))
print("Subtotal:", subtotal)
print("Subtotal type:", type(subtotal))
```

Salida esperada:

```text
Item count: 12
Item count type: <class 'int'>
Unit price: 7.5
Unit price type: <class 'float'>
Available: True
Available type: <class 'bool'>
Subtotal: 90.0
Subtotal type: <class 'float'>
```

Intenta el ejercicio por tu cuenta antes de comparar con el ejemplo.

## 33. Autoevaluación

Ahora deberías poder responder estas preguntas antes de ejecutar Python:

1. ¿Cuál es la principal diferencia conceptual entre `int`, `float` y `bool`?
2. ¿Por qué Python puede almacenar un entero mucho mayor que un entero normal de 64 bits?
3. ¿Qué tipo produce `7 / 2`?
4. ¿Cuál es la diferencia entre `/` y `//`?
5. ¿Por qué `-7 // 3` es igual a `-3`?
6. ¿Qué devuelve `%`?
7. ¿Por qué `0.1 + 0.2 == 0.3` puede ser `False`?
8. ¿`5.0` es un `int` porque su parte fraccionaria es cero?
9. ¿Por qué `bool("False")` es igual a `True`?
10. ¿Por qué `isinstance(True, int)` devuelve `True`?

## 34. Consulta rápida

| Objetivo | Ejemplo | Detalle importante |
|---|---|---|
| Número entero | `count = 12` | `int` tiene precisión arbitraria |
| Valor numérico fraccionario | `rate = 5.42` | `float` normalmente es punto flotante binario aproximado |
| Valor de verdad | `is_ready = True` | `bool` tiene `True` y `False` |
| División verdadera | `7 / 2` | devuelve `3.5` |
| División por piso | `7 // 2` | devuelve el cociente por piso |
| Resto | `7 % 2` | trabaja junto con la división por piso |
| Exponenciación | `2 ** 5` | devuelve `32` |
| Probar valor integral de float | `(5.0).is_integer()` | el valor puede ser integral mientras el tipo sigue siendo `float` |
| Convertir a valor de verdad | `bool(value)` | sigue las reglas de valor de verdad |
| Tipo exacto en tiempo de ejecución | `type(value)` | `type(True) is bool` |
| Tipo compatible | `isinstance(value, int)` | `True` es compatible con `int` |

## 35. Ejecuta los ejemplos

Desde la raíz del repositorio:

```bash
python strings-and-numbers/03-int-float-and-bool/examples/numeric_behavior.py
python strings-and-numbers/03-int-float-and-bool/examples/truth_and_precision.py
```

Después ejecuta las verificaciones del repositorio:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 36. Qué viene después

Ahora tienes un modelo más sólido para números enteros, valores de punto flotante y valores booleanos.

El siguiente capítulo completa la Fase 2 presentando funciones numéricas comunes: **`round()`, `abs()`, `min()`, `max()` y `sum()`**.

Ese capítulo se apoyará directamente en el comportamiento numérico establecido aquí, en lugar de tratar esas funciones como una lista aislada.

## Referencias oficiales

- [Tipos incorporados de Python: Tipos numéricos](https://docs.python.org/3.14/library/stdtypes.html#numeric-types-int-float-complex)
- [Tipos incorporados de Python: Pruebas de valor de verdad](https://docs.python.org/3.14/library/stdtypes.html#truth-value-testing)
- [Tipos incorporados de Python: Tipo booleano](https://docs.python.org/3.14/library/stdtypes.html#boolean-type-bool)
- [Tutorial de Python: Aritmética de punto flotante, problemas y limitaciones](https://docs.python.org/3.14/tutorial/floatingpoint.html)

[← Volver al índice de la sección](../README.es.md)
