# Simulated Automation Flow

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Back to Practical Projects](../README.md)

This is **Project 08 of Phase 10: Practical Projects** and the final planned project in the phase.

The project models a small automation orchestrator with real validation, state transitions, logs, evidence, failure propagation, and final-result contracts while keeping every external integration simulated.

The scenario is original and fictional. It does not reproduce any real company, client, system, credential, or private workflow.

## What you will practice

This project combines concepts from the full learning path:

- immutable data modeling with `dataclass`;
- controlled states with `StrEnum`;
- explicit input contracts and normalization;
- deterministic orchestration;
- ordered execution plans;
- fail-fast behavior;
- structured event logs;
- structured evidence;
- invariant validation;
- pure local simulation instead of external integrations;
- stable text rendering;
- pytest regression coverage.

## Fictional scenario

A local request contains a request id and a tuple of fictional work items:

```python
AutomationRequest(
    request_id="DEMO-001",
    items=("alpha", "beta", "gamma"),
)
```

The orchestrator executes four fixed steps:

```text
prepare
   ↓
process
   ↓
verify
   ↓
finalize
```

A successful run publishes uppercase output items. A controlled simulation policy can force one step to fail so the workflow can demonstrate failure propagation without relying on real APIs, files, credentials, schedulers, or remote systems.

## Requirements

The workflow must:

1. accept only a validated `AutomationRequest`;
2. require a printable non-empty request id;
3. require a non-empty tuple of printable work items;
4. trim surrounding whitespace from request ids and items;
5. reject duplicate items after normalization;
6. execute the canonical step order `prepare → process → verify → finalize`;
7. emit deterministic `started` and terminal events for executed steps;
8. produce structured evidence only for successful steps;
9. support deterministic failure injection at exactly one selected step;
10. stop execution after a failure and mark later steps as `skipped`;
11. preserve evidence produced before a failure;
12. publish output only when the complete run succeeds;
13. validate final result invariants even when result objects are constructed directly;
14. render a stable text report without timestamps, randomness, or memory addresses.

## Deliberate scope

The project uses this rule:

> **Real orchestrator, simulated integrations.**

The control flow is real and testable. The outside world is intentionally absent.

Out of scope:

- SAP or any enterprise system;
- HTTP APIs;
- credentials or secrets;
- databases;
- network access;
- subprocess automation;
- GUI or RPA automation;
- threads or `asyncio`;
- schedulers;
- retries and backoff;
- randomness;
- real time delays.

This keeps the learning target on orchestration contracts instead of infrastructure.

## Structure

```text
08-simulated-automation-flow/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── automation_flow.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_automation_flow.py
```

## Core model

### `AutomationRequest`

Stores the immutable validated input:

```python
AutomationRequest("RUN-001", ("alpha", "beta"))
```

The model trims surrounding whitespace, rejects blank or non-printable text, requires a tuple, requires at least one item, and rejects duplicates after normalization.

### `StepName`

The canonical execution plan is fixed:

```text
PREPARE
PROCESS
VERIFY
FINALIZE
```

A fixed order makes execution and tests deterministic.

### `StepStatus`

Each step finishes in exactly one state:

```text
SUCCEEDED
FAILED
SKIPPED
```

A skipped step was not executed because an earlier step failed.

### `RunStatus`

The complete run is either:

```text
SUCCEEDED
FAILED
```

A successful run requires every step to succeed. A failed run requires exactly one failed step, every previous step to have succeeded, and every later step to be skipped.

### `AutomationEvent`

Events act as the deterministic log.

Instead of timestamps, each event receives a contiguous sequence number:

```text
001 prepare started
002 prepare succeeded
003 process started
004 process succeeded
```

This is deliberate. Wall-clock timestamps would make repeated executions differ even when the input is identical.

### `Evidence`

Successful steps produce structured key/value evidence such as:

```text
prepare.input_count=3
process.transformation=uppercase
verify.verification=count-and-uniqueness
finalize.result=ready
```

Failed and skipped steps cannot publish evidence.

### `AutomationResult`

The final immutable result contains:

- the original validated request;
- final run status;
- all four step results;
- the ordered event log;
- published output items when successful.

It also exposes flattened evidence in execution order through the `evidence` property.

## Automation pipeline

```text
input
  ↓
request validation
  ↓
canonical execution plan
  ↓
prepare
  ↓
process
  ↓
verify
  ↓
finalize
  ↓
run status + events + evidence + output
```

If a step fails:

```text
successful earlier steps
          ↓
      failed step
          ↓
   remaining steps
       skipped
          ↓
failed final result
```

Previous evidence remains available, but output is not published.

## Processing contract

For this educational simulation, the `process` step transforms every item to uppercase:

```text
alpha -> ALPHA
beta  -> BETA
```

The transformation is intentionally simple. The project is about the orchestration surrounding the work, not about complex domain logic.

## Controlled failure injection

`SimulationPolicy` can select one step to fail:

```python
SimulationPolicy(fail_at=StepName.VERIFY)
```

The policy is deterministic and explicit. It replaces unreliable techniques such as random failures or artificial timeouts.

Example state sequence:

```text
prepare   -> succeeded
process   -> succeeded
verify    -> failed
finalize  -> skipped
run       -> failed
```

The evidence from `prepare` and `process` is preserved.

## Basic example

```python
from automation_flow import AutomationRequest, run_automation

request = AutomationRequest(
    request_id="RUN-001",
    items=("alpha", "beta"),
)

result = run_automation(request)

print(result.status)
print(result.output_items)
```

Logical output:

```text
succeeded
('ALPHA', 'BETA')
```

## Demo

Run from this directory:

```bash
python demo.py
```

The demo executes two deterministic scenarios:

1. a complete successful run;
2. a controlled failure at `verify`.

It is non-interactive, network-free, and uses only fictional in-memory data.

## Failure paths

Invalid input fails before orchestration begins:

```python
AutomationRequest("", ("alpha",))
```

raises `ValueError`.

```python
AutomationRequest("RUN-001", [])
```

raises `TypeError` because mutable lists are not silently accepted.

```python
AutomationRequest("RUN-001", (" alpha ", "alpha"))
```

raises `ValueError` because normalization would create a duplicate.

A simulated runtime failure is different from invalid input. It returns a valid `AutomationResult` with `RunStatus.FAILED`.

That distinction is important:

- **invalid contract** → exception;
- **valid request with execution failure** → structured failed result.

## Result invariants

The result object validates its own consistency.

Examples of impossible states that are rejected:

- success with a failed step;
- failure without exactly one failed step;
- a successful step after a failed step;
- published output from a failed run;
- wrong step order;
- non-contiguous event sequence numbers;
- event lifecycles that do not match step statuses;
- evidence attached to failed or skipped steps.

The goal is to make invalid states difficult to represent.

## Common mistakes

### Using `print()` as the only log

Printed text is useful for humans but weak as a program contract. Store structured events first, then render them.

### Adding real timestamps to a deterministic exercise

Time makes equality tests noisy. Sequence numbers communicate order without adding nondeterminism.

### Continuing after failure without a declared policy

If later steps depend on earlier output, silently continuing can create misleading results. This project uses explicit fail-fast behavior.

### Losing earlier evidence

Failure should not erase what already succeeded. Preserving prior evidence makes the run explainable.

### Mixing validation failures with runtime failures

Bad input should raise immediately. A valid request that fails during execution should produce a structured failed result.

### Simulating external systems too literally

Fake credentials, fake SAP screens, sleeps, and network mocks can distract from the actual lesson. This project models the orchestration boundary instead.

## Tests

Run the focused suite from the repository root:

```bash
python -m pytest -q practical-projects/08-simulated-automation-flow/tests
```

The initial suite covers:

- request normalization and duplicate rejection;
- immutable input boundaries;
- deterministic success;
- all four injectable failure points;
- fail-fast and skipped-step semantics;
- preservation of earlier evidence;
- output publication rules;
- result invariant validation;
- contiguous event sequencing;
- explicit runtime type contracts;
- stable text rendering.

## Exercise

Change the demo request to:

```python
("north", "south", "west", "east")
```

Before running it, predict:

1. `input_count`;
2. `processed_count`;
3. the final output tuple;
4. the number of events in a successful run.

Then inject a failure at `PROCESS` and predict which steps will be skipped and which evidence will remain.

## Extension challenges

After the base contract is clear, try one extension at a time:

1. Add a fifth step and update the lifecycle invariants.
2. Replace uppercase transformation with a configurable pure processing function.
3. Add a retry policy while keeping event order deterministic.
4. Add per-step durations supplied by a fake clock instead of reading real time.
5. Add JSON serialization for the final result.
6. Add an alternate renderer without changing orchestration logic.
7. Add dependency-aware steps instead of one fixed linear chain.

## Portfolio discussion

This project demonstrates how to model automation as software contracts rather than as a sequence of ad-hoc side effects.

Useful points to explain in a portfolio:

- explicit orchestration state;
- immutable request and result models;
- deterministic execution;
- structured logs and evidence;
- fail-fast propagation;
- skipped-step semantics;
- distinction between validation and runtime failure;
- invariant-driven design;
- safe simulation boundaries;
- regression testing of both success and failure paths.

## Quick reference

```text
Input:        AutomationRequest
Steps:        prepare -> process -> verify -> finalize
Processing:   uppercase transformation
Step states:  succeeded / failed / skipped
Run states:   succeeded / failed
Logs:         ordered AutomationEvent values
Evidence:     successful steps only
Failure:      deterministic injection through SimulationPolicy
After failure: remaining steps are skipped
Output:       published only after complete success
External I/O: none
```

## Phase 10 finish line

This is the final planned practical project in Phase 10. Once its implementation, documentation, CI checks, and review cycle are complete, the practical-project phase can be marked complete.
