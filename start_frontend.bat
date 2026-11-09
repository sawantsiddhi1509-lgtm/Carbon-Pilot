@echo off
cd /d "%~dp0frontend"
start http://localhost:5500
python -m http.server 5500
