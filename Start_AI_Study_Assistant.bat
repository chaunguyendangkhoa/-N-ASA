@echo off
title AI Study Assistant

echo ===============================
echo      AI Study Assistant
echo ===============================
echo.

REM ==============================
REM Chay Ollama
REM ==============================

start cmd /k "ollama serve"

timeout /t 3 >nul

REM ==============================
REM Chay Streamlit
REM ==============================

start cmd /k "cd /d %~dp0 && python -m streamlit run app.py"

timeout /t 8 >nul

REM ==============================
REM Chay Cloudflare Tunnel
REM ==============================

start cmd /k "cd /d %USERPROFILE%\Desktop\cloudflare && cloudflared tunnel --url http://localhost:8501"

timeout /t 5 >nul

REM ==============================
REM Mo trinh duyet
REM ==============================

start http://localhost:8501

echo.
echo Da khoi dong AI Study Assistant.
pause