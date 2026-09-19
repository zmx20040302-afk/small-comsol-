param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$startup = [Environment]::GetFolderPath("Startup")
$script = Join-Path $PSScriptRoot "start_windows_execution_node.ps1"
$target = Join-Path $startup "COMSOLModelCodex.cmd"

$command = "& '$script' -Python '$Python'"
$encoded = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command))
$content = "@echo off`r`npowershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand $encoded`r`n"
Set-Content -LiteralPath $target -Value $content -Encoding ASCII
Write-Output "Startup launcher installed: $target"
