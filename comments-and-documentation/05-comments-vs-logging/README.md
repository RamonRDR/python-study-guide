<div align="center">

# Comments versus Logging in Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: Task markers](../04-task-markers/README.md)

Comments and logs both communicate information, but they speak to different moments. A comment explains the source code to someone reading it. A log records an event that occurred while a program was running.

> **Guiding principle:** Put stable reasoning beside the code. Put changing runtime facts in log records.

## Chapter information

| Item | Details |
|---|---|
| Level | Intermediate |
| Prerequisites | Comments are recommended; basic familiarity with functions, exceptions, and modules is helpful |
| Estimated study time | 55 to 75 minutes |
| Main concepts | comments, `print()`, `logging`, log levels, module loggers, application configuration, handlers, formatters, propagation, exception logging, privacy |

## Learning objectives

By the end of this chapter, you should be able to:

- distinguish source-code explanation from runtime observation;
- choose between a comment, user-facing output, a log record, and an exception;
- use `logging.getLogger(__name__)` in modules;
- select an appropriate standard logging level;
- configure logging at an application entry point;
- keep reusable libraries from taking control of global logging configuration;
- write parameterized messages with useful, non-sensitive context;
- log exceptions without hiding or duplicating error handling;
- recognize duplicate records, excessive noise, and privacy risks;
- review a logging change for clarity and operational value.

## 1. Comments and logs answer different questions

A useful comment answers questions such as:

- Why does this rule exist?
- Which external constraint shaped this implementation?
- Why is the obvious-looking alternative unsafe?
- What stable assumption would a maintainer otherwise miss?

```python
# The partner API returns monetary values in cents.
amount_cents = payload["amount"]
```

A useful log answers questions such as:

- What happened during this execution?
- Which operation started, completed, retried, or failed?
- Which safe identifier helps correlate the event?
- What severity should operators or developers assign to it?

```python
logger.info("Processed invoice invoice_id=%s", invoice_id)
```

Comments remain in the source. Logs are emitted as the program runs and may be filtered, formatted, stored, searched, or forwarded.

## 2. A compact decision table

| Need | Prefer |
|---|---|
| Explain a stable design decision | Comment |
| Document a public module, function, class, or method | Docstring |
| Show a result or instruction directly to a user | `print()` or the application's user-interface layer |
| Record an execution event for diagnosis or operations | Logging |
| Signal that the current operation cannot continue normally | Exception |
| Measure rates, latency, counts, or service health | Metrics |
| Preserve legally controlled or tamper-resistant business history | Purpose-built audit trail |

No single mechanism replaces all the others.

## 3. `print()` is not a defective logger

`print()` is appropriate when text is part of the program's intended user-facing output:

```python
print("Report saved successfully.")
```

A command-line tool may print a table, an answer, or instructions. A graphical application may display the equivalent through widgets. Logging is usually aimed at developers, operators, support teams, or diagnostic systems rather than the end user.

Avoid replacing every `print()` with logging. First decide who the message is for and whether it is part of the program's interface.

## 4. Create a module-level logger

The recommended module pattern is:

```python
import logging


logger = logging.getLogger(__name__)


def process_order(order_id: str) -> None:
    logger.info("Processing order order_id=%s", order_id)
```

Using `__name__` creates logger names that follow the package and module hierarchy. This allows an application to enable, suppress, or route records from specific parts of the program.

Do not instantiate `logging.Logger` directly for ordinary use. Repeated calls to `logging.getLogger()` with the same name return the same logger object.

## 5. The application owns configuration

Most modules should emit records. The application entry point decides:

- the minimum level;
- destinations such as the console, a file, or a remote handler;
- the message format;
- whether timestamps, process names, or correlation identifiers are included;
- different policies for development, tests, and production.

```python
import logging


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
    )
```

Calling `basicConfig()` is convenient for small applications and examples. Larger applications may use `dictConfig()`, command-line options, environment-based settings, or framework configuration.

## 6. Reusable libraries should not seize global configuration

A library does not know how the application wants to route or format logs. This is intrusive:

```python
# Inside a reusable library module:
logging.basicConfig(level=logging.DEBUG)
```

A reusable library should normally:

1. create a logger with `logging.getLogger(__name__)`;
2. emit records at meaningful levels;
3. avoid configuring the root logger or adding visible handlers;
4. optionally attach `logging.NullHandler()` to its top-level logger.

```python
import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
```

`NullHandler` prevents a library from assuming a destination. Records can still propagate to handlers configured by the application.

## 7. Standard logging levels

Python provides five commonly used levels:

| Level | Typical meaning |
|---|---|
| `DEBUG` | detailed diagnostic information useful during investigation |
| `INFO` | expected milestones and meaningful normal operations |
| `WARNING` | an unexpected or degraded situation occurred, but work may continue |
| `ERROR` | an operation failed or produced an unusable result |
| `CRITICAL` | the application or an important subsystem may be unable to continue |

```python
logger.debug("Validated %s columns", column_count)
logger.info("Imported %s records", record_count)
logger.warning("Retrying after timeout attempt=%s", attempt)
logger.error("Could not save report report_id=%s", report_id)
logger.critical("Database is unavailable; stopping worker")
```

These meanings are policies, not mathematical laws. A project should define examples for its own domain so that two developers classify similar events consistently.

## 8. `DEBUG` should reveal detail without becoming a data dump

Useful debug records can expose:

- selected branches or strategies;
- counts and safe dimensions;
- cache hits or misses;
- retry attempts;
- sanitized request or job identifiers.

Avoid logging entire payloads by default. Large objects create noise, cost storage, slow diagnosis, and may expose sensitive information.

A debug record should still be written for a reader, not used as a replacement for understanding the code.

## 9. `INFO` records meaningful normal events

Good `INFO` events often describe boundaries:

- a job started or completed;
- a report was generated;
- a migration processed a batch;
- a configuration version became active;
- an external integration completed successfully.

Do not log every loop iteration at `INFO` merely because logging is available. A high-volume normal event may belong at `DEBUG`, in a metric, or nowhere.

## 10. `WARNING`, `ERROR`, and `CRITICAL` require judgment

Use `WARNING` when the program can continue but the event deserves attention, such as a fallback, retry, deprecated input, or reduced capability.

Use `ERROR` when a specific operation failed. The process may still continue with other work.

Reserve `CRITICAL` for conditions that threaten the application or a major subsystem. If every validation failure is critical, the level stops communicating severity.

The chosen level should match the consequence, not the developer's frustration.

## 11. Log exceptions inside exception handling

`logger.exception()` logs an `ERROR` record and includes the current exception traceback. Call it inside an exception handler:

```python
try:
    save_report(report)
except OSError:
    logger.exception("Could not save report report_id=%s", report.id)
    raise
```

Logging the exception does not decide whether to recover, translate, retry, or re-raise. Error handling and observability are related but separate responsibilities.

Avoid logging the same exception at every layer. If a lower layer logs and re-raises, and every caller logs again, one failure becomes a wall of repeated tracebacks.

## 12. Prefer parameterized logging messages

Write:

```python
logger.info("Processed %s records", record_count)
```

Instead of eagerly formatting every message:

```python
logger.info(f"Processed {record_count} records")
```

The logging call stores the message template and arguments separately and performs interpolation when the record is formatted. Parameterized messages also preserve a stable event shape for readers and some log-processing tools.

Do not use `%` yourself before calling the logger:

```python
logger.info("Processed %s records" % record_count)
```

That performs eager formatting and loses the benefit.

## 13. Include context that helps someone act

A record should make the event understandable without requiring a treasure hunt:

```python
logger.info(
    "Payment authorized order_id=%s provider=%s",
    order_id,
    provider_name,
)
```

Useful context can include:

- stable internal identifiers;
- operation or job names;
- counts and safe units;
- provider or component names;
- retry numbers;
- elapsed time when measured correctly.

Prefer explicit field names such as `order_id=` or `attempt=`. A bare number has weak meaning.

## 14. Never log secrets or unnecessary personal data

This is unsafe:

```python
logger.debug("Authenticated with token=%s", access_token)
```

Do not log:

- passwords, access tokens, API keys, or session cookies;
- complete payment data;
- private customer content;
- personal identifiers without a documented need;
- raw authentication headers;
- secrets hidden inside full request or configuration objects.

Redaction is useful but does not justify collecting data that the log never needed. Logging policy should follow the project's privacy, security, and retention requirements.

## 15. Handlers, formatters, and filters

A log record passes through a small pipeline:

```text
logging call → logger → filters → handler → formatter → destination
```

- **Logger:** creates and routes the record.
- **Handler:** sends accepted records to a destination.
- **Formatter:** converts a record into text or another representation.
- **Filter:** applies additional acceptance rules or adds controlled context.

Small applications may need only `basicConfig()`. Understanding the pieces helps when an application needs a console handler at `INFO`, a file handler at `DEBUG`, or different policies for different packages.

## 16. Propagation and duplicate records

Logger names form a hierarchy. Records usually propagate from a child logger to ancestor handlers.

Duplicate records often appear when the same handler is attached to both a module logger and the root logger:

```python
logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)

root_logger = logging.getLogger()
root_logger.addHandler(stream_handler)
```

Prefer configuring handlers high enough in the hierarchy and letting child loggers propagate naturally.

This can stop propagation:

```python
logger.propagate = False
```

Use it deliberately. Turning propagation off without attaching an appropriate handler may make records disappear.

## 17. Structured context and adapters

Plain text with stable `key=value` fields is often enough for a small project. Applications may also add structured context with `extra`:

```python
logger.info(
    "Started request",
    extra={"request_id": request_id},
)
```

A `LoggerAdapter` can attach repeated context:

```python
request_logger = logging.LoggerAdapter(
    logger,
    {"request_id": request_id},
)
request_logger.info("Started request")
```

Choose field names that do not collide with built-in `LogRecord` attributes. Structured logging libraries and platform integrations may provide richer schemas, but the same privacy and severity principles still apply.

## 18. Logging is not metrics, tracing, or auditing

Logging records discrete events. Other tools answer different questions:

- **Metrics:** How often? How much? How fast?
- **Tracing:** How did one request travel across components?
- **Audit trail:** Who changed a controlled business object, when, and under which policy?
- **Exception reporting:** Which failures need grouping, alerts, and stack analysis?

A project may derive metrics from logs, but relying on prose messages as the only monitoring design is fragile. Security or financial audits usually need stronger guarantees than ordinary application logs provide.

## 19. Testing logging behavior

Tests should focus on meaningful contracts, not incidental punctuation.

Useful assertions include:

- a warning is emitted for a documented fallback;
- a secret never appears;
- a library does not configure the root logger;
- an error record contains the safe identifier needed for diagnosis;
- a noisy debug event is filtered at the production level.

Python's `unittest` provides `assertLogs()`. Pytest projects often use `caplog`. Avoid tests that freeze every word of an internal message unless that wording is itself a supported interface.

## 20. Examples in this repository

| File | Purpose |
|---|---|
| [`comments_vs_logging.py`](examples/comments_vs_logging.py) | Places stable reasoning in a comment and runtime values in a log record |
| [`logging_levels.py`](examples/logging_levels.py) | Emits deterministic examples of the five standard levels |
| [`application_and_library_logging.py`](examples/application_and_library_logging.py) | Shows application-owned configuration and library-style logging |

Run an example from the repository root:

```bash
python comments-and-documentation/05-comments-vs-logging/examples/comments_vs_logging.py
```

On systems where the command is named `python3`:

```bash
python3 comments-and-documentation/05-comments-vs-logging/examples/comments_vs_logging.py
```

## 21. Practical refactoring example

Before:

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

After:

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

The refactoring removes a comment that described a runtime event, replaces diagnostic prints with records, preserves the exception, and includes a safe file name. The correct recovery policy still depends on the application.

## 22. Common mistakes

### Commenting runtime state

A source comment cannot tell you whether today's execution started, retried, or failed.

### Logging stable design reasoning

A log record disappears when the code does not run and should not be the only place that explains a business rule.

### Calling `basicConfig()` in every module

Configuration becomes unpredictable, libraries become intrusive, and tests become harder to isolate.

### Logging and swallowing an exception

A traceback in a log does not make a failed operation successful.

### Logging the same exception repeatedly

One failure becomes several noisy records with little additional value.

### Using `ERROR` for ordinary validation feedback

Severity should match operational consequence.

### Formatting messages eagerly

F-strings are convenient, but parameterized logger calls preserve deferred formatting and a stable template.

### Including secrets for “temporary debugging”

Git history may forget the code change, but log storage may preserve the secret.

### Adding handlers at several hierarchy levels

Propagation can produce duplicates.

### Treating logs as a user interface

Operational records are not a substitute for clear user-facing messages.

## 23. Exercise

Classify and rewrite each line. Decide whether it belongs as a comment, user-facing output, a log record, an exception, or should be removed:

```python
# The job started at runtime.
# TODO: print every processed customer.
print(f"Could not import {file_name}")
logger.info("The tax rate is fixed by regulation.")
logger.error("Customer password=%s", password)
```

For each decision, explain:

1. Who needs the information?
2. Is it stable reasoning or a runtime fact?
3. Which severity is appropriate?
4. Which safe context would make the event actionable?
5. Could the message expose sensitive data?
6. Should the operation continue, recover, or raise an exception?

Then configure a small script with a module logger and verify how changing the configured level affects the records that appear.

## 24. Review checklist

Before accepting a logging change, verify:

- [ ] comments explain stable decisions rather than runtime events;
- [ ] user-facing output remains separate from diagnostics;
- [ ] modules use `logging.getLogger(__name__)`;
- [ ] the application owns handlers, formatters, and global levels;
- [ ] reusable libraries do not call `basicConfig()`;
- [ ] levels match the consequence of each event;
- [ ] messages use parameterized arguments;
- [ ] records include enough safe context to support action;
- [ ] secrets and unnecessary personal data are excluded;
- [ ] exceptions are logged only where the traceback adds value;
- [ ] propagation does not duplicate records;
- [ ] high-volume events do not overwhelm normal logs;
- [ ] logs are not being used as a substitute for metrics, auditing, or error handling.

## 25. Quick-reference summary

| Situation | Preferred approach |
|---|---|
| Stable reason beside an implementation | Comment |
| Public contract of a module or callable | Docstring |
| Intended output for a person using the program | `print()` or UI layer |
| Detailed diagnostic event | `DEBUG` |
| Meaningful normal milestone | `INFO` |
| Recoverable or degraded condition | `WARNING` |
| Failed operation | `ERROR` |
| Major subsystem may not continue | `CRITICAL` |
| Current exception traceback inside `except` | `logger.exception()` |
| Reusable module logger | `logging.getLogger(__name__)` |
| Application-wide destinations and format | Configure at the entry point |
| Repeated context | Parameterized fields, `extra`, or `LoggerAdapter` |
| Passwords, tokens, private payloads | Never log them |

Comments preserve reasoning in the source. Logging preserves selected evidence from execution. Good software needs both, with a clear border between them.

## Official references

- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Python `logging` module reference](https://docs.python.org/3/library/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
