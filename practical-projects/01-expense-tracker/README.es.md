<div align="center">

# Proyecto 01 · Control de Gastos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Proyectos Prácticos](../README.es.md)

Este es el primer proyecto de la **Fase 10: Proyectos Prácticos**. El objetivo es dejar de estudiar conceptos de forma aislada y combinar modelado de datos, funciones, colecciones, excepciones, archivos, JSON, CSV, `pathlib`, `Decimal` y `pytest` en un flujo pequeño pero completo.

**Tiempo estimado de estudio e implementación:** 180–240 minutos.

## Objetivos de aprendizaje

Al finalizar este proyecto, deberías poder:

- transformar una descripción breve del problema en requisitos explícitos de software;
- modelar un gasto como dato estructurado validado;
- usar `Decimal` para valores monetarios exactos con dos decimales;
- separar responsabilidades de validación, almacenamiento, filtrado e informes;
- persistir registros en JSON sin convertir dinero silenciosamente a punto flotante binario;
- exportar los mismos registros a CSV;
- escribir pruebas automatizadas repetibles para caminos de éxito y fallo;
- explicar el proyecto como pieza de portafolio, no solo mostrar código.

## 1. Descripción del proyecto

Construye un pequeño control de gastos capaz de:

1. registrar gastos;
2. listar gastos almacenados;
3. filtrar gastos por categoría;
4. calcular el total completo;
5. calcular el total de una categoría;
6. resumir totales por categoría;
7. guardar registros en JSON;
8. restaurar registros desde JSON;
9. exportar registros a CSV;
10. demostrar los comportamientos importantes con pruebas automatizadas.

El proyecto comienza deliberadamente como módulo Python y no como aplicación gráfica. La Fase 10 empieza integrando lógica y contratos de datos antes de añadir otra capa de interfaz.

## 2. Requisitos funcionales

Cada gasto debe contener:

```text
spent_on    -> date in YYYY-MM-DD format
description -> non-blank text
category    -> non-blank text
amount      -> positive monetary value with two decimal places
```

El tracker debe conservar el orden de inserción y exponer los registros sin entregar al código consumidor acceso directo para mutar su lista interna.

## 3. Requisitos de validación

La entrada inválida debe fallar explícitamente.

Ejemplos:

- texto de fecha inválido produce `ValueError`;
- descripción vacía produce `ValueError`;
- categoría vacía produce `ValueError`;
- importe cero o negativo produce `ValueError`;
- `NaN` e infinito son rechazados;
- JSON con forma raíz incorrecta es rechazado;
- registros JSON sin campos obligatorios son rechazados.

Una validación fallida no puede añadir un gasto parcial al tracker.

## 4. Por qué el dinero usa `Decimal`

El proyecto almacena importes con `decimal.Decimal` en lugar de `float`.

```python
from decimal import Decimal

amount = Decimal("25.90")
```

El parser redondea a dos decimales con `ROUND_HALF_UP` después de verificar que el valor sea finito y mayor que cero.

Esto no pretende ser un motor contable universal. Es una regla explícita para un control de gastos de dos decimales.

## 5. El modelo de datos `Expense`

`Expense` es una dataclass inmutable:

```python
@dataclass(frozen=True, slots=True)
class Expense:
    spent_on: date
    description: str
    category: str
    amount: Decimal
```

Los registros normalmente se crean mediante `Expense.create(...)`, que aplica toda la normalización antes de que exista el objeto.

## 6. El servicio del tracker

`ExpenseTracker` es responsable de la colección de gastos y de las operaciones que usan esa colección.

```python
tracker = ExpenseTracker()
tracker.add("2026-08-29", "Lunch", "Food", "25.40")
tracker.add("2026-08-29", "Bus", "Transport", "12.00")
```

La propiedad pública `expenses` devuelve una tupla, permitiendo inspeccionar los registros sin recibir la lista interna mutable.

## 7. Filtrado por categoría

La comparación de categorías no distingue mayúsculas y minúsculas:

```python
food_expenses = tracker.filter_by_category("food")
```

`Food`, `food` y `FOOD` se tratan como la misma categoría para filtros y resúmenes, mientras la primera forma almacenada permanece como representación visible.

## 8. Totales

El total completo se obtiene con:

```python
total = tracker.total()
```

El total de una categoría es:

```python
food_total = tracker.total("Food")
```

Como cada importe almacenado ya es `Decimal`, la suma nunca pasa a aritmética binaria de punto flotante.

## 9. Totales por categoría

El tracker puede producir un diccionario como:

```text
Food      -> 53.90
Transport -> 120.00
```

Esta operación combina acumulación en diccionarios, normalización sin distinguir mayúsculas/minúsculas, iteración y aritmética decimal exacta.

## 10. Persistencia JSON

`save_json()` escribe una lista de registros.

El importe monetario se serializa como texto:

```json
{
  "spent_on": "2026-08-29",
  "description": "Coffee",
  "category": "Food",
  "amount": "8.50"
}
```

Guardar el importe como string hace explícita la representación decimal en lugar de pasarlo por un número de punto flotante JSON.

## 11. Restauración JSON

`ExpenseTracker.load_json(...)` interpreta el archivo y reconstruye cada elemento usando el mismo camino validado `Expense.create(...)` utilizado por datos nuevos.

Eso significa que los datos persistidos no evitan validación solo porque provienen de un archivo.

## 12. Exportación CSV

`export_csv()` crea este esquema:

```text
spent_on,description,category,amount
```

El archivo se abre con `newline=""`, siguiendo el contrato de frontera CSV enseñado anteriormente en el currículo.

## 13. Estructura del proyecto

```text
01-expense-tracker/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── expense_tracker.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_expense_tracker.py
```

El proyecto es suficientemente pequeño para entenderse en una sesión, pero contiene fronteras similares a una aplicación real: modelo, comportamiento del servicio, persistencia, exportación, demo y pruebas.

## 14. Ejecuta la demo determinista

Desde la raíz del repositorio:

```bash
python practical-projects/01-expense-tracker/demo.py
```

Salida esperada:

```text
expenses: 3
total: 173.90
food: 53.90
transport: 120.00
json round-trip: True
csv rows: 3
```

La demo usa un directorio temporal, por lo que no deja archivos JSON o CSV en el repositorio.

## 15. Ejecuta las pruebas del proyecto

```bash
python -m pytest -q practical-projects/01-expense-tracker/tests
```

La suite inicial cubre:

- normalización de campos;
- redondeo half-up de importes;
- rechazo de valores monetarios inválidos;
- total completo;
- total por categoría y filtrado sin distinguir mayúsculas/minúsculas;
- round-trip JSON;
- rechazo de una forma raíz JSON inválida;
- header y filas exactas del CSV.

## 16. Nota de diseño: un solo camino de validación

Datos nuevos y registros restaurados desde JSON terminan en `Expense.create(...)`.

Esto evita dos sistemas de validación competidores:

```text
new input ----\
              -> Expense.create -> validated Expense
JSON record --/
```

Una sola frontera de validación es más fácil de razonar y probar.

## 17. Nota de diseño: registros inmutables, colección mutable

Un `Expense` individual está congelado, pero el tracker puede añadir nuevos gastos válidos.

La división representa dos responsabilidades diferentes:

- un registro de gasto representa un hecho que no debería cambiar accidentalmente;
- el tracker representa una colección que crece al registrar nuevos gastos.

## 18. Nota de diseño: persistencia explícita

Añadir un gasto cambia la memoria. Guardar JSON cambia un archivo.

El tracker no escribe silenciosamente en disco cada vez que se ejecuta `add()`. Mantener ambas operaciones explícitas hace los efectos secundarios más visibles, comprobables y reemplazables en el futuro.

## 19. Caminos de fallo para inspeccionar manualmente

Prueba estas llamadas y lee las excepciones:

```python
tracker.add("not-a-date", "Lunch", "Food", "10.00")
tracker.add("2026-08-29", "", "Food", "10.00")
tracker.add("2026-08-29", "Lunch", "Food", "0")
tracker.add("2026-08-29", "Lunch", "Food", "NaN")
```

El objetivo no es solo observar fallos. Confirma que el tracker permanece sin cambios después de cada entrada rechazada.

## 20. Estrategia de pruebas

Las pruebas se enfocan en contratos observables y no en detalles privados de implementación.

Por ejemplo, la prueba CSV verifica el archivo resultante en lugar de afirmar cuántas veces se llamó `csv.DictWriter.writerow()`.

Esto conserva la posibilidad de refactorizar mientras el comportamiento público siga siendo correcto.

## 21. Lo que esta primera versión no incluye

La primera versión no incluye:

- interfaz gráfica;
- base de datos;
- autenticación;
- sincronización en nube;
- múltiples monedas;
- gastos recurrentes;
- presupuestos;
- edición o eliminación de registros;
- gráficos.

Un proyecto pequeño con fronteras claras es más útil para aprender que uno grande con muchas funciones a medio terminar.

## 22. Desafío de extensión: filtrado por fecha

Añade métodos para:

- una fecha exacta;
- un rango inicio/fin;
- un mes.

Escribe pruebas de frontera antes de añadir código de presentación.

## 23. Desafío de extensión: edición y eliminación

Introduce un identificador estable de gasto e implementa actualización/eliminación deliberadas.

Piensa qué debe ocurrir si un ID no existe y si los archivos persistidos deben conservar IDs después de recargarlos.

## 24. Desafío de extensión: presupuestos mensuales

Añade presupuesto por categoría y calcula:

```text
budget
spent
remaining
percentage used
```

Mantén `Decimal` en todo el pipeline monetario.

## 25. Desafío de extensión: informe con pandas

Carga los datos CSV exportados con pandas y produce un resumen por mes/categoría.

El objetivo no es reemplazar el núcleo del tracker con pandas. Es usar pandas en la frontera analítica donde la transformación tabular se vuelve útil.

## 26. Desafío de extensión: informe Excel

Usa openpyxl para generar un workbook con:

- gastos brutos;
- resumen por categoría;
- resumen mensual;
- formatos numéricos;
- una tabla.

Esto conecta directamente el Proyecto 01 con la Fase 9.

## 27. Discusión de portafolio

Al presentar el proyecto, no lo describas solo como “un control de gastos”. Explica las decisiones de ingeniería:

- dinero exacto con `Decimal`;
- registros inmutables y validados;
- un único camino de validación para datos nuevos y persistidos;
- conservación en round-trip JSON;
- interoperabilidad CSV;
- comportamiento de categorías sin distinguir mayúsculas/minúsculas;
- pruebas automatizadas deterministas;
- archivos temporales en demos/pruebas para evitar contaminar el repositorio.

Esas decisiones demuestran más capacidad que la cantidad de líneas del programa.

## 28. Checklist de revisión

Antes de considerar completa tu propia implementación, verifica:

- ¿Cada registro inválido falla antes de mutar estado?
- ¿Los cálculos monetarios son exactos bajo la regla declarada de dos decimales?
- ¿Los datos JSON pueden guardarse y restaurarse sin modificar registros?
- ¿El CSV puede ser leído por otra herramienta?
- ¿Las reglas de categoría son explícitas?
- ¿Los efectos sobre el filesystem son intencionales?
- ¿Las pruebas cubren caminos de éxito y fallo?
- ¿Otro desarrollador puede entender la estructura sin preguntar dónde está el código importante?

## 29. Próximo proyecto

El Proyecto 01 establece el patrón de la Fase 10: **requisitos → diseño → implementación → pruebas → explicación → extensiones → discusión de portafolio**.

El siguiente proyecto planificado es la **Calculadora de Notas**, enfocada en reglas configurables, agregación, validación e informes sin repetir el diseño de persistencia de este proyecto.
