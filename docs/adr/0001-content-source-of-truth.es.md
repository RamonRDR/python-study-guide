# ADR 0001: Fuente única de verdad del contenido

[🇺🇸 English](0001-content-source-of-truth.md) · [🇧🇷 Português](0001-content-source-of-truth.pt-BR.md) · [🇪🇸 Español](0001-content-source-of-truth.es.md)

Estado: dirección arquitectónica aceptada ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)); ejecución en navegador sigue sin verificar.

## Contexto

La guía actual se puede usar de forma independiente en tres idiomas. El futuro sitio necesita el mismo material sin mantener copias manualmente ni acoplar la guía al sitio.

## Decisión

Mantener el repositorio GitHub como fuente oficial de Markdown, Python y datos estructurados. Importar revisiones inmutables y validadas durante la compilación del sitio. Preservar las rutas existentes y el uso en GitHub y localmente. Mantener la implementación del sitio fuera de este repositorio.

## Alternativas

Contenido separado mantenido manualmente en el sitio (rechazado: divergencia); llamadas a la API GitHub en tiempo de ejecución por estudiante (rechazado como opción predeterminada: dependencia de disponibilidad y límites); scraping del HTML GitHub (rechazado: acoplamiento frágil a la presentación).

## Consecuencias

El consumidor necesita un proceso explícito de actualización/compilación, seguimiento de revisiones, renderizado seguro y validación. Las actualizaciones podrían no aparecer hasta una nueva compilación. No se prevé un nuevo servicio de pago.
