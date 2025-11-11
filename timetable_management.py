import sqlite3
import os
from datetime import datetime
from tabulate import tabulate
import sys

# Database configuration
DB_PATH = 'timetable.db'

class TimeTableManager:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.init_database()

    def init_database(self):
        """Initialize database connection and create tables"""
        try:
            self.conn = sqlite3.connect(DB_PATH)
            self.cursor = self.conn.cursor()
            print(f"✓ Connected to database: {DB_PATH}")
        except sqlite3.Error as e:
            print(f"✗ Database connection error: {e}")
            sys.exit(1)

    def load_sql_file(self, filename):
        """Load and execute SQL file"""
        try:
            with open(filename, 'r') as f:
                sql_script = f.read()
            self.cursor.executescript(sql_script)
            self.conn.commit()
            print(f"✓ Database schema initialized successfully!")
        except Exception as e:
            print(f"✗ Error loading SQL file: {e}")

    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self, title):
        """Display formatted header"""
        print("\n" + "="*70)
        print(f"  ⏰ TIME TABLE MANAGEMENT SYSTEM - {title}")
        print("="*70 + "\n")

    def display_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.display_header("MAIN MENU")
        print("  📚 TIME TABLE MENU")
        print("  " + "-"*50)
        print("  1. Add Time Table Entry")
        print("  2. View Time Table")
        print("  3. Update Time Table Entry")
        print("  4. Delete Time Table Entry")
        print("  5. View Teachers")
        print("  6. Add Teacher")
        print("  7. View Classrooms")
        print("  8. Add Classroom")
        print("  9. View Subjects")
        print("  10. Add Subject")
        print("  11. View Time Slots")
        print("  12. Generate Full Week Schedule")
        print("  13. Export Time Table Report")
        print("  0. Exit")
        print("  " + "-"*50)

    def add_timetable_entry(self):
        """Add new time table entry"""
        self.display_header("ADD TIME TABLE ENTRY")
        try:
            print("Available Classrooms:")
            classrooms = self.cursor.execute("SELECT classroom_id, class_name FROM classrooms").fetchall()
            for cid, cname in classrooms:
                print(f"  {cid}. {cname}")
            classroom_id = int(input("\nSelect Classroom ID: "))

            print("\nAvailable Teachers:")
            teachers = self.cursor.execute("SELECT teacher_id, teacher_name FROM teachers").fetchall()
            for tid, tname in teachers:
                print(f"  {tid}. {tname}")
            teacher_id = int(input("\nSelect Teacher ID: "))

            print("\nAvailable Subjects:")
            subjects = self.cursor.execute("SELECT subject_id, subject_name FROM subjects").fetchall()
            for sid, sname in subjects:
                print(f"  {sid}. {sname}")
            subject_id = int(input("\nSelect Subject ID: "))

            print("\nAvailable Days:")
            days = self.cursor.execute("SELECT day_id, day_name FROM days ORDER BY day_order").fetchall()
            for did, dname in days:
                print(f"  {did}. {dname}")
            day_id = int(input("\nSelect Day ID: "))

            print("\nAvailable Time Slots:")
            slots = self.cursor.execute("SELECT slot_id, slot_name, start_time, end_time FROM time_slots").fetchall()
            for slid, slname, stime, etime in slots:
                print(f"  {slid}. {slname} ({stime}-{etime})")
            slot_id = int(input("\nSelect Slot ID: "))

            academic_year = input("\nEnter Academic Year (e.g., 2024-2025): ")
            semester = int(input("Enter Semester (1 or 2): "))
            session_type = input("Enter Session Type (Lecture/Tutorial/Practical/Lab): ")

            self.cursor.execute("""
                INSERT INTO timetable 
                (classroom_id, teacher_id, subject_id, day_id, slot_id, academic_year, semester, session_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (classroom_id, teacher_id, subject_id, day_id, slot_id, academic_year, semester, session_type))
            
            self.conn.commit()
            print("\n✓ Time table entry added successfully!")
        except Exception as e:
            print(f"\n✗ Error adding entry: {e}")
        input("\nPress Enter to continue...")

    def view_timetable(self):
        """View time table with all details"""
        self.display_header("VIEW TIME TABLE")
        try:
            academic_year = input("Enter Academic Year (leave blank for all): ") or None
            semester = input("Enter Semester (leave blank for all): ") or None

            query = """
                SELECT 
                    t.timetable_id,
                    c.class_name,
                    te.teacher_name,
                    s.subject_code,
                    d.day_name,
                    ts.slot_name,
                    ts.start_time,
                    ts.end_time,
                    t.session_type,
                    t.academic_year,
                    t.semester
                FROM timetable t
                JOIN classrooms c ON t.classroom_id = c.classroom_id
                JOIN teachers te ON t.teacher_id = te.teacher_id
                JOIN subjects s ON t.subject_id = s.subject_id
                JOIN days d ON t.day_id = d.day_id
                JOIN time_slots ts ON t.slot_id = ts.slot_id
                WHERE 1=1
            """
            params = []

            if academic_year:
                query += " AND t.academic_year = ?"
                params.append(academic_year)
            if semester:
                query += " AND t.semester = ?"
                params.append(int(semester))

            query += " ORDER BY d.day_order, ts.start_time"

            data = self.cursor.execute(query, params).fetchall()
            
            if data:
                headers = ["ID", "Class", "Teacher", "Subject", "Day", "Slot", "Start", "End", "Type", "Year", "Sem"]
                print("\n" + tabulate(data, headers=headers, tablefmt="grid"))
            else:
                print("\n✗ No time table entries found!")
        except Exception as e:
            print(f"\n✗ Error viewing time table: {e}")
        input("\nPress Enter to continue...")

    def update_timetable_entry(self):
        """Update existing time table entry"""
        self.display_header("UPDATE TIME TABLE ENTRY")
        try:
            timetable_id = int(input("Enter Time Table ID to update: "))
            
            # Show current entry
            current = self.cursor.execute("""
                SELECT classroom_id, teacher_id, subject_id, day_id, slot_id, academic_year, semester, session_type
                FROM timetable WHERE timetable_id = ?
            """, (timetable_id,)).fetchone()

            if not current:
                print("✗ Time table entry not found!")
                input("\nPress Enter to continue...")
                return

            print("\nCurrent entry details:")
            print(f"  Classroom ID: {current[0]}, Teacher ID: {current[1]}, Subject ID: {current[2]}")
            print(f"  Day ID: {current[3]}, Slot ID: {current[4]}")
            print(f"  Academic Year: {current[5]}, Semester: {current[6]}, Type: {current[7]}")

            print("\nEnter new values (leave blank to keep current):")
            classroom_id = input("Classroom ID: ") or current[0]
            teacher_id = input("Teacher ID: ") or current[1]
            subject_id = input("Subject ID: ") or current[2]
            day_id = input("Day ID: ") or current[3]
            slot_id = input("Slot ID: ") or current[4]
            academic_year = input("Academic Year: ") or current[5]
            semester = input("Semester: ") or current[6]
            session_type = input("Session Type: ") or current[7]

            self.cursor.execute("""
                UPDATE timetable
                SET classroom_id=?, teacher_id=?, subject_id=?, day_id=?, slot_id=?, 
                    academic_year=?, semester=?, session_type=?, updated_at=CURRENT_TIMESTAMP
                WHERE timetable_id=?
            """, (classroom_id, teacher_id, subject_id, day_id, slot_id, 
                  academic_year, semester, session_type, timetable_id))
            
            self.conn.commit()
            print("\n✓ Time table entry updated successfully!")
        except Exception as e:
            print(f"\n✗ Error updating entry: {e}")
        input("\nPress Enter to continue...")

    def delete_timetable_entry(self):
        """Delete time table entry"""
        self.display_header("DELETE TIME TABLE ENTRY")
        try:
            timetable_id = int(input("Enter Time Table ID to delete: "))
            confirm = input("Are you sure? (yes/no): ").lower()
            
            if confirm == 'yes':
                self.cursor.execute("DELETE FROM timetable WHERE timetable_id=?", (timetable_id,))
                self.conn.commit()
                print("\n✓ Time table entry deleted successfully!")
            else:
                print("\n✗ Deletion cancelled!")
        except Exception as e:
            print(f"\n✗ Error deleting entry: {e}")
        input("\nPress Enter to continue...")

    def view_teachers(self):
        """View all teachers"""
        self.display_header("VIEW TEACHERS")
        try:
            data = self.cursor.execute("""
                SELECT teacher_id, teacher_name, department, specialization, email
                FROM teachers ORDER BY teacher_id
            """).fetchall()
            
            if data:
                headers = ["ID", "Name", "Department", "Specialization", "Email"]
                print(tabulate(data, headers=headers, tablefmt="grid"))
            else:
                print("✗ No teachers found!")
        except Exception as e:
            print(f"\n✗ Error viewing teachers: {e}")
        input("\nPress Enter to continue...")

    def add_teacher(self):
        """Add new teacher"""
        self.display_header("ADD TEACHER")
        try:
            name = input("Enter Teacher Name: ")
            department = input("Enter Department: ")
            specialization = input("Enter Specialization: ")
            contact = input("Enter Contact Number: ")
            email = input("Enter Email: ")

            self.cursor.execute("""
                INSERT INTO teachers (teacher_name, department, specialization, contact_number, email)
                VALUES (?, ?, ?, ?, ?)
            """, (name, department, specialization, contact, email))
            
            self.conn.commit()
            print("\n✓ Teacher added successfully!")
        except Exception as e:
            print(f"\n✗ Error adding teacher: {e}")
        input("\nPress Enter to continue...")

    def view_classrooms(self):
        """View all classrooms"""
        self.display_header("VIEW CLASSROOMS")
        try:
            data = self.cursor.execute("""
                SELECT classroom_id, class_name, capacity, room_number, building
                FROM classrooms ORDER BY classroom_id
            """).fetchall()
            
            if data:
                headers = ["ID", "Class Name", "Capacity", "Room #", "Building"]
                print(tabulate(data, headers=headers, tablefmt="grid"))
            else:
                print("✗ No classrooms found!")
        except Exception as e:
            print(f"\n✗ Error viewing classrooms: {e}")
        input("\nPress Enter to continue...")

    def add_classroom(self):
        """Add new classroom"""
        self.display_header("ADD CLASSROOM")
        try:
            class_name = input("Enter Class Name: ")
            capacity = int(input("Enter Capacity: "))
            room_number = input("Enter Room Number: ")
            building = input("Enter Building Name: ")

            self.cursor.execute("""
                INSERT INTO classrooms (class_name, capacity, room_number, building)
                VALUES (?, ?, ?, ?)
            """, (class_name, capacity, room_number, building))
            
            self.conn.commit()
            print("\n✓ Classroom added successfully!")
        except Exception as e:
            print(f"\n✗ Error adding classroom: {e}")
        input("\nPress Enter to continue...")

    def view_subjects(self):
        """View all subjects"""
        self.display_header("VIEW SUBJECTS")
        try:
            data = self.cursor.execute("""
                SELECT subject_id, subject_name, subject_code, credits, department
                FROM subjects ORDER BY subject_id
            """).fetchall()
            
            if data:
                headers = ["ID", "Subject Name", "Code", "Credits", "Department"]
                print(tabulate(data, headers=headers, tablefmt="grid"))
            else:
                print("✗ No subjects found!")
        except Exception as e:
            print(f"\n✗ Error viewing subjects: {e}")
        input("\nPress Enter to continue...")

    def add_subject(self):
        """Add new subject"""
        self.display_header("ADD SUBJECT")
        try:
            name = input("Enter Subject Name: ")
            code = input("Enter Subject Code: ")
            credits = int(input("Enter Credits: "))
            department = input("Enter Department: ")

            self.cursor.execute("""
                INSERT INTO subjects (subject_name, subject_code, credits, department)
                VALUES (?, ?, ?, ?)
            """, (name, code, credits, department))
            
            self.conn.commit()
            print("\n✓ Subject added successfully!")
        except Exception as e:
            print(f"\n✗ Error adding subject: {e}")
        input("\nPress Enter to continue...")

    def view_time_slots(self):
        """View all time slots"""
        self.display_header("VIEW TIME SLOTS")
        try:
            data = self.cursor.execute("""
                SELECT slot_id, slot_name, start_time, end_time, duration_minutes
                FROM time_slots ORDER BY start_time
            """).fetchall()
            
            if data:
                headers = ["ID", "Slot Name", "Start Time", "End Time", "Duration (min)"]
                print(tabulate(data, headers=headers, tablefmt="grid"))
            else:
                print("✗ No time slots found!")
        except Exception as e:
            print(f"\n✗ Error viewing time slots: {e}")
        input("\nPress Enter to continue...")

    def generate_schedule(self):
        """Generate full week schedule"""
        self.display_header("FULL WEEK SCHEDULE")
        try:
            academic_year = input("Enter Academic Year: ")
            semester = int(input("Enter Semester: "))

            days = self.cursor.execute("SELECT day_id, day_name FROM days ORDER BY day_order").fetchall()

            for day_id, day_name in days:
                print(f"\n{'='*80}")
                print(f"  📅 {day_name.upper()}")
                print(f"{'='*80}")

                schedule = self.cursor.execute("""
                    SELECT 
                        ts.start_time,
                        ts.end_time,
                        c.class_name,
                        te.teacher_name,
                        s.subject_code,
                        t.session_type
                    FROM timetable t
                    JOIN classrooms c ON t.classroom_id = c.classroom_id
                    JOIN teachers te ON t.teacher_id = te.teacher_id
                    JOIN subjects s ON t.subject_id = s.subject_id
                    JOIN time_slots ts ON t.slot_id = ts.slot_id
                    WHERE t.day_id = ? AND t.academic_year = ? AND t.semester = ?
                    ORDER BY ts.start_time
                """, (day_id, academic_year, semester)).fetchall()

                if schedule:
                    headers = ["Time", "Class", "Teacher", "Subject", "Type"]
                    formatted_data = []
                    for row in schedule:
                        formatted_data.append((f"{row[0]}-{row[1]}", row[2], row[3], row[4], row[5]))
                    print(tabulate(formatted_data, headers=headers, tablefmt="grid"))
                else:
                    print("  No classes scheduled for this day.")

        except Exception as e:
            print(f"\n✗ Error generating schedule: {e}")
        input("\nPress Enter to continue...")

    def export_report(self):
        """Export time table report"""
        self.display_header("EXPORT TIME TABLE REPORT")
        try:
            filename = input("Enter filename (without extension): ") + ".txt"
            
            with open(filename, 'w') as f:
                f.write("="*100 + "\n")
                f.write("TIME TABLE MANAGEMENT SYSTEM - FULL REPORT\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*100 + "\n\n")

                # Teachers
                f.write("\nTEACHERS:\n")
                f.write("-"*100 + "\n")
                teachers = self.cursor.execute("SELECT teacher_id, teacher_name, department, email FROM teachers").fetchall()
                for tid, tname, dept, email in teachers:
                    f.write(f"  {tid}. {tname} | {dept} | {email}\n")

                # Classrooms
                f.write("\n\nCLASSROOMS:\n")
                f.write("-"*100 + "\n")
                classrooms = self.cursor.execute("SELECT classroom_id, class_name, capacity, room_number FROM classrooms").fetchall()
                for cid, cname, cap, room in classrooms:
                    f.write(f"  {cid}. {cname} | Capacity: {cap} | Room: {room}\n")

                # Time Table
                f.write("\n\nTIME TABLE:\n")
                f.write("-"*100 + "\n")
                timetable = self.cursor.execute("""
                    SELECT 
                        c.class_name,
                        te.teacher_name,
                        s.subject_code,
                        d.day_name,
                        ts.start_time,
                        t.session_type
                    FROM timetable t
                    JOIN classrooms c ON t.classroom_id = c.classroom_id
                    JOIN teachers te ON t.teacher_id = te.teacher_id
                    JOIN subjects s ON t.subject_id = s.subject_id
                    JOIN days d ON t.day_id = d.day_id
                    JOIN time_slots ts ON t.slot_id = ts.slot_id
                    ORDER BY d.day_order, ts.start_time
                """).fetchall()
                for row in timetable:
                    f.write(f"  {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}\n")

            print(f"\n✓ Report exported successfully to {filename}!")
        except Exception as e:
            print(f"\n✗ Error exporting report: {e}")
        input("\nPress Enter to continue...")

    def run(self):
        """Main application loop"""
        if os.path.exists('database.sql'):
            self.load_sql_file('database.sql')
        
        while True:
            self.display_menu()
            choice = input("  Choose an option: ").strip()

            if choice == '1':
                self.add_timetable_entry()
            elif choice == '2':
                self.view_timetable()
            elif choice == '3':
                self.update_timetable_entry()
            elif choice == '4':
                self.delete_timetable_entry()
            elif choice == '5':
                self.view_teachers()
            elif choice == '6':
                self.add_teacher()
            elif choice == '7':
                self.view_classrooms()
            elif choice == '8':
                self.add_classroom()
            elif choice == '9':
                self.view_subjects()
            elif choice == '10':
                self.add_subject()
            elif choice == '11':
                self.view_time_slots()
            elif choice == '12':
                self.generate_schedule()
            elif choice == '13':
                self.export_report()
            elif choice == '0':
                print("\n👋 Thank you for using Time Table Management System!")
                self.conn.close()
                break
            else:
                print("\n✗ Invalid option! Please try again.")
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    manager = TimeTableManager()
    manager.run()
