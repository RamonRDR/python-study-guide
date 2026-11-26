# Contrato de evaluación y plan de entrega

[EN](assessment-contract.md) · [PT-BR](assessment-contract.pt-BR.md) · [ES](assessment-contract.es.md)

Sprint 07A: solo fundamentos. El mantenedor aprobó la distribución de 160 preguntas y el piloto. Este PR no publica preguntas, migra ejercicios, implementa ejecución en navegador ni finaliza el manifiesto curricular.

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
