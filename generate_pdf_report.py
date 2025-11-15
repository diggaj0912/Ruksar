"""
Time Table Management System - PDF Report Generator
Generates comprehensive documentation with SQL queries and database outputs
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import sqlite3
from datetime import datetime

def generate_pdf():
    """Generate comprehensive PDF documentation"""
    
    # Create PDF
    pdf_file = "TimeTable_Management_System_Documentation.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    # Container for PDF elements
    elements = []
    
    # Get styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#4285f4'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Courier',
        textColor=colors.HexColor('#2c3e50'),
        backColor=colors.HexColor('#ecf0f1'),
        spaceAfter=8,
        leftIndent=20
    )
    
    # COVER PAGE
    elements.append(Spacer(1, 1.5*inch))
    elements.append(Paragraph("TIME TABLE MANAGEMENT SYSTEM", title_style))
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph("Complete SQL Documentation", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("Queries | Database Schema | Sample Outputs", normal_style))
    elements.append(Spacer(1, 2*inch))
    
    # Date and version info
    info_data = [
        ['Generated:', datetime.now().strftime("%d-%m-%Y %H:%M:%S")],
        ['Version:', '2.0 (GUI Edition)'],
        ['Database:', 'SQLite'],
        ['Status:', 'Production Ready']
    ]
    info_table = Table(info_data, colWidths=[2*inch, 3.5*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(info_table)
    elements.append(PageBreak())
    
    # TABLE OF CONTENTS
    elements.append(Paragraph("TABLE OF CONTENTS", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    toc_items = [
        "1. System Overview",
        "2. Database Schema",
        "3. Table Structures & Field Definitions",
        "4. Sample Data",
        "5. SQL Queries & Results",
        "6. GUI Features",
        "7. Query Examples with Outputs",
    ]
    for item in toc_items:
        elements.append(Paragraph(f"• {item}", normal_style))
    elements.append(PageBreak())
    
    # SECTION 1: SYSTEM OVERVIEW
    elements.append(Paragraph("1. SYSTEM OVERVIEW", heading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    overview_text = """
    The Time Table Management System is a comprehensive solution for managing educational 
    institution schedules. It uses SQLite database to store and manage:
    <br/><br/>
    • <b>Teachers:</b> Faculty information with departments and specializations<br/>
    • <b>Classrooms:</b> Room details with capacity information<br/>
    • <b>Subjects:</b> Course information with codes and credits<br/>
    • <b>Time Slots:</b> Available class periods throughout the day<br/>
    • <b>Time Table:</b> Mapping of teachers, subjects, and classrooms to specific times
    """
    elements.append(Paragraph(overview_text, normal_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # SECTION 2: DATABASE SCHEMA
    elements.append(Paragraph("2. DATABASE SCHEMA", heading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    schema_text = "The system uses 6 main tables with relationships to maintain data integrity:"
    elements.append(Paragraph(schema_text, normal_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Schema diagram description
    schema_data = [
        ['Table', 'Purpose', 'Key Fields'],
        ['teachers', 'Store teacher information', 'teacher_id, name, department, email'],
        ['classrooms', 'Store classroom details', 'classroom_id, class_name, capacity'],
        ['subjects', 'Store subject/course info', 'subject_id, subject_code, credits'],
        ['time_slots', 'Store available time slots', 'slot_id, start_time, end_time'],
        ['days', 'Store days of week', 'day_id, day_name, day_order'],
        ['timetable', 'Main mapping table', 'classroom_id, teacher_id, subject_id, day_id, slot_id'],
    ]
    
    schema_table = Table(schema_data, colWidths=[1.3*inch, 2*inch, 2.5*inch])
    schema_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4285f4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))
    elements.append(schema_table)
    elements.append(PageBreak())
    
    # SECTION 3: TABLE STRUCTURES
    elements.append(Paragraph("3. TABLE STRUCTURES & FIELD DEFINITIONS", heading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Teachers table
    elements.append(Paragraph("3.1 Teachers Table", subheading_style))
    teachers_data = [
        ['Field', 'Type', 'Description'],
        ['teacher_id', 'INTEGER', 'Primary key, auto-increment'],
        ['teacher_name', 'TEXT', 'Name of the teacher (NOT NULL)'],
        ['department', 'TEXT', 'Department name (NOT NULL)'],
        ['specialization', 'TEXT', 'Area of expertise'],
        ['contact_number', 'TEXT', 'Phone number'],
        ['email', 'TEXT', 'Email address (UNIQUE)'],
        ['created_at', 'TIMESTAMP', 'Record creation time'],
    ]
    
    teachers_table = Table(teachers_data, colWidths=[1.5*inch, 1.2*inch, 3.2*inch])
    teachers_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))
    elements.append(teachers_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # Classrooms table
    elements.append(Paragraph("3.2 Classrooms Table", subheading_style))
    classrooms_data = [
        ['Field', 'Type', 'Description'],
        ['classroom_id', 'INTEGER', 'Primary key, auto-increment'],
        ['class_name', 'TEXT', 'Name of classroom (UNIQUE, NOT NULL)'],
        ['capacity', 'INTEGER', 'Maximum students in class'],
        ['room_number', 'TEXT', 'Room number'],
        ['building', 'TEXT', 'Building name'],
        ['created_at', 'TIMESTAMP', 'Record creation time'],
    ]
    
    classrooms_table = Table(classrooms_data, colWidths=[1.5*inch, 1.2*inch, 3.2*inch])
    classrooms_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))
    elements.append(classrooms_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # Subjects table
    elements.append(Paragraph("3.3 Subjects Table", subheading_style))
    subjects_data = [
        ['Field', 'Type', 'Description'],
        ['subject_id', 'INTEGER', 'Primary key, auto-increment'],
        ['subject_name', 'TEXT', 'Subject name (UNIQUE, NOT NULL)'],
        ['subject_code', 'TEXT', 'Subject code (UNIQUE, NOT NULL)'],
        ['credits', 'INTEGER', 'Course credits'],
        ['department', 'TEXT', 'Department offering subject'],
        ['created_at', 'TIMESTAMP', 'Record creation time'],
    ]
    
    subjects_table = Table(subjects_data, colWidths=[1.5*inch, 1.2*inch, 3.2*inch])
    subjects_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))
    elements.append(subjects_table)
    elements.append(PageBreak())
    
    # Time Slots table
    elements.append(Paragraph("3.4 Time Slots Table", subheading_style))
    slots_data = [
        ['Field', 'Type', 'Description'],
        ['slot_id', 'INTEGER', 'Primary key, auto-increment'],
        ['slot_name', 'TEXT', 'Name of slot (UNIQUE, NOT NULL)'],
        ['start_time', 'TIME', 'Class start time'],
        ['end_time', 'TIME', 'Class end time'],
        ['duration_minutes', 'INTEGER', 'Duration in minutes'],
        ['created_at', 'TIMESTAMP', 'Record creation time'],
    ]
    
    slots_table = Table(slots_data, colWidths=[1.5*inch, 1.2*inch, 3.2*inch])
    slots_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))
    elements.append(slots_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # Days table
    elements.append(Paragraph("3.5 Days Table", subheading_style))
    days_data = [
        ['Field', 'Type', 'Description'],
        ['day_id', 'INTEGER', 'Primary key, auto-increment'],
        ['day_name', 'TEXT', 'Name of day (UNIQUE, NOT NULL)'],
        ['day_order', 'INTEGER', 'Day sequence (UNIQUE)'],
        ['created_at', 'TIMESTAMP', 'Record creation time'],
    ]
    
    days_table = Table(days_data, colWidths=[1.5*inch, 1.2*inch, 3.2*inch])
    days_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))
    elements.append(days_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # TimeTable table
    elements.append(Paragraph("3.6 TimeTable (Main) Table", subheading_style))
    timetable_data = [
        ['Field', 'Type', 'Description'],
        ['timetable_id', 'INTEGER', 'Primary key, auto-increment'],
        ['classroom_id', 'INTEGER', 'FK to classrooms table'],
        ['teacher_id', 'INTEGER', 'FK to teachers table'],
        ['subject_id', 'INTEGER', 'FK to subjects table'],
        ['day_id', 'INTEGER', 'FK to days table'],
        ['slot_id', 'INTEGER', 'FK to time_slots table'],
        ['academic_year', 'TEXT', 'Year (e.g., 2024-2025)'],
        ['semester', 'INTEGER', '1 or 2'],
        ['session_type', 'TEXT', 'Lecture/Tutorial/Practical/Lab'],
        ['status', 'TEXT', 'Active or Inactive'],
        ['created_at', 'TIMESTAMP', 'Record creation time'],
        ['updated_at', 'TIMESTAMP', 'Last update time'],
    ]
    
    timetable_table = Table(timetable_data, colWidths=[1.2*inch, 1*inch, 3.7*inch])
    timetable_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))
    elements.append(timetable_table)
    elements.append(PageBreak())
    
    # SECTION 4: SAMPLE DATA
    elements.append(Paragraph("4. SAMPLE DATA", heading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    try:
        conn = sqlite3.connect('timetable.db')
        cursor = conn.cursor()
        
        # Sample Teachers
        elements.append(Paragraph("4.1 Sample Teachers", subheading_style))
        cursor.execute("SELECT teacher_id, teacher_name, department, specialization FROM teachers LIMIT 5")
        teachers_data_sample = [['ID', 'Name', 'Department', 'Specialization']]
        teachers_data_sample.extend([[str(row[0]), row[1], row[2], row[3]] for row in cursor.fetchall()])
        
        teachers_sample_table = Table(teachers_data_sample, colWidths=[0.5*inch, 1.8*inch, 1.8*inch, 1.9*inch])
        teachers_sample_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4285f4')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ]))
        elements.append(teachers_sample_table)
        elements.append(Spacer(1, 0.15*inch))
        
        # Sample Classrooms
        elements.append(Paragraph("4.2 Sample Classrooms", subheading_style))
        cursor.execute("SELECT classroom_id, class_name, capacity, room_number FROM classrooms LIMIT 5")
        classrooms_data_sample = [['ID', 'Class Name', 'Capacity', 'Room']]
        classrooms_data_sample.extend([[str(row[0]), row[1], str(row[2]), row[3]] for row in cursor.fetchall()])
        
        classrooms_sample_table = Table(classrooms_data_sample, colWidths=[0.5*inch, 1.8*inch, 1.2*inch, 1*inch])
        classrooms_sample_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4285f4')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ]))
        elements.append(classrooms_sample_table)
        elements.append(Spacer(1, 0.15*inch))
        
        # Sample Subjects
        elements.append(Paragraph("4.3 Sample Subjects", subheading_style))
        cursor.execute("SELECT subject_id, subject_code, subject_name, credits FROM subjects LIMIT 5")
        subjects_data_sample = [['ID', 'Code', 'Name', 'Credits']]
        subjects_data_sample.extend([[str(row[0]), row[1], row[2], str(row[3])] for row in cursor.fetchall()])
        
        subjects_sample_table = Table(subjects_data_sample, colWidths=[0.5*inch, 0.8*inch, 2.5*inch, 0.7*inch])
        subjects_sample_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4285f4')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ]))
        elements.append(subjects_sample_table)
        elements.append(Spacer(1, 0.15*inch))
        
        # Sample Time Slots
        elements.append(Paragraph("4.4 Sample Time Slots", subheading_style))
        cursor.execute("SELECT slot_id, slot_name, start_time, end_time FROM time_slots LIMIT 8")
        slots_data_sample = [['ID', 'Slot Name', 'Start', 'End']]
        slots_data_sample.extend([[str(row[0]), row[1], row[2], row[3]] for row in cursor.fetchall()])
        
        slots_sample_table = Table(slots_data_sample, colWidths=[0.5*inch, 1.2*inch, 1.2*inch, 1.2*inch])
        slots_sample_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4285f4')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ]))
        elements.append(slots_sample_table)
        elements.append(PageBreak())
        
        # SECTION 5: SQL QUERIES & RESULTS
        elements.append(Paragraph("5. SQL QUERIES & RESULTS", heading_style))
        elements.append(Spacer(1, 0.1*inch))
        
        # Query 1: Select all teachers
        elements.append(Paragraph("5.1 Query: Select All Teachers", subheading_style))
        query_1 = "SELECT teacher_id, teacher_name, department, email FROM teachers ORDER BY teacher_id;"
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier'>{query_1}</font>", code_style))
        elements.append(Spacer(1, 0.1*inch))
        
        elements.append(Paragraph("<b>Output:</b>", normal_style))
        cursor.execute("SELECT teacher_id, teacher_name, department, email FROM teachers ORDER BY teacher_id")
        result_data = [['Teacher ID', 'Name', 'Department', 'Email']]
        result_data.extend([[str(row[0]), row[1], row[2], row[3]] for row in cursor.fetchall()])
        
        result_table = Table(result_data, colWidths=[1*inch, 1.5*inch, 1.5*inch, 1.5*inch])
        result_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ]))
        elements.append(result_table)
        elements.append(Spacer(1, 0.2*inch))
        
        # Query 2: Get time table with joins
        elements.append(Paragraph("5.2 Query: Get Time Table with All Details", subheading_style))
        query_2 = """SELECT t.timetable_id, c.class_name, te.teacher_name, 
       s.subject_code, d.day_name, ts.slot_name, t.session_type
FROM timetable t
JOIN classrooms c ON t.classroom_id = c.classroom_id
JOIN teachers te ON t.teacher_id = te.teacher_id
JOIN subjects s ON t.subject_id = s.subject_id
JOIN days d ON t.day_id = d.day_id
JOIN time_slots ts ON t.slot_id = ts.slot_id
ORDER BY d.day_order, ts.start_time;"""
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier' size='7'>{query_2}</font>", code_style))
        elements.append(Spacer(1, 0.1*inch))
        
        elements.append(Paragraph("<b>Output (Sample):</b>", normal_style))
        cursor.execute("""SELECT t.timetable_id, c.class_name, te.teacher_name, 
       s.subject_code, d.day_name, ts.slot_name, t.session_type
FROM timetable t
JOIN classrooms c ON t.classroom_id = c.classroom_id
JOIN teachers te ON t.teacher_id = te.teacher_id
JOIN subjects s ON t.subject_id = s.subject_id
JOIN days d ON t.day_id = d.day_id
JOIN time_slots ts ON t.slot_id = ts.slot_id
ORDER BY d.day_order, ts.start_time LIMIT 8""")
        
        timetable_result = [['ID', 'Class', 'Teacher', 'Subject', 'Day', 'Slot', 'Type']]
        timetable_result.extend([[str(row[0]), row[1], row[2], row[3], row[4], row[5], row[6]] for row in cursor.fetchall()])
        
        timetable_result_table = Table(timetable_result, colWidths=[0.4*inch, 0.8*inch, 1.2*inch, 0.8*inch, 0.7*inch, 0.7*inch, 0.8*inch])
        timetable_result_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ]))
        elements.append(timetable_result_table)
        elements.append(PageBreak())
        
        # Query 3: Count entries by day
        elements.append(Paragraph("5.3 Query: Count Classes by Day", subheading_style))
        query_3 = """SELECT d.day_name, COUNT(t.timetable_id) as class_count
FROM days d
LEFT JOIN timetable t ON d.day_id = t.day_id
GROUP BY d.day_id, d.day_name
ORDER BY d.day_order;"""
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier'>{query_3}</font>", code_style))
        elements.append(Spacer(1, 0.1*inch))
        
        elements.append(Paragraph("<b>Output:</b>", normal_style))
        cursor.execute("""SELECT d.day_name, COUNT(t.timetable_id) as class_count
FROM days d
LEFT JOIN timetable t ON d.day_id = t.day_id
GROUP BY d.day_id, d.day_name
ORDER BY d.day_order""")
        
        day_result = [['Day', 'Number of Classes']]
        day_result.extend([[row[0], str(row[1])] for row in cursor.fetchall()])
        
        day_result_table = Table(day_result, colWidths=[2*inch, 1.5*inch])
        day_result_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ]))
        elements.append(day_result_table)
        elements.append(Spacer(1, 0.2*inch))
        
        # Query 4: Schedule for specific day
        elements.append(Paragraph("5.4 Query: Get Schedule for Specific Day (Monday)", subheading_style))
        query_4 = """SELECT ts.start_time, ts.end_time, c.class_name, te.teacher_name, s.subject_code
FROM timetable t
JOIN classrooms c ON t.classroom_id = c.classroom_id
JOIN teachers te ON t.teacher_id = te.teacher_id
JOIN subjects s ON t.subject_id = s.subject_id
JOIN days d ON t.day_id = d.day_id
JOIN time_slots ts ON t.slot_id = ts.slot_id
WHERE d.day_name = 'Monday'
ORDER BY ts.start_time;"""
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier' size='8'>{query_4}</font>", code_style))
        elements.append(Spacer(1, 0.1*inch))
        
        elements.append(Paragraph("<b>Output:</b>", normal_style))
        cursor.execute("""SELECT ts.start_time, ts.end_time, c.class_name, te.teacher_name, s.subject_code
FROM timetable t
JOIN classrooms c ON t.classroom_id = c.classroom_id
JOIN teachers te ON t.teacher_id = te.teacher_id
JOIN subjects s ON t.subject_id = s.subject_id
JOIN days d ON t.day_id = d.day_id
JOIN time_slots ts ON t.slot_id = ts.slot_id
WHERE d.day_name = 'Monday'
ORDER BY ts.start_time""")
        
        monday_result = [['Start', 'End', 'Class', 'Teacher', 'Subject']]
        monday_result.extend([[row[0], row[1], row[2], row[3], row[4]] for row in cursor.fetchall()])
        
        monday_result_table = Table(monday_result, colWidths=[0.8*inch, 0.8*inch, 1*inch, 1.3*inch, 1*inch])
        monday_result_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ]))
        elements.append(monday_result_table)
        elements.append(Spacer(1, 0.2*inch))
        
        # Query 5: Teacher schedule
        elements.append(Paragraph("5.5 Query: Get Schedule for Specific Teacher", subheading_style))
        query_5 = """SELECT d.day_name, ts.start_time, c.class_name, s.subject_code, t.session_type
FROM timetable t
JOIN classrooms c ON t.classroom_id = c.classroom_id
JOIN teachers te ON t.teacher_id = te.teacher_id
JOIN subjects s ON t.subject_id = s.subject_id
JOIN days d ON t.day_id = d.day_id
JOIN time_slots ts ON t.slot_id = ts.slot_id
WHERE te.teacher_name = 'Dr. John Smith'
ORDER BY d.day_order, ts.start_time;"""
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier' size='8'>{query_5}</font>", code_style))
        elements.append(Spacer(1, 0.1*inch))
        
        elements.append(Paragraph("<b>Output:</b>", normal_style))
        cursor.execute("""SELECT d.day_name, ts.start_time, c.class_name, s.subject_code, t.session_type
FROM timetable t
JOIN classrooms c ON t.classroom_id = c.classroom_id
JOIN teachers te ON t.teacher_id = te.teacher_id
JOIN subjects s ON t.subject_id = s.subject_id
JOIN days d ON t.day_id = d.day_id
JOIN time_slots ts ON t.slot_id = ts.slot_id
WHERE te.teacher_name = 'Dr. John Smith'
ORDER BY d.day_order, ts.start_time""")
        
        teacher_result = [['Day', 'Time', 'Class', 'Subject', 'Type']]
        teacher_result.extend([[row[0], row[1], row[2], row[3], row[4]] for row in cursor.fetchall()])
        
        if len(teacher_result) > 1:
            teacher_result_table = Table(teacher_result, colWidths=[1*inch, 0.8*inch, 0.9*inch, 0.9*inch, 1*inch])
            teacher_result_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
            ]))
            elements.append(teacher_result_table)
        elements.append(PageBreak())
        
        # Query 6: INSERT query example
        elements.append(Paragraph("5.6 INSERT Query Example", subheading_style))
        insert_query = """INSERT INTO timetable 
(classroom_id, teacher_id, subject_id, day_id, slot_id, 
 academic_year, semester, session_type)
VALUES (1, 1, 1, 1, 1, '2024-2025', 1, 'Lecture');"""
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier' size='8'>{insert_query}</font>", code_style))
        elements.append(Paragraph("<b>Description:</b> Inserts a new time table entry linking classroom 1, teacher 1, subject 1 for Monday morning slot.", normal_style))
        elements.append(Spacer(1, 0.15*inch))
        
        # Query 7: UPDATE query example
        elements.append(Paragraph("5.7 UPDATE Query Example", subheading_style))
        update_query = """UPDATE timetable 
SET teacher_id = 2, updated_at = CURRENT_TIMESTAMP
WHERE timetable_id = 1;"""
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier'>{update_query}</font>", code_style))
        elements.append(Paragraph("<b>Description:</b> Updates the teacher assignment for time table entry with ID 1, changing it to teacher 2.", normal_style))
        elements.append(Spacer(1, 0.15*inch))
        
        # Query 8: DELETE query example
        elements.append(Paragraph("5.8 DELETE Query Example", subheading_style))
        delete_query = """DELETE FROM timetable 
WHERE timetable_id = 1;"""
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier'>{delete_query}</font>", code_style))
        elements.append(Paragraph("<b>Description:</b> Deletes the time table entry with ID 1.", normal_style))
        elements.append(Spacer(1, 0.2*inch))
        
        # Query 9: Statistics
        elements.append(Paragraph("5.9 Query: System Statistics", subheading_style))
        query_stats = """SELECT 
    (SELECT COUNT(*) FROM teachers) as total_teachers,
    (SELECT COUNT(*) FROM classrooms) as total_classrooms,
    (SELECT COUNT(*) FROM subjects) as total_subjects,
    (SELECT COUNT(*) FROM time_slots) as total_slots,
    (SELECT COUNT(*) FROM timetable) as total_entries;"""
        elements.append(Paragraph(f"<b>SQL Query:</b><br/><font face='Courier' size='8'>{query_stats}</font>", code_style))
        elements.append(Spacer(1, 0.1*inch))
        
        elements.append(Paragraph("<b>Output:</b>", normal_style))
        cursor.execute("""SELECT 
    (SELECT COUNT(*) FROM teachers) as total_teachers,
    (SELECT COUNT(*) FROM classrooms) as total_classrooms,
    (SELECT COUNT(*) FROM subjects) as total_subjects,
    (SELECT COUNT(*) FROM time_slots) as total_slots,
    (SELECT COUNT(*) FROM timetable) as total_entries""")
        
        stats = cursor.fetchone()
        stats_data = [
            ['Total Teachers', 'Total Classrooms', 'Total Subjects', 'Total Slots', 'Total Entries'],
            [str(stats[0]), str(stats[1]), str(stats[2]), str(stats[3]), str(stats[4])]
        ]
        
        stats_table = Table(stats_data, colWidths=[1*inch, 1.2*inch, 1*inch, 0.9*inch, 1*inch])
        stats_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ]))
        elements.append(stats_table)
        elements.append(PageBreak())
        
        # SECTION 6: ADDITIONAL QUERIES
        elements.append(Paragraph("6. ADDITIONAL USEFUL QUERIES", heading_style))
        elements.append(Spacer(1, 0.1*inch))
        
        queries_list = [
            ("6.1 Get classroom schedule", """SELECT ts.start_time, te.teacher_name, s.subject_code, d.day_name
FROM timetable t
JOIN classrooms c ON t.classroom_id = c.classroom_id
JOIN teachers te ON t.teacher_id = te.teacher_id
JOIN subjects s ON t.subject_id = s.subject_id
JOIN days d ON t.day_id = d.day_id
JOIN time_slots ts ON t.slot_id = ts.slot_id
WHERE c.class_name = 'Class A1'
ORDER BY d.day_order, ts.start_time;"""),
            
            ("6.2 Find available time slots", """SELECT ts.slot_id, ts.slot_name, ts.start_time, ts.end_time
FROM time_slots ts
WHERE ts.slot_id NOT IN (
    SELECT DISTINCT slot_id FROM timetable 
    WHERE day_id = 1 AND academic_year = '2024-2025'
)
ORDER BY ts.start_time;"""),
            
            ("6.3 Count classes per teacher", """SELECT te.teacher_name, COUNT(t.timetable_id) as class_count
FROM teachers te
LEFT JOIN timetable t ON te.teacher_id = t.teacher_id
GROUP BY te.teacher_id, te.teacher_name
ORDER BY class_count DESC;"""),
            
            ("6.4 Get subjects per department", """SELECT department, COUNT(*) as subject_count
FROM subjects
GROUP BY department
ORDER BY subject_count DESC;"""),
        ]
        
        for idx, (title, query) in enumerate(queries_list, 1):
            elements.append(Paragraph(title, subheading_style))
            elements.append(Paragraph(f"<font face='Courier' size='8'>{query}</font>", code_style))
            elements.append(Spacer(1, 0.08*inch))
        
        conn.close()
        
    except Exception as e:
        elements.append(Paragraph(f"Error retrieving data: {str(e)}", normal_style))
    
    # FINAL PAGE: SUMMARY
    elements.append(PageBreak())
    elements.append(Paragraph("7. SYSTEM SUMMARY", heading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    summary_points = [
        "<b>Total Tables:</b> 6 (teachers, classrooms, subjects, time_slots, days, timetable)",
        "<b>Database Type:</b> SQLite (Relational Database)",
        "<b>Primary Keys:</b> All tables have auto-increment primary keys",
        "<b>Foreign Keys:</b> timetable table has 5 foreign key constraints",
        "<b>Indexes:</b> Created on frequently searched fields",
        "<b>Data Validation:</b> NOT NULL, UNIQUE, and DEFAULT constraints applied",
        "<b>Sample Data:</b> Pre-loaded with 5 teachers, 5 classrooms, 5 subjects, 8 time slots, 6 days",
        "<b>Query Capabilities:</b> Complex JOINs, GROUP BY, aggregation functions",
        "<b>GUI Interface:</b> Tkinter-based professional interface with login and dashboard",
        "<b>Export Functionality:</b> Data can be exported to text files for reporting",
    ]
    
    for point in summary_points:
        elements.append(Paragraph(f"• {point}", normal_style))
    
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("KEY FEATURES:", subheading_style))
    features = [
        "Referential integrity through foreign key constraints",
        "Automatic timestamp tracking (created_at, updated_at)",
        "Unique constraints to prevent duplicate data",
        "Support for complex queries with multiple JOINs",
        "Scalable design for growing data",
        "Easy to query by day, teacher, classroom, or subject",
        "Real-time schedule generation and management",
    ]
    
    for feature in features:
        elements.append(Paragraph(f"✓ {feature}", normal_style))
    
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph("Generated on: " + datetime.now().strftime("%d-%m-%Y at %H:%M:%S"), 
                              ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.grey)))
    
    # Build PDF
    doc.build(elements)
    print(f"✅ PDF generated successfully: {pdf_file}")
    return pdf_file

if __name__ == "__main__":
    generate_pdf()
