# 🎯 How to Run - Visual Guide

## ⚡ FASTEST WAY - Just Double-Click!

### Step 1: Open File Explorer
Navigate to your project folder:
```
C:\Users\digga\Desktop\Ruksar\
```

### Step 2: Find and Double-Click `run.bat`
```
📁 Ruksar
├── 📄 run.bat ...................... ← DOUBLE-CLICK THIS!
├── database.sql
├── timetable_management.py
├── requirements.txt
└── ... (other files)
```

### Step 3: Application Launches!
The CMD window will open and show the menu automatically.

---

## 📌 THREE METHODS TO LAUNCH

### Method 1️⃣ : Direct CMD Launch (EASIEST)
```
ACTION: Double-click run.bat
TIME: Instant
RESULT: Application opens in CMD window
```

### Method 2️⃣ : Desktop Shortcut (CONVENIENT)
```
ACTION: Double-click create_shortcut.bat
        Then use Desktop shortcut daily
TIME: Instant
RESULT: Creates a Desktop icon for quick access
```

### Method 3️⃣ : Standalone Executable (PORTABLE)
```
ACTION: Double-click build_exe.bat
        Wait 1-2 minutes for build
        Run dist\TimeTableManager.exe
TIME: 2-3 minutes (one-time)
RESULT: Portable .exe file that works anywhere
```

---

## 🖥️ What You'll See

When you double-click `run.bat`, you'll see:

```
======================================================================
  ⏰ TIME TABLE MANAGEMENT SYSTEM - MAIN MENU
======================================================================

  📚 TIME TABLE MENU
  --------------------------------------------------
  1. Add Time Table Entry
  2. View Time Table
  3. Update Time Table Entry
  4. Delete Time Table Entry
  5. View Teachers
  6. Add Teacher
  7. View Classrooms
  8. Add Classroom
  9. View Subjects
  10. Add Subject
  11. View Time Slots
  12. Generate Full Week Schedule
  13. Export Time Table Report
  0. Exit
  --------------------------------------------------
  Choose an option: █
```

---

## ✅ Quick Checklist

Before running, make sure:

- ✓ Python is installed (python --version works)
- ✓ All files are in `C:\Users\digga\Desktop\Ruksar\`
- ✓ `run.bat` file exists
- ✓ `database.sql` file exists
- ✓ `timetable_management.py` file exists

---

## 📝 Usage Example

After running `run.bat`:

```
Choose an option: 2
```

Press `2` and Enter to view the time table:

```
ID  Class      Teacher             Subject    Day        Slot    Start  End     Type
--  ---------  ----------------   --------   --------   ------  -----  -----  ------
1   Class A1   Dr. John Smith      CS301      Monday     Slot 1  08:00  09:00  Lecture
2   Class A2   Prof. Sarah Johnson MATH201    Tuesday    Slot 2  09:00  10:00  Lecture
3   Class B1   Dr. Michael Chen    PHY301     Wednesday  Slot 3  10:15  11:15  Lecture
```

---

## 🎓 Features Available

Once running, you can:

- ✏️ **Add** new time table entries
- 👁️ **View** all schedules
- ✏️ **Update** existing entries
- 🗑️ **Delete** entries
- 👨‍🏫 **Manage** teachers and classrooms
- 📚 **Organize** subjects
- 📅 **Generate** full week schedules
- 📊 **Export** reports to text files

---

## 🚀 Pro Tips

1. **Pin to Taskbar:**
   - Right-click `run.bat` → Send to → Desktop (create shortcut)
   - Right-click shortcut → Pin to Taskbar

2. **Always-on-top Window:**
   - Alt + Space → P (in CMD) makes window always visible

3. **Batch Processing:**
   - You can schedule `run.bat` to run daily using Windows Task Scheduler

4. **Network Share:**
   - Place the folder on a network drive to share with others

---

## ❓ Frequently Asked Questions

**Q: Do I need to install Python every time?**
A: No, just once. After Python is installed, double-click `run.bat` anytime.

**Q: Can I move these files?**
A: Yes, keep all files together in one folder. `run.bat` will work from anywhere.

**Q: Is there a graphical version?**
A: The current version is CMD-based (like your inventory system reference). GUI version can be created if needed.

**Q: How do I close the application?**
A: Press `0` to exit, or Ctrl+C in the terminal.

---

## 📞 Need Help?

1. **Check QUICKSTART.md** for troubleshooting
2. **Read README.md** for full documentation
3. **Run test_system.py** to verify setup: `python test_system.py`

---

**Ready to go!** 🎉  
Just double-click `run.bat` and start managing your timetable!
