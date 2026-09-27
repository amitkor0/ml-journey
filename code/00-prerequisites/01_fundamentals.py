"""01 — Python fundamentals.

Every section follows the same shape:

    # ── PREDICT ──  what you think will happen. Commit to an answer.
    <code>
    # actual output printed below the code

    # ── WHY ──  the reason, not just the result

Run:  .\\.venv\\Scripts\\python.exe code\\00-prerequisites\\01_fundamentals.py
"""

from __future__ import annotations


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ─────────────────────────────────────────────────────────────────────
section("1. Indentation defines blocks, not braces")
# ─────────────────────────────────────────────────────────────────────

age = 20

# PREDICT: prints "adult", then "can vote", then "always runs"
if age >= 18:
    print("adult")
    print("can vote")
print("always runs")

# WHY: the two indented lines are the if-body. Indentation is the only thing
# separating them. Shift one line left and it silently stops running.


# ─────────────────────────────────────────────────────────────────────
section("2. Variables are names, not typed boxes")
# ─────────────────────────────────────────────────────────────────────

x = 10
y = x
x = 20

# PREDICT: "20 10" — NOT "20 20"
print(x, y)

# WHY: `y = x` made y point at the same int object. `x = 20` rebound x to a
# new object; y still points at the original 10. Names are labels, not boxes.


# ─────────────────────────────────────────────────────────────────────
section("3. Strings: indexing, negative indexing, slicing")
# ─────────────────────────────────────────────────────────────────────

text = "yoo brother"

# PREDICT each line before running.
print(repr(text[0]))       # 'y'
print(repr(text[-1]))      # 'r'  <- last character
print(repr(text[-2]))      # 'h'
print(repr(text[0:3]))     # 'yoo'  <- stop is EXCLUSIVE
print(repr(text[4:11]))    # 'brother'
print(repr(text[:3]))      # 'yoo'
print(repr(text[4:]))      # 'brother'
print(repr(text[::2]))     # 'yobohr' -- curriculum says 'yo rte'; that is wrong.
                         # [::2] takes indices 0,2,4,6,8,10 = y,o,b,o,h,r
print(repr(text[::-1]))    # reversed

# WHY: stop is excluded, so [0:3] covers indices 0, 1, 2 — three characters.
# A negative step reverses. Slicing syntax is identical for strings, lists,
# tuples and NumPy arrays. Learn it once.

assert text[0:3] == "yoo"
assert text[::-1] == "rehtorb ooy"
assert len(text[-3:]) == 3  # the self-check question #1


# ─────────────────────────────────────────────────────────────────────
section("4. Strings are immutable")
# ─────────────────────────────────────────────────────────────────────

s = "hello"

# PREDICT: this raises TypeError
try:
    s[0] = "H"
except TypeError as exc:
    print(f"as expected -> {exc}")

# WHY: strings cannot be modified in place. "Changing" one builds a new object.
# This is also why strings are legal dictionary keys.

s = "H" + s[1:]
print(s)  # Hello
assert s == "Hello"


# ─────────────────────────────────────────────────────────────────────
section("5. f-strings and format specs")
# ─────────────────────────────────────────────────────────────────────

name, age, city = "Alice", 25, "New York"
print(f"Hello, {name}! You are {age} and live in {city}.")
print(f"Next year you'll be {age + 1}")  # expressions are allowed

accuracy = 0.9666666
f1 = 0.9653
loss = 0.123456789

# These are the four you will use constantly in ML.
print(f"{accuracy:.2f}")  # 2 decimal places
print(f"{accuracy:.1%}")  # AS A PERCENTAGE — the important one
print(f"{loss:.6f}")  # losses need more precision than accuracies
print(f"{1234567:,}")  # thousands separators

# PREDICT the self-check question #3: f"{1/3:.2f}"
print(f"{1 / 3:.2f}")

# WHY: a stored accuracy is a 0-1 float but every paper and dashboard reports a
# percentage. Printing 0.9667 where the reader expects 96.67 is one of the most
# common real reporting bugs in ML.

# print() inserts a single space between arguments, so concatenation is rarely
# needed:
print("Accuracy:", accuracy, "F1:", f1)


# ─────────────────────────────────────────────────────────────────────
section("6. Raw strings vs escaped strings")
# ─────────────────────────────────────────────────────────────────────

escaped = "C:\\Users\\Alice\\Documents"
raw = r"C:\Users\Alice\Documents"
print(escaped)
print(raw)
assert escaped == raw  # same value, one is just painful to type

# WHY it matters: in a regex, "\d" is a backspace character, not a digit
# pattern. r"\d+" is what you actually want. You will hit this in Module 12.


# ─────────────────────────────────────────────────────────────────────
section("7. Type conversion: int() truncates, it does not round")
# ─────────────────────────────────────────────────────────────────────

print(int(3.99))   # 3  <- PREDICT: 4? No. Truncates toward zero.
print(int(-3.99))  # -3
print(round(3.99))  # 4
print(int("123"))  # 123
print(float("3.14"))  # 3.14
print(str(123))  # '123'

assert int(2.99) == 2

# PREDICT: this raises ValueError
try:
    int("abc")
except ValueError as exc:
    print(f"as expected -> {exc}")

# WHY: int() truncating is a real trap. And int("abc") raising ValueError is the
# most common exception you will meet, because it is what a dirty CSV cell or
# bad user input looks like. Module 06 is about handling it.


# ─────────────────────────────────────────────────────────────────────
section("8. Truthy and falsy")
# ─────────────────────────────────────────────────────────────────────

falsy = [False, None, 0, 0.0, 0j, "", [], {}, (), set()]
print("falsy values:", [type(v).__name__ for v in falsy])
for value in falsy:
    assert not value, f"{value!r} should be falsy"

# The confusing ones — all TRUTHY:
surprising = ["0", "False", [0], [False], 0.1, {"a": 1}, " "]
print("truthy values:", surprising)
for value in surprising:
    assert value, f"{value!r} should be truthy"

# PREDICT self-check #4: bool("False")
print("bool('False') =", bool("False"))  # True — non-empty string

# WHY: only ten things are falsy. Anything non-empty is truthy, including the
# string "False". This is why you never write `if flag == True:`.


# ─────────────────────────────────────────────────────────────────────
section("9. The 'or' default trap")
# ─────────────────────────────────────────────────────────────────────

value = None
print(repr(value or "default"))  # 'default' — intended

value = 0
print(repr(value or "default"))  # PREDICT: 'default'? BUG if 0 is valid data

# WHY: `or` returns the falsy operand, not a boolean. With 0 — an extremely
# common value in ML — it silently substitutes the default. When 0 and "" are
# legitimate data, test explicitly:
correct = "default" if value is None else value
print(repr(correct))  # 0

print("\nall assertions passed")
