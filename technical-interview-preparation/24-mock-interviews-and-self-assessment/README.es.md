# Simulaciones de entrevistas y autoevaluación

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../23-behavioral-and-international-interviews/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:top -->

## Cómo usar las simulaciones

Estudia requisitos previos de preguntas y ejercicio seleccionados antes del intento; cierra respuestas y referencias durante sesión. Usa cronómetro, Python 3.13 local y copia nueva del starter fuera del repositorio. Trabaja solo o pide a compañero leer preguntas, no resolverlas. Sin IA ni pistas en intento independiente. Son tiempos de práctica, no criterios universales de contratación. Si acaba tiempo, detente y documenta lo realmente completado. Dificultad de ejercicio y seniority de entrevista son distintas; ejercicios elegidos solo ofrecen reto progresivo. Ejecución en navegador sigue sin verificar.

## Puntuación manual

Cinco dimensiones suman 100 puntos: conocimiento técnico 25, resolución de problemas 25, comunicación 20, pruebas y límites 15, criterio de ingeniería 15. Cada dimensión lista indicadores observables y tres bandas permitidas: concede puntos completos si se demuestran todos indicadores, parciales si al menos uno pero no todos se demuestra, o cero si ninguno se demuestra. No concedas puntos por ejecución solo prevista cuando indicador exige ejecución real. Registra evidencias y pistas, y no cuentes acento, velocidad de habla o métricas inventadas. Puntuaciones son feedback de práctica, no certificación ni evaluación semántica automática. Notas individuales del banco son independientes. Tras cronómetro, revisa respuestas y compara con referencia existente del ejercicio y pruebas confiables. Pruebas funcionales solas no demuestran algoritmo ni complejidad.

El [índice canónico de simulaciones](../../interviews/mocks/mock-index.json) y registros generan las secciones siguientes.

<!-- interview-mocks:start -->
## Simulación Junior

`mock.junior-30` · `junior`

**Duración (minutos):** 30

Usa pregunta 1 en presentación (STAR breve); responde 2–4 en voz alta sin abrir respuestas. En directorio personal nuevo, implementa ejercicio enlazado con starter y contrato original. Separa tiempos de código y pruebas; ejecuta aserciones propias para etiquetas normales, vacías y repetidas/sensibles a mayúsculas y comprueba conservación de entrada. En discusión, explica complejidad, alternativa y comportamiento incompleto. Detente a los 30 minutos; no abras pistas, soluciones ni respuestas hasta terminar.

| Etapa | Minutos |
| --- | ---: |
| Presentación | 3 |
| Preguntas técnicas | 7 |
| Live coding | 13 |
| Pruebas | 4 |
| Discusión | 3 |

**Secuencia de preguntas**

1. [`behavioral.star-evidence`](../22-technical-interview-question-bank/README.es.md#behavioralstar-evidence)
2. [`python.mutable-default`](../22-technical-interview-question-bank/README.es.md#pythonmutable-default)
3. [`algorithms.frequency-map`](../22-technical-interview-question-bank/README.es.md#algorithmsfrequency-map)
4. [`testing.specific-catch`](../22-technical-interview-question-bank/README.es.md#testingspecific-catch)

**Ejercicio:** [`problem-solving.label-counts`](../../exercises/problem-solving/label-counts/README.es.md)

### Rúbrica de puntuación

**Conocimiento técnico (0 / 12 / 25)**

- Predice ambas salidas de valor predeterminado mutable y da corrección con None.
- Explica por qué diccionario conserva conteos y ValueError se trata específicamente.

**Resolución de problemas (0 / 12 / 25)**

- Reformula conteo de etiqueta exacta y traza ejemplo duplicado.
- Implementa acumulación correcta y devuelve diccionario sin mutar entrada ni imprimir.

**Comunicación (0 / 10 / 20)**

- Da STAR breve veraz o explícitamente ficticio con acción y resultado personal.
- Explica enfoque en voz alta y distingue completado, fallido y no probado.

**Pruebas y casos límite (0 / 7 / 15)**

- Ejecuta aserciones de caso duplicado normal y entrada vacía con valores exactos.
- Comprueba etiquetas sensibles a mayúsculas y confirma entrada mutable intacta; informa resultados reales.

**Criterio de ingeniería (0 / 7 / 15)**

- Explica tiempo esperado O(n) bajo supuestos de etiquetas acotadas/hash y distingue espacio de salida requerida.
- Compara conjunto o recorridos repetidos con mapa de frecuencias y declara limitación/siguiente paso.

**Autoevaluación:** Tras cronómetro, marca cada indicador demostrado con evidencia (explicación oral, código o salida real de prueba). Asigna una banda por dimensión según regla anterior; suma sobre 100. Mantén visible trabajo incompleto. Registra pistas aparte. Puntos del banco son solo diagnósticos y no se suman a nota de simulación.

**Mejora:** Elige dimensión de menor puntuación; repasa requisito previo, reimplementa conteo de etiquetas con ejemplos nuevos y repite entradas vacía, repetida y sensible a mayúsculas. Repite después con ejercicio comparable distinto; compara evidencia real, no solo puntos.

## Simulación Mid-level

`mock.mid-45` · `mid`

**Duración (minutos):** 45

Empieza pregunta 1 en inglés, con requisito cambiado y estado honesto de prueba. Responde 2–4 en tiempo técnico. Implementa ejercicio de índice de inserción desde starter, manteniendo contrato de entrada ordenada; 20 minutos de código son menos que estimación individual de 22. En pruebas, ejecuta aserciones propias para vacío, duplicados, objetivos ausentes por debajo/entre/encima y entrada intacta. Comenta invariante de intervalo semiabierto, supuestos de complejidad y comportamiento no verificado. Detente a los 45 minutos; sin pistas, soluciones ni respuestas durante intento.

| Etapa | Minutos |
| --- | ---: |
| Presentación | 5 |
| Preguntas técnicas | 10 |
| Live coding | 20 |
| Pruebas | 5 |
| Discusión | 5 |

**Secuencia de preguntas**

1. [`behavioral.international-clarification`](../22-technical-interview-question-bank/README.es.md#behavioralinternational-clarification)
2. [`python.parameter-rebinding`](../22-technical-interview-question-bank/README.es.md#pythonparameter-rebinding)
3. [`sql.zero-child-count`](../22-technical-interview-question-bank/README.es.md#sqlzero-child-count)
4. [`api.idempotent-retry`](../22-technical-interview-question-bank/README.es.md#apiidempotent-retry)

**Ejercicio:** [`problem-solving.binary-insertion-index`](../../exercises/problem-solving/binary-insertion-index/README.es.md)

### Rúbrica de puntuación

**Conocimiento técnico (0 / 12 / 25)**

- Distingue reasignación de parámetro de mutación compartida.
- Explica filtro/conteo de LEFT JOIN incluido cero e identidad estable de grupo.
- Distingue riesgo de reintento POST de idempotencia de efecto PUT/DELETE y propone política acotada.

**Resolución de problemas (0 / 12 / 25)**

- Reformula primera posición de inserción incluidos duplicados y traza intervalo semiabierto.
- Implementa búsqueda binaria logarítmica con límites correctos sin mutación ni validación por recorrido.

**Comunicación (0 / 10 / 20)**

- Aclara requisito cambiado en inglés comprensible y da ejemplo discriminante.
- Narra invariante y comunica estado real de pruebas y limitaciones sin afirmar pruebas no ejecutadas.

**Pruebas y casos límite (0 / 7 / 15)**

- Ejecuta aserciones de valores exactos para vacío y duplicados.
- Ejecuta casos ausentes por debajo, entre y encima y comprueba conservación de entrada.

**Criterio de ingeniería (0 / 7 / 15)**

- Justifica O(log n) comparaciones y O(1) extra para acceso aleatorio ordenado y comparaciones acotadas.
- Explica orden como precondición del llamador e identifica coste de recorrido de validación o siguiente paso de verificación.

**Autoevaluación:** Tras cronómetro, marca cada indicador demostrado con evidencia (explicación oral, código o salida real de prueba). Asigna una banda por dimensión según regla anterior; suma sobre 100. Mantén visible trabajo incompleto. Registra pistas aparte. Puntos del banco son solo diagnósticos y no se suman a nota de simulación.

**Mejora:** Elige dimensión más débil; traza intervalo semiabierto con objetivos duplicados y ausentes, escribe caso de regresión que falle por carencia y repite con lista ordenada nueva. Ensaya aclaración en inglés sin memorizar ejemplo.

## Simulación Senior

`mock.senior-60` · `senior`

**Duración (minutos):** 60

Usa pregunta 1 como presentación ficticia de decisión colaborativa; responde 2–4 en tiempo técnico. Implementa ejercicio de dos punteros agrupados en directorio personal nuevo, conservando contrato original. Estimación individual de 40 minutos se comprime deliberadamente a 25 de código; solución parcial correcta y limitaciones precisas son evidencia útil, no razón para ocultar incompletitud. Ejecuta aserciones propias para vacío, sin pareja, grupos duplicados distintos, grupo todo igual y conservación de entrada en tiempo de pruebas. En discusión, justifica conteo agrupado, complejidad, decisiones de verificación de transacción/autorización y riesgo medible. Detente a los 60 minutos; sin pistas, soluciones ni respuestas hasta terminar.

| Etapa | Minutos |
| --- | ---: |
| Presentación | 5 |
| Preguntas técnicas | 15 |
| Live coding | 25 |
| Pruebas | 5 |
| Discusión | 10 |

**Secuencia de preguntas**

1. [`behavioral.evidence-disagreement`](../22-technical-interview-question-bank/README.es.md#behavioralevidence-disagreement)
2. [`internals.gil-workload`](../22-technical-interview-question-bank/README.es.md#internalsgil-workload)
3. [`api.object-authorization`](../22-technical-interview-question-bank/README.es.md#apiobject-authorization)
4. [`sql.atomic-transfer`](../22-technical-interview-question-bank/README.es.md#sqlatomic-transfer)

**Ejercicio:** [`problem-solving.sorted-pair-multiplicity`](../../exercises/problem-solving/sorted-pair-multiplicity/README.es.md)

### Rúbrica de puntuación

**Conocimiento técnico (0 / 12 / 25)**

- Distingue CPython 3.13 con GIL de free-threaded experimental y propone concurrencia adecuada con sincronización.
- Exige autorización por objeto con identidad verificada y política de denegación coherente sin datos protegidos.
- Explica ACID y transacción con débito condicional, rollback y evidencia de commit entre conexiones.

**Resolución de problemas (0 / 12 / 25)**

- Reformula conteo de pares de índices distintos y explica invariante de dos punteros agrupados y regla de eliminación.
- Implementa multiplicación de grupos distintos y conteo combinatorio de iguales sin doble conteo, mutación ni almacenamiento extra proporcional a n.

**Comunicación (0 / 10 / 20)**

- Explica desacuerdo ficticio mediante objetivos comunes, alternativas y evidencias sin resultados inventados.
- Comunica invariantes, riesgos, resultados verificados y solución parcial con honestidad.

**Pruebas y casos límite (0 / 7 / 15)**

- Ejecuta pruebas de conteo exacto para grupos duplicados distintos y todos iguales.
- Ejecuta pruebas vacío/sin pareja y verifica entrada intacta; propone comparación con oráculo independiente para validar más.

**Criterio de ingeniería (0 / 7 / 15)**

- Justifica tiempo lineal y espacio extra constante bajo aritmética acotada, sin afirmar pruebas demuestran complejidad.
- Propone validación medible y rollback o mitigación para riesgo de ingeniería, con límites de verificación.

**Autoevaluación:** Tras cronómetro, marca cada indicador demostrado con evidencia (explicación oral, código o salida real de prueba). Asigna una banda por dimensión según regla anterior; suma sobre 100. Mantén visible trabajo incompleto. Registra pistas aparte. Puntos del banco son solo diagnósticos y no se suman a nota de simulación.

**Mejora:** Elige dimensión más débil; compara solución de dos punteros agrupados con oráculo de fuerza bruta pequeño en duplicados y entradas todas iguales. Repasa GIL, autorización o decisiones según evidencias. Repite con otro problema difícil y documenta riesgo que validarías.

<!-- interview-mocks:end -->

<!-- chapter-navigation:bottom -->
[← Anterior](../23-behavioral-and-international-interviews/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:bottom -->
