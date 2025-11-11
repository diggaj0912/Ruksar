@echo off
REM Time Table Management System - Enhanced Launcher
REM This script automatically sets up and runs the application

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

REM Check if tabulate is installed
python -c "import tabulate" >nul 2>&1
if %errorlevel% neq 0 (
    cls
    echo.
    echo Installing required packages...
    echo.
    pip install -q tabulate
    if %errorlevel% neq 0 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
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

REM Set window title and run application
title Time Table Management System

REM Run the main application
python timetable_management.py

REM If there's an error, keep window open
if %errorlevel% neq 0 (
    echo.
    echo.
    echo An error occurred. Press any key to close this window.
    pause >nul
)

exit /b %errorlevel%
