<div align="center">

# Trabajando con Datos Tabulares Usando `pandas`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Bibliotecas Externas](../README.es.md) · [← Fase anterior: `os` + `shutil`](../../standard-library/09-os-shutil/README.es.md)

La Fase 9 comienza donde termina la biblioteca estándar: incorporando paquetes de terceros con sus propios ciclos de lanzamiento, contratos de dependencias y abstracciones específicas de dominio.

`pandas` es la primera biblioteca externa porque se conecta directamente con conceptos ya estudiados: listas, diccionarios, CSV, JSON, fechas, archivos, funciones, excepciones, rutas y validación de datos. El nuevo desafío no es solo aprender métodos. Es aprender a preservar la **semántica de la tabla** mientras las transformaciones se vuelven más expresivas.

Este capítulo apunta a **pandas 3.0.x** y fue investigado usando la documentación oficial de pandas **3.0.5**. pandas 3.0 es compatible con Python 3.11 o superior.

**Tiempo estimado de estudio:** 240–330 minutos.

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- explicar cuándo pandas es más apropiado que las colecciones incorporadas;
- crear e inspeccionar objetos `Series` y `DataFrame`;
- razonar sobre índices, labels, alineación, columnas y dtypes;
- seleccionar filas y columnas con corchetes, `.loc` y `.iloc`;
- construir máscaras booleanas y actualizar filas de forma segura;
- comprender Copy-on-Write en pandas 3.0 y por qué chained assignment no es válido;
- tratar valores ausentes con una política explícita;
- convertir columnas numéricas, de texto y datetime deliberadamente;
- agregar con `groupby()`, `agg()` y `transform()`;
- combinar tablas con `merge()` validado y `concat()`;
- remodelar datos con `pivot_table()` y `melt()`;
- cargar y guardar CSV con decisiones explícitas de schema;
- preferir operaciones vectorizadas cuando expresan el problema;
- reconocer cuándo `apply()` y la iteración por filas no son buenos valores predeterminados;
- construir pipelines de datos tabulares deterministas y revisables.

## 1. Por qué existe `pandas`

`pandas` es una biblioteca de terceros para datos etiquetados y tabulares. Es especialmente útil cuando los datos tienen filas, columnas, etiquetas, valores ausentes, tipos diferentes por columna o requieren filtrado, agrupación, joins, reshape y entrada/salida mediante archivos.

No sustituye las colecciones de Python. Una lista o un diccionario suele ser mejor para pequeños estados de aplicación. `pandas` resulta atractivo cuando el problema es principalmente una tabla y las operaciones se aplican a columnas o grupos de filas.

## 2. Las bibliotecas externas introducen contratos de dependencias

A diferencia de la biblioteca estándar, pandas debe instalarse en el entorno Python que ejecutará el código. El repositorio declara las dependencias ejecutables de la Fase 9 en `requirements-external.txt`.

Un contrato de dependencias responde preguntas como:

```text
¿Qué paquete se requiere?
¿Qué versiones admite el capítulo?
¿Qué versiones de Python admite ese paquete?
¿Cómo reproduce CI el mismo entorno?
¿Qué comportamientos cambiaron entre versiones principales?
```

Este capítulo apunta deliberadamente a pandas 3.0.x en lugar de fingir que todas las versiones históricas se comportan igual.

## 3. Instala pandas en un entorno aislado

Un entorno virtual mantiene las dependencias del proyecto separadas de otras instalaciones de Python.

```bash
python -m venv .venv
```

Actívalo según tu sistema operativo e instala el contrato de dependencias del repositorio:

```bash
python -m pip install -r requirements-external.txt
```

La documentación oficial también permite instalación directa con `pip install pandas` y mediante conda-forge. Aquí se prefiere un archivo de dependencias porque hace reproducible el contrato ejecutable de la guía.

## 4. Importa pandas con el alias convencional

La documentación y la comunidad de pandas usan `pd`:

```python
import pandas as pd
```

Seguir esta convención facilita comparar ejemplos con la documentación oficial y otros proyectos.

## 5. `Series` modela una dimensión etiquetada

Una `Series` es una estructura de datos unidimensional etiquetada. Combina valores con un índice. Una columna de DataFrame suele exponerse como una `Series`.

```python
import pandas as pd


scores = pd.Series([8.5, 9.0, 7.5], index=["A", "B", "C"])
print(scores.loc["B"])
```

```text
9.0
```

Una `Series` no es simplemente una lista con más métodos. Las etiquetas participan en selección y alineación.

## 6. `DataFrame` modela una tabla etiquetada

Un `DataFrame` es una tabla bidimensional con filas y columnas etiquetadas. Columnas diferentes pueden tener dtypes diferentes, lo que lo hace apropiado para muchos datasets similares a hojas de cálculo, SQL y CSV.

```python
import pandas as pd


people = pd.DataFrame(
    {
        "name": ["Ana", "Bruno"],
        "age": [28, 34],
        "active": [True, False],
    }
)
print(people.shape)
```

```text
(2, 3)
```

Un diccionario de secuencias con igual longitud es uno de los constructores más claros para ejemplos pequeños. Las claves se convierten en etiquetas de columnas.

## 7. El índice forma parte del modelo de datos

El índice etiqueta filas. El `RangeIndex` predeterminado es suficiente en muchos casos. Usa un índice personalizado significativo solo cuando las etiquetas de filas participen realmente en selección, alineación o identidad.

```python
import pandas as pd


temperatures = pd.Series([21.5, 19.0], index=["morning", "evening"])
print(temperatures.index.tolist())
```

```text
['morning', 'evening']
```

No conviertas automáticamente todo identificador de negocio en índice. Una columna normal suele ser más fácil de validar, combinar, exportar y explicar.

## 8. La alineación por etiquetas es poderosa y puede sorprender

Cuando pandas combina objetos etiquetados, normalmente alinea valores por etiquetas del índice en lugar de hacerlo ciegamente por posición física.

```python
import pandas as pd


left = pd.Series([10, 20], index=["a", "b"])
right = pd.Series([1, 2], index=["b", "c"])
print((left + right).to_dict())
```

La etiqueta compartida `b` recibe un valor de ambos objetos. Las etiquetas presentes solo en un lado quedan ausentes en el resultado.

Trata el índice como dato, no decoración. Etiquetas inesperadas pueden cambiar aritmética, joins, asignaciones y comparaciones.

## 9. Inspecciona columnas y dtypes temprano

Un flujo confiable inspecciona lo cargado antes de transformarlo. `columns` muestra etiquetas y `dtypes` el dtype elegido para cada columna.

```python
import pandas as pd


table = pd.DataFrame({"label": ["x", "y"], "count": [1, 2]})
print(table.columns.tolist())
print(table.dtypes.astype(str).to_dict())
```

pandas 3.0 cambió un valor predeterminado importante: las columnas que contienen solo strings se infieren con el dtype dedicado `str` en lugar del histórico dtype genérico `object`.

Esa es una razón para declarar explícitamente la versión de pandas de este capítulo.

## 10. `shape`, `size` y `ndim` responden preguntas distintas

```python
import pandas as pd


table = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(table.shape, table.size, table.ndim)
```

```text
(3, 2) 6 2
```

- `shape` devuelve `(filas, columnas)`;
- `size` devuelve la cantidad de celdas;
- `ndim` devuelve el número de dimensiones.

Son hechos estructurales, no validaciones por sí mismos.

## 11. Previsualizar ayuda, pero no valida

`head()` y `tail()` son herramientas rápidas de inspección. `sample()` puede revelar patrones fuera de las primeras filas, pero usa `random_state` cuando importa la reproducibilidad.

```python
import pandas as pd


table = pd.DataFrame({"value": [10, 20, 30, 40]})
print(table.sample(2, random_state=7)["value"].tolist())
```

Una vista previa no demuestra que existan columnas requeridas, que los dtypes sean correctos, que los identificadores sean únicos o que los valores estén dentro de rangos permitidos.

## 12. `info()` y `describe()` responden preguntas distintas

`DataFrame.info()` resume filas, nombres de columnas, conteos no nulos, dtypes y memoria aproximada. Es útil para inspección humana.

`describe()` resume estadísticas como count, mean, dispersión y extremos para columnas apropiadas.

```python
import pandas as pd


values = pd.DataFrame({"amount": [10.0, 20.0, 30.0]})
print(values["amount"].describe()[["count", "mean", "max"]].to_dict())
```

Ninguna función comprende el significado de negocio. Un importe negativo puede ser matemáticamente válido pero inválido para un dataset. Un identificador puede parecer numérico sin tener sentido promediarlo.

## 13. Selecciona una columna con corchetes

`df["column"]` devuelve una `Series`.

```python
import pandas as pd


table = pd.DataFrame({"unit price": [10.0, 12.5]})
prices = table["unit price"]
print(type(prices).__name__)
```

```text
Series
```

Prefiere corchetes al acceso por atributo como `df.column`. Los nombres pueden contener espacios, colisionar con atributos de DataFrame o elegirse dinámicamente.

## 14. Selecciona varias columnas con una lista

Pasar una lista de etiquetas devuelve un DataFrame y conserva el orden solicitado.

```python
import pandas as pd


table = pd.DataFrame({"a": [1], "b": [2], "c": [3]})
subset = table[["c", "a"]]
print(subset.columns.tolist())
```

```text
['c', 'a']
```

La distinción importa: una string selecciona una columna como `Series`; una lista de strings selecciona una tabla `DataFrame`.

## 15. Usa `.loc` para selección basada en etiquetas

`.loc` selecciona por etiquetas y condiciones booleanas.

```python
import pandas as pd


table = pd.DataFrame({"status": ["new", "done"], "value": [5, 8]}, index=["a", "b"])
print(table.loc["b", "value"])
```

```text
8
```

`.loc` también es la herramienta preferida para asignación condicional porque filas objetivo y columna destino pueden expresarse en una operación.

## 16. Usa `.iloc` para selección posicional

`.iloc` selecciona por posición entera, independientemente de las etiquetas del índice.

```python
import pandas as pd


table = pd.DataFrame({"name": ["first", "second", "third"]}, index=[10, 20, 30])
print(table.iloc[1, 0])
```

```text
second
```

Usa `.iloc` cuando la posición misma sea significativa. No la uses solo porque la selección por etiquetas resulte menos familiar.

## 17. Los slices por etiqueta y por posición tienen límites diferentes

Con `.loc`, un slice por etiqueta incluye la etiqueta final cuando existe. Con `.iloc`, el slicing sigue Python posicional y excluye la posición final.

```python
import pandas as pd


table = pd.DataFrame({"value": [10, 20, 30]}, index=["a", "b", "c"])
print(table.loc["a":"b", "value"].tolist())
print(table.iloc[0:2, 0].tolist())
```

```text
[10, 20]
[10, 20]
```

Los dos ejemplos devuelven los mismos valores por razones diferentes. Mantén separados los modelos mentales.

## 18. Las máscaras booleanas filtran filas

Una comparación contra una `Series` produce una `Series` booleana. Usar esa máscara con `.loc` conserva las filas donde la condición es verdadera.

```python
import pandas as pd


orders = pd.DataFrame({"amount": [50, 120, 80]})
mask = orders["amount"] >= 80
print(orders.loc[mask, "amount"].tolist())
```

```text
[120, 80]
```

Las máscaras son uno de los puentes principales entre lógica booleana de Python y operaciones orientadas a tablas.

## 19. Combina máscaras con `&`, `|` y `~`

Usa operadores booleanos elemento a elemento para condiciones de `Series` y pon cada comparación entre paréntesis.

```python
import pandas as pd


orders = pd.DataFrame(
    {"status": ["paid", "paid", "pending"], "amount": [50, 150, 200]}
)
mask = (orders["status"] == "paid") & (orders["amount"] >= 100)
print(orders.loc[mask, "amount"].tolist())
```

```text
[150]
```

Los operadores escalares `and` y `or` no expresan lógica fila a fila para una `Series` de pandas.

## 20. Asigna sobre el objeto que quieres cambiar

Al actualizar un DataFrame, expresa el selector de filas y la columna destino en una sola operación `.loc`.

```python
import pandas as pd


orders = pd.DataFrame({"amount": [50, 150], "priority": ["normal", "normal"]})
orders.loc[orders["amount"] >= 100, "priority"] = "high"
print(orders["priority"].tolist())
```

```text
['normal', 'high']
```

Este patrón es explícito y compatible con Copy-on-Write de pandas 3.0.

## 21. Copy-on-Write es la regla de pandas 3.0

En pandas 3.0, los objetos derivados mediante indexación o métodos se comportan como copias desde el punto de vista del usuario. Modificar un objeto derivado no modifica el original.

```python
import pandas as pd


original = pd.DataFrame({"value": [1, 2, 3]})
subset = original["value"]
subset.iloc[0] = 99

print(original["value"].tolist())
print(subset.tolist())
```

```text
[1, 2, 3]
[99, 2, 3]
```

Internamente pandas puede compartir memoria hasta que una escritura exija copiar. El contrato importante para código de aplicación es el comportamiento observable.

## 22. Chained assignment no es una estrategia válida

Código como este usa varios pasos de indexación:

```text
df["value"][mask] = 10
```

En pandas 3.0, chained assignment no actualiza el DataFrame original. La antigua ambigüedad que producía `SettingWithCopyWarning` fue sustituida por una regla más simple: modifica el objeto mismo en una operación.

```python
import pandas as pd


table = pd.DataFrame({"value": [1, 2, 3]})
table.loc[table["value"] >= 2, "value"] = 10
print(table["value"].tolist())
```

```text
[1, 10, 10]
```

Es un punto importante al consultar material antiguo de pandas 1.x o 2.x.

## 23. Crea columnas derivadas con expresiones vectorizadas

Las expresiones de columna operan sobre objetos `Series` completos y suelen ser más claras que un loop Python por cada fila.

```python
import pandas as pd


sales = pd.DataFrame({"units": [2, 3], "unit_price": [10.0, 12.5]})
sales["total"] = sales["units"] * sales["unit_price"]
print(sales["total"].tolist())
```

```text
[20.0, 37.5]
```

Es un hábito central de pandas: expresa la transformación en términos de columnas cuando la regla es columnar.

## 24. `assign()` es útil en method chains

`assign()` devuelve un DataFrame con columnas añadidas o reemplazadas.

```python
import pandas as pd


sales = pd.DataFrame({"units": [2, 3], "price": [5.0, 8.0]})
result = sales.assign(total=lambda frame: frame["units"] * frame["price"])
print(result["total"].tolist())
```

```text
[10.0, 24.0]
```

Úsalo cuando un pipeline sea más legible encadenando transformaciones. La asignación directa sigue siendo válida cuando es más clara.

## 25. Renombra, elimina y ordena con intención

`rename()` puede normalizar nombres externos incómodos. `drop()` elimina filas o columnas. `sort_values()` y `sort_index()` hacen explícito el orden.

```python
import pandas as pd


table = pd.DataFrame({"Order Amount": [20, 10], "temporary_note": ["b", "a"]})
clean = (
    table.rename(columns={"Order Amount": "amount"})
    .drop(columns=["temporary_note"])
    .sort_values("amount")
)
print(clean["amount"].tolist())
```

```text
[10, 20]
```

Un campo eliminado puede ser imposible de reconstruir. Un sort puede ser necesario para reportes deterministas. Estas operaciones codifican política, no solo formato.

## 26. Los datos ausentes necesitan una política explícita

Los valores ausentes pueden significar desconocido, no aplicable, no recolectado, inválido, retrasado o intencionalmente vacío. No son equivalentes.

Antes de llamar `dropna()` o `fillna()`, decide qué significa la ausencia para cada columna relevante.

```python
import pandas as pd


table = pd.DataFrame({"value": [1.0, None, 3.0], "label": ["a", "b", None]})
print(table.isna().sum().to_dict())
```

```text
{'value': 1, 'label': 1}
```

Contar ausencias es observación. Eliminarlas o rellenarlas es una transformación que necesita una regla.

## 27. `dropna()` descarta observaciones

`dropna()` es correcto solo cuando las observaciones afectadas son realmente descartables bajo el contrato de datos.

```python
import pandas as pd


table = pd.DataFrame({"id": [1, 2, 3], "amount": [10.0, None, 30.0]})
complete = table.dropna(subset=["amount"])
print(complete["id"].tolist())
```

```text
[1, 3]
```

Usar `dropna()` sin `subset` puede eliminar filas por campos irrelevantes para la operación actual.

## 28. `fillna()` inserta un significado elegido

Reemplazar un importe desconocido por cero afirma que cero es la interpretación correcta.

```python
import pandas as pd


table = pd.DataFrame({"discount": [0.1, None, 0.2]})
filled = table["discount"].fillna(0.0)
print(filled.tolist())
```

```text
[0.1, 0.0, 0.2]
```

Documenta reglas de relleno porque cambian el dataset, no solo su apariencia.

## 29. Los dtypes forman parte del schema

Una columna que parece numérica puede haberse cargado como texto. Una fecha puede seguir siendo string. Un identificador puede necesitar permanecer textual aunque todos sus valores sean dígitos.

Usa `astype()` cuando los valores ya sean válidos para el dtype destino:

```python
import pandas as pd


table = pd.DataFrame({"units": ["1", "2", "3"]})
table["units"] = table["units"].astype("int64")
print(table["units"].sum())
```

```text
6
```

Elige tipos según significado y operaciones, no solo apariencia.

## 30. `to_numeric()` hace explícita la política de parsing

`pd.to_numeric()` sirve cuando el parsing numérico puede fallar.

```python
import pandas as pd


raw = pd.Series(["10", "invalid", "30"])
parsed = pd.to_numeric(raw, errors="coerce")
print(parsed.isna().sum())
```

```text
1
```

`errors="coerce"` convierte entradas inválidas en valores ausentes. Solo es seguro si después el flujo audita y trata esas nuevas ausencias.

## 31. Las operaciones de string son vectorizadas bajo `.str`

El accessor `.str` aplica operaciones de string a una `Series`.

```python
import pandas as pd


names = pd.Series(["  Alpha ", "BETA  "])
normalized = names.str.strip().str.lower()
print(normalized.tolist())
```

```text
['alpha', 'beta']
```

Normaliza texto solo cuando coincida con el contrato del dominio. Pasar identificadores a minúsculas o descartar espacios puede cambiar significado.

## 32. Convierte datetimes antes de usar semántica temporal

Usa `pd.to_datetime()` cuando el texto debe convertirse en datetime real.

```python
import pandas as pd


dates = pd.to_datetime(pd.Series(["2026-08-01", "2026-08-03"]), format="%Y-%m-%d")
print((dates.iloc[1] - dates.iloc[0]).days)
```

```text
2
```

El accessor `.dt` expone componentes vectorizados:

```python
import pandas as pd


dates = pd.to_datetime(pd.Series(["2026-01-15", "2026-02-20"]))
print(dates.dt.month.tolist())
```

```text
[1, 2]
```

Los formatos ambiguos deben controlarse explícitamente en lugar de adivinarse.

## 33. Los duplicados necesitan una definición

Dos filas son duplicadas solo con respecto a columnas elegidas. `duplicated()` y `drop_duplicates()` aceptan `subset` para expresar la clave real de unicidad.

```python
import pandas as pd


table = pd.DataFrame(
    {"id": [1, 1, 2], "note": ["first", "repeated", "other"]}
)
print(table.duplicated(subset=["id"]).tolist())
```

```text
[False, True, False]
```

No dedupliques filas completas cuando la regla real es unicidad por identificador.

## 34. Los métodos de frecuencia y resumen son diagnósticos compactos

`value_counts()` muestra frecuencia de categorías. `nunique()` cuenta valores distintos no ausentes por defecto. Reducciones como `sum()`, `mean()`, `min()`, `max()` y `count()` resumen columnas.

```python
import pandas as pd


statuses = pd.Series(["paid", "pending", "paid", "paid"])
print(statuses.value_counts().sort_index().to_dict())
```

```text
{'paid': 3, 'pending': 1}
```

Una frecuencia es evidencia sobre el dataset observado, no prueba de que toda categoría observada esté permitida.

## 35. `groupby()` implementa split-apply-combine

`groupby()` divide filas por una o más claves, aplica agregación o transformación y combina resultados.

```python
import pandas as pd


sales = pd.DataFrame(
    {"category": ["A", "B", "A"], "amount": [10, 20, 30]}
)
summary = sales.groupby("category")["amount"].sum()
print(summary.to_dict())
```

```text
{'A': 40, 'B': 20}
```

Agrupar es central en pandas porque muchas preguntas analíticas son "calcula algo por categoría, cliente, fecha, región u otra clave".

## 36. La agregación nombrada hace explícito el schema de salida

Named aggregation permite declarar columna de origen y operación.

```python
import pandas as pd


sales = pd.DataFrame(
    {"category": ["A", "A", "B"], "amount": [10.0, 30.0, 20.0]}
)
summary = sales.groupby("category", as_index=False).agg(
    total=("amount", "sum"),
    average=("amount", "mean"),
)
print(summary.to_dict(orient="records"))
```

```text
[{'category': 'A', 'total': 40.0, 'average': 20.0}, {'category': 'B', 'total': 20.0, 'average': 20.0}]
```

Un schema de salida estable facilita validación, exportación y pruebas posteriores.

## 37. `transform()` mantiene resultados alineados con las filas originales

A diferencia de una agregación normal, `transform()` devuelve un resultado alineado con el índice original.

```python
import pandas as pd


sales = pd.DataFrame({"team": ["A", "A", "B"], "score": [10, 20, 30]})
sales["team_total"] = sales.groupby("team")["score"].transform("sum")
print(sales["team_total"].tolist())
```

```text
[30, 30, 30]
```

Es útil cuando una estadística del grupo debe quedar junto a cada observación.

## 38. `merge()` combina tablas por claves

`merge()` es la operación de join estilo base de datos de pandas.

```python
import pandas as pd


orders = pd.DataFrame({"customer_id": [1, 2], "amount": [10, 20]})
customers = pd.DataFrame({"customer_id": [1, 2], "name": ["A", "B"]})
result = orders.merge(customers, on="customer_id", how="left")
print(result["name"].tolist())
```

```text
['A', 'B']
```

Un merge que termina sin error todavía puede ser incorrecto lógicamente si las claves tienen duplicados inesperados.

## 39. Valida la cardinalidad del merge

El argumento `validate` puede afirmar relaciones como `one_to_one`, `one_to_many`, `many_to_one` o `many_to_many`.

```python
import pandas as pd


orders = pd.DataFrame({"customer_id": [1, 1], "amount": [10, 20]})
customers = pd.DataFrame({"customer_id": [1], "name": ["A"]})
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one",
)
print(len(result))
```

```text
2
```

Cuando la cardinalidad forma parte del contrato, validarla convierte duplicaciones accidentales en fallos visibles en vez de multiplicar filas silenciosamente.

## 40. `concat()` apila objetos compatibles

`pd.concat()` combina objetos pandas a lo largo de un eje. Concatenar filas es común cuando varios archivos comparten schema.

```python
import pandas as pd


first = pd.DataFrame({"id": [1, 2]})
second = pd.DataFrame({"id": [3]})
combined = pd.concat([first, second], ignore_index=True)
print(combined["id"].tolist())
```

```text
[1, 2, 3]
```

Después de concatenar, decide si deben conservarse o reiniciarse las etiquetas del índice original.

## 41. `pivot_table()` resume en una matriz

Una pivot table agrupa datos entre dimensiones de filas y columnas y agrega valores.

```python
import pandas as pd


sales = pd.DataFrame(
    {
        "region": ["north", "north", "south"],
        "product": ["A", "B", "A"],
        "amount": [10, 20, 30],
    }
)
pivot = sales.pivot_table(
    index="region",
    columns="product",
    values="amount",
    aggfunc="sum",
    fill_value=0,
)
print(pivot.loc["north", "B"])
```

```text
20
```

Usa pivot table cuando la salida deseada sea una matriz de resumen.

## 42. `melt()` convierte datos wide a long

Los datos long suelen facilitar agrupación y visualización.

```python
import pandas as pd


wide = pd.DataFrame({"item": ["A"], "jan": [10], "feb": [20]})
long = wide.melt(id_vars="item", var_name="month", value_name="amount")
print(long.to_dict(orient="records"))
```

```text
[{'item': 'A', 'month': 'jan', 'amount': 10}, {'item': 'A', 'month': 'feb', 'amount': 20}]
```

`melt()` resulta especialmente útil cuando columnas repetidas representan valores de una misma variable conceptual.

## 43. `read_csv()` convierte texto delimitado en DataFrame

`pd.read_csv()` es una de las funciones de I/O más importantes de pandas.

```python
from io import StringIO

import pandas as pd


source = StringIO("id,amount\n1,10.5\n2,20.0\n")
table = pd.read_csv(source)
print(table.shape)
```

```text
(2, 2)
```

pandas infiere un schema salvo que proporciones instrucciones más fuertes. La inferencia es comodidad, no contrato de negocio.

## 44. Controla el parsing de CSV cuando conoces el schema

Argumentos útiles de `read_csv()` incluyen `usecols`, `dtype`, `parse_dates`, `na_values`, `encoding` y opciones de delimitador.

```python
from io import StringIO

import pandas as pd


source = StringIO("code,date,amount\n001,2026-08-01,10.5\n")
table = pd.read_csv(
    source,
    dtype={"code": "str"},
    parse_dates=["date"],
)
print(table.loc[0, "code"])
print(table.loc[0, "date"].year)
```

```text
001
2026
```

Dar a pandas información conocida del schema reduce inferencias accidentales y documenta expectativas cerca de la frontera de entrada.

## 45. Los identificadores suelen pertenecer al dtype string

Un código como `00123` puede parecer numérico sin tener significado aritmético. Convertirlo a entero destruye ceros iniciales.

```python
import pandas as pd


codes = pd.Series(["001", "010"], dtype="str")
print(codes.tolist())
```

```text
['001', '010']
```

Modela identificadores según su semántica, no por los caracteres que contienen.

## 46. `to_csv()` debe hacer explícita la política del índice

Para tablas cuyo índice solo es una etiqueta interna de fila, `index=False` evita una columna extra al reimportar.

```python
from io import StringIO

import pandas as pd


table = pd.DataFrame({"id": [1], "value": [10]})
buffer = StringIO()
table.to_csv(buffer, index=False)
print(buffer.getvalue().strip())
```

```text
id,value
1,10
```

Si el índice contiene información real, expórtalo intencionalmente en vez de desactivarlo siempre.

## 47. Method chains hacen visible el orden de transformación

Una cadena corta puede leerse como pipeline: filtrar, derivar, ordenar, agrupar, exportar.

```python
import pandas as pd


orders = pd.DataFrame(
    {"status": ["paid", "pending", "paid"], "amount": [30, 50, 20]}
)
result = (
    orders.loc[orders["status"] == "paid"]
    .assign(taxed=lambda frame: frame["amount"] * 1.1)
    .sort_values("amount")
)
print(result["amount"].tolist())
```

```text
[20, 30]
```

Las cadenas largas pueden dificultar debugging. Divídelas en etapas nombradas cuando la intención deje de ser clara.

## 48. Prefiere operaciones vectorizadas a loops Python por fila

Cuando un cálculo pueda expresarse con aritmética de `Series`, comparaciones, `.str`, `.dt` o reducciones nativas, prefiere esa forma.

```python
import pandas as pd


table = pd.DataFrame({"quantity": [2, 3], "price": [4.0, 5.0]})
table["total"] = table["quantity"] * table["price"]
print(table["total"].tolist())
```

```text
[8.0, 15.0]
```

La vectorización comunica intención tabular y suele permitir que pandas/NumPy trabajen con mayor eficiencia que llamadas Python repetidas.

## 49. `apply()` no es automáticamente vectorización

`Series.apply()` y `DataFrame.apply()` por fila pueden servir para lógica Python personalizada, pero pueden ejecutar una función Python repetidamente.

Antes de usar `apply()`, pregunta si pandas ya proporciona una operación nativa para la transformación.

Úsalo porque la lógica personalizada sea realmente necesaria, no porque parezca más corto que un loop.

## 50. Evita `iterrows()` para transformaciones normales

La iteración por filas puede ser necesaria en fronteras con efectos externos, pero filtros, cálculos, agregaciones y asignaciones suelen tener formas mejores orientadas a columnas.

Una fila devuelta por `iterrows()` es una representación `Series`. No la trates como un handle mutable para actualizar el DataFrame original.

## 51. `.copy()` todavía tiene un papel deliberado

Copy-on-Write significa que copias defensivas ya no son necesarias solo para silenciar el antiguo `SettingWithCopyWarning`.

Usa `.copy()` cuando una copia independiente inmediata forme parte del diseño o del contrato de ciclo de vida.

```python
import pandas as pd


original = pd.DataFrame({"value": [1, 2]})
independent = original.copy()
independent.loc[0, "value"] = 99
print(original["value"].tolist())
```

```text
[1, 2]
```

## 52. Los errores de DataFrame deben mantenerse visibles

Fallos comunes incluyen:

```text
KeyError
ValueError
pandas.errors.ParserError
pandas.errors.MergeError
```

No captures excepciones amplias solo para mantener un pipeline avanzando. Una tabla parcialmente transformada puede ser más peligrosa que un fallo visible.

Los fallos de validación deben detener el flujo cuando continuar haría la salida no confiable.

## 53. Ejemplo práctico: construir una pequeña tabla de ventas

```python
import pandas as pd


data = {
    "product": ["Notebook", "Keyboard", "Mouse"],
    "units": [2, 5, 8],
    "unit_price": [3500.0, 180.0, 95.0],
}

sales = pd.DataFrame(data)
sales["total"] = sales["units"] * sales["unit_price"]

print(f"shape: {sales.shape}")
print(f"columns: {sales.columns.tolist()}")
print(f"grand total: {sales['total'].sum():.2f}")
```

```text
shape: (3, 4)
columns: ['product', 'units', 'unit_price', 'total']
grand total: 8660.00
```

Este ejemplo refleja `examples/dataframe_basics.py` y demuestra construcción, inspección, columna derivada y agregación.

## 54. Ejemplo práctico: filtrar y asignar con seguridad

```python
import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104],
        "status": ["paid", "pending", "paid", "paid"],
        "amount": [120.0, 80.0, 250.0, 90.0],
    }
)

orders["priority"] = "normal"
orders.loc[
    (orders["status"] == "paid") & (orders["amount"] >= 200),
    "priority",
] = "high"

selected = orders.loc[
    orders["status"] == "paid",
    ["order_id", "priority"],
]
print(selected.to_dict(orient="records"))
```

```text
[{'order_id': 101, 'priority': 'normal'}, {'order_id': 103, 'priority': 'high'}, {'order_id': 104, 'priority': 'normal'}]
```

La actualización ocurre directamente sobre `orders` mediante `.loc`, el patrón seguro para pandas 3.0.

## 55. Ejemplo práctico: resumen agrupado

```python
import pandas as pd


transactions = pd.DataFrame(
    {
        "category": ["books", "games", "books", "games", "office"],
        "amount": [40.0, 120.0, 35.0, 80.0, 25.0],
    }
)

summary = (
    transactions.groupby("category", as_index=False)
    .agg(
        total_amount=("amount", "sum"),
        transaction_count=("amount", "size"),
    )
    .sort_values("category")
)

print(summary.to_dict(orient="records"))
```

Las columnas de salida nombradas forman un schema estable. El sort final hace determinista el ejemplo.

## 56. Ejemplo práctico: merge validado

```python
import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [1, 2, 3],
        "customer_id": [10, 20, 10],
        "amount": [50.0, 80.0, 30.0],
    }
)
customers = pd.DataFrame(
    {
        "customer_id": [10, 20],
        "customer": ["Aster", "Boreal"],
    }
)

report = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one",
)
report = report[["order_id", "customer", "amount"]].sort_values("order_id")

print(report.to_dict(orient="records"))
```

`validate="many_to_one"` documenta que muchos pedidos pueden referenciar a un cliente mientras la tabla de clientes debe mantener claves únicas.

## 57. Ejemplo práctico: pipeline CSV determinista

```python
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source = workspace / "orders.csv"
    destination = workspace / "paid_orders.csv"

    source.write_text(
        "order_id,date,status,amount\n"
        "1,2026-08-01,paid,120.50\n"
        "2,2026-08-02,pending,80.00\n"
        "3,2026-08-03,paid,250.00\n",
        encoding="utf-8",
    )

    orders = pd.read_csv(source, parse_dates=["date"])
    paid_orders = orders.loc[orders["status"] == "paid"].sort_values("order_id")
    paid_orders.to_csv(destination, index=False)

    print(f"rows: {len(paid_orders)}")
    print(f"total: {paid_orders['amount'].sum():.2f}")
    print(f"saved: {destination.name}")
```

```text
rows: 2
total: 370.50
saved: paid_orders.csv
```

El directorio temporal mantiene seguro el ejemplo, `parse_dates` establece semántica datetime en la entrada, el sort estabiliza el resultado y `index=False` mantiene deliberado el schema CSV.

## 58. Errores comunes

Evita estos patrones:

- tratar pandas como reemplazo de toda lista o diccionario;
- confiar en dtypes inferidos sin inspección;
- convertir identificadores a números solo porque contienen dígitos;
- usar chained assignment en vez de una actualización `.loc` única;
- llamar `dropna()` o `fillna()` sin definir el significado de ausencia;
- unir tablas sin comprobar unicidad o cardinalidad de claves;
- depender del orden incidental de filas;
- usar `iterrows()` para cálculos que tienen formas vectorizadas;
- usar `apply()` antes de comprobar operaciones nativas de pandas;
- exportar accidentalmente un índice interno;
- ocultar errores de parsing o merge y continuar con datos parciales;
- copiar consejos de pandas 1.x/2.x sin comprobar el comportamiento de pandas 3.0.

## 59. Tabla de decisión

| Necesidad | Prefiere |
|---|---|
| una columna etiquetada | `Series` |
| tabla etiquetada | `DataFrame` |
| selección por label | `.loc` |
| selección por posición | `.iloc` |
| filtro condicional de filas | máscara booleana + `.loc` |
| actualización condicional | una asignación `.loc[...] = ...` |
| convertir texto numérico | `pd.to_numeric()` |
| convertir texto datetime | `pd.to_datetime()` / `parse_dates` |
| inspeccionar ausencias | `isna()` |
| eliminar filas bajo una regla definida | `dropna()` |
| rellenar ausencias bajo una regla definida | `fillna()` |
| agregar por grupo | `groupby()` + `agg()` |
| estadística de grupo junto a cada fila | `groupby()` + `transform()` |
| join por clave estilo base de datos | `merge()` + `validate=` cuando se conozca |
| apilar tablas compatibles | `concat()` |
| matriz de resumen | `pivot_table()` |
| reshape wide-to-long | `melt()` |
| cargar CSV | `read_csv()` |
| guardar CSV | `to_csv(index=...)` |

## 60. Referencia rápida

```text
import pandas as pd

pd.Series(...)
pd.DataFrame(...)

df.shape
df.columns
df.dtypes
df.head()
df.info()
df.describe()

df["column"]
df[["column_a", "column_b"]]
df.loc[...]
df.iloc[...]

df.assign(...)
df.rename(...)
df.drop(...)
df.sort_values(...)
df.sort_index(...)

df.isna()
df.dropna(...)
df.fillna(...)
df.astype(...)
pd.to_numeric(...)
pd.to_datetime(...)

series.str...
series.dt...
series.value_counts()
series.nunique()

df.groupby(...)
df.agg(...)
df.transform(...)

df.merge(...)
pd.concat(...)
df.pivot_table(...)
df.melt(...)

pd.read_csv(...)
df.to_csv(...)
```

## 61. Checklist de diseño

Antes de aceptar una transformación pandas, pregunta:

- ¿Cuál es el schema esperado de entrada?
- ¿Qué columnas son identificadores, números, texto, fechas o categorías?
- ¿El índice es significativo o solo posicional?
- ¿La alineación por etiquetas puede cambiar el resultado?
- ¿Se permiten valores ausentes y qué significan?
- ¿La inferencia de dtype es aceptable en esta frontera?
- ¿Las actualizaciones condicionales se hacen directamente con `.loc`?
- ¿La cardinalidad del merge se conoce y valida?
- ¿El orden de filas puede variar y debería ordenarse el resultado?
- ¿Existe una operación vectorizada disponible?
- ¿`apply()` o la iteración por filas realmente requieren lógica Python?
- ¿Una exportación incluirá el índice accidentalmente?
- ¿Los fallos permanecen visibles en vez de convertirse silenciosamente?
- ¿Está documentado el contrato de versión de pandas?
- ¿El código depende de supuestos copy/view anteriores a pandas 3.0?

## 62. Ejercicio

Construye un pipeline ficticio de análisis de pedidos:

1. Crea o carga un CSV con `order_id`, `customer_id`, `date`, `status`, `category` y `amount`.
2. Conserva identificadores como strings si se permiten ceros iniciales.
3. Convierte `date` a datetime.
4. Valida columnas requeridas antes de transformar.
5. Convierte `amount` numéricamente y detecta entradas inválidas.
6. Informa valores ausentes por columna.
7. Conserva solo filas `paid` sin un loop Python por fila.
8. Crea una columna derivada `month` desde los datetime.
9. Produce un resumen por `category` con total, promedio y cantidad de transacciones.
10. Une los pedidos con una tabla ficticia de clientes y valida la cardinalidad esperada.
11. Ordena explícitamente la salida del reporte.
12. Guarda el resumen final sin exportar un índice accidental.
13. Haz visibles los fallos esperados de calidad en vez de ocultarlos.

Desafíos de extensión:

- compara una solución vectorizada con una basada en `apply()`;
- construye una pivot table wide;
- conviértela de nuevo a long con `melt()`;
- agrega tests para conteos de filas, totales, unicidad de claves, dtypes y cardinalidad de merge;
- documenta qué transformaciones cambian la cantidad de filas y por qué.

## 63. Conexiones con conceptos anteriores de Python

`pandas` se apoya en conceptos ya estudiados:

- **listas y diccionarios:** constructores y conversiones de resultados;
- **funciones:** etapas reutilizables de transformación;
- **lógica booleana:** máscaras de filas;
- **excepciones:** fallos visibles de I/O, conversión y joins;
- **archivos y context managers:** fronteras CSV y otros datos;
- **`pathlib`:** objetos de ruta funcionan naturalmente con I/O de pandas;
- **`datetime`:** pandas extiende el trabajo temporal a columnas;
- **CSV y JSON:** pandas añade una capa orientada a tablas sobre formatos de datos;
- **`decimal`:** las decisiones de representación siguen importando; columnas float no reemplazan requisitos de decimal exacto;
- **`logging`:** pipelines operativos deben reportar contexto útil sin ocultar excepciones;
- **`os` y `shutil`:** descubrimiento y movimiento de archivos suelen rodear pipelines pandas.

## 64. Referencias

Referencias principales usadas para este capítulo:

- [Documentación pandas 3.0.5](https://pandas.pydata.org/docs/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Visión general del paquete pandas](https://pandas.pydata.org/docs/getting_started/overview.html)
- [Tutoriales Getting Started](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)
- [Notas de versión de pandas 3.0.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html)

La documentación oficial identifica pandas 3.0.5 como la documentación estable usada en este capítulo, y pandas 3.0 requiere Python 3.11 o superior.

## 65. Próximo capítulo

Después de `pandas`, la ruta continúa con **`openpyxl`**, pasando de la semántica de tablas a la estructura de libros de Excel.

Continúa con [`openpyxl`: Automatizando Libros de Excel](../02-openpyxl/README.es.md) para estudiar operaciones con hojas/celdas, límites de fórmulas, estilos, tablas, metadatos de validación, modos optimizados y round-trips seguros.
