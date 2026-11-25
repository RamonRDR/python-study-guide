# Pruebas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

Este directorio ya contiene pruebas de regresión de las herramientas de calidad del repositorio sin dependencias externas. GitHub Actions las ejecuta con:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Las pruebas protegen el procesamiento de enlaces Markdown y la validación de estructura, incluidos metadatos de recursos visuales, accesibilidad SVG y referencias locales seguras.

La documentación histórica preveía contenido educativo de pruebas, empezando por aserciones simples y después introduciendo `pytest` para ejemplos ejecutables y proyectos prácticos.

Las pruebas de regresión de navegación exigen el mismo orden de la ruta principal en los tres idiomas, enlaces exactos anterior/índice/siguiente al inicio y al final, transiciones entre módulos y cobertura de los README versionados de capítulos/proyectos. Ejecuta `python scripts/check_chapter_navigation.py` desde la raíz del repositorio para comprobar todo el currículo.
