# Concurrency, Parallelism and the GIL

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../13-context-managers/README.md) · [Module index](../README.md) · [Next →](../15-exceptions-testing-and-debugging-review/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [technical-interview-preparation/10-python-memory-management](../../technical-interview-preparation/10-python-memory-management/README.md)
- [technical-interview-preparation/13-context-managers](../../technical-interview-preparation/13-context-managers/README.md)

## Concurrency and parallelism

Concurrency means multiple tasks can make progress over overlapping periods; parallelism means work executes simultaneously. I/O-bound work waits mainly for input/output; CPU-bound work spends time computing. Threads share process memory; processes normally have separate address spaces and require communication or serialization. Asyncio uses cooperative scheduling of coroutines: `async def` creates a coroutine function, calling it produces a coroutine object, and `await` can suspend it so another scheduled task can run. Blocking synchronous work can stall the event loop.

## The GIL in Python 3.13

In conventional CPython builds, the global interpreter lock (GIL) permits only one thread at a time to execute Python bytecode in the same interpreter. I/O and some native extensions release it, so threads can still overlap waiting and native work. It does not make compound application operations atomic or guarantee race-free code. CPython 3.13 also offers an experimental free-threaded build; compatible code can run Python threads in parallel, and some extensions can re-enable the GIL. This is implementation/build-specific, not a Python language guarantee.

| Approach | Good starting point | Trade-off |
| --- | --- | --- |
| Threads | Blocking I/O with thread-safe collaborators | Shared-state synchronization |
| Processes | CPU-heavy pure Python work | Startup, memory, serialization |
| Asyncio | Many cooperative I/O operations | Async-compatible APIs and cancellation |

Measure workloads before choosing; for small sequential work, concurrency may add overhead without benefit.

## Shared-state example

A race condition occurs when behavior depends on unsynchronized interleaving. The shared example uses `Lock` with a context manager around the read-modify-write increment. It waits for all futures and propagates worker exceptions with result. Thread execution order is not asserted. Locks protect a chosen invariant, not arbitrary external accesses; avoid holding locks around slow I/O, and acquire multiple locks in a consistent order to reduce deadlock risk.

## Practice

Run four workers with 250 updates each; expected total is 1000. Test zero updates and invalid counts. Explain why observing a correct result without a lock would not prove safety, and why a lock-protected counter is a correctness demonstration, not a speed benchmark. Use local Python 3.13; threading and process support in a browser runtime is not assumed or verified.

**Quick reference:** concurrency overlaps; parallelism runs simultaneously; GIL depends on build; synchronize shared invariants; choose by workload.

## Shared executable example

[safe_counter.py](examples/safe_counter.py)

`python technical-interview-preparation/14-concurrency-parallelism-and-the-gil/examples/safe_counter.py`

## Official references (Python 3.13)

- [Python 3.13: library/threading.html](https://docs.python.org/3.13/library/threading.html)
- [Python 3.13: howto/free-threading-python.html](https://docs.python.org/3.13/howto/free-threading-python.html)
- [Python 3.13: library/concurrent.futures.html](https://docs.python.org/3.13/library/concurrent.futures.html)
- [Python 3.13: library/asyncio-task.html](https://docs.python.org/3.13/library/asyncio-task.html)

<!-- chapter-navigation:bottom -->
[← Previous](../13-context-managers/README.md) · [Module index](../README.md) · [Next →](../15-exceptions-testing-and-debugging-review/README.md)
<!-- /chapter-navigation:bottom -->
