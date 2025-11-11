@echo off
REM Time Table Management System - Setup Script for Windows

echo ========================================
echo Time Table Management System - Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/
    pause
    exit /b 1
)

echo ✓ Python detected
echo.

REM Install dependencies
echo Installing required packages...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ✓ Installation complete!
echo.
echo To start the application, run:
echo   python timetable_management.py
echo.
pause
