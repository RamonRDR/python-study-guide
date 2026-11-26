# Banco de preguntas de entrevistas técnicas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../21-software-engineering-and-technical-decisions/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../23-behavioral-and-international-interviews/README.es.md)
<!-- /chapter-navigation:top -->

60 preguntas de entrevista: 24 Junior, 24 Mid-level y 12 Senior, incluidas nueve preguntas piloto originales y tres conductuales/internacionales. Navega por tema y nivel; IDs permanecen estables al reordenar. Nivel indica profundidad esperada, no estándar universal de contratación. Estudia primero la sección de requisito previo, responde en voz alta sin revelar referencia y luego abre respuesta. Asigna a cada criterio sus puntos solo si tu respuesta lo demuestra; si no, cero. Usa puntuación para identificar carencias, no como certificación ni evaluación semántica automática. Preguntas de seguimiento son práctica opcional, sin puntuación separada. Registros JSON canónicos e índice en [interviews](../../interviews/README.es.md); esta sección se genera a partir de ellos. Estudia [entrevistas conductuales e internacionales](../23-behavioral-and-international-interviews/README.es.md) antes de esas preguntas y luego intenta las [simulaciones cronometradas](../24-mock-interviews-and-self-assessment/README.es.md).

<!-- interview-questions:start -->
## Distribución

| Tema | Junior | Mid-level | Senior | Total |
| --- | ---: | ---: | ---: | ---: |
| Fundamentos de entrevistas | 3 | 2 | 1 | 6 |
| Fundamentos de Python | 4 | 3 | 1 | 8 |
| Estructuras de datos y algoritmos | 3 | 3 | 1 | 7 |
| Programación orientada a objetos | 3 | 3 | 2 | 8 |
| Internals de Python | 2 | 4 | 2 | 8 |
| Pruebas y depuración | 3 | 3 | 1 | 7 |
| Backend y APIs | 2 | 2 | 1 | 5 |
| Bases de datos y SQL | 2 | 2 | 1 | 5 |
| Ingeniería de software | 1 | 1 | 1 | 3 |
| Entrevistas conductuales e internacionales | 1 | 1 | 1 | 3 |

## Fundamentos de entrevistas

### interview.allowed-tools

`junior` · `interview-fundamentals`

Antes de un take-home, ¿qué confirmar sobre alcance, entrega y herramientas de IA? ¿Y si se prohíbe la IA?

<details>
<summary>Respuesta esperada</summary>

Confirma plazo, alcance, formato, criterios y herramientas permitidas. Si se prohíbe la IA, no la uses; si se permite, declara su uso según las reglas.

**Explicación:** Las reglas varían entre empresas; pregunta en vez de inferir.

**Intención del entrevistador:** Evaluar respeto por las reglas de evaluación.

**Errores comunes**

- Suponer que sigue vigente la política de la empresa anterior.

**Preguntas de seguimiento**

- ¿Qué preguntarías si la documentación permitida no está clara?

**Ejemplo**

Si las instrucciones permiten documentación de la biblioteca estándar pero prohíben IA, consulta solo la documentación.

**Rúbrica de autoevaluación**

- 1 — Identifica plazo, alcance, formato, criterios y política de herramientas.
- 1 — Respeta prohibición u obligación de declarar uso.

Máximo: 2

</details>

**Requisitos previos**

- [Propósito y proceso](../../technical-interview-preparation/01-understanding-technical-interviews/README.es.md)
- [Tareas take-home](../../technical-interview-preparation/02-live-coding-and-take-home/README.es.md)

### interview.clarify-contract

`junior` · `interview-fundamentals`

Un entrevistador pide contar registros elegibles. Elegibilidad, duplicados y entrada vacía no están definidos. ¿Qué haces antes de programar?

<details>
<summary>Respuesta esperada</summary>

Pregunta qué califica, si cuentan duplicados y el resultado para entrada vacía. Reformula el contrato acordado, da ejemplo concreto y explica cómo lo probarás antes de implementar.

**Explicación:** Aclarar evita resolver otro problema. Si sigue desconocida una regla, declara supuesto y pide confirmación.

**Intención del entrevistador:** Evaluar comunicación, razonamiento sobre contrato y planificación de pruebas, no solo velocidad.

**Errores comunes**

- Empezar a programar sin definir elegibilidad.
- Inventar política de duplicados y presentarla como dada.

**Preguntas de seguimiento**

- ¿Cómo afectaría a tus pruebas cambiar de conteo de filas a IDs distintos?

**Ejemplo**

Si la regla acordada cuenta IDs elegibles distintos, dos filas elegibles con ID 7 cuentan como una y entrada vacía devuelve cero si se acordó.

**Rúbrica de autoevaluación**

- 1 — Pregunta explícitamente sobre elegibilidad, duplicados y entrada vacía.
- 1 — Reformula contrato y distingue supuestos de hechos.
- 1 — Proporciona ejemplo concreto y al menos una prueba relevante.

Máximo: 3

</details>

**Requisitos previos**

- [Una conversación práctica](../../technical-interview-preparation/01-understanding-technical-interviews/README.es.md)

### interview.live-coding-start

`junior` · `interview-fundamentals`

¿Cómo empiezas una tarea cronometrada antes de escribir solución? Describe una traza pequeña y cómo te comunicas.

<details>
<summary>Respuesta esperada</summary>

Lee y reformula el contrato, traza un ejemplo pequeño, elige enfoque directo, implementa y prueba explicando decisiones.

**Explicación:** Una traza revela supuestos antes de implementar; explica decisiones, no teclas.

**Intención del entrevistador:** Evaluar proceso bajo presión de tiempo.

**Errores comunes**

- Escribir solución optimizada antes de comprobar contrato.

**Preguntas de seguimiento**

- ¿Y si la traza contradice el contrato declarado?

**Ejemplo**

Para suma de cantidades no negativas, traza [2, 0, 3] hasta 5 tras confirmar que cero está permitido.

**Rúbrica de autoevaluación**

- 1 — Reformula contrato y traza ejemplo concreto.
- 1 — Elige enfoque sencillo y explica decisiones de implementación/prueba en voz alta.

Máximo: 2

</details>

**Requisitos previos**

- [Live coding](../../technical-interview-preparation/02-live-coding-and-take-home/README.es.md)

### interview.incomplete-live-task

`mid` · `interview-fundamentals`

Se acaba el tiempo; solución cubre entradas típicas pero falla un caso límite. ¿Cómo informas estado y priorizas trabajo restante?

<details>
<summary>Respuesta esperada</summary>

Indica qué comportamiento se verificó y cuál falla; aísla caso mínimo, intenta corrección pequeña verificable si hay tiempo y explica próxima prueba y limitación.

**Explicación:** Resultado parcial preciso aporta más evidencia que afirmar finalización sin respaldo.

**Intención del entrevistador:** Evaluar priorización y evidencia honesta.

**Errores comunes**

- Decir que todas las pruebas pasan porque funciona flujo principal.

**Preguntas de seguimiento**

- ¿Cómo comunicarías una corrección fallida?

**Ejemplo**

Función pasa [2,3] pero falla en []; informa el fallo y prueba el resultado acordado para vacío.

**Rúbrica de autoevaluación**

- 1 — Distingue comportamiento verificado, fallo y trabajo no verificado.
- 1 — Propone caso mínimo reproducible y próximo paso de verificación.

Máximo: 2

</details>

**Requisitos previos**

- [Live coding](../../technical-interview-preparation/02-live-coding-and-take-home/README.es.md)

### interview.take-home-evidence

`mid` · `interview-fundamentals`

Para take-home pequeño, ¿qué deben demostrar README de entrega y pruebas? Explica cómo evitar afirmaciones sin respaldo.

<details>
<summary>Respuesta esperada</summary>

Documenta requisitos, supuestos, comandos de instalación/ejecución, pruebas realmente ejecutadas y limitaciones. Incluye entradas normal, vacía e inválida según contrato y explica complejidad.

**Explicación:** Revisor debe poder reproducir evidencias sin secretos ni código propietario.

**Intención del entrevistador:** Evaluar reproducibilidad y disciplina de entrega.

**Errores comunes**

- Añadir funciones especulativas y dejar instalación sin documentar.

**Preguntas de seguimiento**

- ¿Qué registrarías si una prueba de integración no puede ejecutarse localmente?

**Ejemplo**

Para suma de enteros no negativos, registra política del cero, prueba de entrada inválida y comando real de prueba.

**Rúbrica de autoevaluación**

- 1 — Incluye instrucciones reproducibles, supuestos explícitos y evidencia real de pruebas.
- 1 — Describe casos límite, complejidad y limitaciones sin afirmaciones falsas.

Máximo: 2

</details>

**Requisitos previos**

- [Tareas take-home](../../technical-interview-preparation/02-live-coding-and-take-home/README.es.md)

### interview.scope-prioritization

`senior` · `interview-fundamentals`

Take-home pide servicio pequeño funcional en dos horas; opcionales son ambiguos. ¿Cómo acuerdas prioridades, eliges entrega y comunicas riesgo?

<details>
<summary>Respuesta esperada</summary>

Confirma criterios de aceptación, plazo y herramientas; separa obligatorio de opcional. Entrega implementación pequeña probada con supuestos, evidencias y riesgos aplazados explícitos en vez de ampliar alcance.

**Explicación:** Entrega restringida intercambia amplitud por comportamiento verificado; entrevistador debe saber qué no se implementó.

**Intención del entrevistador:** Evaluar criterio sobre alcance y evidencias.

**Errores comunes**

- Prometer arquitectura completa sin validar comportamiento central.

**Preguntas de seguimiento**

- ¿Cómo responderías a un requisito nuevo a mitad del tiempo?

**Ejemplo**

Prioriza cálculo validado e instrucciones de ejecución sobre UI no solicitada; aplaza UI explícitamente.

**Rúbrica de autoevaluación**

- 1 — Prioriza criterios de aceptación explícitos y acuerda supuestos con evaluador.
- 1 — Justifica compromiso de alcance y comunica resultados probados y riesgos aplazados.

Máximo: 2

</details>

**Requisitos previos**

- [Propósito y proceso](../../technical-interview-preparation/01-understanding-technical-interviews/README.es.md)
- [Tareas take-home](../../technical-interview-preparation/02-live-coding-and-take-home/README.es.md)

## Fundamentos de Python

### python.binding-vs-copy

`junior` · `python-fundamentals`

Dado a = [1]; b = a; b.append(2), ¿cuáles son a y b? Explica si asignación copia lista.

<details>
<summary>Respuesta esperada</summary>

Ambos son [1, 2]; a y b nombran la misma lista mutable. Asignación enlaza nombre y no copia objeto.

**Explicación:** Mutar mediante una referencia es visible mediante la otra.

**Intención del entrevistador:** Evaluar alias y mutación de listas.

**Errores comunes**

- Tratar b = a como lista independiente.

**Preguntas de seguimiento**

- ¿Qué cambia si luego b se enlaza a []?

**Ejemplo**

Tras `a = [1]; b = a`, la expresión `a is b` da `True` antes de reasignar `b`.

**Rúbrica de autoevaluación**

- 1 — Predice valores de ambas listas.
- 1 — Explica identidad compartida y mutación, no copia.

Máximo: 2

</details>

**Requisitos previos**

- [Repaso mediante razonamiento](../../technical-interview-preparation/03-python-fundamentals-review/README.es.md)
- [Identidad, igualdad y enlace](../../technical-interview-preparation/09-object-identity-references-and-copying/README.es.md)

### python.conversion-contract

`junior` · `python-fundamentals`

¿Qué ocurre con int("12") e int("twelve")? Explica por qué importan tipo y contenido.

<details>
<summary>Respuesta esperada</summary>

El primero devuelve entero 12; el segundo lanza ValueError porque texto no representa entero aceptado por int.

**Explicación:** Conversión tiene contrato de entrada, no garantía de éxito para toda cadena.

**Intención del entrevistador:** Evaluar conversión de tipos y razonamiento sobre fallo.

**Errores comunes**

- Suponer que conversión inválida devuelve cero o None.

**Preguntas de seguimiento**

- ¿Qué probarías para cadena vacía?

**Ejemplo**

int("0") devuelve 0; int("") lanza ValueError.

**Rúbrica de autoevaluación**

- 1 — Predice valor y tipo de conversión exitosa.
- 1 — Identifica ValueError y explica restricción de entrada.

Máximo: 2

</details>

**Requisitos previos**

- [Repaso mediante razonamiento](../../technical-interview-preparation/03-python-fundamentals-review/README.es.md)

### python.immutable-string

`junior` · `python-fundamentals`

Dado s = "python"; s.upper(); print(s), ¿qué se imprime? ¿Cómo conservas el valor en mayúsculas?

<details>
<summary>Respuesta esperada</summary>

Imprime python. Las cadenas son inmutables; upper devuelve una cadena resultante. Usa s = s.upper() para enlazar s al resultado en mayúsculas.

**Explicación:** Llamar un método no implica mutación; comprueba contrato.

**Intención del entrevistador:** Evaluar valores de retorno e inmutabilidad.

**Errores comunes**

- Esperar que upper modifique cadena original en el lugar.

**Preguntas de seguimiento**

- ¿Qué sigue enlazado a un alias de la cadena original?

**Ejemplo**

s = "hi"; t = s.upper() deja s igual a "hi" y t igual a "HI".

**Rúbrica de autoevaluación**

- 1 — Predice salida original y explica inmutabilidad.
- 1 — Muestra asignación del resultado devuelto.

Máximo: 2

</details>

**Requisitos previos**

- [Repaso mediante razonamiento](../../technical-interview-preparation/03-python-fundamentals-review/README.es.md)

### python.mutable-default

`junior` · `python-fundamentals`

Dado `def add(x, items=[]): items.append(x); return items`, ¿qué muestran `print(add(1)); print(add(2))` en llamadas consecutivas? Corrige el comportamiento cuando se omite la lista. Conserva la mutación de listas suministradas explícitamente, incluida una lista vacía.

<details>
<summary>Respuesta esperada</summary>

Las impresiones son `[1]` y `[1, 2]`. La lista predeterminada se crea al definir la función y se reutiliza. Usa None por defecto y crea lista nueva solo cuando items sea None.

**Explicación:** Asignación enlaza objetos; el valor predeterminado compartido se muta. Listas suministradas explícitamente siguen mutándose bajo este contrato.

**Intención del entrevistador:** Evaluar momento de evaluación, mutabilidad y propiedad pretendida.

**Errores comunes**

- Suponer lista nueva en cada llamada.
- Usar `if not items` y sustituir lista vacía suministrada.

**Preguntas de seguimiento**

- ¿Qué cambia si el llamador suministra una lista vacía?

**Ejemplo**

```python
def add(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
```

**Rúbrica de autoevaluación**

- 1 — Predice correctamente ambas listas impresas.
- 1 — Explica evaluación única y mutación compartida.
- 1 — Usa None y comprobación de identidad sin sustituir lista vacía suministrada.

Máximo: 3

</details>

**Requisitos previos**

- [Repaso mediante razonamiento](../../technical-interview-preparation/03-python-fundamentals-review/README.es.md)

### python.identity-none

`mid` · `python-fundamentals`

Compara x == y y x is y para dos listas [1] creadas independientemente. ¿Por qué is None es apropiado pero is no es fiable para comparar valor de cadenas?

<details>
<summary>Respuesta esperada</summary>

Igualdad es True e identidad False. == compara semántica de igualdad; is compara identidad. None es singleton, así que identidad es prueba prevista; caché de cadenas no es contrato de igualdad por valor.

**Explicación:** Dos objetos distintos pueden ser iguales. Identidad de valores en caché depende de implementación.

**Intención del entrevistador:** Evaluar identidad frente a igualdad.

**Errores comunes**

- Usar is para comparar valores enteros o cadenas.

**Preguntas de seguimiento**

- ¿Qué ocurre cuando y recibe x?

**Ejemplo**

Dado `x = [1]; y = [1]`, la expresión `x == y` da `True`, mientras que `x is y` da `False`.

**Rúbrica de autoevaluación**

- 1 — Predice identidad e igualdad para listas separadas.
- 1 — Explica singleton None y regla de comparación de valor.

Máximo: 2

</details>

**Requisitos previos**

- [Práctica independiente](../../technical-interview-preparation/03-python-fundamentals-review/README.es.md)
- [Identidad, igualdad y enlace](../../technical-interview-preparation/09-object-identity-references-and-copying/README.es.md)

### python.parameter-rebinding

`mid` · `python-fundamentals`

Función recibe items=[1] del llamador, luego asigna items = [9] localmente. Compara con items.append(9). ¿Qué ve el llamador?

<details>
<summary>Respuesta esperada</summary>

Reasignar parámetro local no cambia lista ni enlace del llamador; sigue viendo [1]. Hacer append en lista compartida cambia a [1, 9].

**Explicación:** Parámetros son nombres locales enlazados a objetos suministrados; distingue enlace de cambio del objeto.

**Intención del entrevistador:** Evaluar frontera de función y propiedad.

**Errores comunes**

- Describir argumentos Python simplemente como valores copiados o referencias a variable del llamador.

**Preguntas de seguimiento**

- ¿Cómo devolverías lista nueva conservando original?

**Ejemplo**

def f(items): items = [9] deja lista original sin cambio.

**Rúbrica de autoevaluación**

- 1 — Predice resultado de reasignación local.
- 1 — Predice mutación compartida y explica diferencia.

Máximo: 2

</details>

**Requisitos previos**

- [Repaso mediante razonamiento](../../technical-interview-preparation/03-python-fundamentals-review/README.es.md)
- [Identidad, igualdad y enlace](../../technical-interview-preparation/09-object-identity-references-and-copying/README.es.md)

### python.scope-lookup

`mid` · `python-fundamentals`

Explica búsqueda LEGB y qué cambia nonlocal cuando función interna actualiza contador envolvente. Compara con reasignar variable local independiente.

<details>
<summary>Respuesta esperada</summary>

LEGB busca local, funciones envolventes, global del módulo y builtins para nombre no cualificado ordinario. nonlocal permite reasignar enlace existente en función envolvente; asignación local normal no actualiza ese enlace.

**Explicación:** Un cierre puede conservar estado envolvente entre llamadas. nonlocal no es declaración global.

**Intención del entrevistador:** Evaluar ámbito y semántica de enlace.

**Errores comunes**

- Usar global cuando contador pertenece a función envolvente.

**Preguntas de seguimiento**

- ¿Por qué dos llamadas de fábrica pueden tener contadores separados?

**Ejemplo**

Incremento interno con nonlocal count actualiza count conservado por su propia llamada externa.

**Rúbrica de autoevaluación**

- 1 — Nombra los cuatro ámbitos LEGB en orden.
- 1 — Explica enlace envolvente existente y contrasta reasignación local.

Máximo: 2

</details>

**Requisitos previos**

- [Repaso mediante razonamiento](../../technical-interview-preparation/03-python-fundamentals-review/README.es.md)
- [Cierres y ámbito](../../technical-interview-preparation/12-closures-and-decorators/README.es.md)

### python.hash-equality-contract

`senior` · `python-fundamentals`

Diseñas clase de igualdad por valor para claves de diccionario. ¿Qué contrato hash/igualdad debe cumplirse, qué riesgo si cambia estado relevante y cómo lo probarías?

<details>
<summary>Respuesta esperada</summary>

Objetos iguales deben tener hashes iguales y hashes deben permanecer estables durante vida como objetos hashables; distintos pueden colisionar. Prefiere estado de igualdad inmutable estable para claves o haz no hashables objetos mutables de igualdad por valor. Prueba instancias distintas iguales, búsqueda con clave igual y política de mutación soportada.

**Explicación:** Cambiar hash de clave puede invalidar búsqueda; definir __eq__ sin __hash__ normalmente vuelve clase Python no hashable.

**Intención del entrevistador:** Evaluar diseño de invariantes y pruebas, no unicidad de hash.

**Errores comunes**

- Exigir hashes distintos para cada par desigual.

**Preguntas de seguimiento**

- ¿Por qué una tupla con una lista no es clave utilizable?

**Ejemplo**

Dos objetos clave inmutables distintos e iguales deben recuperar mismo valor asociado; prueba sin suponer hashes distintos para desiguales.

**Rúbrica de autoevaluación**

- 1 — Declara reglas de hash igual y estabilidad durante vida, permitiendo colisiones.
- 1 — Explica riesgo de clave mutable y propone pruebas de igualdad, búsqueda y política de mutación.

Máximo: 2

</details>

**Requisitos previos**

- [Igualdad y hashing](../../technical-interview-preparation/09-object-identity-references-and-copying/README.es.md)

## Estructuras de datos y algoritmos

### algorithms.binary-precondition

`junior` · `data-structures-algorithms`

¿Por qué búsqueda binaria no sirve para lista arbitraria desordenada? Compara con lineal y declara coste en acceso aleatorio ordenado.

<details>
<summary>Respuesta esperada</summary>

Búsqueda binaria descarta mitad de posiciones usando orden ascendente. Sin orden puede descartar objetivo. Lineal funciona sin ordenar en O(n) peor caso; binaria en entrada ordenada de acceso aleatorio usa O(log n) comparaciones.

**Explicación:** Invariante de datos ordenados justifica eliminación.

**Intención del entrevistador:** Evaluar precondiciones de algoritmos.

**Errores comunes**

- Suponer búsqueda binaria válida en cualquier lista.

**Preguntas de seguimiento**

- ¿Validar orden en cada búsqueda conservaría coste total logarítmico?

**Ejemplo**

En [9,1,3], comparar valor central no permite eliminar izquierda de forma segura al buscar 9.

**Rúbrica de autoevaluación**

- 1 — Declara orden y explica eliminación segura.
- 1 — Compara costes de peor caso lineal y binario bajo supuestos indicados.

Máximo: 2

</details>

**Requisitos previos**

- [Elige según el contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.es.md)
- [2. Búsqueda binaria](../../problem-solving-and-live-coding/05-searching-algorithms/README.es.md)

### algorithms.duplicate-membership

`junior` · `data-structures-algorithms`

Detecta si una lista de IDs hashables contiene duplicado. ¿Qué estructura elegirías y cuáles son los costes de tiempo y espacio auxiliar?

<details>
<summary>Respuesta esperada</summary>

Mantén conjunto de IDs vistos. Por cada ID, devuelve True si ya visto, si no insértalo. Devuelve False al final. Bajo supuestos habituales de hashing promedio y hash/igualdad de coste constante, tiempo O(n), espacio extra O(n) en el peor tamaño de entrada.

**Explicación:** Conjunto permite pertenencia sin recorrer prefijo repetidamente. Colisiones en peor caso pueden degradar tiempo; hashabilidad es requisito.

**Intención del entrevistador:** Evaluar elección de representación, corrección y supuestos de complejidad.

**Errores comunes**

- Afirmar búsqueda O(1) garantizada en peor caso.
- Olvidar entrada vacía o tratar IDs iguales como distintos por posición.

**Preguntas de seguimiento**

- ¿Y si IDs no son hashables?

**Ejemplo**

`[3, 8, 3]` → True; `[]` → False; `[3, 8]` → False.

**Rúbrica de autoevaluación**

- 1 — Describe algoritmo de conjunto de vistos con terminación correcta.
- 1 — Declara tiempo promedio O(n) con supuestos de hashing y espacio extra O(n).
- 1 — Comprueba entrada vacía y repetida y declara requisito hashable.

Máximo: 3

</details>

**Requisitos previos**

- [Elige según el contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.es.md)

### algorithms.frequency-map

`junior` · `data-structures-algorithms`

¿Cómo contarías ocurrencias de cada etiqueta hashable en una lista? Muestra resultado para [a,a,b] y explica elección de estructura.

<details>
<summary>Respuesta esperada</summary>

Usa diccionario de etiqueta a conteo, actualizando con get(label, 0) + 1. Resultado {"a": 2, "b": 1}.

**Explicación:** Conjunto pierde multiplicidad; mapeo conserva contador por clave.

**Intención del entrevistador:** Evaluar elección de colección y acumulación.

**Errores comunes**

- Usar conjunto esperando conservar conteos.

**Preguntas de seguimiento**

- ¿Qué debe devolver entrada vacía?

**Ejemplo**

Para ["b","b","b"], mapeo es {"b":3}.

**Rúbrica de autoevaluación**

- 1 — Elige diccionario y describe incremento por clave.
- 1 — Predice ambos conteos y explica insuficiencia del conjunto.

Máximo: 2

</details>

**Requisitos previos**

- [Elige según el contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.es.md)
- [1. Acumulador y mapa de frecuencias](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)

### algorithms.recursion-stack

`mid` · `data-structures-algorithms`

Para sumar enteros de 0 a n con n no negativo, da caso base y recurrencia. Compara tiempo/espacio auxiliar recursivo e iterativo bajo aritmética de coste fijo.

<details>
<summary>Respuesta esperada</summary>

S(0)=0; S(n)=n+S(n-1). Ambos recorridos usan O(n) tiempo; recursivo usa O(n) pila y acumulador O(1) espacio extra.

**Explicación:** Progreso al caso base importa; límite de recursión Python restringe profundidad práctica.

**Intención del entrevistador:** Evaluar terminación y análisis de recursos.

**Errores comunes**

- Ignorar marcos de pila al informar espacio auxiliar.

**Preguntas de seguimiento**

- ¿Por qué rechazar negativos antes de recurrir?

**Ejemplo**

S(3) = 3 + 2 + 1 + 0 = 6.

**Rúbrica de autoevaluación**

- 1 — Da base, recurrencia y progreso hacia cero.
- 1 — Informa tiempo y espacio de pila/acumulador correctamente.

Máximo: 2

</details>

**Requisitos previos**

- [Elige según el contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.es.md)
- [2. Implementación en Python](../../problem-solving-and-live-coding/04-recursion/README.es.md)

### algorithms.stable-insertion

`mid` · `data-structures-algorithms`

Define estabilidad al ordenar registros por nota. ¿Cómo la conserva insertion sort y cuál es su tiempo de peor caso? Ilustra con registros de notas iguales.

<details>
<summary>Respuesta esperada</summary>

Registros de claves iguales conservan orden relativo original. En insertion sort desplaza solo claves estrictamente mayores e inserta tras iguales en prefijo ordenado. Peor tiempo O(n²).

**Explicación:** Desplazar iguales puede invertir orden aunque notas queden ordenadas correctamente.

**Intención del entrevistador:** Evaluar estabilidad más allá de salida ordenada.

**Errores comunes**

- Verificar solo notas numéricas e ignorar identidad del registro.

**Preguntas de seguimiento**

- ¿Qué entrada revelaría implementación inestable?

**Ejemplo**

[(A,2),(B,1),(C,2)] se vuelve [(B,1),(A,2),(C,2)] al ordenar establemente por nota.

**Rúbrica de autoevaluación**

- 1 — Define estabilidad y regla de desplazar estrictamente mayor.
- 1 — Declara O(n²) en peor caso e ilustra orden de claves iguales.

Máximo: 2

</details>

**Requisitos previos**

- [Elige según el contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.es.md)
- [4. Insertion sort](../../problem-solving-and-live-coding/06-sorting-algorithms/README.es.md)

### algorithms.two-pointer-pair

`mid` · `data-structures-algorithms`

Para enteros ordenados ascendentes, decide si dos índices distintos suman objetivo. Explica movimientos, terminación y costes.

<details>
<summary>Respuesta esperada</summary>

Empieza left=0, right=n-1. Mientras left < right compara suma: igual éxito, menor incrementa left, mayor decrementa right. Si se encuentran, falla. Orden justifica pares descartados. O(n) tiempo, O(1) extra bajo aritmética de coste fijo.

**Explicación:** Cada movimiento reduce intervalo y nunca usa mismo índice dos veces.

**Intención del entrevistador:** Evaluar invariante, corrección y complejidad.

**Errores comunes**

- Usar left <= right permitiendo contar elemento único dos veces.

**Preguntas de seguimiento**

- ¿Por qué [3,3] funciona para objetivo 6 pero [3] no?

**Ejemplo**

[1,3,4,7] con objetivo 7 tiene éxito por índices 1 y 2.

**Rúbrica de autoevaluación**

- 1 — Describe movimientos, justificación del orden y separación estricta de índices.
- 1 — Declara tiempo lineal y espacio extra constante con terminación.

Máximo: 2

</details>

**Requisitos previos**

- [Elige según el contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.es.md)
- [2. Dos punteros](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)

### algorithms.window-tradeoff

`senior` · `data-structures-algorithms`

Halla suma máxima de k enteros consecutivos, incluida entrada toda negativa. Compara recalcular cada ventana con suma móvil, declara supuestos y propone pruebas límite.

<details>
<summary>Respuesta esperada</summary>

Exige 1 <= k <= n. Suma primeros k, inicializa best con esa suma, luego resta saliente y añade entrante. Recalcular cuesta O((n-k+1)k); móvil cuesta O(n) tiempo y O(1) extra para acceso aleatorio bajo aritmética de coste fijo. Prueba k=1, k=n, negativos y k inválido.

**Explicación:** Actualización móvil reutiliza trabajo; iniciar best en cero admite ventana inexistente para negativos.

**Intención del entrevistador:** Evaluar optimización ligada a contrato preciso y oráculo de prueba.

**Errores comunes**

- Afirmar O(nk) inevitable o iniciar best en cero.

**Preguntas de seguimiento**

- ¿Qué resultado debe producir [-4,-2,-5] con k=2?

**Ejemplo**

[-4,-2,-5], k=2 da max(-6,-7) = -6.

**Rúbrica de autoevaluación**

- 1 — Define k válido, invariante móvil e inicialización correcta.
- 1 — Compara costes con supuestos y propone pruebas límite/negativas.

Máximo: 2

</details>

**Requisitos previos**

- [Elige según el contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.es.md)
- [3. Ventana deslizante fija](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)

## Programación orientada a objetos

### oop.class-list-sharing

`junior` · `oop`

Clase define members=[] a nivel de clase. ¿Por qué instancias pueden compartir adiciones inesperadamente? Muestra cómo hacer listas independientes.

<details>
<summary>Respuesta esperada</summary>

Atributo mutable de clase se comparte salvo si se oculta por atributo de instancia. Inicializa self.members=[] en __init__ para crear lista distinta por instancia.

**Explicación:** Append muta objeto compartido, mientras asignar atributo de instancia cambia búsqueda de esa instancia.

**Intención del entrevistador:** Evaluar atributos mutables de clase.

**Errores comunes**

- Mantener lista en clase y suponer self crea copia.

**Preguntas de seguimiento**

- ¿Qué atributo de clase podría compartirse razonablemente?

**Ejemplo**

Dos grupos nuevos deben tener listas vacías separadas; añadir miembro a uno deja otro vacío.

**Rúbrica de autoevaluación**

- 1 — Explica atributo mutable compartido y mutación.
- 1 — Inicializa lista independiente y predice aislamiento.

Máximo: 2

</details>

**Requisitos previos**

- [Atributos y enlace](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.es.md)

### oop.independent-state

`junior` · `oop`

Dos instancias Counter inicializan self.value=0. Solo first.increment() se ejecuta. ¿Qué valores y por qué?

<details>
<summary>Respuesta esperada</summary>

Primera 1 y segunda 0; cada instancia posee su atributo y método enlazado recibe instancia como self.

**Explicación:** Clase define comportamiento; objetos pueden mantener estado independiente.

**Intención del entrevistador:** Evaluar estado de instancia y enlace de método.

**Errores comunes**

- Tratar todas instancias como compartiendo self.value.

**Preguntas de seguimiento**

- ¿Cómo probarías instancias independientes?

**Ejemplo**

first.increment(); assert second.value == 0.

**Rúbrica de autoevaluación**

- 1 — Predice ambos valores.
- 1 — Explica estado por instancia y enlace de self.

Máximo: 2

</details>

**Requisitos previos**

- [Qué es y por qué](../../technical-interview-preparation/05-classes-and-objects/README.es.md)

### oop.initialization

`junior` · `oop`

¿Para qué sirve __init__ y cómo difiere de __new__? ¿Qué puede devolver __init__?

<details>
<summary>Respuesta esperada</summary>

__new__ es mecanismo de creación; __init__ inicializa instancia ya creada. __init__ debe devolver None, normalmente implícitamente.

**Explicación:** Llamada normal de clase coordina creación e inicialización.

**Intención del entrevistador:** Evaluar fundamentos del ciclo de vida de objetos.

**Errores comunes**

- Devolver self desde __init__ o llamarlo mecanismo de asignación.

**Preguntas de seguimiento**

- ¿Dónde inicializarías lista por instancia?

**Ejemplo**

def __init__(self): self.value = 0 inicializa estado sin devolver valor.

**Rúbrica de autoevaluación**

- 1 — Distingue creación de inicialización.
- 1 — Declara contrato de retorno None.

Máximo: 2

</details>

**Requisitos previos**

- [Qué es y por qué](../../technical-interview-preparation/05-classes-and-objects/README.es.md)

### oop.constructor-binding

`mid` · `oop`

Compara métodos de instancia, clase y estático. ¿Por qué constructor alternativo heredado debe usar cls(...) en vez de nombre de clase base? Declara supuesto de compatibilidad del constructor de subclase.

<details>
<summary>Respuesta esperada</summary>

Métodos de instancia reciben self; de clase reciben cls; estáticos no reciben ninguno implícitamente. Usar cls(...) permite subclase compatible construir instancia propia en vez de forzar tipo base.

**Explicación:** Enlace determina argumento implícito, no ausencia de efectos secundarios.

**Intención del entrevistador:** Evaluar elección de método y extensibilidad de subclase.

**Errores comunes**

- Suponer método estático automáticamente puro.

**Preguntas de seguimiento**

- ¿Y si subclase exige argumentos adicionales?

**Ejemplo**

SubGroup.from_label("A") compatible debe devolver SubGroup si fábrica usa cls.

**Rúbrica de autoevaluación**

- 1 — Identifica enlace implícito en los tres tipos.
- 1 — Explica construcción con cls y restricción de compatibilidad.

Máximo: 2

</details>

**Requisitos previos**

- [Atributos y enlace](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.es.md)

### oop.length-and-repr

`mid` · `oop`

StudyGroup necesita len(group), str(group) amigable y repr(group) para depuración. ¿Qué métodos implementan y qué debe devolver longitud?

<details>
<summary>Respuesta esperada</summary>

Implementa __len__, __str__, __repr__. __len__ devuelve entero no negativo representando longitud; __str__ se orienta al usuario, __repr__ ayuda depuración y no necesita ser Python ejecutable.

**Explicación:** Usa protocolos documentados en vez de inventar nombres dunder.

**Intención del entrevistador:** Evaluar integración con protocolos Python.

**Errores comunes**

- Devolver conteo negativo o suponer que repr debe reconstruir objeto.

**Preguntas de seguimiento**

- ¿Qué devolvería len para grupo vacío?

**Ejemplo**

__len__ puede devolver len(self.members); grupo vacío tiene longitud cero.

**Rúbrica de autoevaluación**

- 1 — Mapea tres operaciones a métodos correctos.
- 1 — Explica longitud entera no negativa y finalidades distintas de cadenas.

Máximo: 2

</details>

**Requisitos previos**

- [Métodos especiales](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.es.md)

### oop.replaceable-collaborator

`mid` · `oop`

Un notificador de informes debe admitir canales de texto y email, luego canal falso en pruebas. Compara herencia y composición; propone diseño sin cambiar notificador por canal. Explica un compromiso y cómo un doble probaría el contrato.

<details>
<summary>Respuesta esperada</summary>

Inyecta colaborador con contrato send definido; notificador delega. Canales compatibles pueden heredar base o cumplir comportamiento mediante duck typing. Herencia sirve a subtipos reales que respetan contrato base, no solo reutilización.

**Explicación:** Composición hace dependencias explícitas y sustituibles, al coste de indirección. Nombres de métodos solos no aseguran sustitución.

**Intención del entrevistador:** Evaluar contratos de comportamiento y decisiones de diseño comprobable.

**Errores comunes**

- Exigir jerarquía profunda solo para reutilizar código.
- Suponer que todo método send tiene misma semántica.

**Preguntas de seguimiento**

- ¿Qué debe demostrar un canal falso sobre el contrato?

**Ejemplo**

`Notifier(channel).notify('Ready')` delega al `send('Ready')` del doble, devolviendo `test: Ready` sin acceder a red.

**Rúbrica de autoevaluación**

- 1 — Propone inyección explícita de colaborador y delegación.
- 1 — Distingue contrato de subtipo de composición y duck typing.
- 1 — Explica prueba con doble y al menos un compromiso.

Máximo: 3

</details>

**Requisitos previos**

- [Polimorfismo y composición](../../technical-interview-preparation/07-inheritance-polymorphism-and-composition/README.es.md)

### oop.invariant-boundary

`senior` · `oop`

Diseña retirada de inventario para que cantidad nunca sea negativa por contrato público. Explica orden de validación, lectura y pruebas; ¿guion bajo es frontera de seguridad?

<details>
<summary>Respuesta esperada</summary>

Expón remove con validación antes de mutación; rechaza cantidad fuera del dominio documentado o superior a inventario sin cambiar saldo. Expón property de lectura si útil. Prueba retirada válida, insuficiente y estado intacto al fallar. Guion bajo es convención; name mangling/property no es seguridad.

**Explicación:** Encapsulación protege invariantes para operaciones admitidas; no impone control de acceso contra llamadores arbitrarios.

**Intención del entrevistador:** Evaluar diseño de invariante de dominio y pruebas negativas.

**Errores comunes**

- Restar primero y lanzar excepción dejando estado corrupto.

**Preguntas de seguimiento**

- ¿Cómo demostrarías que validación fallida no tiene efectos?

**Ejemplo**

Con cantidad 5, rechazar retirada de 6 debe dejar cantidad 5.

**Rúbrica de autoevaluación**

- 1 — Diseña validación antes de mutación y contrato de lectura explícito.
- 1 — Propone pruebas de estado intacto y distingue convención de seguridad.

Máximo: 2

</details>

**Requisitos previos**

- [Encapsulación y abstracción](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.es.md)

### oop.solid-contracts

`senior` · `oop`

Política de saldo depende de lector de base concreto con métodos de escritura ajenos. Rediseña dependencia usando DIP e ISP, con prueba doble y compromiso.

<details>
<summary>Respuesta esperada</summary>

Depende de contrato pequeño available, opcionalmente ABC con método abstracto, e inyecta lector que lo implemente. DIP separa política de infraestructura; ISP evita exigir operaciones no usadas. Prueba doble que devuelve saldo fijo. Añade abstracción solo si sustitución justifica indirección.

**Explicación:** Llamador necesita comportamiento, no detalles de almacenamiento; anotaciones solas no imponen semántica en ejecución.

**Intención del entrevistador:** Evaluar SOLID como compromisos de diseño.

**Errores comunes**

- Crear cinco clases solo para corresponder a cinco principios.

**Preguntas de seguimiento**

- ¿Cuándo una función simple sería más adecuada?

**Ejemplo**

Inyecta doble solo available que devuelve 7 y comprueba política sin base.

**Rúbrica de autoevaluación**

- 1 — Explica DIP e ISP mediante contrato pequeño sustituible.
- 1 — Propone prueba con doble y sopesa indirección adicional.

Máximo: 2

</details>

**Requisitos previos**

- [Encapsulación y abstracción](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.es.md)
- [SOLID como preguntas de diseño](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.es.md)

## Internals de Python

### internals.del-binding

`junior` · `python-internals`

Dado first=[]; second=first; del first; second.append(3), ¿cuál es second? ¿del garantiza destrucción?

<details>
<summary>Respuesta esperada</summary>

second es [3]. del elimina enlace first, no objeto mientras second aún lo referencia fuertemente. Python no garantiza destrucción inmediata.

**Explicación:** Alcanzabilidad y propiedad, no nombre particular, determinan si referencia aún mantiene objeto vivo.

**Intención del entrevistador:** Evaluar razonamiento sobre vida del objeto.

**Errores comunes**

- Suponer que del first vacía lista.

**Preguntas de seguimiento**

- ¿Y si contenedor global aún guarda lista?

**Ejemplo**

Lista almacenada en dos nombres sigue utilizable mediante nombre restante.

**Rúbrica de autoevaluación**

- 1 — Predice second y distingue eliminación de enlace de destrucción.
- 1 — Explica referencia fuerte y ausencia de garantía de finalización inmediata.

Máximo: 2

</details>

**Requisitos previos**

- [Vida y alcanzabilidad de objetos](../../technical-interview-preparation/10-python-memory-management/README.es.md)

### internals.iterator-exhaustion

`junior` · `python-internals`

Dado it=iter([1,2,3]); next(it); print(list(it)); print(list(it)), ¿qué imprime y por qué?

<details>
<summary>Respuesta esperada</summary>

Imprime [2,3] luego []. next consumió 1; primera llamada list consumió resto, así que iterador se agotó. iter(it) devuelve ese iterador, no nuevo recorrido.

**Explicación:** Lista es iterable y suministra nuevos iteradores; iterador conserva estado del recorrido.

**Intención del entrevistador:** Evaluar consumo único.

**Errores comunes**

- Suponer list(it) reinicia iterador.

**Preguntas de seguimiento**

- ¿Qué excepción lanza next(it) una vez agotado?

**Ejemplo**

iter([1,2]) y otro iter([1,2]) son recorridos separados.

**Rúbrica de autoevaluación**

- 1 — Predice ambas listas impresas.
- 1 — Explica estado, agotamiento y diferencia de iterable.

Máximo: 2

</details>

**Requisitos previos**

- [Protocolo de iteración](../../technical-interview-preparation/11-iterators-generators-and-comprehensions/README.es.md)

### internals.context-exit

`mid` · `python-internals`

Gestor abre recurso y cuerpo lanza RuntimeError. Explica __enter__, __exit__, supresión y qué cambia si falla propia entrada.

<details>
<summary>Respuesta esperada</summary>

__enter__ devuelve valor de as. Tras entrada exitosa, __exit__ recibe detalles de excepción y libera recurso; false/None propaga excepción del cuerpo, truthy suprime. Si entrada falla, exit de ese gestor no se llama automáticamente; entrada gestiona adquisición parcial.

**Explicación:** Limpieza y supresión son decisiones separadas; retorno truthy accidental oculta errores.

**Intención del entrevistador:** Evaluar gestión de recursos y semántica de fallo.

**Errores comunes**

- Suponer exit se ejecuta aunque enter lance excepción.

**Preguntas de seguimiento**

- ¿Cómo probarías limpieza exactamente una vez?

**Ejemplo**

Entrada exitosa seguida de fallo del cuerpo registra open y close una vez, con RuntimeError propagado si exit devuelve False.

**Rúbrica de autoevaluación**

- 1 — Describe entrada, detalles de salida y contrato de supresión truthy.
- 1 — Distingue fallo de cuerpo de entrada y adquisición parcial.

Máximo: 2

</details>

**Requisitos previos**

- [Protocolo with](../../technical-interview-preparation/13-context-managers/README.es.md)
- [Decisiones prácticas](../../technical-interview-preparation/13-context-managers/README.es.md)

### internals.decorator-contract

`mid` · `python-internals`

Decorador de registro debe registrar cada intento, incluidas llamadas que lanzan excepción, sin cambiar contrato del cálculo. ¿Cómo implementarías y probarías registro de intentos, retorno, argumentos, metadatos y propagación de fallo?

<details>
<summary>Respuesta esperada</summary>

Suponiendo que el registro funcione, registra cada intento antes de invocar la función decorada. Reenvía `*args` y `**kwargs`, devuelve resultado, conserva metadatos con `functools.wraps` y deja propagar excepciones. Prueba llamadas posicionales y nombradas, resultado, nombre y excepción deliberada; comprueba exactamente un registro por intento, incluido fallo.

**Explicación:** Wrapper transversal no debe alterar comportamiento central silenciosamente.

**Intención del entrevistador:** Evaluar decoradores y pruebas de conservación de comportamiento.

**Errores comunes**

- Olvidar devolver resultado u ocultar excepciones.
- Registrar solo retornos exitosos, omitiendo intentos fallidos.

**Preguntas de seguimiento**

- ¿Cuándo se aplican decoradores apilados?

**Ejemplo**

Usando `record_calls(records)` con lista inicialmente vacía, `divide(8, denominator=2)` decorada devuelve `4`; `divide(8, denominator=0)` lanza `ZeroDivisionError`. Después, `records` es igual a `['divide', 'divide']`.

**Rúbrica de autoevaluación**

- 1 — Especifica un registro por intento antes de llamada, reenvío, retorno, metadatos y conservación de excepción.
- 1 — Propone pruebas para cada contrato nombrado, comprobando registro de intentos en éxito y fallo.

Máximo: 2

</details>

**Requisitos previos**

- [Decoradores](../../technical-interview-preparation/12-closures-and-decorators/README.es.md)

### internals.late-binding

`mid` · `python-internals`

Dentro de fábrica, crea tres lambdas en bucle range(3), cada una devolviendo i. Si se llaman solo tras bucle, ¿qué devuelven? Muestra corrección para índices inmutables.

<details>
<summary>Respuesta esperada</summary>

Todas devuelven 2 porque cierres comparten enlace envolvente cambiante. Usa lambda i=i: i para enlazar valor inmutable actual como predeterminado al definir, o fábrica separada.

**Explicación:** Captura del cierre no es instantánea automática; valor predeterminado se evalúa al crear función.

**Intención del entrevistador:** Evaluar momento de enlace y comportamiento de cierre.

**Errores comunes**

- Esperar 0, 1, 2 sin enlazar valores individuales.

**Preguntas de seguimiento**

- ¿Enlazar lista mutable como predeterminada la copiaría profundamente?

**Ejemplo**

[lambda i=i: i for i in range(3)] produce funciones que devuelven 0, 1, 2 respectivamente.

**Rúbrica de autoevaluación**

- 1 — Predice resultados tardíos y explica enlace compartido.
- 1 — Demuestra corrección válida por instantánea/fábrica para inmutables.

Máximo: 2

</details>

**Requisitos previos**

- [Cierres y ámbito](../../technical-interview-preparation/12-closures-and-decorators/README.es.md)

### internals.nested-copy

`mid` · `python-internals`

Diccionario contiene dos claves referenciando misma lista mutable. Necesitas grafo independiente conservando relación de alias dentro de copia. Compara asignación, copia superficial y profunda. Explica límites de copia y cómo probarías aislamiento y conservación del alias.

<details>
<summary>Respuesta esperada</summary>

Asignación comparte diccionario original; copia superficial crea diccionario externo nuevo pero comparte lista. Para estos contenedores incorporados, deepcopy copia lista anidada una vez y reutiliza copia para ambas claves mediante memo.

**Explicación:** Copia profunda puede preservar referencias repetidas y ciclos; no garantiza clonar cada objeto o recurso externo. Elige por propiedad y coste.

**Intención del entrevistador:** Evaluar identidad, alias anidados y semántica de copia.

**Errores comunes**

- Suponer copia superficial aislando valores mutables internos.
- Afirmar deepcopy creando objeto nuevo por referencia.

**Preguntas de seguimiento**

- ¿Cómo probarías que mutar lista copiada no afecta original?

**Ejemplo**

```python
from copy import deepcopy
shared = [1]
original = {"a": shared, "b": shared}
cloned = deepcopy(original)
assert cloned["a"] is cloned["b"]
assert cloned["a"] is not shared
```

**Rúbrica de autoevaluación**

- 1 — Contrasta correctamente asignación y copia superficial.
- 1 — Explica memo de deepcopy e identidad de alias conservada.
- 1 — Propone comprobaciones de identidad/mutación y declara límites de copia.

Máximo: 3

</details>

**Requisitos previos**

- [Identidad, igualdad y enlace](../../technical-interview-preparation/09-object-identity-references-and-copying/README.es.md)

### internals.cache-retention

`senior` · `python-internals`

Servicio CPython crece memoria reteniendo caché global. Explica retención alcanzable frente a ciclos inalcanzables, qué puede hacer gc.collect y cómo medirías y limitarías problema.

<details>
<summary>Respuesta esperada</summary>

Valores alcanzables de caché siguen vivos; conteo convencional de referencias más GC de ciclos recupera muchos objetos/ciclos inalcanzables, pero gc.collect no libera alcanzables ni garantiza RSS menor. Inspecciona propiedad y compara instantáneas tracemalloc junto con métricas de memoria del proceso; limita por presupuesto de cantidad/bytes, expulsa referencias y comprueba alias externos.

**Explicación:** Instantáneas de asignación Python no miden toda asignación nativa o RSS. Límite de cantidad no limita bytes.

**Intención del entrevistador:** Evaluar diagnóstico de memoria antes de optimización.

**Errores comunes**

- Forzar GC periódicamente manteniendo misma caché alcanzable ilimitada.

**Preguntas de seguimiento**

- ¿Por qué vaciar caché puede dejar valores vivos?

**Ejemplo**

Límite de 100 entradas no implica 100 bytes; compara asignaciones antes/después de expulsiones con carga representativa.

**Rúbrica de autoevaluación**

- 1 — Explica alcanzabilidad, GC de ciclos y límites de recolección.
- 1 — Propone retención limitada y medición distinguiendo tracemalloc de memoria del proceso.

Máximo: 2

</details>

**Requisitos previos**

- [Vida y alcanzabilidad de objetos](../../technical-interview-preparation/10-python-memory-management/README.es.md)
- [Retención y medición](../../technical-interview-preparation/10-python-memory-management/README.es.md)

### internals.gil-workload

`senior` · `python-internals`

Servicio CPython 3.13 ejecuta muchas operaciones I/O bloqueantes, transformaciones pesadas en Python puro e incrementa contador compartido. Propón elecciones de concurrencia y plan de verificación; considera builds convencional y experimental free-threaded.

<details>
<summary>Respuesta esperada</summary>

CPython convencional con GIL permite un hilo ejecutar bytecode Python a la vez en un intérprete. Hilos sirven a I/O bloqueante; asyncio a I/O cooperativa con APIs compatibles; procesos pueden beneficiar Python CPU-bound al coste de serialización/memoria. Build experimental free-threaded puede permitir hilos Python paralelos; algunas extensiones pueden reactivar GIL. Sincroniza contador con lock compartido y mide throughput, costes de recursos y corrección en build real.

**Explicación:** GIL depende de implementación y no garantiza ausencia de carreras en aplicación. Total correcto aislado sin sincronización es evidencia débil; prueba contrato del lock y propagación de fallos aparte del rendimiento.

**Intención del entrevistador:** Evaluar razonamiento arquitectónico condicional, conciencia de versión y validación de invariantes.

**Errores comunes**

- Afirmar hilos nunca ayudan o GIL hace seguras actualizaciones.
- Suponer free-threading predeterminado o aceleración garantizada.

**Preguntas de seguimiento**

- ¿Por qué total correcto en una ejecución sin sincronización no prueba seguridad?

**Ejemplo**

Compara base secuencial, hilos limitados para I/O bloqueante y procesos para CPU; registra tiempo y memoria aparte de prueba de corrección del contador con lock.

**Rúbrica de autoevaluación**

- 1 — Distingue GIL convencional de free-threading experimental con salvedad de extensiones.
- 1 — Elige estrategias I/O/CPU con compromiso y propone medición en la carga real.
- 1 — Protege invariante compartido y distingue pruebas de corrección de benchmarks.

Máximo: 3

</details>

**Requisitos previos**

- [GIL en Python 3.13](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.es.md)
- [Concurrencia y paralelismo](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.es.md)
- [Ejemplo de estado compartido](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.es.md)

## Pruebas y depuración

### testing.else-finally

`junior` · `testing-debugging`

¿Qué roles tienen else y finally en try? Explica comportamiento cuando operación protegida lanza excepción inesperada.

<details>
<summary>Respuesta esperada</summary>

else se ejecuta cuando bloque try termina normalmente sin excepción; finally ejecuta al salir para limpieza. Excepción no capturada se propaga tras finally salvo si limpieza altera resultado.

**Explicación:** No retornes desde finally para ocultar fallo.

**Intención del entrevistador:** Evaluar flujo estructurado de excepciones.

**Errores comunes**

- Tratar finally como código solo de éxito.

**Preguntas de seguimiento**

- ¿Cuándo with puede ser más claro?

**Ejemplo**

Tras RuntimeError no capturado, limpieza en finally aún se ejecuta antes de propagar.

**Rúbrica de autoevaluación**

- 1 — Distingue else de finalización normal de finally de limpieza.
- 1 — Explica propagación de excepción inesperada y salvedad de limpieza.

Máximo: 2

</details>

**Requisitos previos**

- [Fronteras de excepción](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)

### testing.specific-catch

`junior` · `testing-debugging`

Al convertir texto a int, ¿por qué capturar ValueError específicamente en vez de ocultar toda excepción? ¿Qué debe hacer texto inválido?

<details>
<summary>Respuesta esperada</summary>

Captura fallo esperado de conversión en frontera que puede tratar o traducir. Informa o lanza error acordado de entrada inválida; deja propagar excepciones inesperadas ajenas.

**Explicación:** Devolver cero para texto incorrecto confunde entrada inválida con cero válido.

**Intención del entrevistador:** Evaluar alcance de excepción y contratos de datos.

**Errores comunes**

- Capturar todo y devolver cero incondicionalmente.

**Preguntas de seguimiento**

- ¿Qué distingue "0" de "abc" en pruebas?

**Ejemplo**

int("0") funciona, int("abc") lanza ValueError.

**Rúbrica de autoevaluación**

- 1 — Elige excepción específica esperada y explica propagación.
- 1 — Distingue texto inválido de cero válido en contrato.

Máximo: 2

</details>

**Requisitos previos**

- [Fronteras de excepción](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)

### testing.test-levels

`junior` · `testing-debugging`

Distingue pruebas unitarias, integración y extremo a extremo para servicio de informes. Da ejemplo de cada.

<details>
<summary>Respuesta esperada</summary>

Unitario: cuenta IDs únicos con loader doble controlado. Integración: ejercita loader real contra base de pruebas. Extremo a extremo: solicita informe por interfaz admitida y verifica respuesta en flujo completo.

**Explicación:** Niveles difieren por fronteras ejercitadas, no solo número de aserciones.

**Intención del entrevistador:** Evaluar alcance de pruebas y fronteras de dependencia.

**Errores comunes**

- Llamar prueba con todas dependencias simuladas de extremo a extremo.

**Preguntas de seguimiento**

- ¿Por qué conservar prueba de integración real si unitarias pasan?

**Ejemplo**

Loader doble que devuelve [1,1,2] permite aserción unitaria de dos finalizaciones únicas.

**Rúbrica de autoevaluación**

- 1 — Identifica fronteras unitaria e integración con ejemplos distintos.
- 1 — Describe flujo completo admitido para extremo a extremo.

Máximo: 2

</details>

**Requisitos previos**

- [Probar y depurar con evidencias](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)
- [Decisiones empiezan en el requisito](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.es.md)

### testing.boundary-oracle

`mid` · `testing-debugging`

parse_quantity acepta texto entero no negativo, incluso espacios admitidos por int, y rechaza inválidos o negativos. Da pruebas con salidas/errores esperados que detecten versión devolviendo cero en entrada incorrecta.

<details>
<summary>Respuesta esperada</summary>

Afirma "0" devuelve 0 y " 12 " devuelve 12; exige InvalidQuantity documentada para "abc", "-1" y "". Comprobar excepción específica en vez de mera ejecución detecta cero silencioso.

**Explicación:** Aserciones positivas y negativas deben distinguir contrato previsto de implementaciones incorrectas plausibles.

**Intención del entrevistador:** Evaluar precisión del oráculo y cobertura de límites.

**Errores comunes**

- Afirmar solo que función fue llamada o devolvió int.

**Preguntas de seguimiento**

- ¿Qué caso detecta rechazo de cero válido?

**Ejemplo**

Prueba exigiendo InvalidQuantity para "abc" falla cuando implementación devuelve 0 silenciosamente.

**Rúbrica de autoevaluación**

- 1 — Especifica resultados exactos para normal y límite cero.
- 1 — Especifica comportamiento de error exacto para inválidos y negativos.

Máximo: 2

</details>

**Requisitos previos**

- [Fronteras de excepción](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)
- [Probar y depurar con evidencias](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)
- [Práctica](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)

### testing.debugging-evidence

`mid` · `testing-debugging`

Parser antes funcional falla en una entrada. Describe secuencia de depuración y evidencias a registrar sin exponer payloads privados.

<details>
<summary>Respuesta esperada</summary>

Reproduce con entrada mínima saneada, inspecciona traceback y estado relevante, formula hipótesis, cambia una causa, repite reproducción y añade prueba de regresión. Registra contexto seguro y resultados reales, ocultando secretos.

**Explicación:** Cambios controlados facilitan interpretar evidencia causal.

**Intención del entrevistador:** Evaluar depuración disciplinada y privacidad.

**Errores comunes**

- Registrar credenciales crudas y cambiar varias condiciones a la vez.

**Preguntas de seguimiento**

- ¿Y si no logras reproducir fallo?

**Ejemplo**

Sustituye entrada privada por cadena ficticia mínima malformada que reproduzca misma excepción.

**Rúbrica de autoevaluación**

- 1 — Describe secuencia de reproducción, hipótesis y verificación controlada.
- 1 — Propone evidencia de regresión con logs saneados y resultados reales.

Máximo: 2

</details>

**Requisitos previos**

- [Probar y depurar con evidencias](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)

### testing.exception-cause

`mid` · `testing-debugging`

En frontera de conversión, traduce ValueError a InvalidQuantity sin perder causa. Muestra sintaxis y distingue de raise sin argumento.

<details>
<summary>Respuesta esperada</summary>

En except ValueError as error, usa raise InvalidQuantity("invalid quantity") from error. Causa explícita se conserva. raise sin argumento relanza excepción activa en vez de traducir.

**Explicación:** Traducción ofrece contrato de dominio estable conservando evidencia diagnóstica.

**Intención del entrevistador:** Evaluar encadenamiento de excepciones y diagnóstico.

**Errores comunes**

- Sustituir error por valor de éxito.

**Preguntas de seguimiento**

- ¿Qué aserción verifica tipo de causa original?

**Ejemplo**

assert isinstance(caught.exception.__cause__, ValueError) en contexto assertRaises de unittest.

**Rúbrica de autoevaluación**

- 1 — Muestra sintaxis raise-from explícita con error capturado.
- 1 — Distingue relanzar de traducir y explica conservación de causa.

Máximo: 2

</details>

**Requisitos previos**

- [Fronteras de excepción](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)

### testing.coverage-vs-discrimination

`senior` · `testing-debugging`

Parser tiene alta cobertura de líneas pero implementación mutada que devuelve cero para texto inválido sigue pasando. Explica significado y propone estrategia más fuerte sin afirmar pruebas demuestran toda corrección.

<details>
<summary>Respuesta esperada</summary>

Cobertura mide ejecución, no corrección. Defecto plausible superviviente muestra oráculo insuficiente para ese comportamiento. Añade aserciones precisas de valor/excepción, límites y regresión; ejecuta versiones correcta e incorrecta intencional. Prueba fronteras reales por separado, con preparación determinista. Pasar refuerza evidencia, no prueba todo comportamiento.

**Explicación:** Prueba negativa útil rechaza defecto representativo mientras referencia pasa.

**Intención del entrevistador:** Evaluar calidad de pruebas y límites de garantía.

**Errores comunes**

- Tratar porcentaje de cobertura como prueba de corrección.

**Preguntas de seguimiento**

- ¿Por qué conservar aserciones de estado intacto tras operación rechazada?

**Ejemplo**

Exige salida cero correcta para "0" y excepción específica para "abc"; variante cero silencioso debe fallar.

**Rúbrica de autoevaluación**

- 1 — Explica defecto superviviente y distinción cobertura/oráculo.
- 1 — Propone pruebas discriminantes deterministas, verificación de fronteras y límites honestos.

Máximo: 2

</details>

**Requisitos previos**

- [Probar y depurar con evidencias](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)
- [Práctica](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)

## Backend y APIs

### api.http-request-response

`junior` · `backend-apis`

Describe elementos principales de solicitud y respuesta HTTP. Da ejemplo GET y explica qué lado elige estado.

<details>
<summary>Respuesta esperada</summary>

Solicitud tiene método, destino, headers y contenido opcional. Servidor responde estado, headers y contenido opcional. Cliente envía GET /lessons; servidor determina estado y representación según contrato.

**Explicación:** Estado HTTP describe resultado, no acción elegida por cliente.

**Intención del entrevistador:** Evaluar fundamentos de solicitud/respuesta HTTP.

**Errores comunes**

- Suponer que toda solicitud o respuesta HTTP debe contener JSON.

**Preguntas de seguimiento**

- ¿Qué header de respuesta puede describir formato del contenido?

**Ejemplo**

GET /lessons → 200 con Content-Type: application/json y representación de lecciones.

**Rúbrica de autoevaluación**

- 1 — Identifica método/destino frente a estado y ambos conjuntos de headers.
- 1 — Da ejemplo GET coherente y distingue contenido opcional.

Máximo: 2

</details>

**Requisitos previos**

- [Contratos cliente, servidor y recurso](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.es.md)

### api.status-contract

`junior` · `backend-apis`

Endpoint /lessons solo GET recibe GET /missing y POST /lessons. ¿Qué estados adecuados y qué header acompaña método no admitido?

<details>
<summary>Respuesta esperada</summary>

Devuelve 404 para recurso ausente y 405 para destino conocido con método no admitido. Incluye Allow: GET bajo contrato solo GET. GET exitoso puede devolver 200.

**Explicación:** Destinos ausentes y métodos no admitidos son fallos distintos.

**Intención del entrevistador:** Evaluar semántica de estados y contratos.

**Errores comunes**

- Devolver 200 para todo resultado o confundir 404 con 405.

**Preguntas de seguimiento**

- ¿Qué evitaría revelar un cuerpo de error estable?

**Ejemplo**

GET /missing → 404; POST /lessons → 405 y Allow: GET.

**Rúbrica de autoevaluación**

- 1 — Elige ambos estados correctos para casos distintos.
- 1 — Incluye Allow y explica relación con destino conocido.

Máximo: 2

</details>

**Requisitos previos**

- [Diseño de respuesta](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.es.md)

### api.idempotent-retry

`mid` · `backend-apis`

POST de creación agota tiempo tras posible éxito. Compara reintentar POST con semántica PUT y DELETE; propone contrato seguro y explica por qué respuestas iguales no son necesarias.

<details>
<summary>Respuesta esperada</summary>

POST no garantiza idempotencia, así que reintento ciego puede duplicar creación. PUT y DELETE tienen efectos previstos idempotentes según HTTP, no respuestas necesariamente idénticas. Para creación reintentable usa contrato explícito de clave de idempotencia persistida, intentos limitados, timeouts y respeto a Retry-After cuando corresponda.

**Explicación:** Timeout no determina si servidor confirmó efecto secundario.

**Intención del entrevistador:** Evaluar incertidumbre de solicitud distribuida y diseño de contrato.

**Errores comunes**

- Reintentar todo POST sin semántica de deduplicación.

**Preguntas de seguimiento**

- ¿Por qué DELETE repetido puede devolver 204 y luego 404?

**Ejemplo**

Misma solicitud de creación con clave persistida no debe crear segundo recurso bajo contrato explícito.

**Rúbrica de autoevaluación**

- 1 — Distingue riesgo de reintento POST de idempotencia de efecto PUT/DELETE.
- 1 — Propone contrato explícito de reintento y comportamiento de red limitado.

Máximo: 2

</details>

**Requisitos previos**

- [Contratos cliente, servidor y recurso](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.es.md)

### api.payload-boundary

`mid` · `backend-apis`

API acepta exactamente campo title, cadena de 1–80 caracteres tras trim. Explica parsing frente a validación; propone entradas aceptadas/rechazadas y límites de transporte.

<details>
<summary>Respuesta esperada</summary>

Parsing decodifica JSON; validación comprueba forma objeto, campo permitido, tipo cadena y longitud tras trim. Acepta {"title":" SQL "} como SQL; rechaza campos ausentes/extras, booleanos, blancos y título largo. Limita cuerpo antes de parsing cuando sea posible y define tratamiento de claves duplicadas aparte.

**Explicación:** JSON sintácticamente válido puede violar reglas de dominio. Dict decodificado no revela de forma fiable claves duplicadas en entrada cruda.

**Intención del entrevistador:** Evaluar validación por capas y pruebas de frontera.

**Errores comunes**

- Tratar parsing JSON exitoso como prueba de entrada de negocio válida.

**Preguntas de seguimiento**

- ¿Por qué rechazar campo owner adicional en este contrato?

**Ejemplo**

Título de exactamente 80 caracteres tras trim se acepta; 81 se rechaza.

**Rúbrica de autoevaluación**

- 1 — Separa parsing de validación de forma/tipo/longitud con ejemplos positivos y negativos.
- 1 — Identifica límites de transporte y claves duplicadas crudas como asuntos separados.

Máximo: 2

</details>

**Requisitos previos**

- [Validar la frontera](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.es.md)

### api.object-authorization

`senior` · `backend-apis`

Alumno autenticado puede pedir nota por ID. Diseña comprobaciones de acceso y política de respuesta para impedir leer nota ajena; explica filtración de existencia y pruebas de regresión.

<details>
<summary>Respuesta esperada</summary>

Autentica por identidad confiable verificada, luego autoriza acción en objeto específico mediante propiedad o política controlada por servidor antes de devolver contenido. Ausencia de credenciales válidas produce 401 con desafío. Acceso prohibido puede producir 403, o 404 bajo política coherente de ocultación. No confíes en propietario suministrado o token no verificado. Prueba ausencia de credenciales, propietario autorizado, no propietario autenticado, ID inexistente y cuerpo de denegación sin datos protegidos.

**Explicación:** 403 frente a 404 puede revelar existencia. Ocultación exige política coherente; no sustituye autorización. Ejemplo local modela frontera posterior a autenticación, no verificación de tokens.

**Intención del entrevistador:** Evaluar control de acceso a nivel de objeto, contrato de error y pruebas negativas de seguridad.

**Errores comunes**

- Comprobar solo si llamador inició sesión.
- Devolver contenido con denegación o confiar en propietario indicado por cliente.

**Preguntas de seguimiento**

- ¿Cómo cambiarías pruebas si política oculta existencia intencionalmente?

**Ejemplo**

Para nota 7 de alumno A, B autenticado recibe 403 (o 404 definido por política) sin contenido; A recibe 200; anónimos reciben 401.

**Rúbrica de autoevaluación**

- 1 — Exige identidad verificada en servidor más autorización por objeto.
- 1 — Explica 401/403/404 y política coherente de divulgación de existencia.
- 1 — Especifica pruebas positivas y negativas incluida confidencialidad del cuerpo denegado.

Máximo: 3

</details>

**Requisitos previos**

- [Autenticación frente a autorización](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.es.md)

## Bases de datos y SQL

### sql.keys-and-constraints

`junior` · `databases-sql`

Tabla lessons exige títulos únicos no nulos y minutos positivos no nulos. ¿Qué restricciones expresan reglas y para qué clave primaria? Explica la salvedad del tipado INTEGER en SQLite si minutes debe ser entero.

<details>
<summary>Respuesta esperada</summary>

Usa title TEXT NOT NULL UNIQUE y minutes INTEGER NOT NULL CHECK(minutes > 0); clave primaria identifica fila. En SQLite, INTEGER declarado solo no impone tipo estricto; usa comprobación adecuada de tipo almacenado y validación de aplicación para dominio entero.

**Explicación:** CHECK solo no rechaza NULL; combina con NOT NULL.

**Intención del entrevistador:** Evaluar restricciones de integridad relacional.

**Errores comunes**

- Suponer CHECK(minutes > 0) solo prohíbe NULL o fraccionarios.

**Preguntas de seguimiento**

- ¿Qué debe hacer insertar título duplicado?

**Ejemplo**

SQLite puede usar CHECK(typeof(minutes) = 'integer' AND minutes > 0) junto con NOT NULL.

**Rúbrica de autoevaluación**

- 1 — Selecciona restricciones correctas UNIQUE, NOT NULL y CHECK positivo.
- 1 — Explica clave primaria y por qué tipado entero SQLite requiere cuidado.

Máximo: 2

</details>

**Requisitos previos**

- [Modelo relacional y restricciones](../../technical-interview-preparation/18-relational-databases-and-sql/README.es.md)

### sql.null-and-order

`junior` · `databases-sql`

Dada lessons(id, title, minutes) con minutes anulable, escribe consulta para filas sin minutes ordenadas por id. Explica por qué = NULL y omitir ORDER BY son inadecuados.

<details>
<summary>Respuesta esperada</summary>

SELECT id, title FROM lessons WHERE minutes IS NULL ORDER BY id; comparación con NULL normalmente resulta desconocido, no verdadero, y WHERE conserva verdaderos. Sin ORDER BY, orden no garantizado.

**Explicación:** NULL representa información ausente/desconocida, no cero.

**Intención del entrevistador:** Evaluar filtro SQL con valor desconocido y orden explícito.

**Errores comunes**

- Usar minutes = NULL o suponer orden de inserción.

**Preguntas de seguimiento**

- ¿minutes=0 coincidiría con consulta?

**Ejemplo**

Con minutes NULL, 0, 20, solo fila NULL coincide.

**Rúbrica de autoevaluación**

- 1 — Usa IS NULL y ORDER BY id explícito.
- 1 — Explica comparación desconocida y ausencia de orden predeterminado.

Máximo: 2

</details>

**Requisitos previos**

- [Modelo relacional y restricciones](../../technical-interview-preparation/18-relational-databases-and-sql/README.es.md)

### sql.bound-values

`mid` · `databases-sql`

En sqlite3 Python, búsqueda acepta título y columna de orden elegida. ¿Cómo enlazar título de forma segura y restringir columna? Explica por qué placeholders no enlazan identificadores.

<details>
<summary>Respuesta esperada</summary>

Pasa title como parámetro de valor, p. ej. db.execute("SELECT id FROM lessons WHERE title = ?", (title,)). Usa consulta fija o mapa allowlist de opciones a identificadores SQL confiables; nunca interpoles entrada arbitraria. Placeholders representan valores, no sintaxis SQL como identificadores de columnas.

**Explicación:** Entrada enlazada sigue siendo dato incluso con comillas. Coma forma tupla de un elemento.

**Intención del entrevistador:** Evaluar construcción SQL segura y frontera de identificadores.

**Errores comunes**

- Concatenar título o nombre de columna crudo en SQL.

**Preguntas de seguimiento**

- ¿Cómo probarías títulos con comillas y opciones de orden no admitidas?

**Ejemplo**

Mapea "duration" a identificador fijo minutes; rechaza opciones desconocidas. Enlaza "O'Reilly" como dato title.

**Rúbrica de autoevaluación**

- 1 — Muestra valor title enlazado con tupla correcta.
- 1 — Explica límite de identificadores y enfoque consulta fija/allowlist.

Máximo: 2

</details>

**Requisitos previos**

- [Conectar con Python](../../technical-interview-preparation/18-relational-databases-and-sql/README.es.md)
- [Seguridad SQL](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.es.md)

### sql.zero-child-count

`mid` · `databases-sql`

Dadas groups(id, name) y tasks(id, group_id, done), devuelve conteo de tareas completadas por grupo, incluidos grupos sin completadas. ¿Cómo afectan ON, WHERE y COUNT a corrección? Supón que ambas columnas id son claves primarias, tasks.group_id referencia groups.id y done vale 0 o 1. Explica por qué agrupar solo por nombre es insuficiente.

<details>
<summary>Respuesta esperada</summary>

Haz LEFT JOIN tasks por ID de grupo con done = 1 en ON; agrupa por ID y nombre, cuenta tasks.id (no nulo en tareas reales). WHERE tasks.done = 1 descartaría filas extendidas con NULL; COUNT(*) contaría fila sin coincidencia.

**Explicación:** Agrupa por identidad estable incluso con nombres repetidos. Filtro en ON controla coincidencias sin eliminar grupos izquierdos.

**Intención del entrevistador:** Evaluar semántica de joins, granularidad y casos cero.

**Errores comunes**

- Usar INNER JOIN o filtrar completadas en WHERE.
- Agrupar solo por nombre no único o contar todas filas.

**Preguntas de seguimiento**

- ¿Qué ocurre si dos grupos tienen mismo nombre?

**Ejemplo**

```sql
SELECT g.id, g.name, COUNT(t.id)
FROM groups AS g LEFT JOIN tasks AS t
ON g.id = t.group_id AND t.done = 1
GROUP BY g.id, g.name
ORDER BY g.id;
```

**Rúbrica de autoevaluación**

- 1 — Usa LEFT JOIN por claves y filtro de completadas en ON.
- 1 — Cuenta ID no nulo del hijo y explica conteo cero.
- 1 — Agrupa por identidad estable y explica por qué solo nombre falla.

Máximo: 3

</details>

**Requisitos previos**

- [Relaciones y cardinalidad de joins](../../technical-interview-preparation/19-joins-aggregations-and-data-relationships/README.es.md)

### sql.atomic-transfer

`senior` · `databases-sql`

Transferencia de créditos debita cuenta y acredita otra. Diseña propiedad de transacción, comprobación condicional de saldo y verificación de fallo. Explica ACID y si índice nuevo solo garantiza mejor rendimiento.

<details>
<summary>Respuesta esperada</summary>

Usa transacción dedicada sin escrituras ajenas pendientes; valida cuentas distintas y cantidad entera positiva, debita solo si saldo suficiente, comprueba filas afectadas, acredita destino y confirma solo tras ambas; rollback si destino ausente o cualquier fallo. ACID significa atomicidad, consistencia de invariantes, reglas de visibilidad de aislamiento y durabilidad según garantías de almacenamiento. Comprueba saldos tras éxito/fallo y desde conexión separada tras commit. Índices cuestan almacenamiento/escrituras; inspecciona planes y mide antes de afirmar mejora.

**Explicación:** Atomicidad evita débito parcial; base en memoria no es durable tras salida del proceso. Aislamiento depende del motor.

**Intención del entrevistador:** Evaluar garantías de integridad, pruebas de fallo y optimización medida.

**Errores comunes**

- Confirmar débito antes de crédito o suponer que todo índice ayuda.

**Preguntas de seguimiento**

- ¿Por qué observar saldo nuevo en conexión escritora no basta para probar commit?

**Ejemplo**

Saldos 10 y 2 pasan a 7 y 5 tras transferir 3; transferencia posterior fallida a destino inexistente deja ambos intactos.

**Rúbrica de autoevaluación**

- 1 — Diseña propiedad atómica, updates condicionales y comprobaciones entre conexiones/de fallo.
- 1 — Explica cuatro propiedades ACID y propone medir beneficio del índice frente a coste.

Máximo: 2

</details>

**Requisitos previos**

- [Transacciones e integridad](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.es.md)
- [Índices y plan de consulta](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.es.md)

## Ingeniería de software

### engineering.sdd-tdd

`junior` · `software-engineering`

Distingue SDD de TDD para función que cuenta lecciones completadas únicas. ¿Qué evidencia se necesita antes de afirmar Red y Green?

<details>
<summary>Respuesta esperada</summary>

SDD define requisito, plan, tareas y criterios de aceptación observables. TDD escribe prueba de comportamiento, observa fallo por razón prevista, implementa y observa pruebas pasando antes de refactorizar. Registra resultados reales; solo escribir prueba no establece Red.

**Explicación:** Especificaciones definen qué entregar; pruebas aportan evidencia de ejecución de comportamiento.

**Intención del entrevistador:** Evaluar disciplina de desarrollo y honestidad de evidencia.

**Errores comunes**

- Afirmar Red porque archivo de prueba se confirmó primero.

**Preguntas de seguimiento**

- ¿Qué caso de aceptación rechazaría conteo duplicado?

**Ejemplo**

Entrada [1,2,2] tiene conteo esperado 2; ejecuta prueba antes y después de implementar.

**Rúbrica de autoevaluación**

- 1 — Distingue artefactos de especificación del ciclo TDD.
- 1 — Exige evidencia observada de fallo/éxito antes de afirmar Red/Green.

Máximo: 2

</details>

**Requisitos previos**

- [Decisiones empiezan en el requisito](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.es.md)

### engineering.dependency-boundary

`mid` · `software-engineering`

Regla de informe de progreso abre base directamente. Rediseña frontera para pruebas unitarias sin almacenamiento; explica integración y cómo registrar decisión en ADR.

<details>
<summary>Respuesta esperada</summary>

Inyecta callable loader que devuelve IDs completados para alumno; conserva conteo de IDs únicos y validación en regla. Usa doble para duplicados, vacío, IDs inválidos y fallo de dependencia propagado. Integración verifica consulta/mapeo real aparte. Registra contexto, alternativas (consulta directa vs loader inyectado), decisión, consecuencias y criterios de aceptación.

**Explicación:** Inyección aísla pruebas de política pero no verifica frontera real; abstracción añade indirección.

**Intención del entrevistador:** Evaluar mantenibilidad, fronteras de prueba y decisiones documentadas.

**Errores comunes**

- Sustituir toda prueba de integración por pruebas de loader doble.

**Preguntas de seguimiento**

- ¿Cuándo código directo sería más simple que nueva abstracción?

**Ejemplo**

progress_report("learner-a", lambda _: [1,2,2]) debe devolver {"completed":2}.

**Rúbrica de autoevaluación**

- 1 — Propone loader sustituible y distingue responsabilidades unitaria/integración.
- 1 — Registra contexto, alternativas, decisión y consecuencias incluida evidencia de prueba.

Máximo: 2

</details>

**Requisitos previos**

- [Decisiones empiezan en el requisito](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.es.md)
- [Compromisos y operación](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.es.md)

### engineering.architecture-tradeoffs

`senior` · `software-engineering`

Servicio pequeño de informes tiene solicitudes lentas. Un colega propone dividir en servicios y añadir caché. ¿Cómo decidirías, medirías y desplegarías cambios de forma segura?

<details>
<summary>Respuesta esperada</summary>

Define metas de latencia/fiabilidad y mide base con logs, métricas y trazas para localizar cuello de botella. Compara monolito modular y servicios por escala/deploy independientes y coste de red/operación. Considera caché solo con restricciones explícitas de desfase, invalidación y memoria. Registra alternativas y consecuencias en ADR, prueba criterios de aceptación, usa cambios enfocados revisados y planifica despliegue medido y rollback, incluida compatibilidad de datos.

**Explicación:** Etiquetas de arquitectura no establecen rendimiento. Evidencias y restricciones de calidad determinan si complejidad adicional se justifica.

**Intención del entrevistador:** Evaluar juicio técnico, decisiones medibles y riesgo operacional.

**Errores comunes**

- Suponer microservicios o cachés mejoran latencia automáticamente.
- Ignorar desfase de caché o suponer rollback de código revierte migraciones.

**Preguntas de seguimiento**

- ¿Qué evidencia justificaría conservar diseño actual?

**Ejemplo**

Si mediciones localizan lecturas costosas repetidas y contrato permite desfase limitado, evalúa caché pequeña contra base; recházala si invalidación o coste de memoria supera presupuesto acordado.

**Rúbrica de autoevaluación**

- 1 — Define base medible e investiga cuello de botella antes de elegir.
- 1 — Compara compromisos de servicios y caché frente a restricciones.
- 1 — Propone decisión documentada, pruebas de aceptación y rollback incluyendo datos.

Máximo: 3

</details>

**Requisitos previos**

- [Compromisos y operación](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.es.md)
- [Decisiones empiezan en el requisito](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.es.md)

## Entrevistas conductuales e internacionales

### behavioral.star-evidence

`junior` · `behavioral-international`

Describe un error o reto de aprendizaje con STAR. Usa ejemplo veraz no confidencial (estudio o proyecto personal es válido), o identifica explícitamente ensayo ficticio. Distingue tu acción, resultado observable, aprendizaje y limitación.

<details>
<summary>Respuesta esperada</summary>

Indica situación breve, tarea bajo tu responsabilidad, acciones específicas realizadas y resultado observable más aprendizaje. Describe limitación con honestidad; no inventes métricas, atribuyas trabajo ajeno a ti ni expongas material confidencial.

**Explicación:** STAR organiza evidencias sin exigir experiencia profesional ni impacto numérico.

**Intención del entrevistador:** Evaluar responsabilidad, evidencia concreta y aprendizaje.

**Errores comunes**

- Presentar éxito ficticio como empleo real o atribuir resultados colectivos a trabajo individual.

**Preguntas de seguimiento**

- ¿Qué mejorarías después y cómo lo verificarías?

**Ejemplo**

Ensayo ficticio: script de estudio contaba IDs duplicados (S); era responsable de regla (T); aclaré requisito, escribí prueba de regresión y corregí regla (A); prueba pasó, integración con base quedó sin verificar (R). Aprendí a distinguir evidencia unitaria de integración.

**Rúbrica de autoevaluación**

- 1 — Presenta situación, tarea y acción personal concreta, identificando material ficticio.
- 1 — Declara resultado observable, aprendizaje y limitación sin afirmaciones sin respaldo ni datos confidenciales.

Máximo: 2

</details>

**Requisitos previos**

- [Evidencias conductuales con STAR](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.es.md)

### behavioral.international-clarification

`mid` · `behavioral-international`

En entrevista en inglés, requisito cambia de devolver primera aparición del objetivo (o -1) a primera posición de inserción en lista ordenada. Da aclaración breve en inglés, ejemplo discriminante y actualización honesta con prueba que añadirías.

<details>
<summary>Respuesta esperada</summary>

Reconoce cambio de contrato, aclara si iguales se insertan antes del primero igual y reformula requisito. Para [2,4,7], objetivo 5, resultado antiguo -1 e índice de inserción 2. Propón prueba de ese caso y duplicados; distingue pruebas previstas de ejecutadas. Usa inglés comprensible, no jerga memorizada.

**Explicación:** Ejemplo concreto hace observable contrato cambiado; calidad comunicativa es comprensión compartida, no acento.

**Intención del entrevistador:** Evaluar aclaración, inglés técnico y respuesta a comentarios.

**Errores comunes**

- Seguir implementando contrato antiguo o afirmar que pruebas no ejecutadas pasaron.

**Preguntas de seguimiento**

- ¿Cómo pedirías al entrevistador repetir frase desconocida?

**Ejemplo**

Ensayo en inglés: "Let me restate the requirement. Should the insertion position be before equal values? For [2,4,7] and 5, I expect index 2. I would add this test; I have not run it yet."

**Rúbrica de autoevaluación**

- 1 — Usa inglés comprensible para aclarar y reformular contrato cambiado.
- 1 — Da ejemplo discriminante y actualización honesta de prueba/estado.

Máximo: 2

</details>

**Requisitos previos**

- [Entrevistas internacionales e inglés técnico](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.es.md)
- [2. Búsqueda binaria](../../problem-solving-and-live-coding/05-searching-algorithms/README.es.md)

### behavioral.evidence-disagreement

`senior` · `behavioral-international`

Compañero prefiere dividir servicio lento de informes; prefieres investigar caché. En este escenario ficticio, explica cómo resolverías desacuerdo usando objetivo compartido, evidencias, compromisos, decisión documentada y comunicación de riesgos. Distingue trabajo propuesto de resultados reales.

<details>
<summary>Respuesta esperada</summary>

Acuerda objetivo de latencia/fiabilidad e investiga evidencias de base antes de elegir. Escucha restricciones del compañero; compara desfase, invalidación y memoria de caché con despliegue/escala independientes y coste de red. Acuerda experimento pequeño y registro de decisión con criterios, riesgos y rollback. Declara tu función y decisión del equipo por separado; sin resultados, informa experimento como previsto, no ganancia verificada.

**Explicación:** Objetivo es decisión fundamentada y seguimiento colaborativo, no ganar discusión.

**Intención del entrevistador:** Evaluar liderazgo técnico, responsabilidad y comunicación transparente de riesgos.

**Errores comunes**

- Desestimar compañero o inventar mejoras antes de medición.

**Preguntas de seguimiento**

- Si equipo elige otra opción, ¿cómo apoyarías y vigilarías plan acordado?

**Ejemplo**

Plan ficticio: mide costes de lecturas repetidas, acuerda desfase aceptable, prueba caché limitada frente a base y documenta cuándo rechazarla. No se afirma mejora hasta medir.

**Rúbrica de autoevaluación**

- 1 — Declara objetivo común, escucha alternativas y compara compromisos medibles.
- 1 — Propone experimento/decisión documentado con criterios, riesgo y rollback, distinguiendo roles individual/equipo y resultados previstos/verificados.

Máximo: 2

</details>

**Requisitos previos**

- [Desacuerdos, responsabilidad y compromisos](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.es.md)

<!-- interview-questions:end -->

<!-- chapter-navigation:bottom -->
[← Anterior](../21-software-engineering-and-technical-decisions/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../23-behavioral-and-international-interviews/README.es.md)
<!-- /chapter-navigation:bottom -->
