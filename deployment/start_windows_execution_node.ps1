param(
    [string]$Python = "python",
    [int]$Port = 8880,
    [switch]$WorkerOnly,
    [switch]$Open
)

$root = Split-Path -Parent $PSScriptRoot
$launcher = Join-Path $root "scripts\start_local_service.py"
$arguments = @("`"$launcher`"", "--port", "$Port", "--with-worker", "--ensure-comsol-server")
if ($WorkerOnly) { $arguments += "--worker-only" }
if ($Open) { $arguments += "--open" }

Start-Process -FilePath $Python `
    -ArgumentList $arguments `
    -WorkingDirectory $root `
    -WindowStyle Hidden

Write-Output "COMSOL task center startup requested. Local web port: $Port; COMSOL mphserver is checked automatically."
