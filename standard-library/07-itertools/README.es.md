<div align="center">

# Diseñando Pipelines Lazy de Iteradores con `itertools`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Standard Library](../README.es.md) · [← Capítulo anterior: Collections](../06-collections/README.es.md)

Los capítulos anteriores introdujeron `for`, iterables, la diferencia básica entre iterable e iterator y helpers como `range()`, `enumerate()` y `zip()`. Este capítulo va más allá: estudia `itertools` como una caja de herramientas para componer **pipelines lazy de iteradores** con contratos explícitos de consumo, buffering, agrupación y combinatoria.

La pregunta central es:

```text
Can this transformation be expressed as a stream of values
without materializing every intermediate collection?
```

`itertools` es potente porque sus funciones devuelven iteradores. Eso puede reducir el uso de memoria intermedia y hacer más preciso el flujo de datos, pero también significa que el orden de consumo importa.

**Tiempo estimado de estudio:** 170–220 minutos.

**Requisito de Python:** Python 3.10 o más reciente para el contenido central y los ejemplos ejecutables. Las secciones sensibles a versión identifican `batched()` (3.12) y `batched(strict=...)` (3.13).

**Base documental:** los comportamientos y notas de versión se verificaron contra la documentación oficial de Python 3.14 para `itertools` y el Functional Programming HOWTO.

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- explicar por qué `itertools` es una caja de herramientas de álgebra de iteradores y no un módulo de colecciones;
- distinguir construcción lazy de pipelines de materialización eager;
- razonar sobre el consumo single-pass de iteradores;
- combinar streams con `chain()` y `chain.from_iterable()`;
- agrupar entradas finitas en lotes y entender los requisitos de versión de `batched(strict=...)`;
- cortar streams con `islice()` sin asumir semántica de secuencia;
- comparar elementos vecinos con `pairwise()`;
- seleccionar elementos con `compress()`, `filterfalse()`, `dropwhile()` y `takewhile()`;
- construir estado acumulado con `accumulate()`;
- aplicar tuplas de argumentos preagrupadas con `starmap()`;
- limitar iteradores infinitos como `count()`, `cycle()` y `repeat()`;
- alinear streams de longitudes distintas con `zip_longest()`;
- entender el buffering y las limitaciones de thread safety de `tee()`;
- usar `groupby()` para runs consecutivos en lugar de agrupación global estilo SQL;
- estimar el crecimiento de `product()`, `permutations()` y combinations antes de consumirlos;
- probar pipelines de iteradores sin ocultar accidentalmente bugs de consumo.

## 1. Qué añade este capítulo después de los capítulos anteriores de iteración

Los capítulos anteriores ya establecieron:

```text
for item in iterable
range() -> numeric progression
enumerate() -> position + item
zip() -> parallel items
```

Este capítulo añade un modelo más composicional:

```text
source
  -> transform lazily
  -> select lazily
  -> combine lazily
  -> consume at an intentional boundary
```

El objetivo no es reemplazar loops legibles. Es reconocer cuándo un pipeline expresa el flujo de datos de forma más directa.

## 2. Las funciones de `itertools` construyen iteradores

La documentación oficial describe el módulo como un conjunto de building blocks de iteradores rápidos y eficientes en memoria.

```python
from itertools import islice

numbers = iter(range(100))
first_five = islice(numbers, 5)

print(type(first_five))
```

`islice()` no devuelve una lista. Devuelve un iterador que produce valores cuando es consumido.

## 3. Lazy no significa sin coste

Laziness normalmente significa que el trabajo se pospone hasta que la iteración pide un valor.

```python
from itertools import chain

stream = chain([1, 2], [3, 4])
print(next(stream))
```

Solo se realiza el trabajo suficiente para entregar el valor solicitado.

Aun así, los pipelines lazy pueden:

- consumir CPU;
- retener valores en buffer;
- mantener referencias a objetos;
- materializar datos más tarde en un consumidor;
- volverse infinitos.

"Lazy" describe el momento de evaluación, no coste cero.

## 4. Los iteradores normalmente son single-pass

```python
values = iter([10, 20, 30])

print(list(values))
print(list(values))
```

Salida:

```text
[10, 20, 30]
[]
```

La primera conversión agota el iterador. La segunda no encuentra valores restantes.

Este modelo de consumo es central en `itertools`.

## 5. Elige deliberadamente la frontera de materialización

Un pipeline útil suele permanecer lazy hasta que el programa necesita un resultado concreto:

```python
from itertools import islice

stream = (number * number for number in range(1_000_000))
preview = list(islice(stream, 3))
print(preview)
```

Aquí solo se materializa el preview.

Materializa porque la siguiente operación necesita una colección, no solo porque `list(...)` resulte familiar.

## 6. Importa las herramientas que comuniquen el pipeline

```python
from itertools import (
    accumulate,
    chain,
    combinations,
    groupby,
    islice,
    pairwise,
    product,
    tee,
    zip_longest,
)
```

Imports específicos hacen visible el vocabulario del pipeline.

# Parte I: componiendo y dando forma a streams

## 7. `chain()` concatena iterables de forma lazy

```python
from itertools import chain

combined = chain(["a", "b"], ("c", "d"), "ef")
print(list(combined))
```

Salida:

```text
['a', 'b', 'c', 'd', 'e', 'f']
```

`chain()` consume el primer iterable, luego el siguiente y así sucesivamente.

## 8. `chain()` no es un algoritmo de merge

`chain()` no ordena, deduplica, alinea ni compara entradas.

```text
input A -> all values
input B -> all values
input C -> all values
```

Si el requisito real es un merge ordenado o reconciliación por clave, elige una herramienta que modele ese contrato.

## 9. `chain.from_iterable()` aplana un nivel

```python
from itertools import chain

pages = [[1, 2], [3], [4, 5]]
flattened = chain.from_iterable(pages)
print(list(flattened))
```

Salida:

```text
[1, 2, 3, 4, 5]
```

Aplana un nivel de iterable-of-iterables. No es una función recursiva para flattening de profundidad arbitraria.

## 10. `chain.from_iterable()` mantiene lazy la fuente externa

El iterable externo también puede ser lazy:

```python
from itertools import chain

rows = ([number, number * 10] for number in range(3))
print(list(chain.from_iterable(rows)))
```

El siguiente iterable interno se solicita a medida que la chain avanza.

## 11. `batched()` crea tuplas no solapadas

Python 3.12 añadió `itertools.batched()`:

```python
from itertools import batched

print(list(batched("ABCDEFG", 3)))
```

En Python 3.12+, el resultado es:

```text
[('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
```

El lote final puede ser más corto que `n`.

## 12. `batched(strict=True)` convierte lotes completos en contrato

Python 3.13 añadió el parámetro `strict`:

```python
from itertools import batched

print(list(batched([1, 2, 3, 4], 2, strict=True)))
```

Si el lote final está incompleto, `strict=True` lanza `ValueError`.

Usa modo estricto cuando datos incompletos deban tratarse como inválidos y no como un lote más pequeño válido.

## 13. `batched()` consume solo lo necesario para el siguiente lote

La implementación es lazy respecto a la entrada. Solicita suficientes valores para llenar la siguiente tupla, entrega el lote y continúa.

Eso hace batching adecuado para streams donde construir una lista completa primero sería innecesario.

## 14. `islice()` corta iterables, no secuencias

```python
from itertools import islice

stream = iter(range(20))
print(list(islice(stream, 2, 10, 3)))
```

Salida:

```text
[2, 5, 8]
```

`islice()` expresa start, stop y step sobre iteración.

## 15. `islice()` no admite índices negativos

El slicing de secuencias puede trabajar desde el final porque una secuencia puede conocer su longitud y ofrecer acceso indexado.

Un iterador arbitrario puede ni siquiera tener un final conocido.

Por eso `start` negativo, `stop` negativo y `step` no positivo no están soportados por `islice()`.

## 16. Cortar un stream avanza la fuente

```python
from itertools import islice

source = iter([0, 1, 2, 3, 4, 5])
print(list(islice(source, 3)))
print(list(source))
```

Salida:

```text
[0, 1, 2]
[3, 4, 5]
```

`islice()` no copia el iterador de entrada. Lo consume.

## 17. Un `islice()` con step sigue consumiendo valores omitidos

Si la entrada es un iterador, consumir completamente un `islice()` avanza la entrada según los límites del slice, aunque no todos los valores atravesados se entreguen.

Esto importa cuando otra parte del programa continúa usando el mismo iterador subyacente después.

## 18. `pairwise()` expone relaciones adyacentes

Python 3.10 añadió `pairwise()`:

```python
from itertools import pairwise

readings = [10, 15, 13, 18]
for previous, current in pairwise(readings):
    print(previous, current)
```

Salida:

```text
10 15
15 13
13 18
```

Es ideal para transiciones, deltas, aristas y comparaciones adyacentes.

## 19. `pairwise()` produce un resultado menos

Una entrada con `n` valores produce `n - 1` pares cuando `n >= 1`.

Entradas con menos de dos elementos no producen pares.

Ese comportamiento de frontera debería formar parte de los tests cuando la cantidad de pares importe.

# Parte II: seleccionando y deteniendo

## 20. `compress()` aplica un stream de selectores Booleanos

```python
from itertools import compress

names = ["Ana", "Bo", "Cy", "Di"]
selected = [True, False, True, False]
print(list(compress(names, selected)))
```

Salida:

```text
['Ana', 'Cy']
```

Los iterables de datos y selectores avanzan juntos.

## 21. `compress()` se detiene cuando termina cualquiera de las entradas

Un stream de selectores más corto trunca el resultado aunque todavía queden datos.

Ese es un contrato de alineación parecido al de `zip()`. Valida longitudes por separado si tamaños distintos representan entrada malformada.

## 22. `filterfalse()` conserva fallos del predicado

```python
from itertools import filterfalse

numbers = [1, 2, 3, 4, 5]
print(list(filterfalse(lambda value: value % 2 == 0, numbers)))
```

Salida:

```text
[1, 3, 5]
```

Es la contraparte de selección inversa de `filter()`.

## 23. `dropwhile()` cambia de comportamiento después del primer fallo

```python
from itertools import dropwhile

values = [1, 2, 5, 2, 1]
print(list(dropwhile(lambda value: value < 4, values)))
```

Salida:

```text
[5, 2, 1]
```

Después de que el predicado se vuelve falso por primera vez, todos los elementos restantes se entregan sin filtrado adicional.

## 24. `dropwhile()` no es `filterfalse()`

Para el mismo predicado:

```text
dropwhile -> discard only the leading matching prefix
filterfalse -> test every element and keep every failure
```

Los nombres representan formas de stream diferentes.

## 25. `takewhile()` se detiene en el primer fallo

```python
from itertools import takewhile

values = [1, 2, 5, 2, 1]
print(list(takewhile(lambda value: value < 4, values)))
```

Salida:

```text
[1, 2]
```

A diferencia de `filter()`, los valores después del primer fallo nunca son considerados por `takewhile()`.

## 26. `takewhile()` consume el primer elemento que falla

Este es un contrato sutil e importante.

```python
from itertools import takewhile

source = iter([1, 2, 5, 6])
print(list(takewhile(lambda value: value < 4, source)))
print(list(source))
```

Salida:

```text
[1, 2]
[6]
```

El `5` que falló fue consumido para descubrir que el prefijo debía terminar.

# Parte III: estado acumulado y aplicación de argumentos

## 27. `accumulate()` entrega resultados acumulados

```python
from itertools import accumulate

print(list(accumulate([2, 3, 4])))
```

Salida:

```text
[2, 5, 9]
```

La operación por defecto es suma.

## 28. `accumulate()` difiere de `sum()` y `reduce()`

```text
accumulate -> every running result
sum        -> final additive total
reduce     -> final accumulated result
```

Elige según si los estados intermedios forman parte o no de la salida requerida.

## 29. `accumulate()` acepta otra función binaria

```python
from itertools import accumulate

values = [3, 1, 5, 2]
print(list(accumulate(values, max)))
```

Salida:

```text
[3, 3, 5, 5]
```

Mínimos, máximos, productos, saldos y transiciones de estado pueden seguir el mismo contrato.

## 30. `initial=` cambia tanto el estado como la longitud de salida

```python
from itertools import accumulate

print(list(accumulate([1, 2, 3], initial=10)))
```

Salida:

```text
[10, 11, 13, 16]
```

Con `initial`, el valor inicial se entrega primero, así que la salida tiene un elemento más que la entrada.

## 31. La función de acumulación recibe estado y luego elemento

Conceptualmente:

```text
new_state = function(previous_state, next_element)
```

El orden de argumentos importa cuando la función no es conmutativa.

## 32. `starmap()` desempaqueta tuplas de argumentos

```python
from itertools import starmap

arguments = [(2, 5), (3, 2), (10, 3)]
print(list(starmap(pow, arguments)))
```

Salida:

```text
[32, 9, 1000]
```

Es útil cuando un iterable ya contiene tuplas de argumentos.

## 33. `map()` y `starmap()` modelan formas de entrada diferentes

```text
map(function, a, b)       -> function(a_item, b_item)
starmap(function, tuples) -> function(*tuple_item)
```

Elige según cómo se representen los argumentos upstream.

# Parte IV: iteradores infinitos

## 34. Los iteradores infinitos exigen un diseño de terminación

`count()`, `cycle()` y `repeat()` pueden producir valores indefinidamente.

Una fuente infinita no es peligrosa por sí misma. El problema es un **consumidor sin límite**.

Diseña el límite antes de consumir el stream.

## 35. `count()` crea una progresión aritmética

```python
from itertools import count, islice

numbers = count(10, 3)
print(list(islice(numbers, 5)))
```

Salida:

```text
[10, 13, 16, 19, 22]
```

`count()` es útil cuando la progresión debe permanecer como iterador.

## 36. `count()` con float puede acumular error

La documentación oficial indica que a veces puede lograrse mejor precisión de punto flotante derivando cada valor de un índice entero:

```python
from itertools import count, islice

values = (0.1 * index for index in count())
print(list(islice(values, 4)))
```

Para reglas que requieran decimal exacto, el próximo capítulo introducirá `decimal`.

## 37. `repeat()` proporciona un stream constante

```python
from itertools import repeat

print(list(repeat("x", 3)))
```

Salida:

```text
['x', 'x', 'x']
```

Sin el segundo argumento, la repetición es infinita.

## 38. `repeat()` compone naturalmente con `map()`

```python
from itertools import repeat

print(list(map(pow, [2, 3, 4], repeat(2))))
```

Salida:

```text
[4, 9, 16]
```

La constante repetida proporciona el mismo exponente a cada llamada.

## 39. `cycle()` repite indefinidamente la secuencia de entrada

```python
from itertools import cycle, islice

rotating = cycle(["A", "B", "C"])
print(list(islice(rotating, 7)))
```

Salida:

```text
['A', 'B', 'C', 'A', 'B', 'C', 'A']
```

## 40. `cycle()` almacena valores de entrada para repeticiones futuras

Para repetir un iterable arbitrario, `cycle()` guarda los valores a medida que los encuentra.

Por eso su memoria auxiliar puede crecer con el tamaño de la entrada finita original.

No interpretes automáticamente "iterator" como "memoria constante".

## 41. Limita streams infinitos cerca de la fuente

Un patrón legible es:

```python
from itertools import count, islice

limited = islice(count(1), 5)
print(list(limited))
```

Poner el límite cerca del productor infinito hace la terminación más fácil de auditar.

# Parte V: alineación y fan-out

## 42. `zip_longest()` alinea hasta que termina la entrada más larga

```python
from itertools import zip_longest

left = [1, 2, 3]
right = ["a"]
print(list(zip_longest(left, right, fillvalue="-")))
```

Salida:

```text
[(1, 'a'), (2, '-'), (3, '-')]
```

Esto contrasta con `zip()` normal, que se detiene en el iterable más corto.

## 43. `zip_longest()` y `zip(strict=True)` representan políticas distintas

```text
zip()                -> shortest wins
zip(strict=True)     -> unequal lengths are invalid
zip_longest()        -> longest wins; missing values are filled
```

Elige la política que corresponda al contrato de los datos, en lugar de reparar diferencias después.

## 44. Una entrada infinita puede volver infinito a `zip_longest()`

Si cualquier entrada puede continuar para siempre, `zip_longest()` también puede continuar para siempre.

Envuelve el resultado con una herramienta limitadora como `islice()` cuando el consumidor deba ser finito.

## 45. `tee()` crea vistas independientes del iterador

```python
from itertools import tee

source = iter([10, 20, 30])
left, right = tee(source, 2)

print(next(left))
print(list(right))
print(list(left))
```

Salida:

```text
10
[10, 20, 30]
[20, 30]
```

Cada iterador devuelto tiene su propia posición lógica.

## 46. La independencia de `tee()` exige buffering

Si una branch avanza más rápido, `tee()` debe retener valores hasta que las branches más lentas los consuman.

El coste de memoria depende entonces de cuánto diverjan los consumidores.

## 47. Prefiere materialización cuando los consumidores estén muy separados

La documentación oficial señala que si una branch consume casi todos o todos los datos antes de que otra empiece, convertir a lista puede ser más rápido que `tee()`.

`tee()` es valioso para consumidores streaming coordinados, no automáticamente para cualquier necesidad de "usar dos veces".

## 48. Los iteradores de `tee()` no son thread-safe

El uso simultáneo de iteradores devueltos por la misma llamada a `tee()` no es thread-safe y puede lanzar `RuntimeError`.

No trates `tee()` como una primitiva de concurrencia.

## 49. Evita mezclar el iterador original con sus branches de tee

Después de crear las branches, continúa consumiendo a través de ellas en lugar de seguir usando el iterador original en código independiente.

Un único camino de ownership hace mucho más fácil razonar sobre buffering y consumo.

# Parte VI: agrupando runs consecutivos

## 50. `groupby()` agrupa claves iguales consecutivas

```python
from itertools import groupby

values = ["A", "A", "B", "B", "A"]
for key, group in groupby(values):
    print(key, list(group))
```

Salida:

```text
A ['A', 'A']
B ['B', 'B']
A ['A']
```

El `A` final inicia un grupo nuevo porque no está adyacente al primer run de `A`.

## 51. `groupby()` no es `GROUP BY` de SQL

La agrupación estilo SQL normalmente reúne todas las filas que comparten clave, independientemente de su posición.

`itertools.groupby()` inicia un grupo nuevo cada vez que cambia la clave.

Piensa en **runs**, no en buckets globales.

## 52. Ordena primero cuando quieras agrupar globalmente por clave

```python
from itertools import groupby
from operator import itemgetter

records = [("b", 2), ("a", 1), ("b", 3)]
records.sort(key=itemgetter(0))

for key, group in groupby(records, key=itemgetter(0)):
    print(key, list(group))
```

Ordenar por la misma función de clave aproxima las claves iguales antes de agrupar.

## 53. Los iteradores de grupo comparten la fuente subyacente

El `group` devuelto por `groupby()` es en sí mismo un iterador sobre la entrada compartida.

Cuando el `groupby()` externo avanza, un grupo anterior puede dejar de estar disponible.

Materializa un grupo si debe sobrevivir más allá de la iteración externa actual.

## 54. `groupby()` puede expresar run-length encoding

```python
from itertools import groupby

values = "AAABBCCCCA"
runs = [(key, len(list(group))) for key, group in groupby(values)]
print(runs)
```

Salida:

```text
[('A', 3), ('B', 2), ('C', 4), ('A', 1)]
```

Esto preserva los límites de los runs en lugar de colapsar todos los valores iguales.

# Parte VII: iteradores combinatorios

## 55. `product()` modela un producto cartesiano

```python
from itertools import product

print(list(product(["A", "B"], [1, 2])))
```

Salida:

```text
[('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

En significado equivale a loops anidados sobre cada pool de entrada.

## 56. `product()` consume pools de entrada antes de producir combinaciones

Aunque `product()` devuelve un iterador, primero consume cada iterable de entrada en pools mantenidos en memoria.

Por lo tanto requiere entradas finitas, y su comportamiento de memoria del lado de entrada difiere de herramientas como `chain()`.

## 57. `repeat=` multiplica dimensiones del producto

```python
from itertools import product

print(list(product([0, 1], repeat=2)))
```

Salida:

```text
[(0, 0), (0, 1), (1, 0), (1, 1)]
```

La cantidad de resultados crece multiplicativamente con cada dimensión.

## 58. `permutations()` modela selecciones ordenadas

```python
from itertools import permutations

print(list(permutations("ABC", 2)))
```

Salida:

```text
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

El orden importa y las posiciones no se reutilizan dentro de una misma permutación.

## 59. La unicidad combinatoria es posicional

Si valores iguales aparecen en posiciones distintas de la entrada, las herramientas siguen tratando esas posiciones como elecciones diferentes.

No asumas que valores duplicados en la entrada producirán automáticamente tuplas de salida deduplicadas.

## 60. `combinations()` ignora el orden dentro del subconjunto elegido

```python
from itertools import combinations

print(list(combinations("ABC", 2)))
```

Salida:

```text
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

`('B', 'A')` no es otra combinación porque esas mismas dos posiciones ya fueron elegidas.

## 61. `combinations_with_replacement()` permite reutilizar posiciones

```python
from itertools import combinations_with_replacement

print(list(combinations_with_replacement("AB", 2)))
```

Salida:

```text
[('A', 'A'), ('A', 'B'), ('B', 'B')]
```

Es útil cuando repetir una elección está permitido y el orden no crea un resultado nuevo.

## 62. Estima la cardinalidad antes de consumir

Entradas pequeñas pueden producir salidas enormes rápidamente.

Fórmulas útiles incluyen:

```text
product sizes       -> multiply pool sizes
permutations(n, r)  -> n! / (n-r)!
combinations(n, r)  -> n! / (r! * (n-r)!)
```

`math.perm()` y `math.comb()` pueden estimar dos de esas cantidades sin generar las tuplas.

## 63. Un iterador aún puede representar un cálculo enorme

Entregar valores de forma lazy evita crear automáticamente una lista gigante de resultados, pero no reduce el número de combinaciones que deben generarse si consumes todas.

Laziness protege almacenamiento intermedio, no elimina la complejidad algorítmica.

# Parte VIII: diseño de pipelines

## 64. Compón de izquierda a derecha alrededor de una fuente clara

```python
from itertools import chain, islice

pages = [[1, 2], [3, 4], [5, 6]]
stream = chain.from_iterable(pages)
preview = islice(stream, 4)
print(list(preview))
```

Salida:

```text
[1, 2, 3, 4]
```

Cada etapa responde una pregunta: aplanar, limitar, consumir.

## 65. Las generator expressions y `itertools` se complementan

```python
from itertools import islice

squares = (number * number for number in range(100))
print(list(islice(squares, 5)))
```

Usa generator expressions para expresiones personalizadas simples e `itertools` para patrones reutilizables de iteración.

## 66. No comprimas todos los loops en un pipeline

Un loop de varios pasos puede ser más claro cuando contiene:

- branching complejo;
- varios efectos secundarios;
- manejo de errores por item;
- estado mutable que merece nombres explícitos.

El estilo pipeline es una opción de diseño, no una obligación de code golf.

## 67. Nombra las etapas significativas

Prefiere:

```python
from itertools import chain, islice

rows = [[1, 2], [3], [4, 5]]
flattened = chain.from_iterable(rows)
preview = islice(flattened, 3)
print(list(preview))
```

a una expresión profundamente anidada cuando nombres intermedios expliquen el modelo.

## 68. Documenta el ownership de iteradores compartidos

Cuando varios helpers consumen el mismo iterador, deja claro qué etapa posee el siguiente valor.

Los bugs con `takewhile()`, `islice()`, `groupby()` o `tee()` suelen ser bugs de consumo y no de aritmética.

## 69. Prueba consumo parcial, no solo listas finales

Un test útil puede inspeccionar lo que queda:

```python
from itertools import islice

source = iter([1, 2, 3, 4])
assert list(islice(source, 2)) == [1, 2]
assert list(source) == [3, 4]
```

Eso verifica directamente el contrato de consumo.

## 70. Limita explícitamente los tests infinitos

Nunca escribas un test que intente materializar un iterador infinito.

Usa `islice()`, un `repeat(..., times)` finito u otra condición explícita de parada.

## 71. Cuatro ejemplos ejecutables en este capítulo

El directorio `examples/` contiene programas deterministas:

```text
lazy_pipeline.py
pairwise_deltas.py
groupby_runs.py
combinatoric_options.py
```

Son suficientemente pequeños para CI no interactivo y usan APIs de `itertools` compatibles con Python 3.10.

## 72. Errores comunes

### Error 1: materializar todas las etapas

```python
values = list(range(1_000_000))
```

cuando el consumidor solo necesita un prefijo corto.

Mejor: conserva laziness hasta que realmente se necesite una colección concreta.

### Error 2: reutilizar un iterador agotado

Un iterador consumido no se reinicia automáticamente.

### Error 3: esperar que `groupby()` reúna claves iguales no adyacentes

Agrupa runs consecutivos.

### Error 4: olvidar que `takewhile()` consume el valor que falla

Ese valor no queda disponible para un consumidor posterior de la misma fuente.

### Error 5: asumir que `tee()` duplica datos gratis

Branches rezagadas provocan buffering.

### Error 6: usar un iterador infinito sin un límite visible

El pipeline puede no terminar nunca.

### Error 7: tratar combinatoria lazy como combinatoria barata

La cantidad de resultados aún puede explotar.

### Error 8: usar `islice()` como slicing normal de secuencia

Índices negativos no están soportados y los elementos recorridos se consumen.

## 73. Ejercicio práctico

Construye un pequeño pipeline de análisis de eventos.

Requisitos:

1. Empieza con varias páginas de mediciones enteras representadas como una lista de listas.
2. Aplana un nivel con `chain.from_iterable()`.
3. Usa `islice()` para inspeccionar solo las primeras ocho mediciones.
4. Usa `pairwise()` para calcular diferencias adyacentes.
5. Clasifica cada diferencia como `"up"`, `"down"` o `"same"`.
6. Usa `groupby()` para resumir runs consecutivos de clasificaciones.
7. No materialices toda la fuente aplanada antes de la frontera de preview.

Bonus: explica qué etapas consumen su entrada y dónde ocurre la materialización.

## 74. Referencia rápida

```text
chain(a, b, c)                  concatenate iterables
chain.from_iterable(rows)       flatten one level
batched(iterable, n)            non-overlapping batches [Python 3.12+]
batched(..., strict=True)       require complete batches [Python 3.13+]
islice(iterable, ...)           lazy positive slicing
pairwise(iterable)              adjacent pairs
compress(data, selectors)       Boolean-mask selection
filterfalse(predicate, items)   keep predicate failures
dropwhile(predicate, items)     drop leading matching prefix
takewhile(predicate, items)     keep leading matching prefix
accumulate(items, func)         running state
starmap(func, argument_tuples)  call func(*args)
count(start, step)              infinite arithmetic progression
cycle(iterable)                 repeat saved input indefinitely
repeat(value, times=None)       repeat one object
zip_longest(..., fillvalue=x)   align until longest input ends
tee(iterable, n)                fork logical iterator positions
groupby(iterable, key)          group consecutive equal keys
product(...)                    Cartesian product
permutations(items, r)          ordered selections
combinations(items, r)          unordered selections
combinations_with_replacement   unordered selections with reuse
```

## 75. Checklist de diseño

Antes de añadir una etapa de `itertools`, pregúntate:

- ¿La fuente es finita o potencialmente infinita?
- ¿Quién posee el consumo de este iterador?
- ¿La etapa es lazy, usa buffer o materializa internamente la entrada?
- ¿Otro consumidor necesitará los valores después?
- ¿Un helper de frontera consume un sentinel o valor que falla?
- ¿Entradas de longitudes distintas deben truncar, fallar o rellenar?
- ¿La agrupación es consecutiva o global?
- ¿La divergencia entre branches puede volver caro a `tee()`?
- ¿Cuántos resultados combinatorios puede generar esta solicitud?
- ¿Dónde debe el pipeline convertirse en una colección concreta?
- ¿Un loop explícito sería más fácil de entender?
- ¿Estoy dependiendo de una API sensible a versión?

## 76. Conexiones con otros conceptos de Python

`itertools` se conecta directamente con temas ya estudiados:

- **loops `for` e iteración:** cada itertool participa del protocolo de iteradores de Python.
- **`range()`, `enumerate()` y `zip()`:** estos built-ins son vecinos naturales de los pipelines de iteradores.
- **funciones:** predicados, funciones de clave y funciones binarias de acumulación se pasan como comportamiento.
- **colecciones:** `chain()` recorre contenedores; `groupby()` expone iteradores de grupo; herramientas combinatorias suelen crear pools de entradas finitas.
- **generators:** generator expressions y etapas de itertools componen naturalmente sin listas intermedias eager.
- **algoritmos:** laziness cambia el comportamiento de almacenamiento, pero no borra complejidad temporal ni crecimiento combinatorio.
- **tests:** ownership y comportamiento de consumo parcial son contratos que vale la pena afirmar directamente.
- **próximo `decimal`:** la aritmética exacta se vuelve importante cuando pipelines numéricos representan dinero u otros valores sensibles a precisión.

## Referencias

Referencias primarias usadas en este capítulo:

- [Documentación Python 3.14: `itertools` — funciones que crean iteradores para bucles eficientes](https://docs.python.org/3.14/library/itertools.html)
- [Python 3.14 Functional Programming HOWTO — iteradores, generators e `itertools`](https://docs.python.org/3.14/howto/functional.html)
- [Documentación Python 3.14 del built-in `zip()`, incluido `strict=True`](https://docs.python.org/3.14/library/functions.html#zip)
- [Documentación Python 3.14 de `math.comb()` y `math.perm()`](https://docs.python.org/3.14/library/math.html#combinatorics)

## Próximo capítulo

Continúa con el **Capítulo 08: `decimal`** cuando esté disponible.

El próximo capítulo cambia de contratos de iteración lazy a **contratos de precisión numérica**: representación decimal, contexts, rounding, traps, cuantización y aritmética exacta para valores donde el comportamiento binario de punto flotante no es el modelo deseado.
