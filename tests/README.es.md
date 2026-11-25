# Pruebas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

Este directorio ya contiene pruebas de regresión de las herramientas de calidad del repositorio sin dependencias externas. GitHub Actions las ejecuta con:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Las pruebas protegen el procesamiento de enlaces Markdown y la validación de estructura, incluidos metadatos de recursos visuales, accesibilidad SVG y referencias locales seguras.

La documentación histórica preveía contenido educativo de pruebas, empezando por aserciones simples y después introduciendo `pytest` para ejemplos ejecutables y proyectos prácticos.
