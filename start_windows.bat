@echo off
setlocal
cd /d "%~dp0"
set "PYTHON_EXE=D:\pathon\python.exe"
if not exist "%PYTHON_EXE%" set "PYTHON_EXE=python"
echo Starting or reusing the COMSOL small model web service...
"%PYTHON_EXE%" "%~dp0scripts\start_local_service.py" --port 8880 --open --with-worker --wait-seconds 30
echo Service command completed. If initialization is pending, open http://127.0.0.1:8880/ after a short wait.
endlocal