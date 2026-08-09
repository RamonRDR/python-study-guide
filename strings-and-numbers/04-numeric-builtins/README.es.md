<div align="center">

# Funciones Numéricas Incorporadas: `round()`, `abs()`, `min()`, `max()` y `sum()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: `int`, `float` y `bool`](../03-int-float-and-bool/README.es.md)

La Fase 2 ya presentó texto, operaciones con strings, enteros, valores de punto flotante y valores booleanos. Este capítulo cierra la fase combinando ese conocimiento con cinco funciones incorporadas que resuelven tareas numéricas comunes sin requerir importaciones.

Estas funciones parecen pequeñas, pero varias contienen detalles importantes en programas reales. En particular, `round()` no siempre se comporta como la regla cotidiana de que "5 siempre redondea hacia arriba", la representación de punto flotante puede influir en los resultados redondeados y `min()` y `max()` requieren cuidado con entradas vacías.

## Información del capítulo

- **Nivel:** Principiante
- **Prerrequisito:** completar los Capítulos 01 a 03 de la Fase 2
- **Tiempo estimado de estudio:** 70 a 90 minutos
- **Conceptos principales:** `round()`, `abs()`, `min()`, `max()`, `sum()`, `ndigits`, iterables vacíos, agregación numérica, redondeo de punto flotante

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- usar `abs()` para obtener la magnitud numérica sin modificar el valor original;
- usar `min()` y `max()` con varios argumentos o con un iterable;
- explicar por qué los iterables vacíos requieren cuidado con `min()` y `max()`;
- usar `sum()` para agregar valores numéricos y comprender su argumento `start`;
- usar `round()` con `ndigits` omitido, positivo, cero y negativo;
- explicar la regla de desempate que usa Python para el redondeo numérico incorporado;
- reconocer por qué la representación de punto flotante puede afectar un resultado redondeado;
- elegir estas funciones incorporadas para expresar la intención con claridad en lugar de reproducir manualmente su comportamiento;
- reconocer cuándo herramientas posteriores, como `math.fsum()` o la aritmética decimal, pueden ser más apropiadas.

---

## 1. Las funciones incorporadas están disponibles sin importaciones

Python proporciona un conjunto de funciones incorporadas disponibles directamente en el código normal.

Ya conoces ejemplos como:

```python
print("Python")
length = len("Python")
number = int("42")
```

Las funciones de este capítulo funcionan de la misma manera desde el punto de vista de uso:

```python
print(abs(-8))
print(round(3.14159, 2))
```

No necesitas esto:

```python
import builtins
```

El uso directo es el enfoque normal.

### Modelo mental

Piensa en estas funciones como pequeñas herramientas estándar que comunican intención:

```text
abs()    -> magnitude
round()  -> rounded numeric value
min()    -> smallest item
max()    -> largest item
sum()    -> accumulated total
```

La claridad de intención es importante. `min(values)` le dice al lector lo que quieres de una forma mucho más directa que comparar manualmente cada valor.

---

## 2. `abs()` devuelve un valor absoluto

Para enteros y números de punto flotante comunes, `abs()` devuelve la distancia a cero sin signo negativo.

```python
print(abs(-12))
print(abs(12))
print(abs(-3.5))
```

```text
12
12
3.5
```

El signo de la entrada no determina el signo del resultado. El resultado representa magnitud.

### `abs()` no modifica el valor original

```python
temperature_change = -7
magnitude = abs(temperature_change)

print(temperature_change)
print(magnitude)
```

```text
-7
7
```

La variable original sigue apuntando a `-7`. `abs()` calculó y devolvió otro valor.

Esto sigue un patrón que ya has visto en Python:

```text
input value -> operation -> result value
```

### Uso práctico: distancia respecto de un objetivo

Supón que un valor objetivo es `100`, mientras que el valor observado es `93`.

```python
observed = 93
target = 100
difference = observed - target
absolute_difference = abs(difference)

print(absolute_difference)
```

```text
7
```

Cuando la dirección no importa y solo interesa el tamaño de la diferencia, `abs()` comunica claramente esa intención.

---

## 3. `min()` encuentra el elemento más pequeño

`min()` puede recibir dos o más argumentos posicionales:

```python
print(min(8, 3, 12, -2))
```

```text
-2
```

También puede recibir un único iterable que contenga los valores.

El siguiente ejemplo usa una lista solo como un contenedor sencillo. Las listas se enseñan adecuadamente en la Fase 3.

```python
values = [8, 3, 12, -2]
print(min(values))
```

```text
-2
```

Las dos formas responden al mismo tipo de pregunta, pero son útiles en situaciones diferentes:

```text
min(a, b, c)   -> values already exist as separate arguments
min(values)    -> values are already grouped in an iterable
```

### `min()` devuelve un elemento existente

Con números comunes, esto parece obvio:

```python
smallest = min(10, 4, 7)
print(smallest)
```

```text
4
```

Más adelante, cuando estudies objetos más ricos y el argumento `key`, esta idea será todavía más importante. Por ahora, concéntrate en comparaciones numéricas.

---

## 4. `max()` encuentra el elemento más grande

`max()` refleja a `min()`.

Con argumentos separados:

```python
print(max(8, 3, 12, -2))
```

```text
12
```

Con un único iterable:

```python
values = [8, 3, 12, -2]
print(max(values))
```

```text
12
```

Esta simetría hace que el par sea fácil de recordar:

```text
min(...) -> smallest
max(...) -> largest
```

### Uso práctico: amplitud de un rango

Si la medición más baja es `min(values)` y la más alta es `max(values)`, la diferencia entre ambas describe la amplitud del rango observado.

```python
values = [8, 3, 12, -2]
range_width = max(values) - min(values)
print(range_width)
```

```text
14
```

Este cálculo combina varios conceptos sin ocultar la intención.

---

## 5. Las entradas vacías son importantes para `min()` y `max()`

Un iterable vacío no tiene elemento más pequeño ni más grande.

```python
values = []
```

Llamar a cualquiera de las funciones sin un valor alternativo genera `ValueError`:

```python
min(values)
```

```text
ValueError: min() iterable argument is empty
```

Y, de forma similar:

```python
max(values)
```

```text
ValueError: max() iterable argument is empty
```

Al usar la forma con un único iterable, puedes proporcionar `default=`:

```python
values = []
print(min(values, default=0))
print(max(values, default=0))
```

```text
0
0
```

### El valor alternativo debe tener sentido para el dominio

`default=0` no es automáticamente la elección correcta.

Por ejemplo, si un conjunto vacío significa "no hay medición", devolver cero podría sugerir incorrectamente que realmente se midió cero.

La lección importante es:

```text
default is a domain decision, not merely an error-suppression trick
```

Tomarás estas decisiones de forma más deliberada después de aprender flujo del programa y manejo de `None` en fases posteriores.

---

## 6. Se requieren valores comparables

`min()` y `max()` comparan elementos.

Los valores numéricos compatibles normalmente pueden participar juntos:

```python
print(min(4, 2.5, 9))
print(max(4, 2.5, 9))
```

```text
2.5
9
```

Pero tipos sin relación entre sí pueden no tener una relación de orden:

```python
min(4, "2")
```

```text
TypeError: '<' not supported between instances of 'str' and 'int'
```

No conviertas valores solo para silenciar el error. Primero decide qué deberían significar los datos.

---

## 7. `sum()` acumula valores numéricos

`sum()` recibe un iterable y suma conceptualmente sus elementos de izquierda a derecha, devolviendo el total.

```python
values = [10, 20, 5]
print(sum(values))
```

```text
35
```

Un iterable vacío tiene una suma bien definida porque el valor inicial predeterminado es cero:

```python
print(sum([]))
```

```text
0
```

Este comportamiento difiere de `min()` y `max()`, donde una entrada vacía no tiene un menor o mayor elemento natural.

---

## 8. `sum()` tiene un argumento `start`

El segundo argumento de `sum()` proporciona el valor inicial.

```python
values = [10, 20, 5]
print(sum(values, 100))
```

```text
135
```

Un modelo mental útil es:

```text
total = start + all iterable items
```

El valor predeterminado equivale a:

```python
sum(values, 0)
```

### `start` no es un índice

Un error común entre principiantes es interpretar el segundo argumento como "empieza a sumar desde esta posición".

No significa eso.

```python
values = [10, 20, 5]
print(sum(values, 2))
```

```text
37
```

El `2` se añade al total. No le dice a Python que omita los dos primeros elementos.

---

## 9. No uses `sum()` para concatenar strings

Esto no está soportado:

```python
sum(["Py", "thon"])
```

La llamada genera `TypeError`.

Para strings, el patrón estándar es `join()`, que estudiaste anteriormente en esta fase:

```python
parts = ["Py", "thon"]
print("".join(parts))
```

```text
Python
```

Las funciones comunican intenciones diferentes:

```text
sum()  -> numeric accumulation
join() -> string concatenation from an iterable
```

Mantener esas responsabilidades separadas produce código más claro.

---

## 10. Los totales de punto flotante todavía pueden ser aproximados

El capítulo anterior explicó que muchas fracciones decimales no pueden representarse exactamente como valores binarios de punto flotante.

`sum()` no convierte la aritmética con `float` en aritmética decimal exacta.

```python
values = [0.1, 0.2]
print(sum(values))
```

```text
0.30000000000000004
```

Esto es un asunto de representación de punto flotante, no un fallo de `sum()`.

La biblioteca estándar de Python contiene herramientas para casos que necesitan garantías numéricas diferentes. Por ejemplo, `math.fsum()` está diseñado para sumas de punto flotante más precisas, mientras que la aritmética decimal es útil cuando se requiere semántica decimal.

Esas herramientas están fuera del alcance de este capítulo. La idea importante ahora es no asumir que la agregación elimina la aproximación de punto flotante.

---

## 11. `round()` devuelve un valor numérico redondeado

Para los valores incorporados `int` y `float` usados en este capítulo, `round(number)` devuelve el entero más cercano.

```python
print(round(3.2))
print(round(3.8))
```

```text
3
4
```

Cuando `ndigits` se omite o es `None`, los casos de `int` y `float` tratados aquí devuelven un `int`:

```python
result = round(3.8)
print(type(result))
```

```text
<class 'int'>
```

---

## 12. `ndigits` controla la posición del redondeo

Un segundo argumento controla la precisión solicitada.

```python
print(round(3.14159, 2))
print(round(3.14159, 4))
```

```text
3.14
3.1416
```

Para los casos de `int` y `float` usados aquí, proporcionar `ndigits` afecta una regla importante del tipo de retorno:

```python
print(round(2.5))
print(type(round(2.5)))
print(round(2.5, 0))
print(type(round(2.5, 0)))
```

```text
2
<class 'int'>
2.0
<class 'float'>
```

Sin `ndigits`, el resultado demostrado con `float` es entero. En los casos de `int` y `float` tratados aquí, proporcionar `ndigits` mantiene un resultado `int` como `int` y un resultado `float` como `float`; esto no es una regla para todos los tipos numéricos incorporados.

---

## 13. `ndigits` puede ser cero o negativo

Cero solicita redondeo a la posición de unidades. Para los tipos incorporados usados en este capítulo, un `int` sigue siendo `int` y un `float` sigue siendo `float` cuando `ndigits` se proporciona explícitamente:

```python
print(round(12.7, 0))
```

```text
13.0
```

Los valores negativos redondean a posiciones a la izquierda del separador decimal:

```python
print(round(1234, -1))
print(round(1234, -2))
print(round(1234, -3))
```

```text
1230
1200
1000
```

Una imagen posicional útil es:

```text
ndigits =  2 -> hundredths
ndigits =  1 -> tenths
ndigits =  0 -> units
ndigits = -1 -> tens
ndigits = -2 -> hundreds
```

Un `ndigits` negativo es especialmente útil cuando los valores deben agruparse o presentarse en una escala más amplia.

---

## 14. Python no usa la regla "5 siempre redondea hacia arriba"

Para los casos de `int` y `float` usados en este capítulo, cuando dos múltiplos candidatos están igualmente cerca, Python elige el valor par.

Observa:

```python
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))
```

```text
2
4
4
6
```

El resultado no se basa en subir siempre.

Se eligen las opciones pares más cercanas:

```text
2.5 -> 2
3.5 -> 4
4.5 -> 4
5.5 -> 6
```

La misma idea aparece con valores negativos:

```python
print(round(-0.5))
print(round(-1.5))
print(round(-2.5))
```

```text
0
-2
-2
```

Esta regla suele llamarse redondeo de empates hacia el par.

---

## 15. El desempate hacia el par también importa con `ndigits` negativo

Los enteros proporcionan una forma limpia de observar la regla porque sus valores son exactos.

```python
print(round(125, -1))
print(round(135, -1))
```

```text
120
140
```

`125` está a la misma distancia de `120` y `130`, por lo que la opción de decena par es `120`.

`135` está a la misma distancia de `130` y `140`, por lo que la opción de decena par es `140`.

Este ejemplo evita mezclar la regla de desempate con cuestiones de representación de punto flotante.

---

## 16. `round()` y la representación de punto flotante son ideas separadas

Un ejemplo famoso es:

```python
print(round(2.675, 2))
```

```text
2.67
```

Alguien que espere aritmética decimal común puede predecir `2.68`.

El resultado sorprendente proviene de cómo el literal decimal `2.675` se representa como un `float` binario. El valor almacenado es una aproximación y `round()` opera sobre ese valor realmente almacenado.

Esto no es un error de Python.

Un modelo mental práctico es:

```text
source decimal text
        ↓
nearest representable binary float
        ↓
round() operates on that stored value
```

El capítulo anterior introdujo este problema de representación. Aquí estás viendo una de sus consecuencias.

---

## 17. `round()` no vuelve exacta la aritmética de punto flotante

Considera:

```python
print(0.1 + 0.1 + 0.1 == 0.3)
```

```text
False
```

Redondear previamente los valores individuales no transforma mágicamente su representación interna en fracciones decimales exactas.

```python
print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))
```

```text
False
```

Usa `round()` cuando un valor redondeado sea realmente lo que necesita tu programa. No lo uses como herramienta universal para reparar la aritmética de punto flotante.

Según el requisito, herramientas como `math.isclose()` para comparaciones aproximadas o la aritmética decimal para cálculos basados en decimales pueden ser más adecuadas.

---

## 18. Redondear un valor y formatear una visualización son objetivos diferentes

Supón que quieres mostrar dos lugares decimales.

`round()` cambia el resultado numérico:

```python
value = 3.1
rounded = round(value, 2)
print(rounded)
```

```text
3.1
```

No promete que la impresión mostrará ceros finales como `3.10`.

Eso es una cuestión de formato, no de redondeo numérico.

El formato de strings es un tema separado de este capítulo. Mantén la distinción en mente:

```text
rounding   -> numeric value
formatting -> textual presentation
```

---

## 19. Combinando las cinco funciones incorporadas

Estas funciones son especialmente útiles juntas.

```python
values = [12, -4, 7.5, 3]

print(abs(-12))
print(min(values))
print(max(values))
print(sum(values))
print(round(sum(values), 1))
```

```text
12
-4
12
18.5
18.5
```

El código se lee casi como un pequeño informe:

```text
magnitude
minimum
maximum
total
rounded total
```

Esa legibilidad es una de las razones por las que las funciones incorporadas son preferibles a bucles manuales innecesarios o comparaciones repetidas.

---

## 20. Una vista previa de iterables sin adelantar el aprendizaje de colecciones

`min()`, `max()` y `sum()` reciben iterables con frecuencia.

Este capítulo usa literales de lista como:

```python
values = [10, 20, 30]
```

Todavía no necesitas dominar las listas.

Por ahora, trata la lista como un contenedor ordenado sencillo de valores que puede pasarse a una función.

La Fase 3 enseñará listas, tuplas, diccionarios y conjuntos, incluida la indexación o el slicing cuando el tipo de colección los admita y formas adecuadas de agregar, actualizar o eliminar valores.

Esta pequeña vista previa existe porque sería difícil enseñar `sum()` de forma significativa sin ningún grupo de valores.

---

## 21. Error común: recrear `abs()` manualmente

Un principiante puede intentar reproducir manualmente el comportamiento del valor absoluto comprobando si un valor es negativo y cambiando su signo de forma condicional. Los condicionales se enseñan más adelante en el roadmap. Si la intención real es simplemente obtener el valor absoluto, esto es más claro:

```python
value = -8
magnitude = abs(value)
```

Usa las herramientas estándar cuando expresen directamente el requisito.

---

## 22. Error común: llamar `min()` o `max()` con un iterable vacío

Esto falla:

```python
values = []
minimum = min(values)
```

Antes de elegir una solución, pregunta qué significa una colección vacía en el programa.

Posibles diseños posteriores pueden incluir:

- usar un valor `default=` con sentido semántico;
- verificar si existen datos antes de llamar a la función;
- tratar la entrada vacía como datos inválidos;
- representar explícitamente la ausencia de datos.

No elijas un valor alternativo solo porque evita una excepción.

---

## 23. Error común: confundir `sum(..., start)` con slicing

Esto:

```python
sum([10, 20, 30], 5)
```

significa:

```text
5 + 10 + 20 + 30
```

No significa:

```text
start at index 5
```

El resultado es:

```text
65
```

El nombre del parámetro `start` se refiere al total inicial.

---

## 24. Error común: usar `sum()` para strings

No escribas:

```python
sum(["A", "B", "C"])
```

Usa la operación de strings diseñada para ese propósito:

```python
print("".join(["A", "B", "C"]))
```

```text
ABC
```

Este es un buen ejemplo de elegir una operación según la semántica de los datos, y no solo según la idea de que ambas tareas parecen "combinar" valores.

---

## 25. Error común: asumir que `round()` siempre redondea las mitades hacia arriba

Esta expectativa es incorrecta para el redondeo de `int` y `float` mostrado en este capítulo:

```text
2.5 -> expected by some beginners: 3
```

Resultado real:

```python
print(round(2.5))
```

```text
2
```

Recuerda la regla de desempate hacia el par cuando los candidatos están igualmente cerca.

---

## 26. Error común: usar `round()` para ocultar toda sorpresa con `float`

Si un cálculo depende de semántica decimal exacta, aplicar `round()` repetidamente en pasos intermedios arbitrarios puede crear un problema nuevo en lugar de resolver el original.

La herramienta correcta depende del dominio.

Ejemplos de herramientas y cuestiones fuera del alcance de este capítulo incluyen:

```text
approximate scientific comparison -> math.isclose()
more accurate float summation      -> math.fsum()
decimal arithmetic requirements    -> decimal.Decimal
textual decimal display             -> formatting
```

Estas son referencias de contexto, no requisitos para este capítulo de nivel principiante.

---

## 27. Error común: olvidar que las funciones devuelven valores

Este código calcula un resultado, pero no lo guarda:

```python
round(9.876, 2)
```

En un script, no ocurre nada visible si no usas el valor devuelto.

Puedes imprimirlo:

```python
print(round(9.876, 2))
```

O asignarlo:

```python
rounded_value = round(9.876, 2)
```

El mismo principio se aplica a las cinco funciones incorporadas de este capítulo.

---

## 28. Conexiones con capítulos anteriores

### Variables

Los valores devueltos pueden asignarse a nombres:

```python
maximum_value = max(4, 8, 2)
```

### Tipos

Estas funciones operan sobre valores cuyos tipos importan.

```python
print(type(round(2.5)))
print(type(round(2.5, 0)))
```

```text
<class 'int'>
<class 'float'>
```

### Conversión de tipos

No confundas redondeo con conversión.

```python
print(int(3.9))
print(round(3.9))
```

```text
3
4
```

`int()` convierte truncando hacia cero para un `float` finito. `round()` realiza el redondeo según sus reglas.

### Comportamiento de punto flotante

La explicación del capítulo anterior sobre aproximación binaria es esencial para comprender casos como `round(2.675, 2)`.

### Métodos de strings

`sum()` es agregación numérica; `join()` es la herramienta adecuada para combinar strings.

Estas conexiones son exactamente la razón por la que la guía enseña conceptos como una secuencia, y no como tarjetas de sintaxis aisladas.

---

## 29. Ejercicio práctico: informe numérico

Crea un archivo llamado `numeric_report.py`.

Comienza con:

```python
measurements = [12.5, -3.2, 8.75, 4.0]
```

Produce estos resultados usando las funciones incorporadas de este capítulo:

1. la medición más pequeña;
2. la medición más grande;
3. el total;
4. el valor absoluto de la medición más pequeña;
5. el total redondeado a un decimal;
6. la amplitud del rango, calculada como máximo menos mínimo.

Tu salida debe tener esta forma:

```text
Minimum: -3.2
Maximum: 12.5
Total: 22.05
Minimum magnitude: 3.2
Rounded total: 22.1
Range width: 15.7
```

No ordenes ni compares manualmente los valores uno por uno.

### Ejercicio adicional

Agrega:

```python
empty_measurements = []
```

Usa `min()` y `max()` con un `default=` explícito y escribe una o dos frases debajo del código explicando por qué el valor elegido tendría o no sentido semántico en un sistema real de mediciones.

La parte importante es el razonamiento, no solo evitar `ValueError`.

---

## 30. Autoevaluación

Intenta responder sin ejecutar Python primero.

1. ¿Qué devuelve `abs(-9)`?
2. ¿`abs()` modifica la variable original?
3. ¿Qué ocurre cuando se llama `min([])` sin `default=`?
4. ¿Qué devuelve `sum([], 10)`?
5. ¿Qué significa el segundo argumento de `sum()`?
6. ¿Por qué las strings normalmente deben usar `join()` en lugar de `sum()`?
7. ¿Qué devuelve `round(2.5)`?
8. ¿Por qué `round(2.675, 2)` puede producir `2.67`?
9. ¿Qué hace `round(1234, -2)`?
10. ¿Cuál es la diferencia de tipo entre `round(2.5)` y `round(2.5, 0)`?
11. ¿Por qué `min()` y `max()` pueden comparar valores `int` y `float`, pero pueden rechazar un `int` y una `str` sin relación?
12. ¿`round()` vuelve exactos todos los cálculos de punto flotante?

### Respuestas sugeridas

1. `9`.
2. No. Devuelve un valor de resultado.
3. Se genera `ValueError`.
4. `10`.
5. Es el total inicial que se suma a los elementos del iterable.
6. `sum()` es para agregación numérica, mientras que `join()` está diseñado para combinar strings.
7. `2`, porque un empate exacto se resuelve hacia el candidato par.
8. Porque el `float` binario almacenado es una aproximación del literal decimal.
9. Redondea a la posición de centenas y produce `1200`.
10. El primero es `int`; con `ndigits` explícito, el resultado del `float` incorporado permanece `float`.
11. Los tipos numéricos tienen semántica de orden compatible, mientras que tipos sin relación pueden no definir una relación de orden.
12. No.

---

## 31. Referencia rápida

| Objetivo | Herramienta | Ejemplo | Resultado |
|---|---|---|---|
| Magnitud absoluta | `abs()` | `abs(-8)` | `8` |
| Argumento más pequeño | `min()` | `min(8, 2, 5)` | `2` |
| Argumento más grande | `max()` | `max(8, 2, 5)` | `8` |
| Menor elemento del iterable | `min()` | `min([8, 2, 5])` | `2` |
| Mayor elemento del iterable | `max()` | `max([8, 2, 5])` | `8` |
| Alternativa para iterable vacío | `min()` | `min([], default=0)` | `0` |
| Total numérico | `sum()` | `sum([8, 2, 5])` | `15` |
| Total con valor inicial | `sum()` | `sum([8, 2, 5], 10)` | `25` |
| Entero más cercano | `round()` | `round(3.6)` | `4` |
| Redondeo decimal | `round()` | `round(3.14159, 2)` | `3.14` |
| Redondeo a decenas | `round()` | `round(125, -1)` | `120` |

---

## 32. Ejemplos del repositorio

Ejecuta los ejemplos deterministas desde la raíz del repositorio:

```bash
python strings-and-numbers/04-numeric-builtins/examples/numeric_summary.py
python strings-and-numbers/04-numeric-builtins/examples/rounding_behavior.py
```

Salida esperada de `numeric_summary.py`:

```text
Absolute: 12
Minimum: -4
Maximum: 12
Total: 18.5
Total with start: 28.5
```

Salida esperada de `rounding_behavior.py`:

```text
2.5: 2
3.5: 4
125 to tens: 120
135 to tens: 140
2.675 to two decimals: 2.67
Type without ndigits: <class 'int'>
Type with ndigits: <class 'float'>
```

---

## 33. Fase 2 completada

Con este capítulo, la Fase 2 cubrió:

```text
string creation and indexing
        ↓
common string methods
        ↓
int, float, and bool behavior
        ↓
common numeric built-ins
```

Ahora tienes una base más sólida para trabajar con valores individuales de texto y números.

La siguiente fase curricular introduce **Colecciones**, donde múltiples valores pasan a convertirse en estructuras de primera clase en tus programas. Listas, tuplas, conjuntos y diccionarios harán mucho más poderosos varios patrones anticipados en esta fase.


---

## Referencias oficiales

- [Funciones incorporadas](https://docs.python.org/3/library/functions.html)
- [`abs()`](https://docs.python.org/3/library/functions.html#abs)
- [`max()`](https://docs.python.org/3/library/functions.html#max)
- [`min()`](https://docs.python.org/3/library/functions.html#min)
- [`round()`](https://docs.python.org/3/library/functions.html#round)
- [`sum()`](https://docs.python.org/3/library/functions.html#sum)
- [Aritmética de punto flotante: problemas y limitaciones](https://docs.python.org/3/tutorial/floatingpoint.html)

---

## Siguiente paso

La Fase 2 está completada. Continúa con el [roadmap principal](../../docs/roadmap.es.md) para revisar la fase completada y ver la **Fase 3: Colecciones**, planificada a continuación.
