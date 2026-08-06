<div align="center">

# Comentarios frente a Logging en Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Marcadores de tareas](../04-task-markers/README.es.md)

Los comentarios y los logs comunican información, pero hablan de momentos diferentes. Un comentario explica el código fuente a quien lo lee. Un log registra un evento ocurrido mientras el programa se ejecutaba.

> **Principio rector:** Coloca el razonamiento estable junto al código. Coloca los hechos variables de ejecución en los registros de log.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Intermedio |
| Requisitos previos | Se recomienda el capítulo de comentarios; ayuda una familiaridad básica con funciones, excepciones y módulos |
| Tiempo estimado de estudio | 55 a 75 minutos |
| Conceptos principales | comentarios, `print()`, `logging`, niveles, loggers por módulo, configuración de la aplicación, handlers, formatters, propagación, excepciones, privacidad |

## Objetivos de aprendizaje

Al terminar este capítulo, deberías poder:

- diferenciar la explicación del código fuente de la observación durante la ejecución;
- elegir entre comentario, salida para el usuario, registro de log y excepción;
- utilizar `logging.getLogger(__name__)` en módulos;
- seleccionar un nivel estándar apropiado;
- configurar logging en el punto de entrada de la aplicación;
- evitar que las bibliotecas reutilizables controlen la configuración global;
- escribir mensajes parametrizados con contexto útil y no sensible;
- registrar excepciones sin ocultar ni duplicar el manejo de errores;
- reconocer registros duplicados, ruido excesivo y riesgos de privacidad;
- revisar un cambio de logging por su claridad y valor operativo.

## 1. Comentarios y logs responden preguntas diferentes

Un comentario útil responde preguntas como:

- ¿Por qué existe esta regla?
- ¿Qué restricción externa dio forma a esta implementación?
- ¿Por qué la alternativa aparentemente obvia es insegura?
- ¿Qué supuesto estable podría pasar desapercibido?

```python
# The partner API returns monetary values in cents.
amount_cents = payload["amount"]
```

Un log útil responde preguntas como:

- ¿Qué ocurrió en esta ejecución?
- ¿Qué operación comenzó, terminó, volvió a intentarse o falló?
- ¿Qué identificador seguro ayuda a correlacionar el evento?
- ¿Qué severidad corresponde?

```python
logger.info("Processed invoice invoice_id=%s", invoice_id)
```

Los comentarios permanecen en el código fuente. Los logs se emiten durante la ejecución y pueden filtrarse, formatearse, almacenarse, buscarse o reenviarse.

## 2. Una tabla de decisión compacta

| Necesidad | Prefiere |
|---|---|
| Explicar una decisión estable de diseño | Comentario |
| Documentar un módulo, función, clase o método público | Docstring |
| Mostrar un resultado o instrucción directamente al usuario | `print()` o la capa de interfaz |
| Registrar un evento de ejecución para diagnóstico u operación | Logging |
| Señalar que la operación actual no puede continuar normalmente | Excepción |
| Medir tasas, latencia, cantidades o salud del servicio | Métricas |
| Preservar historial empresarial controlado o resistente a manipulaciones | Registro de auditoría específico |

Ningún mecanismo sustituye a todos los demás.

## 3. `print()` no es un logger defectuoso

`print()` es apropiado cuando el texto forma parte de la salida destinada al usuario:

```python
print("Report saved successfully.")
```

Una herramienta de línea de comandos puede imprimir una tabla, una respuesta o instrucciones. Una aplicación gráfica puede mostrar el equivalente mediante componentes visuales. Logging normalmente se dirige a desarrollo, operaciones, soporte o sistemas de diagnóstico.

No reemplaces cada `print()` por logging. Primero decide quién necesita el mensaje y si forma parte de la interfaz del programa.

## 4. Crea un logger a nivel de módulo

El patrón recomendado es:

```python
import logging


logger = logging.getLogger(__name__)


def process_order(order_id: str) -> None:
    logger.info("Processing order order_id=%s", order_id)
```

Usar `__name__` crea nombres que siguen la jerarquía de paquetes y módulos. Así la aplicación puede activar, suprimir o dirigir registros de partes específicas.

No instancies `logging.Logger` directamente en el uso común. Las llamadas repetidas a `logging.getLogger()` con el mismo nombre devuelven el mismo logger.

## 5. La aplicación controla la configuración

La mayoría de los módulos debe emitir registros. El punto de entrada decide:

- nivel mínimo;
- destinos como consola, archivo o handler remoto;
- formato;
- inclusión de hora, proceso o identificador de correlación;
- políticas distintas para desarrollo, pruebas y producción.

```python
import logging


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
    )
```

`basicConfig()` es práctico para aplicaciones pequeñas y ejemplos. Aplicaciones mayores pueden usar `dictConfig()`, opciones de línea de comandos, configuración por entorno o recursos del framework.

## 6. Las bibliotecas reutilizables no deben apropiarse de la configuración global

Una biblioteca no sabe cómo la aplicación desea dirigir o formatear los logs. Esto es intrusivo:

```python
# Inside a reusable library module:
logging.basicConfig(level=logging.DEBUG)
```

Una biblioteca reutilizable normalmente debe:

1. crear un logger con `logging.getLogger(__name__)`;
2. emitir registros en niveles significativos;
3. evitar configurar el logger raíz o añadir handlers visibles;
4. opcionalmente añadir `logging.NullHandler()` a su logger principal.

```python
import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
```

`NullHandler` evita que la biblioteca presuma un destino. Los registros aún pueden propagarse a handlers configurados por la aplicación.

## 7. Niveles estándar de logging

Python ofrece cinco niveles comunes:

| Nivel | Significado típico |
|---|---|
| `DEBUG` | información diagnóstica detallada para investigación |
| `INFO` | hitos esperados y operaciones normales relevantes |
| `WARNING` | situación inesperada o degradada, pero el trabajo puede continuar |
| `ERROR` | una operación falló o produjo un resultado inutilizable |
| `CRITICAL` | la aplicación o un subsistema importante quizá no pueda continuar |

```python
logger.debug("Validated %s columns", column_count)
logger.info("Imported %s records", record_count)
logger.warning("Retrying after timeout attempt=%s", attempt)
logger.error("Could not save report report_id=%s", report_id)
logger.critical("Database is unavailable; stopping worker")
```

Estos significados son políticas, no leyes matemáticas. El proyecto debe definir ejemplos de su dominio para clasificar eventos similares con coherencia.

## 8. `DEBUG` debe revelar detalles sin convertirse en un volcado de datos

Los registros de debug útiles pueden mostrar:

- estrategia o rama seleccionada;
- cantidades y dimensiones seguras;
- aciertos o fallos de caché;
- intentos;
- identificadores sanitizados de solicitudes o tareas.

Evita registrar payloads completos por defecto. Los objetos grandes crean ruido, aumentan costes, dificultan el diagnóstico y pueden exponer información sensible.

Un registro de debug debe escribirse para una persona, no utilizarse como sustituto de comprender el código.

## 9. `INFO` registra eventos normales relevantes

Los buenos eventos de `INFO` suelen describir límites:

- una tarea comenzó o terminó;
- se generó un informe;
- una migración procesó un lote;
- se activó una versión de configuración;
- una integración externa finalizó correctamente.

No registres cada iteración de un bucle en `INFO` solo porque logging está disponible. Un evento normal de gran volumen puede pertenecer a `DEBUG`, a una métrica o a ninguna parte.

## 10. `WARNING`, `ERROR` y `CRITICAL` requieren criterio

Usa `WARNING` cuando el programa puede continuar pero el evento merece atención, como un fallback, un reintento, una entrada obsoleta o capacidad reducida.

Usa `ERROR` cuando una operación concreta falló. El proceso aún puede continuar con otro trabajo.

Reserva `CRITICAL` para condiciones que amenazan la aplicación o un subsistema importante. Si cada fallo de validación es crítico, el nivel deja de comunicar severidad.

El nivel debe corresponder a la consecuencia, no a la frustración de quien desarrolla.

## 11. Registra excepciones durante su manejo

`logger.exception()` crea un registro `ERROR` e incluye el traceback de la excepción actual. Úsalo dentro de un manejador:

```python
try:
    save_report(report)
except OSError:
    logger.exception("Could not save report report_id=%s", report.id)
    raise
```

Registrar la excepción no decide si el programa debe recuperarse, traducirla, reintentar o volver a lanzarla. Manejo de errores y observabilidad son responsabilidades relacionadas, pero distintas.

Evita registrar la misma excepción en cada capa. Cuando una capa inferior registra y relanza y todos los llamadores vuelven a registrar, un fallo se convierte en una pared de tracebacks repetidos.

## 12. Prefiere mensajes parametrizados

Escribe:

```python
logger.info("Processed %s records", record_count)
```

En lugar de formatear anticipadamente:

```python
logger.info(f"Processed {record_count} records")
```

La llamada conserva la plantilla y los argumentos por separado y realiza la interpolación cuando el registro se formatea. Los mensajes parametrizados también mantienen una forma estable para lectores y algunas herramientas.

No uses `%` manualmente antes de llamar al logger:

```python
logger.info("Processed %s records" % record_count)
```

Eso formatea anticipadamente y pierde la ventaja.

## 13. Incluye contexto que permita actuar

El registro debe ser comprensible sin una búsqueda interminable:

```python
logger.info(
    "Payment authorized order_id=%s provider=%s",
    order_id,
    provider_name,
)
```

El contexto útil puede incluir:

- identificadores internos estables;
- nombres de operaciones o tareas;
- cantidades y unidades seguras;
- nombres de proveedores o componentes;
- número del intento;
- tiempo transcurrido cuando se mide correctamente.

Prefiere campos explícitos como `order_id=` o `attempt=`. Un número aislado tiene poco significado.

## 14. Nunca registres secretos ni datos personales innecesarios

Esto es inseguro:

```python
logger.debug("Authenticated with token=%s", access_token)
```

No registres:

- contraseñas, tokens, claves de API o cookies de sesión;
- datos completos de pago;
- contenido privado de clientes;
- identificadores personales sin necesidad documentada;
- cabeceras de autenticación sin filtrar;
- secretos ocultos dentro de objetos completos de solicitud o configuración.

La redacción ayuda, pero no justifica recopilar datos que el log nunca necesitó. La política debe seguir los requisitos de privacidad, seguridad y retención.

## 15. Handlers, formatters y filters

Un registro recorre un pequeño pipeline:

```text
logging call → logger → filters → handler → formatter → destination
```

- **Logger:** crea y dirige el registro.
- **Handler:** envía registros aceptados a un destino.
- **Formatter:** convierte el registro en texto u otra representación.
- **Filter:** aplica reglas adicionales o añade contexto controlado.

Las aplicaciones pequeñas pueden necesitar solo `basicConfig()`. Comprender las piezas ayuda cuando se necesita consola en `INFO`, archivo en `DEBUG` o políticas distintas por paquete.

## 16. Propagación y registros duplicados

Los nombres forman una jerarquía. Normalmente los registros se propagan de un logger hijo a handlers antecesores.

Los duplicados suelen aparecer cuando el mismo handler se añade al logger del módulo y al logger raíz:

```python
logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)

root_logger = logging.getLogger()
root_logger.addHandler(stream_handler)
```

Prefiere configurar handlers suficientemente arriba y dejar que los loggers hijos propaguen naturalmente.

Esto detiene la propagación:

```python
logger.propagate = False
```

Úsalo de forma deliberada. Desactivarla sin añadir un handler apropiado puede hacer que los registros desaparezcan.

## 17. Contexto estructurado y adapters

Texto con campos estables `clave=valor` suele bastar para proyectos pequeños. Las aplicaciones también pueden añadir contexto con `extra`:

```python
logger.info(
    "Started request",
    extra={"request_id": request_id},
)
```

Un `LoggerAdapter` puede añadir contexto repetido:

```python
request_logger = logging.LoggerAdapter(
    logger,
    {"request_id": request_id},
)
request_logger.info("Started request")
```

Elige nombres que no colisionen con atributos integrados de `LogRecord`. Bibliotecas de logging estructurado e integraciones de plataforma pueden ofrecer esquemas más ricos, pero los principios de privacidad y severidad permanecen.

## 18. Logging no es métricas, tracing ni auditoría

Logging registra eventos discretos. Otros instrumentos responden preguntas distintas:

- **Métricas:** ¿Con qué frecuencia? ¿Cuánto? ¿Qué tan rápido?
- **Tracing:** ¿Cómo viajó una solicitud entre componentes?
- **Registro de auditoría:** ¿Quién cambió un objeto controlado, cuándo y bajo qué política?
- **Reporte de excepciones:** ¿Qué fallos necesitan agrupación, alertas y análisis?

Un proyecto puede derivar métricas de logs, pero depender solo de mensajes en prosa es frágil. Las auditorías de seguridad o finanzas suelen requerir garantías más fuertes que los logs comunes.

## 19. Probar el comportamiento de logging

Las pruebas deben enfocarse en contratos relevantes, no en puntuación incidental.

Afirmaciones útiles incluyen:

- se emite un warning para un fallback documentado;
- un secreto nunca aparece;
- una biblioteca no configura el logger raíz;
- un registro de error contiene el identificador seguro necesario;
- un evento ruidoso de debug se filtra en producción.

`unittest` ofrece `assertLogs()`. Los proyectos con pytest suelen usar `caplog`. Evita congelar cada palabra de un mensaje interno salvo que su redacción sea una interfaz soportada.

## 20. Ejemplos de este repositorio

| Archivo | Propósito |
|---|---|
| [`comments_vs_logging.py`](examples/comments_vs_logging.py) | Coloca razonamiento estable en un comentario y valores de ejecución en un log |
| [`logging_levels.py`](examples/logging_levels.py) | Emite ejemplos deterministas de los cinco niveles estándar |
| [`application_and_library_logging.py`](examples/application_and_library_logging.py) | Muestra configuración de la aplicación y uso al estilo de biblioteca |

Ejecuta un ejemplo desde la raíz:

```bash
python comments-and-documentation/05-comments-vs-logging/examples/comments_vs_logging.py
```

En sistemas que usan `python3`:

```bash
python3 comments-and-documentation/05-comments-vs-logging/examples/comments_vs_logging.py
```

## 21. Ejemplo práctico de refactorización

Antes:

```python
def import_file(file_path):
    # The import started.
    print("Importing...")
    try:
        return parse_file(file_path)
    except OSError:
        print("Import failed")
        return None
```

Después:

```python
import logging


logger = logging.getLogger(__name__)


def import_file(file_path):
    logger.info("Starting import file_name=%s", file_path.name)
    try:
        return parse_file(file_path)
    except OSError:
        logger.exception("Import failed file_name=%s", file_path.name)
        raise
```

La refactorización elimina un comentario que describía un evento de ejecución, reemplaza prints diagnósticos por registros, conserva la excepción e incluye un nombre de archivo seguro. La política de recuperación correcta aún depende de la aplicación.

## 22. Errores comunes

### Comentar el estado de ejecución

Un comentario no informa si la ejecución de hoy comenzó, reintentó o falló.

### Registrar razonamiento estable únicamente en logs

Un registro no existe cuando el código no se ejecuta y no debe ser el único lugar que explica una regla empresarial.

### Llamar `basicConfig()` en cada módulo

La configuración se vuelve impredecible, las bibliotecas intrusivas y las pruebas más difíciles.

### Registrar y ocultar una excepción

Un traceback en el log no convierte una operación fallida en correcta.

### Registrar la misma excepción repetidamente

Un fallo se convierte en varios registros ruidosos con poco valor adicional.

### Usar `ERROR` para validación común

La severidad debe corresponder a la consecuencia operativa.

### Formatear mensajes anticipadamente

Las f-strings son prácticas, pero los argumentos parametrizados preservan formato diferido y una plantilla estable.

### Incluir secretos para “debug temporal”

El historial de Git puede olvidar el cambio, pero el almacenamiento de logs puede conservar el secreto.

### Añadir handlers en varios niveles

La propagación puede producir duplicados.

### Tratar logs como interfaz de usuario

Los registros operativos no sustituyen mensajes claros para el usuario.

## 23. Ejercicio

Clasifica y reescribe cada línea. Decide si corresponde a comentario, salida para usuario, log, excepción o si debe eliminarse:

```python
# The job started at runtime.
# TODO: print every processed customer.
print(f"Could not import {file_name}")
logger.info("The tax rate is fixed by regulation.")
logger.error("Customer password=%s", password)
```

Para cada decisión, explica:

1. ¿Quién necesita la información?
2. ¿Es razonamiento estable o un hecho de ejecución?
3. ¿Qué nivel es apropiado?
4. ¿Qué contexto seguro vuelve accionable el evento?
5. ¿El mensaje puede exponer datos sensibles?
6. ¿La operación debe continuar, recuperarse o lanzar una excepción?

Después configura un script pequeño con logger de módulo y comprueba cómo cambiar el nivel configurado modifica los registros visibles.

## 24. Lista de revisión

Antes de aceptar un cambio de logging, comprueba:

- [ ] los comentarios explican decisiones estables y no eventos de ejecución;
- [ ] la salida al usuario permanece separada del diagnóstico;
- [ ] los módulos usan `logging.getLogger(__name__)`;
- [ ] la aplicación controla handlers, formatters y niveles globales;
- [ ] las bibliotecas reutilizables no llaman `basicConfig()`;
- [ ] los niveles corresponden a la consecuencia;
- [ ] los mensajes usan argumentos parametrizados;
- [ ] los registros incluyen suficiente contexto seguro;
- [ ] se excluyen secretos y datos personales innecesarios;
- [ ] las excepciones se registran solo donde el traceback aporta valor;
- [ ] la propagación no duplica registros;
- [ ] los eventos de gran volumen no saturan los logs normales;
- [ ] los logs no sustituyen métricas, auditoría ni manejo de errores.

## 25. Resumen de consulta rápida

| Situación | Enfoque recomendado |
|---|---|
| Razón estable junto a una implementación | Comentario |
| Contrato público de módulo o callable | Docstring |
| Salida destinada a quien usa el programa | `print()` o capa de interfaz |
| Evento diagnóstico detallado | `DEBUG` |
| Hito normal relevante | `INFO` |
| Condición recuperable o degradada | `WARNING` |
| Operación fallida | `ERROR` |
| Un subsistema importante quizá no continúe | `CRITICAL` |
| Traceback actual dentro de `except` | `logger.exception()` |
| Logger en módulo reutilizable | `logging.getLogger(__name__)` |
| Destinos y formato de la aplicación | Configurar en el punto de entrada |
| Contexto repetido | Campos parametrizados, `extra` o `LoggerAdapter` |
| Contraseñas, tokens y payloads privados | Nunca registrarlos |

Los comentarios preservan razonamiento en el código fuente. Logging preserva evidencia seleccionada de la ejecución. El buen software necesita ambos, con una frontera clara.

## Referencias oficiales

- [Python Logging HOWTO](https://docs.python.org/es/3/howto/logging.html)
- [Referencia del módulo `logging`](https://docs.python.org/es/3/library/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
