#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Database Initializer for STEM Simple Machines Lab (เครื่องกลอย่างง่าย ม.1)
Creates SQLite database with students, quiz scores, mission progress, and summary tables.
"""

import sqlite3
import os
import json

DB_PATH = "stem_students.db"

def init_database():
    if os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} already exists. Verifying tables...")
    else:
        print(f"Creating new database at {DB_PATH}...")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Students Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_code TEXT UNIQUE NOT NULL,
        prefix TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        classroom TEXT NOT NULL,
        roll_number INTEGER NOT NULL,
        gender TEXT NOT NULL,
        avatar TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # 2. Quiz Scores Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quiz_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        room_id TEXT NOT NULL,
        room_title TEXT NOT NULL,
        score INTEGER NOT NULL,
        max_score INTEGER NOT NULL,
        percentage REAL NOT NULL,
        passed INTEGER NOT NULL,
        answers_json TEXT,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
    );
    ''')

    # 3. Mission Progress Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mission_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        room_id TEXT NOT NULL,
        mission_key TEXT NOT NULL,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(student_id, room_id, mission_key),
        FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
    );
    ''')

    # 4. Student Summary Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_summary (
        student_id INTEGER PRIMARY KEY,
        total_stars INTEGER DEFAULT 0,
        total_quiz_score INTEGER DEFAULT 0,
        completed_missions_count INTEGER DEFAULT 0,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
    );
    ''')

    # Insert default mock students if table is empty
    cursor.execute("SELECT COUNT(*) FROM students;")
    count = cursor.fetchone()[0]
    
    if count == 0:
        print("Populating initial student directory for Grade 7 (ม.1/1 และ ม.1/2)...")
        students_data = [
            # ม.1/1
            ("670101", "ด.ช.", "กิตติศักดิ์", "วงศ์สุวรรณ", "ม.1/1", 1, "ชาย", "👦"),
            ("670102", "ด.ช.", "ธนกร", "เจริญผล", "ม.1/1", 2, "ชาย", "🧑"),
            ("670103", "ด.ช.", "ปัณณธร", "ศรีสุข", "ม.1/1", 3, "ชาย", "👦"),
            ("670104", "ด.ช.", "ภูริชญ์", "มั่นคง", "ม.1/1", 4, "ชาย", "🧒"),
            ("670105", "ด.ช.", "วรเมธ", "รัตนพงศ์", "ม.1/1", 5, "ชาย", "🧑"),
            ("670106", "ด.ญ.", "กัญญารัตน์", "ชัยชนะ", "ม.1/1", 6, "หญิง", "👧"),
            ("670107", "ด.ญ.", "ชนัญชิดา", "แสงทอง", "ม.1/1", 7, "หญิง", "👩"),
            ("670108", "ด.ญ.", "ฐิติมา", "พัฒนกิจ", "ม.1/1", 8, "หญิง", "👧"),
            ("670109", "ด.ญ.", "นภัสสร", "สุริยา", "ม.1/1", 9, "หญิง", "👧"),
            ("670110", "ด.ญ.", "พิมพิกา", "อัครเดช", "ม.1/1", 10, "หญิง", "👩"),
            ("670111", "ด.ช.", "ศุภวิชญ์", "ตั้งตระกูล", "ม.1/1", 11, "ชาย", "👦"),
            ("670112", "ด.ญ.", "อัญชิสา", "วิเศษสมบัติ", "ม.1/1", 12, "หญิง", "👧"),

            # ม.1/2
            ("670201", "ด.ช.", "ชนะภัย", "เกียรติสกุล", "ม.1/2", 1, "ชาย", "👦"),
            ("670202", "ด.ช.", "ณภัทร", "บุญญาธิการ", "ม.1/2", 2, "ชาย", "🧑"),
            ("670203", "ด.ช.", "เตชินท์", "อริยวงศ์", "ม.1/2", 3, "ชาย", "🧒"),
            ("670204", "ด.ช.", "ปุณณพัฒน์", "โชติช่วง", "ม.1/2", 4, "ชาย", "👦"),
            ("670205", "ด.ญ.", "จิรภิญญา", "พงษ์ไพศาล", "ม.1/2", 5, "หญิง", "👧"),
            ("670206", "ด.ญ.", "ธันยพร", "เทพรักษา", "ม.1/2", 6, "หญิง", "👩"),
            ("670207", "ด.ญ.", "นิชาภา", "อภิสิทธิ์", "ม.1/2", 7, "หญิง", "👧"),
            ("670208", "ด.ญ.", "ปรียาภรณ์", "ดำรงศิลป์", "ม.1/2", 8, "หญิง", "👧"),
            ("670209", "ด.ญ.", "รินรดา", "เกียรติคุณ", "ม.1/2", 9, "หญิง", "👩"),
            ("670210", "ด.ญ.", "อมลวรรณ", "สิทธิเสรี", "ม.1/2", 10, "หญิง", "👧"),
            ("670211", "ด.ช.", "อิทธิพัฒน์", "เมธากุล", "ม.1/2", 11, "ชาย", "🧑"),
            ("670212", "ด.ญ.", "วรินทร", "ชูโชค", "ม.1/2", 12, "หญิง", "👧")
        ]

        cursor.executemany('''
        INSERT INTO students (student_code, prefix, first_name, last_name, classroom, roll_number, gender, avatar)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        ''', students_data)

        # Initialize student_summary rows
        cursor.execute('''
        INSERT INTO student_summary (student_id, total_stars, total_quiz_score, completed_missions_count)
        SELECT id, 0, 0, 0 FROM students;
        ''')

        # Insert a sample completed record for student 1 to demonstrate reporting
        sample_answers = json.dumps({"lq1": "b", "lq2": "a", "lq3": "a", "lq4": "a"})
        cursor.execute('''
        INSERT INTO quiz_scores (student_id, room_id, room_title, score, max_score, percentage, passed, answers_json)
        VALUES (1, 'lever', 'คาน (Lever)', 4, 4, 100.0, 1, ?);
        ''', (sample_answers,))

        cursor.execute('''
        INSERT INTO mission_progress (student_id, room_id, mission_key)
        VALUES (1, 'lever', 'm1'), (1, 'lever', 'm2'), (1, 'lever', 'm3');
        ''')

        # Update student 1 summary (3 missions + 1 quiz star = 4 stars, 4 quiz points)
        cursor.execute('''
        UPDATE student_summary 
        SET total_stars = 4, total_quiz_score = 4, completed_missions_count = 3 
        WHERE student_id = 1;
        ''')

        conn.commit()
        print(f"Successfully inserted {len(students_data)} students with initial schema.")
    else:
        print(f"Database contains {count} students.")

    conn.close()

if __name__ == "__main__":
    init_database()
