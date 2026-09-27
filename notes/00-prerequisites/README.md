# Module 00 — Prerequisites

> Source: [`00-prerequisites/`](https://github.com/NabidAlam/road-to-machine-learning/tree/main/00-prerequisites)
> Stage 0 · Estimated 6-8 weeks thorough, 4 weeks minimum

The foundation layer. Everything in the other 25 modules assumes the habits
formed here. The curriculum is blunt about it: *"Weak foundations here are the
main reason learners stall later."*

## What is actually in this module

| Curriculum file | Lines | Covers | My notes |
|---|---|---|---|
| `01-python-basics.md` | 1507 | syntax → OOP → generators → tkinter → Big-O | 01-11 below |
| `prerequisites-advanced-topics.md` | 389 | decorators, context managers, advanced NumPy | 08, and Module 01 |
| `02-linear-algebra.md` | 1655 | vectors, matrices, eigenvalues, SVD | separate file |
| `03-statistics-probability.md` | 1149 | descriptive stats, distributions, inference | separate file |
| `04-calculus.md` | 643 | derivatives, gradients, gradient descent | separate file |
| `05-environment-setup.md` | 390 | Python, venv, Jupyter, git | **already done — see `SETUP.md`** |
| `prerequisites-project-tutorial.md` | 489 | neural network in pure NumPy | the capstone |
| `prerequisites-quick-reference.md` | 326 | syntax + formula cheat sheet | use as a crutch, don't memorise |

## Reading order, and one deviation

The curriculum's suggested order is Python → linear algebra → statistics →
calculus → environment setup. I am following that, with two changes:

1. **`05-environment-setup.md` is already complete.** We installed Git, GitHub
   CLI, uv, Python 3.12, a venv, Jupyter, and 15 VS Code extensions, and
   verified it by running a real project. Read it only to check nothing was
   missed.
2. **I am inserting `08-scope-and-decorators.md` after OOP.** The module README
   lists *"Decorators; namespaces and the LEGB scope rule"* as a required topic,
   but decorators only appear later in `prerequisites-advanced-topics.md` and
   **LEGB is not covered anywhere in the module.** Since scope rules are
   something a beginner needs *before* closures make sense, I have written that
   material rather than leaving a hole in the syllabus.

## The order within Python, and why

The curriculum presents these in one flat list. This is the order that works,
because each item is a prerequisite for the next:

1. **Fundamentals** — types, strings, f-strings, truthy/falsy. Without
   truthiness, every later `if` is mysterious.
2. **Control flow** — indentation, branches, loops. `break`/`continue`/`pass`
   belong here, not in a separate section.
3. **Functions** — including *first-class functions*, which is what makes
   `map`/`filter`/`reduce` and lambdas comprehensible rather than magic.
4. **Data structures** — list/dict/tuple/set and comprehensions. Dict lookup
   being O(1) is what makes Big-O meaningful later.
5. **File I/O** — `with`, CSV, `tell`/`seek`. This is where the exit gate lives
   (read a CSV, handle a missing file).
6. **Error handling** — comes *before* OOP on purpose, because the capstone
   needs it and because exceptions read better once you have seen functions.
7. **OOP** — classes, inheritance, polymorphism, dunder methods.
8. **Scope and decorators** — LEGB, closures, decorators. Placed here because
   decorators only make sense once you know how names resolve.
9. **Iterators and generators** — laziness and memory. The single most
   data-science-relevant topic in the module.
10. **Big-O** — put *after* the data structures, not before, because complexity
    is a property of a concrete data structure plus an operation. Studying it
    in the abstract is how people memorise a table and understand nothing.
11. **tkinter** — skim. Useful, but nothing in ML depends on it. Read it once,
    run the calculator, move on.

## How to use the code in `code/00-prerequisites/`

Each script is standalone and runnable:

```powershell
.\.venv\Scripts\python.exe code\00-prerequisites\01_fundamentals.py
```

Every script follows the same pattern:

- A `# ── PREDICT ──` comment states what the output will be **before** it runs.
  Stop there and commit to an answer. Then run it. If you were wrong, the
  comment stays wrong until you fix it, which is the point.
- Output you should reason about is labelled `# WHY:`.
- `assert` statements check facts that must be true. If one fails, the script
  stops and tells you.

Run them in order. They build on each other.

## Exit gate (must pass before Module 01)

From the module README. Do not start Module 01 until you can do all six.

| Skill | Self-check | Where |
|---|---|---|
| Python | Write a function **and** a class that reads a CSV and handles a missing-file error | `05`, `07` |
| Complexity | State Big-O of a single loop vs a nested loop over *n* items | `10` |
| Linear algebra | Multiply two 2×2 matrices; explain what a dot product measures | linear algebra notes |
| Statistics | Compute mean and standard deviation; explain when median beats mean | statistics notes |
| Calculus | Describe gradient descent and the role of the learning rate | calculus notes |
| Environment | Create a venv, `pip install` packages, open Jupyter | **done — `SETUP.md`** |

**Proof of work (pick one):**

- [ ] Movie script generator capstone — `code/00-prerequisites/12_capstone_movie_script.py`
- [ ] NumPy neural network from scratch — `prerequisites-project-tutorial.md`

The movie script is the default because it exercises file I/O and exceptions,
which the exit gate tests directly. The NumPy network is the better proof of
mathematical understanding. Doing both is the honest answer.

## Progress

- [x] Environment gate (done during setup)
- [ ] 01 Fundamentals
- [ ] 02 Control flow
- [ ] 03 Functions
- [ ] 04 Data structures
- [ ] 05 File I/O
- [ ] 06 Error handling
- [ ] 07 OOP
- [ ] 08 Scope and decorators
- [ ] 09 Iterators and generators
- [ ] 10 Big-O
- [ ] 11 tkinter
- [ ] 12 Capstone
- [ ] Linear algebra
- [ ] Statistics and probability
- [ ] Calculus
- [ ] Exit gate review
