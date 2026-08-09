<div align="center">

# Colecciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta sección es la Fase 3 de la secuencia principal de aprendizaje de Python Study Guide. Parte de textos y números para enseñar cómo varios valores relacionados pueden organizarse en colecciones antes de que el flujo del programa introduzca iteración repetida y ramificaciones.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Nivel | Estado |
|---|---|---|---|
| [01. Creación, indexación y slicing de listas](01-list-creation-and-indexing/README.es.md) | Crear colecciones ordenadas y leer elementos individuales y rangos | Principiante | Disponible |
| 02. Modificar listas y métodos comunes de listas | Cambiar deliberadamente el contenido de listas y comprender la mutación | Principiante | Planificado |
| 03. Tuplas e inmutabilidad | Usar secuencias inmutables y compararlas con listas | Principiante | Planificado |
| 04. Diccionarios: claves y valores | Organizar valores mediante claves significativas en lugar de posiciones | Principiante | Planificado |
| 05. Conjuntos y valores únicos | Trabajar con elementos únicos y operaciones de pertenencia de conjuntos | Principiante | Planificado |
| 06. Elegir la colección correcta | Comparar listas, tuplas, diccionarios y conjuntos según la intención | Principiante | Planificado |

## ¿Por qué este orden?

La ruta desarrolla una idea a la vez:

```text
one value
    ↓
ordered group of values
    ↓
changing an ordered group
    ↓
immutable ordered group
    ↓
key -> value relationships
    ↓
unique-value collections
    ↓
choose by intent
```

Las listas aparecen primero porque su indexación y slicing reutilizan el modelo de secuencia de la Fase 2. La mutación se separa en un segundo capítulo para que una persona principiante comprenda primero la forma de una lista antes de aprender todas las maneras de modificarla.

Las tuplas hacen explícita la diferencia entre mutabilidad e inmutabilidad. Los diccionarios introducen un cambio conceptual mayor desde posiciones numéricas hacia claves. Los conjuntos vienen después porque son colecciones cuyo modelo principal no es la indexación posicional. El capítulo final reúne las cuatro opciones.

## Orientación de prerrequisitos

- **01. Creación, indexación y slicing de listas:** completa primero las Fases 1 y 2. Debes comprender variables, tipos incorporados comunes, `len()`, índices enteros, slicing de strings, valores booleanos y funciones numéricas incorporadas comunes.
- **02. Modificar listas y métodos comunes de listas:** completa primero el Capítulo 01 para aprender mutación sobre un modelo de secuencia ya estable.
- **03. Tuplas e inmutabilidad:** completa los dos capítulos de listas para que el contraste entre secuencias mutables e inmutables tenga una referencia concreta.
- **04. Diccionarios: claves y valores:** completa primero los capítulos de secuencias. Este capítulo cambia el modelo de búsqueda de posiciones a claves.
- **05. Conjuntos y valores únicos:** completa primero el capítulo de diccionarios. Los conjuntos eliminan la búsqueda posicional y se centran en pertenencia y unicidad.
- **06. Elegir la colección correcta:** completa los cinco capítulos anteriores para que la comparación se base en conceptos que ya has practicado.

Al seguir la ruta completa, estudia los capítulos en orden numérico.

## Objetivos de la sección

Al final de la Fase 3, deberías poder:

- crear y leer listas con confianza;
- modificar listas deliberadamente y reconocer cambios realizados sobre el mismo objeto;
- explicar la diferencia entre listas mutables y tuplas inmutables;
- almacenar y recuperar valores mediante claves de diccionario;
- usar conjuntos cuando la unicidad y la pertenencia sean centrales;
- reconocer qué tipos de colección son posicionales y cuáles no;
- elegir una colección según la relación entre los valores y no solo por familiaridad con la sintaxis;
- entrar en la Fase 4 preparado para usar bucles y condicionales con colecciones que ya comprendes.

## Límite de alcance

La Fase 3 se centra en la estructura de las colecciones y en operaciones básicas.

Intencionalmente **no** enseña:

- bucles `for` o `while`;
- comprensiones de listas, diccionarios o conjuntos;
- `enumerate()` o `zip()`;
- callbacks avanzados de ordenación;
- clases de colección personalizadas.

Estas ideas resultan más sencillas después de comprender primero qué contienen las colecciones y cómo organiza sus valores cada colección.

## Estado de la sección

La Fase 3 está **en progreso**. El Capítulo 01 está disponible en inglés, portugués de Brasil y español. Los Capítulos 02 a 06 siguen planificados y se añadirán como capítulos completos y revisables, sin placeholders vacíos.

## Estructura actual del directorio

```text
collections/
├── README.md
├── README.pt-BR.md
├── README.es.md
└── 01-list-creation-and-indexing/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── list_basics.py
        └── list_slicing.py
```
