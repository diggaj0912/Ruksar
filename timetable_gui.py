import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime
import os

class TimeTableGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Table Management System")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        
        self.conn = None
        self.cursor = None
        
        # Set style
        self.setup_styles()
        
        # Show login window first
        self.show_login_window()
    
    def setup_styles(self):
        """Setup color scheme and styles"""
        self.bg_color = "#f0f0f0"
        self.button_color = "#d9d9d9"
        self.header_color = "#2c3e50"
        self.button_bg_color = "#ffb366"
        self.accent_color = "#4285f4"
        
        self.root.configure(bg=self.bg_color)
    
    def show_login_window(self):
        """Show login screen"""
        self.clear_window()
        
        # Header
        header_frame = tk.Frame(self.root, bg=self.header_color, height=80)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="Time Table Management System", 
                              font=("Arial", 24, "bold"), fg="white", bg=self.header_color)
        title_label.pack(pady=15)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Welcome message
        welcome_label = tk.Label(main_frame, text="Welcome", font=("Arial", 16, "bold"), bg=self.bg_color)
        welcome_label.pack(pady=20)
        
        # Database connection frame
        db_frame = tk.LabelFrame(main_frame, text="Database Connection", font=("Arial", 12, "bold"),
                                bg=self.button_color, padx=15, pady=15)
        db_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Host
        tk.Label(db_frame, text="Host name:", font=("Arial", 11), bg=self.button_color).pack(anchor=tk.W, pady=5)
        self.host_entry = tk.Entry(db_frame, font=("Arial", 11), width=40)
        self.host_entry.insert(0, "localhost")
        self.host_entry.pack(anchor=tk.W, pady=5)
        
        # Username
        tk.Label(db_frame, text="User name:", font=("Arial", 11), bg=self.button_color).pack(anchor=tk.W, pady=5)
        self.user_entry = tk.Entry(db_frame, font=("Arial", 11), width=40)
        self.user_entry.insert(0, "root")
        self.user_entry.pack(anchor=tk.W, pady=5)
        
        # Password
        tk.Label(db_frame, text="Password:", font=("Arial", 11), bg=self.button_color).pack(anchor=tk.W, pady=5)
        self.pass_entry = tk.Entry(db_frame, show="*", font=("Arial", 11), width=40)
        self.pass_entry.insert(0, "1234567890")
        self.pass_entry.pack(anchor=tk.W, pady=5)
        
        # Connect button
        connect_btn = tk.Button(db_frame, text="Connect", font=("Arial", 12, "bold"),
                               bg=self.button_bg_color, fg="white", command=self.connect_database,
                               width=20, cursor="hand2")
        connect_btn.pack(pady=20)
    
    def connect_database(self):
        """Connect to SQLite database"""
        try:
            # For SQLite, we create/connect to local database
            if os.path.exists('timetable.db'):
                self.conn = sqlite3.connect('timetable.db')
                self.cursor = self.conn.cursor()
                messagebox.showinfo("Success", "Database connected successfully!")
                self.show_main_window()
            else:
                # Initialize database from SQL file
                self.conn = sqlite3.connect('timetable.db')
                self.cursor = self.conn.cursor()
                with open('database.sql', 'r') as f:
                    self.cursor.executescript(f.read())
                self.conn.commit()
                messagebox.showinfo("Success", "Database initialized and connected!")
                self.show_main_window()
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect: {str(e)}")
    
    def show_main_window(self):
        """Show main dashboard"""
        self.clear_window()
        
        # Header with date/time
        header_frame = tk.Frame(self.root, bg=self.header_color, height=60)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        left_header = tk.Frame(header_frame, bg=self.header_color)
        left_header.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Date and time
        date_time = datetime.now().strftime("%d/%m/%Y\n%H:%M:%S")
        date_label = tk.Label(left_header, text=date_time, font=("Arial", 10), 
                             fg="white", bg=self.header_color, justify=tk.LEFT)
        date_label.pack(side=tk.LEFT)
        
        # Title
        title_label = tk.Label(header_frame, text="TIME TABLE MANAGEMENT", font=("Arial", 18, "bold"),
                              fg="white", bg=self.header_color)
        title_label.pack(side=tk.LEFT, expand=True)
        
        # Connect button on right
        connect_btn = tk.Button(header_frame, text="connect To database", font=("Arial", 9),
                               bg=self.button_bg_color, fg="white", cursor="hand2",
                               command=self.show_login_window)
        connect_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left sidebar with buttons
        button_frame = tk.Frame(content_frame, bg=self.bg_color, width=150)
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        buttons = [
            ("Add Time Table", self.add_timetable),
            ("Search Time Table", self.search_timetable),
            ("Delete Time Table", self.delete_timetable),
            ("Update Time Table", self.update_timetable),
            ("Show All", self.show_all_timetable),
            ("Export Data", self.export_data),
            ("Exit", self.exit_app)
        ]
        
        for btn_text, cmd in buttons:
            btn = tk.Button(button_frame, text=btn_text, font=("Arial", 10), 
                           bg=self.button_color, fg="black", cursor="hand2",
                           command=cmd, width=18, height=2, wraplength=120)
            btn.pack(pady=8, fill=tk.X)
        
        # Right side - Data display
        data_frame = tk.Frame(content_frame, bg="white", relief=tk.SUNKEN, bd=1)
        data_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        # Column headers
        columns = ("ID", "Class", "Teacher", "Subject", "Day", "Slot", "Type")
        self.tree = ttk.Treeview(data_frame, columns=columns, height=18, show="headings")
        
        # Define column headings and widths
        self.tree.column("ID", width=40, anchor=tk.CENTER)
        self.tree.column("Class", width=80, anchor=tk.W)
        self.tree.column("Teacher", width=120, anchor=tk.W)
        self.tree.column("Subject", width=100, anchor=tk.W)
        self.tree.column("Day", width=60, anchor=tk.CENTER)
        self.tree.column("Slot", width=60, anchor=tk.CENTER)
        self.tree.column("Type", width=70, anchor=tk.CENTER)
        
        for col in columns:
            self.tree.heading(col, text=col)
        
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(data_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Load initial data
        self.load_timetable_data()
    
    def load_timetable_data(self):
        """Load time table data from database"""
        try:
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Fetch data
            query = """
                SELECT 
                    t.timetable_id,
                    c.class_name,
                    te.teacher_name,
                    s.subject_code,
                    d.day_name,
                    ts.slot_name,
                    t.session_type
                FROM timetable t
                JOIN classrooms c ON t.classroom_id = c.classroom_id
                JOIN teachers te ON t.teacher_id = te.teacher_id
                JOIN subjects s ON t.subject_id = s.subject_id
                JOIN days d ON t.day_id = d.day_id
                JOIN time_slots ts ON t.slot_id = ts.slot_id
                ORDER BY d.day_order, ts.start_time
            """
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            
            for row in data:
                self.tree.insert("", tk.END, values=row)
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
    
    def add_timetable(self):
        """Open add time table window"""
        self.open_add_window()
    
    def open_add_window(self):
        """Open add entry window"""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Time Table Entry")
        add_window.geometry("400x500")
        
        # Header
        header = tk.Label(add_window, text="Add Time Table Entry", font=("Arial", 14, "bold"),
                         bg=self.header_color, fg="white")
        header.pack(fill=tk.X, padx=0, pady=0)
        
        # Form frame
        form_frame = tk.Frame(add_window, bg=self.bg_color)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Classroom dropdown
        tk.Label(form_frame, text="Classroom:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W, pady=5)
        classrooms = self.get_classrooms()
        self.classroom_var = tk.StringVar(value=classrooms[0] if classrooms else "")
        classroom_combo = ttk.Combobox(form_frame, textvariable=self.classroom_var,
                                       values=classrooms, state="readonly", width=35)
        classroom_combo.pack(anchor=tk.W, pady=5)
        
        # Teacher dropdown
        tk.Label(form_frame, text="Teacher:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W, pady=5)
        teachers = self.get_teachers()
        self.teacher_var = tk.StringVar(value=teachers[0] if teachers else "")
        teacher_combo = ttk.Combobox(form_frame, textvariable=self.teacher_var,
                                     values=teachers, state="readonly", width=35)
        teacher_combo.pack(anchor=tk.W, pady=5)
        
        # Subject dropdown
        tk.Label(form_frame, text="Subject:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W, pady=5)
        subjects = self.get_subjects()
        self.subject_var = tk.StringVar(value=subjects[0] if subjects else "")
        subject_combo = ttk.Combobox(form_frame, textvariable=self.subject_var,
                                    values=subjects, state="readonly", width=35)
        subject_combo.pack(anchor=tk.W, pady=5)
        
        # Day dropdown
        tk.Label(form_frame, text="Day:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W, pady=5)
        days = self.get_days()
        self.day_var = tk.StringVar(value=days[0] if days else "")
        day_combo = ttk.Combobox(form_frame, textvariable=self.day_var,
                                values=days, state="readonly", width=35)
        day_combo.pack(anchor=tk.W, pady=5)
        
        # Time slot dropdown
        tk.Label(form_frame, text="Time Slot:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W, pady=5)
        slots = self.get_slots()
        self.slot_var = tk.StringVar(value=slots[0] if slots else "")
        slot_combo = ttk.Combobox(form_frame, textvariable=self.slot_var,
                                 values=slots, state="readonly", width=35)
        slot_combo.pack(anchor=tk.W, pady=5)
        
        # Session type dropdown
        tk.Label(form_frame, text="Session Type:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W, pady=5)
        self.session_var = tk.StringVar(value="Lecture")
        session_combo = ttk.Combobox(form_frame, textvariable=self.session_var,
                                    values=["Lecture", "Tutorial", "Practical", "Lab"],
                                    state="readonly", width=35)
        session_combo.pack(anchor=tk.W, pady=5)
        
        # Buttons
        button_frame = tk.Frame(form_frame, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        add_btn = tk.Button(button_frame, text="ADD ENTRY", font=("Arial", 11, "bold"),
                           bg=self.button_bg_color, fg="white", cursor="hand2",
                           command=lambda: self.save_timetable(add_window))
        add_btn.pack(side=tk.LEFT, padx=5)
        
        close_btn = tk.Button(button_frame, text="CLOSE", font=("Arial", 11, "bold"),
                             bg=self.button_color, fg="black", cursor="hand2",
                             command=add_window.destroy)
        close_btn.pack(side=tk.LEFT, padx=5)
    
    def get_classrooms(self):
        """Get list of classrooms"""
        self.cursor.execute("SELECT class_name FROM classrooms")
        return [row[0] for row in self.cursor.fetchall()]
    
    def get_teachers(self):
        """Get list of teachers"""
        self.cursor.execute("SELECT teacher_name FROM teachers")
        return [row[0] for row in self.cursor.fetchall()]
    
    def get_subjects(self):
        """Get list of subjects"""
        self.cursor.execute("SELECT subject_code || ' - ' || subject_name FROM subjects")
        return [row[0] for row in self.cursor.fetchall()]
    
    def get_days(self):
        """Get list of days"""
        self.cursor.execute("SELECT day_name FROM days ORDER BY day_order")
        return [row[0] for row in self.cursor.fetchall()]
    
    def get_slots(self):
        """Get list of time slots"""
        self.cursor.execute("SELECT slot_name FROM time_slots ORDER BY start_time")
        return [row[0] for row in self.cursor.fetchall()]
    
    def save_timetable(self, window):
        """Save new time table entry"""
        try:
            # Get values
            classroom = self.classroom_var.get()
            teacher = self.teacher_var.get()
            subject = self.subject_var.get()
            day = self.day_var.get()
            slot = self.slot_var.get()
            session = self.session_var.get()
            
            # Get IDs
            self.cursor.execute("SELECT classroom_id FROM classrooms WHERE class_name = ?", (classroom,))
            classroom_id = self.cursor.fetchone()[0]
            
            self.cursor.execute("SELECT teacher_id FROM teachers WHERE teacher_name = ?", (teacher,))
            teacher_id = self.cursor.fetchone()[0]
            
            self.cursor.execute("SELECT subject_id FROM subjects WHERE subject_code || ' - ' || subject_name = ?", (subject,))
            subject_id = self.cursor.fetchone()[0]
            
            self.cursor.execute("SELECT day_id FROM days WHERE day_name = ?", (day,))
            day_id = self.cursor.fetchone()[0]
            
            self.cursor.execute("SELECT slot_id FROM time_slots WHERE slot_name = ?", (slot,))
            slot_id = self.cursor.fetchone()[0]
            
            # Insert
            self.cursor.execute("""
                INSERT INTO timetable 
                (classroom_id, teacher_id, subject_id, day_id, slot_id, academic_year, semester, session_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (classroom_id, teacher_id, subject_id, day_id, slot_id, "2024-2025", 1, session))
            
            self.conn.commit()
            messagebox.showinfo("Success", "Time table entry added successfully!")
            self.load_timetable_data()
            window.destroy()
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add entry: {str(e)}")
    
    def search_timetable(self):
        """Search time table"""
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Time Table")
        search_window.geometry("400x200")
        
        header = tk.Label(search_window, text="Search Time Table", font=("Arial", 14, "bold"),
                         bg=self.header_color, fg="white")
        header.pack(fill=tk.X)
        
        frame = tk.Frame(search_window, bg=self.bg_color)
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        tk.Label(frame, text="Search by Day:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W, pady=5)
        days = self.get_days()
        search_var = tk.StringVar(value=days[0] if days else "")
        search_combo = ttk.Combobox(frame, textvariable=search_var, values=days, state="readonly")
        search_combo.pack(anchor=tk.W, pady=5, fill=tk.X)
        
        def search():
            try:
                day = search_var.get()
                for item in self.tree.get_children():
                    self.tree.delete(item)
                
                query = """
                    SELECT 
                        t.timetable_id,
                        c.class_name,
                        te.teacher_name,
                        s.subject_code,
                        d.day_name,
                        ts.slot_name,
                        t.session_type
                    FROM timetable t
                    JOIN classrooms c ON t.classroom_id = c.classroom_id
                    JOIN teachers te ON t.teacher_id = te.teacher_id
                    JOIN subjects s ON t.subject_id = s.subject_id
                    JOIN days d ON t.day_id = d.day_id
                    JOIN time_slots ts ON t.slot_id = ts.slot_id
                    WHERE d.day_name = ?
                    ORDER BY ts.start_time
                """
                self.cursor.execute(query, (day,))
                data = self.cursor.fetchall()
                
                for row in data:
                    self.tree.insert("", tk.END, values=row)
                
                messagebox.showinfo("Success", f"Found {len(data)} entries for {day}")
                search_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        search_btn = tk.Button(frame, text="SEARCH", font=("Arial", 11, "bold"),
                              bg=self.button_bg_color, fg="white", cursor="hand2", command=search)
        search_btn.pack(pady=15)
    
    def delete_timetable(self):
        """Delete time table entry"""
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Warning", "Please select an entry to delete")
            return
        
        values = self.tree.item(item, 'values')
        entry_id = values[0]
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this entry?"):
            try:
                self.cursor.execute("DELETE FROM timetable WHERE timetable_id = ?", (entry_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Entry deleted successfully!")
                self.load_timetable_data()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete: {str(e)}")
    
    def update_timetable(self):
        """Update time table entry"""
        messagebox.showinfo("Update", "Select an entry and use Add window to update")
    
    def show_all_timetable(self):
        """Show all time table entries"""
        self.load_timetable_data()
        messagebox.showinfo("Success", "All entries displayed")
    
    def export_data(self):
        """Export data to file"""
        try:
            filename = simpledialog.askstring("Export", "Enter filename (without extension):")
            if not filename:
                return
            
            with open(f"{filename}.txt", 'w') as f:
                f.write("TIME TABLE MANAGEMENT SYSTEM - REPORT\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*80 + "\n\n")
                
                self.cursor.execute("""
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
                """)
                
                for row in self.cursor.fetchall():
                    f.write(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}\n")
            
            messagebox.showinfo("Success", f"Data exported to {filename}.txt")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def exit_app(self):
        """Exit application"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            if self.conn:
                self.conn.close()
            self.root.quit()
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTableGUI(root)
    root.mainloop()
