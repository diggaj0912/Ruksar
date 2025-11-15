@echo off
REM Time Table Management System - GUI Launcher
REM This script automatically sets up and runs the GUI application

setlocal enabledelayedexpansion

cd /d "%~dp0"

REM Set window title and formatting
title Time Table Management System - Loading...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    cls
    echo.
    echo ====================================================================
    echo              ERROR: Python is not installed!
    echo ====================================================================
    echo.
    echo Please install Python 3.7 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    echo ====================================================================
    echo.
    pause
    exit /b 1
)

REM Check if required packages are installed
python -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    cls
    echo.
    echo Installing required packages...
    echo.
    pip install -q tabulate
    echo.
    echo Packages installed successfully!
    echo.
)

REM Check if database.sql exists
if not exist database.sql (
    echo.
    echo ERROR: database.sql not found!
    echo Please ensure all files are in the same directory.
    echo.
    pause
    exit /b 1
)

REM Set window title and run GUI application
title Time Table Management System

REM Run the GUI application
python timetable_gui.py

REM If there's an error, keep window open
if %errorlevel% neq 0 (
    echo.
    echo.
    echo An error occurred. Press any key to close this window.
    pause >nul
)

exit /b %errorlevel%
