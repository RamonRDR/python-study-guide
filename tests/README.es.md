# Pruebas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

Este directorio contiene pruebas de regresión de las herramientas de calidad del repositorio, incluido el contrato de evaluación. Instala `requirements-assessment.txt` en un entorno virtual antes de ejecutar la suite. GitHub Actions la ejecuta con:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Las pruebas protegen el procesamiento de enlaces Markdown y la validación de estructura, incluidos metadatos de recursos visuales, accesibilidad SVG y referencias locales seguras.

La documentación histórica preveía contenido educativo de pruebas, empezando por aserciones simples y después introduciendo `pytest` para ejemplos ejecutables y proyectos prácticos.

Las pruebas de regresión de navegación exigen el mismo orden de la ruta principal en los tres idiomas, enlaces exactos anterior/índice/siguiente al inicio y al final, transiciones entre módulos y cobertura de los README versionados de capítulos/proyectos. Ejecuta `python scripts/check_chapter_navigation.py` desde la raíz del repositorio para comprobar todo el currículo.

Las pruebas de fundamentos exigen asignación aprobada por lección/dificultad, cobertura exacta del índice y calificación determinista; ejecutan fixtures literales confiables, nunca código arbitrario cargado de los registros. Las regresiones del piloto siguen cubiertas.

La suite de expansión comprueba la matriz completa de 160 preguntas, 2.850 XP, 82 nuevos fixtures de respuestas, fixtures literales de código confiables, diversidad de tipos y los tres índices localizados. Las regresiones de fundamentos y piloto siguen activas; no se ejecuta código del alumno.

La suite de migración comprueba el índice completo de 30 registros, los 192 casos existentes, flags explícitos sin alias, enteros grandes exactos, modalidades, metadatos de tiempo y referencias/candidatos incorrectos confiables. El índice histórico de 29 entradas y su suite de regresión siguen intactos. El runtime del navegador y la aplicación de timeout no se prueban aquí.
