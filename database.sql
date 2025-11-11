-- Time Table Management System Database
-- SQLite Database Schema

-- Create database tables

-- Teachers table
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name TEXT NOT NULL,
    department TEXT NOT NULL,
    specialization TEXT,
    contact_number TEXT,
    email TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Classrooms table
CREATE TABLE IF NOT EXISTS classrooms (
    classroom_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL UNIQUE,
    capacity INTEGER,
    room_number TEXT,
    building TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Subjects table
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL UNIQUE,
    subject_code TEXT NOT NULL UNIQUE,
    credits INTEGER,
    department TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Time Slots table
CREATE TABLE IF NOT EXISTS time_slots (
    slot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    slot_name TEXT NOT NULL UNIQUE,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    duration_minutes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Days table
CREATE TABLE IF NOT EXISTS days (
    day_id INTEGER PRIMARY KEY AUTOINCREMENT,
    day_name TEXT NOT NULL UNIQUE,
    day_order INTEGER UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Time Table table (Main table)
CREATE TABLE IF NOT EXISTS timetable (
    timetable_id INTEGER PRIMARY KEY AUTOINCREMENT,
    classroom_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    day_id INTEGER NOT NULL,
    slot_id INTEGER NOT NULL,
    academic_year TEXT,
    semester INTEGER,
    session_type TEXT DEFAULT 'Lecture',
    status TEXT DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(classroom_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (day_id) REFERENCES days(day_id),
    FOREIGN KEY (slot_id) REFERENCES time_slots(slot_id),
    UNIQUE(classroom_id, day_id, slot_id, academic_year, semester)
);

-- Insert sample days
INSERT OR IGNORE INTO days (day_name, day_order) VALUES 
('Monday', 1),
('Tuesday', 2),
('Wednesday', 3),
('Thursday', 4),
('Friday', 5),
('Saturday', 6);

-- Insert sample time slots
INSERT OR IGNORE INTO time_slots (slot_name, start_time, end_time, duration_minutes) VALUES 
('Slot 1', '08:00', '09:00', 60),
('Slot 2', '09:00', '10:00', 60),
('Slot 3', '10:15', '11:15', 60),
('Slot 4', '11:15', '12:15', 60),
('Slot 5', '13:00', '14:00', 60),
('Slot 6', '14:00', '15:00', 60),
('Slot 7', '15:15', '16:15', 60),
('Slot 8', '16:15', '17:15', 60);

-- Insert sample teachers
INSERT OR IGNORE INTO teachers (teacher_name, department, specialization, contact_number, email) VALUES 
('Dr. John Smith', 'Computer Science', 'Database Systems', '555-0101', 'john.smith@university.edu'),
('Prof. Sarah Johnson', 'Mathematics', 'Calculus', '555-0102', 'sarah.johnson@university.edu'),
('Dr. Michael Chen', 'Physics', 'Quantum Mechanics', '555-0103', 'michael.chen@university.edu'),
('Prof. Emma Wilson', 'English', 'Literature', '555-0104', 'emma.wilson@university.edu'),
('Dr. Rajesh Kumar', 'Computer Science', 'Web Development', '555-0105', 'rajesh.kumar@university.edu');

-- Insert sample classrooms
INSERT OR IGNORE INTO classrooms (class_name, capacity, room_number, building) VALUES 
('Class A1', 50, '101', 'Main Building'),
('Class A2', 50, '102', 'Main Building'),
('Class B1', 40, '201', 'Science Building'),
('Class B2', 40, '202', 'Science Building'),
('Lab 1', 30, '301', 'Computer Lab Building');

-- Insert sample subjects
INSERT OR IGNORE INTO subjects (subject_name, subject_code, credits, department) VALUES 
('Database Management Systems', 'CS301', 3, 'Computer Science'),
('Advanced Mathematics', 'MATH201', 4, 'Mathematics'),
('Quantum Physics', 'PHY301', 3, 'Physics'),
('British Literature', 'ENG201', 3, 'English'),
('Web Development', 'CS305', 3, 'Computer Science');

-- Insert sample timetable entries
INSERT OR IGNORE INTO timetable (classroom_id, teacher_id, subject_id, day_id, slot_id, academic_year, semester, session_type) VALUES 
(1, 1, 1, 1, 1, '2024-2025', 1, 'Lecture'),
(2, 2, 2, 2, 2, '2024-2025', 1, 'Lecture'),
(3, 3, 3, 3, 3, '2024-2025', 1, 'Lecture'),
(4, 4, 4, 4, 4, '2024-2025', 1, 'Lecture'),
(5, 5, 5, 1, 2, '2024-2025', 1, 'Lab'),
(1, 2, 2, 1, 3, '2024-2025', 1, 'Lecture'),
(2, 3, 3, 2, 4, '2024-2025', 1, 'Tutorial'),
(3, 1, 1, 3, 5, '2024-2025', 1, 'Practical');
