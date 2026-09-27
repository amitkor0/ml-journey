# Environment Setup

Everything installed to work through the curriculum, why it is installed, and how
to rebuild it from scratch on a new machine.

Recorded: 2026-09-27

## Hardware this was built for

| Component | Spec | Consequence |
|---|---|---|
| CPU | 12 logical cores | fine for classical ML, slow for deep learning |
| RAM | 15.3 GB | limits dataset size; close Jupyter/VS Code when training |
| GPU | **AMD Radeon integrated, no NVIDIA** | **PyTorch is CPU-only.** See [GPU strategy](#gpu-strategy). |
| Disk | F: 144 GB free | environments and datasets live here, not on C: |

The GPU is the single biggest constraint. Modules 09-12 and 25 involve training
networks that expect a CUDA GPU. On CPU they still *run* — a small CNN on MNIST
takes minutes instead of seconds — but a transformer fine-tune is not happening
locally. Plan to use cloud GPUs for those; details below.

## Installed tooling

| Tool | Version | Why |
|---|---|---|
| Git | 2.55.0 | version control for every note and script |
| GitHub CLI (`gh`) | 2.101.0 | auth, repo creation, pull requests without leaving the terminal |
| uv | 0.12.19 | manages Python versions and virtual environments; far faster than pip/venv |
| Python | 3.12.14 | managed by uv, the interpreter every project uses |
| VS Code | 1.138.0 | already present |

Python was **not** previously installed — `python` on this machine was only the
Microsoft Store stub that opens the Store when you run it. uv now provides the
real interpreter.

## Why environments are split

The curriculum's own `requirements.txt` lists TensorFlow, PyTorch, spaCy,
Prophet, Stable-Baselines3, OpenCV and more. Installed together that is roughly
8 GB, takes a long time, and frequently produces dependency conflicts that are
painful to debug while learning.

So each stage gets a small environment with only what it needs:

| Environment | Modules | Installed with |
|---|---|---|
| `.venv` | 00-08, 19, 20, 21 | `requirements/core.txt` |
| `.venv-torch` | 09-12, 25 | `requirements/torch-cpu.txt` |

More will be added as later modules need them. This is also what a working
data scientist actually does — one environment per project, never one global
environment for everything.

## Rebuilding from scratch

```powershell
git clone <this-repo> F:\ml-journey
Set-Location F:\ml-journey

# 1. Python
uv python install 3.12

# 2. Core environment (Stages 0-4)
uv venv --python 3.12 .venv
uv pip install --python .venv\Scripts\python.exe -r requirements/core.txt

# 3. Deep learning environment (Stages 5-7) - optional, large
uv venv --python 3.12 .venv-torch
uv pip install --python .venv-torch\Scripts\python.exe -r requirements/torch-cpu.txt

# 4. Jupyter kernel for the core environment
.venv\Scripts\python.exe -m ipykernel install --user --name ml-core `
  --display-name "Python (ml-core)"
```

`scripts/setup-envs.ps1` does steps 1-4 in one command.

## VS Code

The repo ships `.vscode/settings.json`, so opening `F:\ml-journey` in VS Code
configures itself: the interpreter points at `.venv`, Ruff formats and fixes on
save, and `.venv` is hidden from the file explorer.

Installed extensions:

| Extension | Purpose |
|---|---|
| `ms-python.python` + `vscode-pylance` | language server, autocomplete, type hints |
| `ms-python.vscode-python-envs` | environment and interpreter management |
| `ms-python.debugpy` | Python debugging |
| `ms-toolsai.jupyter` | notebook editing and execution |
| `charliermarsh.ruff` | linting and formatting (replaces Black + flake8) |
| `eamodio.gitlens` | blame, history, and "who wrote this" inline |
| `mhutchie.git-graph` | visualises the commit graph — good for learning git |
| `github.vscode-github-pull-request-github` | review PRs without leaving VS Code |
| `github.vscode-github-actions` | view and debug CI workflows |
| `redhat.vscode-yaml` | syntax for workflow and config files |
| `shd101wyy.markdown-preview-enhanced` | notes preview with export |
| `bierner.markdown-mermaid` | Mermaid diagram rendering, which the curriculum uses heavily |
| `streetsidesoftware.code-spell-checker` | spell check in notes |
| `DavidAnson.vscode-markdownlint` | markdown linting |
| `mikestead.dotenv` | `.env` files for API keys |

`.vscode/extensions.json` lists these so VS Code offers to install them
automatically when the repo is opened elsewhere.

## GPU strategy

Because there is no NVIDIA GPU, `torch` on Windows resolves to the CPU-only
build. That is fine for learning the mechanics — you can read training curves,
watch a loss go down, and debug a training loop, which is the actual skill.

For anything that needs real compute:

| Option | Cost | Good for |
|---|---|---|
| [Google Colab](https://colab.research.google.com) | free, ~12 h/day | Module 11 CNNs, general training |
| [Kaggle Notebooks](https://www.kaggle.com/code) | free, 30 h/week GPU | Kaggle-style comps, Module 18 |
| [Lightning AI](https://lightning.ai) | free tier | persistent GPU studios |

Notebook flow for cloud: develop locally, then push the `.ipynb` to
`/content` in Colab and run it there. Keep the data in `data/` locally and
download the small version, or fetch the dataset from the notebook directly.

Skip TensorFlow unless a specific lesson needs Keras. The default
`torch-cpu.txt` keeps it commented out because it is a ~600 MB download that
duplicates what PyTorch already teaches.

## Troubleshooting

**`python` opens the Microsoft Store**
The Store stub is still first on `PATH`. Use the uv-installed interpreter at
`.venv\Scripts\python.exe`, or run `uv python update-shell` and reopen the
terminal.

**`Activate.ps1` is blocked**
PowerShell execution policy. Either use `.venv\Scripts\python.exe` directly, or:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

**VS Code does not see the packages**
Check the interpreter: `Ctrl+Shift+P` → *Python: Select Interpreter* →
`.\.venv\Scripts\python.exe`. Then reload the window.

**`uv` or `gh` not found after install**
winget updated `PATH` but the terminal was already open. Close and reopen the
terminal, or run:
```powershell
$env:Path = "$([Environment]::GetEnvironmentVariable('Path','Machine'));$([Environment]::GetEnvironmentVariable('Path','User'))"
```

**Kernel dies on a large dataset**
15 GB of RAM is the limit. Load fewer columns, sample the data, or use
`dtype` downcasts in `pd.read_csv`. Closing VS Code frees 1-2 GB.
