@echo off
REM Create Windows Shortcut for Time Table Management System
REM This script creates a desktop shortcut that launches the application

setlocal

set SCRIPT_DIR=%~dp0
set PYTHON_PATH=%PYTHON%

REM Try to find Python
for /f "delims=" %%A in ('where python') do set PYTHON_PATH=%%A

if "%PYTHON_PATH%"=="" (
    echo Error: Python not found. Please install Python.
    pause
    exit /b 1
)

REM Create VBS script to create shortcut
(
echo Set oWS = WScript.CreateObject("WScript.Shell"^)
echo strDesktop = oWS.SpecialFolders("Desktop"^)
echo Set oLink = oWS.CreateShortcut(strDesktop ^& "\Time Table Management.lnk"^)
echo oLink.TargetPath = "%SCRIPT_DIR%run.bat"
echo oLink.WorkingDirectory = "%SCRIPT_DIR%"
echo oLink.IconLocation = "C:\Windows\System32\cmd.exe"
echo oLink.Save
echo WScript.Echo "Shortcut created successfully on Desktop!"
) > create_shortcut.vbs

REM Run the VBS script
cscript create_shortcut.vbs

REM Clean up
del create_shortcut.vbs

echo.
echo Done! You can now find "Time Table Management" shortcut on your Desktop.
echo.
pause
