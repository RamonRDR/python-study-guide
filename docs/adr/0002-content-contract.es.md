# ADR 0002: Contrato de contenido versionado

[🇺🇸 English](0002-content-contract.md) · [🇧🇷 Português](0002-content-contract.pt-BR.md) · [🇪🇸 Español](0002-content-contract.es.md)

Estado: dirección arquitectónica aceptada ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)); ejecución en navegador sigue sin verificar.

## Contexto

Markdown ofrece una buena experiencia de lectura, pero por sí solo es insuficiente para navegación programática fiable, corrección de cuestionarios y asociación de ejercicios.

## Decisión

Usar registros JSON y un manifiesto curricular versionado que referencie archivos existentes, con IDs estables independientes del orden, campos localizados y referencias validadas. Mantener scripts/example_manifest.txt como lista de ejecución autorizada. Definir registros preliminares antes de los pilotos; finalizar esquemas con ejemplos reales y pruebas en los Sprints 07–08.

## Alternativas

Inferir metadatos de nombres/Markdown (frágil); duplicar Python por idioma (coste de mantenimiento); sustituir Markdown por JSON exclusivo (perjudica el uso en GitHub).

## Consecuencias

Los validadores deben detectar errores de esquema, referencias huérfanas, rutas inseguras, duplicados e idiomas ausentes. El contenido educativo sigue disponible en GitHub; los registros estructurados son canónicos cuando proceda, prefiriendo vistas generadas o referencias a duplicar texto manualmente.
