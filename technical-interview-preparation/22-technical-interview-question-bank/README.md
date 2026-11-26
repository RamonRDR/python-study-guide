# Technical Interview Question Bank

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../21-software-engineering-and-technical-decisions/README.md) · [Module index](../README.md)
<!-- /chapter-navigation:top -->

Nine pilot questions: three junior, three mid-level and three senior. Level indicates expected depth, not a universal hiring standard. Study the linked prerequisite section first, answer aloud without revealing the reference, then open the answer. Award each criterion its stated points only if your response demonstrates it; otherwise award zero. Use the score to identify study gaps, not as certification or automatic semantic evaluation. Follow-ups are optional practice, not separately scored. The canonical JSON records and index are in [interviews](../../interviews/README.md); this section is generated from them. The full technical bank and mocks are planned.

## Pilot questions

<!-- interview-questions:start -->
### interview.clarify-contract

`junior` · `interview-fundamentals`

An interviewer asks you to count eligible registrations. Eligibility, duplicate handling and empty input are unspecified. What do you do before coding?

<details>
<summary>Expected answer</summary>

Ask what qualifies, whether duplicates count and the empty-input result. Restate the agreed contract, give a concrete example and explain how you will test it before implementing.

**Explanation:** Clarification prevents solving a different problem. If a rule remains unknown, label an assumption and ask for confirmation.

**Interviewer intent:** Assess communication, contract reasoning and test planning, not speed alone.

**Common errors**

- Start coding without defining eligibility.
- Invent a duplicate policy and present it as given.

**Follow-ups**

- How would a change from counting rows to counting distinct IDs affect your tests?

**Example**

If the agreed rule counts distinct eligible IDs, two eligible rows with ID 7 count as one and empty input returns zero if agreed.

**Self-assessment rubric**

- 1 — Asks explicitly about eligibility, duplicates and empty input.
- 1 — Restates the contract and distinguishes assumptions from facts.
- 1 — Provides a concrete example and at least one relevant test.

Maximum: 3

</details>

**Prerequisites**

- [A practical conversation](../../technical-interview-preparation/01-understanding-technical-interviews/README.md)

### python.mutable-default

`junior` · `python-fundamentals`

Given `def add(x, items=[]): items.append(x); return items`, what do `print(add(1)); print(add(2))` display on consecutive calls? Fix the omitted-list behavior.

<details>
<summary>Expected answer</summary>

The prints are `[1]` and `[1, 2]`. The default list is created when the function is defined and reused. Default to None, then create a new list only when items is None.

**Explanation:** Assignment binds objects; the shared default is mutated. Explicitly supplied lists still mutate under this contract.

**Interviewer intent:** Assess evaluation time, mutability and intended ownership.

**Common errors**

- Assume a fresh list is created on every call.
- Use `if not items` and replace an explicitly supplied empty list.

**Follow-ups**

- What changes if the caller supplies an empty list?

**Example**

```python
def add(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
```

**Self-assessment rubric**

- 1 — Predicts both printed lists correctly.
- 1 — Explains one-time default evaluation and shared mutation.
- 1 — Uses None and an identity check without replacing a supplied empty list.

Maximum: 3

</details>

**Prerequisites**

- [Review by reasoning](../../technical-interview-preparation/03-python-fundamentals-review/README.md)

### algorithms.duplicate-membership

`junior` · `data-structures-algorithms`

Detect whether a list of hashable IDs contains a duplicate. Which structure would you choose, and what are the time and auxiliary-space costs?

<details>
<summary>Expected answer</summary>

Keep a set of seen IDs. For each ID, return True if already seen, otherwise insert it. Return False at the end. Under ordinary average-case hashing and constant-cost hash/equality assumptions, time is O(n), extra space O(n) in the worst input size.

**Explanation:** A set supports membership without repeatedly scanning the prefix. Worst-case hash collisions can degrade time; hashability is a prerequisite.

**Interviewer intent:** Assess representation choice, correctness and complexity assumptions.

**Common errors**

- Claim guaranteed O(1) worst-case set lookup.
- Forget empty input or treat equal IDs as different because of position.

**Follow-ups**

- What if IDs are not hashable?

**Example**

`[3, 8, 3]` → True; `[]` → False; `[3, 8]` → False.

**Self-assessment rubric**

- 1 — Describes a seen-set algorithm with correct termination.
- 1 — States average O(n) time with hashing assumptions and O(n) extra space.
- 1 — Checks empty and repeated input and states hashability requirement.

Maximum: 3

</details>

**Prerequisites**

- [Choose by the contract](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.md)

### oop.replaceable-collaborator

`mid` · `oop`

A report notifier must support text and email channels, then a fake channel in tests. Compare inheritance and composition; propose a design without changing the notifier for each channel.

<details>
<summary>Expected answer</summary>

Inject a collaborator with a defined send contract; the notifier delegates to it. Compatible channels may subclass a base or satisfy the behavior through duck typing. Inheritance is useful for genuine subtypes that honor the base contract, not merely reuse.

**Explanation:** Composition makes dependencies explicit and replaceable, at the cost of indirection. Method names alone do not ensure substitutability.

**Interviewer intent:** Assess behavioral contracts and testable design decisions.

**Common errors**

- Require a deep inheritance tree just to reuse code.
- Assume every method named send has the same semantics.

**Follow-ups**

- What should a fake channel demonstrate about the contract?

**Example**

`Notifier(channel)` delegates `send('Ready')` to a fake returning `test: Ready`, without contacting a network.

**Self-assessment rubric**

- 1 — Proposes explicit collaborator injection and delegation.
- 1 — Distinguishes subtype contract from composition and duck typing.
- 1 — Explains a fake-based test and at least one trade-off.

Maximum: 3

</details>

**Prerequisites**

- [Polymorphism and composition](../../technical-interview-preparation/07-inheritance-polymorphism-and-composition/README.md)

### internals.nested-copy

`mid` · `python-internals`

A dictionary contains two keys referencing the same mutable list. You need an independent graph while preserving the alias relationship inside the copy. Compare assignment, shallow copy and deep copy.

<details>
<summary>Expected answer</summary>

Assignment shares the original dictionary; shallow copy creates a new outer dictionary but shares the list. For these built-in containers, deepcopy copies the nested list once and reuses that copy for both keys via its memo.

**Explanation:** Deep copying can preserve repeated references and cycles; it does not guarantee cloning every object or external resource. Choose by ownership and cost.

**Interviewer intent:** Assess identity, nested aliasing and copy semantics.

**Common errors**

- Assume a shallow copy isolates nested mutable values.
- Claim deepcopy creates a new object for every reference.

**Follow-ups**

- How would you test that mutating the copied list does not affect the original?

**Example**

```python
from copy import deepcopy
shared = [1]
original = {"a": shared, "b": shared}
cloned = deepcopy(original)
assert cloned["a"] is cloned["b"]
assert cloned["a"] is not shared
```

**Self-assessment rubric**

- 1 — Correctly contrasts assignment and shallow copy.
- 1 — Explains deepcopy memo and preserved alias identity.
- 1 — Proposes identity/mutation checks and states copying limitations.

Maximum: 3

</details>

**Prerequisites**

- [Identity, equality and binding](../../technical-interview-preparation/09-object-identity-references-and-copying/README.md)

### sql.zero-child-count

`mid` · `databases-sql`

Given groups(id, name) and tasks(id, group_id, done), return the count of completed tasks per group, including groups with no completed tasks. How do ON, WHERE and COUNT affect correctness?

<details>
<summary>Expected answer</summary>

LEFT JOIN tasks on the group ID with done = 1 in ON; group by the group ID and name, count tasks.id (non-null for actual tasks). WHERE tasks.done = 1 would discard null-extended rows; COUNT(*) would count the unmatched row.

**Explanation:** Group by stable identity even if display names repeat. A filter inside ON controls matches without dropping left-side groups.

**Interviewer intent:** Assess join semantics, aggregation grain and zero-case reasoning.

**Common errors**

- Use INNER JOIN or filter completed tasks in WHERE.
- Group only by nonunique name or count all joined rows.

**Follow-ups**

- What happens if two groups have the same name?

**Example**

```sql
SELECT g.id, g.name, COUNT(t.id)
FROM groups AS g LEFT JOIN tasks AS t
ON g.id = t.group_id AND t.done = 1
GROUP BY g.id, g.name
ORDER BY g.id;
```

**Self-assessment rubric**

- 1 — Uses LEFT JOIN on keys and places completed filter in ON.
- 1 — Counts non-null child ID and explains zero-count behavior.
- 1 — Groups by stable identity and explains why name-only grouping fails.

Maximum: 3

</details>

**Prerequisites**

- [Relationships and join cardinality](../../technical-interview-preparation/19-joins-aggregations-and-data-relationships/README.md)

### internals.gil-workload

`senior` · `python-internals`

A CPython 3.13 service performs many blocking I/O operations, CPU-heavy pure Python transformations and increments a shared counter. Propose concurrency choices and a verification plan; account for conventional and experimental free-threaded builds.

<details>
<summary>Expected answer</summary>

Conventional GIL-enabled CPython allows one thread to execute Python bytecode at a time in an interpreter. Threads suit blocking I/O; asyncio suits cooperative I/O with compatible APIs; processes may benefit CPU-heavy Python at serialization/memory cost. The experimental free-threaded build can allow parallel Python threads; some extensions may re-enable the GIL. Synchronize the counter with a shared lock and measure throughput, resource costs and correctness on the actual build.

**Explanation:** The GIL is implementation-specific and not an application-level race-freedom guarantee. A single correct total without synchronization is weak evidence; test the lock contract and failure propagation separately from performance.

**Interviewer intent:** Assess conditional architectural reasoning, version awareness and validation of invariants.

**Common errors**

- Claim threads never help in Python or that the GIL makes all updates safe.
- Assume free-threading is the default or guarantees a speedup.

**Follow-ups**

- Why is a correct counter result in one unsynchronized run not a proof of safety?

**Example**

Compare sequential baseline, bounded threads for blocking I/O and processes for CPU work; record elapsed time and memory separately from a locked-counter correctness check.

**Self-assessment rubric**

- 1 — Distinguishes conventional GIL from experimental free-threading with extension caveat.
- 1 — Chooses I/O/CPU strategies with at least one trade-off and actual workload measurement.
- 1 — Protects shared invariant and distinguishes correctness tests from benchmarks.

Maximum: 3

</details>

**Prerequisites**

- [The GIL in Python 3.13](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.md)

### api.object-authorization

`senior` · `backend-apis`

An authenticated learner can request a note by ID. Design access checks and response policy to prevent reading another learner's note; explain existence leakage and regression tests.

<details>
<summary>Expected answer</summary>

Authenticate using a trusted verified identity, then authorize the action on the specific object using server-controlled ownership or policy before returning content. Missing valid credentials yield 401 with a challenge. Forbidden access can yield 403, or 404 under a consistent concealment policy. Never trust a supplied owner or unverified token. Test missing credentials, allowed owner, authenticated non-owner, nonexistent ID and denial body without protected data.

**Explanation:** 403 versus 404 can disclose existence. Concealment requires a consistent policy; it does not replace authorization. The local example models a post-authentication boundary, not token verification.

**Interviewer intent:** Assess object-level access control, error contract and negative security tests.

**Common errors**

- Check only whether the caller is logged in.
- Return note content with a denial or trust the client-supplied owner.

**Follow-ups**

- How would you change tests if policy intentionally hides resource existence?

**Example**

For note 7 owned by learner A, authenticated B gets 403 (or policy-defined 404) and no note content; A gets 200; anonymous callers get 401.

**Self-assessment rubric**

- 1 — Requires verified server-side identity plus per-object authorization.
- 1 — Explains 401/403/404 and consistent existence-disclosure policy.
- 1 — Specifies positive and negative tests including unauthorized body confidentiality.

Maximum: 3

</details>

**Prerequisites**

- [Authentication versus authorization](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.md)

### engineering.architecture-tradeoffs

`senior` · `software-engineering`

A small reporting service has slow requests. A colleague proposes splitting it into services and adding a cache. How would you decide, measure and roll out changes safely?

<details>
<summary>Expected answer</summary>

Define latency/reliability targets and measure a baseline with logs, metrics and traces to locate the bottleneck. Compare a modular monolith and services against independent scaling/deployment and network/operational cost. Consider cache only with explicit staleness, invalidation and memory constraints. Record alternatives and consequences in an ADR, test acceptance criteria, use focused reviewed changes and plan measured rollout and rollback, including data compatibility.

**Explanation:** Architecture labels do not establish performance. Evidence and quality constraints determine whether additional complexity is justified.

**Interviewer intent:** Assess technical judgment, measurable decisions and operational risk.

**Common errors**

- Assume microservices or caches automatically improve latency.
- Ignore cache staleness or assume code rollback reverses data migrations.

**Follow-ups**

- What evidence would justify keeping the current design instead?

**Example**

If measurements locate repeated expensive reads and the contract permits bounded staleness, evaluate a small cache against the baseline; reject it if invalidation or memory cost exceeds the agreed budget.

**Self-assessment rubric**

- 1 — Defines measurable baseline and investigates bottleneck before choosing.
- 1 — Compares service and cache trade-offs against constraints.
- 1 — Proposes documented decision, acceptance tests and rollback including data concerns.

Maximum: 3

</details>

**Prerequisites**

- [Trade-offs and operation](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.md)

<!-- interview-questions:end -->

<!-- chapter-navigation:bottom -->
[← Previous](../21-software-engineering-and-technical-decisions/README.md) · [Module index](../README.md)
<!-- /chapter-navigation:bottom -->
