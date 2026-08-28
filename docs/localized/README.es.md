<div align="center">

# Guía de Estudio de Python 🐍

### Estudia. Comprende. Practica.

<img src="../../assets/banner.png" alt="Identidad visual de Python Study Guide con una serpiente geométrica, llaves de código, un libro abierto y nodos de aprendizaje conectados." width="100%">

[🇺🇸 English](../../README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Una guía práctica y multilingüe para estudiar Python, comprender cómo se conectan sus partes y aplicar los conceptos mediante ejemplos claros.

Este proyecto funciona como ruta de aprendizaje y también como biblioteca de consulta rápida. En lugar de presentar comandos aislados, cada tema explica qué hace un recurso, por qué existe, cuándo utilizarlo, cuándo evitarlo y cómo funciona junto con otras partes de Python.

## ¿Por qué el código está escrito en inglés?

Los nombres de carpetas, archivos, variables, funciones, clases y otros identificadores están escritos en inglés. Esto ayuda a quienes están aprendiendo a familiarizarse con convenciones comunes en bibliotecas, documentación técnica y proyectos internacionales.

Las explicaciones están disponibles en inglés, portugués de Brasil y español.

## Cómo estudiar

Cada capítulo sigue una estructura consistente:

1. Qué es
2. Por qué existe
3. Sintaxis y convenciones
4. Cuándo utilizarlo
5. Cuándo evitarlo
6. Cómo se conecta con otros recursos
7. Ejemplos básicos y prácticos
8. Errores comunes
9. Ejercicio
10. Lista de revisión
11. Resumen de consulta rápida

## Ruta de aprendizaje

La guía crece desde los fundamentos de Python hasta funciones, documentación, manejo de errores, archivos, biblioteca estándar, bibliotecas externas, pruebas y proyectos prácticos.

- [Ruta completa de aprendizaje: enlaces directos a todos los capítulos publicados](../learning-path.es.md)
- [Roadmap en Español](../roadmap.es.md)
- [Roadmap in English](../roadmap.en.md)
- [Roadmap em Português](../roadmap.pt-BR.md)

## Estructura del proyecto

```text
python-study-guide/
├── assets/
├── comments-and-documentation/
├── collections/
├── docs/
├── errors-files-and-modules/
├── exercises/
├── external-libraries/
├── functions/
├── fundamentals/
├── practical-projects/
├── program-flow/
├── scripts/
├── standard-library/
├── strings-and-numbers/
└── tests/
```

Explicaciones detalladas:

- [Estructura del proyecto en Español](../project-structure.es.md)
- [Project structure in English](../project-structure.en.md)
- [Estrutura do projeto em Português](../project-structure.pt-BR.md)

## Estado actual

La base del proyecto está completada. La Fase 0 estableció la documentación multilingüe, el flujo de contribución, las plantillas de colaboración, los estándares de la comunidad, la autoría, la licencia, la gobernanza de IA, las verificaciones automáticas, la identidad visual original, la estructura escalable y la auditoría final de la base.

La base del proyecto y siete secciones educativas completas están disponibles, y la [Fase 8: Biblioteca Estándar](../../standard-library/README.es.md) está ahora en progreso con el [Capítulo 01: `pathlib`](../../standard-library/01-pathlib/README.es.md) y el [Capítulo 02: `datetime`](../../standard-library/02-datetime/README.es.md). La [Fase 7: Errores, Archivos y Módulos](../../errors-files-and-modules/README.es.md) está completada con cinco capítulos revisados. La [Fase 1: Fundamentos](../../fundamentals/README.es.md) ofrece seis capítulos revisados para principiantes. La Fase 6 reúne seis capítulos de aprendizaje revisados:

- [Comentarios en Python](../../comments-and-documentation/01-comments/README.es.md)
- [Docstrings en Python](../../comments-and-documentation/02-docstrings/README.es.md)
- [Nombres Significativos y Código Autoexplicativo](../../comments-and-documentation/03-meaningful-names/README.es.md)
- [Marcadores de Tareas y Seguimiento Técnico](../../comments-and-documentation/04-task-markers/README.es.md)
- [Comentarios frente a Logging en Python](../../comments-and-documentation/05-comments-vs-logging/README.es.md)
- [PEP 8 y Legibilidad en Python](../../comments-and-documentation/06-pep8-and-readability/README.es.md)

Las Fases 1, 2, 3, 4, 5, 6 y 7 están completadas. La Fase 8 está en progreso con [Trabajar con Rutas del Sistema de Archivos Usando `pathlib`](../../standard-library/01-pathlib/README.es.md) y [Trabajar con Fechas y Cálculos de Tiempo Usando `datetime`](../../standard-library/02-datetime/README.es.md). Juntos introducen trabajo de filesystem orientado a rutas y tipos explícitos de fecha/hora, duraciones, parsing, formato, conciencia de timezone, conversión UTC y aritmética de tiempo determinista. La Fase 7 reúne cinco capítulos revisados: manejo de excepciones; lanzamiento y excepciones personalizadas; uso seguro de archivos con `open()` y `with`; [Trabajar con TXT, CSV y JSON](../../errors-files-and-modules/04-txt-csv-and-json/README.es.md); y [Organizar Código con Imports, Módulos y Paquetes](../../errors-files-and-modules/05-imports-modules-and-packages/README.es.md), que cierra la fase con imports explícitos de módulos, estructura de paquete regular, main guard, contexto de búsqueda de imports, imports absolutos y relativos, `python -m` y diseño de dependencias. La Fase 5: Funciones reúne nueve capítulos revisados: [Definir y Llamar Funciones](../../functions/01-defining-and-calling-functions/README.es.md), [Parámetros y Argumentos](../../functions/02-parameters-and-arguments/README.es.md), [Valores de Retorno](../../functions/03-return-values/README.es.md), [Alcance](../../functions/04-scope/README.es.md), [Type Hints](../../functions/05-type-hints/README.es.md), [Valores Predeterminados](../../functions/06-default-values/README.es.md), [`*args` y `**kwargs`](../../functions/07-args-and-kwargs/README.es.md), [Funciones Trabajando Juntas](../../functions/08-functions-working-together/README.es.md) y [Flujo de Datos Entre Funciones](../../functions/09-data-flow-between-functions/README.es.md). Juntos establecen definición y llamada, flujo de entrada obligatorio, resultados retornados, alcance local y global, interfaces tipadas, entradas opcionales seguras, recolección intencionalmente flexible de argumentos posicionales y por palabra clave, composición mediante funciones auxiliares y coordinadoras y flujo explícito desde el llamador hacia parámetros y retornos, incluida la reasignación frente a la mutación. La Fase 4 permanece completada con ocho capítulos revisados de Flujo del Programa, terminando con [Elegir y Combinar el Flujo del Programa](../../program-flow/08-choosing-and-combining-program-flow/README.es.md). La Fase 3 reúne seis capítulos revisados de Colecciones, terminando con [Elegir la Colección Adecuada](../../collections/06-choosing-the-right-collection/README.es.md). La Fase 2 permanece completada con cuatro capítulos revisados, terminando con [Funciones Numéricas Incorporadas](../../strings-and-numbers/04-numeric-builtins/README.es.md). Consulta el [roadmap](../roadmap.es.md) o la [ruta completa de aprendizaje](../learning-path.es.md) para seguir el estado del currículo y acceder directamente a los capítulos.

## Identidad visual

El símbolo del proyecto conecta Python, código, aprendizaje y relaciones entre conceptos mediante una serpiente geométrica, llaves, un libro abierto y nodos conectados.

Consulta la [guía de identidad visual](../../assets/README.md) para conocer los archivos, la paleta, los significados, las orientaciones de accesibilidad y las reglas de uso.

## Desarrollo asistido por IA

Este proyecto utiliza herramientas de inteligencia artificial, incluidas ChatGPT y Codex, para apoyar la planificación, la investigación, la redacción, la traducción, la revisión y el mantenimiento del repositorio.

El contenido producido por IA no se acepta automáticamente. Cada cambio debe comprenderse, verificarse y revisarse antes de incorporarse a la rama `main`.

Las instrucciones generales están registradas en [AGENTS.md](../../AGENTS.md). Lee la [guía de desarrollo asistido por IA](../ai-assisted-development/README.es.md) para conocer el flujo responsable.

## Autoría y mantenimiento

Python Study Guide fue creado y es mantenido por [Ramon Estevez Rodriguez](https://github.com/RamonRDR).

Las contribuciones permanecen reconocidas en los metadatos de los commits, el historial de Git y los pull requests. Consulta el [registro de autoría del proyecto](AUTHORS.es.md).

## Comunidad y soporte

La participación se rige por el [Código de Conducta](CODE_OF_CONDUCT.es.md). La [Guía de Soporte](SUPPORT.es.md) explica qué canal corresponde a cada solicitud. Las posibles vulnerabilidades deben seguir el proceso privado de la [Política de Seguridad](SECURITY.es.md).

## Cómo contribuir

Las contribuciones, correcciones, ejemplos y mejoras de traducción son bienvenidas. Lee la [guía de contribución en español](CONTRIBUTING.es.md) antes de abrir un pull request. También están disponibles las versiones en [inglés](../../CONTRIBUTING.md) y [portugués](CONTRIBUTING.pt-BR.md).

## Licencia

Este proyecto está disponible bajo la [Licencia MIT](../../LICENSE).
