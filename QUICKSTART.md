# Quick Start Guide

## 🚀 Running the Application

You have **3 different ways** to run the Time Table Management System:

### **Option 1: Quick Launch (RECOMMENDED) ⭐**

Simply **double-click** the `run.bat` file in the project folder.

- No terminal window required
- Automatically checks for Python and installs dependencies
- Direct launch into the application

**Steps:**
1. Navigate to: `C:\Users\digga\Desktop\Ruksar`
2. Double-click: `run.bat`
3. The application will open immediately in CMD

---

### **Option 2: Create Desktop Shortcut**

Run the shortcut creator to place a launcher on your Desktop.

**Steps:**
1. Double-click: `create_shortcut.bat`
2. A shortcut named "Time Table Management" will appear on your Desktop
3. Click the Desktop shortcut anytime to launch the application

---

### **Option 3: Build Standalone Executable** (Advanced)

Create a standalone `.exe` file that works without Python installed.

**Steps:**
1. Double-click: `build_exe.bat`
2. Wait for the build to complete (takes 1-2 minutes)
3. Find the executable in: `dist\TimeTableManager.exe`
4. You can copy this `.exe` file anywhere and run it independently

**Note:** This requires PyInstaller to be installed.

---

## 📋 File Structure

```
C:\Users\digga\Desktop\Ruksar\
├── run.bat                      ← MAIN LAUNCHER (Double-click this!)
├── create_shortcut.bat          ← Creates Desktop shortcut
├── build_exe.bat                ← Builds standalone executable
├── timetable_management.py      ← Main application
├── database.sql                 ← Database schema
├── requirements.txt             ← Python dependencies
├── launcher.py                  ← Python launcher wrapper
├── README.md                    ← Full documentation
└── timetable.db                 ← Database file (created on first run)
```

---

## ✅ System Requirements

- **Windows 7, 8, 10, or 11**
- **Python 3.7+** (for options 1 & 2)
  - Download from: https://www.python.org/downloads/
  - ✓ Make sure to check "Add Python to PATH" during installation

---

## 🔧 Troubleshooting

### Problem: "Python is not installed"
**Solution:** Install Python from https://www.python.org/downloads/
- During installation, make sure to check "Add Python to PATH"

### Problem: "database.sql not found"
**Solution:** Ensure all files are in the same directory: `C:\Users\digga\Desktop\Ruksar\`

### Problem: Permission denied errors
**Solution:** Run as Administrator
1. Right-click on `run.bat`
2. Select "Run as Administrator"

### Problem: "ModuleNotFoundError: No module named 'tabulate'"
**Solution:** The run.bat script will install it automatically. If it still fails:
```bash
pip install tabulate
```

---

## 💡 Tips & Tricks

1. **Pin to Start Menu:** Right-click the Desktop shortcut → Pin to Start
2. **Quick Access:** Move `run.bat` to your Quick Access folder
3. **Scheduled Tasks:** You can schedule the application to run at specific times using Windows Task Scheduler

---

## 📞 Support

If you encounter any issues:

1. Check that all files are present in the directory
2. Ensure Python is properly installed and in your PATH
3. Try running as Administrator
4. Check the README.md for detailed documentation

---

**Created:** November 2025  
**Status:** Production Ready ✅
