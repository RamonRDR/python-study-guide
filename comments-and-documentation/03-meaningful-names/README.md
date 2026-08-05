<div align="center">

# Meaningful Names and Self-Explanatory Code

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: Docstrings](../02-docstrings/README.md)

A name is one of the smallest design decisions in a program, but it may be read hundreds of times. Good names reduce the amount of context a reader must reconstruct and help code communicate intention before a comment or docstring is needed.

> **Guiding principle:** Name a concept according to what it means in the program, not merely according to the value currently stored in it.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Basic familiarity with variables and functions is recommended |
| Estimated study time | 50 to 70 minutes |
| Main concepts | intention-revealing names, `snake_case`, `PascalCase`, constants, booleans, units, collections, scope, vocabulary, built-ins, refactoring |

## Learning objectives

By the end of this chapter, you should be able to:

- choose names that reveal purpose, domain meaning, state, and units;
- follow common Python naming conventions without treating them as syntax rules;
- distinguish useful brevity from harmful vagueness;
- name boolean values as questions or conditions;
- use plural names for collections and singular names for individual elements;
- avoid shadowing built-in names and reserved keywords;
- use one consistent vocabulary for the same concept;
- recognize when a small function or variable can reveal intention;
- understand where comments and docstrings remain necessary;
- rename code safely while considering public interfaces.

## 1. Why names matter

Python executes identifiers without caring whether they are expressive:

```python
x = 30
y = 0.10
z = x - (x * y)
```

A person must infer what each value means. The same calculation can communicate much more:

```python
subtotal = 30
discount_rate = 0.10
discounted_total = subtotal - (subtotal * discount_rate)
```

The second version does not change the algorithm. It changes the reader's workload.

Meaningful names help answer:

- What does this value represent?
- Which unit does it use?
- Is it one item or a collection?
- Is the boolean a state, capability, or decision?
- What action does this function perform?
- What concept does this class model?

## 2. Python naming syntax and conventions

In the common ASCII convention, an identifier begins with a letter or underscore and continues with letters, digits, or underscores. Python's complete lexical grammar is broader: it accepts many Unicode characters according to the `XID_Start` and `XID_Continue` rules, and identifiers are case-sensitive. See the [official lexical reference](https://docs.python.org/3/reference/lexical_analysis.html#identifiers).

This project uses English ASCII identifiers for portability, searchability, and consistency across international tools and documentation.

Valid:

```python
customer_name = "Mina"
invoice2_total = 125
_internal_cache = {}
```

Invalid:

```python
2nd_invoice = 125
customer-name = "Mina"
```

Python keywords cannot be used as ordinary identifiers:

```python
class = "premium"
```

When an external concept conflicts with a keyword, a trailing underscore is a common option:

```python
class_ = "premium"
```

### Common style conventions

| Kind of name | Common convention | Example |
|---|---|---|
| Variable | `snake_case` | `invoice_total` |
| Function | `snake_case` | `calculate_invoice_total()` |
| Class | `PascalCase` | `InvoiceCalculator` |
| Constant | `UPPER_SNAKE_CASE` | `MAX_RETRY_ATTEMPTS` |
| Internal-use name | leading underscore | `_load_cached_value()` |

These conventions improve recognition, but Python usually does not enforce them. A project may add linters or style checks.

## 3. Reveal intention, not only content

Weak names often describe the container rather than the concept:

```python
data = ["Ana", "Diego", "Mina"]
value = 30
result = value * 60
```

Clearer:

```python
customer_names = ["Ana", "Diego", "Mina"]
duration_minutes = 30
duration_seconds = duration_minutes * 60
```

`data`, `value`, `item`, and `result` are not always wrong. They become harmful when the surrounding context does not make their meaning obvious.

A useful naming question is:

> What would a reader need to know to use this value correctly?

## 4. Include units and representation when they matter

A number without a unit can create silent mistakes:

```python
timeout = 30
total = 12_750
```

The reader cannot know whether `timeout` is seconds or milliseconds, or whether `total` is currency units or cents.

Clearer:

```python
timeout_seconds = 30
invoice_total_cents = 12_750
```

Useful representation details may include:

- `_seconds`, `_minutes`, or `_milliseconds`;
- `_bytes` or `_megabytes`;
- `_cents` when avoiding floating-point currency;
- `_percentage` for values from 0 through 100;
- `_rate` for fractional values such as `0.15`;
- `_text`, `_path`, `_date`, or `_datetime` when forms could be confused.

Do not add every type to every name. Add information that prevents a realistic misunderstanding.

## 5. Name booleans as questions or conditions

A boolean name should make `True` and `False` readable.

Weak:

```python
active = True
retry = False
```

Clearer:

```python
is_active = True
should_retry = False
```

Common prefixes include:

- `is_` for state or classification;
- `has_` for possession or presence;
- `can_` for capability or permission;
- `should_` for a decision;
- `needs_` for required action.

Example:

```python
RETRYABLE_STATUS_CODES = {502, 503, 504}

is_status_configured_for_retry = (
    response_status_code in RETRYABLE_STATUS_CODES
)
has_retry_attempts_remaining = attempt_number < MAX_RETRY_ATTEMPTS
should_retry_request = (
    is_status_configured_for_retry and has_retry_attempts_remaining
)
```

Avoid negative names when they create double negatives:

```python
if not is_not_ready:
    ...
```

Prefer a positive concept:

```python
if is_ready:
    ...
```

## 6. Collections and individual elements

Plural names help readers recognize collections:

```python
customer_names = ["Ana", "Diego", "Mina"]

for customer_name in customer_names:
    print(customer_name)
```

The plural and singular forms show the relationship immediately.

For mappings, name both sides when useful:

```python
country_code_by_name = {
    "Brazil": "BR",
    "Spain": "ES",
}
```

Other readable patterns include:

```python
users_by_id = {}
price_by_product_code = {}
errors_by_file_path = {}
```

Names such as `mapping`, `dictionary`, and `list_data` reveal the container type but often hide the domain relationship.

## 7. Functions, classes, and constants

### Functions usually describe actions

Function names commonly begin with verbs:

```python
calculate_total()
load_configuration()
normalize_account_code()
is_supported_account()
```

The verb should match the behavior. A function named `get_report()` should not unexpectedly delete files or send emails.

### Classes usually describe entities or responsibilities

Class names commonly use nouns:

```python
Invoice
ReportGenerator
ValidationResult
```

Avoid empty suffixes such as `Manager`, `Helper`, or `Processor` when they do not clarify responsibility. Sometimes those words are accurate, but they should not become fog machines.

### Constants describe stable configuration or policy

```python
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
SUPPORTED_FILE_EXTENSIONS = {".csv", ".json"}
```

Uppercase communicates that the value is intended to remain stable by convention. It does not make the object technically immutable.

## 8. Scope determines how much detail a name needs

A short name can be clear inside a tiny local scope:

```python
for row in rows:
    print(row)
```

The same name may be too vague across a large function or module.

A loop index is often understandable as `index` or even `i` in a very small mathematical loop:

```python
for i in range(3):
    print(i)
```

Longer scope usually deserves more context:

```python
for retry_attempt_index in range(MAX_RETRY_ATTEMPTS):
    ...
```

Long names are not automatically good. A name should carry enough information for its scope without becoming a paragraph wearing underscores.

## 9. Abbreviations, acronyms, and project vocabulary

Use an abbreviation when it is more familiar than its expanded form or when the project has defined it clearly:

```python
url = "https://example.com"
user_id = 42
csv_file_path = "report.csv"
```

Avoid private puzzles:

```python
usr_cfg_tmp = {}
```

A consistent vocabulary is more important than finding a new synonym on every line.

Confusing:

```python
customer_id = 42
client_name = "Ana"
consumer_status = "active"
```

If these names represent the same domain entity, choose one term:

```python
customer_id = 42
customer_name = "Ana"
customer_status = "active"
```

A project glossary can prevent vocabulary drift in larger systems.

## 10. Avoid shadowing built-ins and important names

Python provides built-ins such as `list`, `str`, `sum`, `id`, `input`, and `type`.

Avoid:

```python
list = ["Ana", "Diego"]
sum = 100
```

After those assignments, calling `list()` or `sum()` in the same scope no longer refers to the built-in.

Prefer:

```python
customer_names = ["Ana", "Diego"]
invoice_total = 100
```

Shadowing can also happen with imported modules or functions:

```python
import logging

logging = True
```

The assignment hides the imported module. Choose a distinct name such as `is_logging_enabled`.

## 11. Do not encode unnecessary type information

Names such as these often age badly:

```python
customer_name_string = "Ana"
invoice_items_list = []
settings_dictionary = {}
```

Type hints and the operations around a value already communicate much of its structure:

```python
customer_name: str = "Ana"
invoice_items: list[str] = []
settings: dict[str, str] = {}
```

Include representation in the name only when it prevents ambiguity, such as `invoice_total_cents` or `created_at_text`.

## 12. Small abstractions can reveal intention

A complicated expression can be named:

```python
is_priority_customer = (
    customer_status == "active"
    and annual_purchase_total >= 10_000
    and not has_overdue_invoice
)
```

A reusable operation can become a function:

```python
def is_priority_customer(
    customer_status,
    annual_purchase_total,
    has_overdue_invoice,
):
    return (
        customer_status == "active"
        and annual_purchase_total >= 10_000
        and not has_overdue_invoice
    )
```

The name creates a conceptual handle. It should not hide arbitrary complexity behind a misleading label.

Good abstraction names explain **what** the operation means. The implementation explains **how** it works.

## 13. Self-explanatory code does not eliminate documentation

Clear names reduce comments that merely translate syntax:

```python
# Check whether the account is supported.
if account_code in supported_account_codes:
    ...
```

The comment adds little because the names already explain the condition.

Comments remain useful for reasons and constraints:

```python
# Keep the legacy code for compatibility with exports created before 2024.
supported_account_codes.add("LEGACY")
```

Docstrings remain useful for public contracts, exceptions, side effects, and usage expectations.

Readable code, comments, docstrings, type hints, tests, and external documentation solve different problems.

## 14. Renaming safely

Renaming is a refactoring: behavior should remain the same while the code becomes easier to understand.

A safe workflow is:

1. identify the concept the name represents;
2. search for every reference;
3. use editor refactoring tools when available;
4. update tests, examples, docstrings, and documentation;
5. run the project checks;
6. review public compatibility.

Renaming a local variable is usually low risk. Renaming a public function, class, module, command-line option, configuration key, database field, or serialized attribute may break users.

Public renames may require:

- a deprecation period;
- an alias;
- migration instructions;
- a versioned release;
- coordination with external systems.

## 15. Examples in this repository

| File | Purpose |
|---|---|
| [`vague_and_clear_names.py`](examples/vague_and_clear_names.py) | Compares vague identifiers with names that communicate calculation intent |
| [`booleans_and_units.py`](examples/booleans_and_units.py) | Demonstrates booleans, units, collections, and constants |
| [`refactor_for_intent.py`](examples/refactor_for_intent.py) | Shows small named operations revealing a workflow |

Run an example from the repository root:

```bash
python comments-and-documentation/03-meaningful-names/examples/vague_and_clear_names.py
```

On systems where the command is named `python3`:

```bash
python3 comments-and-documentation/03-meaningful-names/examples/vague_and_clear_names.py
```

## 16. Practical example

Before:

```python
def f(p, d):
    t = sum(p)
    return t - (t * d)
```

After:

```python
def calculate_discounted_total(
    prices: list[float],
    discount_rate: float,
) -> float:
    subtotal = sum(prices)
    discount_amount = subtotal * discount_rate
    return subtotal - discount_amount
```

The second version communicates:

- the function's action;
- what the collection contains;
- that the discount is a fractional rate;
- what the intermediate values represent;
- what the returned value means.

See the complete comparison in [`examples/vague_and_clear_names.py`](examples/vague_and_clear_names.py).

## 17. Common mistakes

### Choosing a long name without adding meaning

```python
the_value_that_we_are_currently_using = 10
```

Long does not equal precise. Prefer the domain concept:

```python
retry_delay_seconds = 10
```

### Using one name for several meanings

Reusing `result` for unrelated steps makes debugging and review harder.

### Naming by implementation instead of responsibility

`json_dictionary` may become inaccurate if the implementation changes. `report_payload` may better describe its role.

### Using misleading verbs

A function named `check_permissions()` that modifies permissions violates reader expectations.

### Mixing singular and plural

```python
customer = ["Ana", "Diego"]
```

Use `customers` or `customer_names`.

### Hiding a built-in

```python
type = "premium"
```

Use `customer_type` or another domain-specific name.

### Keeping obsolete names after behavior changes

A variable called `discount_percentage` is misleading if the code now stores `0.15` as a rate.

## 18. Exercise

Refactor this code without changing its result:

```python
def p(x, y, z):
    a = x * y
    if z:
        a = a * 1.15
    return a
```

Assume:

- `x` is an hourly rate in cents;
- `y` is a number of worked hours;
- `z` indicates whether a fictional premium applies;
- `1.15` represents a fictional premium multiplier.

One possible answer:

```python
PREMIUM_PAY_MULTIPLIER = 1.15


def calculate_pay_cents(
    hourly_rate_cents,
    worked_hours,
    has_premium_pay,
):
    base_pay_cents = hourly_rate_cents * worked_hours

    if has_premium_pay:
        return base_pay_cents * PREMIUM_PAY_MULTIPLIER

    return base_pay_cents
```

Review questions:

1. Does each name reveal a concept rather than only a type?
2. Are units explicit where confusion is possible?
3. Does the boolean read naturally in a condition?
4. Does the constant explain the unexplained number?
5. Did the refactoring preserve behavior?

## 19. Naming review checklist

Before accepting a name, ask:

- Can a reader explain the concept without tracing several lines?
- Does the name distinguish one item from a collection?
- Are units or representations explicit when necessary?
- Does a boolean read naturally as true or false?
- Does a function name match its effects?
- Is the same domain term used consistently?
- Does the name avoid shadowing a built-in or import?
- Is the amount of detail appropriate for the scope?
- Would behavior changes make the name false?
- Does public compatibility require a migration plan?

## 20. Quick-reference summary

| Situation | Prefer |
|---|---|
| Variable or function | `snake_case` |
| Class | `PascalCase` |
| Constant | `UPPER_SNAKE_CASE` |
| Boolean state | `is_active`, `has_access`, `should_retry` |
| Collection | plural noun such as `customer_names` |
| Individual element | singular noun such as `customer_name` |
| Numeric unit | `timeout_seconds`, `total_cents` |
| Mapping relationship | `users_by_id`, `code_by_name` |
| Function behavior | clear verb such as `calculate`, `load`, `normalize` |
| Reserved keyword conflict | trailing underscore such as `class_` |
| Built-in name | choose a domain-specific alternative |
| Repeated complex condition | intention-revealing variable or function |

## Conclusion

Meaningful names are executable documentation woven directly into the code. They do not replace design, comments, docstrings, tests, or guides, but they make every one of those tools easier to use.

Choose names that remain true, reveal the program's vocabulary, and reduce the number of guesses a reader must make.

[← Previous chapter: Docstrings](../02-docstrings/README.md) · [Back to the section index](../README.md) · Next chapter: Task markers
