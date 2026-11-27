# Transferencia al Learning Hub

[🇺🇸 English](handoff.md) · [🇧🇷 Português](handoff.pt-BR.md) · [🇪🇸 Español](handoff.es.md)

Estado: 09B en revisión; referencia de implementación, no aprobación final de AC-09 ni despliegue de producción. Revisión de contenido 09A integrada y aprobada en CI; validación exacta del candidato, revisión 09B y aprobación del mantenedor preceden al cierre.

## 1. Fuente y revisión inmutable

Repositorio: [RamonRDR/python-study-guide](https://github.com/RamonRDR/python-study-guide), público con licencia MIT. Conservar autoría y licencia. Candidato de contenido (SHA Git completo e inmutable): `03e91ff9952f2b02293f16a11260d166eb00ea8a`, árbol `f1cbf0689a8bf1f26539ed1b330b5c51ce7ce4e6`. Es el squash de 09A, no el commit documental de 09B, nombre de rama ni etiqueta. No se creó tag/release. El handoff se revisa en un commit posterior; no insertar su propio SHA en sí mismo. Seleccionar pin de consumo aprobado solo tras validación y aprobación del mantenedor.

[PR #113](https://github.com/RamonRDR/python-study-guide/pull/113) · [CI #46059023528](https://github.com/RamonRDR/python-study-guide/actions/runs/46059023528) · [Codex](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226444778) · [Final Pre-Merge Audit](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226469107) · [09A closure](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226902203)

## 2. Arquitectura y responsabilidades

La guía es fuente única de verdad; sitio externo consume un commit validado al compilar, sin scraping HTML ni llamadas a API GitHub por estudiante. Conservar estudio independiente en GitHub/local. Markdown y Python compartido son canónicos; JSON estructurado dirige la UI. Fuera de alcance: servicio de pago, Python en servidor, calificación por IA o entrevistador IA. Progreso local del navegador específico del dispositivo, sin sincronización de cuenta. ADR aceptados: 0001 fuente de verdad, 0002 contrato de contenido, 0003 dirección de runtime futuro (implementación sin verificar), 0004 manifiesto. Consultar índice ADR y contrato.

[ADR](../../adr/README.es.md) · [Integration contract](integration-contract.es.md) · [Assessment contract](assessment-contract.es.md)

## 3. Contrato canónico e inventario

| Entrada canónica | Versión | Esquema / validador | Cantidad |
| --- | --- | --- | --- |
| `curriculum/manifest.json` | 1.0.0 | `schemas/curriculum-manifest.schema.json` | 14 / 115 |
| `quizzes/quiz-index.json` | 1.0.0 | `schemas/quiz-index.schema.json`, `schemas/quiz.schema.json` | 160 |
| `exercises/problem-solving/exercise-index.json` | 1.0.0 | `schemas/exercise-index.schema.json`, `schemas/exercise.schema.json` | 30 |
| `interviews/interview-index.json` | 0.1.0 | `scripts/interview_records.py` | 60 |
| `interviews/mocks/mock-index.json` | 0.1.0 | `scripts/interview_mocks.py` | 3 |

Cinco esquemas JSON usan Draft 2020-12; registros de entrevista/simulacro siguen preliminares y usan validadores Python confiables, sin inventar esquemas JSON. association_status debe ser complete. Inventario: 107 lecciones + ocho proyectos = 115 entradas, 345 rutas localizadas, 42 índices de módulo, 243 recursos de capítulo, seis assets globales. 253 registros canónicos; 268 asociaciones (160 cuestionarios, 30 ejercicios, 75 enlaces de requisitos previos de entrevistas, tres de simulacros). Dificultad easy/medium/hard: cuestionarios 64/67/29, 2.850 XP; ejercicios 12/12/6, 192 casos; entrevistas junior/mid/senior 24/24/12; simulacros 30/45/60 minutos. Pruebas existentes respaldan recuentos; consultar QA.

## 4. Navegación, idiomas y recursos

Usar arrays de módulos/capítulos y orden explícito zero-based, previous_id/next_id globales (null en extremos), IDs estables y mapas de índice/contenido/título por idioma. Predeterminado en; admitidos en, pt-BR, es. No usar títulos, rutas u orden de directorios como identidad. Fase no es número de sprint de ingeniería. chapter_id de cuestionario/ejercicio indica propiedad; interview_ids son referencias inversas de requisitos previos; mock_ids pertenecen a lección de simulacros. Seguir índices y referencias tipadas; no interpretar matriz de autoría ni rutas maestras. Resolver enlaces/assets en misma revisión validada, sanitizar Markdown/HTML, conservar cambio de idioma y fallback/errores accesibles. Recursos no son lista de ejecución; solo scripts/example_manifest.txt enumera ejemplos autorizados del repositorio. Dependencia opcional ausente significa no especificada; cuatro lecciones externas declaran requirements-external.txt.

## 5. Ejemplos de registros reales

- Capítulo `getting-started.install-python`: order 0, previous_id null, next_id `getting-started.configure-vscode`, cuestionario `quiz.interpreter-purpose`, execution unverified.
- Cuestionario `quiz.absolute-distance-zero`: `quizzes/questions/quiz.absolute-distance-zero.json`, cadena exacta aceptada `abs`, `magnitude = ____(-11)`, 10 XP. Resultado 11.
- Ejercicio `problem-solving.ascii-digit-counter`: `exercises/problem-solving/ascii-digit-counter/exercise.json`; starter.py y solution.py referenciados; entrada `a12-3` devuelve entero 3; ignora dígitos Unicode fuera de ASCII.
- Entrevista `interview.allowed-tools`: `interviews/questions/interview.allowed-tools.json`; respuesta esperada, explicación, follow-ups y rúbrica; respetar restricciones de IA/herramientas.
- Simulacro `mock.junior-30`: `interviews/mocks/mock.junior-30.json`; 30 minutos, cuatro preguntas indexadas, `problem-solving.label-counts`, rúbrica de autoevaluación de 100 puntos.

## 6. Calificación determinista

Usar scripts/assessment_grading.py confiable como referencia de comportamiento, no código del snapshot. Cuestionario multiple_choice/error_identification acepta cadena de ID de opción conocida; true_false acepta booleano real; output_prediction/objective_code_completion acepta cadena de valores explícitos. Comparación exact o normalize_lf (solo CRLF/CR a LF), sin trim/case folding implícitos, sin eval. Tipos inválidos/IDs desconocidos generan error de validación; distinguir inválido de incorrecto. XP orientativo. Ejercicios llaman función declarada con copias profundas independientes de args JSON y comparan retorno recursivamente por tipo/valor exacto (bool, int, float distintos, claves cadena); conservar entradas finales, rechazar stdout/stderr y excepciones, impedir alias de contenedores de entrada anidados si new_container true. No evalúa automáticamente complejidad/refactorización o mutación transitoria; timeout declarado no se impone por calificador de fixtures confiables. Usar parser JSON estricto sin pérdida, conservar distinción entre entero y float (ej. 9007199254740993 y 2432902008176640000), rechazar claves duplicadas/no finitos y no redondear mediante JavaScript Number. Entrevistas/simulacros abiertos usan respuestas de referencia y rúbricas de autoevaluación; sin calificación semántica automática. Pruebas/soluciones públicas son inspeccionables; revelar bajo demanda no es secreto.

## 7. Ejecución y compatibilidad del navegador

30 ejercicios sin verificar para navegador, sin dependencias externas permitidas; local_python 3.13. 114 capítulos unverified, File Organizer local_only con motivo localizado. No promover estado ni ejecutar automáticamente contenido unverified/local_only. ADR 0003 elige Pyodide fijado + Web Worker como dirección futura del sitio, no implementación verificada. Antes de habilitar ejercicio individual, probar versión, compatibilidad, calificación determinista, límites de tiempo/salida, cancelación y recreación del worker; evaluar memoria, filesystem, almacenamiento, red y exposición de credenciales con aislamiento de origen cuando proceda. Worker no es frontera de seguridad. Conservar instrucciones locales. Comportamiento de navegador/SO/plataforma/red no probado por fixtures Linux o pruebas File Organizer Windows.

## 8. Importación, validación de candidato y rollback

Usar base de objetos Git confiable (historial completo, sin objetos de reemplazo), checkout de tooling confiable independiente y cinco esquemas fuera del snapshot. Instalar requirements-assessment.txt confiable (jsonschema 4.26.0 en esta revisión). Obtener commit aprobado una vez al compilar y verificar SHA completo. Copiar JSON estricto siguiente a lock fuera del snapshot. Archivo idéntico tests/fixtures/learning-hub/handoff-lock.json pertenece a tooling 09B, no al snapshot 09A ni configuración activa del sitio; consumidor debe aprobar/guardar su lock de forma independiente. tests/fixtures/learning-hub/consumer-lock.json histórico fija 08C y permanece intacto.

```json
{
  "lock_version": "1.0.0",
  "revision": "03e91ff9952f2b02293f16a11260d166eb00ea8a",
  "versions": {
    "manifest": "1.0.0",
    "quizzes": "1.0.0",
    "exercises": "1.0.0",
    "interviews": "0.1.0",
    "mocks": "0.1.0"
  }
}
```

```bash
# From the independently trusted tooling checkout (Python 3.13).
python -m pip install -r requirements-assessment.txt
python scripts/curriculum_consumer.py --repository /path/to/trusted-source-git --lock /path/to/external/handoff-lock.json
```

Comando es validador de referencia (Git archive y staging temporal aislado; sin despliegue persistente). Rutas son placeholders a sustituir, no directorios reales. No ejecutar scripts de contenido exportado. Validador comprueba cada archivo/directorio regular rastreado, confinamiento, cobertura exacta de árbol/blob Git, bytes de esquemas confiables, versiones, JSON estricto, IDs/navegación únicos y relaciones completas. Rechazar archivos ausentes/extra/modificados, symlinks/submodules, SHA desconocido/abreviado, versiones no admitidas y asociaciones incompletas. Nuevo test_ac09_handoff_content_pin en tests/test_curriculum_acceptance.py copia lock fuera del snapshot, valida 09A exacta, compara manifiesto/rutas/bytes canónicos con fixture histórica aprobada y registra evidencia en CI. Ejecución en PR pendiente al redactar. Identidad Git no es firma; base Git confiable y staging aislado son supuestos, no protección concurrente de filesystem. Solo seleccionar candidato activo tras validar; ante fallo mantener pin y contenido anteriores, registrar motivo y fallar build sin publicación parcial. Rollback: seleccionar SHA completo + versiones anteriores válidas, repetir validación/build y publicar con despliegue atómico controlado por consumidor. Rollback sintético local probado antes; despliegue/rollback atómico real no probado.

## 9. Evidencias, aceptación y límites

CI push exacto 09A pasó ambos jobs: 180 unittest de calidad, siete unittest de ingeniería, 406 pruebas prácticas aprobadas/una omitida, Windows 63/17 omitidas, 210 ejemplos, 9.282 enlaces internos en 583 Markdown, 345 documentos de navegación. Windows se solapa con Linux; no sumar. Codex 09A sin hallazgos, auditoría final registrada. 09B exige nuevo CI en HEAD exacto con prueba de pin, Codex sin hallazgos pendientes, auditoría final distinta, autorización explícita de squash y CI de push exacto. Sin AC-09 concluido antes de gates. QA mapea AC-00–09, PR previos y límites de revisión: muestra de 42 documentos localizados, 314 bloques Python por idioma y cuatro registros, no auditoría semántica/humana exhaustiva. Ejecución local no disponible por acceso GitHub del contenedor; sin certificación integral de enlaces externos, secretos en contenido/historial, instalaciones en plataformas o navegador/seguridad. Sin infraestructura de pago, runtime o sitio externo implementado. Publicación/enlaces entre guías requieren aprobación separada.

[Final QA](final-qa.es.md) · [AC](acceptance-criteria.es.md) · [Tasks](tasks.es.md)

## 10. Lista de implementación del consumidor

- [ ] Verificar SHA exacto aprobado, versiones del lock, confianza independiente en validador/esquemas; fallar de forma cerrada antes de renderizar.
- [ ] Importar solo datos canónicos indicados por manifiesto/índices desde snapshot validado; conservar idiomas, IDs, enlaces, assets y accesibilidad.
- [ ] Implementar UI de calificación determinista sin pérdida numérica o coerción implícita; entrevistas/simulacros autoevaluados.
- [ ] Mantener ejecución unverified/local_only desactivada hasta comprobaciones por ejercicio de runtime/aislamiento; conservar práctica manual/local.
- [ ] Guardar progreso local por ID estable y versión/revisión; tratar migración/reset explícitamente; sin sincronización de cuenta supuesta.
- [ ] Validar actualizaciones antes de cambiar contenido activo, conservar lock anterior y demostrar rollback en entorno de despliegue; nunca obtener por visitante.
- [ ] Revisar renderizador seguro, licencia/autoría, pin de dependencias/runtime, pruebas, navegadores y límites operativos en proyecto separado del sitio.
- [ ] Obtener revisión final del PR/aprobación del mantenedor y CI posterior; registrar revisión documental del handoff separada del pin de contenido.
