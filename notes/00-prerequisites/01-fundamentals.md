# 01 — Python Fundamentals

> Source: [`01-python-basics.md`](https://github.com/NabidAlam/road-to-machine-learning/blob/main/00-prerequisites/01-python-basics.md) § Comments → § Type Conversion
> Run: `.\.venv\Scripts\python.exe code\00-prerequisites\01_fundamentals.py`

## The one thing that makes Python different from most languages

There are no braces, no semicolons, no `int age;`. **Indentation *is* the
syntax.** A block of code is defined by how far it is indented, not by
delimiters.

```python
age = 20
if age >= 18:
    print("adult")   # 4 spaces
    print("can vote")  # same 4 spaces, so also inside the if
print("always runs")   # 0 spaces, so outside
```

Get the indentation wrong and Python does not warn you — it silently changes
which lines belong to the `if`. That is the single most common beginner bug.
The curriculum flags this in a `RECALL` box and it is worth taking seriously.

**Convention:** 4 spaces per level. Never mix tabs and spaces. VS Code is
already configured for this via Ruff.

## Variables and dynamic typing

```python
name = "Alice"        # str
age = 25              # int
height = 5.6          # float
is_student = True     # bool
z = 3 + 4j            # complex
```

Python infers the type from the value. You never declare it.

The consequence beginners miss: **a variable is a name pointing at a value,
not a box holding a type.** Rebinding a name does not change the original
object.

```python
x = 10
y = x          # y points at the SAME int object as x
x = 20         # x now points at a new int; y still points at 10
print(x, y)    # 20 10
```

This is why the next section matters. Strings and tuples are **immutable** —
you cannot change them in place, so any "modification" silently creates a new
object.

### Naming

| Convention | Example | Use for |
|---|---|---|
| `snake_case` | `user_name` | variables, functions, methods |
| `PascalCase` | `BankAccount` | classes |
| `SCREAMING_SNAKE` | `MAX_ITERATIONS` | constants |

Rules: start with a letter or `_`; letters/digits/underscores only; case
sensitive (`name` ≠ `Name`); cannot be a keyword (`if`, `for`, `def`, `class`,
`lambda`, `None`, `True`, `False`…).

Note `True`/`False`/`None` are **capitalised** in Python. `true`, `false`,
`null`, `None` typos are extremely common coming from JavaScript or C.

## Strings

Strings are sequences of characters, indexed from 0.

```python
text = "hello"
#  index:  0  1  2  3  4
#  char:   h  e  l  l  o
#  index: -5 -4 -3 -2 -1
```

Negative indices count from the end, so `text[-1]` is the last character. This
is not in the curriculum as a numbered feature but it is the single most useful
string operation, and you will use it constantly when parsing filenames and
file headers.

### Slicing: `[start:stop:step]`

The trap: **`stop` is excluded.** `text[0:3]` gives three characters, indices
0, 1, 2.

```python
text = "yoo brother"
text[0:3]      # 'yoo'        indices 0,1,2
text[4:11]     # 'brother'    indices 4..10
text[:3]       # 'yoo'        start defaults to 0
text[4:]       # 'brother'    stop defaults to end
text[::2]      # 'yobohr'     every 2nd character
text[::-1]     # 'rehtorb ooy' reversed
```

> **Correction to the curriculum.** The source lesson annotates `text[::2]` as
> `'yo rte'`. That is wrong. `"yoo brother"[::2]` takes indices 0, 2, 4, 6, 8,
> 10 — which are `y o b o h r`, giving `'yobohr'`. The prose answer assumed
> it was stepping over *words*. Verified by running it, not by reading it.

`text[::-1]` is worth memorising — reversing a string is a one-liner, and it
appears in text-processing and palindrome exercises.

Slicing works identically on lists, tuples, and NumPy arrays. Learn it once.

### Immutability

```python
text = "hello"
text[0] = "H"        # TypeError: 'str' object does not support item assignment
text = "H" + text[1:]  # correct: build a new string
```

Strings cannot be modified in place. Why it matters:

- Safe to share between variables — nobody can mutate it behind your back
- Can be used as **dictionary keys** (keys must be hashable and immutable)
- Cheaper than you would think: Python may return the identical object rather
  than copying

The same rule applies to tuples. Lists and dicts are mutable.

## Printing and f-strings

Use f-strings. Always. `str.format()` and `%` are legacy.

```python
name, age, city = "Alice", 25, "New York"

# f-string: prefix the string with f, put expressions in {braces}
f"Hello, {name}! You are {age} and live in {city}."
f"Next year you'll be {age + 1}"          # expressions are allowed
f"{'nested string'}"                       # even a string inside
```

The format spec after `:` is the part you will use most in ML, because you
will print metrics constantly:

```python
accuracy = 0.9666666
f"{accuracy:.2f}"        # '0.97'      2 decimal places
f"{accuracy:.1%}"        # '96.7%'      as a percentage
f"{1234567:,}"           # '1,234,567'  thousands separators
f"{42:08d}"              # '00000042'   zero-padded
f"{3.14159:8.3f}"        # '   3.142'   width 8, 3 decimals, right aligned
```

`f"{accuracy:.1%}"` deserves attention. Model evaluation output is
percentage-based in every paper and dashboard, but stored as a 0-1 float.
Getting this wrong — printing `0.9667` where the reader expects `96.67` — is
one of the most common real-world reporting bugs.

Also: `print` accepts multiple arguments and inserts a single space between
them, so you rarely need concatenation at all.

```python
print("Accuracy:", accuracy, "F1:", f1)
# Accuracy: 0.9667 F1: 0.9653
```

### Escape sequences and raw strings

`\n` newline, `\t` tab, `\\` backslash, `\"` quote. For Windows paths you need
raw strings or doubled backslashes:

```python
r"C:\Users\Alice\Documents"    # raw: backslashes are literal
"C:\\Users\\Alice\\Documents"  # escaped: same result, uglier
```

Raw strings matter for regex in Module 12: `r"\d+"` is a digit pattern, while
`"\d+"` is a string containing an actual tab character followed by `d+`, which
silently matches nothing like what you meant.

## Type conversion

```python
int("123")     # 123
int(3.14)      # 3      <- TRUNCATES toward zero, does not round
float("3.14")  # 3.14
str(123)       # '123'
bool(0)        # False
```

`int()` truncating rather than rounding is a genuine trap. `int(2.7)` is `2`.
If you need rounding, use `round(2.7)` → `3`.

`int("abc")` raises `ValueError`. This is the single most common exception you
will meet, because it is what happens when user input or a dirty CSV cell is
not a number. Module 06 is entirely about handling it.

## Truthy and falsy

This is more important than it looks, and it is the concept that makes every
later `if` readable.

In a boolean context, Python coerces any value to `True` or `False`.

**Falsy** — only ten things in the whole language:

| Falsy | Why it matters |
|---|---|
| `False` | the literal |
| `None` | "no value"; missing data, no return, failed lookup |
| `0`, `0.0`, `0j` | numeric zero |
| `""` | empty string |
| `[]`, `{}`, `()`, `set()` | empty containers |

**Everything else is truthy** — including `"0"`, `"False"`, `[0]`, and `0.1`.

```python
if my_list:            # idiomatic: "if it has items"
    ...
```

### The `or` default trap

```python
value = None
result = value or "default"     # 'default'  ✓ intended

value = 0
result = value or "default"     # 'default'  ✗ BUG if 0 is legitimate
```

`or` returns the *falsy* operand, not `True`/`False`. With `0` — a perfectly
valid number, and an extremely common one in ML — this silently substitutes
the default. Use an explicit `is None` check when `0` and `""` are valid data.

Note the contrast with `pandas`, where `NaN` is truthy in some contexts and
falsy in others. When you reach Module 01, prefer `isna()` over truthiness for
missing-value checks. This single difference causes more confusion in ML than
any other language quirk.

## Summary

- Indentation defines blocks, and getting it wrong fails silently
- Variables are names bound to objects; strings and tuples are immutable
- `text[-1]` and `text[::-1]` are worth memorising
- f-strings with format specs, especially `:.1%` for metrics
- `int()` truncates; it does not round
- Only ten falsy values; `"0"` and `[0]` are truthy
- `x or default` breaks when `0` is valid data

## Self-check

Answer these without running anything. Then run the script and see.

1. What is `len("hello"[-3:])`?
2. Why does `text[0:3]` return three characters and not four?
3. `f"{1/3:.2f}"` — what prints?
4. Is `bool("False")` true or false?
5. Why is `int(2.99)` equal to `2` and not `3`?
6. `value = []` then `result = value or "empty"` — what is `result`?
