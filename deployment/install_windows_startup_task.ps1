param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$script = Join-Path $PSScriptRoot "start_windows_execution_node.ps1"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$script`" -Python `"$Python`""
$trigger = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -TaskName "COMSOLModelCodex" -Action $action -Trigger $trigger -Description "Start COMSOL Model Codex and its local execution worker after Windows logon." -Force
Write-Output "Scheduled task COMSOLModelCodex installed. It starts after Windows logon."
