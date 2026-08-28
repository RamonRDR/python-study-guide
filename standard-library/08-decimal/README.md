<div align="center">

# Engineering Decimal Precision and Rounding Contracts

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Standard Library](../README.md) · [← Previous: `itertools`](../07-itertools/README.md)

Python's built-in `float` is the right tool for a large amount of numerical work, but it models numbers with binary floating-point. Chapter 03 of Strings and Numbers already showed why a value such as `0.1` may not have an exact binary representation.

The `decimal` module solves a different problem. It provides decimal floating-point arithmetic with explicit control over representation, precision, rounding, exceptional conditions, and validation.

This chapter is not about replacing every `float` with `Decimal`. It is about choosing a numeric contract deliberately when decimal digits themselves are part of the meaning of the data.

**Estimated study time:** 180–240 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain what `Decimal` solves and what it does not solve;
- construct decimal values without accidentally importing binary floating-point approximation;
- distinguish exact decimal representation from unlimited-precision arithmetic;
- explain sign, coefficient digits, exponent, and preserved trailing zeros;
- inspect representation with `as_tuple()` and distinguish value equality from representation ordering;
- explain why context precision counts significant digits rather than decimal places;
- inspect and temporarily override the active arithmetic context;
- choose rounding rules explicitly instead of relying on an accidental default;
- use `quantize()` to enforce a target exponent or fixed decimal scale;
- distinguish `Rounded` from `Inexact` signals;
- use flags for monitoring and traps for enforcement;
- validate a decimal scale by trapping `Inexact`;
- handle `Infinity`, `NaN`, signaling NaN, and signed zero deliberately;
- recognize when arithmetic with `Decimal` and `float` is intentionally rejected;
- use `FloatOperation` to detect implicit float conversion paths;
- explain the purpose of `BasicContext`, `ExtendedContext`, and explicit `Context` objects;
- use `fma()` when one rounding instead of an intermediate rounding matters;
- choose safe boundaries for JSON, text, databases, APIs, and user input;
- recognize performance, interoperability, and maintainability trade-offs;
- test decimal policies as behavior, not only as formatted output.

## 1. The problem is not that `float` is broken

Binary floating-point is a deliberate representation model. It is fast, widely supported by hardware, and appropriate for scientific, graphical, statistical, and many general numerical workloads.

The mismatch appears when the **decimal representation itself is part of the contract**.

```python
print(0.1 + 0.1 + 0.1 == 0.3)
```

```text
False
```

That result comes from binary representation error, not from Python forgetting arithmetic.

## 2. `Decimal` uses decimal representation

```python
from decimal import Decimal


result = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")
print(result)
print(result == Decimal("0.3"))
```

```text
0.3
True
```

The decimal strings can be represented exactly as decimal numbers.

## 3. Exact representation does not mean every result is exact forever

A crucial distinction:

```text
exact decimal input
        ↓
Decimal representation
        ↓
arithmetic under a finite context precision
        ↓
possibly rounded result
```

For example, `1 / 7` has an infinite decimal expansion.

```python
from decimal import Decimal, localcontext


with localcontext(prec=8):
    print(Decimal(1) / Decimal(7))
```

```text
0.14285714
```

`Decimal` removes binary representation error for decimal inputs. It does not make finite precision disappear.

## 4. Import the names your code actually uses

For learning examples, explicit imports keep dependencies visible:

```python
from decimal import Decimal, ROUND_HALF_EVEN
```

The module exposes many contexts, signals, and rounding constants. Avoid `from decimal import *` in normal application code when explicit names make the numeric policy easier to audit.

## 5. Prefer strings when the source value is decimal text

```python
from decimal import Decimal


price = Decimal("19.90")
rate = Decimal("0.075")

print(price)
print(rate)
```

A string constructor expresses the decimal digits directly.

## 6. Integers convert exactly

```python
from decimal import Decimal


quantity = Decimal(7)
print(quantity)
```

```text
7
```

Integer-to-Decimal conversion is exact.

## 7. Passing a `float` preserves the exact binary float value

This is one of the most important boundaries in the module:

```python
from decimal import Decimal


print(Decimal(0.1))
```

The result contains many digits because Python converts the already-existing binary float **exactly** into its decimal equivalent.

That is different from:

```python
from decimal import Decimal


print(Decimal("0.1"))
```

The second form represents the decimal value one tenth directly.

## 8. `Decimal.from_float()` makes that boundary explicit

```python
from decimal import Decimal


converted = Decimal.from_float(0.1)
print(converted)
```

Use this when preserving the exact value of an existing `float` is the actual intent.

It is not a shortcut for recovering decimal text that existed before the float was created.

## 9. `Decimal.from_number()` is a Python 3.14 addition

Python 3.14 adds an alternative constructor that accepts `int`, `float`, or `Decimal`, but not strings or tuples:

```python
from decimal import Decimal


value = Decimal.from_number(314)
print(value)
```

When compatibility with Python versions before 3.14 matters, use the older constructors appropriate to the source type.

## 10. Decide where the decimal contract begins

A robust boundary often looks like:

```text
text / database decimal / validated API text
                    ↓
              Decimal(...)
                    ↓
          Decimal-only calculation
                    ↓
      explicit rounding / quantization
                    ↓
         output or persistence boundary
```

Converting to `Decimal` only after several binary-float calculations does not erase approximation already introduced upstream.

## 11. `Decimal` and `float` do not generally mix in arithmetic

```python
from decimal import Decimal


amount = Decimal("1.25")
# amount + 0.5  # TypeError
```

This rejection is useful. It prevents a pipeline from silently mixing two different numeric models.

Comparisons have separate rules, but ordinary arithmetic should usually stay inside one deliberate numeric representation.

## 12. A Decimal has sign, coefficient digits, and exponent

Conceptually:

```text
Decimal("12.340")

sign        = positive
coefficient = 1, 2, 3, 4, 0
exponent    = -3
```

The exponent describes the decimal scale relative to the coefficient.

## 13. Trailing zeros can preserve significance

```python
from decimal import Decimal


print(Decimal("1.20"))
print(Decimal("1.2000"))
```

```text
1.20
1.2000
```

The values compare numerically equal, but their stored representations retain different trailing-zero information.

## 14. Inspect representation with `as_tuple()`

```python
from decimal import Decimal


value = Decimal("12.340")
print(value.as_tuple())
```

The result exposes the sign, coefficient digits, and exponent as a named tuple.

## 15. Numeric equality ignores representational differences

```python
from decimal import Decimal


print(Decimal("12.0") == Decimal("12.00"))
```

```text
True
```

The numbers have the same numeric value.

## 16. `compare_total()` can distinguish representations

When representation itself matters, `compare_total()` provides a total ordering based on the abstract Decimal representation:

```python
from decimal import Decimal


left = Decimal("12.0")
right = Decimal("12")
print(left.compare_total(right))
```

Do not use representation-sensitive comparison when ordinary numeric equality is the real requirement.

## 17. Decimal objects are immutable

Arithmetic creates new values rather than changing existing Decimal objects.

```python
from decimal import Decimal


amount = Decimal("10.00")
updated = amount + Decimal("2.50")

print(amount)
print(updated)
```

```text
10.00
12.50
```

This behaves naturally with functions, dictionary keys, sets, and repeatable calculations.

## 18. Arithmetic happens under a context

The arithmetic context controls properties such as:

- precision;
- rounding mode;
- exponent limits;
- signal flags;
- trap enablers.

Think of the context as the **numeric execution policy** surrounding Decimal operations.

## 19. Inspect the active context with `getcontext()`

```python
from decimal import getcontext


context = getcontext()
print(context.prec)
print(context.rounding)
```

The standard default precision is 28 digits and the default rounding mode is `ROUND_HALF_EVEN` unless the active context has been changed.

## 20. Precision means significant digits, not decimal places

This distinction is essential.

```python
from decimal import Decimal, localcontext


with localcontext(prec=4):
    print(Decimal("12345") + Decimal("1"))
    print(Decimal("1.2345") + Decimal("0"))
```

The context precision limits significant digits in arithmetic results. It does not mean "always keep four digits after the decimal point."

Use `quantize()` when a fixed exponent or scale is required.

## 21. Construction from a string does not round to context precision

```python
from decimal import Decimal, localcontext


with localcontext(prec=4):
    value = Decimal("3.1415926535")
    print(value)
```

The constructor preserves the digits supplied by the string. Context precision becomes relevant when arithmetic is performed.

## 22. Arithmetic applies the context

```python
from decimal import Decimal, localcontext


with localcontext(prec=6):
    result = Decimal("3.1415926535") + Decimal("2.7182818285")
    print(result)
```

```text
5.85987
```

The exact operands contain more digits than the result precision permits, so rounding occurs.

## 23. Avoid changing global arithmetic policy casually

This works:

```python
from decimal import getcontext


getcontext().prec = 50
```

But mutating the active context in reusable library code can surprise callers whose calculations share that context.

Prefer a local scope when the precision or rounding rule belongs only to one operation.

## 24. `localcontext()` scopes temporary policy

```python
from decimal import Decimal, getcontext, localcontext


original_precision = getcontext().prec

with localcontext(prec=8):
    result = Decimal(1) / Decimal(7)

print(result)
print(getcontext().prec == original_precision)
```

The previous context is restored after the `with` block.

Keyword arguments for setting context attributes directly in `localcontext()` are available starting with Python 3.11.

## 25. Explicit `Context` objects make policy portable

```python
from decimal import Context, Decimal, ROUND_HALF_UP


policy = Context(prec=12, rounding=ROUND_HALF_UP)
result = policy.divide(Decimal(1), Decimal(7))
print(result)
```

An explicit context can be passed or reused as a policy object instead of relying on ambient state.

## 26. `Context.create_decimal()` applies context during conversion

The ordinary `Decimal` constructor does not trim input digits according to context precision.

`Context.create_decimal()` is different: it applies that context's precision, rounding, flags, and traps during conversion.

```python
from decimal import Context, ROUND_DOWN


policy = Context(prec=5, rounding=ROUND_DOWN)
value = policy.create_decimal("3.1415926")
print(value)
```

```text
3.1415
```

Use this when input normalization is intentionally part of the context policy.

## 27. Rounding is a business or numerical rule, not decoration

Formatting controls presentation. Rounding changes the numeric value.

Those are separate decisions:

```text
calculation precision
        ≠
quantization policy
        ≠
display formatting
```

Make each one explicit when correctness depends on it.

## 28. `ROUND_HALF_EVEN` is the default context mode

Half-even rounds to the nearest result and resolves an exact tie toward the candidate whose last retained digit is even.

```python
from decimal import Decimal, ROUND_HALF_EVEN


whole = Decimal("1")
print(Decimal("2.5").quantize(whole, rounding=ROUND_HALF_EVEN))
print(Decimal("3.5").quantize(whole, rounding=ROUND_HALF_EVEN))
```

```text
2
4
```

Do not call this "round down at .5". The tie depends on which neighboring result is even.

## 29. `ROUND_HALF_UP` resolves ties away from zero

```python
from decimal import Decimal, ROUND_HALF_UP


whole = Decimal("1")
print(Decimal("2.5").quantize(whole, rounding=ROUND_HALF_UP))
print(Decimal("-2.5").quantize(whole, rounding=ROUND_HALF_UP))
```

```text
3
-3
```

Choose a rounding mode because the domain requires it, not because its name sounds familiar.

## 30. Directional rounding modes have distinct contracts

The module also includes:

```text
ROUND_CEILING  -> toward +Infinity
ROUND_FLOOR    -> toward -Infinity
ROUND_DOWN     -> toward zero
ROUND_UP       -> away from zero
ROUND_HALF_DOWN
ROUND_05UP
```

The behavior for negative numbers is why "up" and "ceiling" must not be treated as synonyms.

## 31. `quantize()` imposes the exponent of another Decimal

```python
from decimal import Decimal


value = Decimal("1.41421356")
rounded = value.quantize(Decimal("1.000"))
print(rounded)
```

```text
1.414
```

The right-hand operand acts as an exponent template.

## 32. Use a named quantum for repeated fixed-scale work

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")
amount = Decimal("12.345")

print(amount.quantize(CENT, rounding=ROUND_HALF_UP))
```

```text
12.35
```

A named quantum makes the scale contract visible and reusable.

## 33. Quantize after operations that can change scale

Multiplication and division can produce more decimal places than a fixed-scale domain permits.

```python
from decimal import Decimal, ROUND_HALF_EVEN


CENT = Decimal("0.01")
amount = Decimal("10.00")
rate = Decimal("0.0375")
raw_result = amount * rate
final_result = raw_result.quantize(CENT, rounding=ROUND_HALF_EVEN)

print(raw_result)
print(final_result)
```

The right place to quantize depends on the domain's rule. Do not insert rounding after every operation automatically.

## 34. Quantization can also validate scale

A scale validator should define both the allowed scale and the supported magnitude. `quantize()` can signal `InvalidOperation` when the coefficient of the quantized result would exceed the context precision. The validator below traps both conditions and explicitly limits accepted coefficient digits:

```python
from decimal import Context, Decimal, Inexact, InvalidOperation


TWO_PLACES = Decimal("0.01")
MAX_COEFFICIENT_DIGITS = 28
validator = Context(
    prec=MAX_COEFFICIENT_DIGITS,
    traps=[Inexact, InvalidOperation],
)

value = Decimal("3.21")

if not value.is_finite() or len(value.as_tuple().digits) > MAX_COEFFICIENT_DIGITS:
    raise ValueError("unsupported decimal value")

print(value.quantize(TWO_PLACES, context=validator))
```

A value such as `Decimal("3.214")` raises `Inexact`. Oversized or non-finite values are rejected before they can fall through as an accepted `NaN`, while `InvalidOperation` is also trapped as a defensive backstop.

## 35. `quantize()` has a special Underflow rule

Unlike other operations, `quantize()` never signals `Underflow`, even when the result is subnormal and inexact.

This is an advanced contract, but it matters when signal monitoring is part of a validation or numerical-control design.

## 36. `round()` and Decimal context interact differently depending on arguments

```python
from decimal import Decimal


value = Decimal("2.675")
print(round(value, 2))
```

With an integer `ndigits`, Decimal rounding respects the context rounding mode and is equivalent to quantizing to the corresponding power of ten.

By contrast, `round(decimal_value)` without `ndigits` returns an `int`, resolves ties to even, and ignores the Decimal context's rounding mode.

## 37. `to_integral_value()` rounds without signaling `Inexact` or `Rounded`

```python
from decimal import Decimal, ROUND_HALF_UP


value = Decimal("7.8")
print(value.to_integral_value(rounding=ROUND_HALF_UP))
```

Use this when an integral Decimal result is needed without those rounding signals.

## 38. `to_integral_exact()` reports rounding conditions

```python
from decimal import Decimal, Inexact, Rounded, localcontext


with localcontext() as context:
    context.clear_flags()
    result = Decimal("7.8").to_integral_exact()
    print(result)
    print(context.flags[Rounded])
    print(context.flags[Inexact])
```

The `exact` variant is useful when monitoring whether information was discarded.

## 39. Signals are part of the Decimal contract

Signals describe conditions encountered during decimal arithmetic.

Important examples include:

- `Clamped`;
- `DivisionByZero`;
- `InvalidOperation`;
- `Inexact`;
- `Rounded`;
- `Subnormal`;
- `Overflow`;
- `Underflow`;
- `FloatOperation`.

A signal can set a flag, raise through a trap, or do both in sequence.

## 40. Flags are sticky

Once a signal flag becomes true, it remains set until cleared.

```python
from decimal import Decimal, Inexact, localcontext


with localcontext(prec=5) as context:
    context.clear_flags()
    Decimal(1) / Decimal(7)
    print(context.flags[Inexact])
```

```text
True
```

Always clear flags before a calculation that you intend to monitor independently.

## 41. `Rounded` and `Inexact` are not the same condition

`Rounded` means digits were discarded.

`Inexact` means discarded digits contained non-zero information, so the result differs from the exact mathematical result.

For example, reducing `5.00` to `5.0` can signal `Rounded` even though no non-zero information was lost.

## 42. Traps turn selected signals into exceptions

```python
from decimal import Decimal, DivisionByZero, localcontext


with localcontext() as context:
    context.traps[DivisionByZero] = True
    # Decimal(1) / Decimal(0)  # raises DivisionByZero
```

A trap is an enforcement rule. A flag is an observation record.

## 43. Choose traps according to the contract

Possible policies include:

```text
monitor and continue -> inspect flags
reject inexact input -> trap Inexact
reject divide by zero -> trap DivisionByZero
reject accidental float conversion -> trap FloatOperation
```

Do not enable every trap merely because exceptions feel safer. The desired semantics depend on the application.

## 44. `FloatOperation` can expose implicit float boundaries

```python
from decimal import Decimal, FloatOperation, localcontext


with localcontext() as context:
    context.traps[FloatOperation] = True
    # Decimal(3.14)  # raises FloatOperation
```

Explicit conversion through `Decimal.from_float()` does not signal `FloatOperation`, because the conversion intent is already visible.

## 45. Equality comparison with float has a special allowance

Decimal and float arithmetic is generally rejected, but comparison rules are more nuanced.

When `FloatOperation` is trapped, ordering comparisons such as `<` can raise, while equality comparisons remain permitted.

Do not build a numeric pipeline around mixed-type comparison quirks. Normalize numeric boundaries deliberately instead.

## 46. `BasicContext` is useful for debugging

`BasicContext` has precision 9, uses `ROUND_HALF_UP`, and enables many traps.

That makes unexpected conditions visible quickly during debugging.

```python
from decimal import BasicContext


print(BasicContext.prec)
print(BasicContext.rounding)
```

## 47. `ExtendedContext` prefers result values over exceptions

`ExtendedContext` has precision 9, uses `ROUND_HALF_EVEN`, and has no traps enabled.

An operation such as division by zero can therefore produce `Infinity` while recording the signal instead of immediately raising.

Use such behavior only when special numeric values are an intentional part of the algorithm.

## 48. The default context is not the same thing as `BasicContext`

The ordinary default context uses precision 28 and `ROUND_HALF_EVEN`, with traps enabled for `Overflow`, `InvalidOperation`, and `DivisionByZero`.

Do not infer default behavior from the settings of the named standard contexts.

## 49. `IEEEContext()` is new in Python 3.14

Python 3.14 adds `decimal.IEEEContext(bits)` for creating a context configured for one of the supported IEEE interchange formats.

```python
from decimal import IEEEContext


context = IEEEContext(128)
print(context.prec)
```

Code that must run on earlier Python versions should not depend on this API without a compatibility strategy.

## 50. Decimal supports special values

```python
from decimal import Decimal


values = [
    Decimal("Infinity"),
    Decimal("-Infinity"),
    Decimal("NaN"),
    Decimal("sNaN"),
    Decimal("-0"),
]

for value in values:
    print(value)
```

These are arithmetic values with defined Decimal semantics, not ordinary error strings.

## 51. Classify special values before ordinary processing when needed

```python
from decimal import Decimal


value = Decimal("Infinity")
print(value.is_finite())
print(value.is_infinite())
print(value.is_nan())
```

Validation boundaries often need to reject non-finite values before persistence or downstream calculations.

## 52. NaN does not behave like an ordinary number

A NaN represents an undefined or unrepresentable numeric result.

Do not rely on ordinary ordering logic for NaN values. Detect them explicitly with `is_nan()` when the domain disallows them.

Signaling NaNs (`sNaN`) are designed to signal `InvalidOperation` when used in most operations.

## 53. Signed zero can preserve directional information

Decimal distinguishes positive and negative zero representations:

```python
from decimal import Decimal


positive_zero = Decimal("0")
negative_zero = Decimal("-0")

print(positive_zero == negative_zero)
print(negative_zero.is_signed())
```

The values compare equal numerically even though sign information can remain in the representation.

## 54. Finite precision can still cause loss of significance

Decimal arithmetic can round whenever a result exceeds context precision.

```python
from decimal import Decimal, localcontext


with localcontext(prec=5):
    large = Decimal("10000")
    small = Decimal("0.12345")
    result = large + small
    print(result)
```

The decimal model prevents binary representation error, but a low precision can still discard meaningful decimal digits.

## 55. Increasing precision can be part of a numerical strategy

For intermediate calculations, it can be appropriate to use more precision than the final output needs and round only at the required boundary.

```python
from decimal import Decimal, localcontext


with localcontext(prec=30):
    ratio = Decimal(1) / Decimal(7)

print(ratio)
```

The required working precision is a property of the algorithm and domain, not a universal magic number.

## 56. `fma()` avoids rounding the intermediate product

Fused multiply-add computes:

```text
self * other + third
```

without rounding the intermediate multiplication result.

```python
from decimal import Decimal


value = Decimal("2").fma(Decimal("3"), Decimal("5"))
print(value)
```

```text
11
```

This can matter in precision-sensitive formulas where an intermediate rounding would otherwise alter the final result.

## 57. `normalize()` simplifies representation while preserving value

```python
from decimal import Decimal


print(Decimal("32.1000").normalize())
```

```text
32.1
```

Use normalization when significance encoded by trailing zeros is not needed. Do not normalize automatically if representation carries domain meaning.

## 58. Formatting is not a substitute for quantization

```python
from decimal import Decimal


value = Decimal("2.675")
print(f"{value:.2f}")
print(value)
```

Formatting produces text for display. The original Decimal object is still unchanged.

If downstream calculations require a value at a fixed scale, create that numeric value explicitly with the required rounding policy.

## 59. Parse decimal JSON numbers deliberately

The earlier JSON chapter introduced this boundary:

```python
import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
```

`parse_float=Decimal` lets the decoder construct a Decimal from the JSON number's textual form instead of first converting it to a Python `float`.

## 60. JSON encoding needs its own explicit policy

The standard `json` encoder does not serialize arbitrary `Decimal` objects as JSON numbers automatically.

Possible application designs include:

- convert to a string when the external schema defines a string;
- use an integer minor-unit representation when that schema is appropriate;
- implement a deliberate custom encoding boundary;
- use another serialization technology with a native decimal type.

Do not silently coerce a Decimal to float merely to make serialization convenient if exact decimal semantics matter.

## 61. Preserve decimal text at input boundaries

Suppose a form supplies:

```text
19.90
```

Prefer:

```python
from decimal import Decimal


raw_value = "19.90"
amount = Decimal(raw_value)
```

over converting the text to float first and then to Decimal.

## 62. Database boundaries should respect the database numeric type

When a database driver exposes an exact numeric or decimal column as `Decimal`, keeping that value as Decimal avoids an unnecessary float round trip.

Driver behavior varies, so inspect the actual adapter contract rather than assuming every numeric column arrives with the same Python type.

## 63. API contracts should state the representation

"Number" is often too vague for precision-sensitive data.

Useful contract questions include:

- Is the value JSON number text or JSON string text?
- How many decimal places are allowed?
- Which rounding mode applies?
- Are trailing zeros meaningful?
- Are non-finite values allowed?
- Who performs final quantization?

Numeric correctness starts at the boundary, not at the final arithmetic expression.

## 64. Keep rounding policy close to the domain rule

A helper can make policy explicit:

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")


def to_cents(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)
```

The helper name and tests should explain why that rounding mode is correct for the domain using it.

## 65. Avoid hidden context mutation inside helpers

A risky helper changes ambient state:

```python
from decimal import getcontext


def calculate_something():
    getcontext().prec = 6
    # calculation continues
```

A safer design either:

- uses `localcontext()`;
- accepts an explicit `Context`;
- documents that context mutation is part of the public API.

Local policy is easier to reason about than invisible global side effects.

## 66. Decimal contexts and concurrency deserve deliberate design

The active decimal context is managed independently for execution contexts according to the Python build and context-management support.

The practical rule is simpler: do not use uncontrolled ambient context mutation as a communication mechanism between concurrent tasks.

Pass policy explicitly or scope changes with `localcontext()` when isolation matters.

## 67. Decimal is usually slower than binary float

Decimal arithmetic provides richer decimal semantics, software-controlled context, and signal handling. Those features have a cost.

Do not choose Decimal for every numeric workload merely because it sounds "more precise."

Choose it when decimal representation, rounding control, auditability, or exact decimal boundaries justify the trade-off.

## 68. Decimal is not the same as rational arithmetic

`Decimal("0.1")` is exactly representable, but a repeating value such as one third still needs finite precision during division.

For algorithms whose contract is exact ratios such as `1/3`, the standard-library `fractions.Fraction` type models a different form of exactness.

Numeric type selection should follow the mathematical model the program needs.

## 69. A practical fixed-scale calculation

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")

unit_price = Decimal("19.95")
quantity = 3
discount = Decimal("2.50")

subtotal = unit_price * quantity
final_amount = (subtotal - discount).quantize(
    CENT,
    rounding=ROUND_HALF_UP,
)

print(f"subtotal: {subtotal}")
print(f"final: {final_amount}")
```

```text
subtotal: 59.85
final: 57.35
```

The important part is not that this example uses money. The important part is that input representation, arithmetic, final scale, and rounding policy are all visible.

## 70. A practical local precision calculation

```python
from decimal import Decimal, getcontext, localcontext


default_precision = getcontext().prec

with localcontext(prec=8):
    result = Decimal(1) / Decimal(7)

print(f"default precision: {default_precision}")
print(f"local result: {result}")
print(f"restored precision: {getcontext().prec}")
```

With the standard default context, the visible output is:

```text
default precision: 28
local result: 0.14285714
restored precision: 28
```

## 71. A practical scale validator

```python
from decimal import Context, Decimal, Inexact, InvalidOperation


TWO_PLACES = Decimal("0.01")
MAX_COEFFICIENT_DIGITS = 28
validator = Context(
    prec=MAX_COEFFICIENT_DIGITS,
    traps=[Inexact, InvalidOperation],
)


def normalize_two_places(raw_value: str) -> Decimal:
    value = Decimal(raw_value)

    if (
        not value.is_finite()
        or len(value.as_tuple().digits) > MAX_COEFFICIENT_DIGITS
    ):
        raise ValueError("unsupported decimal value")

    normalized = value.quantize(TWO_PLACES, context=validator)

    if not normalized.is_finite():
        raise ValueError("quantization produced a non-finite result")

    return normalized


for raw_value in [
    "12.50",
    "7.00",
    "3.141",
    "12345678901234567890123456789.00",
    "NaN",
]:
    try:
        normalized = normalize_two_places(raw_value)
    except (Inexact, InvalidOperation, ValueError):
        print(f"rejected: {raw_value}")
    else:
        print(f"accepted: {normalized}")
```

```text
accepted: 12.50
accepted: 7.00
rejected: 3.141
rejected: 12345678901234567890123456789.00
rejected: NaN
```

This validator has two explicit policies: at most 28 coefficient digits and a two-place result that does not discard non-zero digits. It also rejects non-finite values and traps `InvalidOperation`, so an invalid quantization cannot be accepted as `NaN`.

## 72. A practical signal monitor

```python
from decimal import Decimal, Inexact, Rounded, localcontext


with localcontext(prec=5) as context:
    context.clear_flags()
    result = Decimal(1) / Decimal(7)

    print(f"result: {result}")
    print(f"rounded: {context.flags[Rounded]}")
    print(f"inexact: {context.flags[Inexact]}")
```

```text
result: 0.14286
rounded: True
inexact: True
```

## 73. Common mistakes

### Mistake: constructing from a float when the original source is decimal text

```python
from decimal import Decimal


bad_boundary = Decimal(0.1)
good_boundary = Decimal("0.1")
```

The two constructors preserve different source values.

### Mistake: treating precision as decimal places

```python
from decimal import localcontext


with localcontext(prec=2):
    pass
```

`prec=2` means two significant digits for arithmetic, not two digits after the decimal point.

### Mistake: formatting instead of defining a numeric rounding policy

```python
from decimal import Decimal


value = Decimal("12.345")
print(f"{value:.2f}")
```

That is presentation. It does not mutate `value` into a two-place Decimal.

### Mistake: reading stale flags

If a previous operation set `Inexact`, a later check can be misleading unless flags were cleared before the monitored calculation.

### Mistake: using one ambient context as hidden shared state

A function that silently changes precision can alter unrelated calculations later in the same execution context.

### Mistake: converting to float at the final integration boundary without checking the contract

A float conversion may be acceptable for a visualization API, or unacceptable for an exact persisted value. The destination contract decides.

## 74. Decision table

| Requirement | Prefer |
|---|---|
| fast general binary floating-point arithmetic | `float` |
| exact decimal input representation | `Decimal` from text or exact decimal source |
| explicit fixed decimal scale | `Decimal.quantize()` |
| temporary working precision | `localcontext()` |
| reusable explicit numeric policy | `Context` |
| observe rounding without raising | signal flags |
| reject a specific arithmetic condition | traps |
| preserve an existing float exactly | `Decimal.from_float()` |
| detect accidental float conversion | `FloatOperation` |
| exact rational ratios | consider `fractions.Fraction` |
| display-only decimal formatting | format specification / f-string |

## 75. Quick reference

```text
Decimal("1.25")
Decimal(7)
Decimal.from_float(0.1)
Decimal.from_number(value)        # Python 3.14+

getcontext()
setcontext(context)
localcontext()
localcontext(prec=40)             # keyword attributes: Python 3.11+
Context(prec=28, rounding=...)
Context.create_decimal(value)

value.quantize(Decimal("0.01"))
value.to_integral_value()
value.to_integral_exact()
value.normalize()
value.as_tuple()
value.compare_total(other)
value.fma(other, third)

context.clear_flags()
context.flags[Inexact]
context.flags[Rounded]
context.traps[Inexact] = True
context.traps[FloatOperation] = True

BasicContext
ExtendedContext
DefaultContext
IEEEContext(bits)                 # Python 3.14+
```

## 76. Design checklist

Before choosing or configuring Decimal, ask:

- Where does the value originate?
- Does the source already exist as binary float?
- Is exact decimal representation required?
- How many significant digits does the calculation need?
- Does the domain require a fixed number of decimal places?
- Which rounding rule applies, and at which step?
- Is rounding an accepted transformation or a validation failure?
- Do I need to monitor `Rounded` or `Inexact`?
- Should any signals become exceptions through traps?
- Are `NaN` and infinities valid domain values?
- Do trailing zeros carry meaning?
- Will another library or API coerce the value to float?
- Is ambient context mutation safe here?
- Would an explicit `Context` make the policy clearer?
- Have I tested midpoint values, negatives, zero, and scale boundaries?
- Am I relying on a version-specific API?

## 77. Exercise

Build a fictional measurement-pricing calculator with these requirements:

1. Read unit price, quantity, and adjustment rate from strings.
2. Convert decimal text directly to `Decimal`.
3. Perform intermediate arithmetic with at least 20 significant digits of local precision.
4. Quantize the final amount to two decimal places using an explicitly selected rounding rule.
5. Reject an input unit price that contains more than two non-zero decimal places by trapping `Inexact` during validation.
6. Clear and inspect flags around the main calculation.
7. Print whether the main calculation produced an `Inexact` or `Rounded` signal before final quantization.
8. Keep the original active context unchanged after the function returns.

Extension challenges:

- reject non-finite values;
- add a test for a midpoint rounding case;
- accept an explicit `Context` as a function argument;
- serialize the final value under a documented external representation contract.

## 78. Connections to other Python concepts

`decimal` connects directly to topics already studied:

- **`float`:** the earlier binary representation model explains why Decimal exists.
- **Strings:** decimal text is often the safest exact input boundary.
- **Functions:** rounding helpers and explicit contexts turn numeric policy into reusable interfaces.
- **Exceptions:** trapped signals become exceptions and can participate in normal validation flows.
- **Context managers:** `localcontext()` scopes numeric policy with `with`.
- **JSON:** `parse_float=Decimal` preserves JSON number text as Decimal without an intermediate Python float.
- **Logging:** flags and validation failures can be recorded as runtime evidence without exposing sensitive data.
- **Testing:** midpoint rounding, precision boundaries, signal flags, and context restoration deserve behavioral assertions.
- **`itertools`:** iterator pipelines that aggregate Decimal values should preserve the chosen numeric model from source to sink.
- **Upcoming system utilities:** decimal values often cross file, environment, or external-process boundaries where text conversion contracts matter.

## References

Primary references used for this chapter:

- [Python 3.14 documentation: `decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3.14/library/decimal.html)
- [Python 3.14 tutorial: Floating-Point Arithmetic — Issues and Limitations](https://docs.python.org/3.14/tutorial/floatingpoint.html)
- [Python 3.14 tutorial: Decimal floating-point arithmetic](https://docs.python.org/3.14/tutorial/stdlib2.html#decimal-floating-point-arithmetic)
- [Python 3.14 documentation: Numeric and Mathematical Modules](https://docs.python.org/3.14/library/numeric.html)

## Next chapter

Continue with **Chapter 09: `os` and `shutil`** when it becomes available.

The next chapter moves from numeric contracts to **operating-system and filesystem-operation contracts**: environment access, low-level path operations, copying, moving, directory trees, metadata, destructive operations, and the boundary between `pathlib`, `os`, and `shutil`.
