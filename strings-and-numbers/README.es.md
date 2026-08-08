<div align="center">

# Textos y Números

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta sección corresponde a la Fase 2 de la secuencia principal de aprendizaje de Python Study Guide. Se apoya en Fundamentos para profundizar en los valores de texto y numéricos de Python antes de introducir colecciones y flujo del programa.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Nivel | Estado |
|---|---|---|---|
| [01. Creación e indexación de strings](01-string-creation-and-indexing/README.es.md) | Crear strings y leer posiciones e intervalos de forma segura | Principiante | Disponible |
| [02. Métodos comunes de strings](02-common-string-methods/README.es.md) | Transformar, buscar, dividir y unir texto | Principiante | Disponible |
| [03. `int`, `float` y `bool`](03-int-float-and-bool/README.es.md) | Profundizar en el comportamiento de enteros, punto flotante y booleanos | Principiante | Disponible |
| 04. `round()`, `abs()`, `min()`, `max()` y `sum()` | Usar funciones incorporadas numéricas comunes | Principiante | Planificado |

## Orientación de prerrequisitos

- **01. Creación e indexación de strings:** completa primero la Fase 1. Debes comprender variables, `str`, `int`, `type()`, conversión de tipos y ejecución básica de programas.
- **02. Métodos comunes de strings:** completa primero el Capítulo 01. Debes comprender la inmutabilidad de las strings, la indexación, el slicing y la diferencia entre la string original y un resultado de tipo string producido sin modificarla.
- **03. `int`, `float` y `bool`:** completa primero el Capítulo 02. La Fase 1 ya presentó estos tipos; este capítulo profundiza el comportamiento numérico, la precisión de punto flotante y los valores de verdad.
- **04. Funciones numéricas incorporadas:** completa primero el capítulo sobre tipos numéricos para aprender estas funciones en contexto y no como una lista aislada.

Estudia los capítulos en orden numérico al seguir la ruta completa.

```text
01. String creation and indexing
        ↓
02. Common string methods
        ↓
03. int, float, and bool
        ↓
04. round(), abs(), min(), max(), and sum()
```

## Objetivos de la sección

Al final de esta ruta de aprendizaje, deberías poder:

- crear e inspeccionar valores de texto con confianza;
- leer posiciones e intervalos de strings mediante indexación y slicing;
- usar operaciones comunes de strings respetando su inmutabilidad;
- distinguir y usar tipos comunes de valores numéricos y lógicos;
- aplicar adecuadamente funciones numéricas incorporadas de uso frecuente;
- conectar entrada de texto, conversión de tipos y cálculo numérico;
- reconocer cuándo una operación textual o numérica produce un valor de resultado sin modificar el valor original.

## Capítulo actual

Continúa con [`int`, `float` y `bool`](03-int-float-and-bool/README.es.md). Profundiza en el comportamiento de enteros y punto flotante, división verdadera y por piso, restos, aproximación de punto flotante, valores de verdad y la relación entre `bool` e `int`.

## Estructura del directorio

```text
strings-and-numbers/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-string-creation-and-indexing/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── fixed_position_text.py
│       └── string_basics.py
├── 02-common-string-methods/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── normalize_text.py
│       └── split_and_join.py
└── 03-int-float-and-bool/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── numeric_behavior.py
        └── truth_and_precision.py
```

El árbol representa archivos que existen actualmente. Los capítulos planificados aparecen en la ruta de aprendizaje, pero no se muestran como directorios hasta que se agrega su contenido.
