<div align="center">

# Diseñando Pipelines de Logging y Contratos de Contexto en Runtime

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Biblioteca Estándar](../README.es.md) · [← Capítulo anterior: CSV](../04-csv/README.es.md)

El capítulo anterior sobre logging en la Fase 6 presentó el propósito del logging, los niveles estándar, los loggers de módulo, la configuración bajo responsabilidad de la aplicación, handlers, formatters, propagación, logging de excepciones, privacidad y la diferencia entre logs y comentarios.

Este capítulo profundiza. El foco deja de ser solamente **¿qué mensaje debería registrar?** y pasa a incluir:

```text
¿Cómo recorre un LogRecord el grafo de logging,
qué componente puede modificarlo
y qué contrato de runtime promete la aplicación?
```

El paquete `logging` es flexible porque separa creación de eventos, filtrado, enrutamiento, formateo y salida. Esa flexibilidad solo resulta útil cuando la configuración se trata como un diseño explícito del sistema y no como una colección de llamadas dispersas a `basicConfig()`.

**Tiempo estimado de estudio:** 150–190 minutos.

**Requisito de Python:** Python 3.10 o posterior para el contenido central y los ejemplos ejecutables. Las secciones específicas de versión identifican recursos añadidos en Python 3.12, 3.13 y 3.14.

**Base de documentación:** los comportamientos y notas de versión fueron verificados con la documentación oficial de Python 3.14 para `logging`, `logging.config`, `logging.handlers`, Logging HOWTO y Logging Cookbook.

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- modelar logging como un pipeline que transporta objetos `LogRecord`;
- distinguir umbrales de logger, niveles efectivos, umbrales de handler, filtros y propagación;
- explicar por qué los niveles de loggers ancestros no se vuelven a aplicar durante la propagación;
- diagnosticar registros duplicados o inesperadamente ausentes;
- usar `basicConfig(force=True)` de forma deliberada al reemplazar una configuración existente del root;
- diseñar diccionarios explícitos de `dictConfig()` sin deshabilitar loggers preexistentes por accidente;
- explicar qué puede y qué no puede cambiar una configuración incremental;
- distinguir el estilo del formatter de la interpolación del mensaje en la llamada de logging;
- agregar campos contextuales sin colisionar con atributos integrados de `LogRecord`;
- elegir entre `extra`, `LoggerAdapter`, filters, `contextvars` y una record factory;
- preservar la atribución del llamador a través de helpers de logging con `stacklevel`;
- distinguir `exc_info` de `stack_info`;
- evitar trabajo costoso para niveles de logging deshabilitados;
- comprender la política de error de los handlers y `logging.raiseExceptions`;
- mover trabajo lento de handlers detrás de `QueueHandler` y `QueueListener` cuando corresponda;
- razonar sobre threads, procesos, rotación de archivos y diseños de escritor único;
- reconocer patrones inseguros de configuración dinámica de logging;
- probar el comportamiento de logging como contrato de aplicación y no como texto incidental.

## 1. Qué añade este capítulo después de la Fase 6

La Fase 6 enseñó la interfaz cotidiana:

```python
import logging


logger = logging.getLogger(__name__)
logger.info("Processed %s records", record_count)
```

Eso sigue siendo correcto. Este capítulo estudia lo que ocurre alrededor de esa llamada:

```text
call site
   ↓
logger eligibility
   ↓
LogRecord creation
   ↓
logger filters
   ↓
handlers on this logger
   ↓
propagation to ancestor handlers
   ↓
handler levels and filters
   ↓
formatter
   ↓
destination
```

Los detalles importan cuando una aplicación real tiene varios paquetes, bibliotecas de terceros, múltiples destinos, trabajo asíncrono, worker threads, verbosidad dinámica o contexto estructurado.

## 2. Un evento de logging se convierte en un `LogRecord`

Cuando un logger acepta un evento, Python representa ese evento como un `LogRecord`.

El registro transporta información como:

- nombre del logger;
- nivel numérico y textual;
- template del mensaje y argumentos;
- pathname de origen, nombre de función y número de línea;
- información de proceso y thread;
- información opcional de excepción o stack;
- atributos personalizados proporcionados por mecanismos controlados de contexto.

Formatters y handlers consumen ese registro después.

Un modelo mental útil es:

```text
logging call = event request
LogRecord    = event data object
handler      = delivery policy
formatter    = output representation
```

No trates la línea de texto ya renderizada como si fuera todo el sistema de logging. El registro existe antes de la representación final.

## 3. Los nombres de logger forman una jerarquía

Los nombres de logger usan una jerarquía separada por puntos:

```python
import logging


root = logging.getLogger()
service = logging.getLogger("app.service")
worker = logging.getLogger("app.service.worker")
```

`app.service.worker` es descendiente de `app.service`, que es descendiente de `app`, que finalmente llega al root logger.

Por eso `logging.getLogger(__name__)` encaja naturalmente con los paquetes Python. Un módulo como:

```text
catalog.importer.csv_reader
```

puede participar en la jerarquía:

```text
catalog
catalog.importer
catalog.importer.csv_reader
```

La jerarquía es un namespace de enrutamiento. No significa que los objetos logger deban pasarse como dependencias. Llamadas repetidas a `getLogger()` con el mismo nombre devuelven el mismo objeto logger.

## 4. `NOTSET` significa herencia en loggers no root

Los nuevos loggers que no son root normalmente comienzan en `NOTSET`.

Para un logger no root, `NOTSET` no significa "no registres nada". Significa que Python sube por la jerarquía hasta encontrar un ancestro con un nivel explícito o llegar al root.

```python
import logging


root = logging.getLogger()
root.setLevel(logging.WARNING)

logger = logging.getLogger("app.worker")
logger.setLevel(logging.NOTSET)

print(logger.getEffectiveLevel() == logging.WARNING)
```

El root logger comienza en `WARNING`, salvo que la configuración lo cambie.

Esta distinción explica muchos errores del tipo "¿por qué desapareció mi registro INFO?".

## 5. La elegibilidad del logger ocurre antes de la entrega

Primero el logger decide si el evento está habilitado.

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug("Cache snapshot size=%s", cache_size)
```

`isEnabledFor()` considera:

1. el override global establecido por `logging.disable()`;
2. el nivel efectivo del logger.

Si el evento no supera esta etapa, no se crea un `LogRecord` normal para entregarlo a los handlers.

Eso es diferente de que un handler rechace el registro más tarde.

## 6. Los niveles de handler son un segundo umbral

Un logger puede aceptar un registro mientras un handler concreto lo rechaza.

```python
import logging


logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
```

Aquí:

```text
DEBUG event
  logger accepts it
  handler rejects it

WARNING event
  logger accepts it
  handler accepts it
```

Este modelo de dos etapas permite diseños como:

```text
logger: DEBUG
console handler: INFO
file handler: DEBUG
alert handler: ERROR
```

El logger controla si el evento entra en el pipeline de entrega. Cada handler controla si ese destino recibe el evento.

## 7. La propagación no vuelve a comprobar los niveles de los loggers ancestros

Este detalle es fácil de perder.

Cuando un registro se propaga desde un logger hijo, Python lo ofrece directamente a los handlers asociados a loggers ancestros. Los niveles y filtros de esos **objetos logger ancestros** no se vuelven a aplicar durante la propagación.

Los handlers siguen aplicando sus propios niveles y filtros.

Conceptualmente:

```text
app.worker logger accepts INFO
        ↓
record created
        ↓
app.worker handlers
        ↓ propagate=True
app handlers receive record directly
        ↓
root handlers receive record directly
```

No supongas que poner el logger ancestro en `ERROR` filtrará registros ya aceptados por descendientes y propagados a sus handlers. Coloca los umbrales de destino en los handlers cuando esa sea la política necesaria.

## 8. Los registros duplicados suelen ser un problema del grafo

Considera esta configuración:

```python
import logging


handler = logging.StreamHandler()

root = logging.getLogger()
root.addHandler(handler)

child = logging.getLogger("app.worker")
child.addHandler(handler)
child.propagate = True
```

Un registro emitido por `app.worker` puede llegar al mismo handler a través del hijo y otra vez por la ruta del ancestro.

Un buen patrón inicial es:

```text
application entry point configures shared handlers high in the hierarchy
modules create loggers
modules do not attach duplicate visible handlers
propagation remains enabled unless isolation is intentional
```

Definir `propagate = False` puede resolver una frontera deliberada de enrutamiento, pero no es un botón universal para eliminar duplicados. Un logger con propagación desactivada también deja de llegar a handlers ancestros.

## 9. `hasHandlers()` sigue las fronteras de propagación

`logger.hasHandlers()` comprueba el logger y recorre los ancestros.

La búsqueda se detiene al encontrar un logger cuyo `propagate` sea `False`.

```python
import logging


logger = logging.getLogger("app.worker")
print(isinstance(logger.hasHandlers(), bool))
```

Este método responde si la jerarquía puede encontrar un handler por su ruta actual de propagación. No promete que cada registro será emitido, porque niveles y filtros todavía pueden rechazarlo.

## 10. `basicConfig()` es simple a propósito

`basicConfig()` es útil para aplicaciones pequeñas y herramientas CLI, pero configura el root logger y tiene un comportamiento de ciclo de vida importante.

Por defecto, si el root logger ya tiene handlers, otra llamada a `basicConfig()` no hace nada.

```python
import logging


logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

print(logging.getLogger().level == logging.WARNING)
```

Eso puede sorprender en notebooks, procesos de prueba, hosts de plugins o aplicaciones cuyas dependencias ya tocaron logging.

## 11. `force=True` reemplaza handlers existentes del root

Desde Python 3.8, `basicConfig(force=True)` elimina y cierra handlers existentes del root antes de aplicar la nueva configuración básica.

```python
import logging


logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.INFO, force=True)

print(logging.getLogger().level == logging.INFO)
```

Usa `force=True` cuando la aplicación controla deliberadamente la configuración global del proceso y pretende reemplazarla.

No lo uses casualmente dentro de bibliotecas reutilizables. Puede borrar configuración instalada por la aplicación anfitriona.

## 12. `dictConfig()` hace explícito el grafo de objetos

Para aplicaciones mayores, `logging.config.dictConfig()` puede describir formatters, filters, handlers, loggers y root logger en un único objeto de configuración.

Un diccionario de configuración requiere `version`, y la versión de schema soportada actualmente es `1`.

```python
import logging.config


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "brief": {
            "format": "%(levelname)s:%(name)s:%(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "brief",
            "level": "INFO",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}

logging.config.dictConfig(config)
```

El beneficio no es que los diccionarios sean mágicos. El beneficio es que el grafo de logging se convierte en configuración inspeccionable en lugar de mutaciones dispersas por el código.

## 13. Sé explícito con `disable_existing_loggers`

Una omisión peligrosa en `dictConfig()` es olvidar esta clave:

```python
"disable_existing_loggers": False,
```

Si la clave no existe, los loggers no root ya existentes se tratan como deshabilitados salvo que ellos o un ancestro estén nombrados explícitamente según las reglas de configuración.

En una aplicación que importa bibliotecas antes de configurar logging, el valor histórico predeterminado `True` puede silenciar loggers que ya existen.

Guía del proyecto:

```text
If preserving pre-existing library loggers is intended,
write disable_existing_loggers=False explicitly.
```

No dependas de que alguien recuerde ese valor histórico.

## 14. La configuración incremental es deliberadamente limitada

`dictConfig()` admite:

```python
incremental_config = {
    "version": 1,
    "incremental": True,
    "handlers": {
        "console": {"level": "WARNING"},
    },
    "root": {
        "level": "WARNING",
    },
}
```

Pero el modo incremental **no** reconstruye todo el grafo de objetos de logging.

Cuando `incremental` es verdadero, Python ignora las entradas de `formatters` y `filters`. Procesa `level` de handlers y `level` más `propagate` de loggers/root.

Usa configuración incremental para cambios controlados de verbosidad, no como mecanismo general de hot reload para topologías arbitrarias de handlers y formatters.

## 15. El estilo del formatter y la interpolación del mensaje son contratos diferentes

Un `Formatter` puede usar estilo `%`, `{` o `$` para el **formato de salida**:

```python
import logging


formatter = logging.Formatter(
    "{levelname}:{name}:{message}",
    style="{",
)
```

Eso no cambia el contrato normal de interpolación de las llamadas del logger:

```python
logger.info("Processed %s records", record_count)
```

El template del mensaje y sus argumentos siguen usando la mezcla `%` normal del paquete logging.

No deduzcas que esto:

```python
logger.info("Processed {} records", record_count)
```

funciona solo porque el `Formatter(style="{")` del handler usa llaves. Son capas distintas.

## 16. `Formatter(validate=True)` detecta estilos incompatibles

La validación del formatter está activada por defecto.

```python
import logging


try:
    logging.Formatter("%(levelname)s:%(message)s", style="{")
except ValueError:
    print("format and style do not match")
```

La validación detecta un error de configuración pronto, en lugar de esperar a que un evento posterior revele el problema.

## 17. `Formatter(defaults=...)` puede definir campos fallback seguros

Python 3.10 añadió el argumento `defaults` a `Formatter`.

```python
import logging


formatter = logging.Formatter(
    "%(request_id)s:%(message)s",
    defaults={"request_id": "-"},
)
```

Sin fallback, un formatter que requiere un campo personalizado puede fallar al recibir registros que no lo contienen.

Los defaults son útiles cuando un handler recibe registros contextualizados y registros comunes. No sustituyen la definición de un schema coherente cuando sistemas consumidores exigen campos estructurados.

## 18. `extra` enriquece el `LogRecord`

Puedes agregar atributos personalizados a un registro:

```python
logger.info(
    "Job started",
    extra={"job_id": "job-104", "component": "importer"},
)
```

Un formatter puede referirse después a esos campos:

```python
logging.Formatter(
    "%(levelname)s:%(job_id)s:%(component)s:%(message)s"
)
```

Las claves proporcionadas mediante `extra` se insertan en el diccionario de atributos del registro.

## 19. Los campos personalizados no deben colisionar con atributos integrados del registro

Este diseño es inválido:

```python
logger.info(
    "Job started",
    extra={"levelname": "CUSTOM"},
)
```

Nombres integrados como `levelname`, `name`, `message`, `pathname` y muchos otros pertenecen a `LogRecord`.

Elige un namespace de aplicación claro y estable:

```text
request_id
job_id
component
tenant_code
operation
```

No agregues secretos o datos personales innecesarios solamente porque `extra` lo hace fácil.

## 20. `LoggerAdapter` transporta contexto repetido

Cuando varios registros comparten los mismos valores contextuales, un adapter reduce repetición:

```python
import logging


logger = logging.getLogger("app.worker")
worker_logger = logging.LoggerAdapter(
    logger,
    {"job_id": "job-104"},
)

worker_logger.info("Started")
worker_logger.info("Validated input")
```

El adapter delega en un logger subyacente mientras inserta contexto.

Esto es útil para ámbitos como un job, request, conexión u operación.

## 21. Python 3.13 añadió `LoggerAdapter(merge_extra=True)`

Históricamente, el `extra` del propio adapter prevalecía y un `extra` pasado en una llamada individual no era mezclado por la implementación estándar del adapter.

Python 3.13 añadió `merge_extra`:

```python
import logging


base_logger = logging.getLogger("app.worker")
adapter = logging.LoggerAdapter(
    base_logger,
    {"job_id": "job-104"},
    merge_extra=True,
)

adapter.info(
    "Batch complete",
    extra={"batch_id": "batch-7"},
)
```

Si tu biblioteca o aplicación soporta versiones anteriores de Python, no publiques configuración que asuma silenciosamente este comportamiento de 3.13.

## 22. Los filters hacen más que responder sí o no

Un logger o handler puede tener filtros.

Un filtro tradicional devuelve un valor verdadero para conservar un registro o falso para rechazarlo:

```python
import logging


class IgnoreHealthChecks(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return getattr(record, "route", None) != "/health"
```

Los filters son útiles cuando los umbrales de nivel no pueden expresar la política.

Ejemplos:

- descartar una categoría demasiado ruidosa;
- permitir un subárbol concreto de loggers;
- inyectar contexto controlado;
- contar registros que atraviesan un destino determinado.

## 23. Los filters en Python 3.12 pueden devolver un `LogRecord` de reemplazo

Desde Python 3.12, un filter puede devolver una instancia de `LogRecord` para reemplazar el registro original en el procesamiento posterior de esa ruta.

Esto es especialmente útil en un handler cuando quieres enriquecimiento específico del destino sin mutar el registro visto por otros handlers.

```python
import copy
import logging


def add_destination(record: logging.LogRecord):
    cloned = copy.copy(record)
    cloned.destination = "console"
    return cloned
```

Poder reemplazar en lugar de mutar un registro compartido reduce efectos secundarios entre múltiples handlers.

Documenta el requisito de Python 3.12 si dependes de este comportamiento.

## 24. Una factory de `LogRecord` puede agregar contexto global del proceso

Python expone la factory actual de registros:

```python
import logging


old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.application = "study-guide"
    return record


logging.setLogRecordFactory(record_factory)
```

Una factory afecta globalmente la creación de registros dentro del proceso.

Ese poder requiere cautela. Encadenar factories añade overhead, y bibliotecas independientes pueden colisionar si eligen los mismos nombres de atributos personalizados.

Prefiere un filter o adapter cuando el contexto pertenece solamente a un destino o ámbito.

## 25. Elige el mecanismo de contexto más estrecho que resuelva el problema

Una tabla práctica:

| Necesidad | Prefiere |
|---|---|
| Una llamada tiene campos extra | `extra={...}` |
| Muchas llamadas de una operación comparten campos | `LoggerAdapter` |
| Un handler necesita enriquecimiento específico del destino | filter en handler |
| Contexto de request/task debe fluir en código async/thread-aware | `contextvars` + adapter/filter |
| Cada registro creado necesita un atributo global del proceso | factory de `LogRecord`, con cuidado |

El mecanismo más global no es automáticamente el más conveniente.

## 26. `contextvars` puede transportar contexto de request o task

`contextvars.ContextVar` es útil cuando datos contextuales deben seguir la ejecución lógica sin pasar manualmente un logger por cada función.

```python
import contextvars
import logging


request_id_var = contextvars.ContextVar("request_id", default="-")


class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get()
        return True
```

Un handler que use ese filtro puede formatear `%(request_id)s`.

Este patrón puede funcionar entre threads y tareas asíncronas cuando el contexto se gestiona correctamente. También mantiene los nombres de logger vinculados a áreas del código, en vez de crear un logger nuevo por request.

## 27. No crees un logger por request, archivo o cliente

Las instancias de logger se almacenan en caché por nombre y no se liberan durante la ejecución normal del script.

Este patrón crea namespaces de logger sin límite:

```python
logger = logging.getLogger(f"request.{request_id}")
```

Prefiere un logger estable:

```python
logger = logging.getLogger("app.request")
logger.info("Request started", extra={"request_id": request_id})
```

Los nombres de logger suelen identificar áreas de software. Los campos de contexto identifican entidades individuales de runtime.

## 28. `stacklevel` preserva el llamador real a través de helpers

Sin cuidado, un wrapper de logging puede hacer que todos los registros parezcan originarse en el propio helper.

```python
import logging


logger = logging.getLogger("app")


def log_notice(message: str) -> None:
    logger.info(message, stacklevel=2)
```

El llamador:

```python
def run_job() -> None:
    log_notice("Job started")
```

puede entonces aparecer como origen en lugar de `log_notice()`.

Esto es valioso cuando helpers estandarizan la forma del evento, pero la atribución de origen todavía debe apuntar al call site de la aplicación.

## 29. `exc_info` y `stack_info` responden preguntas diferentes

`exc_info` captura información del traceback de la excepción.

```python
try:
    int("not-a-number")
except ValueError:
    logger.error("Parsing failed", exc_info=True)
```

`stack_info=True` captura la stack actual que llevó a la llamada de logging, incluso sin excepción:

```python
logger.debug("Reached diagnostic checkpoint", stack_info=True)
```

Piénsalo así:

```text
exc_info   → which frames were unwound by this exception?
stack_info → how did execution reach this logging call?
```

Pueden usarse de forma independiente.

## 30. Evita registrar la misma excepción en cada capa

Una capa inferior puede registrar y relanzar:

```python
try:
    load_document()
except OSError:
    logger.exception("Document load failed")
    raise
```

Si cada llamador repite el mismo patrón, un fallo se convierte en varios tracebacks casi idénticos.

Elige una frontera que sea responsable del registro operativo. Otras capas solo deben agregar información cuando realmente aportan contexto nuevo o cambian la decisión de manejo.

Registrar una excepción y manejarla son responsabilidades separadas.

## 31. El formateo diferido no difiere el cálculo de argumentos costosos

Esto usa parametrización:

```python
logger.debug("Graph summary=%s", build_graph_summary())
```

pero `build_graph_summary()` todavía se ejecuta antes de llamar a `logger.debug()`.

Protege diagnósticos caros:

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug("Graph summary=%s", build_graph_summary())
```

Úsalo cuando preparar los argumentos sea realmente costoso. No envuelvas cada variable trivial en un `isEnabledFor()`.

## 32. `logging.disable()` es un override global del proceso

`logging.disable(level)` deshabilita todas las llamadas de logging de esa severidad o inferior, independientemente de los niveles individuales de los loggers.

```python
import logging


logging.disable(logging.INFO)
# DEBUG and INFO calls are disabled process-wide.

logging.disable(logging.NOTSET)
# Remove the override.
```

Esto es diferente de cambiar el nivel efectivo de un logger.

Usa la supresión global con cuidado porque también afecta jerarquías de logger no relacionadas.

## 33. `lastResort` explica warnings inesperados sin configuración

Si no se puede encontrar ningún handler, Python proporciona `logging.lastResort`.

Es un `StreamHandler` en `WARNING` que escribe el mensaje sin formato en `sys.stderr`.

Esto explica por qué una biblioteca reutilizable aún puede parecer imprimir warnings aunque la aplicación anfitriona no haya configurado logging.

Una biblioteca que intencionalmente quiera silencio en esa situación puede asociar `logging.NullHandler()` a su logger superior, pero debe seguir dejando la configuración de destinos visibles a la aplicación.

## 34. Los fallos de handler tienen su propia política de error

Pueden ocurrir errores mientras se emite un registro: un stream puede fallar, un formatter puede ser incorrecto, un destino de red puede no estar disponible o un handler personalizado puede lanzar una excepción.

`logging.raiseExceptions` es consultado por `Handler.handleError()` cuando un handler ha capturado una excepción durante la emisión y envía explícitamente ese fallo por la ruta estándar de error de handlers:

```python
logging.raiseExceptions
```

Su valor predeterminado es `True`, útil durante el desarrollo porque `handleError()` puede hacer visibles los fallos de logging en `sys.stderr`. Establecerlo en `False` es común en producción cuando los diagnósticos de esa ruta de error deben permanecer silenciosos.

Esta flag **no es un escudo global contra cualquier excepción de handler**. Si una implementación personalizada o de terceros de `emit()` deja escapar una excepción, en lugar de capturarla y llamar a `handleError()`, `logging.raiseExceptions = False` no impide que esa excepción se propague de vuelta a la llamada de logging.

No confundas la flag con suprimir excepciones de la aplicación. Controla los diagnósticos producidos por la ruta estándar de `handleError()`; los handlers personalizados robustos todavía necesitan una política explícita de fallo.

## 35. Implementaciones personalizadas de `emit()` deben respetar los locks

Los handlers usan locks durante la emisión.

Un `Handler.emit()` personalizado que llama APIs de configuración de logging u otras operaciones de logging que adquieren locks puede crear problemas de orden de bloqueo con otra thread configurando logging.

Mantén las implementaciones personalizadas de `emit()` enfocadas en la entrega. Evita reentrar en la maquinaria de configuración desde la emisión del handler.

Si un destino tiene comportamiento bloqueante complejo, una frontera por cola puede ser un diseño mejor.

## 36. Logging es thread-safe, pero handlers lentos todavía bloquean al llamador

El módulo estándar de logging usa locks para que múltiples threads compartan infraestructura de logging con seguridad dentro de un proceso.

Thread safety no significa latencia cero.

Un handler que realiza disco lento, red, SMTP u otro I/O bloqueante puede mantener ocupada la thread llamadora mientras emite el registro.

Para rutas sensibles a latencia, desacopla la creación del evento de la entrega lenta.

## 37. `QueueHandler` mueve registros a una cola

`logging.handlers.QueueHandler` envía registros a una cola:

```python
import logging
import queue
from logging.handlers import QueueHandler


log_queue = queue.Queue()
queue_handler = QueueHandler(log_queue)

logger = logging.getLogger("app")
logger.addHandler(queue_handler)
```

El llamador encola en lugar de realizar directamente el trabajo lento del destino.

Una cola limitada puede llenarse. `QueueHandler` usa enqueue no bloqueante por defecto, y los fallos siguen la política de error de handlers.

La capacidad de la cola y la política de descarte/bloqueo son decisiones operativas, no detalles para ignorar.

## 38. `QueueListener` ejecuta el trabajo de handlers en otra thread

Un listener consume registros encolados y los entrega a handlers reales:

```python
import logging
import queue
from logging.handlers import QueueHandler, QueueListener


log_queue = queue.Queue()
output_handler = logging.StreamHandler()
listener = QueueListener(
    log_queue,
    output_handler,
    respect_handler_level=True,
)

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(QueueHandler(log_queue))

listener.start()
try:
    logger.info("Job queued")
finally:
    listener.stop()
```

Con `respect_handler_level=True`, el listener comprueba el nivel de cada handler de destino antes de entregarle el registro.

Este patrón es útil en web services, sistemas de workers y aplicaciones asíncronas donde el I/O bloqueante del handler no debería ejecutarse en una ruta sensible a latencia.

## 39. Python 3.14 convirtió `QueueListener` en context manager

Python 3.14 permite:

```python
with QueueListener(log_queue, output_handler) as listener:
    logger.info("Job queued")
```

Entrar en el contexto inicia el listener. Salir lo detiene.

El ejemplo ejecutable de este repositorio usa `start()` / `stop()` explícitamente para seguir siendo compatible con Python 3.10+, mientras esta sección documenta la API más reciente.

## 40. `QueueHandler.prepare()` cambia lo que cruza la frontera de la cola

La implementación base de `QueueHandler.prepare()` formatea el registro para que pueda ser encolado y serializado con pickle en escenarios comunes.

Esa preparación fusiona mensaje y argumentos y elimina información como `args`, `exc_info` y `exc_text` que puede no ser serializable o causar problemas de formateo posterior.

Si el lado listener necesita formateo personalizado de excepciones u otro schema serializado, crea una subclase de `QueueHandler` y sobrescribe `prepare()` deliberadamente.

La frontera de la cola es un contrato de serialización. No supongas que el listener recibe una copia intacta de cada atributo original del registro.

## 41. Cuidado con `multiprocessing.Queue` y su logger interno

El módulo `multiprocessing` tiene un logger interno. Un `multiprocessing.Queue` puede emitir registros `DEBUG` mientras ocurren operaciones de cola.

Si esos registros internos pasan por un `QueueHandler` que usa la **misma** cola de multiprocessing, el sistema puede entrar en recursión o deadlock.

Al combinar multiprocessing y colas de logging, diseña la topología del listener deliberadamente y sigue el warning documentado de `QueueHandler` para multiprocessing.

## 42. Varios procesos no deberían escribir independientemente en el mismo file handler estándar

Logging es thread-safe dentro de un proceso, pero la biblioteca estándar no proporciona locking compartido entre procesos para un único `FileHandler` usado por procesos independientes.

Procesos distintos escribiendo el mismo archivo pueden mezclar salida o interferir con la rotación.

Una arquitectura más segura es:

```text
worker process ─┐
worker process ─┼─> queue/socket ─> single listener/writer ─> file
worker process ─┘
```

Centraliza la escritura real del archivo cuando múltiples procesos deban contribuir a un solo flujo de log.

## 43. Los rotating handlers son herramientas de retención, no coordinación multiprocess

La biblioteca estándar incluye:

- `RotatingFileHandler` para rollover basado en tamaño;
- `TimedRotatingFileHandler` para rollover basado en tiempo.

```python
from logging.handlers import RotatingFileHandler


handler = RotatingFileHandler(
    "application.log",
    maxBytes=1_000_000,
    backupCount=5,
    encoding="utf-8",
)
```

La rotación controla el crecimiento de archivos y la forma de retención. No hace seguros a escritores independientes de múltiples procesos.

También define quién controla retención externa, compresión, envío o borrado. Una configuración de rollover no es una política completa de retención de observabilidad.

## 44. Los timestamps forman parte del contrato de salida

Los formatters usan hora local por defecto para `asctime`.

Para sistemas que requieren una zona horaria consistente, un formatter puede usar conversión UTC:

```python
import logging
import time


formatter = logging.Formatter(
    "%(asctime)sZ %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
formatter.converter = time.gmtime
```

Sé explícito sobre la zona horaria cuando logs viajan entre máquinas o regiones.

En tests deterministas, evita afirmar el timestamp real actual salvo que el comportamiento temporal sea el contrato que se está probando.

## 45. Los campos de identidad de runtime dependen de la versión

`LogRecord` incluye campos de thread y proceso, y Python 3.12 añadió `taskName` para nombres de `asyncio.Task` cuando están disponibles.

Antes de agregar un campo a todos los formatters, comprueba las versiones soportadas de Python y si el valor es significativo para todos los modelos de ejecución.

Un formatter que exige ciegamente contexto opcional puede fallar. Usa un schema estable o defaults del formatter cuando corresponda.

## 46. `logging.captureWarnings()` puede enrutar `warnings` mediante logging

Python puede redirigir warnings emitidos por el módulo `warnings` hacia logging:

```python
import logging


logging.captureWarnings(True)
```

Esos registros usan el logger `py.warnings`.

Esto puede unificar destinos, pero también cambia cómo se enruta la salida de warnings. La aplicación debe controlar esa decisión.

No confundas `warnings.warn()` con `logger.warning()`: son APIs distintas y pueden tener consumidores y reglas de filtrado diferentes.

## 47. La configuración dinámica por socket tiene una frontera de seguridad

`logging.config.listen()` puede iniciar un servidor de socket local que recibe configuración de logging.

Esta capacidad es poderosa porque la configuración de logging puede referenciar o construir objetos Python. Configuración no confiable puede por tanto convertirse en riesgo de ejecución de código en entornos donde otro usuario o proceso local pueda enviar datos maliciosos.

Si se usa este mecanismo, estudia el callback `verify` y autentica o rechaza bytes de configuración no confiables.

No expongas configuración dinámica de logging solamente porque cambiar la verbosidad de forma remota parezca conveniente.

## 48. Las bibliotecas deben documentar nombres de logger, no apropiarse de los destinos

Una biblioteca reutilizable debería indicar bajo qué namespace de logger emite:

```text
examplelib
examplelib.client
examplelib.parser
```

Normalmente debería evitar:

- llamar `basicConfig()`;
- asociar handlers visibles de archivo, consola, correo o red;
- reemplazar handlers del root;
- deshabilitar globalmente otros loggers.

La aplicación anfitriona controla destinos y formato.

Esto mantiene la biblioteca componible dentro de herramientas CLI, aplicaciones web, notebooks, tests y plataformas mayores.

## 49. Los schemas de logging deberían ser suficientemente estables para operar

Incluso los logs de texto plano se benefician de nombres de campos intencionales:

```text
operation=import job_id=job-104 records=87
```

Contratos útiles definen:

- significado del evento;
- política de severidad;
- identificadores contextuales estables;
- clasificación de privacidad;
- política de timestamp y zona horaria;
- política de destino y retención;
- si consumidores automáticos dependen de nombres de campo.

No conviertas cada frase en una API pública permanente, pero tampoco hagas aleatorios los campos operacionalmente importantes.

## 50. La privacidad viene antes del formateo

Un formatter no puede rescatar un registro que ya contiene un secreto innecesario.

Evita insertar:

- contraseñas;
- API keys;
- headers de autorización;
- tokens de sesión;
- datos personales o de pago completos;
- objetos crudos de request o configuración que contengan secretos.

La redacción debe ser defensa en profundidad, no permiso para recopilar todo primero.

Mecanismos contextuales como `extra`, adapters, filters y record factories necesitan la misma revisión de privacidad.

## 51. Prueba contratos semánticos de logging

Los tests deben afirmar comportamiento importante.

Por ejemplo:

```python
import logging
import unittest


class ImportTests(unittest.TestCase):
    def test_fallback_logs_warning(self):
        logger = logging.getLogger("app.importer")

        with self.assertLogs(logger, level="WARNING") as captured:
            logger.warning("Using fallback parser")

        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].levelno, logging.WARNING)
```

Prefiere verificar el registro, severidad, nombre del logger o campos seguros obligatorios en lugar de congelar puntuación incidental del texto renderizado.

## 52. Restablece el estado de logging con cuidado en tests

La configuración de logging es lo suficientemente global al proceso como para que un test filtre handlers o niveles hacia otro.

Estrategias posibles:

- configurar una vez para el proceso de tests;
- crear loggers nombrados aislados y restaurar atributos modificados;
- eliminar handlers agregados por un test durante cleanup;
- usar `basicConfig(force=True)` solamente cuando el test controla intencionalmente el estado del root;
- evitar depender del orden de ejecución de los tests.

Una suite verde no debería necesitar una configuración de logger dejada por casualidad por un test anterior.

## 53. Ejemplo práctico: enrutar registros con `dictConfig()`

```python
import logging
import logging.config
import sys


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "brief": {
            "format": "%(levelname)s:%(name)s:%(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "brief",
            "level": "INFO",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "study.service": {
            "level": "INFO",
            "propagate": True,
        }
    },
    "root": {
        "level": "WARNING",
        "handlers": ["console"],
    },
}

logging.config.dictConfig(config)

service_logger = logging.getLogger("study.service")
dependency_logger = logging.getLogger("study.dependency")

service_logger.info("service started")
dependency_logger.info("hidden detail")
dependency_logger.warning("slow response")
```

Versión ejecutable: [`examples/dict_config_routing.py`](examples/dict_config_routing.py).

## 54. Ejemplo práctico: inyectar contexto de ámbito

```python
import contextvars
import logging
import sys


request_id_var = contextvars.ContextVar("request_id", default="-")


class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get()
        return True


logger = logging.getLogger("study.context")
logger.setLevel(logging.INFO)
logger.propagate = False

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter("%(levelname)s:%(request_id)s:%(message)s")
)
handler.addFilter(RequestContextFilter())
logger.addHandler(handler)

request_id_var.set("req-104")
logger.info("request started")
```

Versión ejecutable: [`examples/context_filter.py`](examples/context_filter.py).

## 55. Ejemplo práctico: preservar la atribución del llamador

```python
import logging


class RecordCollector(logging.Handler):
    def __init__(self) -> None:
        super().__init__()
        self.records: list[logging.LogRecord] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.records.append(record)


logger = logging.getLogger("study.stacklevel")
logger.setLevel(logging.INFO)
logger.propagate = False
collector = RecordCollector()
logger.addHandler(collector)


def log_notice(message: str) -> None:
    logger.info(message, stacklevel=2)


def run_job() -> None:
    log_notice("job started")


run_job()
record = collector.records[0]
print(f"{record.levelname}:{record.funcName}:{record.getMessage()}")
```

Versión ejecutable: [`examples/stacklevel_helper.py`](examples/stacklevel_helper.py).

## 56. Ejemplo práctico: mover la salida detrás de una cola

```python
import logging
import queue
import sys
from logging.handlers import QueueHandler, QueueListener


log_queue = queue.Queue()
output_handler = logging.StreamHandler(sys.stdout)
output_handler.setFormatter(
    logging.Formatter("%(levelname)s:%(name)s:%(message)s")
)

logger = logging.getLogger("study.queue")
logger.setLevel(logging.INFO)
logger.propagate = False
logger.addHandler(QueueHandler(log_queue))

listener = QueueListener(
    log_queue,
    output_handler,
    respect_handler_level=True,
)
listener.start()
try:
    logger.info("queued event")
finally:
    listener.stop()
```

Versión ejecutable: [`examples/queue_listener.py`](examples/queue_listener.py).

## 57. Errores comunes

### Configurar solamente el nivel de un logger ancestro y esperar que filtre registros propagados

Los niveles de loggers ancestros no se vuelven a aplicar durante la propagación. Configura el nivel del handler relevante.

### Asociar el mismo handler visible en varios niveles de la jerarquía

La propagación puede emitir duplicados.

### Llamar `basicConfig()` repetidamente y asumir que cada llamada reconfigura logging

Sin `force=True`, normalmente no hace nada cuando el root ya tiene handlers.

### Omitir `disable_existing_loggers` en `dictConfig()`

Loggers no root preexistentes pueden ser deshabilitados inesperadamente.

### Tratar configuración incremental como reemplazo completo de topología

El modo incremental ignora definiciones de formatter y filter y cambia solo un subconjunto limitado de propiedades.

### Asumir que `Formatter(style="{")` cambia la interpolación del mensaje del logger

El estilo del formatter aplica al formato de salida, no a la mezcla normal de argumentos de la llamada de logger.

### Usar claves de `extra` que colisionan con `LogRecord`

Los atributos integrados pertenecen al logging.

### Exigir campos personalizados en formatters para registros que tal vez no los tengan

Usa un contrato coherente de contexto o `Formatter(defaults=...)` cuando corresponda.

### Crear un logger por request o entidad de runtime

Usa nombres de logger estables más campos contextuales.

### Ocultar al llamador real detrás de un helper

Usa `stacklevel` cuando la atribución de origen deba apuntar al llamador del wrapper.

### Calcular diagnósticos costosos para niveles deshabilitados

Usa `isEnabledFor()` alrededor de preparación de argumentos realmente costosa.

### Enviar I/O lento directamente desde código sensible a latencia

Considera `QueueHandler` / `QueueListener`.

### Escribir el mismo archivo independientemente desde varios procesos

Los file handlers estándar no ofrecen locking compartido entre procesos.

### Tratar rotación como garantía de concurrencia

El rollover gestiona archivos; no coordina procesos independientes.

### Confiar en configuración dinámica de remitentes no confiables

La configuración puede construir objetos y cruza una frontera de seguridad.

### Registrar secretos esperando que un formatter los elimine después

No pongas datos sensibles innecesarios en el registro desde el principio.

## 58. Ejercicio: diseña un contrato de logging para una aplicación de workers

Diseña una pequeña aplicación con estos namespaces de logger:

```text
worker
worker.fetch
worker.parse
```

Requisitos:

1. usa `dictConfig()` con `version=1`;
2. configura `disable_existing_loggers=False` explícitamente;
3. configura un console handler en `INFO`;
4. configura un segundo handler que acepte `ERROR` o superior;
5. permite que `worker.fetch` emita registros `DEBUG` sin convertir paquetes no relacionados globalmente en `DEBUG`;
6. agrega un campo estable `job_id` a todos los registros de un job;
7. preserva el llamador real cuando uses un helper de logging;
8. garantiza que un formatter no falle cuando un registro de tercero carezca de `job_id`;
9. evita salida duplicada mediante propagación;
10. documenta qué componente controla la configuración de logging;
11. explica cómo moverías I/O lento de destino detrás de una cola;
12. explica qué cambia si varios **procesos** workers deben contribuir a un único archivo;
13. enumera al menos tres campos que decides no registrar por privacidad o seguridad.

Después prueba al menos estos escenarios:

```text
DEBUG record from worker.fetch
INFO record from worker.parse
ERROR record reaching both intended destinations
third-party WARNING with no job_id
helper call preserving the caller function
exception record with one traceback only
```

El objetivo no es crear la configuración más grande. El objetivo es que el contrato de enrutamiento y contexto sea explicable.

## 59. Referencia rápida

| Necesidad | Herramienta / política |
|---|---|
| Crear logger de módulo | `logging.getLogger(__name__)` |
| Inspeccionar umbral heredado | `logger.getEffectiveLevel()` |
| Comprobar antes de diagnóstico costoso | `logger.isEnabledFor(level)` |
| Definir umbral de destino | `handler.setLevel(level)` |
| Detener entrega a ancestros | `logger.propagate = False` |
| Comprobar handlers en la jerarquía | `logger.hasHandlers()` |
| Reemplazar configuración básica del root | `logging.basicConfig(..., force=True)` |
| Configurar grafo de objetos | `logging.config.dictConfig()` |
| Preservar loggers de bibliotecas existentes | `disable_existing_loggers=False` |
| Cambiar solo verbosidad en runtime incrementalmente | `incremental=True`, dentro de su semántica limitada |
| Agregar contexto a una llamada | `extra={...}` |
| Reutilizar contexto de ámbito | `logging.LoggerAdapter` |
| Mezclar contexto del adapter y de la llamada en 3.13+ | `merge_extra=True` |
| Filtrar o enriquecer una ruta | filter de logger/handler |
| Reemplazar registros en un filter en 3.12+ | devolver un nuevo `LogRecord` |
| Agregar atributos globales del proceso | `setLogRecordFactory()`, con cautela |
| Transportar contexto lógico request/task | `contextvars` |
| Preservar llamador a través de wrapper | `stacklevel=...` |
| Incluir traceback de excepción | `exc_info=True` / `logger.exception()` |
| Incluir stack actual | `stack_info=True` |
| Deshabilitar niveles globalmente | `logging.disable(level)` |
| Proporcionar fallbacks para campos personalizados | `Formatter(defaults=...)` |
| Mover entrega lenta fuera de la thread llamadora | `QueueHandler` + `QueueListener` |
| Iniciar/detener listener automáticamente en 3.14+ | `with QueueListener(...)` |
| Rotar por tamaño | `RotatingFileHandler` |
| Rotar por tiempo | `TimedRotatingFileHandler` |
| Enrutar warnings de Python hacia logging | `logging.captureWarnings(True)` |
| Controlar diagnósticos internos de handlers | `logging.raiseExceptions` |

## 60. Checklist de diseño

Antes de publicar una configuración de logging, pregunta:

```text
Which code area owns each logger name?
Which component owns process-wide configuration?
What is each logger's effective level?
Which handler levels apply after logger eligibility?
Where does propagation stop?
Can one record reach the same destination twice?
Could dictConfig disable an existing logger accidentally?
Are custom fields present for every formatter that requires them?
Could custom field names collide with LogRecord attributes?
Should context be per call, per scope, per handler, or process-wide?
Does a helper preserve caller attribution?
Are exception tracebacks emitted exactly where they add value?
Is expensive diagnostic context guarded when the level is disabled?
Could a slow handler block latency-sensitive code?
What happens if a queue fills?
Are several processes writing one file independently?
Who owns rotation and retention?
What timezone do timestamps represent?
Could a logging failure affect application behavior?
Can untrusted input alter logging configuration?
Could any record contain secrets or unnecessary personal data?
Which logging behaviors are covered by tests?
```

Si estas preguntas tienen respuestas explícitas, el sistema de logging es mucho más fácil de operar y mantener.

## 61. Conexiones con otros conceptos de Python

Este capítulo combina varios temas anteriores:

- **módulos y paquetes:** los nombres de logger siguen naturalmente la jerarquía de módulos;
- **diccionarios:** `dictConfig()` modela un grafo de configuración;
- **objetos y clases:** handlers, filters, formatters, adapters y records colaboran mediante interfaces;
- **excepciones:** fallos de logging y fallos de aplicación tienen políticas diferentes;
- **context managers:** Python 3.14 añade ciclo de vida por context manager a `QueueListener`;
- **threads y colas:** la entrega lenta puede desacoplarse de la creación de eventos;
- **procesos:** un único archivo necesita una estrategia deliberada de escritor único;
- **variables de contexto:** el contexto lógico de ejecución puede enriquecer registros sin nombres dinámicos de logger;
- **tests:** los registros pueden verificarse semánticamente en lugar de comparar solo strings renderizadas;
- **seguridad:** tanto configuración como payloads de log cruzan fronteras de confianza.

Por eso el logging avanzado trata menos de imprimir mensajes y más de diseñar un grafo fiable de entrega de eventos.

## Referencias

- [Referencia Python de `logging`](https://docs.python.org/3/library/logging.html)
- [Referencia Python de `logging.config`](https://docs.python.org/3/library/logging.config.html)
- [Referencia Python de `logging.handlers`](https://docs.python.org/3/library/logging.handlers.html)
- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)

## Próximo capítulo

Continúa con el [Capítulo 06: `collections`](../06-collections/README.es.md). Estudia contenedores especializados como `Counter`, `defaultdict`, `deque`, registros de tuplas nombradas, mappings por capas, herramientas de reordenación, bases wrapper e interfaces de colección como elecciones explícitas de estructura de datos y no trucos de conveniencia.
