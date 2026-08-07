<div align="center">

# Conversión de Tipos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: `type()` e `isinstance()`](../05-type-and-isinstance/README.es.md)

El Capítulo 05 enseñó cómo inspeccionar el tipo que un valor ya tiene. Este último capítulo de Fundamentos enseña el siguiente paso: crear deliberadamente un valor de otro tipo compatible.

Este capítulo se centra en la conversión explícita. Llamar a `int()`, `float()`, `str()` o `bool()` produce un resultado según las reglas de conversión de ese tipo. El valor original no cambia silenciosamente dentro del objeto que ya existía.

Python también puede realizar algunas conversiones implícitas en contextos específicos, como operaciones numéricas mixtas. Esos casos quedan fuera del alcance de este capítulo; aquí, toda conversión se escribe deliberadamente con una de estas llamadas incorporadas.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar los Capítulos 01 a 05 |
| Tiempo estimado de estudio | 60 a 80 minutos |
| Conceptos principales | `int()`, `float()`, `str()`, `bool()`, conversión, `ValueError`, valor de verdad |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- convertir texto compatible a `int` y `float`;
- convertir valores a `str`;
- explicar que una conversión crea un valor resultante en vez de modificar el valor original;
- explicar por qué `int()` trunca un valor de punto flotante hacia cero en vez de redondearlo;
- reconocer conversiones textuales inválidas que producen `ValueError`;
- usar `bool()` de acuerdo con las reglas de valor de verdad de Python;
- explicar por qué `bool("False")` es `True`;
- convertir el texto devuelto por `input()` antes de cálculos numéricos;
- evitar conversiones que oculten la intención o descarten información accidentalmente.

## 1. Por qué existe la conversión

Los programas a menudo reciben un valor en una forma y lo necesitan en otra. Una terminal entrega los resultados de `input()` como texto, mientras que la aritmética normalmente necesita valores numéricos.

La conversión crea un puente explícito entre esas representaciones.

## 2. Las llamadas básicas de conversión

Los nombres de los tipos incorporados se pueden llamar:

```python
integer_value = int(value)
decimal_value = float(value)
text_value = str(value)
boolean_value = bool(value)
```

Lee `int(value)` como "crea un entero a partir de este valor compatible". La misma idea se aplica a las otras llamadas.

## 3. Convierte texto entero con `int()`

Una cadena que contiene una representación entera válida puede convertirse a `int`:

```python
age_text = "28"
age = int(age_text)

print(age)
print(type(age))
```

Salida esperada:

```text
28
<class 'int'>
```

Los caracteres `"28"` son texto. El resultado `28` es un valor entero.

## 4. Convierte texto decimal con `float()`

Una cadena que contiene una representación de punto flotante compatible puede convertirse a `float`:

```python
temperature_text = "21.5"
temperature = float(temperature_text)

print(temperature)
print(type(temperature))
```

Salida esperada:

```text
21.5
<class 'float'>
```

## 5. Convierte valores a texto con `str()`

`str()` crea una representación como cadena de un valor:

```python
attempts = 3
message = "Attempts: " + str(attempts)

print(message)
print(type(message))
```

Salida esperada:

```text
Attempts: 3
<class 'str'>
```

Sin la conversión, concatenar una cadena y un entero con `+` mezclaría tipos de operandos incompatibles.

## 6. La conversión crea un nuevo resultado

El valor original no se convierte silenciosamente en otro tipo:

```python
price_text = "19.90"
price = float(price_text)

print(type(price_text))
print(type(price))
```

Salida esperada:

```text
<class 'str'>
<class 'float'>
```

`price_text` sigue haciendo referencia a una cadena. `price` hace referencia al nuevo resultado de punto flotante.

## 7. Una conversión numérica puede cambiar la representación

Un entero puede convertirse a un valor de punto flotante:

```python
whole_number = float(8)

print(whole_number)
print(type(whole_number))
```

Salida esperada:

```text
8.0
<class 'float'>
```

La magnitud numérica es la misma aquí, pero el tipo resultante es diferente.

## 8. `int()` no redondea valores de punto flotante

Al convertir un número de punto flotante finito, `int()` descarta la parte fraccionaria hacia cero:

```python
print(int(8.9))
print(int(-8.9))
```

Salida esperada:

```text
8
-8
```

Esto es truncamiento, no redondeo.

## 9. Algunas conversiones textuales son inválidas

El texto siguiente es válido para `float()`, pero no para `int()`:

```python
int("8.9")
```

Esta llamada produce `ValueError`.

Si una conversión en dos pasos de texto decimal a entero es realmente la intención, deja visibles las etapas en vez de asumir que `int()` interpreta texto decimal directamente.

## 10. El texto numérico inválido puede producir `ValueError`

Esta llamada también falla:

```python
float("hello")
```

Python produce `ValueError` porque la cadena no puede interpretarse como una representación de punto flotante admitida.

El manejo detallado de excepciones pertenece a una fase posterior. Por ahora, reconoce el error y entiende por qué falló la conversión.

## 11. `bool()` sigue las reglas de valor de verdad

`bool()` no interpreta palabras humanas. Aplica las reglas de valor de verdad de Python:

```python
print(bool(""))
print(bool("False"))
print(bool(0))
print(bool(7))
print(bool(None))
```

Salida esperada:

```text
False
True
False
True
False
```

Las cadenas vacías, el cero numérico y `None` son falsos. Muchos valores no vacíos o distintos de cero son verdaderos.

## 12. `bool("False")` sigue siendo `True`

Un error común es esperar que el texto se interprete como una palabra booleana:

```python
print(bool("False"))
print(bool("0"))
```

Salida esperada:

```text
True
True
```

Ambas cadenas contienen caracteres, por lo que ambas son verdaderas en contexto booleano.

Convertir palabras textuales como `"true"` y `"false"` en booleanos de la aplicación requiere una lógica explícita de interpretación, no solo `bool(text)`.

## 13. Los booleanos pueden convertirse a enteros

Como `bool` es subclase de `int`, la conversión explícita asigna los dos valores booleanos a enteros:

```python
print(int(True))
print(int(False))
```

Salida esperada:

```text
1
0
```

Úsalo solo cuando la representación numérica tenga un significado real. Una intención booleana clara suele ser mejor que tratar casualmente los booleanos como números.

## 14. `None` puede convertirse en texto o booleano

Tipos de destino diferentes aplican reglas diferentes:

```python
print(str(None))
print(bool(None))
```

Salida esperada:

```text
None
False
```

`str(None)` crea el texto `"None"`. No crea un marcador especial de valor ausente dentro de la cadena.

## 15. Convierte `input()` antes de la aritmética numérica

`input()` siempre devuelve texto. Convierte ese texto antes de la aritmética cuando el programa espera un número:

```python
age_text = input("Age: ")
age = int(age_text)

print("Next year:", age + 1)
```

Ejemplo de interacción en la terminal:

```text
Age: 28
Next year: 29
```

Las teclas introducidas llegan primero como texto. La llamada a `int()` crea el entero utilizado en el cálculo.

## 16. Convierte en un límite claro

Un patrón útil para principiantes es:

1. recibir texto externo;
2. almacenarlo con un nombre que deje clara su forma actual;
3. convertirlo una vez cuando se conozca el tipo previsto;
4. seguir utilizando el valor convertido.

Esto evita que el resto del programa arrastre texto ambiguo durante más tiempo del necesario.

## 17. Mantén legibles las conversiones de varios pasos

Las conversiones pueden anidarse, pero los nombres intermedios suelen hacer la transformación más fácil de entender:

```python
number_text = "8.9"
number = float(number_text)
whole_number = int(number)

print(whole_number)
```

Salida esperada:

```text
8
```

El código deja visibles las dos transformaciones: texto a `float` y después `float` a `int`.

## 18. Una conversión puede descartar información

Convertir `8.9` a `8` pierde la parte fraccionaria.

Antes de convertir, pregunta si el tipo de destino puede representar todo lo que todavía necesitas. Una conversión exitosa puede seguir siendo una mala decisión si descarta información significativa.

## 19. Conversión y validación son trabajos diferentes

Una conversión exitosa significa que Python pudo crear el valor solicitado. No demuestra que el valor sea razonable para tu aplicación.

Por ejemplo:

```python
quantity = int("-4")
```

La conversión en sí es válida. Un programa futuro todavía puede rechazar cantidades negativas según sus propias reglas.

La conversión responde "¿esta representación puede convertirse en este tipo?". La validación de la aplicación responde otra pregunta.

## 20. No conviertas solo para hacer desaparecer un error

Una conversión debe representar la intención del programa.

Convertir todo a texto o forzar todo a número puede ocultar un error de modelado en vez de resolverlo. Prefiere conversiones en los puntos donde un valor realmente pasa de una representación a otra.

## 21. Ejemplo práctico: convierte antes del cálculo

Aquí un precio llega como texto:

```python
price_text = "19.90"
price = float(price_text)
shipping = 2.50
total = price + shipping

print(total)
```

Salida esperada:

```text
22.4
```

La conversión ocurre antes de la aritmética, por lo que los dos operandos de la suma son numéricos.

## 22. Errores comunes

Observa estos patrones:

- suponer que `int(8.9)` redondea a `9`;
- esperar que `int("8.9")` funcione solo porque el texto representa un número;
- esperar que `bool("False")` devuelva `False`;
- convertir un valor sin considerar la pérdida de información;
- convertir repetidamente el mismo valor de un tipo a otro sin una razón clara;
- olvidar que `input()` devuelve texto.

## 23. Referencia rápida

| Expresión | Resultado | Significado |
|---|---|---|
| `int("28")` | `28` | Convertir texto entero válido |
| `float("21.5")` | `21.5` | Convertir texto decimal compatible |
| `float(8)` | `8.0` | Crear punto flotante desde un entero |
| `int(8.9)` | `8` | Truncar un float finito hacia cero |
| `str(28)` | `"28"` | Crear texto |
| `bool(0)` | `False` | Aplicar prueba de valor de verdad |
| `bool("False")` | `True` | Las cadenas no vacías son verdaderas |

## 24. Ejercicio

Escribe un pequeño programa interactivo que:

1. pida una cantidad entera;
2. pida un precio decimal;
3. convierta los dos resultados de `input()`;
4. calcule `quantity * price`;
5. muestre el resultado.

Prueba una vez con texto numérico válido. Después introduce deliberadamente texto incompatible y observa el error sin intentar manejarlo todavía.

## 25. Autoevaluación

Antes de salir de Fundamentos, confirma que puedes responder estas preguntas:

- ¿Qué tipo devuelve `input()`?
- ¿Por qué `int("8.9")` falla mientras `float("8.9")` funciona?
- ¿`int(8.9)` redondea?
- ¿Por qué `bool("False")` es verdadero?
- ¿Convertir `price_text` a `float` cambia el valor almacenado en `price_text`?
- ¿Cuándo puede una conversión perder información?

## 26. Ejemplo: conversiones básicas

El primer ejemplo del repositorio mantiene separados los valores textuales originales y los valores convertidos:

```python
age_text = "28"
temperature_text = "21.5"

age = int(age_text)
temperature = float(temperature_text)
summary = str(age) + " years"

print(age, type(age))
print(temperature, type(temperature))
print(summary, type(summary))
```

Salida esperada:

```text
28 <class 'int'>
21.5 <class 'float'>
28 years <class 'str'>
```

## 27. Ejemplo: sorpresas de la conversión

El segundo ejemplo registra comportamientos importantes:

```python
print(int(8.9))
print(int(-8.9))
print(bool(""))
print(bool("False"))
print(bool(0))
print(bool(1))
```

Salida esperada:

```text
8
-8
False
True
False
True
```

## 28. Ejecuta los ejemplos

Desde la raíz del repositorio:

```bash
python fundamentals/06-type-conversion/examples/conversion_basics.py
python fundamentals/06-type-conversion/examples/conversion_surprises.py
```

Los dos ejemplos son deterministas, no interactivos, no usan red ni dependencias externas y son adecuados para ejecución automática.

## 29. Ejecuta las verificaciones del repositorio

Después de editar el capítulo o los ejemplos:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 30. Fase 1 completada

Con este capítulo, la ruta de Fundamentos está completada.

Ahora puedes ejecutar un archivo de Python, mostrar y recibir información, almacenar valores, reconocer e inspeccionar tipos comunes y convertir deliberadamente valores compatibles. El roadmap continúa con la **Fase 2: Textos y números**.

## Referencias oficiales

- [Funciones incorporadas de Python — `int()`](https://docs.python.org/3/library/functions.html#int)
- [Funciones incorporadas de Python — `float()`](https://docs.python.org/3/library/functions.html#float)
- [Funciones incorporadas de Python — `str()`](https://docs.python.org/3/library/functions.html#str)
- [Funciones incorporadas de Python — `bool()`](https://docs.python.org/3/library/functions.html#bool)
- [Tipos incorporados de Python — prueba de valor de verdad](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Excepciones incorporadas de Python — `ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: `type()` e `isinstance()`](../05-type-and-isinstance/README.es.md)
