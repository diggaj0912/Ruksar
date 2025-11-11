@echo off
REM Build executable from Python using PyInstaller
REM This creates a standalone .exe file that doesn't require Python to be installed

echo.
echo ================================================
echo Time Table Management System - Build Executable
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed
    pause
    exit /b 1
)

echo Installing PyInstaller...
pip install pyinstaller >nul 2>&1

if %errorlevel% neq 0 (
    echo Error: Failed to install PyInstaller
    pause
    exit /b 1
)

echo.
echo Building executable...
echo This may take a few minutes...
echo.

REM Build the executable
pyinstaller --onefile ^
    --icon=timetable.ico ^
    --windowed ^
    --name "TimeTableManager" ^
    --add-data "database.sql:." ^
    launcher.py

if %errorlevel% neq 0 (
    echo.
    echo Error: Build failed
    pause
    exit /b 1
)

echo.
echo ================================================
echo BUILD SUCCESSFUL!
echo ================================================
echo.
echo Executable created: dist\TimeTableManager.exe
echo.
echo You can now:
echo 1. Run the executable directly
echo 2. Create a shortcut to it
echo 3. Move it anywhere on your system
echo.
pause
