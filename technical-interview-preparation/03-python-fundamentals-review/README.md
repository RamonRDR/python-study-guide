# Python Fundamentals Review

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../02-live-coding-and-take-home/README.md) · [Module index](../README.md) · [Next →](../04-data-structures-and-algorithms-review/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [fundamentals/03-variables-and-naming](../../fundamentals/03-variables-and-naming/README.md)
- [fundamentals/04-built-in-data-types](../../fundamentals/04-built-in-data-types/README.md)
- [fundamentals/06-type-conversion](../../fundamentals/06-type-conversion/README.md)
- [strings-and-numbers/02-common-string-methods](../../strings-and-numbers/02-common-string-methods/README.md)
- [program-flow/01-conditions-comparisons-and-boolean-logic](../../program-flow/01-conditions-comparisons-and-boolean-logic/README.md)
- [program-flow/02-if-elif-and-else](../../program-flow/02-if-elif-and-else/README.md)
- [program-flow/04-for-loops-and-iteration](../../program-flow/04-for-loops-and-iteration/README.md)
- [functions/01-defining-and-calling-functions](../../functions/01-defining-and-calling-functions/README.md)
- [functions/02-parameters-and-arguments](../../functions/02-parameters-and-arguments/README.md)
- [functions/03-return-values](../../functions/03-return-values/README.md)
- [functions/04-scope](../../functions/04-scope/README.md)
- [functions/06-default-values](../../functions/06-default-values/README.md)
- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.md)

## Review by reasoning

Use the linked chapters rather than relearning their syntax here. A name binds to an object; its type determines supported operations. Conversions may fail: `int("12")` works, but `int("twelve")` raises ValueError. Strings are immutable; methods return results. Conditions select execution; loops repeat work; functions have parameters, return values and local bindings. Explain a rule, show an example and describe a boundary.

```python
def add_tag(tags, tag):
    tags.append(tag)
    return tags

original = ["python"]
result = add_tag(original, "testing")
print(original, result)
```

Both names refer to the modified list. Rebinding the parameter to a new list would not rebind the caller's name. A default list is evaluated at function definition, not freshly on each call; use None when omission means a new list. See the linked data-flow and default-value lessons.

## Independent practice

Predict the output before running the snippet. Change the function to return a new list without mutating its input. Test an empty list and repeated tags. Explain whether duplicates are allowed by your chosen contract. Review LEGB, boolean short-circuiting, equality versus identity and why `is None` is appropriate. Do not infer identity from integer or string caching.

**Quick reference:** types, conversion, binding, mutation, conditions, loops, functions, scope and returns.

<!-- chapter-navigation:bottom -->
[← Previous](../02-live-coding-and-take-home/README.md) · [Module index](../README.md) · [Next →](../04-data-structures-and-algorithms-review/README.md)
<!-- /chapter-navigation:bottom -->
