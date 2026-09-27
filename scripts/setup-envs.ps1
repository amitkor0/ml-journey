<#
.SYNOPSIS
    Rebuilds the ML Journey Python environments from scratch.

.DESCRIPTION
    Installs Python 3.12 via uv, then creates one virtual environment per
    stage group. Each environment is kept small on purpose - see SETUP.md for
    why a single environment with every ML package is a mistake.

.PARAMETER Torch
    Also build the deep learning environment (.venv-torch). It is a large
    download, so it is opt-in.

.EXAMPLE
    .\scripts\setup-envs.ps1
    .\scripts\setup-envs.ps1 -Torch
#>
[CmdletBinding()]
param(
    [switch]$Torch
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

function Invoke-Step {
    param([string]$Name, [scriptblock]$Action)
    Write-Host "`n=== $Name ===" -ForegroundColor Cyan
    & $Action
}

Invoke-Step 'Python 3.12 via uv' {
    uv python install 3.12
    if ($LASTEXITCODE -ne 0) { throw 'uv python install failed' }
}

Invoke-Step 'Core environment (.venv)' {
    uv venv --python 3.12 .venv
    if ($LASTEXITCODE -ne 0) { throw 'uv venv failed' }
    uv pip install --python .venv\Scripts\python.exe -r requirements\core.txt
    if ($LASTEXITCODE -ne 0) { throw 'core install failed' }
}

Invoke-Step 'Register Jupyter kernel' {
    & .venv\Scripts\python.exe -m ipykernel install --user --name ml-core --display-name 'Python (ml-core)'
}

if ($Torch) {
    Invoke-Step 'Deep learning environment (.venv-torch)' {
        uv venv --python 3.12 .venv-torch
        if ($LASTEXITCODE -ne 0) { throw 'uv venv failed' }
        uv pip install --python .venv-torch\Scripts\python.exe -r requirements\torch-cpu.txt
        if ($LASTEXITCODE -ne 0) { throw 'torch install failed' }
    }
    Invoke-Step 'Register Jupyter kernel (torch)' {
        & .venv-torch\Scripts\python.exe -m ipykernel install --user --name ml-torch --display-name 'Python (ml-torch, CPU)'
    }
}

Write-Host "`nDone. Verify with:" -ForegroundColor Green
Write-Host '  .\.venv\Scripts\python.exe -c "import sklearn, pandas; print(sklearn.__version__)"'
Write-Host '  .\.venv\Scripts\python.exe -m jupyter lab'
