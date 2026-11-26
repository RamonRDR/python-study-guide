# Mock Interviews and Self-Assessment

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../23-behavioral-and-international-interviews/README.md) · [Module index](../README.md)
<!-- /chapter-navigation:top -->

## How to use the mocks

Study the prerequisites of the selected questions and exercise before the attempt; close answers and references during the session. Use a timer, a local Python 3.13 environment and a fresh copy of the starter outside the repository. Work alone or ask a partner to read the prompts, not solve them. No AI or hints during the independent attempt. These are practice allocations, not universal hiring thresholds. If you run out of time, stop and document what was actually completed. Exercise difficulty and interview seniority are distinct; the chosen exercises simply provide a progressive challenge. Browser execution remains unverified.

## Manual scoring

The five dimensions total 100 points: technical knowledge 25, problem solving 25, communication 20, tests and edge cases 15, engineering judgment 15. Each dimension lists observable indicators and three allowed bands: award full points if all listed indicators are demonstrated, partial points if at least one but not all is demonstrated, or zero if none is demonstrated. Do not award points for merely planned execution when an indicator requires an actual run. Record evidence and hints, and do not count accent, speaking speed or invented metrics. Scores are practice feedback, not certification or automatic semantic grading. The question bank's individual scores are separate. After the timer, review answers and compare with the existing exercise reference and trusted tests. Functional tests alone do not prove algorithm choice or complexity.

The canonical [mock index](../../interviews/mocks/mock-index.json) and records generate the sections below.

<!-- interview-mocks:start -->
## Junior mock

`mock.junior-30` · `junior`

**Duration (minutes):** 30

Use question 1 for the introduction (brief STAR); answer questions 2–4 aloud without opening answers. In a fresh practice directory, implement the linked exercise using its starter and original contract. Spend the coding and testing slots separately; run your own assertions for normal, empty and repeated/case-sensitive labels and check input preservation. In discussion, explain complexity, one alternative and any unfinished behavior. Stop at 30 minutes; do not open hints, solutions or reference answers until the timer ends.

| Phase | Minutes |
| --- | ---: |
| Introduction | 3 |
| Technical questions | 7 |
| Live coding | 13 |
| Tests | 4 |
| Discussion | 3 |

**Question sequence**

1. [`behavioral.star-evidence`](../22-technical-interview-question-bank/README.md#behavioralstar-evidence)
2. [`python.mutable-default`](../22-technical-interview-question-bank/README.md#pythonmutable-default)
3. [`algorithms.frequency-map`](../22-technical-interview-question-bank/README.md#algorithmsfrequency-map)
4. [`testing.specific-catch`](../22-technical-interview-question-bank/README.md#testingspecific-catch)

**Exercise:** [`problem-solving.label-counts`](../../exercises/problem-solving/label-counts/README.md)

### Scoring rubric

**Technical knowledge (0 / 12 / 25)**

- Predicts both mutable-default outputs and gives a None-based correction.
- Explains why a dictionary preserves counts and why ValueError is handled specifically.

**Problem solving (0 / 12 / 25)**

- Restates exact-label counting and traces a small duplicate example.
- Implements correct frequency accumulation and returns a dictionary without mutating input or printing.

**Communication (0 / 10 / 20)**

- Gives a concise truthful or explicitly fictional STAR with personal action and result.
- Explains the approach aloud and distinguishes completed, failed and untested behavior.

**Tests and edge cases (0 / 7 / 15)**

- Runs assertions for a normal duplicate case and empty input with exact expected values.
- Checks case-sensitive labels and confirms mutable input is unchanged; reports actual outcomes.

**Engineering judgment (0 / 7 / 15)**

- Explains expected O(n) time under bounded-label/hash assumptions and distinguishes required output space.
- Compares a set or repeated scans with a frequency map and states a limitation/next step.

**Self-evaluation:** After the timer, mark every demonstrated indicator with evidence (spoken explanation, code, or actual test output). Assign one band per dimension using the rule above; sum out of 100. Keep incomplete work visible. Record any hints separately. Question-bank points are diagnostic only and are not added to the mock score.

**Improvement:** Choose the lowest-scoring dimension; revisit its prerequisite, reimplement label counting with fresh examples and rerun empty, repeated and case-sensitive inputs. Repeat the mock later with a different comparable exercise; compare actual evidence, not just points.

## Mid-level mock

`mock.mid-45` · `mid`

**Duration (minutes):** 45

Start with question 1 in English, including the changed requirement and honest test status. Answer questions 2–4 in the technical slot. Implement the linked insertion-index exercise from its starter, keeping the original sorted-input contract; the 20-minute coding slot is shorter than its 22-minute standalone estimate. During tests, run your own assertions for empty input, duplicate values, absent targets below/between/above values and unchanged input. Discuss the half-open interval invariant, complexity assumptions, and unverified behavior. Stop at 45 minutes; no hints, solutions or reference answers during the attempt.

| Phase | Minutes |
| --- | ---: |
| Introduction | 5 |
| Technical questions | 10 |
| Live coding | 20 |
| Tests | 5 |
| Discussion | 5 |

**Question sequence**

1. [`behavioral.international-clarification`](../22-technical-interview-question-bank/README.md#behavioralinternational-clarification)
2. [`python.parameter-rebinding`](../22-technical-interview-question-bank/README.md#pythonparameter-rebinding)
3. [`sql.zero-child-count`](../22-technical-interview-question-bank/README.md#sqlzero-child-count)
4. [`api.idempotent-retry`](../22-technical-interview-question-bank/README.md#apiidempotent-retry)

**Exercise:** [`problem-solving.binary-insertion-index`](../../exercises/problem-solving/binary-insertion-index/README.md)

### Scoring rubric

**Technical knowledge (0 / 12 / 25)**

- Distinguishes parameter rebinding from shared mutation.
- Explains LEFT JOIN filter/count semantics including zero and stable group identity.
- Distinguishes POST retry risk from PUT/DELETE intended-effect idempotence and proposes bounded retry policy.

**Problem solving (0 / 12 / 25)**

- Restates first insertion position including duplicates and traces the half-open interval.
- Implements logarithmic binary search with correct bounds and no input mutation or scanning validation.

**Communication (0 / 10 / 20)**

- Clarifies changed requirement in understandable English and gives a discriminating example.
- Narrates the invariant and communicates actual test status and limitations without claiming unrun tests.

**Tests and edge cases (0 / 7 / 15)**

- Runs exact-value assertions for empty and duplicate cases.
- Runs missing-target cases below, between and above values and checks input preservation.

**Engineering judgment (0 / 7 / 15)**

- Justifies O(log n) comparisons and O(1) auxiliary space for sorted random-access input with bounded comparisons.
- Explains sortedness as a caller precondition and identifies the cost of a validating scan or a next verification step.

**Self-evaluation:** After the timer, mark every demonstrated indicator with evidence (spoken explanation, code, or actual test output). Assign one band per dimension using the rule above; sum out of 100. Keep incomplete work visible. Record any hints separately. Question-bank points are diagnostic only and are not added to the mock score.

**Improvement:** Choose the weakest dimension; trace a half-open interval on duplicate and absent targets, write a failing regression case for the specific gap and repeat with a fresh sorted list. Rehearse your English clarification without memorizing the sample.

## Senior mock

`mock.senior-60` · `senior`

**Duration (minutes):** 60

Use question 1 as a fictional introduction to collaborative decision-making; answer questions 2–4 in the technical slot. Implement the linked grouped-two-pointer exercise in a fresh practice directory, preserving its original contract. Its 40-minute standalone estimate is deliberately compressed into 25 minutes of coding; a correct partial solution and precise limitations are useful evidence, not a reason to hide incomplete work. Run your own assertions for empty, no-match, distinct duplicate groups, all-equal groups and input preservation in the testing slot. In discussion, justify grouped counting, complexity, transaction/authorization verification choices and one measurable risk. Stop at 60 minutes; no hints, solutions or reference answers until the timer ends.

| Phase | Minutes |
| --- | ---: |
| Introduction | 5 |
| Technical questions | 15 |
| Live coding | 25 |
| Tests | 5 |
| Discussion | 10 |

**Question sequence**

1. [`behavioral.evidence-disagreement`](../22-technical-interview-question-bank/README.md#behavioralevidence-disagreement)
2. [`internals.gil-workload`](../22-technical-interview-question-bank/README.md#internalsgil-workload)
3. [`api.object-authorization`](../22-technical-interview-question-bank/README.md#apiobject-authorization)
4. [`sql.atomic-transfer`](../22-technical-interview-question-bank/README.md#sqlatomic-transfer)

**Exercise:** [`problem-solving.sorted-pair-multiplicity`](../../exercises/problem-solving/sorted-pair-multiplicity/README.md)

### Scoring rubric

**Technical knowledge (0 / 12 / 25)**

- Distinguishes GIL-enabled and experimental free-threaded CPython 3.13 and proposes workload-appropriate concurrency with synchronization.
- Requires per-object authorization using verified identity and a consistent denial policy with no protected data.
- Explains ACID and a transaction with conditional debit, rollback and cross-connection commit evidence.

**Problem solving (0 / 12 / 25)**

- Restates distinct-index pair counting and explains the grouped two-pointer invariant and elimination rule.
- Implements distinct-group multiplication and the all-equal combination count without double counting, mutation or extra storage proportional to n.

**Communication (0 / 10 / 20)**

- Explains a fictional disagreement through shared goals, alternatives and evidence without invented outcomes.
- Communicates invariants, risks, verified results and any partial solution honestly.

**Tests and edge cases (0 / 7 / 15)**

- Runs exact-count tests for distinct duplicate groups and all-equal groups.
- Runs empty/no-match tests and verifies unchanged input; proposes independent oracle comparison for further validation.

**Engineering judgment (0 / 7 / 15)**

- Justifies linear time and constant auxiliary space under bounded arithmetic, without claiming tests prove complexity.
- Proposes measurable validation and rollback or mitigation for an engineering risk, with limitations of the verification.

**Self-evaluation:** After the timer, mark every demonstrated indicator with evidence (spoken explanation, code, or actual test output). Assign one band per dimension using the rule above; sum out of 100. Keep incomplete work visible. Record any hints separately. Question-bank points are diagnostic only and are not added to the mock score.

**Improvement:** Choose the weakest dimension; compare your grouped two-pointer solution with a small brute-force oracle on duplicates and all-equal input. Revisit GIL, authorization or decision-making prerequisites as indicated by the evidence. Repeat with another hard problem and document one risk you would validate.

<!-- interview-mocks:end -->

<!-- chapter-navigation:bottom -->
[← Previous](../23-behavioral-and-international-interviews/README.md) · [Module index](../README.md)
<!-- /chapter-navigation:bottom -->
