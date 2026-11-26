# Quiz bank

[English](README.md) | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)

The complete quiz bank contains 160 quizzes: 64 easy, 67 medium and 29 hard, worth 2,850 XP. It preserves the 78 foundation questions (including the original ten pilot questions) and adds 82 expansion questions.

Study the linked prerequisite sections first. Open a question JSON file and use the English prompt, explanation and hints. Answers are public: try each question before revealing its answer. For output prediction, reproduce exact output (including the final newline when specified); only LF normalization is allowed by the record. For code completion, supply only the requested text, symbol, function name or keyword. No browser execution is provided.

## 00 · Getting Started (8)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `configure-vscode` | [quiz.editor-replaces-interpreter](questions/quiz.editor-replaces-interpreter.json) | Easy |
| `git-and-version-control` | [quiz.git-inspect-staged](questions/quiz.git-inspect-staged.json) | Easy |
| `install-python` | [quiz.interpreter-purpose](questions/quiz.interpreter-purpose.json) | Easy |
| `packages-and-dependencies` | [quiz.install-declared-requirements](questions/quiz.install-declared-requirements.json) | Easy |
| `run-your-first-program` | [quiz.unclosed-print](questions/quiz.unclosed-print.json) | Easy |
| `run-your-first-program` | [quiz.unsaved-source-edit](questions/quiz.unsaved-source-edit.json) | Medium |
| `virtual-environments` | [quiz.venv-direct-executable](questions/quiz.venv-direct-executable.json) | Easy |
| `virtual-environments` | [quiz.venv-recreate](questions/quiz.venv-recreate.json) | Medium |

## 01 · Fundamentals (12)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `built-in-data-types` | [quiz.decimal-literal-type](questions/quiz.decimal-literal-type.json) | Easy |
| `built-in-data-types` | [quiz.quoted-digits-type](questions/quiz.quoted-digits-type.json) | Easy |
| `how-python-runs-a-program` | [quiz.source-file-extension](questions/quiz.source-file-extension.json) | Easy |
| `print-and-input` | [quiz.input-digits-text](questions/quiz.input-digits-text.json) | Easy |
| `print-and-input` | [quiz.print-custom-separator](questions/quiz.print-custom-separator.json) | Medium |
| `print-and-input` | [quiz.print-literal](questions/quiz.print-literal.json) | Easy |
| `type-and-isinstance` | [quiz.bool-int-exact-versus-compatible](questions/quiz.bool-int-exact-versus-compatible.json) | Hard |
| `type-and-isinstance` | [quiz.exact-type-function](questions/quiz.exact-type-function.json) | Easy |
| `type-conversion` | [quiz.integer-text-conversion](questions/quiz.integer-text-conversion.json) | Easy |
| `type-conversion` | [quiz.nonempty-false-text](questions/quiz.nonempty-false-text.json) | Medium |
| `variables-and-naming` | [quiz.assignment-symbol](questions/quiz.assignment-symbol.json) | Easy |
| `variables-and-naming` | [quiz.reassignment-order](questions/quiz.reassignment-order.json) | Medium |

## 02 · Strings and Numbers (12)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `common-string-methods` | [quiz.replace-does-not-mutate](questions/quiz.replace-does-not-mutate.json) | Medium |
| `common-string-methods` | [quiz.split-preserves-empty-fields](questions/quiz.split-preserves-empty-fields.json) | Medium |
| `common-string-methods` | [quiz.strip-surrounding-whitespace](questions/quiz.strip-surrounding-whitespace.json) | Easy |
| `int-float-and-bool` | [quiz.division-zero-error](questions/quiz.division-zero-error.json) | Easy |
| `int-float-and-bool` | [quiz.negative-floor-remainder](questions/quiz.negative-floor-remainder.json) | Hard |
| `int-float-and-bool` | [quiz.positive-remainder](questions/quiz.positive-remainder.json) | Medium |
| `int-float-and-bool` | [quiz.true-division-integers](questions/quiz.true-division-integers.json) | Easy |
| `numeric-builtins` | [quiz.absolute-distance-zero](questions/quiz.absolute-distance-zero.json) | Easy |
| `numeric-builtins` | [quiz.round-ties-to-even](questions/quiz.round-ties-to-even.json) | Medium |
| `string-creation-and-indexing` | [quiz.string-negative-index](questions/quiz.string-negative-index.json) | Easy |
| `string-creation-and-indexing` | [quiz.string-slice-exclusive-stop](questions/quiz.string-slice-exclusive-stop.json) | Medium |
| `string-creation-and-indexing` | [quiz.string-zero-index](questions/quiz.string-zero-index.json) | Easy |

## 03 · Collections (16)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `choosing-the-right-collection` | [quiz.collection-keyed-quantities](questions/quiz.collection-keyed-quantities.json) | Medium |
| `choosing-the-right-collection` | [quiz.collection-membership](questions/quiz.collection-membership.json) | Easy |
| `dictionaries-keys-and-values` | [quiz.dictionary-fallback](questions/quiz.dictionary-fallback.json) | Medium |
| `dictionaries-keys-and-values` | [quiz.dictionary-membership-keys](questions/quiz.dictionary-membership-keys.json) | Easy |
| `dictionaries-keys-and-values` | [quiz.dictionary-none-versus-absent](questions/quiz.dictionary-none-versus-absent.json) | Hard |
| `list-creation-and-indexing` | [quiz.list-slice-last-two](questions/quiz.list-slice-last-two.json) | Medium |
| `list-creation-and-indexing` | [quiz.list-stored-item-type](questions/quiz.list-stored-item-type.json) | Easy |
| `modifying-lists-and-methods` | [quiz.list-add-one](questions/quiz.list-add-one.json) | Easy |
| `modifying-lists-and-methods` | [quiz.list-extend-not-nest](questions/quiz.list-extend-not-nest.json) | Medium |
| `modifying-lists-and-methods` | [quiz.list-pop-result](questions/quiz.list-pop-result.json) | Medium |
| `modifying-lists-and-methods` | [quiz.shallow-list-copy-nested](questions/quiz.shallow-list-copy-nested.json) | Hard |
| `sets-and-unique-values` | [quiz.empty-braces-not-set](questions/quiz.empty-braces-not-set.json) | Easy |
| `sets-and-unique-values` | [quiz.set-directional-difference](questions/quiz.set-directional-difference.json) | Hard |
| `sets-and-unique-values` | [quiz.set-shared-members](questions/quiz.set-shared-members.json) | Medium |
| `tuples-and-immutability` | [quiz.singleton-tuple-comma](questions/quiz.singleton-tuple-comma.json) | Easy |
| `tuples-and-immutability` | [quiz.tuple-nested-mutability](questions/quiz.tuple-nested-mutability.json) | Medium |

## 04 · Program Flow (16)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `break-continue-and-loop-else` | [quiz.loop-else-break-versus-continue](questions/quiz.loop-else-break-versus-continue.json) | Hard |
| `choosing-and-combining-program-flow` | [quiz.combined-classification-loop](questions/quiz.combined-classification-loop.json) | Medium |
| `conditions-comparisons-and-boolean-logic` | [quiz.boolean-precedence](questions/quiz.boolean-precedence.json) | Medium |
| `conditions-comparisons-and-boolean-logic` | [quiz.chained-comparison-boundary](questions/quiz.chained-comparison-boundary.json) | Easy |
| `conditions-comparisons-and-boolean-logic` | [quiz.short-circuit-operand-result](questions/quiz.short-circuit-operand-result.json) | Hard |
| `for-loops-and-iteration` | [quiz.for-accumulator-initial-value](questions/quiz.for-accumulator-initial-value.json) | Medium |
| `for-loops-and-iteration` | [quiz.for-item-driven](questions/quiz.for-item-driven.json) | Easy |
| `if-elif-and-else` | [quiz.conditional-chain-one-branch](questions/quiz.conditional-chain-one-branch.json) | Easy |
| `if-elif-and-else` | [quiz.overlapping-threshold-order](questions/quiz.overlapping-threshold-order.json) | Medium |
| `match-and-case` | [quiz.match-guard-fallthrough](questions/quiz.match-guard-fallthrough.json) | Hard |
| `match-and-case` | [quiz.match-or-alternatives](questions/quiz.match-or-alternatives.json) | Medium |
| `match-and-case` | [quiz.match-wildcard](questions/quiz.match-wildcard.json) | Easy |
| `range-enumerate-and-zip` | [quiz.enumerate-default-start](questions/quiz.enumerate-default-start.json) | Easy |
| `range-enumerate-and-zip` | [quiz.range-stop](questions/quiz.range-stop.json) | Medium |
| `while-loops-and-state-driven-repetition` | [quiz.while-initial-false](questions/quiz.while-initial-false.json) | Easy |
| `while-loops-and-state-driven-repetition` | [quiz.while-state-overshoot](questions/quiz.while-state-overshoot.json) | Medium |

## 05 · Functions (14)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `args-and-kwargs` | [quiz.variadic-collection-shapes](questions/quiz.variadic-collection-shapes.json) | Medium |
| `data-flow-between-functions` | [quiz.discarded-return-does-not-rebind](questions/quiz.discarded-return-does-not-rebind.json) | Medium |
| `data-flow-between-functions` | [quiz.parameter-rebind-versus-mutation](questions/quiz.parameter-rebind-versus-mutation.json) | Hard |
| `default-values` | [quiz.default-argument-omission](questions/quiz.default-argument-omission.json) | Easy |
| `default-values` | [quiz.mutable-default-reuse](questions/quiz.mutable-default-reuse.json) | Hard |
| `defining-and-calling-functions` | [quiz.definition-body-delayed](questions/quiz.definition-body-delayed.json) | Easy |
| `functions-working-together` | [quiz.function-result-pipeline](questions/quiz.function-result-pipeline.json) | Medium |
| `parameters-and-arguments` | [quiz.missing-required-argument](questions/quiz.missing-required-argument.json) | Medium |
| `parameters-and-arguments` | [quiz.positional-argument-binding](questions/quiz.positional-argument-binding.json) | Easy |
| `return-values` | [quiz.implicit-none-return](questions/quiz.implicit-none-return.json) | Medium |
| `return-values` | [quiz.return-keyword](questions/quiz.return-keyword.json) | Easy |
| `scope` | [quiz.local-before-assignment](questions/quiz.local-before-assignment.json) | Hard |
| `scope` | [quiz.local-binding-shadow](questions/quiz.local-binding-shadow.json) | Medium |
| `type-hints` | [quiz.type-hints-runtime](questions/quiz.type-hints-runtime.json) | Easy |

## 06 · Comments and Documentation (8)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `comments` | [quiz.hash-inside-string](questions/quiz.hash-inside-string.json) | Easy |
| `comments-vs-logging` | [quiz.log-fallback-level](questions/quiz.log-fallback-level.json) | Medium |
| `docstrings` | [quiz.docstring-first-statement](questions/quiz.docstring-first-statement.json) | Easy |
| `docstrings` | [quiz.docstring-runtime-attribute](questions/quiz.docstring-runtime-attribute.json) | Medium |
| `meaningful-names` | [quiz.name-with-explicit-unit](questions/quiz.name-with-explicit-unit.json) | Easy |
| `pep8-and-readability` | [quiz.none-check-preserve-zero](questions/quiz.none-check-preserve-zero.json) | Hard |
| `pep8-and-readability` | [quiz.pep8-guidance-not-syntax](questions/quiz.pep8-guidance-not-syntax.json) | Medium |
| `task-markers` | [quiz.task-marker-no-runtime](questions/quiz.task-marker-no-runtime.json) | Easy |

## 07 · Errors, Files and Modules (12)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `imports-modules-and-packages` | [quiz.import-alias-keyword](questions/quiz.import-alias-keyword.json) | Medium |
| `imports-modules-and-packages` | [quiz.import-initialization-side-effect](questions/quiz.import-initialization-side-effect.json) | Hard |
| `imports-modules-and-packages` | [quiz.python-source-module](questions/quiz.python-source-module.json) | Easy |
| `open-and-with` | [quiz.append-preserve-existing-file](questions/quiz.append-preserve-existing-file.json) | Medium |
| `open-and-with` | [quiz.open-returns-file](questions/quiz.open-returns-file.json) | Easy |
| `raise-and-custom-exceptions` | [quiz.raise-keyword](questions/quiz.raise-keyword.json) | Easy |
| `raise-and-custom-exceptions` | [quiz.value-error-contract](questions/quiz.value-error-contract.json) | Medium |
| `try-except-else-finally` | [quiz.catch-invalid-integer](questions/quiz.catch-invalid-integer.json) | Easy |
| `try-except-else-finally` | [quiz.finally-propagates-unhandled](questions/quiz.finally-propagates-unhandled.json) | Hard |
| `try-except-else-finally` | [quiz.try-else-success-only](questions/quiz.try-else-success-only.json) | Medium |
| `txt-csv-and-json` | [quiz.csv-quoted-comma](questions/quiz.csv-quoted-comma.json) | Medium |
| `txt-csv-and-json` | [quiz.extension-does-not-parse](questions/quiz.extension-does-not-parse.json) | Easy |

## 08 · Standard Library (10)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `collections` | [quiz.counter-tally-purpose](questions/quiz.counter-tally-purpose.json) | Easy |
| `csv` | [quiz.csv-convert-before-validation](questions/quiz.csv-convert-before-validation.json) | Medium |
| `datetime` | [quiz.timedelta-duration](questions/quiz.timedelta-duration.json) | Easy |
| `decimal` | [quiz.decimal-exact-input-boundary](questions/quiz.decimal-exact-input-boundary.json) | Hard |
| `decimal` | [quiz.decimal-float-arithmetic-error](questions/quiz.decimal-float-arithmetic-error.json) | Medium |
| `itertools` | [quiz.chain-one-level](questions/quiz.chain-one-level.json) | Medium |
| `json` | [quiz.json-dumps-text-not-bytes](questions/quiz.json-dumps-text-not-bytes.json) | Medium |
| `logging` | [quiz.logging-handler-threshold](questions/quiz.logging-handler-threshold.json) | Medium |
| `os-shutil` | [quiz.os-getcwd-process-state](questions/quiz.os-getcwd-process-state.json) | Easy |
| `pathlib` | [quiz.relative-path-working-directory](questions/quiz.relative-path-working-directory.json) | Easy |

## 09 · External Libraries (8)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `openpyxl` | [quiz.openpyxl-formula-not-engine](questions/quiz.openpyxl-formula-not-engine.json) | Medium |
| `openpyxl` | [quiz.openpyxl-xlsx-format](questions/quiz.openpyxl-xlsx-format.json) | Easy |
| `pandas` | [quiz.dataframe-labeled-table](questions/quiz.dataframe-labeled-table.json) | Easy |
| `pandas` | [quiz.pandas-label-selection](questions/quiz.pandas-label-selection.json) | Medium |
| `pandas` | [quiz.pandas-merge-cardinality](questions/quiz.pandas-merge-cardinality.json) | Hard |
| `pytest` | [quiz.pytest-collect-only](questions/quiz.pytest-collect-only.json) | Medium |
| `requests` | [quiz.requests-explicit-timeout](questions/quiz.requests-explicit-timeout.json) | Easy |
| `requests` | [quiz.requests-json-not-success](questions/quiz.requests-json-not-success.json) | Medium |

## 10 · Practical Projects (8)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `csv-analyzer` | [quiz.csv-row-rejection-isolated](questions/quiz.csv-row-rejection-isolated.json) | Medium |
| `expense-tracker` | [quiz.expense-reject-zero](questions/quiz.expense-reject-zero.json) | Easy |
| `fictional-reconciliation-workflow` | [quiz.reconciliation-duplicate-source](questions/quiz.reconciliation-duplicate-source.json) | Medium |
| `file-organizer` | [quiz.organizer-exact-name-atomic-boundary](questions/quiz.organizer-exact-name-atomic-boundary.json) | Hard |
| `grade-calculator` | [quiz.grade-weight-atomic-rejection](questions/quiz.grade-weight-atomic-rejection.json) | Medium |
| `report-generator` | [quiz.report-inclusive-boundaries](questions/quiz.report-inclusive-boundaries.json) | Easy |
| `simulated-automation-flow` | [quiz.automation-failure-publication](questions/quiz.automation-failure-publication.json) | Hard |
| `user-registration` | [quiz.registration-canonical-uniqueness](questions/quiz.registration-canonical-uniqueness.json) | Medium |

## Manual Programming Practices (8)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `manual-coding-and-debugging` | [quiz.predict-before-execution](questions/quiz.predict-before-execution.json) | Easy |
| `manual-coding-and-debugging` | [quiz.traceback-diagnosis-first](questions/quiz.traceback-diagnosis-first.json) | Medium |
| `professional-workflow` | [quiz.green-ci-not-complete-proof](questions/quiz.green-ci-not-complete-proof.json) | Medium |
| `specification-driven-development` | [quiz.acceptance-observable-evidence](questions/quiz.acceptance-observable-evidence.json) | Easy |
| `specification-driven-development` | [quiz.sdd-exact-int-contract](questions/quiz.sdd-exact-int-contract.json) | Medium |
| `specification-driven-development` | [quiz.sdd-type-before-range](questions/quiz.sdd-type-before-range.json) | Hard |
| `test-driven-development` | [quiz.tdd-red-first](questions/quiz.tdd-red-first.json) | Easy |
| `test-driven-development` | [quiz.tdd-refactor-preserve-behavior](questions/quiz.tdd-refactor-preserve-behavior.json) | Medium |

## 11 · Problem Solving and Live Coding (14)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `algorithmic-complexity` | [quiz.big-o-not-seconds](questions/quiz.big-o-not-seconds.json) | Easy |
| `algorithmic-complexity` | [quiz.repeated-lookup-tradeoff](questions/quiz.repeated-lookup-tradeoff.json) | Medium |
| `algorithms-and-complexity` | [quiz.pair-duplicate-multiplicity](questions/quiz.pair-duplicate-multiplicity.json) | Hard |
| `constraints-and-edge-cases` | [quiz.capacity-inclusive-boundary](questions/quiz.capacity-inclusive-boundary.json) | Easy |
| `debugging` | [quiz.negative-window-initialization](questions/quiz.negative-window-initialization.json) | Medium |
| `functions-and-recursion` | [quiz.flatten-shared-accumulator](questions/quiz.flatten-shared-accumulator.json) | Hard |
| `mixed` | [quiz.inventory-order-and-delta](questions/quiz.inventory-order-and-delta.json) | Hard |
| `problem-solving-fundamentals` | [quiz.qualifying-minute-sum](questions/quiz.qualifying-minute-sum.json) | Easy |
| `problem-solving-patterns` | [quiz.rolling-window-update](questions/quiz.rolling-window-update.json) | Medium |
| `recursion` | [quiz.recursive-sum-trace](questions/quiz.recursive-sum-trace.json) | Medium |
| `searching-algorithms` | [quiz.binary-first-match-boundary](questions/quiz.binary-first-match-boundary.json) | Medium |
| `searching-and-sorting` | [quiz.binary-target-exclusive-end](questions/quiz.binary-target-exclusive-end.json) | Hard |
| `sorting-algorithms` | [quiz.insertion-stable-shift](questions/quiz.insertion-stable-shift.json) | Medium |
| `strings-and-numbers` | [quiz.distinct-window-monotonic](questions/quiz.distinct-window-monotonic.json) | Hard |

## 12 · Technical Interview Preparation (14)

| Chapter | Quiz ID | Difficulty |
|---|---|---|
| `api-contracts-authentication-and-authorization` | [quiz.authentication-not-object-authorization](questions/quiz.authentication-not-object-authorization.json) | Easy |
| `attributes-methods-and-object-behavior` | [quiz.classmethod-subclass-factory](questions/quiz.classmethod-subclass-factory.json) | Medium |
| `classes-and-objects` | [quiz.instance-initialization-role](questions/quiz.instance-initialization-role.json) | Easy |
| `closures-and-decorators` | [quiz.closure-late-binding-snapshot](questions/quiz.closure-late-binding-snapshot.json) | Hard |
| `concurrency-parallelism-and-the-gil` | [quiz.gil-compound-invariant](questions/quiz.gil-compound-invariant.json) | Hard |
| `context-managers` | [quiz.context-exit-false-propagation](questions/quiz.context-exit-false-propagation.json) | Medium |
| `http-rest-and-backend-fundamentals` | [quiz.http-get-retrieval](questions/quiz.http-get-retrieval.json) | Easy |
| `inheritance-polymorphism-and-composition` | [quiz.composition-replaceable-collaborator](questions/quiz.composition-replaceable-collaborator.json) | Medium |
| `iterators-generators-and-comprehensions` | [quiz.exhausted-generator-next](questions/quiz.exhausted-generator-next.json) | Medium |
| `joins-aggregations-and-data-relationships` | [quiz.left-join-zero-child-count](questions/quiz.left-join-zero-child-count.json) | Hard |
| `object-identity-references-and-copying` | [quiz.deepcopy-preserves-internal-alias](questions/quiz.deepcopy-preserves-internal-alias.json) | Medium |
| `python-memory-management` | [quiz.reachable-cache-retention](questions/quiz.reachable-cache-retention.json) | Hard |
| `relational-databases-and-sql` | [quiz.sql-check-null-constraint](questions/quiz.sql-check-null-constraint.json) | Medium |
| `transactions-indexes-and-sql-safety` | [quiz.transaction-failed-credit-rollback](questions/quiz.transaction-failed-credit-rollback.json) | Hard |

- [Exercise bank](../exercises/README.md)
- [Versioned exercise index](../exercises/problem-solving/exercise-index.json)
- [Assessment contract](../docs/specs/learning-hub-foundation/assessment-contract.md)
