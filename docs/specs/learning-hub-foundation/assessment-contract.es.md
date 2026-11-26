# Contrato de evaluación y plan de entrega

[EN](assessment-contract.md) · [PT-BR](assessment-contract.pt-BR.md) · [ES](assessment-contract.es.md)

Sprint 07A fusionado y CI posterior aprobado ([PR #102](https://github.com/RamonRDR/python-study-guide/pull/102), [CI](https://github.com/RamonRDR/python-study-guide/actions/runs/45871235887)). Sprint 07B es el piloto aprobado: diez quizzes y tres ejercicios existentes, sin ampliar más el banco ni ejecutar en navegador.

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
Baseline: `bf56305f42d10ab7c5b31c2b70f6c38140353db4`. Ver [cierre de Sprint 06](https://github.com/RamonRDR/python-study-guide/pull/101#issuecomment-7193467128). Los 30 ejercicios existentes tienen 192 casos y ninguna dependencia externa declarada; ejecución en navegador no verificada. El piloto antiguo de vocales carece de practice_mode y assumptions de complejidad; normalizarlos explícitamente durante la migración. Preservar índice legado de 29 entradas hasta migración aprobada. Revisar evidencia didáctica por pregunta y soluciones por ejercicio en PR correspondientes. CI en head exacto, Codex Review, Final Pre-Merge Audit y autorización del mantenedor siguen obligatorios.

## Aceptación del piloto (07B)

- Publicar exactamente diez preguntas, dos por tipo, siete easy y tres medium (130 XP), con tres variantes de idioma y títulos exactos de requisitos previos. Contarlas en la matriz aprobada, sin duplicar código Python por idioma.
- Migrar solo vowel-counter, binary-insertion-index e inventory-reconciliation a 1.0.0, preservando los 24 casos canónicos e implementaciones existentes. Mantener intactos los otros 27 registros legados y el índice de expansión. Índice parcial versionado identifica los tres registros migrados.
- Ejecutar ambos índices nuevos en CI, rechazar registros versionados no indexados o inesperados, probar límites de asignación y verificar soluciones confiables y candidatos incorrectos representativos. Rechazar resultados esperados contradictorios para entradas con tipos y valores iguales. Cuando se exija un contenedor nuevo, rechazar alias a contenedores mutables internos de las entradas y alias directos. Detección de mutación compara estado final, no cada operación intermedia.
- Sin ejecución de código del alumno, nueva dependencia de pago ni afirmación de runtime. Los 150 quizzes y 27 migraciones restantes pertenecen a C1/C2/D; AC-07 se cierra solo en E.
