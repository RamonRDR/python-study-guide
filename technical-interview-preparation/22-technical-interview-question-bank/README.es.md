# Banco de preguntas de entrevistas técnicas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../21-software-engineering-and-technical-decisions/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:top -->

Nueve preguntas piloto: tres Junior, tres Mid-level y tres Senior. Nivel indica profundidad esperada, no estándar universal de contratación. Estudia primero la sección de requisito previo, responde en voz alta sin revelar referencia y luego abre respuesta. Asigna a cada criterio sus puntos solo si tu respuesta lo demuestra; si no, cero. Usa puntuación para identificar carencias, no como certificación ni evaluación semántica automática. Preguntas de seguimiento son práctica opcional, sin puntuación separada. Registros JSON canónicos e índice en [interviews](../../interviews/README.es.md); esta sección se genera a partir de ellos. Banco técnico completo y simulaciones previstos.

## Preguntas piloto

<!-- interview-questions:start -->
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

<!-- interview-questions:end -->

<!-- chapter-navigation:bottom -->
[← Anterior](../21-software-engineering-and-technical-decisions/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:bottom -->
