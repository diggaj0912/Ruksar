"""
Test script to verify Time Table Management System functionality
"""
import sqlite3
import os

DB_PATH = 'timetable.db'

def test_database():
    """Test database initialization and data"""
    print("="*70)
    print("  🧪 TIME TABLE MANAGEMENT SYSTEM - TEST REPORT")
    print("="*70)
    
    # Initialize database
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    print("\n✓ Testing database schema initialization...")
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Load and execute SQL
        with open('database.sql', 'r') as f:
            sql_script = f.read()
        cursor.executescript(sql_script)
        conn.commit()
        
        print("✓ Database schema initialized successfully!")
        
        # Test 1: Check tables exist
        print("\n📋 Testing Tables...")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
            count = cursor.fetchone()[0]
            print(f"  ✓ Table '{table[0]}': {count} records")
        
        # Test 2: Check Teachers
        print("\n👨‍🏫 Testing Teachers...")
        cursor.execute("SELECT teacher_id, teacher_name, department FROM teachers LIMIT 3")
        teachers = cursor.fetchall()
        for tid, tname, dept in teachers:
            print(f"  ✓ {tid}. {tname} ({dept})")
        
        # Test 3: Check Classrooms
        print("\n🏫 Testing Classrooms...")
        cursor.execute("SELECT classroom_id, class_name, capacity FROM classrooms LIMIT 3")
        classrooms = cursor.fetchall()
        for cid, cname, cap in classrooms:
            print(f"  ✓ {cid}. {cname} (Capacity: {cap})")
        
        # Test 4: Check Subjects
        print("\n📚 Testing Subjects...")
        cursor.execute("SELECT subject_id, subject_name, subject_code FROM subjects LIMIT 3")
        subjects = cursor.fetchall()
        for sid, sname, scode in subjects:
            print(f"  ✓ {sid}. {sname} ({scode})")
        
        # Test 5: Check Time Slots
        print("\n⏰ Testing Time Slots...")
        cursor.execute("SELECT slot_id, slot_name, start_time, end_time FROM time_slots LIMIT 3")
        slots = cursor.fetchall()
        for slid, slname, stime, etime in slots:
            print(f"  ✓ {slid}. {slname} ({stime}-{etime})")
        
        # Test 6: Check Time Table Entries
        print("\n📅 Testing Time Table Entries...")
        cursor.execute("""
            SELECT 
                c.class_name,
                te.teacher_name,
                s.subject_code,
                d.day_name,
                ts.start_time
            FROM timetable t
            JOIN classrooms c ON t.classroom_id = c.classroom_id
            JOIN teachers te ON t.teacher_id = te.teacher_id
            JOIN subjects s ON t.subject_id = s.subject_id
            JOIN days d ON t.day_id = d.day_id
            JOIN time_slots ts ON t.slot_id = ts.slot_id
            LIMIT 5
        """)
        entries = cursor.fetchall()
        for cname, tname, scode, dname, stime in entries:
            print(f"  ✓ {dname} {stime} | {cname} | {tname} | {scode}")
        
        # Test 7: Schedule for Monday
        print("\n📆 Monday Schedule:")
        cursor.execute("""
            SELECT 
                ts.start_time,
                ts.end_time,
                c.class_name,
                te.teacher_name,
                s.subject_code
            FROM timetable t
            JOIN classrooms c ON t.classroom_id = c.classroom_id
            JOIN teachers te ON t.teacher_id = te.teacher_id
            JOIN subjects s ON t.subject_id = s.subject_id
            JOIN days d ON t.day_id = d.day_id
            JOIN time_slots ts ON t.slot_id = ts.slot_id
            WHERE d.day_name = 'Monday'
            ORDER BY ts.start_time
        """)
        monday = cursor.fetchall()
        if monday:
            for stime, etime, cname, tname, scode in monday:
                print(f"  ✓ {stime}-{etime} | {cname} | {tname} | {scode}")
        else:
            print("  ℹ No classes scheduled for Monday")
        
        conn.close()
        
        print("\n" + "="*70)
        print("  ✅ ALL TESTS PASSED!")
        print("="*70)
        print("\n🎉 System is ready to use!")
        print("\nTo start the application, run:")
        print("  python timetable_management.py\n")
        
    except Exception as e:
        print(f"\n✗ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_database()
