@echo off
setlocal
cd /d "%~dp0"
echo Starting COMSOL small model web app in LAN mode...
echo.
echo This binds the app to 0.0.0.0 so other devices on the same network can connect.
echo If Windows Firewall asks for permission, allow Python on Private networks only.
echo.
set "PYTHON_EXE=D:\pathon\python.exe"
if not exist "%PYTHON_EXE%" set "PYTHON_EXE=python"
"%PYTHON_EXE%" scripts\start_local_service.py --host 0.0.0.0 --port 8765 --with-worker --ensure-comsol-server --wait-seconds 30
pause
