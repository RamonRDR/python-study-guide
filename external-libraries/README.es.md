<div align="center">

# Fase 9: Bibliotecas Externas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al repositorio](../docs/localized/README.es.md)

La Fase 9 introduce paquetes de terceros después de completar las bases del lenguaje Python y de la biblioteca estándar.

Las bibliotecas externas agregan una nueva responsabilidad de ingeniería: **contratos de dependencias**. Un programa pasa a depender no solo de Python, sino también de versiones de paquetes, estado de instalación, release notes y límites de compatibilidad.

## Estado

> ✅ **Completada**

## Ruta de aprendizaje

1. ✅ [`pandas`: Trabajando con Datos Tabulares](01-pandas/README.es.md)
2. ✅ [`openpyxl`: Automatizando Libros de Excel](02-openpyxl/README.es.md)
3. ✅ [`requests`: Consumiendo APIs HTTP](03-requests/README.es.md)
4. ✅ [`pytest`: Ingeniería de Pruebas Automatizadas](04-pytest/README.es.md)

## Contrato de dependencias

Los ejemplos ejecutables publicados en esta fase usan las dependencias declaradas en [`requirements-external.txt`](../requirements-external.txt). El CI del repositorio instala ese archivo antes de ejecutar los ejemplos aprobados de bibliotecas externas.

Los contratos publicados apuntan a **pandas 3.0.x**, **openpyxl 3.1.x**, **Requests 2.34.x** y **pytest 9.1.x**. pandas 3.0 soporta Python 3.11+, PyPI declara Python 3.8+ para openpyxl 3.1.5, y Requests 2.34.2 y pytest 9.1.1 requieren Python 3.10+. Este repositorio valida los ejemplos con Python 3.13.

## Lo que estableció esta fase

La Fase 9 pasó de la biblioteca estándar a cuatro fronteras de ingeniería con terceros: transformación de datos tabulares, automatización de libros de Excel, clientes HTTP/API y pruebas automatizadas. Cada capítulo trata la biblioteca como una dependencia versionada con contratos explícitos de comportamiento, seguridad y validación.

La siguiente fase es **Fase 10: Proyectos Prácticos**.
