# Contrato de integración del Learning Hub

[🇺🇸 English](integration-contract.md) · [🇧🇷 Português](integration-contract.pt-BR.md) · [🇪🇸 Español](integration-contract.es.md)

Estado: contratos de manifiesto 1.0.0 y cuestionario/ejercicio 1.0.0 implementados; índices de entrevista/simulacro siguen preliminares 0.1.0. AC-08 cerrado. Las secciones 08A–E de abajo prevalecen sobre el modelo preliminar histórico; 09B validará y documentará la revisión exacta del consumidor. No se implementa runtime del sitio.

## Versión y transporte

El repositorio público es oficial. El consumidor importa contenido al compilar usando SHA de commit Git inmutable aprobado (una etiqueta puede identificar SHA). Registra revisión y schema_version, rechaza todas las versiones exactas no admitidas (incluidas minor o patch no admitidas) y falla la compilación con datos inválidos en vez de mezclar revisiones silenciosamente. JSON y Markdown UTF-8, sin scraping HTML GitHub. Sin llamadas a API por visitante ni servicios de pago.

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

## Sprint 08A · Manifiesto curricular 1.0.0

Las decisiones específicas del manifiesto abajo sustituyen el modelo preliminar anterior; los contratos de bancos no cambian.

Publicar `curriculum/manifest.json` con `schemas/curriculum-manifest.schema.json` (Draft 2020-12, versión 1.0.0 del manifiesto). Reutilizar la dependencia jsonschema y las funciones estrictas de JSON/rutas de evaluaciones. El manifiesto referencia archivos fuente sin duplicar lecciones ni evaluaciones. Los 115 IDs estables proceden de la matriz de evaluación; orden y títulos de las tres rutas. Preservar la base histórica separada del orden curricular 00, fases educativas 1–12 y módulo complementario. Los órdenes de módulos y capítulos son enteros desde cero, contiguos entre hermanos e independientes de los IDs; previous/next recorre todo el currículo.

El manifiesto incluye títulos localizados, rutas de índice/contenido, tipo de capítulo, recursos y assets, metadatos de ejecución, referencias tipadas de evaluación y descriptores de bancos canónicos. Los cuatro bancos mantienen versiones independientes: cuestionario/ejercicio 1.0.0, entrevista/simulacro 0.1.0. Referencias de entrevistas en capítulos indican prerrequisitos documentados, no propiedad; referencias de simulacros indican la lección de simulacros. Cuestionario/ejercicio usa chapter_id existente. Sin asociaciones pedagógicas inferidas. Ejecución del capítulo es unverified o local_only con motivo localizado; browser_compatible exige evidencia real en runtime fijado a nivel de ejercicio. Metadatos opcionales de Python local/dependencias significan no especificado si faltan, no irrestricto.

Manifiesto con association_status pending es artefacto de desarrollo; consumidores exigen complete y validación referencial integral. A valida esquema y archivos confinados con fixtures sintéticas; B publica inventario con asociaciones pendientes; C completa y valida asociaciones; D demuestra consumo por revisión fijada; E cierra AC-08. Versiones soportadas explícitas (inicialmente exactas); datos desconocidos o incompatibles fallan explícitamente. Preservar tokens enteros, rechazar claves duplicadas y números no finitos, sin redondeo JavaScript. Consumidores registran SHA completo aprobado y versiones soportadas fuera del snapshot; verifican el commit e importan solo sus archivos. Nunca insertar el propio SHA ni consultar por estudiante. Guías relacionadas opcionales y aplazadas hasta verificación. Sin implementación de sitio o runtime aquí.

[ADR 0004](../../adr/0004-curriculum-manifest.es.md).

## Sprint 08B · Inventario curricular

08B publica el primer inventario curricular completo: 14 módulos, 107 lecciones y ocho proyectos prácticos, 115 IDs estables y 345 rutas de contenido localizadas. Orden y títulos deben coincidir con las tres rutas maestras (texto simple de visualización; quitar solo delimitadores de código en línea). Nombres de módulos proceden de encabezados de sección localizados, sin prefijos de fase/estado. Preservar IDs de la matriz como baseline revisado, incluidas las tres excepciones históricas de problem-solving; matriz es evidencia de planificación, no entrada del consumidor. Usar órdenes de módulos y capítulos contiguos desde cero, previous/next global explícito, metadatos de fase distintos del orden curricular e índices localizados canónicos. Verificar rutas y cobertura de capítulos rastreados. Inventario incluye cada archivo rastreado ajeno al contenido bajo cada capítulo como recurso, o asset para extensiones de imagen admitidas; assets globales son imágenes rastreadas en assets/. Recursos son referencias, no allowlist de ejecución. Rutas opcionales de dependencias se declaran en las cuatro lecciones de bibliotecas externas mediante el archivo compartido existente; File Organizer es local_only por ejercitar comportamiento de sistema de archivos específico de plataforma. Demás capítulos son unverified, sin afirmar compatibilidad en navegador. B exige association_status pending y listas tipadas de asociaciones vacías; C completará y validará relaciones. CI verifica manifiesto versionado real y fixtures negativas de regresión; usar archivos rastreados por Git en inventario de autoría, no cachés sin rastrear ni API de runtime del consumidor. Sin duplicar fuente, nuevas dependencias ni sitio.

## Sprint 08C · Relaciones de evaluaciones

08C completa listas de asociaciones tipadas en orden de los índices canónicos. Cada cuestionario/ejercicio pertenece exactamente a su chapter_id existente; interview_ids de un capítulo son referencias inversas a preguntas cuyos caminos localizados de prerrequisitos documentados identifican ese capítulo, no propiedad. mock_ids pertenecen exclusivamente a la lección de simulacros; cada simulacro debe referenciar preguntas indexadas y un ejercicio canónico indexado, preservando orden y dificultad existentes. Todos los 253 registros únicos deben estar representados, sin asociaciones ausentes, duplicadas, desplazadas, inventadas o colgantes. Leer cuatro índices y registros con JSON estricto (rechazar claves duplicadas y números no finitos, preservar enteros exactos); verificar versiones declaradas, rutas canónicas, cobertura de índices y validadores existentes, incluidos rutas/encabezados de prerrequisitos y metadatos de ejecución. Índices de entrevistas/simulacros siguen preliminares 0.1.0; no implica nuevo esquema de registro. Sin cambiar cuerpos de bancos ni índice legado. Mantener comprobaciones estructurales y de inventario de autoría; gate completo rechaza relaciones pendientes o parciales. Generar listas de asociaciones determinísticamente desde bancos validados y comparar manifiesto versionado, no solo salida generada. Sin promover compatibilidad de navegador, sitio, runtime, nueva dependencia ni afirmar revisión del consumidor; D establece consumo inmutable.

## Sprint 08D · Fixtures inmutables del consumidor

08D proporciona una fixture de referencia del consumidor, no el sitio. Un lock JSON estricto externo fija el SHA completo de 40 caracteres y versiones exactas admitidas de manifiesto/bancos. Implementación confiable del consumidor y sus cinco esquemas confiables quedan fuera del snapshot exportado. Resolver solo objeto commit completo existente en base de objetos Git local confiable, con objetos de reemplazo deshabilitados. Exportar árbol rastreado a staging aislado, sin filtros de checkout, symlinks ni submódulos; rechazar rutas inseguras, entradas no regulares, archivos ausentes/extras y hashes de blobs Git divergentes. Verificar árbol completo preparado contra commit fijado, incluidos bytes de esquemas frente a esquemas confiables. No cargar ni ejecutar código del snapshot. Usar JSON estricto, validadores estructurales/de bancos confiables existentes y comprobaciones independientes de orden de módulos/capítulos, IDs únicos y navegación global, sin matriz de autoría ni parsing de rutas de aprendizaje. Validar candidato antes de cambiar pin activo; mantener pin aprobado anterior si falla validación y demostrar rollback seleccionándolo otra vez. Pruebas cubren revisión 08C aprobada real, rechazo de 08B pendiente, revisiones desconocidas/abreviadas, archivos mezclados/modificados/ausentes/extras, symlinks, divergencia de esquema y versiones exactas, actualización/rollback sintéticos válidos. Confianza en base de objetos Git y staging aislado son premisas; sin verificación de firma, sandbox contra concurrencia del filesystem, runtime de navegador, publicación ni sitio. CI obtiene historial una vez en build, no por visitante. AC-08 sigue abierto hasta E.

## Sprint 08E · Aceptación consolidada

08E consolida AC-08 sin cambiar contenido curricular o de bancos, esquemas, lock del consumidor, dependencias ni runtime. Verificar inventario de autoría, pin original del consumidor 08C y pin externo temporal de revisión squash aprobada de 08D; los tres deben resolver el mismo manifiesto completo y registros canónicos. Verificar recuentos fijados de módulos/capítulos, cobertura localizada, IDs únicos, orden, referencias y metadatos de ejecución. Añadir fixtures negativas de extremo a extremo: commit Git real con pin completo correspondiente y versión de manifiesto incompatible, ruta insegura, contenido localizado ausente, asociación incorrecta o registro canónico malformado debe pasar verificación de identidad de bytes pero fallar aceptación semántica. Probar decodificación estricta de enteros y rechazo de rutas; mantener regresiones anteriores. Registrar evidencia posterior a merge de 08D y mapear AC-08 a pruebas y validadores reales. E sigue en revisión hasta CI en HEAD exacto, Codex, auditoría final distinta, aprobación explícita del mantenedor, squash y CI posterior. Sprint 09 es responsable de QA final, revisión de release aprobada y handoff. Sin afirmar preparación de navegador o producción.
