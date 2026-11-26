# Contrato de integración del Learning Hub

[🇺🇸 English](integration-contract.md) · [🇧🇷 Português](integration-contract.pt-BR.md) · [🇪🇸 Español](integration-contract.es.md)

Estado: preliminar para el manifiesto del consumidor y fixtures de integración en Sprint 08. Los esquemas y registros versionados de evaluación siguen el [contrato de evaluación](assessment-contract.es.md). Aquí no se implementa integración de ejecución.

## Versión y transporte

El repositorio público es oficial. El consumidor importa contenido al compilar usando SHA de commit Git inmutable aprobado (una etiqueta puede identificar SHA). Registra revisión y schema_version, rechaza versiones major no admitidas y falla la compilación con datos inválidos en vez de mezclar revisiones silenciosamente. JSON y Markdown UTF-8, sin scraping HTML GitHub. Sin llamadas a API por visitante ni servicios de pago.

## Convenciones compartidas

- Locales: en (predeterminado), pt-BR, es. Campos visibles al estudiante requieren tres traducciones; archivos Python e IDs compartidos en inglés.
- IDs: cadenas ASCII minúsculas con puntos/guiones; estables, independientes de título/orden; nunca reutilizar ID para otro elemento. Unicidad por tipo, referencias tipadas por campo.
- Rutas POSIX relativas al repositorio; sin absolutas, recorridos de directorio, barras invertidas, esquemas URL ni escape por symlink. Verificar existencia/confinamiento antes de importar. Renderizar Markdown/HTML de forma segura, resolver enlaces/recursos en la misma revisión y sanear contenido no confiable.
- Órdenes: enteros no negativos explícitos, únicos entre hermanos; anterior/siguiente sigue orden curricular, no lexicográfico. Extremos con vecinos null.
- Metadatos opcionales con valores predeterminados explícitos; no presuponer capacidad no admitida.

## Modelo preliminar de registros

| Entidad | Campos obligatorios del piloto |
| --- | --- |
| Currículo | schema_version, default_locale, supported_locales, modules |
| Módulo | id, order, slug, title (mapa de idiomas), index (mapa de rutas por idioma), chapters |
| Capítulo | id, order, slug, title, content (mapa de rutas por idioma), assets, previous_id, next_id, exercise_ids, quiz_ids, interview_ids, execution |
| Cuestionario | id, chapter_id, difficulty, type, prompt (mapa de idiomas), choices (IDs estables y texto traducido cuando corresponda), answer, explanation, hints, xp |
| Ejercicio | id, chapter_id, difficulty, estimated_minutes, title, prompt, concepts, constraints, examples, starter_path o texto inicial, hints, solution_path, explanation, complexity (tiempo/espacio cuando tenga sentido), tests, execution, allowed_dependencies |
| Pregunta de entrevista | id, topic, level, prompt, expected_answer, explanation, intent, common_errors, follow_ups, examples, rubric |
| Simulación | id, level, duration_minutes (30/45/60), question_ids, exercise_ids, rúbrica de puntuación |

Campos localizados incluyen explicaciones visibles, alternativas, ejemplos con prosa, pistas, descripciones de puntuación y rúbricas. Usar IDs para referencias internas cuando sea posible. Tipos: multiple_choice, true_false, error_identification, output_prediction, objective_code_completion. Dificultad: easy/medium/hard. Respuestas usan IDs estables de opciones, booleanos o cadenas aceptadas explícitas según tipo. XP es entero no negativo, orientativo, no certificación.

## Ejemplo (ilustrativo, no manifiesto publicado)

```json
{
  "id": "fundamentals.print-and-input",
  "order": 2,
  "slug": "print-and-input",
  "content": {
    "en": "fundamentals/02-print-and-input/README.md",
    "pt-BR": "fundamentals/02-print-and-input/README.pt-BR.md",
    "es": "fundamentals/02-print-and-input/README.es.md"
  },
  "previous_id": "fundamentals.how-python-runs-a-program",
  "next_id": "fundamentals.variables-and-naming",
  "execution": "unverified"
}
```

El fragmento omite otros metadatos obligatorios y no es un registro completo válido por esquema. Rutas existentes; IDs propuestos.

## Corrección y ejecución

Corrección de cuestionarios determinista. Comparar valores canónicos exactos por defecto; normalizar saltos de línea o espacios solo cuando la pregunta lo permite explícitamente. Pruebas de código declaran interfaz de llamada de función o stdin/stdout, entradas/salidas compatibles con JSON, reglas de comparación (tolerancia solo si especificada), casos límite y límites de ejecución. Validar discriminación con soluciones de referencia e incorrectas representativas. No ejecutar código arbitrario del estudiante en CI del repositorio.

Valores execution: browser_compatible (verificado en entorno fijado), local_only (documentar motivo), unverified (predeterminado; sin ejecución automática en navegador). Python local y dependencias permitidas explícitos. Compatibilidad por ejercicio, no inferida de todo código del capítulo. Archivos, red, bibliotecas externas y ejemplos específicos de SO requieren evaluación individual.

Consumidor: ejecutar código fuera del hilo de interfaz en Web Worker dedicado; limitar tiempo y salida, terminar/recrear ante timeout o cancelación, evitar exposición de credenciales privilegiadas y aislar del origen principal cuando sea necesario. Worker solo no es frontera de seguridad; evaluar acceso a red/almacenamiento y sandbox antes del despliegue. Sin afirmar aislamiento rígido de memoria. Probar versión y soporte de navegador en el proyecto del sitio. Sin ejecución en servidor en esta fase.

Soluciones y pruebas públicas son inspeccionables; revelar pistas/soluciones bajo demanda, no como garantía de seguridad. Preguntas abiertas usan referencias y rúbricas de autoevaluación, nunca corrección semántica automática.

## Responsabilidades

Guía: Markdown, metadatos, ejemplos, soluciones, pruebas, rúbricas y validación de esquemas. Sitio: renderizador seguro, editor, entorno, interfaz de corrección determinista, progreso local, accesibilidad y despliegue. Almacenamiento local específico del dispositivo y puede borrarse; sin sincronización backend presupuesta.

## Decisiones pendientes

Finalizar estructura, esquemas completos, política de versiones, semántica exacta de puntuación/comparación, renderizado seguro y entorno fijado tras pilotos. Documentar compatibilidad y ejemplos de migración en handoff final. Ver [ADR](../../adr/README.es.md).
