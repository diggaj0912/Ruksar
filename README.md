# Time Table Management System

A comprehensive SQL-based time table management system built with Python and SQLite. This system allows educational institutions to manage class schedules, teachers, subjects, classrooms, and time slots efficiently.

## 📋 Features

- **Time Table Management**: Create, view, update, and delete class schedules
- **Teacher Management**: Add and manage teacher information with departments and specializations
- **Classroom Management**: Manage classroom details including capacity and location
- **Subject Management**: Organize subjects with codes and credits
- **Time Slot Management**: Configure available class time slots
- **Week Schedule Generation**: Generate and view complete weekly schedules
- **Report Export**: Export detailed time table reports to text files
- **Data Integrity**: Foreign key constraints and unique entries to prevent scheduling conflicts

## 🗄️ Database Structure

### Tables

1. **teachers** - Teacher information and contact details
2. **classrooms** - Classroom details and capacity
3. **subjects** - Course subjects with codes and credits
4. **time_slots** - Available class time slots
5. **days** - Days of the week
6. **timetable** - Main table linking all components with scheduling information

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd c:\Users\digga\Desktop\Ruksar
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python timetable_management.py
   ```

## 📖 Usage

### Main Menu Options

```
⏰ TIME TABLE MANAGEMENT SYSTEM - MAIN MENU
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
```

### Example Workflows

#### Adding a Time Table Entry
1. Select option 1 from the menu
2. Choose classroom from the available list
3. Select teacher for the class
4. Pick the subject to be taught
5. Choose the day and time slot
6. Enter academic year and semester
7. Specify session type (Lecture/Tutorial/Practical/Lab)

#### Viewing the Schedule
1. Select option 2 to view the time table
2. Optionally filter by academic year or semester
3. View results in a formatted table

#### Generating Weekly Schedule
1. Select option 12
2. Enter the academic year (e.g., 2024-2025)
3. Enter the semester
4. View complete week schedule organized by days

#### Exporting Reports
1. Select option 13
2. Enter desired filename
3. Report will be saved as a text file with complete information

## 💾 Database Schema Details

### Key Fields

- **Academic Year**: Format (e.g., 2024-2025)
- **Semester**: 1 or 2
- **Session Type**: Lecture, Tutorial, Practical, Lab
- **Status**: Active (default) or Inactive

### Constraints

- Unique classroom per time slot to prevent double booking
- Foreign key relationships maintain referential integrity
- Automatic timestamps for tracking changes

## 📊 Sample Data

The system comes pre-loaded with:
- 5 Teachers from various departments
- 5 Classrooms (including a lab)
- 5 Subjects
- 8 Time slots (08:00 to 17:15)
- 6 Days of the week
- 8 Sample timetable entries

## 🔧 Technical Details

### Technology Stack
- **Database**: SQLite
- **Language**: Python 3
- **Table Format**: Tabulate library for formatted output

### Data Validation
- Automatic timestamp generation
- Referential integrity through foreign keys
- Unique constraints to prevent duplicate entries

## 📝 Notes

- All times are in 24-hour format
- Database file (timetable.db) is created automatically on first run
- Export reports are saved in the project directory
- The system prevents scheduling conflicts through unique constraints

## 🐛 Troubleshooting

**Q: "No module named 'tabulate'" error**
- A: Run `pip install -r requirements.txt`

**Q: Database not initializing**
- A: Ensure database.sql is in the same directory as timetable_management.py

**Q: Cannot add duplicate entries**
- A: This is by design - the system prevents scheduling conflicts

## 📄 License

This project is provided as-is for educational purposes.

## ✉️ Support

For issues or questions, please review the code comments or refer to the database schema in database.sql.

---

**Created**: 2024
**Version**: 1.0
**Status**: Production Ready
