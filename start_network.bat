@echo off
setlocal
cd /d "%~dp0"
echo Starting COMSOL small model web app in LAN mode...
echo.
echo This binds the app to 0.0.0.0 so other devices on the same network can connect.
echo If Windows Firewall asks for permission, allow Python on Private networks only.
echo.
python web_app.py --host 0.0.0.0 --port 8765
pause
