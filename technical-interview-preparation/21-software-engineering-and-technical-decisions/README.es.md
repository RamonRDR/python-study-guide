# Ingeniería de software y decisiones técnicas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../20-transactions-indexes-and-sql-safety/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [manual-programming-practices/02-specification-driven-development](../../manual-programming-practices/02-specification-driven-development/README.es.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.es.md)
- [technical-interview-preparation/08-encapsulation-abstraction-and-solid](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.es.md)
- [technical-interview-preparation/20-transactions-indexes-and-sql-safety](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.es.md)

## Decisiones empiezan en el requisito

Separa comportamiento funcional de atributos de calidad (latencia, fiabilidad, mantenibilidad, seguridad, coste). Aclara restricciones y ejemplos de aceptación antes de código. SDD transforma necesidades en especificación, plan, tareas y criterios observables; TDD prueba comportamiento primero, observa fallo, implementa y refactoriza con pruebas verdes. No afirmes Red observado sin ejecutar. ADR registra contexto, alternativas, decisión y consecuencias. Prefiere diseño pequeño mantenible a abstracciones prematuras.

Para informe ficticio de progreso, requisito es contar IDs únicos de lecciones completadas para alumno suministrado. Historial vacío devuelve cero, IDs inválidos fallan, fallo de almacenamiento se propaga. Ejemplo inyecta callable que carga IDs, haciendo regla comprobable sin base real. Es regla de informe solo lectura, no API autenticada. Autorización corresponde a frontera protegida. Pruebas unitarias usan loaders falsos; pruebas de integración de repositorio real verificarían consulta y mapeo con base real.

## Compromisos y operación

| Decisión | Pregunta a hacer |
| --- | --- |
| Monolito modular vs servicios | ¿Escala/deploy independientes justifican complejidad de red y operación? |
| Caché vs lectura directa | ¿Qué desfase, invalidación y presupuesto de memoria son aceptables? |
| Sync vs async | ¿Carga medida espera I/O y dependencias son compatibles? |
| SQL vs otro modelo | ¿Qué patrones de integridad, consulta y acceso predominan? |

Define base y éxito medible; no deduzcas velocidad de etiquetas de arquitectura. Usa control de versiones con cambios enfocados, comprobaciones automatizadas CI, revisión y plan probado de deploy/rollback. Separa configuración de código, no subas secretos y aplica privilegio mínimo. Observabilidad combina logs estructurados, métricas y trazas para investigar fallos; registra contexto útil sin datos privados, observa latencia/errores y distingue síntomas de causas. Despliega migraciones compatibles deliberadamente; rollback de código puede no deshacer cambios de datos.

## Práctica

Escribe criterios de aceptación del informe, compara llamadas a base dentro de regla con loader inyectado, registra ADR breve y prueba fallo de dependencia. Explica alternativa, compromiso, medición y estrategia de rollback. Estudia guía Git dedicada por separado para flujos de plataforma avanzados; no hay requisito externo obligatorio.

**Referencia rápida:** aclara; especifica; prueba; elige por compromisos; observa; revisa y verifica.

## Ejemplo ejecutable compartido

[progress_report.py](examples/progress_report.py)

`python technical-interview-preparation/21-software-engineering-and-technical-decisions/examples/progress_report.py`

## Referencias oficiales

- [docs.python.org/3.13/library/unittest.html](https://docs.python.org/3.13/library/unittest.html)
- [docs.python.org/3.13/library/logging.html](https://docs.python.org/3.13/library/logging.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../20-transactions-indexes-and-sql-safety/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:bottom -->
