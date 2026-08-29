<div align="center">

# Fase 9: Bibliotecas Externas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al repositorio](../docs/localized/README.es.md)

La Fase 9 introduce paquetes de terceros después de completar las bases del lenguaje Python y de la biblioteca estándar.

Las bibliotecas externas agregan una nueva responsabilidad de ingeniería: **contratos de dependencias**. Un programa pasa a depender no solo de Python, sino también de versiones de paquetes, estado de instalación, release notes y límites de compatibilidad.

## Estado

> 🚧 **En progreso**

## Ruta de aprendizaje

1. ✅ [`pandas`: Trabajando con Datos Tabulares](01-pandas/README.es.md)
2. ✅ [`openpyxl`: Automatizando Libros de Excel](02-openpyxl/README.es.md)
3. ⏳ `requests`: clientes HTTP y consumo de APIs
4. ⏳ `pytest`: pruebas automatizadas

## Contrato de dependencias

Los ejemplos ejecutables publicados en esta fase usan las dependencias declaradas en [`requirements-external.txt`](../requirements-external.txt). El CI del repositorio instala ese archivo antes de ejecutar los ejemplos aprobados de bibliotecas externas.

Los contratos actuales apuntan a **pandas 3.0.x** y **openpyxl 3.1.x**. pandas 3.0 soporta Python 3.11+, mientras PyPI declara Python 3.8+ para openpyxl 3.1.5. Este repositorio valida los ejemplos en Python 3.13.

## Por qué esta fase viene ahora

Las fases anteriores establecieron colecciones, funciones, errores, archivos, módulos, CSV/JSON, fechas, rutas, logging, iteración, aritmética decimal y contratos de filesystem. Las bibliotecas externas deben construir sobre esas habilidades, no sustituirlas.

El próximo capítulo planificado es **`requests`**.
