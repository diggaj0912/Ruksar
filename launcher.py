#!/usr/bin/env python
"""
Time Table Management System - GUI Launcher
This script runs the GUI application and can be converted to an executable using PyInstaller
"""
import subprocess
import sys
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Run the GUI application
    try:
        subprocess.run([sys.executable, 'timetable_gui.py'], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nApplication closed by user.")
        sys.exit(0)

if __name__ == '__main__':
    main()
