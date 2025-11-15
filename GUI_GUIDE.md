═══════════════════════════════════════════════════════════════════════════════
              🎨 TIME TABLE MANAGEMENT SYSTEM - GUI VERSION 🎨
═══════════════════════════════════════════════════════════════════════════════

✅ NOW WITH PROFESSIONAL GRAPHICAL INTERFACE!

The Time Table Management System now has a beautiful GUI (Graphical User Interface)
similar to the Hospital Management System, with windows, buttons, and data tables.

═══════════════════════════════════════════════════════════════════════════════
🖥️ WHAT YOU'LL SEE:
═══════════════════════════════════════════════════════════════════════════════

SCREEN 1: LOGIN/CONNECTION WINDOW
─────────────────────────────────
Title: Time Table Management System
Fields:
  • Host name: localhost (pre-filled)
  • User name: root (pre-filled)
  • Password: 1234567890 (pre-filled)
  • Connect Button (orange)

Simply click "Connect" to proceed.


SCREEN 2: MAIN DASHBOARD
───────────────────────
Header:
  • Date and Time (updates every second)
  • "TIME TABLE MANAGEMENT" title
  • "connect To database" button

Left Sidebar (Buttons):
  ☑ Add Time Table ........... Add new class/schedule
  ☑ Search Time Table ........ Find classes by day
  ☑ Delete Time Table ........ Remove a class
  ☑ Update Time Table ........ Edit existing class
  ☑ Show All ................. Display all entries
  ☑ Export Data .............. Save to text file
  ☑ Exit ..................... Close application

Right Side (Data Table):
  Displays all time table entries in a formatted table with columns:
  • ID ............. Entry number
  • Class .......... Classroom name
  • Teacher ........ Teacher's name
  • Subject ........ Subject code
  • Day ............ Day of week
  • Slot ........... Time slot
  • Type ........... Lecture/Tutorial/Practical/Lab

═══════════════════════════════════════════════════════════════════════════════
🎯 HOW TO USE:
═══════════════════════════════════════════════════════════════════════════════

STEP 1: RUN THE APPLICATION
────────────────────────────
1. Navigate to: C:\Users\digga\Desktop\Ruksar\
2. Double-click: run.bat
3. Wait for Python to load...

STEP 2: CONNECT TO DATABASE
──────────────────────────
You'll see the login window with pre-filled values:
  • Host name: localhost
  • User name: root
  • Password: 1234567890

Simply click "Connect" button to proceed.

✅ Success! Main dashboard will open with all the data.


STEP 3: USE THE FEATURES
────────────────────────

🔹 VIEW ALL DATA:
   • Data loads automatically in the right table
   • Shows all time table entries
   • Scroll through to see all entries

🔹 ADD NEW ENTRY:
   1. Click "Add Time Table" button
   2. New window opens with dropdowns
   3. Select: Classroom, Teacher, Subject, Day, Time Slot
   4. Choose Session Type (Lecture/Tutorial/Practical/Lab)
   5. Click "ADD ENTRY" button
   6. Entry is saved and table updates

🔹 SEARCH BY DAY:
   1. Click "Search Time Table" button
   2. Select a day from dropdown
   3. Click "SEARCH" button
   4. Table shows only entries for that day

🔹 DELETE AN ENTRY:
   1. Click on an entry in the table (highlight it)
   2. Click "Delete Time Table" button
   3. Click "Yes" in confirmation dialog
   4. Entry is deleted and table updates

🔹 SHOW ALL ENTRIES:
   1. Click "Show All" button
   2. Shows all time table entries in the table

🔹 EXPORT DATA:
   1. Click "Export Data" button
   2. Type filename (e.g., "my_schedule")
   3. Click OK
   4. File is created as "my_schedule.txt" in the same folder

🔹 EXIT APPLICATION:
   1. Click "Exit" button
   2. Click "Yes" in confirmation dialog
   3. Application closes

═══════════════════════════════════════════════════════════════════════════════
📊 SAMPLE DATA INCLUDED:
═══════════════════════════════════════════════════════════════════════════════

The system comes with pre-loaded data:

Teachers (5):
  • Dr. John Smith (Computer Science)
  • Prof. Sarah Johnson (Mathematics)
  • Dr. Michael Chen (Physics)
  • Prof. Emma Wilson (English)
  • Dr. Rajesh Kumar (Computer Science)

Classrooms (5):
  • Class A1, A2 (50 capacity each)
  • Class B1, B2 (40 capacity each)
  • Lab 1 (30 capacity)

Subjects (5):
  • Database Management Systems (CS301)
  • Advanced Mathematics (MATH201)
  • Quantum Physics (PHY301)
  • British Literature (ENG201)
  • Web Development (CS305)

Time Slots (8):
  • 08:00-09:00 through 16:15-17:15

Days: Monday - Saturday

Sample Classes: 8 pre-loaded schedules

═══════════════════════════════════════════════════════════════════════════════
🎨 GUI FEATURES:
═══════════════════════════════════════════════════════════════════════════════

✓ Professional color scheme (dark header, light background)
✓ Easy-to-use buttons on left sidebar
✓ Data table with scrolling
✓ Dropdown menus for selecting values
✓ Confirmation dialogs for dangerous operations
✓ Error handling with informative messages
✓ Date and time display in header
✓ Responsive layout that resizes
✓ Windows that pop up for specific tasks
✓ Input validation

═══════════════════════════════════════════════════════════════════════════════
❓ FREQUENTLY ASKED QUESTIONS:
═══════════════════════════════════════════════════════════════════════════════

Q: Where do I click to connect to the database?
A: In the first window, click the orange "Connect" button at the bottom.

Q: The data table is empty after connecting
A: Click "Show All" button or refresh by clicking "Search Time Table" and 
   selecting any day.

Q: Can I edit an existing entry?
A: Yes, delete the old entry and add a new one, or click Update Time Table.

Q: Where are the exported files saved?
A: In the same folder as the application (C:\Users\digga\Desktop\Ruksar\)

Q: How do I exit the application?
A: Click the "Exit" button and confirm.

Q: Can I resize the windows?
A: Yes, you can drag the window edges to resize.

═══════════════════════════════════════════════════════════════════════════════
📁 FILES USED:
═══════════════════════════════════════════════════════════════════════════════

✓ timetable_gui.py ........... Main GUI application (NEW!)
✓ database.sql ............... Database schema and sample data
✓ timetable.db ............... SQLite database file
✓ run.bat .................... Launcher script (updated)
✓ launcher.py ................ Python launcher (updated)

═══════════════════════════════════════════════════════════════════════════════
⚡ QUICK START:
═══════════════════════════════════════════════════════════════════════════════

1. Double-click: run.bat
2. Click: Connect
3. See: Main dashboard with data
4. Try: "Add Time Table", "Search Time Table", "Export Data"
5. Exit: Click "Exit" button

═══════════════════════════════════════════════════════════════════════════════
🎉 THAT'S IT!
═══════════════════════════════════════════════════════════════════════════════

You now have a professional GUI-based Time Table Management System!

Enjoy! 🚀
