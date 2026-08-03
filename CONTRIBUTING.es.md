<div align="center">

# Cómo contribuir a Python Study Guide

[🇺🇸 English](CONTRIBUTING.md) · [🇧🇷 Português](CONTRIBUTING.pt-BR.md) · [🇪🇸 Español](CONTRIBUTING.es.md)

</div>

Gracias por ayudar a mejorar este proyecto de aprendizaje.

## Principios fundamentales

- Mantén los identificadores del código y los nombres de los archivos en inglés.
- Prefiere explicaciones claras antes que textos innecesariamente elaborados.
- Explica por qué y cuándo utilizar un recurso, no solamente cómo utilizarlo.
- Utiliza ejemplos originales creados para este repositorio.
- Mantén las tres versiones de idioma conceptualmente alineadas.
- Nunca incluyas datos confidenciales, propietarios o personales.

## Flujo de contribución

1. Crea o elige una issue que describa la mejora.
2. Crea una branch específica a partir de `main`.
3. Realiza commits pequeños y fáciles de revisar.
4. Actualiza todos los documentos de idioma afectados.
5. Ejecuta los ejemplos y las pruebas que hayan sido modificados.
6. Abre un pull request explicando qué cambió y por qué.

## Nombres de branches

```text
feat/topic-name
docs/topic-name
fix/topic-name
test/topic-name
refactor/topic-name
```

Los nombres de las branches deben permanecer en inglés para seguir el estándar internacional adoptado por el proyecto.

## Mensajes de commit

Utiliza mensajes breves con el estilo de Conventional Commits:

```text
docs: add chapter about comments
feat: add string validation example
fix: correct average calculation
```

## Formato de los capítulos

Los nuevos capítulos de aprendizaje deben incluir:

1. Qué es
2. Por qué existe
3. Sintaxis
4. Cuándo utilizarlo
5. Cuándo evitarlo
6. Cómo se conecta con otros recursos
7. Ejemplo básico
8. Ejemplo práctico
9. Errores comunes
10. Ejercicio
11. Resumen de consulta rápida

## Idiomas

El inglés es el idioma predeterminado del repositorio. Las traducciones al portugués de Brasil y al español deben conservar el mismo significado técnico, sin exigir una traducción literal palabra por palabra.

Al modificar documentación traducida, actualiza todas las versiones de idioma afectadas siempre que sea posible. Si una traducción no puede completarse en el mismo pull request, identifica claramente qué versión falta.

## Contribuciones asistidas por IA

Las herramientas de IA pueden utilizarse para apoyar la investigación, la redacción, la traducción, la programación, las pruebas y la revisión.

Quien contribuye sigue siendo responsable de comprender, comprobar, probar y verificar todo lo enviado. No envíes contenido generado automáticamente sin una revisión humana significativa.

Antes de enviar trabajo asistido por IA:

- verifica las afirmaciones técnicas importantes en fuentes confiables;
- ejecuta los ejemplos y las pruebas relevantes;
- revisa todas las versiones de idioma afectadas;
- informa las incertidumbres o cualquier elemento que no haya podido verificarse;
- elimina material confidencial, personal o propietario;
- confirma que la contribución cumple las licencias aplicables.

Lee la [guía de desarrollo asistido por IA](docs/ai-assisted-development/README.es.md) para conocer las prácticas del proyecto sobre prompts, validación, privacidad y revisión.

## Estilo del código

- Utiliza nombres descriptivos en inglés.
- Sigue PEP 8.
- Añade type hints cuando mejoren la comprensión.
- Comenta decisiones, restricciones y motivos que no sean evidentes.
- No comentes código que ya se explica por sí mismo.

## Pull requests

Un pull request debe ser específico, fácil de revisar y libre de cambios no relacionados. Se pueden incluir capturas de pantalla cuando el diseño de la documentación se vea afectado.

Antes de enviarlo, confirma que:

- los enlaces funcionan correctamente;
- los ejemplos se ejecutan como se describe;
- la terminología es coherente;
- los documentos traducidos continúan conceptualmente alineados;
- el material asistido por IA fue comprendido y verificado;
- no se incluyó material confidencial o propietario de terceros.

## Licencia de las contribuciones

Al enviar una contribución, aceptas que pueda distribuirse bajo la misma [Licencia MIT](LICENSE) utilizada por este repositorio.
