"""Repoint a notebook's kernelspec at the project environment.

Study Hub notebooks ship with a kernelspec baked in that names the machine's
global Python, so VS Code resolves `python3` to an interpreter that has no
ipykernel and every cell fails. This rewrites the metadata to the registered
`ml-core` kernel, which points at F:\\ml-journey\\.venv.

Usage:
    .\\.venv\\Scripts\\python.exe scripts\\fix_notebook_kernel.py <notebook.ipynb> [...]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

KERNEL_NAME = "ml-core"
KERNEL_DISPLAY = "Python (ml-core)"


def fix(path: Path) -> bool:
    """Point `path` at the project kernel. Returns True if the file changed."""
    raw = path.read_text(encoding="utf-8")
    nb = json.loads(raw)

    before = json.dumps(nb.get("metadata", {}).get("kernelspec"), sort_keys=True)

    nb.setdefault("metadata", {})["kernelspec"] = {
        "display_name": KERNEL_DISPLAY,
        "language": "python",
        "name": KERNEL_NAME,
    }

    after = json.dumps(nb["metadata"]["kernelspec"], sort_keys=True)
    if before == after:
        print(f"  already correct: {path}")
        return False

    # indent=1 and a trailing newline match what nbformat writes, so the file
    # does not show up as a whole-file diff in git later.
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  repointed: {path}")
    print(f"    was: {before}")
    print(f"    now: {after}")
    return True


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        print("error: pass at least one .ipynb path", file=sys.stderr)
        return 2

    changed = 0
    for arg in argv:
        path = Path(arg)
        if not path.is_file():
            print(f"  not found: {path}", file=sys.stderr)
            return 1
        if path.suffix != ".ipynb":
            print(f"  not a notebook: {path}", file=sys.stderr)
            return 1
        changed += fix(path)

    print(f"\n{changed} file(s) updated.")
    print("In VS Code: Ctrl+Shift+P -> 'Notebook: Select Notebook Kernel'")
    print("           -> 'Python (ml-core)'")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
