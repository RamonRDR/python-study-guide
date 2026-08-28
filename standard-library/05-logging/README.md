<div align="center">

# Engineering Logging Pipelines and Runtime Context Contracts

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Standard Library](../README.md) · [← Previous chapter: CSV](../04-csv/README.md)

The earlier logging chapter in Phase 6 introduced the purpose of logging, standard levels, module loggers, application-owned configuration, handlers, formatters, propagation, exception logging, privacy, and the difference between logs and comments.

This chapter goes deeper. The focus is no longer only **what message should I log?** but also:

```text
How does a LogRecord move through the logging graph,
which component is allowed to change it,
and what runtime contract does the application promise?
```

The `logging` package is flexible because it separates event creation, filtering, routing, formatting, and output. That flexibility is useful only when the configuration is treated as an explicit system design rather than a pile of `basicConfig()` calls.

**Estimated study time:** 150–190 minutes.

**Python requirement:** Python 3.10 or newer for the core material and executable examples. Version-specific sections identify features added in Python 3.12, 3.13, and 3.14.

**Documentation baseline:** behavior and version notes were checked against the official Python 3.14 `logging`, `logging.config`, `logging.handlers`, Logging HOWTO, and Logging Cookbook documentation.

## Learning objectives

By the end of this chapter, you should be able to:

- model logging as a pipeline that carries `LogRecord` objects;
- distinguish logger thresholds, effective levels, handler thresholds, filters, and propagation;
- explain why ancestor logger levels are not re-applied during propagation;
- diagnose duplicate and unexpectedly missing records;
- use `basicConfig(force=True)` deliberately when replacing existing root configuration;
- design explicit `dictConfig()` dictionaries without accidentally disabling pre-existing loggers;
- explain what incremental logging configuration can and cannot change;
- distinguish formatter style from logging-call message interpolation;
- add contextual fields without colliding with built-in `LogRecord` attributes;
- choose between `extra`, `LoggerAdapter`, filters, `contextvars`, and a record factory;
- preserve caller attribution through logging helper functions with `stacklevel`;
- distinguish `exc_info` from `stack_info`;
- avoid expensive work for disabled log levels;
- understand handler error policy and `logging.raiseExceptions`;
- move slow handler work behind `QueueHandler` and `QueueListener` when appropriate;
- reason about threads, processes, file rotation, and single-writer logging designs;
- recognize unsafe dynamic logging configuration patterns;
- test logging behavior as an application contract rather than as incidental text output.

## 1. What this chapter adds after Phase 6

Phase 6 taught the everyday interface:

```python
import logging


logger = logging.getLogger(__name__)
logger.info("Processed %s records", record_count)
```

That remains correct. This chapter studies what happens around that call:

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

The details matter when a real application has several packages, third-party libraries, multiple destinations, async work, worker threads, dynamic verbosity, or structured context.

## 2. A logging event becomes a `LogRecord`

When a logger accepts an event, Python represents that event as a `LogRecord`.

The record carries information such as:

- logger name;
- numeric and textual level;
- message template and arguments;
- source pathname, function name, and line number;
- process and thread information;
- optional exception or stack information;
- custom attributes supplied by controlled context mechanisms.

Formatters and handlers consume that record later.

A useful mental model is:

```text
logging call = event request
LogRecord    = event data object
handler      = delivery policy
formatter    = output representation
```

Do not treat the rendered text line as the whole logging system. The record exists before the final representation.

## 3. Logger names form a hierarchy

Logger names use dot-separated hierarchy:

```python
import logging


root = logging.getLogger()
service = logging.getLogger("app.service")
worker = logging.getLogger("app.service.worker")
```

`app.service.worker` is a descendant of `app.service`, which is a descendant of `app`, which ultimately reaches the root logger.

This is why `logging.getLogger(__name__)` fits Python packages naturally. A module such as:

```text
catalog.importer.csv_reader
```

can participate in the hierarchy:

```text
catalog
catalog.importer
catalog.importer.csv_reader
```

The hierarchy is a routing namespace. It does not mean logger objects must be passed around as dependencies. Repeated `getLogger()` calls with the same name return the same logger object.

## 4. `NOTSET` means inheritance on non-root loggers

New non-root loggers normally start at `NOTSET`.

For a non-root logger, `NOTSET` does not mean "log nothing." It means Python walks upward until it finds an ancestor with an explicit level, or reaches the root.

```python
import logging


root = logging.getLogger()
root.setLevel(logging.WARNING)

logger = logging.getLogger("app.worker")
logger.setLevel(logging.NOTSET)

print(logger.getEffectiveLevel() == logging.WARNING)
```

The root logger starts at `WARNING` unless configuration changes it.

This distinction explains many "why did my INFO record disappear?" bugs.

## 5. Logger eligibility happens before record delivery

A logger first decides whether an event is enabled.

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug("Cache snapshot size=%s", cache_size)
```

`isEnabledFor()` considers:

1. the module-wide override established by `logging.disable()`;
2. the logger's effective level.

If the event does not pass this stage, a normal `LogRecord` is not created for delivery to handlers.

This is different from a handler rejecting a record later.

## 6. Handler levels are a second threshold

A logger may accept a record while a particular handler rejects it.

```python
import logging


logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
```

Here:

```text
DEBUG event
  logger accepts it
  handler rejects it

WARNING event
  logger accepts it
  handler accepts it
```

This two-stage model supports designs such as:

```text
logger: DEBUG
console handler: INFO
file handler: DEBUG
alert handler: ERROR
```

The logger controls whether the event enters the delivery pipeline. Each handler controls whether that destination receives it.

## 7. Propagation does not re-check ancestor logger levels

This detail is easy to miss.

When a record propagates from a child logger, Python offers it directly to handlers attached to ancestor loggers. The levels and filters of those ancestor **logger objects** are not re-applied during propagation.

The handlers still apply their own levels and filters.

Conceptually:

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

Do not assume that setting the ancestor logger itself to `ERROR` will filter records already accepted by descendants and propagating to its handlers. Put destination thresholds on handlers when that is the policy you need.

## 8. Duplicate records are usually a graph problem

Consider this configuration:

```python
import logging


handler = logging.StreamHandler()

root = logging.getLogger()
root.addHandler(handler)

child = logging.getLogger("app.worker")
child.addHandler(handler)
child.propagate = True
```

A record emitted by `app.worker` can reach the same handler through the child and again through the ancestor path.

A reliable default is:

```text
application entry point configures shared handlers high in the hierarchy
modules create loggers
modules do not attach duplicate visible handlers
propagation remains enabled unless isolation is intentional
```

Setting `propagate = False` can solve a deliberate routing boundary, but it is not a universal duplicate-removal button. A logger with propagation disabled also stops reaching ancestor handlers.

## 9. `hasHandlers()` follows propagation boundaries

`logger.hasHandlers()` checks the logger and walks upward through ancestors.

The search stops when it reaches a logger whose `propagate` is `False`.

```python
import logging


logger = logging.getLogger("app.worker")
print(isinstance(logger.hasHandlers(), bool))
```

This method answers whether the logger hierarchy can find a handler through its current propagation path. It does not promise that every record will actually be emitted because levels and filters may still reject the event.

## 10. `basicConfig()` is intentionally simple

`basicConfig()` is useful for small applications and command-line tools, but it configures the root logger and has lifecycle behavior that matters.

By default, if the root logger already has handlers, another `basicConfig()` call does nothing.

```python
import logging


logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

print(logging.getLogger().level == logging.WARNING)
```

That can surprise notebooks, test processes, plugin hosts, or applications whose dependencies already touched logging.

## 11. `force=True` replaces existing root handlers

Since Python 3.8, `basicConfig(force=True)` removes and closes existing root handlers before applying the new basic configuration.

```python
import logging


logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.INFO, force=True)

print(logging.getLogger().level == logging.INFO)
```

Use `force=True` when the application deliberately owns the process-wide root configuration and intends to replace it.

Do not casually use it inside reusable libraries. It can erase configuration installed by the host application.

## 12. `dictConfig()` makes the object graph explicit

For larger applications, `logging.config.dictConfig()` can describe formatters, filters, handlers, loggers, and the root logger in one configuration object.

A configuration dictionary requires `version`, and the supported schema version is currently `1`.

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

The benefit is not that dictionaries are magical. The benefit is that the logging graph becomes inspectable configuration instead of scattered mutation calls.

## 13. Be explicit about `disable_existing_loggers`

A dangerous omission in `dictConfig()` is forgetting this key:

```python
"disable_existing_loggers": False,
```

If the key is absent, existing non-root loggers are treated as disabled unless they or an ancestor are explicitly named by the configuration rules.

In an application that imports libraries before configuring logging, an accidental default of `True` can silence loggers that already exist.

Project guidance:

```text
If preserving pre-existing library loggers is intended,
write disable_existing_loggers=False explicitly.
```

Do not rely on a maintainer remembering the historical default.

## 14. Incremental configuration is intentionally narrow

`dictConfig()` supports:

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

But incremental mode does **not** rebuild the whole logging object graph.

When `incremental` is true, Python ignores `formatters` and `filters` entries. It processes handler `level`, and logger/root `level` plus logger `propagate` settings.

Use incremental configuration for controlled verbosity changes, not as a general hot-reload mechanism for arbitrary handler and formatter topology.

## 15. Formatter style and message interpolation are different contracts

A `Formatter` can use `%`, `{`, or `$` style for the **output format**:

```python
import logging


formatter = logging.Formatter(
    "{levelname}:{name}:{message}",
    style="{",
)
```

That does not change the normal interpolation contract of logger calls:

```python
logger.info("Processed %s records", record_count)
```

The message template and its arguments still use the logging package's normal `%`-style merging.

Do not infer this:

```python
logger.info("Processed {} records", record_count)
```

merely because the handler's `Formatter(style="{")` uses braces. Those are separate layers.

## 16. `Formatter(validate=True)` catches mismatched styles

Formatter validation is enabled by default.

```python
import logging


try:
    logging.Formatter("%(levelname)s:%(message)s", style="{")
except ValueError:
    print("format and style do not match")
```

Validation catches a configuration mistake early instead of waiting for a later event to reveal it.

## 17. `Formatter(defaults=...)` can define safe fallback fields

Python 3.10 added the `defaults` argument to `Formatter`.

```python
import logging


formatter = logging.Formatter(
    "%(request_id)s:%(message)s",
    defaults={"request_id": "-"},
)
```

Without a fallback, a formatter that requires a custom field may fail for records that do not contain it.

Defaults are useful when a handler receives both contextualized and ordinary records. They are not a substitute for defining a coherent schema when downstream systems require structured fields.

## 18. `extra` enriches the `LogRecord`

You can add custom attributes to a record:

```python
logger.info(
    "Job started",
    extra={"job_id": "job-104", "component": "importer"},
)
```

A formatter can then reference those fields:

```python
logging.Formatter(
    "%(levelname)s:%(job_id)s:%(component)s:%(message)s"
)
```

The keys supplied through `extra` are inserted into the record's attribute dictionary.

## 19. Custom fields must not collide with built-in record attributes

This is invalid design:

```python
logger.info(
    "Job started",
    extra={"levelname": "CUSTOM"},
)
```

Built-in names such as `levelname`, `name`, `message`, `pathname`, and many others belong to `LogRecord`.

Choose an application namespace that is clear and stable:

```text
request_id
job_id
component
tenant_code
operation
```

Do not add secrets or unnecessary personal data merely because `extra` makes it easy.

## 20. `LoggerAdapter` carries repeated context

When several records share the same contextual values, an adapter can reduce repetition:

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

The adapter delegates to an underlying logger while inserting context.

This is useful for scoped context such as one job, request, connection, or operation.

## 21. Python 3.13 added `LoggerAdapter(merge_extra=True)`

Historically, the adapter's own `extra` took precedence and an `extra` passed to an individual logging call was not merged by the default adapter implementation.

Python 3.13 added `merge_extra`:

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

If your library or application supports older Python versions, do not publish a configuration that silently assumes this 3.13 behavior.

## 22. Filters are more than yes/no predicates

A logger or handler can have filters.

A traditional filter returns a truthy value to keep a record or a false value to reject it:

```python
import logging


class IgnoreHealthChecks(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return getattr(record, "route", None) != "/health"
```

Filters are useful when level thresholds alone cannot express the policy.

Examples include:

- dropping one noisy category;
- allowing one logger subtree;
- injecting controlled context;
- counting records passing through a particular destination.

## 23. Python 3.12 filters can return a replacement `LogRecord`

Starting with Python 3.12, a filter may return a `LogRecord` instance to replace the original for future processing on that path.

This is especially useful on a handler when you want handler-specific enrichment without mutating the record seen by other handlers.

```python
import copy
import logging


def add_destination(record: logging.LogRecord):
    cloned = copy.copy(record)
    cloned.destination = "console"
    return cloned
```

The ability to replace rather than mutate a shared record reduces side effects across multiple handlers.

Document the Python 3.12 requirement if you depend on this behavior.

## 24. A `LogRecord` factory can add process-wide record context

Python exposes the current record factory:

```python
import logging


old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.application = "study-guide"
    return record


logging.setLogRecordFactory(record_factory)
```

A factory affects record creation globally inside the process.

That power requires restraint. Chaining factories adds overhead, and independent libraries can collide if they choose the same custom attribute names.

Prefer a filter or adapter when the context belongs only to one destination or scope.

## 25. Choose the narrowest context mechanism that fits

A practical decision table:

| Need | Prefer |
|---|---|
| One call has extra fields | `extra={...}` |
| Many calls in one scoped operation share fields | `LoggerAdapter` |
| One handler needs destination-specific enrichment | handler filter |
| Request/task context must flow through async/thread-aware code | `contextvars` + adapter/filter |
| Every created record needs a process-wide attribute | `LogRecord` factory, used carefully |

The most global mechanism is not automatically the most convenient one.

## 26. `contextvars` can carry request or task context

`contextvars.ContextVar` is useful when contextual data must follow logical execution without manually passing a logger through every function.

```python
import contextvars
import logging


request_id_var = contextvars.ContextVar("request_id", default="-")


class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get()
        return True
```

A handler using that filter can format `%(request_id)s`.

This pattern can work across threads and asynchronous tasks when context is managed correctly. It also keeps logger names tied to code areas rather than creating a new logger per request.

## 27. Do not create one logger per request, file, or customer

Logger instances are cached by name and are not freed during normal script execution.

This pattern creates unbounded logger namespaces:

```python
logger = logging.getLogger(f"request.{request_id}")
```

Prefer a stable logger:

```python
logger = logging.getLogger("app.request")
logger.info("Request started", extra={"request_id": request_id})
```

Logger names should usually identify software areas. Context fields identify individual runtime entities.

## 28. `stacklevel` preserves the real caller through helpers

A logging wrapper can otherwise make every record appear to originate from the helper itself.

```python
import logging


logger = logging.getLogger("app")


def log_notice(message: str) -> None:
    logger.info(message, stacklevel=2)
```

The caller:

```python
def run_job() -> None:
    log_notice("Job started")
```

can then be reported as the source rather than `log_notice()`.

This is valuable when helper functions standardize event shape but source attribution still needs to point to the application call site.

## 29. `exc_info` and `stack_info` answer different questions

`exc_info` captures exception traceback information.

```python
try:
    int("not-a-number")
except ValueError:
    logger.error("Parsing failed", exc_info=True)
```

`stack_info=True` captures the current call stack leading to the logging call, even without an exception:

```python
logger.debug("Reached diagnostic checkpoint", stack_info=True)
```

Think of them as:

```text
exc_info   → which frames were unwound by this exception?
stack_info → how did execution reach this logging call?
```

They can be used independently.

## 30. Avoid logging one exception at every layer

A lower layer may log and re-raise:

```python
try:
    load_document()
except OSError:
    logger.exception("Document load failed")
    raise
```

If every caller repeats the same pattern, one failure becomes several nearly identical tracebacks.

Choose a boundary that owns the operational record. Other layers can add information only when they truly add new context or change the handling decision.

Logging an exception and handling an exception are separate responsibilities.

## 31. Deferred formatting does not defer expensive argument computation

This is parameterized:

```python
logger.debug("Graph summary=%s", build_graph_summary())
```

but `build_graph_summary()` still executes before `logger.debug()` is called.

Guard expensive diagnostics:

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug("Graph summary=%s", build_graph_summary())
```

Use this when computing the arguments is meaningfully expensive. Do not wrap every trivial variable in an `isEnabledFor()` branch.

## 32. `logging.disable()` is a process-wide override

`logging.disable(level)` disables all logging calls at that severity and below, regardless of individual logger levels.

```python
import logging


logging.disable(logging.INFO)
# DEBUG and INFO calls are disabled process-wide.

logging.disable(logging.NOTSET)
# Remove the override.
```

This is different from changing one logger's effective level.

Use process-wide suppression sparingly because it affects unrelated logger hierarchies too.

## 33. `lastResort` explains unexpected warnings without configuration

If no handler can be found, Python provides `logging.lastResort`.

It is a `StreamHandler` at `WARNING` that writes the bare message to `sys.stderr`.

This explains why a reusable library can still appear to print warnings even when the host application has not configured logging.

A library that intentionally wants silence in this situation may attach `logging.NullHandler()` to its top-level logger, but it should still leave visible destination configuration to the application.

## 34. Handler failures have their own error policy

Errors can happen while emitting a log record: a stream may fail, a formatter may be wrong, a network destination may be unavailable, or a custom handler may raise.

`logging.raiseExceptions` is consulted by `Handler.handleError()` when a handler has caught an exception during emission and explicitly sends that failure through the standard handler-error path:

```python
logging.raiseExceptions
```

Its default is `True`, which is useful during development because `handleError()` can make logging failures visible on `sys.stderr`. Setting it to `False` is common in production when diagnostics from that error path should stay quiet.

This flag is **not a process-wide shield against every handler exception**. If a custom or third-party `emit()` implementation lets an exception escape instead of catching it and calling `handleError()`, `logging.raiseExceptions = False` does not prevent that exception from propagating back to the logging call.

Do not confuse the flag with suppressing application exceptions. It controls diagnostics produced by the standard `handleError()` path; robust custom handlers still need an explicit failure policy.

## 35. Custom `emit()` implementations must respect locking constraints

Handlers use locks around emission.

A custom `Handler.emit()` that calls logging configuration APIs or other lock-taking logging operations can create lock-order problems with another thread that is configuring logging.

Keep custom `emit()` implementations focused on delivery. Avoid re-entering configuration machinery from inside handler emission.

If a destination has complex blocking behavior, a queue boundary may be a better design.

## 36. Logging is thread-safe, but slow handlers still block the caller

The standard logging module uses locks so multiple threads can use shared logging infrastructure safely within one process.

Thread safety does not mean zero latency.

A handler that performs slow disk, network, SMTP, or other blocking I/O can keep the calling thread busy while the handler emits the record.

For latency-sensitive paths, decouple event creation from slow delivery.

## 37. `QueueHandler` moves records onto a queue

`logging.handlers.QueueHandler` sends records to a queue:

```python
import logging
import queue
from logging.handlers import QueueHandler


log_queue = queue.Queue()
queue_handler = QueueHandler(log_queue)

logger = logging.getLogger("app")
logger.addHandler(queue_handler)
```

The caller enqueues instead of performing the slow destination work directly.

A bounded queue can fill. `QueueHandler` uses non-blocking enqueue by default, and failures follow handler error policy.

Queue capacity and drop/block policy are operational design decisions, not details to ignore.

## 38. `QueueListener` performs handler work on a separate thread

A listener consumes queued records and forwards them to real handlers:

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

With `respect_handler_level=True`, the listener checks each target handler's level before dispatching a record to it.

This pattern is useful for web services, worker systems, and asynchronous applications where blocking handler I/O should not run on a latency-sensitive path.

## 39. Python 3.14 made `QueueListener` a context manager

Python 3.14 allows:

```python
with QueueListener(log_queue, output_handler) as listener:
    logger.info("Job queued")
```

Entering starts the listener. Exiting stops it.

The executable example in this repository uses explicit `start()` / `stop()` so it remains compatible with Python 3.10+, while this section documents the newer convenience API.

## 40. `QueueHandler.prepare()` changes what crosses the queue boundary

The base `QueueHandler.prepare()` formats the record so it can be safely queued and pickled in common scenarios.

That preparation merges the message and arguments and removes information such as `args`, `exc_info`, and `exc_text` that may be unpickleable or cause later formatting problems.

If the listener side needs custom exception formatting or a different serialized schema, subclass `QueueHandler` and override `prepare()` deliberately.

The queue boundary is a serialization contract. Do not assume the listener receives an untouched copy of every original record attribute.

## 41. Be careful with `multiprocessing.Queue` and its internal logger

The `multiprocessing` module has an internal logger. A `multiprocessing.Queue` can emit `DEBUG` records while queue operations occur.

If those internal records are routed through a `QueueHandler` that uses the **same** multiprocessing queue, the system can recurse or deadlock.

When combining multiprocessing and logging queues, design the listener topology deliberately and follow the documented `QueueHandler` multiprocessing warning.

## 42. Multiple processes should not independently write one standard file handler

Logging is thread-safe within a process, but the standard library does not provide process-shared locking for one `FileHandler` across multiple processes.

Independent processes writing the same file may interleave output or interfere with rotation.

A safer architecture is:

```text
worker process ─┐
worker process ─┼─> queue/socket ─> single listener/writer ─> file
worker process ─┘
```

Centralize the actual file write when multiple processes must contribute to one log stream.

## 43. Rotating handlers are retention tools, not multi-process coordination

The standard library includes:

- `RotatingFileHandler` for size-based rollover;
- `TimedRotatingFileHandler` for time-based rollover.

```python
from logging.handlers import RotatingFileHandler


handler = RotatingFileHandler(
    "application.log",
    maxBytes=1_000_000,
    backupCount=5,
    encoding="utf-8",
)
```

Rotation controls file growth and retention shape. It does not make independent multi-process writers safe.

Also define who owns external retention, compression, shipping, or deletion. A rollover setting is not a complete observability-retention policy.

## 44. Timestamps are part of the output contract

Formatters use local time by default for `asctime`.

For systems that require a consistent timezone, a formatter can use UTC conversion:

```python
import logging
import time


formatter = logging.Formatter(
    "%(asctime)sZ %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
formatter.converter = time.gmtime
```

Be explicit about timezone expectations when logs move across machines or regions.

For deterministic tests, avoid asserting the real current timestamp unless time behavior itself is the contract being tested.

## 45. Runtime identity fields are version-sensitive

`LogRecord` includes thread and process fields, and Python 3.12 added `taskName` for `asyncio.Task` names when available.

Before adding a field to every formatter, verify the supported Python versions and whether the value is meaningful for all execution models.

A formatter that blindly requires optional custom context can fail. Use a stable schema or formatter defaults where appropriate.

## 46. `logging.captureWarnings()` can route `warnings` through logging

Python can redirect warnings emitted by the `warnings` module into logging:

```python
import logging


logging.captureWarnings(True)
```

Those warning records use the `py.warnings` logger.

This can unify destinations, but it also changes how warning output is routed. The application should own that decision.

Do not confuse `warnings.warn()` with `logger.warning()`: they serve different APIs and can have different consumers and filtering rules.

## 47. Dynamic socket configuration has a security boundary

`logging.config.listen()` can start a local socket server that receives logging configuration.

That capability is powerful because logging configuration can reference or construct Python objects. Untrusted configuration can therefore become a code-execution risk in environments where another local user or process can send malicious data.

If this mechanism is used, study the `verify` callback and authenticate or reject untrusted configuration bytes.

Do not expose dynamic logging configuration merely because changing verbosity remotely sounds convenient.

## 48. Libraries should document logger names, not seize destinations

A reusable library should tell users which logger namespace it emits under:

```text
examplelib
examplelib.client
examplelib.parser
```

It should normally avoid:

- calling `basicConfig()`;
- attaching visible file, console, email, or network handlers;
- replacing root handlers;
- globally disabling other loggers.

The host application owns destinations and formatting.

This keeps the library composable inside command-line tools, web applications, notebooks, tests, and larger platforms.

## 49. Logging schemas should be stable enough to operate

Even plain-text logs benefit from intentional field names:

```text
operation=import job_id=job-104 records=87
```

Useful contracts define:

- event meaning;
- severity policy;
- stable contextual identifiers;
- privacy classification;
- timestamp and timezone policy;
- destination and retention policy;
- whether machine consumers depend on field names.

Do not turn every prose phrase into a permanent public API, but do not make operationally important fields random either.

## 50. Privacy belongs before formatting

A formatter cannot rescue a record that already contains an unnecessary secret.

Avoid inserting:

- passwords;
- API keys;
- authorization headers;
- session tokens;
- complete personal or payment data;
- raw request or configuration objects containing secrets.

Redaction should be a defense in depth, not permission to collect everything first.

Context mechanisms such as `extra`, adapters, filters, and record factories all need the same privacy review.

## 51. Test semantic logging contracts

Tests should assert behavior that matters.

For example:

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

Prefer checking the record, severity, logger name, or required safe fields over freezing incidental punctuation in the final rendered text.

## 52. Reset logging state carefully in tests

Logging configuration is process-global enough that one test can leak handlers or levels into another.

Possible strategies include:

- configure once for the test process;
- create isolated named loggers and restore changed attributes;
- remove handlers added by a test in cleanup;
- use `basicConfig(force=True)` only when the test intentionally owns root state;
- avoid depending on test execution order.

A passing test suite should not require a lucky logger configuration left behind by an earlier test.

## 53. Practical example: route records with `dictConfig()`

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

Executable version: [`examples/dict_config_routing.py`](examples/dict_config_routing.py).

## 54. Practical example: inject scoped context

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

Executable version: [`examples/context_filter.py`](examples/context_filter.py).

## 55. Practical example: preserve caller attribution

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

Executable version: [`examples/stacklevel_helper.py`](examples/stacklevel_helper.py).

## 56. Practical example: move output behind a queue

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

Executable version: [`examples/queue_listener.py`](examples/queue_listener.py).

## 57. Common mistakes

### Setting only an ancestor logger level and expecting it to filter propagated records

Ancestor logger levels are not re-applied during propagation. Configure the relevant handler level.

### Attaching the same visible handler at several hierarchy levels

Propagation can emit duplicates.

### Calling `basicConfig()` repeatedly and assuming every call reconfigures logging

Without `force=True`, it normally does nothing once the root already has handlers.

### Omitting `disable_existing_loggers` in `dictConfig()`

Pre-existing non-root loggers can be disabled unexpectedly.

### Treating incremental configuration as a full topology replacement

Incremental mode ignores formatter and filter definitions and changes only a limited subset of properties.

### Assuming `Formatter(style="{")` changes logger message interpolation

Formatter style applies to the output format, not ordinary logger-call argument merging.

### Using `extra` keys that collide with `LogRecord`

Built-in attributes are owned by logging.

### Requiring custom formatter fields on records that may not have them

Use a coherent context contract or `Formatter(defaults=...)` where appropriate.

### Creating one logger per request or runtime entity

Use stable logger names plus context fields.

### Hiding the real caller behind a helper

Use `stacklevel` when wrapper attribution should point to its caller.

### Computing expensive diagnostics for disabled levels

Use `isEnabledFor()` around genuinely expensive argument preparation.

### Sending slow I/O directly from latency-sensitive code

Consider `QueueHandler` / `QueueListener`.

### Writing the same file independently from several processes

The standard file handlers do not provide process-shared locking.

### Treating rotation as a concurrency guarantee

Rollover manages files; it does not coordinate unrelated processes.

### Trusting dynamic logging configuration from untrusted senders

Configuration can construct objects and has a security boundary.

### Logging secrets and hoping a formatter removes them later

Do not put unnecessary sensitive data into the record in the first place.

## 58. Exercise: design a logging contract for a worker application

Design a small application with these logger namespaces:

```text
worker
worker.fetch
worker.parse
```

Requirements:

1. use `dictConfig()` with `version=1`;
2. set `disable_existing_loggers=False` explicitly;
3. configure one console handler at `INFO`;
4. configure one second handler that accepts `ERROR` and above;
5. allow `worker.fetch` to emit `DEBUG` records without making unrelated packages globally `DEBUG`;
6. attach a stable `job_id` field to all records for one job;
7. preserve the real caller when using one logging helper;
8. ensure a formatter does not fail when a third-party record lacks `job_id`;
9. avoid duplicate output through propagation;
10. document which component owns logging configuration;
11. explain how you would move slow destination I/O behind a queue;
12. explain what changes if several worker **processes** need to contribute to one file;
13. list at least three fields you intentionally refuse to log for privacy or security reasons.

Then test at least these scenarios:

```text
DEBUG record from worker.fetch
INFO record from worker.parse
ERROR record reaching both intended destinations
third-party WARNING with no job_id
helper call preserving the caller function
exception record with one traceback only
```

The goal is not to create the largest configuration. The goal is to make the routing and context contract explainable.

## 59. Quick reference

| Need | Tool / policy |
|---|---|
| Create module logger | `logging.getLogger(__name__)` |
| Inspect inherited threshold | `logger.getEffectiveLevel()` |
| Check before expensive diagnostics | `logger.isEnabledFor(level)` |
| Set destination threshold | `handler.setLevel(level)` |
| Stop ancestor delivery | `logger.propagate = False` |
| Check hierarchy for handlers | `logger.hasHandlers()` |
| Replace root basic config | `logging.basicConfig(..., force=True)` |
| Configure an object graph | `logging.config.dictConfig()` |
| Preserve existing library loggers | `disable_existing_loggers=False` |
| Change only runtime verbosity incrementally | `incremental=True`, within its limited semantics |
| Add one-call context | `extra={...}` |
| Reuse scoped context | `logging.LoggerAdapter` |
| Merge adapter and per-call context on 3.13+ | `merge_extra=True` |
| Filter or enrich one path | logger/handler filter |
| Replace records in a filter on 3.12+ | return a new `LogRecord` |
| Add process-wide record attributes | `setLogRecordFactory()`, cautiously |
| Carry logical request/task context | `contextvars` |
| Preserve caller through wrapper | `stacklevel=...` |
| Include exception traceback | `exc_info=True` / `logger.exception()` |
| Include current call stack | `stack_info=True` |
| Disable levels process-wide | `logging.disable(level)` |
| Provide custom field fallbacks | `Formatter(defaults=...)` |
| Move slow delivery off caller thread | `QueueHandler` + `QueueListener` |
| Auto-start/stop listener on 3.14+ | `with QueueListener(...)` |
| Rotate by size | `RotatingFileHandler` |
| Rotate by time | `TimedRotatingFileHandler` |
| Route Python warnings into logging | `logging.captureWarnings(True)` |
| Control handler-internal diagnostics | `logging.raiseExceptions` |

## 60. Design checklist

Before publishing a logging configuration, ask:

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

If these questions have explicit answers, the logging system is much easier to operate and maintain.

## 61. Connections to other Python concepts

This chapter combines several earlier topics:

- **modules and packages:** logger names naturally follow module hierarchy;
- **dictionaries:** `dictConfig()` models a configuration graph;
- **objects and classes:** handlers, filters, formatters, adapters, and records collaborate through interfaces;
- **exceptions:** logging failures and application failures have different policies;
- **context managers:** Python 3.14 adds context-manager lifecycle to `QueueListener`;
- **threads and queues:** slow delivery can be decoupled from event creation;
- **processes:** one file needs a deliberate single-writer strategy;
- **context variables:** logical execution context can enrich records without dynamic logger names;
- **testing:** records can be asserted semantically instead of comparing only rendered strings;
- **security:** configuration and log payloads both cross trust boundaries.

This is why advanced logging is less about printing messages and more about designing a reliable event-delivery graph.

## References

- [Python `logging` reference](https://docs.python.org/3/library/logging.html)
- [Python `logging.config` reference](https://docs.python.org/3/library/logging.config.html)
- [Python `logging.handlers` reference](https://docs.python.org/3/library/logging.handlers.html)
- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)

## Next chapter

Continue to [Chapter 06: `collections`](../06-collections/README.md). It studies specialized containers such as `Counter`, `defaultdict`, `deque`, named tuple records, layered mappings, reordering tools, wrapper bases, and collection interfaces as explicit data-structure choices rather than convenience tricks.
