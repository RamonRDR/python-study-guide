# Quiz bank

[English](README.md) | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)

The foundation bank contains 78 quizzes across modules 00–05: 37 easy, 30 medium and 11 hard, worth 1,300 XP. This includes the ten original pilot questions. The remaining 82 quizzes are planned for C2.

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

- [Exercise bank](../exercises/README.md)
- [Versioned exercise index](../exercises/problem-solving/exercise-index.json)
- [Assessment contract](../docs/specs/learning-hub-foundation/assessment-contract.md)
