<div align="center">

# Fundamentos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta sección inicia la secuencia principal de aprendizaje de Python Study Guide. No presupone experiencia previa en programación y construye el modelo mental necesario para escribir, guardar, ejecutar, analizar y ampliar gradualmente programas de Python.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Nivel | Estado |
|---|---|---|---|
| [01. Cómo ejecuta Python un programa](01-how-python-runs-a-program/README.es.md) | Crear, ejecutar, modificar y corregir un primer archivo de Python | Principiante absoluto | Disponible |
| [02. `print()` e `input()`](02-print-and-input/README.es.md) | Mostrar información y recibir texto de una persona usuaria | Principiante absoluto | Disponible |
| [03. Variables y nombres](03-variables-and-naming/README.es.md) | Almacenar valores y elegir identificadores comprensibles | Principiante | Disponible |
| [04. Tipos de datos incorporados](04-built-in-data-types/README.es.md) | Reconocer categorías comunes de valores y su notación en el código fuente | Principiante | Disponible |
| 05. `type()` e `isinstance()` | Inspeccionar y verificar tipos de valores | Principiante | Planificado |
| 06. Conversión de tipos | Convertir valores compatibles de forma deliberada | Principiante | Planificado |

## Orientación de prerrequisitos

- **01. Cómo ejecuta Python un programa:** no se requiere experiencia previa en programación. Python debe estar instalado, y la persona estudiante necesita acceso a un editor de texto plano o de código y a una terminal.
- **02. `print()` e `input()`:** completa primero el Capítulo 01. La persona estudiante debe poder crear, guardar y ejecutar un archivo `.py` desde la terminal.
- **03. Variables y nombres:** completa primero el Capítulo 02. La persona estudiante debe comprender `print()`, `input()` y por qué el resultado de una entrada debe almacenarse antes de reutilizarse.
- **04. Tipos de datos incorporados:** completa primero el Capítulo 03. La persona estudiante debe comprender la asignación, la reasignación y cómo los nombres de variables referencian valores.
- Los capítulos posteriores dependen de la capacidad de almacenar, mostrar, reconocer e inspeccionar valores mediante nombres claros.

Estudia los capítulos en orden numérico cuando sigas la ruta completa.

```text
01. Cómo ejecuta Python un programa
        ↓
02. print() e input()
        ↓
03. Variables y nombres
        ↓
04. Tipos de datos incorporados
        ↓
05. type() e isinstance()
        ↓
06. Conversión de tipos
```

## Objetivos de la sección

Al final de esta ruta, deberías poder:

- crear y ejecutar archivos de código fuente de Python;
- mostrar información y recibir entradas básicas;
- almacenar valores usando nombres de variables significativos;
- reconocer tipos de datos incorporados comunes;
- inspeccionar valores con `type()` e `isinstance()`;
- convertir valores compatibles entre tipos básicos;
- leer salidas simples y mensajes básicos de error.

## Capítulo actual

Continúa con [Tipos de Datos Incorporados](04-built-in-data-types/README.es.md). El capítulo explica valores y tipos, notación en el código fuente, `str`, `int`, `float`, `bool`, `None`, valores con apariencia similar y comportamientos dependientes del tipo.

## Estructura del directorio

```text
fundamentals/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-how-python-runs-a-program/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       └── hello_world.py
├── 02-print-and-input/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── interactive_greeting.py
│       └── output_basics.py
├── 03-variables-and-naming/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── learning_profile.py
│       └── variable_basics.py
└── 04-built-in-data-types/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── same_looking_values.py
        └── value_catalog.py
```
