# Phase II: Learning Hub Foundation — especificación

[🇺🇸 English](specification.md) · [🇧🇷 Português](specification.pt-BR.md) · [🇪🇸 Español](specification.es.md)

Estado: propuesta para revisión. Dirección aprobada el 25/11/2026. Base: main en 86f1c8517ef8e0e51d97e03388075a4d3fe41386.

## Propósito

Mejorar Python Study Guide como guía independiente y permitir que el futuro Learning Hub del sitio personal consuma el contenido, sin implementar aquí el sitio. Apoyar práctica manual, entrevistas técnicas internacionales y estudio independiente en GitHub.

## Base

La fundación original y las fases educativas 1–10 están completas según el roadmap existente. La auditoría encontró 57 directorios de capítulos y 8 proyectos, cada uno con README EN/PT-BR/ES (195 archivos), 498 archivos versionados y 221 archivos Python. La presencia de archivos no demuestra equivalencia de traducciones. El workflow de calidad de main del 10/11/2026 fue exitoso (ejecución 42921078332); no se ejecutaron nuevas pruebas durante la auditoría. Las cifras históricas de badges corresponden a la ejecución 34731456104, no a conteos actuales.

Los recursos visuales existentes, [ruta de aprendizaje](../../learning-path.es.md), [roadmap](../../roadmap.es.md), [estructura](../../project-structure.es.md), [instrucciones de agentes](../../../docs/localized/AGENTS.es.md), [plantilla de PR](../../../.github/pull_request_template.es.md) y scripts de calidad siguen siendo oficiales dentro de sus alcances.

## Requisitos funcionales

| ID | Requisito |
| --- | --- |
| FR-01 | Navegación anterior/índice/siguiente en ubicaciones coherentes, con transiciones entre módulos y límites inicial/final en los tres idiomas. |
| FR-02 | Introducir Getting Started (orden curricular 00) antes de Fundamentals sin renumerar rutas existentes. Cubrir descargas oficiales Python y VS Code, Windows/macOS/Linux, PATH cuando proceda, verificación en terminal, extensión Python, selección de intérprete, carpetas, archivos .py, terminal integrado, primera ejecución manual y resolución de problemas. VS Code recomendado, no obligatorio. Reutilizar Fundamentals para la enseñanza conceptual de Hello World. |
| FR-03 | Actualizar los tres README, rutas, roadmap, estructura y requisitos previos según corresponda; preservar banner, lema, autoría y orientación técnica relevante. Las cifras de badges deben proceder de validaciones exitosas identificadas. |
| FR-04 | Enseñar programación manual, interpretación de errores, documentación oficial, pruebas, intentos independientes, requisitos, especificaciones, planes, tareas, criterios de aceptación, ADR y revisión. Explicar complementariedad entre SDD y TDD; elegir ubicación tras verificar solapamientos. |
| FR-05 | Añadir fase curricular 11, Problem Solving & Live Coding: razonamiento, cadenas/números, colecciones, funciones/recursión, búsqueda/ordenación, algoritmos/complejidad, depuración, refactorización, retos mixtos y práctica cronometrada. Easy/Medium/Hard; pistas progresivas, soluciones de referencia, complejidad y pruebas con casos límite. Antes de cualquier reto afectado, mapear requisitos previos a las lecciones existentes y enseñar conceptos ausentes (incluidas recursión, búsqueda/ordenación y complejidad algorítmica) en los tres idiomas; enlazar la enseñanza antes de la práctica. |
| FR-06 | Añadir fase curricular 12, Technical Interview Preparation: proceso de entrevista, fundamentos, estructuras de datos, OOP, internals, memoria, excepciones, pruebas/depuración, APIs/backend, bases/SQL, ingeniería, comportamiento, take-home, simulaciones junior/mid/senior, entrevistas internacionales e inglés técnico. Incluir respuestas esperadas, explicaciones, objetivos, errores comunes, preguntas adicionales, ejemplos, simulaciones de 30/45/60 minutos y rúbricas objetivas de autoevaluación. |
| FR-07 | Ofrecer cuestionarios y contratos de ejercicios legibles por máquinas, IDs estables, tres idiomas, corrección objetiva de tipos admitidos, código Python original compartido y soluciones probadas contra respuestas incorrectas representativas. Preservar uso en GitHub y local. |
| FR-08 | Ofrecer manifiesto versionado, esquemas, relaciones, títulos traducidos, rutas, recursos, asociaciones de ejercicios/cuestionarios/simulaciones y compatibilidad de navegador. Consumir revisión inmutable validada, sin scraping del HTML GitHub. |
| FR-09 | Validar contenido nuevo y afectado, entregando handoff con revisión aprobada, contratos, registros de ejemplo, resultados, limitaciones y pendientes. |

## Requisitos no funcionales

- NFR-01: ningún coste financiero adicional, servidor/servicio/API de pago ni implementación web en este repositorio.
- NFR-02: sin duplicación innecesaria; código compartido en inglés; toda documentación pública en tres idiomas, incluida arquitectura e ingeniería. Documentación privada fuera del repositorio público, preferiblemente en inglés.
- NFR-03: preservar rutas y funcionalidad; validar enlaces, navegación, ejemplos y pruebas.
- NFR-04: IDs estables independientes del orden, rutas relativas confinadas al repositorio, esquema versionado y trazabilidad de revisión.
- NFR-05: sin corrección por IA; respuestas públicas solo ocultas visualmente; respuestas abiertas con referencias y autoevaluación.
- NFR-06: ejecución en navegador opcional por ejercicio, sujeta a verificación del entorno; Python local admitido. Sin secretos ni ejemplos confidenciales.
- NFR-07: nunca declarar aprobada una prueba no ejecutada. Reutilizar CI y añadir controles incrementalmente.

## Límites de alcance

Incluidos: contenido, metadatos, validación y handoff. Excluidos: interfaz del sitio, autenticación, sincronización en nube, ejecución en servidor, pago, certificación, despliegue de producción y evaluación semántica automatizada.

OOP, SQL, algoritmos e internals no se enseñan todos en módulos propios actualmente. Introducir requisitos previos antes de evaluar; no presuponer dominio ni renumerar fases. La Phase 0 histórica sigue siendo Project Foundation; orden curricular 00 es Getting Started.

## Referencias

- [Constitución](../constitution.es.md)
- [Plan](implementation-plan.es.md)
- [Tareas](tasks.es.md)
- [Criterios de aceptación](acceptance-criteria.es.md)
- [Contrato](integration-contract.es.md)
- [Decisiones arquitectónicas](../../adr/README.es.md)
- [Handoff](handoff.es.md)
