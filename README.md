# ML Journey

My notes, code, and projects from working through
**[Road to Machine Learning](https://github.com/NabidAlam/road-to-machine-learning)**
by Nabid Alam — 26 modules, 283 lessons, 23 projects, zero to ML engineer.

**Progress:** see [PROGRESS.md](PROGRESS.md) · **Environment:** see [SETUP.md](SETUP.md)

This repository is *my* work, not a copy of the curriculum. The curriculum is
read-only reference material; everything here is written by me, in my own
words, with code I wrote and understood. That distinction is the whole point —
notes I can re-read in a year are worth far more than a fork.

## Layout

```
ml-journey/
├── notes/          # Concept notes, one folder per module. Markdown.
├── notebooks/      # Runnable experiments, one folder per module. Jupyter.
├── projects/       # The 23 portfolio projects, each with its own README.
├── data/           # Datasets. Git-ignored. Re-downloadable via scripts/.
├── scripts/        # Setup and helper scripts.
├── requirements/   # Pinned package sets, one file per environment.
├── assets/         # Images and diagrams used in notes.
└── PROGRESS.md     # Module-by-module tracker.
```

The curriculum itself is cloned separately, read-only, at
`F:\curriculum\road-to-machine-learning` so I can grep every lesson locally
without vendoring someone else's content into my repo.

## How I work through a module

1. **Read** the module's lessons in the curriculum.
2. **Write** notes in my own words as I go — `notes/<module>/<lesson>.md`.
   Copying the source teaches nothing; the template in `notes/_template.md`
   forces me to explain and to record what surprised me.
3. **Rebuild** each example from a blank notebook — `notebooks/<module>/`.
   If I cannot write it without looking, I have not learned it.
4. **Break it on purpose.** Change one thing, predict the outcome, then check.
5. **Answer the exit-gate questions** in `notes/<module>/review.md`.
6. **Commit** with a message that says what I learned, not just which files changed.

## Quick commands

Run these from the repo root. The core environment covers Stages 0-4 and
modules 19-21; other stages have their own environment (see `SETUP.md`).

```powershell
# activate the core environment
.\.venv\Scripts\Activate.ps1

# run a notebook
jupyter lab

# lint and format
ruff check .
ruff format .

# run the tests
pytest
```

If activation is blocked by PowerShell policy, skip it and call the interpreter
directly — it needs no activation:

```powershell
.\.venv\Scripts\python.exe -m jupyter lab
```

## Principles

- **Write code, do not copy code.** Reading a solution teaches syntax. Writing it
  teaches judgement.
- **Prefer the small experiment.** One changed variable, a recorded prediction,
  a recorded result. That is how the judgement forms.
- **Notes in my own words, or they do not count.** If I cannot explain a
  concept to a friend, I do not understand it yet.
- **Version everything.** Small frequent commits with meaningful messages build
  a history I can actually learn from.
- **Ship the projects.** The 23 projects are the portfolio. Notes are the
  reasoning behind them.
- **Ask for help when stuck, then explain the answer back.** Being rescued is
  not learning; being able to reconstruct the reasoning is.

## Related

- Study hub: <https://nabidinmotion.com/>
- Curriculum repo: <https://github.com/NabidAlam/road-to-machine-learning>
- License: this work is mine. The curriculum it follows is MIT licensed.
