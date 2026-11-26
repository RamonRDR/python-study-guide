# Contrato de evaluación y plan de entrega

[EN](assessment-contract.md) · [PT-BR](assessment-contract.pt-BR.md) · [ES](assessment-contract.es.md)

Sprints 07A–C2 fusionados y CI posterior aprobado ([PR #102](https://github.com/RamonRDR/python-study-guide/pull/102), [PR #103](https://github.com/RamonRDR/python-study-guide/pull/103), [PR #104](https://github.com/RamonRDR/python-study-guide/pull/104), [PR #105](https://github.com/RamonRDR/python-study-guide/pull/105), [CI de C2](https://github.com/RamonRDR/python-study-guide/actions/runs/45901661393)). D completa el índice versionado de 30 ejercicios; el cierre AC-07 y el runtime del navegador quedan fuera de D.

## Alcance y aceptación
- Inventario: 115 entradas, 345 rutas localizadas, 64 quizzes easy / 67 medium / 29 hard (2.850 XP a 10/20/30). La [matriz de distribución](assessment-matrix.json) es metadato de planificación de ingeniería, no manifiesto del consumidor. Las asignaciones cero preservan práctica manual o evitan evaluaciones repetidas.
- Antes de redactar cada pregunta, inspeccionar secciones de origen en los tres idiomas y registrar títulos exactos en requisitos previos; enseñar conceptos ausentes primero. La matriz establece rutas por lección, no demuestra revisión semántica completa de traducciones. No afirmar que un quiz mide seniority.
- Usar JSON Schema Draft 2020-12 y comprobaciones de relaciones en Python; versión 1.0.0. Preservar IDs, rutas, soluciones, restricciones y pruebas existentes. Rechazar campos desconocidos y versiones no compatibles. Las entrevistas conservan su contrato preliminar.
- Respuestas: ID estable de opción para multiple_choice/error_identification; booleano estricto para true_false; cadenas aceptadas explícitas para output_prediction/objective_code_completion. Comparación exacta salvo normalización LF expresamente seleccionada en output_prediction; sin eval ni calificación semántica.
- Interfaz: solo function_call en v1, argumentos/resultados compatibles con JSON, tipo y valor exactos recursivamente, valores de entrada conservados, silencio y requisito declarado de contenedor nuevo cuando proceda. Las pruebas funcionales no prueban complejidad ni calidad de refactorización. Timeout es límite declarado, no aplicado por el comparador puro. CI no ejecuta código arbitrario del alumno.
- Decodificación JSON rechaza claves duplicadas y números no finitos. Los enteros Python pueden superar el rango seguro JavaScript: preservar tokens enteros canónicos, usar análisis sin pérdidas o calificación en Python en el consumidor futuro; nunca redondear ni convertir silenciosamente. Navegador sigue unverified; las pruebas reales de runtime corresponden al sitio.
- Validar índices, IDs únicos, mapas de idioma, rutas existentes seguras, títulos didácticos, ejemplos/casos y respuestas. Código compartido. Pruebas usan fixtures, incluidos registros inválidos; registros publicados llegan en B–D. Sin servicios de pago nuevos.

## Entrega
A: contrato, matriz y validadores de fixtures; B: diez quizzes (dos por tipo) y tres ejercicios existentes (vowel-counter, binary-insertion-index, inventory-reconciliation); C1: completar 78 quizzes de fundamentos; C2: completar 160; D: otros 27 ejercicios; E: cierre AC-07. Los diez pilotos cuentan dentro de 160. Ningún PR posterior antes de fusión y CI aprobado del anterior.

## Evidencias y limitaciones
Baseline: `bf56305f42d10ab7c5b31c2b70f6c38140353db4`. Ver [cierre de Sprint 06](https://github.com/RamonRDR/python-study-guide/pull/101#issuecomment-7193467128). Los 30 ejercicios existentes tienen 192 casos y ninguna dependencia externa declarada; ejecución en navegador no verificada. El piloto antiguo de vocales carecía de practice_mode y assumptions de complejidad; se normalizaron en B. Preservar índice legado de 29 entradas hasta migración aprobada. Revisar evidencia didáctica por pregunta y soluciones por ejercicio en PR correspondientes. CI en head exacto, Codex Review, Final Pre-Merge Audit y autorización del mantenedor siguen obligatorios.

## Aceptación del piloto (07B)

- Publicar exactamente diez preguntas, dos por tipo, siete easy y tres medium (130 XP), con tres variantes de idioma y títulos exactos de requisitos previos. Contarlas en la matriz aprobada, sin duplicar código Python por idioma.
- Migrar solo vowel-counter, binary-insertion-index e inventory-reconciliation a 1.0.0, preservando los 24 casos canónicos e implementaciones existentes. Mantener intactos los otros 27 registros legados y el índice de expansión. Índice parcial versionado identifica los tres registros migrados.
- Ejecutar ambos índices nuevos en CI, rechazar registros versionados no indexados o inesperados, probar límites de asignación y verificar soluciones confiables y candidatos incorrectos representativos. Rechazar resultados esperados contradictorios para entradas con tipos y valores iguales. Cuando se exija un contenedor nuevo, rechazar alias a contenedores mutables internos de las entradas y alias directos. Detección de mutación compara estado final, no cada operación intermedia.
- Sin ejecución de código del alumno, nueva dependencia de pago ni afirmación de runtime. Los 150 quizzes y 27 migraciones restantes pertenecen a C1/C2/D; AC-07 se cierra solo en E.

## Aceptación de fundamentos (07C1)

- Completar todas las asignaciones aprobadas de módulos 00–05, incluidas las diez preguntas piloto: 78 en total (37 easy, 30 medium, 11 hard; 1.300 XP). Añadir solo 68 registros. Conservar los tres ejercicios versionados y banco legado. C2 cubre las otras 82 preguntas.
- Leer las secciones didácticas en EN/PT-BR/ES antes de redactar; mantener títulos localizados exactos, IDs estables, ejemplos originales, código único compartido y respuestas aceptadas explícitas. Refinar requisitos previos de salto de línea en las dos preguntas piloto de salida; conservar respuestas. Equilibrar verdadero/falso en el banco ampliado y variar posiciones de opciones.
- Conservar regresiones del piloto y exigir asignación exacta por lección/dificultad, cobertura del índice, paridad de idiomas y calificación determinista. Probar ejemplos literales confiables, no código arbitrario leído de registros. Revisar ambigüedad, casos límite, dificultad, navegación y privacidad antes de solicitar aprobación de fusión.
- Sin runtime, dependencia de pago, migración de ejercicios ni cierre AC-07 en C1. Todos los gates en el head exacto siguen siendo obligatorios.

## Aceptación de la expansión (07C2)

- Completar los 82 cuestionarios restantes según la matriz aprobada por lección/dificultad: 27 easy, 37 medium, 18 hard (1.550 XP). Conservar los 78 registros de fundamentos y sus regresiones. Inventario final: 160 cuestionarios, 64 easy/67 medium/29 hard, 2.850 XP. Las asignaciones cero permanecen vacías.
- Leer las secciones pertinentes en los tres idiomas antes de redactar; mantener títulos exactos, ejemplos originales, IDs estables, enunciados, explicaciones, pistas y opciones localizados. Diversificar formatos, priorizando elecciones situacionales, identificación de errores y completado restringido frente al exceso de predicción de salida; equilibrar verdadero/falso y variar posiciones. No afirmar que se mide la seniority.
- Exigir cobertura exacta de matriz e índice completos, fixtures de respuestas correctas/incorrectas por registro nuevo y ejecución literal confiable de código compartido ejecutable (sin código del alumno, red ni operaciones inseguras con archivos). Conservar regresiones del piloto y fundamentos. Mantener navegación localizada y verificar todos los enlaces. Conservar ejercicios, índices, banco de entrevistas, dependencias y runtime.
- C2 no cierra AC-07; D migra los 27 ejercicios restantes y E cierra. CI del head exacto, Codex Review, Final Pre-Merge Audit, autorización expresa y CI posterior siguen siendo obligatorios.

## Aceptación de la migración de ejercicios (07D)

- Migrar exactamente los 27 registros restantes al esquema 1.0.0 y completar el índice versionado de 30 ejercicios (12 easy, 12 medium, 6 hard; 192 casos existentes). Conservar los 3 registros piloto y los 160 cuestionarios. Mantener IDs, rutas, tokens numéricos JSON originales, contenido localizado, ejemplos, casos, starters, referencias, candidatos incorrectos, complejidad, modalidades y metadatos de tiempo.
- Añadir solo schema_version y tests.new_container a los registros legados. Establecer este último en true para los ocho registros migrados que devuelven una lista o diccionario nuevo, según sus contratos y la regla de ausencia de alias de la prueba de expansión existente; false para resultados escalares. El piloto existente tiene un flag true. Conservar el índice legado de 29 registros como vista de compatibilidad, no como índice canónico versionado.
- Validar los 30 registros canónicos mediante esquema y relaciones; usar rutas explícitas de fixtures confiables del repositorio para probar cada referencia e implementación incorrecta representativa, tipo/valor exacto, conservación de entrada, silencio y alias anidados. Conservar pruebas de modalidades de starter y oráculos independientes. Comprobar tokens de enteros grandes con semántica exacta de enteros Python. Sin ejecución de código del alumno, nuevo runtime, dependencias ni expansión de contenido.
- La ejecución en navegador sigue sin verificarse, los timeouts declarados no se aplican aquí y las pruebas funcionales no certifican complejidad ni calidad de refactorización. AC-07 se cierra solo en E tras todos los gates del head exacto y la aprobación del mantenedor.
