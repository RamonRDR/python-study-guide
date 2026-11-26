# Technical Interview Question Bank

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../21-software-engineering-and-technical-decisions/README.md) · [Module index](../README.md) · [Next →](../23-behavioral-and-international-interviews/README.md)
<!-- /chapter-navigation:top -->

60 interview questions: 24 junior, 24 mid-level and 12 senior, including the original nine pilot questions and three behavioral/international questions. Browse by topic and level; question IDs remain stable across ordering changes. Level indicates expected depth, not a universal hiring standard. Study the linked prerequisite section first, answer aloud without revealing the reference, then open the answer. Award each criterion its stated points only if your response demonstrates it; otherwise award zero. Use the score to identify study gaps, not as certification or automatic semantic evaluation. Follow-ups are optional practice, not separately scored. The canonical JSON records and index are in [interviews](../../interviews/README.md); this section is generated from them. Study [behavioral and international interviews](../23-behavioral-and-international-interviews/README.md) before those questions, and then try the [timed mocks](../24-mock-interviews-and-self-assessment/README.md).

<!-- interview-questions:start -->
## Coverage

| Topic | Junior | Mid-level | Senior | Total |
| --- | ---: | ---: | ---: | ---: |
| Interview fundamentals | 3 | 2 | 1 | 6 |
| Python fundamentals | 4 | 3 | 1 | 8 |
| Data structures and algorithms | 3 | 3 | 1 | 7 |
| Object-oriented programming | 3 | 3 | 2 | 8 |
| Python internals | 2 | 4 | 2 | 8 |
| Testing and debugging | 3 | 3 | 1 | 7 |
| Backend and APIs | 2 | 2 | 1 | 5 |
| Databases and SQL | 2 | 2 | 1 | 5 |
| Software engineering | 1 | 1 | 1 | 3 |
| Behavioral and international interviews | 1 | 1 | 1 | 3 |

## Interview fundamentals

### interview.allowed-tools

`junior` · `interview-fundamentals`

Before a take-home, what must you confirm about scope, delivery and AI tools? What if AI is forbidden?

<details>
<summary>Expected answer</summary>

Confirm deadline, scope, format, criteria and permitted tools. If AI is forbidden, do not use it; if permitted, disclose as required.

**Explanation:** Rules differ between employers; ask rather than infer.

**Interviewer intent:** Assess respect for assessment constraints.

**Common errors**

- Assume the previous employer's tool policy still applies.

**Follow-ups**

- What would you ask if the allowed documentation is unclear?

**Example**

If instructions permit the standard library documentation but forbid AI, consult the documentation only.

**Self-assessment rubric**

- 1 — Identifies deadline, scope, format, criteria and tool policy.
- 1 — Respects the prohibition or disclosure requirement.

Maximum: 2

</details>

**Prerequisites**

- [Purpose and process](../../technical-interview-preparation/01-understanding-technical-interviews/README.md)
- [Take-home assignments](../../technical-interview-preparation/02-live-coding-and-take-home/README.md)

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

### interview.live-coding-start

`junior` · `interview-fundamentals`

How do you start a timed coding task before typing the solution? Describe a small trace and how you communicate.

<details>
<summary>Expected answer</summary>

Read and restate the contract, trace a small example, choose a straightforward approach, then implement and test while explaining decisions.

**Explanation:** A trace exposes assumptions before implementation; narrate decisions, not keystrokes.

**Interviewer intent:** Assess process under time pressure.

**Common errors**

- Type an optimized solution before checking the contract.

**Follow-ups**

- What if the trace contradicts the stated contract?

**Example**

For a sum of nonnegative quantities, trace [2, 0, 3] to 5 after confirming zero is allowed.

**Self-assessment rubric**

- 1 — Restates contract and traces a concrete example.
- 1 — Chooses a simple approach and describes implementation/test decisions aloud.

Maximum: 2

</details>

**Prerequisites**

- [Live coding](../../technical-interview-preparation/02-live-coding-and-take-home/README.md)

### interview.incomplete-live-task

`mid` · `interview-fundamentals`

Time is almost over; your solution handles typical inputs but an edge case fails. How do you report status and prioritize the remaining work?

<details>
<summary>Expected answer</summary>

State which behavior was verified and which fails; isolate a minimal failing case, attempt a small verifiable correction if time permits, and explain the next test and limitation.

**Explanation:** A precise partial result is stronger evidence than an unsupported completion claim.

**Interviewer intent:** Assess prioritization and honest evidence.

**Common errors**

- Say all tests pass because the happy path works.

**Follow-ups**

- How would you communicate a failed correction?

**Example**

A function passes [2,3] but fails []; report the failure and test the agreed empty-input result next.

**Self-assessment rubric**

- 1 — Distinguishes verified behavior, failure and unverified work.
- 1 — Proposes a minimal reproducible case and next verification step.

Maximum: 2

</details>

**Prerequisites**

- [Live coding](../../technical-interview-preparation/02-live-coding-and-take-home/README.md)

### interview.take-home-evidence

`mid` · `interview-fundamentals`

For a small take-home, what should the submission README and tests demonstrate? Explain how you avoid unsupported claims.

<details>
<summary>Expected answer</summary>

Document requirements, assumptions, setup/run commands, tests actually executed and known limitations. Include normal, empty and invalid inputs against the agreed contract and explain complexity.

**Explanation:** A reviewer should be able to reproduce evidence without secrets or proprietary code.

**Interviewer intent:** Assess reproducibility and delivery discipline.

**Common errors**

- Add speculative features while leaving setup undocumented.

**Follow-ups**

- What would you record if an integration test cannot run locally?

**Example**

For sum of nonnegative integers, record the zero policy, one invalid-input test and the actual test command.

**Self-assessment rubric**

- 1 — Includes reproducible instructions, explicit assumptions and actual test evidence.
- 1 — Describes boundary cases, complexity and limitations without false claims.

Maximum: 2

</details>

**Prerequisites**

- [Take-home assignments](../../technical-interview-preparation/02-live-coding-and-take-home/README.md)

### interview.scope-prioritization

`senior` · `interview-fundamentals`

A take-home requests a small working service in two hours; optional features are ambiguous. How would you agree priorities, choose a deliverable and communicate risk?

<details>
<summary>Expected answer</summary>

Confirm acceptance criteria, deadline and permitted tools; separate required behavior from optional work. Deliver a small tested implementation with documented assumptions, evidence and explicit deferred risks rather than expanding scope.

**Explanation:** A constrained delivery trades breadth for verified behavior; the interviewer must know what was not implemented.

**Interviewer intent:** Assess judgment about scope and evidence.

**Common errors**

- Promise a complete architecture without validating the core behavior.

**Follow-ups**

- How would you respond to a new requirement halfway through?

**Example**

Prioritize validated calculation and run instructions over an unrequested UI; explicitly defer the UI.

**Self-assessment rubric**

- 1 — Prioritizes explicit acceptance criteria and agrees assumptions with the evaluator.
- 1 — Justifies scope trade-off and communicates tested outcomes and deferred risk.

Maximum: 2

</details>

**Prerequisites**

- [Purpose and process](../../technical-interview-preparation/01-understanding-technical-interviews/README.md)
- [Take-home assignments](../../technical-interview-preparation/02-live-coding-and-take-home/README.md)

## Python fundamentals

### python.binding-vs-copy

`junior` · `python-fundamentals`

Given a = [1]; b = a; b.append(2), what are a and b? Explain whether assignment copies the list.

<details>
<summary>Expected answer</summary>

Both are [1, 2]; a and b name the same mutable list. Assignment binds a name and does not copy the object.

**Explanation:** Mutating through one reference is visible through the other.

**Interviewer intent:** Assess aliasing and list mutation.

**Common errors**

- Treat b = a as an independent list.

**Follow-ups**

- What changes if b is then rebound to []?

**Example**

After `a = [1]; b = a`, the expression `a is b` evaluates to `True` before rebinding `b`.

**Self-assessment rubric**

- 1 — Predicts both list values.
- 1 — Explains shared identity and mutation rather than copying.

Maximum: 2

</details>

**Prerequisites**

- [Review by reasoning](../../technical-interview-preparation/03-python-fundamentals-review/README.md)
- [Identity, equality and binding](../../technical-interview-preparation/09-object-identity-references-and-copying/README.md)

### python.conversion-contract

`junior` · `python-fundamentals`

What happens with int("12") and int("twelve")? Explain why the type and input content matter.

<details>
<summary>Expected answer</summary>

The first returns integer 12; the second raises ValueError because the text does not represent an integer accepted by int.

**Explanation:** Conversion is an operation with an input contract, not a guarantee that all strings succeed.

**Interviewer intent:** Assess type conversion and failure reasoning.

**Common errors**

- Assume failed conversion returns zero or None.

**Follow-ups**

- What would you test for an empty string?

**Example**

int("0") returns 0; int("") raises ValueError.

**Self-assessment rubric**

- 1 — Predicts the value and type of the successful conversion.
- 1 — Identifies ValueError and explains the input constraint.

Maximum: 2

</details>

**Prerequisites**

- [Review by reasoning](../../technical-interview-preparation/03-python-fundamentals-review/README.md)

### python.immutable-string

`junior` · `python-fundamentals`

Given s = "python"; s.upper(); print(s), what is printed? How do you retain the uppercase value?

<details>
<summary>Expected answer</summary>

It prints python. Strings are immutable; upper returns a string result. Assign s = s.upper() to bind s to the uppercase result.

**Explanation:** Calling a method does not imply mutation; inspect the contract.

**Interviewer intent:** Assess return values and immutability.

**Common errors**

- Expect upper to modify the original string in place.

**Follow-ups**

- What remains bound to an alias of the original string?

**Example**

s = "hi"; t = s.upper() leaves s equal to "hi" and t equal to "HI".

**Self-assessment rubric**

- 1 — Predicts the original output and explains immutability.
- 1 — Shows assignment of the returned result.

Maximum: 2

</details>

**Prerequisites**

- [Review by reasoning](../../technical-interview-preparation/03-python-fundamentals-review/README.md)

### python.mutable-default

`junior` · `python-fundamentals`

Given `def add(x, items=[]): items.append(x); return items`, what do `print(add(1)); print(add(2))` display on consecutive calls? Fix the omitted-list behavior. Preserve mutation of explicitly supplied lists, including an empty list.

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

### python.identity-none

`mid` · `python-fundamentals`

Compare x == y and x is y for two independently created lists [1]. Why is is None appropriate but is unreliable for value comparison of strings?

<details>
<summary>Expected answer</summary>

Equality is True and identity is False. == compares equality semantics; is compares object identity. None is a singleton, so identity is the intended test; string caching is not a value-equality contract.

**Explanation:** Two distinct objects can compare equal. Identity behavior for cached values is implementation-dependent.

**Interviewer intent:** Assess identity versus equality.

**Common errors**

- Use is to compare integer or string values.

**Follow-ups**

- What happens when y is assigned x?

**Example**

Given `x = [1]; y = [1]`, the expression `x == y` evaluates to `True`, while `x is y` evaluates to `False`.

**Self-assessment rubric**

- 1 — Predicts identity and equality for separate lists.
- 1 — Explains None singleton and value comparison rule.

Maximum: 2

</details>

**Prerequisites**

- [Independent practice](../../technical-interview-preparation/03-python-fundamentals-review/README.md)
- [Identity, equality and binding](../../technical-interview-preparation/09-object-identity-references-and-copying/README.md)

### python.parameter-rebinding

`mid` · `python-fundamentals`

A function receives items=[1] from a caller, then assigns items = [9] locally. Contrast this with items.append(9). What does the caller see?

<details>
<summary>Expected answer</summary>

Rebinding the local parameter does not change the caller's list or binding; the caller still sees [1]. Appending to the shared list instead changes it to [1, 9].

**Explanation:** Parameters are local names bound to supplied objects; distinguish a binding change from an object change.

**Interviewer intent:** Assess function boundary and ownership reasoning.

**Common errors**

- Describe Python arguments simply as copied values or caller-variable references.

**Follow-ups**

- How would you return a new list while preserving the original?

**Example**

def f(items): items = [9] leaves the original list unchanged.

**Self-assessment rubric**

- 1 — Predicts the result of local rebinding.
- 1 — Predicts shared mutation and explains why it differs.

Maximum: 2

</details>

**Prerequisites**

- [Review by reasoning](../../technical-interview-preparation/03-python-fundamentals-review/README.md)
- [Identity, equality and binding](../../technical-interview-preparation/09-object-identity-references-and-copying/README.md)

### python.scope-lookup

`mid` · `python-fundamentals`

Explain LEGB lookup and what nonlocal changes when an inner function updates an enclosing counter. Contrast with rebinding an unrelated local variable.

<details>
<summary>Expected answer</summary>

LEGB searches local, enclosing function scopes, global module and builtins for an ordinary unqualified name. nonlocal permits rebinding an existing enclosing function binding; normal local assignment does not update that binding.

**Explanation:** A closure can retain enclosing state between calls. nonlocal is not the global declaration.

**Interviewer intent:** Assess scope and binding semantics.

**Common errors**

- Use global when the counter belongs to an enclosing function.

**Follow-ups**

- Why can two factory calls have separate counters?

**Example**

An inner increment with nonlocal count updates the count retained by its own outer call.

**Self-assessment rubric**

- 1 — Names the four LEGB scopes in order.
- 1 — Explains existing enclosing binding and contrasts with local rebinding.

Maximum: 2

</details>

**Prerequisites**

- [Review by reasoning](../../technical-interview-preparation/03-python-fundamentals-review/README.md)
- [Closures and scope](../../technical-interview-preparation/12-closures-and-decorators/README.md)

### python.hash-equality-contract

`senior` · `python-fundamentals`

You design a value-equality class for dictionary keys. What hash/equality contract must hold, what risk arises if equality-relevant state changes, and how would you test it?

<details>
<summary>Expected answer</summary>

Equal objects must have equal hashes and hashes must remain stable over their lifetime as hashable objects; unequal objects may collide. Prefer stable immutable equality state for keys or make mutable value-equality objects unhashable. Test equal distinct instances, lookup through an equal key and the supported mutation policy.

**Explanation:** Changing a key hash can invalidate dictionary lookup; defining __eq__ without __hash__ normally makes a Python class unhashable.

**Interviewer intent:** Assess invariant design and tests, not hash uniqueness.

**Common errors**

- Demand different hashes for every unequal pair.

**Follow-ups**

- Why is a tuple containing a list not a usable dictionary key?

**Example**

Two distinct equal immutable key objects must retrieve the same associated value; test without assuming distinct unequal hashes.

**Self-assessment rubric**

- 1 — States equal-hash and lifetime stability rules and allows collisions.
- 1 — Explains mutable-key risk and proposes equality, lookup and mutation-policy tests.

Maximum: 2

</details>

**Prerequisites**

- [Equality and hashing](../../technical-interview-preparation/09-object-identity-references-and-copying/README.md)

## Data structures and algorithms

### algorithms.binary-precondition

`junior` · `data-structures-algorithms`

Why is binary search inappropriate for an arbitrary unsorted list? Compare with linear search and state the sorted random-access cost.

<details>
<summary>Expected answer</summary>

Binary search discards half of the remaining positions using ascending order. Without that order, the target may be discarded. Linear search works on unsorted input in O(n) worst-case time; binary search on sorted random-access input needs O(log n) comparisons.

**Explanation:** The ordered-data invariant justifies elimination.

**Interviewer intent:** Assess algorithm preconditions.

**Common errors**

- Assume binary search is valid on any list.

**Follow-ups**

- Would validating sortedness for each lookup preserve logarithmic total cost?

**Example**

In [9,1,3], comparison with the middle value cannot safely eliminate the left side when searching for 9.

**Self-assessment rubric**

- 1 — States sortedness and explains safe elimination.
- 1 — Compares worst-case linear and binary search costs under the stated assumptions.

Maximum: 2

</details>

**Prerequisites**

- [Choose by the contract](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.md)
- [2. Binary search](../../problem-solving-and-live-coding/05-searching-algorithms/README.md)

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

### algorithms.frequency-map

`junior` · `data-structures-algorithms`

How would you count occurrences of each hashable label in a list? Show the result for [a,a,b] and explain the choice of structure.

<details>
<summary>Expected answer</summary>

Use a dictionary from label to count, updating count with get(label, 0) + 1. The result is {"a": 2, "b": 1}.

**Explanation:** A set loses multiplicity; a mapping preserves one counter per key.

**Interviewer intent:** Assess collection choice and accumulation.

**Common errors**

- Use a set and expect counts to remain.

**Follow-ups**

- What should empty input return?

**Example**

For ["b","b","b"], the mapping is {"b":3}.

**Self-assessment rubric**

- 1 — Chooses dictionary and describes increment per key.
- 1 — Predicts both counts and explains why a set is insufficient.

Maximum: 2

</details>

**Prerequisites**

- [Choose by the contract](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.md)
- [1. Accumulator and frequency map](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)

### algorithms.recursion-stack

`mid` · `data-structures-algorithms`

For summing integers from 0 to n with n nonnegative, give a base case and recurrence. Compare recursive and iterative time/auxiliary space under fixed-cost arithmetic.

<details>
<summary>Expected answer</summary>

S(0)=0; S(n)=n+S(n-1). Both iterative and recursive scans take O(n) time; the recursive version uses O(n) call-stack space while the accumulator uses O(1) extra space.

**Explanation:** Progress toward the base case matters; Python's recursion limit constrains practical depth.

**Interviewer intent:** Assess termination and resource analysis.

**Common errors**

- Ignore stack frames when reporting auxiliary space.

**Follow-ups**

- Why reject negative inputs before recursion?

**Example**

S(3) = 3 + 2 + 1 + 0 = 6.

**Self-assessment rubric**

- 1 — Gives base case, recurrence and progress toward zero.
- 1 — Reports time and stack/accumulator space correctly.

Maximum: 2

</details>

**Prerequisites**

- [Choose by the contract](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.md)
- [2. Python implementation](../../problem-solving-and-live-coding/04-recursion/README.md)

### algorithms.stable-insertion

`mid` · `data-structures-algorithms`

Define stability in sorting records by score. How does insertion sort preserve it, and what is its worst-case time? Illustrate with equal-score records.

<details>
<summary>Expected answer</summary>

Equal-key records retain their original relative order. In insertion sort, shift only strictly greater keys and insert after equal keys in the sorted prefix. Worst-case time is O(n²).

**Explanation:** Shifting equal keys can reverse their order even when scores are sorted correctly.

**Interviewer intent:** Assess stability beyond sorted output.

**Common errors**

- Verify only numeric scores and ignore record identity.

**Follow-ups**

- What input would reveal an unstable implementation?

**Example**

[(A,2),(B,1),(C,2)] becomes [(B,1),(A,2),(C,2)] when sorted stably by score.

**Self-assessment rubric**

- 1 — Defines stability and the strict-greater shift rule.
- 1 — States O(n²) worst-case time and illustrates equal-key order.

Maximum: 2

</details>

**Prerequisites**

- [Choose by the contract](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.md)
- [4. Insertion sort](../../problem-solving-and-live-coding/06-sorting-algorithms/README.md)

### algorithms.two-pointer-pair

`mid` · `data-structures-algorithms`

For sorted ascending integers, decide if two different indices sum to target. Explain pointer moves, termination and costs.

<details>
<summary>Expected answer</summary>

Start left=0, right=n-1. While left < right, compare their sum: equal succeeds, too small increments left, too large decrements right. If pointers meet, fail. Sortedness justifies discarded pairs. O(n) time, O(1) extra space under fixed-cost arithmetic.

**Explanation:** Each move shrinks the remaining interval and never uses the same index twice.

**Interviewer intent:** Assess invariant, correctness and complexity.

**Common errors**

- Use left <= right, allowing a single element to count twice.

**Follow-ups**

- Why does [3,3] work for target 6 but [3] does not?

**Example**

[1,3,4,7] with target 7 succeeds via indices 1 and 2.

**Self-assessment rubric**

- 1 — Describes moves, sortedness rationale and strict index separation.
- 1 — States linear time and constant extra space with termination.

Maximum: 2

</details>

**Prerequisites**

- [Choose by the contract](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.md)
- [2. Two pointers](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)

### algorithms.window-tradeoff

`senior` · `data-structures-algorithms`

Find the maximum sum of k consecutive integers, including all-negative input. Compare recomputing every window with a rolling sum, state assumptions and propose boundary tests.

<details>
<summary>Expected answer</summary>

Require 1 <= k <= n. Sum the first k elements, initialize best to that sum, then subtract each outgoing and add incoming value. Recomputing costs O((n-k+1)k); rolling costs O(n) time and O(1) auxiliary space for random-access input under fixed-cost arithmetic. Test k=1, k=n, all-negative values and invalid k.

**Explanation:** A rolling update reuses work; initializing best to zero incorrectly admits a nonexistent window for all-negative input.

**Interviewer intent:** Assess optimization tied to a precise contract and test oracle.

**Common errors**

- Claim O(nk) work is unavoidable or initialize best to zero.

**Follow-ups**

- What result should [-4,-2,-5] with k=2 produce?

**Example**

[-4,-2,-5], k=2 gives max(-6,-7) = -6.

**Self-assessment rubric**

- 1 — Defines valid k, rolling invariant and correct initialization.
- 1 — Compares costs with assumptions and proposes boundary/negative tests.

Maximum: 2

</details>

**Prerequisites**

- [Choose by the contract](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.md)
- [3. Fixed sliding window](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)

## Object-oriented programming

### oop.class-list-sharing

`junior` · `oop`

A class defines members=[] at class level. Why can two instances unexpectedly share additions? Show how to make lists independent.

<details>
<summary>Expected answer</summary>

The mutable class attribute is shared unless shadowed by an instance attribute. Initialize self.members=[] inside __init__ to create a distinct list for each instance.

**Explanation:** Appending mutates the shared object, whereas assigning an instance attribute changes lookup for that instance.

**Interviewer intent:** Assess mutable class attributes.

**Common errors**

- Keep one list on the class and assume self creates a copy.

**Follow-ups**

- What class attribute would reasonably be shared?

**Example**

Two new groups should have separate empty lists; adding a member to one leaves the other empty.

**Self-assessment rubric**

- 1 — Explains shared mutable class attribute and mutation.
- 1 — Initializes independent instance list and predicts isolation.

Maximum: 2

</details>

**Prerequisites**

- [Attributes and binding](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.md)

### oop.independent-state

`junior` · `oop`

Two Counter instances initialize self.value=0. Only first.increment() runs. What are their values, and why?

<details>
<summary>Expected answer</summary>

First is 1 and second is 0; each instance owns its attribute and the bound method receives the instance as self.

**Explanation:** A class defines behavior; objects can hold independent state.

**Interviewer intent:** Assess instance state and method binding.

**Common errors**

- Treat all instances as sharing self.value.

**Follow-ups**

- How would you test independent instances?

**Example**

first.increment(); assert second.value == 0.

**Self-assessment rubric**

- 1 — Predicts both values.
- 1 — Explains per-instance state and self binding.

Maximum: 2

</details>

**Prerequisites**

- [What and why](../../technical-interview-preparation/05-classes-and-objects/README.md)

### oop.initialization

`junior` · `oop`

What is __init__ for, and how does it differ from __new__? What may __init__ return?

<details>
<summary>Expected answer</summary>

__new__ is the creation hook; __init__ initializes an already created instance. __init__ must return None, usually implicitly.

**Explanation:** The normal class call coordinates creation and initialization.

**Interviewer intent:** Assess object lifecycle basics.

**Common errors**

- Return self from __init__ or call it the allocation hook.

**Follow-ups**

- Where would you initialize a per-instance list?

**Example**

def __init__(self): self.value = 0 initializes state without returning a value.

**Self-assessment rubric**

- 1 — Distinguishes creation from initialization.
- 1 — States None return contract.

Maximum: 2

</details>

**Prerequisites**

- [What and why](../../technical-interview-preparation/05-classes-and-objects/README.md)

### oop.constructor-binding

`mid` · `oop`

Compare instance, class and static methods. Why should an inherited alternative constructor use cls(...) instead of the base class name? State the subclass constructor compatibility assumption.

<details>
<summary>Expected answer</summary>

Instance methods receive self; class methods receive cls; static methods receive neither implicitly. Using cls(...) lets a compatible subclass construct its own instance rather than forcing the base type.

**Explanation:** Binding determines the implicit argument, not whether the operation has side effects.

**Interviewer intent:** Assess method selection and subclass extensibility.

**Common errors**

- Assume a static method is automatically pure.

**Follow-ups**

- What if a subclass requires extra constructor arguments?

**Example**

A compatible SubGroup.from_label("A") should return a SubGroup when the factory uses cls.

**Self-assessment rubric**

- 1 — Identifies implicit binding for all three method kinds.
- 1 — Explains cls-based construction and compatibility constraint.

Maximum: 2

</details>

**Prerequisites**

- [Attributes and binding](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.md)

### oop.length-and-repr

`mid` · `oop`

A StudyGroup needs len(group), a user-friendly str(group) and debugging repr(group). Which methods implement these and what must length return?

<details>
<summary>Expected answer</summary>

Implement __len__, __str__, __repr__. __len__ returns a nonnegative integer representing length; __str__ is user-oriented, __repr__ supports debugging and need not be executable Python.

**Explanation:** Use documented language protocols rather than invented dunder names.

**Interviewer intent:** Assess integration with Python protocols.

**Common errors**

- Return a negative count or assume repr must reconstruct the object.

**Follow-ups**

- What would len return for an empty group?

**Example**

__len__ can return len(self.members); an empty group has length zero.

**Self-assessment rubric**

- 1 — Maps all three operations to the correct methods.
- 1 — Explains nonnegative integer length and distinct string purposes.

Maximum: 2

</details>

**Prerequisites**

- [Special methods](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.md)

### oop.replaceable-collaborator

`mid` · `oop`

A report notifier must support text and email channels, then a fake channel in tests. Compare inheritance and composition; propose a design without changing the notifier for each channel. Explain a trade-off and how a fake would test the contract.

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

`Notifier(channel).notify('Ready')` delegates to the fake channel's `send('Ready')`, returning `test: Ready` without contacting a network.

**Self-assessment rubric**

- 1 — Proposes explicit collaborator injection and delegation.
- 1 — Distinguishes subtype contract from composition and duck typing.
- 1 — Explains a fake-based test and at least one trade-off.

Maximum: 3

</details>

**Prerequisites**

- [Polymorphism and composition](../../technical-interview-preparation/07-inheritance-polymorphism-and-composition/README.md)

### oop.invariant-boundary

`senior` · `oop`

Design stock removal so quantity never becomes negative through the public contract. Explain validation order, read access and tests; is underscore naming a security boundary?

<details>
<summary>Expected answer</summary>

Expose remove with validation before mutation; reject an amount outside the documented domain or beyond stock without changing quantity. Expose read-only property if useful. Test valid removal, insufficient stock and unchanged state on failure. Underscore is convention; name mangling/property is not security.

**Explanation:** Encapsulation protects invariants for supported operations; it does not enforce access control against arbitrary callers.

**Interviewer intent:** Assess domain invariant design and negative tests.

**Common errors**

- Subtract first then raise, leaving corrupted state.

**Follow-ups**

- How would you show that failed validation has no side effects?

**Example**

With quantity 5, rejecting removal of 6 must leave quantity 5.

**Self-assessment rubric**

- 1 — Designs validation-before-mutation and explicit read contract.
- 1 — Proposes unchanged-state tests and distinguishes convention from security.

Maximum: 2

</details>

**Prerequisites**

- [Encapsulation and abstraction](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.md)

### oop.solid-contracts

`senior` · `oop`

A high-level remaining-stock policy depends on a concrete database reader exposing unrelated write methods. Redesign the dependency using DIP and ISP, with a fake test and a trade-off.

<details>
<summary>Expected answer</summary>

Depend on a small available contract, optionally an ABC with an abstract method, and inject a reader implementing it. DIP separates policy from infrastructure; ISP avoids requiring unused operations. Test with a fake returning a fixed balance. Add abstraction only when replaceability justifies indirection.

**Explanation:** The caller needs behavior, not storage details; type hints alone do not enforce runtime semantics.

**Interviewer intent:** Assess SOLID as design trade-offs.

**Common errors**

- Create five classes merely to match five principles.

**Follow-ups**

- When would a plain function be simpler?

**Example**

Inject an available-only fake returning 7 and check the policy without a database.

**Self-assessment rubric**

- 1 — Explains DIP and ISP through a small replaceable contract.
- 1 — Proposes fake-based test and weighs added indirection.

Maximum: 2

</details>

**Prerequisites**

- [Encapsulation and abstraction](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.md)
- [SOLID as design questions](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.md)

## Python internals

### internals.del-binding

`junior` · `python-internals`

Given first=[]; second=first; del first; second.append(3), what is second? Does del guarantee destruction?

<details>
<summary>Expected answer</summary>

second is [3]. del removes the first binding, not the object while second still strongly references it. Python does not guarantee immediate destruction.

**Explanation:** Reachability and ownership, not a particular variable name, determine whether a reference still keeps an object alive.

**Interviewer intent:** Assess object lifetime reasoning.

**Common errors**

- Assume del first empties the list.

**Follow-ups**

- What if a global container still holds the list?

**Example**

A list stored in two names remains usable through the surviving name.

**Self-assessment rubric**

- 1 — Predicts second correctly and distinguishes binding deletion from object destruction.
- 1 — Explains strong reference and absence of guaranteed immediate finalization.

Maximum: 2

</details>

**Prerequisites**

- [Object lifetime and reachability](../../technical-interview-preparation/10-python-memory-management/README.md)

### internals.iterator-exhaustion

`junior` · `python-internals`

Given it=iter([1,2,3]); next(it); print(list(it)); print(list(it)), what is printed and why?

<details>
<summary>Expected answer</summary>

It prints [2,3] then []. next consumed 1; the first list call consumed the remainder, so the iterator is exhausted. iter(it) returns that iterator, not a fresh traversal.

**Explanation:** A list is iterable and can supply fresh iterators; an iterator keeps traversal state.

**Interviewer intent:** Assess one-shot consumption.

**Common errors**

- Assume list(it) resets the iterator.

**Follow-ups**

- What exception does next(it) raise once exhausted?

**Example**

iter([1,2]) and another iter([1,2]) are separate traversals.

**Self-assessment rubric**

- 1 — Predicts both printed lists.
- 1 — Explains iterator state, exhaustion and difference from iterable.

Maximum: 2

</details>

**Prerequisites**

- [Iteration protocol](../../technical-interview-preparation/11-iterators-generators-and-comprehensions/README.md)

### internals.context-exit

`mid` · `python-internals`

A context manager opens a resource and its body raises RuntimeError. Explain __enter__, __exit__, suppression and what changes if entry itself fails.

<details>
<summary>Expected answer</summary>

__enter__ returns the as value. After successful entry, __exit__ receives exception details and releases the resource; false/None propagates the body exception, truthy suppresses it. If entry fails, that manager's exit is not called automatically; entry must handle partial acquisition.

**Explanation:** Cleanup and suppression are separate decisions; returning truthy accidentally hides errors.

**Interviewer intent:** Assess resource management and failure semantics.

**Common errors**

- Assume exit runs even if enter raises.

**Follow-ups**

- How would you test cleanup exactly once?

**Example**

A successful enter followed by a body failure records open and close once, with RuntimeError propagated if exit returns False.

**Self-assessment rubric**

- 1 — Describes entry, exit details and truthy suppression contract.
- 1 — Distinguishes body failure from entry failure and partial acquisition.

Maximum: 2

</details>

**Prerequisites**

- [The with protocol](../../technical-interview-preparation/13-context-managers/README.md)
- [Practical decisions](../../technical-interview-preparation/13-context-managers/README.md)

### internals.decorator-contract

`mid` · `python-internals`

A logging decorator must record every attempt, including calls that raise, without changing the wrapped calculation's contract. How would you implement and test attempt recording, return values, arguments, metadata and failure propagation?

<details>
<summary>Expected answer</summary>

Assuming the recording operation succeeds, record each attempt before invoking the wrapped function. Forward `*args` and `**kwargs`, return the wrapped result, preserve metadata with `functools.wraps` and let exceptions propagate. Test positional and keyword calls, result, name and a deliberate exception; check exactly one record per attempt, including failure.

**Explanation:** A cross-cutting wrapper should not silently alter core behavior.

**Interviewer intent:** Assess decorators and behavior-preserving tests.

**Common errors**

- Forget to return the wrapped result or swallow exceptions.
- Record only successful returns, omitting failed attempts.

**Follow-ups**

- When are stacked decorators applied?

**Example**

Using `record_calls(records)` with an initially empty list, a wrapped `divide(8, denominator=2)` returns `4`; `divide(8, denominator=0)` raises `ZeroDivisionError`. Afterwards, `records` equals `['divide', 'divide']`.

**Self-assessment rubric**

- 1 — Specifies one record per attempt before invocation, forwarding, return, metadata and exception preservation.
- 1 — Proposes tests for each named contract, asserting recorded attempts on both success and failure.

Maximum: 2

</details>

**Prerequisites**

- [Decorators](../../technical-interview-preparation/12-closures-and-decorators/README.md)

### internals.late-binding

`mid` · `python-internals`

Inside a factory, create three lambdas in a loop over range(3), each returning i. If called only after the loop, what do they return? Show a fix for immutable indices.

<details>
<summary>Expected answer</summary>

All return 2 because the closures share the changing enclosing binding. Use lambda i=i: i to bind the current immutable value as a default at definition, or use a separate factory call.

**Explanation:** Closure capture is not automatically a snapshot; default binding is evaluated at function creation.

**Interviewer intent:** Assess binding time and closure behavior.

**Common errors**

- Expect 0, 1, 2 without binding individual values.

**Follow-ups**

- Would binding a mutable list as a default deep-copy it?

**Example**

[lambda i=i: i for i in range(3)] yields functions returning 0, 1, 2 respectively.

**Self-assessment rubric**

- 1 — Predicts late-bound results and explains shared binding.
- 1 — Demonstrates a valid snapshot/factory correction for immutable values.

Maximum: 2

</details>

**Prerequisites**

- [Closures and scope](../../technical-interview-preparation/12-closures-and-decorators/README.md)

### internals.nested-copy

`mid` · `python-internals`

A dictionary contains two keys referencing the same mutable list. You need an independent graph while preserving the alias relationship inside the copy. Compare assignment, shallow copy and deep copy. Explain copying limitations and how you would test isolation and preserved aliasing.

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

### internals.cache-retention

`senior` · `python-internals`

A long-running CPython service grows memory while retaining a global cache. Explain reachable retention versus unreachable cycles, what gc.collect can do, and how you would measure and bound the problem.

<details>
<summary>Expected answer</summary>

Reachable cache values remain alive; conventional reference counting plus cyclic GC can reclaim many unreachable objects and cycles, but gc.collect cannot free reachable values or guarantee lower RSS. Inspect ownership and compare tracemalloc snapshots alongside process memory metrics; bound retention by suitable count/byte budget, evict references and check external aliases.

**Explanation:** Python allocation snapshots are not a full measure of native allocations or RSS. Count bounds are not byte bounds.

**Interviewer intent:** Assess memory diagnosis before optimization.

**Common errors**

- Force GC periodically while keeping the same unbounded reachable cache.

**Follow-ups**

- Why could clearing the cache leave values alive?

**Example**

An entry-count limit of 100 does not imply 100 bytes; compare allocations before and after evictions with a representative load.

**Self-assessment rubric**

- 1 — Explains reachability, cyclic GC and collection limitations.
- 1 — Proposes bounded retention and measurement while distinguishing tracemalloc from process memory.

Maximum: 2

</details>

**Prerequisites**

- [Object lifetime and reachability](../../technical-interview-preparation/10-python-memory-management/README.md)
- [Retention and measurement](../../technical-interview-preparation/10-python-memory-management/README.md)

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
- 1 — Chooses I/O/CPU strategies with at least one trade-off and proposes measurement on the actual workload.
- 1 — Protects shared invariant and distinguishes correctness tests from benchmarks.

Maximum: 3

</details>

**Prerequisites**

- [The GIL in Python 3.13](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.md)
- [Concurrency and parallelism](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.md)
- [Shared-state example](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.md)

## Testing and debugging

### testing.else-finally

`junior` · `testing-debugging`

What are the roles of else and finally in a try statement? Explain behavior when the protected operation raises an unexpected exception.

<details>
<summary>Expected answer</summary>

else runs when the try suite finishes normally without an exception; finally runs on exit to perform cleanup. An unmatched exception propagates after finally unless cleanup itself changes that outcome.

**Explanation:** Do not return from finally to hide a failure.

**Interviewer intent:** Assess structured exception flow.

**Common errors**

- Treat finally as success-only code.

**Follow-ups**

- When might with be clearer?

**Example**

After an unmatched RuntimeError, cleanup in finally still runs before propagation.

**Self-assessment rubric**

- 1 — Distinguishes normal completion else from exit cleanup finally.
- 1 — Explains unexpected exception propagation and cleanup caveat.

Maximum: 2

</details>

**Prerequisites**

- [Exception boundaries](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)

### testing.specific-catch

`junior` · `testing-debugging`

When converting user text to int, why catch ValueError specifically instead of hiding every exception? What should invalid text do?

<details>
<summary>Expected answer</summary>

Catch the expected conversion failure at a boundary that can handle or translate it. Report or raise the agreed invalid-input error; let unrelated unexpected exceptions propagate.

**Explanation:** Returning zero for bad text confuses invalid input with a valid zero.

**Interviewer intent:** Assess exception scope and data contracts.

**Common errors**

- Catch everything and return zero unconditionally.

**Follow-ups**

- What distinguishes "0" from "abc" in tests?

**Example**

int("0") succeeds, int("abc") raises ValueError.

**Self-assessment rubric**

- 1 — Chooses the specific expected exception and explains propagation.
- 1 — Distinguishes invalid text from valid zero in the contract.

Maximum: 2

</details>

**Prerequisites**

- [Exception boundaries](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)

### testing.test-levels

`junior` · `testing-debugging`

Distinguish unit, integration and end-to-end tests for a reporting service. Give one example of each.

<details>
<summary>Expected answer</summary>

Unit: count unique IDs using a controlled fake loader. Integration: exercise the real database loader against a test database. End-to-end: request a report through the supported interface and verify the resulting response across the full workflow.

**Explanation:** The levels differ by boundaries exercised, not simply by number of assertions.

**Interviewer intent:** Assess testing scope and dependency boundaries.

**Common errors**

- Call a test with all dependencies mocked an end-to-end test.

**Follow-ups**

- Why keep a real-boundary integration test if units pass?

**Example**

A fake loader returning [1,1,2] supports a unit assertion of two unique completions.

**Self-assessment rubric**

- 1 — Identifies unit and integration boundaries with distinct examples.
- 1 — Describes a full supported workflow example for end-to-end.

Maximum: 2

</details>

**Prerequisites**

- [Test and debug by evidence](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)
- [Decisions start with a requirement](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.md)

### testing.boundary-oracle

`mid` · `testing-debugging`

parse_quantity must accept nonnegative integer text, including whitespace supported by int, and reject invalid or negative inputs. Give tests with expected outputs/errors that would catch a version returning zero on bad input.

<details>
<summary>Expected answer</summary>

Assert "0" returns 0 and " 12 " returns 12; assert the documented InvalidQuantity for "abc", "-1" and "". Checking the specific exception rather than mere execution detects silent-zero behavior.

**Explanation:** Positive and negative assertions must distinguish the intended contract from plausible wrong implementations.

**Interviewer intent:** Assess test oracle precision and boundary coverage.

**Common errors**

- Assert only that a function was called or returned an int.

**Follow-ups**

- Which case detects rejection of valid zero?

**Example**

A test requiring InvalidQuantity for "abc" fails when the implementation silently returns 0.

**Self-assessment rubric**

- 1 — Specifies exact results for normal and zero-boundary inputs.
- 1 — Specifies exact error behavior for invalid and negative inputs.

Maximum: 2

</details>

**Prerequisites**

- [Exception boundaries](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)
- [Test and debug by evidence](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)
- [Practice](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)

### testing.debugging-evidence

`mid` · `testing-debugging`

A previously passing parser now fails on a particular input. Describe a debugging sequence and what evidence you record without exposing private payloads.

<details>
<summary>Expected answer</summary>

Reproduce with minimal sanitized input, inspect traceback and relevant state, form a hypothesis, change one cause, rerun the reproducer and add a regression test. Record safe context and actual results, redacting secrets.

**Explanation:** Controlled changes make causal evidence easier to interpret.

**Interviewer intent:** Assess disciplined debugging and privacy.

**Common errors**

- Log every raw credential and change several conditions at once.

**Follow-ups**

- What if you cannot reproduce the failure?

**Example**

Replace a private input with a fictional minimal malformed string that reproduces the same exception.

**Self-assessment rubric**

- 1 — Describes reproduction, hypothesis and controlled verification sequence.
- 1 — Proposes regression evidence with sanitized logs and actual outcomes.

Maximum: 2

</details>

**Prerequisites**

- [Test and debug by evidence](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)

### testing.exception-cause

`mid` · `testing-debugging`

At a conversion boundary, translate ValueError to a domain-specific InvalidQuantity without losing the cause. Show syntax and distinguish it from bare raise.

<details>
<summary>Expected answer</summary>

Inside except ValueError as error, use raise InvalidQuantity("invalid quantity") from error. The explicit cause is retained. Bare raise inside that handler re-raises the active exception instead of translating it.

**Explanation:** Translation offers a stable domain contract while keeping diagnostic evidence.

**Interviewer intent:** Assess exception chaining and diagnostics.

**Common errors**

- Replace the error with a success value.

**Follow-ups**

- Which assertion verifies the original cause type?

**Example**

assert isinstance(caught.exception.__cause__, ValueError) in a unittest assertRaises context.

**Self-assessment rubric**

- 1 — Shows explicit raise-from syntax with caught error.
- 1 — Distinguishes re-raising from translating and explains cause preservation.

Maximum: 2

</details>

**Prerequisites**

- [Exception boundaries](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)

### testing.coverage-vs-discrimination

`senior` · `testing-debugging`

A parser has high line coverage but a mutated implementation returning zero for invalid text still passes. Explain what this means and propose a stronger verification strategy without claiming tests prove all correctness.

<details>
<summary>Expected answer</summary>

Coverage measures execution, not correctness. A surviving plausible defect shows the oracle is insufficient for that behavior. Add precise expected-value and exception assertions, boundary cases and regression tests; rerun correct and intentionally wrong versions. Test real component boundaries separately, with deterministic setup. Passing strengthens evidence, not proof of every behavior.

**Explanation:** A useful negative test rejects a representative defect while the reference passes.

**Interviewer intent:** Assess test quality and limits of assurance.

**Common errors**

- Treat a coverage percentage as proof of correct behavior.

**Follow-ups**

- Why keep assertions about unchanged state after a rejected operation?

**Example**

Require correct zero output for "0" and specific exception for "abc"; the silent-zero variant must fail.

**Self-assessment rubric**

- 1 — Explains surviving defect and the coverage/oracle distinction.
- 1 — Proposes discriminating deterministic tests, boundary verification and honest limits.

Maximum: 2

</details>

**Prerequisites**

- [Test and debug by evidence](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)
- [Practice](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)

## Backend and APIs

### api.http-request-response

`junior` · `backend-apis`

Describe the main elements of an HTTP request and response. Give a GET example and explain which side chooses the response status.

<details>
<summary>Expected answer</summary>

A request has method, target, headers and optional content. The server responds with status, headers and optional content. The client sends GET /lessons; the server determines a status and representation according to the contract.

**Explanation:** HTTP status describes the outcome, not the client-selected action.

**Interviewer intent:** Assess HTTP request/response basics.

**Common errors**

- Assume every HTTP request or response must contain JSON.

**Follow-ups**

- Which response header can describe content format?

**Example**

GET /lessons → 200 with Content-Type: application/json and a lesson representation.

**Self-assessment rubric**

- 1 — Identifies method/target versus response status and both sets of headers.
- 1 — Gives a coherent GET example and distinguishes optional content.

Maximum: 2

</details>

**Prerequisites**

- [Client, server and resource contracts](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.md)

### api.status-contract

`junior` · `backend-apis`

A GET-only /lessons endpoint receives GET /missing and POST /lessons. Which statuses are appropriate and which header must accompany the unsupported method?

<details>
<summary>Expected answer</summary>

Return 404 for the missing resource and 405 for a known target with an unsupported method. Include Allow: GET under the stated GET-only contract. A successful GET can return 200.

**Explanation:** Missing targets and unsupported methods are distinct failure cases.

**Interviewer intent:** Assess status-code semantics and contracts.

**Common errors**

- Return 200 for all outcomes or confuse 404 with 405.

**Follow-ups**

- What would a stable error body avoid revealing?

**Example**

GET /missing → 404; POST /lessons → 405 and Allow: GET.

**Self-assessment rubric**

- 1 — Chooses both correct statuses for the distinct cases.
- 1 — Includes Allow and explains its relation to the known target.

Maximum: 2

</details>

**Prerequisites**

- [Response design](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.md)

### api.idempotent-retry

`mid` · `backend-apis`

A POST creation times out after possibly succeeding. Compare retrying POST with PUT and DELETE semantics; propose a safe retry contract and explain why response equality is not required.

<details>
<summary>Expected answer</summary>

POST is not guaranteed idempotent, so a blind retry may duplicate creation. PUT and DELETE have idempotent intended effects under HTTP semantics, not necessarily identical responses. For retryable creation use an explicit persisted idempotency-key contract, bounded attempts, timeouts and respect Retry-After where applicable.

**Explanation:** A timeout does not establish whether the server committed a side effect.

**Interviewer intent:** Assess distributed request uncertainty and contract design.

**Common errors**

- Retry every POST without deduplication semantics.

**Follow-ups**

- Why can repeated DELETE return 204 and then 404?

**Example**

The same creation request with a persisted key should not create a second resource under its explicit retry contract.

**Self-assessment rubric**

- 1 — Distinguishes POST retry risk from PUT/DELETE intended-effect idempotence.
- 1 — Proposes explicit retry contract and bounded network behavior.

Maximum: 2

</details>

**Prerequisites**

- [Client, server and resource contracts](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.md)

### api.payload-boundary

`mid` · `backend-apis`

An API accepts exactly one title field, a string with 1–80 characters after trimming. Explain parsing versus validation; propose accepted and rejected inputs plus transport-level limits.

<details>
<summary>Expected answer</summary>

Parsing decodes JSON; validation checks object shape, allowed field, string type and trimmed length. Accept {"title":" SQL "} as SQL; reject missing/extra fields, booleans, blank and overlong titles. Enforce body-size limits before parsing when possible and define duplicate-key handling separately.

**Explanation:** Syntactically valid JSON can violate domain rules. An already decoded dict cannot reliably reveal duplicate keys in raw input.

**Interviewer intent:** Assess layered validation and boundary tests.

**Common errors**

- Treat successful JSON parsing as proof of valid business input.

**Follow-ups**

- Why reject extra owner fields in this contract?

**Example**

A title of exactly 80 characters after trimming is accepted; 81 is rejected.

**Self-assessment rubric**

- 1 — Separates parsing and shape/type/length validation with positive and negative examples.
- 1 — Identifies transport limits and raw duplicate-key handling as separate concerns.

Maximum: 2

</details>

**Prerequisites**

- [Validate the boundary](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.md)

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

## Databases and SQL

### sql.keys-and-constraints

`junior` · `databases-sql`

A lessons table requires unique non-null titles and positive non-null minutes. Which constraints express these rules, and what is the primary key for? Explain the SQLite INTEGER typing caveat if minutes must be an integer.

<details>
<summary>Expected answer</summary>

Use title TEXT NOT NULL UNIQUE and minutes INTEGER NOT NULL CHECK(minutes > 0); a primary key identifies each row. In SQLite, declared INTEGER alone is not strict type enforcement; use an appropriate type/storage check and application validation for a true integer domain.

**Explanation:** CHECK alone does not reject NULL; combine it with NOT NULL.

**Interviewer intent:** Assess relational integrity constraints.

**Common errors**

- Assume CHECK(minutes > 0) alone forbids NULL or fractional values.

**Follow-ups**

- What should inserting a duplicate title do?

**Example**

SQLite can use CHECK(typeof(minutes) = 'integer' AND minutes > 0) together with NOT NULL.

**Self-assessment rubric**

- 1 — Selects correct UNIQUE, NOT NULL and positive CHECK constraints.
- 1 — Explains primary key and why SQLite integer typing needs care.

Maximum: 2

</details>

**Prerequisites**

- [Relational model and constraints](../../technical-interview-preparation/18-relational-databases-and-sql/README.md)

### sql.null-and-order

`junior` · `databases-sql`

Given lessons(id, title, minutes) with nullable minutes, write a query for rows with missing minutes ordered by id. Explain why = NULL and omitting ORDER BY are unsuitable.

<details>
<summary>Expected answer</summary>

SELECT id, title FROM lessons WHERE minutes IS NULL ORDER BY id; comparison with NULL normally yields unknown, not true, and WHERE keeps true rows. Without ORDER BY, result ordering is not guaranteed.

**Explanation:** NULL represents missing/unknown information, not zero.

**Interviewer intent:** Assess SQL three-valued filtering and explicit order.

**Common errors**

- Use minutes = NULL or assume insertion order.

**Follow-ups**

- Would minutes=0 match the query?

**Example**

With minutes values NULL, 0, 20, only the NULL row matches.

**Self-assessment rubric**

- 1 — Uses IS NULL and explicit ORDER BY id.
- 1 — Explains unknown comparison result and lack of default order.

Maximum: 2

</details>

**Prerequisites**

- [Relational model and constraints](../../technical-interview-preparation/18-relational-databases-and-sql/README.md)

### sql.bound-values

`mid` · `databases-sql`

In Python sqlite3, a search accepts a title and a user-selected sort column. How do you bind the title safely and constrain the column? Explain why placeholders cannot bind identifiers.

<details>
<summary>Expected answer</summary>

Pass title as a value parameter, e.g. db.execute("SELECT id FROM lessons WHERE title = ?", (title,)). Use a fixed query or allowlist mapping of sort options to trusted SQL identifiers; never interpolate arbitrary input. Placeholders represent values, not SQL syntax such as column identifiers.

**Explanation:** Bound input remains data even when it contains quotes. The comma forms a one-element tuple.

**Interviewer intent:** Assess safe SQL construction and identifier boundaries.

**Common errors**

- Concatenate raw title or raw column names into SQL.

**Follow-ups**

- How would you test quote-containing titles and unsupported sort choices?

**Example**

Map "duration" to the fixed identifier minutes; reject unknown sort options. Bind "O'Reilly" as title data.

**Self-assessment rubric**

- 1 — Shows bound title value with correct parameter tuple.
- 1 — Explains identifier limitation and fixed-query/allowlist approach.

Maximum: 2

</details>

**Prerequisites**

- [Connect from Python](../../technical-interview-preparation/18-relational-databases-and-sql/README.md)
- [SQL safety](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.md)

### sql.zero-child-count

`mid` · `databases-sql`

Given groups(id, name) and tasks(id, group_id, done), return the count of completed tasks per group, including groups with no completed tasks. How do ON, WHERE and COUNT affect correctness? Assume both id columns are primary keys, tasks.group_id references groups.id and done is 0 or 1. Explain why grouping only by name is insufficient.

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

### sql.atomic-transfer

`senior` · `databases-sql`

A credit transfer debits one account and credits another. Design transaction ownership, conditional balance checks and failure verification. Explain ACID and whether a new index alone guarantees better performance.

<details>
<summary>Expected answer</summary>

Use a dedicated transaction with no unrelated pending writes; validate distinct accounts and positive integer amount, debit only if sufficient balance, verify affected rows, credit target and commit only after both succeed; rollback on missing target or any failure. ACID means atomicity, consistency of invariants, isolation visibility rules and durability under storage guarantees. Check balances after success/failure and from a separate connection after commit. Indexes cost storage/writes; inspect query plans and measure before claiming improvement.

**Explanation:** Atomicity prevents partial debit; an in-memory database is not durable across process exit. Isolation behavior depends on the engine.

**Interviewer intent:** Assess integrity guarantees, failure testing and measured optimization.

**Common errors**

- Commit the debit before credit or assume every index helps.

**Follow-ups**

- Why is observing the new balance on the writing connection insufficient to prove a commit?

**Example**

Balances 10 and 2 become 7 and 5 after transfer of 3; a failed subsequent transfer to a missing target leaves both unchanged.

**Self-assessment rubric**

- 1 — Designs atomic ownership, conditional updates and cross-connection/failure checks.
- 1 — Explains four ACID properties and proposes measuring index benefit against cost.

Maximum: 2

</details>

**Prerequisites**

- [Transactions and integrity](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.md)
- [Indexes and query planning](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.md)

## Software engineering

### engineering.sdd-tdd

`junior` · `software-engineering`

Distinguish SDD from TDD for a function counting unique completed lessons. What evidence is needed before claiming Red and Green?

<details>
<summary>Expected answer</summary>

SDD defines the requirement, plan, tasks and observable acceptance criteria. TDD writes a behavior test, observes its failure for the intended reason, implements and observes passing tests before refactoring. Record actual execution results; writing a test alone does not establish Red.

**Explanation:** Specifications define what to deliver; tests provide execution evidence for behavior.

**Interviewer intent:** Assess development discipline and honesty of evidence.

**Common errors**

- Claim Red occurred just because a test file was committed first.

**Follow-ups**

- What acceptance case would reject duplicate counting?

**Example**

Input [1,2,2] has expected count 2; run the test before and after implementation.

**Self-assessment rubric**

- 1 — Distinguishes specification artifacts from the TDD feedback cycle.
- 1 — Requires observed failure/pass evidence before claiming Red/Green.

Maximum: 2

</details>

**Prerequisites**

- [Decisions start with a requirement](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.md)

### engineering.dependency-boundary

`mid` · `software-engineering`

A progress-report rule currently opens a database directly. Redesign the boundary to support unit tests without storage; explain integration tests and how to record the decision in an ADR.

<details>
<summary>Expected answer</summary>

Inject a loader callable returning completion IDs for the learner; keep unique-ID counting and validation in the domain rule. Use a fake to test duplicates, empty input, invalid IDs and propagated dependency failure. Integration tests verify actual query/mapping separately. Record context, alternatives (direct query vs injected loader), decision, consequences and acceptance criteria.

**Explanation:** Dependency injection isolates policy tests but does not verify the real storage boundary; abstraction adds indirection.

**Interviewer intent:** Assess maintainability, test seams and documented decisions.

**Common errors**

- Replace every integration test with fake-loader tests.

**Follow-ups**

- When would direct code be simpler than introducing a new abstraction?

**Example**

progress_report("learner-a", lambda _: [1,2,2]) should return {"completed":2}.

**Self-assessment rubric**

- 1 — Proposes a replaceable loader and distinguishes unit and integration responsibilities.
- 1 — Records context, alternatives, decision and consequences including test evidence.

Maximum: 2

</details>

**Prerequisites**

- [Decisions start with a requirement](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.md)
- [Trade-offs and operation](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.md)

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
- [Decisions start with a requirement](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.md)

## Behavioral and international interviews

### behavioral.star-evidence

`junior` · `behavioral-international`

Describe a bug or learning challenge using STAR. Use a truthful nonconfidential example (study or personal work is acceptable), or label a fictional rehearsal explicitly. Distinguish your own action, observable result, learning and limitation.

<details>
<summary>Expected answer</summary>

State brief situation, your assigned task, specific actions you took and an observable result plus learning. Describe a limitation honestly; do not invent metrics, attribute others' work to yourself or expose confidential material.

**Explanation:** STAR organizes evidence rather than requiring professional tenure or numeric impact.

**Interviewer intent:** Assess ownership, concrete evidence and learning.

**Common errors**

- Present a fictional success as real employment or claim team outcomes as individual work.

**Follow-ups**

- What would you improve next and how would you verify it?

**Example**

Fictional rehearsal: a study script counted duplicate IDs (S); I owned the counting rule (T); I clarified the requirement, wrote a regression test and corrected the rule (A); that test passed, while database integration remained unverified (R). I learned to distinguish unit and integration evidence.

**Self-assessment rubric**

- 1 — Provides situation, task and personal concrete action, labeling fictional material.
- 1 — States observable result, learning and limitation without unsupported claims or confidential data.

Maximum: 2

</details>

**Prerequisites**

- [Behavioral evidence with STAR](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.md)

### behavioral.international-clarification

`mid` · `behavioral-international`

In an English-language interview, the requirement changes from returning the first occurrence of a target (or -1) to returning its first insertion position in a sorted list. Give a short English clarification, a discriminating example and an honest status update including a test you would add.

<details>
<summary>Expected answer</summary>

Acknowledge the changed contract, clarify whether equal values insert before the first equal, and restate the new requirement. For [2,4,7], target 5, the old result is -1 and the insertion index is 2. Propose a test for that case and duplicates; distinguish planned tests from executed ones. Use understandable English, not memorized jargon.

**Explanation:** A concrete example makes the changed contract observable; communication quality is about shared understanding, not accent.

**Interviewer intent:** Assess clarification, technical English and response to feedback.

**Common errors**

- Continue implementing the old contract or assert unexecuted tests passed.

**Follow-ups**

- How would you ask the interviewer to repeat an unfamiliar phrase?

**Example**

English rehearsal: "Let me restate the requirement. Should the insertion position be before equal values? For [2,4,7] and 5, I expect index 2. I would add this test; I have not run it yet."

**Self-assessment rubric**

- 1 — Uses understandable English to clarify and restate the changed contract.
- 1 — Gives a discriminating example and an honest test/status update.

Maximum: 2

</details>

**Prerequisites**

- [International interviews and technical English](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.md)
- [2. Binary search](../../problem-solving-and-live-coding/05-searching-algorithms/README.md)

### behavioral.evidence-disagreement

`senior` · `behavioral-international`

A teammate favors splitting a slow reporting service; you favor investigating a cache. In this fictional scenario, explain how you would resolve the disagreement using a shared goal, evidence, trade-offs, a documented decision and risk communication. Distinguish proposed work from actual outcomes.

<details>
<summary>Expected answer</summary>

Agree on a latency/reliability target and investigate baseline evidence before choosing. Hear the colleague's constraints; compare cache staleness, invalidation and memory with independent deployment/scaling and network cost. Agree a small experiment and decision record with success criteria, risks and rollback. State your role and team decision separately; without results, report the experiment as planned, not a verified gain.

**Explanation:** The goal is a supported decision and collaborative follow-through, not winning an argument.

**Interviewer intent:** Assess technical leadership, ownership and transparent risk communication.

**Common errors**

- Dismiss a teammate or invent performance improvements before measurement.

**Follow-ups**

- If the team chooses the other option, how would you support and monitor the agreed plan?

**Example**

Fictional plan: measure repeated read costs, agree acceptable staleness, test a bounded cache against baseline and document when to reject it. No improvement is claimed until measured.

**Self-assessment rubric**

- 1 — States shared goal, listens to alternatives and compares measurable trade-offs.
- 1 — Proposes documented experiment/decision with criteria, risk and rollback, distinguishing individual/team roles and planned/verified outcomes.

Maximum: 2

</details>

**Prerequisites**

- [Disagreement, ownership and trade-offs](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.md)

<!-- interview-questions:end -->

<!-- chapter-navigation:bottom -->
[← Previous](../21-software-engineering-and-technical-decisions/README.md) · [Module index](../README.md) · [Next →](../23-behavioral-and-international-interviews/README.md)
<!-- /chapter-navigation:bottom -->
