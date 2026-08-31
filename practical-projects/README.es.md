<div align="center">

# Proyectos Prácticos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a la página principal del repositorio](../docs/localized/README.es.md)

La Fase 10 combina conceptos de las fases anteriores en flujos completos y comprobables. Los proyectos enfatizan requisitos, decisiones de diseño, implementación, validación, caminos de extensión y comunicación de portafolio.

## Estado

> 🚧 **En progreso**

## Ruta de proyectos

1. ✅ [Control de Gastos](01-expense-tracker/README.es.md)
2. ✅ [Calculadora de Notas](02-grade-calculator/README.es.md)
3. ✅ [Registro de Usuarios](03-user-registration/README.es.md)
4. ✅ [Analizador CSV](04-csv-analyzer/README.es.md)
5. ✅ [Generador de Informes](05-report-generator/README.es.md)
6. 🚧 [Organizador de Archivos](06-file-organizer/README.es.md)
7. ⏳ Flujo Ficticio de Conciliación
8. ⏳ Flujo Simulado de Automatización

## Contrato de los proyectos

Cada proyecto debe incluir:

- requisitos explícitos;
- notas de diseño y trade-offs;
- implementación funcional;
- demostración determinista cuando corresponda;
- pruebas automatizadas del comportamiento importante;
- explicación de caminos de fallo;
- desafíos de extensión;
- discusión de portafolio.

El Proyecto 01 establece el patrón de integración con registros monetarios validados y persistencia. El Proyecto 02 amplía ese patrón con políticas de calificación configurables, agregación ponderada exacta, estados parcial/final explícitos, informe estructurado y cobertura pytest centrada en límites. El Proyecto 03 añade datos de identidad canónicos, prevención de duplicados, índices secundarios de lookup, actualizaciones seguras de campos indexados y transiciones explícitas del ciclo de vida sin introducir autenticación. El Proyecto 04 añade schemas CSV exactos, conversión tipada, separación entre fallos estructurales y fallos de fila, parsing con éxito parcial, identificadores duplicados, filtros deterministas y agregación sin ocultar la ingestión detrás de pandas. El Proyecto 05 transforma registros operativos validados en artefactos de informe deterministas con ventanas de fecha explícitas, métricas de resumen exactas, renderizadores TXT/Markdown y escritura UTF-8, manteniendo separadas la agregación, la presentación y la persistencia. El Proyecto 06 añade descubrimiento superficial del filesystem, clasificación por sufijo, planificación inmutable de movimientos, políticas explícitas de colisión, fronteras de symlink, revalidación en el momento de ejecución y protección exacta no-replace del destino antes de organizar los archivos en carpetas por categoría.
