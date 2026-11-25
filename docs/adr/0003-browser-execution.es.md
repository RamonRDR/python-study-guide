# ADR 0003: Ejecución y evaluación en el navegador

[🇺🇸 English](0003-browser-execution.md) · [🇧🇷 Português](0003-browser-execution.pt-BR.md) · [🇪🇸 Español](0003-browser-execution.es.md)

Estado: propuesto (dirección aprobada el 25/11/2026; revisión del PR pendiente).

## Contexto

La práctica interactiva no debe requerir infraestructura de pago adicional. La guía incluye Python portable y ejemplos específicos de plataforma.

## Decisión

Usar Pyodide con entorno de ejecución fijado y Web Worker en el proyecto separado del sitio, solo para ejercicios con compatibilidad verificada. Mantener ejecución local. Usar pruebas deterministas, comparación objetiva de cuestionarios y rúbricas de autoevaluación. No implementar entrevistador ni evaluación semántica por IA. Guardar el progreso localmente en el navegador por defecto.

## Alternativas

Docker/Python remoto (rechazado por coste y operación); evaluación por IA (fuera del alcance); guía solo en navegador (rechazado, pues el material específico de plataforma debe seguir siendo utilizable).

## Consecuencias

El proyecto del sitio debe validar inicio del entorno, paquetes, diferencias de SO, aislamiento, interrupción y límites de salida. Los Workers por sí solos no garantizan aislamiento seguro. Las respuestas públicas pueden inspeccionarse; el progreso local puede perderse. Los costes dependen de los límites del alojamiento existente; no se promete capacidad ilimitada.
