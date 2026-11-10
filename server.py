#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Backend HTTP Server & REST API for STEM Simple Machines Lab (สื่อการสอนเครื่องกลอย่างง่าย ม.1)
Pure Python Standard Library (http.server + sqlite3) - Zero external dependencies needed!
"""

import http.server
import socketserver
import sqlite3
import json
import urllib.parse
import os
import sys

PORT = 8000
DB_PATH = "stem_students.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def recalculate_student_summary(cursor, student_id):
    # Count unique completed missions
    cursor.execute("""
        SELECT COUNT(DISTINCT room_id || '_' || mission_key) 
        FROM mission_progress 
        WHERE student_id = ?;
    """, (student_id,))
    missions_count = cursor.fetchone()[0]

    # Count unique passed quizzes (score == max_score or best quiz score per room)
    cursor.execute("""
        SELECT room_id, MAX(score) as best_score, MAX(max_score) as max_s
        FROM quiz_scores 
        WHERE student_id = ?
        GROUP BY room_id;
    """, (student_id,))
    quiz_rows = cursor.fetchall()

    total_quiz_score = sum(r['best_score'] for r in quiz_rows)
    quiz_stars = sum(1 for r in quiz_rows if r['best_score'] == r['max_s'])

    total_stars = missions_count + quiz_stars

    cursor.execute("""
        INSERT INTO student_summary (student_id, total_stars, total_quiz_score, completed_missions_count, updated_at)
        VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(student_id) DO UPDATE SET
            total_stars = excluded.total_stars,
            total_quiz_score = excluded.total_quiz_score,
            completed_missions_count = excluded.completed_missions_count,
            updated_at = CURRENT_TIMESTAMP;
    """, (student_id, total_stars, total_quiz_score, missions_count))

class STEMLabRequestHandler(http.server.SimpleHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

        # API Routes
        if path == '/api/health':
            try:
                conn = get_db()
                c = conn.cursor()
                c.execute("SELECT COUNT(*) FROM students;")
                s_count = c.fetchone()[0]
                c.execute("SELECT COUNT(*) FROM quiz_scores;")
                q_count = c.fetchone()[0]
                conn.close()
                self.send_json({
                    "status": "ok",
                    "database": DB_PATH,
                    "student_count": s_count,
                    "quiz_count": q_count
                })
            except Exception as e:
                self.send_json({"status": "error", "message": str(e)}, 500)
            return

        if path == '/api/students':
            try:
                conn = get_db()
                c = conn.cursor()
                classroom = query.get('classroom', [None])[0]
                search = query.get('search', [None])[0]

                sql = """
                SELECT s.id, s.student_code, s.prefix, s.first_name, s.last_name, 
                       s.classroom, s.roll_number, s.gender, s.avatar,
                       COALESCE(sm.total_stars, 0) as total_stars,
                       COALESCE(sm.total_quiz_score, 0) as total_quiz_score,
                       COALESCE(sm.completed_missions_count, 0) as completed_missions_count
                FROM students s
                LEFT JOIN student_summary sm ON s.id = sm.student_id
                WHERE 1=1
                """
                params = []
                if classroom:
                    sql += " AND s.classroom = ?"
                    params.append(classroom)
                if search:
                    sql += " AND (s.first_name LIKE ? OR s.last_name LIKE ? OR s.student_code LIKE ?)"
                    term = f"%{search}%"
                    params.extend([term, term, term])

                sql += " ORDER BY s.classroom ASC, s.roll_number ASC;"
                c.execute(sql, params)
                rows = c.fetchall()
                students = []
                for r in rows:
                    students.append({
                        "id": r["id"],
                        "student_code": r["student_code"],
                        "prefix": r["prefix"],
                        "first_name": r["first_name"],
                        "last_name": r["last_name"],
                        "full_name": f"{r['prefix']}{r['first_name']} {r['last_name']}",
                        "classroom": r["classroom"],
                        "roll_number": r["roll_number"],
                        "gender": r["gender"],
                        "avatar": r["avatar"],
                        "total_stars": r["total_stars"],
                        "total_quiz_score": r["total_quiz_score"],
                        "completed_missions_count": r["completed_missions_count"]
                    })
                conn.close()
                self.send_json(students)
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
            return

        if path.startswith('/api/students/'):
            try:
                student_id = int(path.split('/')[-1])
                conn = get_db()
                c = conn.cursor()
                c.execute("SELECT * FROM students WHERE id = ?;", (student_id,))
                student = c.fetchone()
                if not student:
                    conn.close()
                    self.send_json({"error": "Student not found"}, 404)
                    return

                # Fetch missions
                c.execute("SELECT room_id, mission_key FROM mission_progress WHERE student_id = ?;", (student_id,))
                missions = c.fetchall()

                # Fetch quiz scores
                c.execute("""
                    SELECT room_id, room_title, score, max_score, percentage, passed, completed_at
                    FROM quiz_scores 
                    WHERE student_id = ? 
                    ORDER BY completed_at DESC;
                """, (student_id,))
                quizzes = c.fetchall()

                # Build stars structure
                stars_structure = {
                    "lever": {"m1": False, "m2": False, "m3": False, "quiz": False},
                    "pulley": {"m1": False, "m2": False, "m3": False, "quiz": False},
                    "incline": {"m1": False, "m2": False, "m3": False, "quiz": False},
                    "gears": {"m1": False, "m2": False, "m3": False, "quiz": False},
                    "arm": {"m1": False, "m2": False, "m3": False, "quiz": False}
                }

                for m in missions:
                    r_id = m["room_id"]
                    m_key = m["mission_key"]
                    if r_id in stars_structure:
                        stars_structure[r_id][m_key] = True

                for q in quizzes:
                    r_id = q["room_id"]
                    if r_id in stars_structure and q["score"] == q["max_score"]:
                        stars_structure[r_id]["quiz"] = True

                c.execute("SELECT * FROM student_summary WHERE student_id = ?;", (student_id,))
                summary = c.fetchone()

                conn.close()
                self.send_json({
                    "student": {
                        "id": student["id"],
                        "student_code": student["student_code"],
                        "prefix": student["prefix"],
                        "first_name": student["first_name"],
                        "last_name": student["last_name"],
                        "full_name": f"{student['prefix']}{student['first_name']} {student['last_name']}",
                        "classroom": student["classroom"],
                        "roll_number": student["roll_number"],
                        "gender": student["gender"],
                        "avatar": student["avatar"]
                    },
                    "stars": stars_structure,
                    "total_stars": summary["total_stars"] if summary else 0,
                    "total_quiz_score": summary["total_quiz_score"] if summary else 0,
                    "completed_missions_count": summary["completed_missions_count"] if summary else 0,
                    "quiz_history": [dict(q) for q in quizzes]
                })
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
            return

        if path == '/api/leaderboard':
            try:
                conn = get_db()
                c = conn.cursor()
                classroom = query.get('classroom', [None])[0]
                sql = """
                SELECT s.id, s.student_code, s.prefix, s.first_name, s.last_name, 
                       s.classroom, s.roll_number, s.avatar,
                       COALESCE(sm.total_stars, 0) as total_stars,
                       COALESCE(sm.total_quiz_score, 0) as total_quiz_score,
                       COALESCE(sm.completed_missions_count, 0) as completed_missions_count
                FROM students s
                LEFT JOIN student_summary sm ON s.id = sm.student_id
                WHERE 1=1
                """
                params = []
                if classroom:
                    sql += " AND s.classroom = ?"
                    params.append(classroom)
                sql += " ORDER BY total_stars DESC, total_quiz_score DESC, s.roll_number ASC;"
                c.execute(sql, params)
                rows = c.fetchall()
                conn.close()
                self.send_json([dict(r) for r in rows])
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
            return

        if path == '/api/export-csv':
            try:
                conn = get_db()
                c = conn.cursor()
                c.execute("""
                SELECT s.id, s.student_code, s.prefix, s.first_name, s.last_name, 
                       s.classroom, s.roll_number,
                       COALESCE(sm.total_stars, 0) as total_stars,
                       COALESCE(sm.total_quiz_score, 0) as total_quiz_score,
                       COALESCE(sm.completed_missions_count, 0) as completed_missions_count
                FROM students s
                LEFT JOIN student_summary sm ON s.id = sm.student_id
                ORDER BY s.classroom ASC, s.roll_number ASC;
                """)
                students = c.fetchall()

                # Query quiz scores per room for each student
                csv_lines = [
                    "ลำดับ,ห้อง,เลขที่,รหัสนักเรียน,ชื่อ-สกุล,ควิซคาน (4),ควิซรอก (4),ควิซทางลาด (4),ควิซเฟือง (4),ควิซแขนกล (4),คะแนนควิซรวม (20),ดาวภารกิจ (15),ดาวสะสมรวม (20),ระดับผลการเรียน"
                ]

                rooms = ['lever', 'pulley', 'incline', 'gears', 'arm']

                for idx, s in enumerate(students, 1):
                    s_id = s['id']
                    # Best score for each room
                    room_scores = {}
                    for rm in rooms:
                        c.execute("SELECT MAX(score) FROM quiz_scores WHERE student_id = ? AND room_id = ?;", (s_id, rm))
                        res = c.fetchone()[0]
                        room_scores[rm] = res if res is not None else 0

                    full_name = f"{s['prefix']}{s['first_name']} {s['last_name']}"
                    total_q = sum(room_scores.values())
                    total_stars = s['total_stars']
                    
                    # Grade tier
                    if total_stars >= 18:
                        grade = "ยอดเยี่ยมมาก (ดีเลิศ)"
                    elif total_stars >= 12:
                        grade = "ดีมาก"
                    elif total_stars >= 8:
                        grade = "ผ่านเกณฑ์"
                    else:
                        grade = "กำลังพัฒนา"

                    line = f"{idx},{s['classroom']},{s['roll_number']},{s['student_code']},\"{full_name}\"," \
                           f"{room_scores['lever']},{room_scores['pulley']},{room_scores['incline']},{room_scores['gears']},{room_scores['arm']}," \
                           f"{total_q},{s['completed_missions_count']},{total_stars},\"{grade}\""
                    csv_lines.append(line)

                conn.close()
                csv_data = "\ufeff" + "\n".join(csv_lines) # UTF-8 BOM for Thai Excel
                body = csv_data.encode('utf-8')

                self.send_response(200)
                self.send_header('Content-Type', 'text/csv; charset=utf-8')
                self.send_header('Content-Disposition', 'attachment; filename="stem_student_scores.csv"')
                self.send_header('Content-Length', str(len(body)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(body)
                return
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
                return

        # Default static file serving
        return super().do_GET()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        data = {}
        if post_data:
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}

        if path == '/api/students':
            try:
                conn = get_db()
                c = conn.cursor()
                code = data.get('student_code', '').strip()
                prefix = data.get('prefix', 'ด.ช.').strip()
                first = data.get('first_name', '').strip()
                last = data.get('last_name', '').strip()
                classroom = data.get('classroom', 'ม.1/1').strip()
                roll = int(data.get('roll_number', 1))
                gender = data.get('gender', 'ชาย')
                avatar = data.get('avatar', '👦' if gender == 'ชาย' else '👧')

                if not code or not first or not last:
                    self.send_json({"error": "กรุณากรอกรหัส ชื่อ และนามสกุล ให้ครบถ้วน"}, 400)
                    conn.close()
                    return

                c.execute("""
                INSERT INTO students (student_code, prefix, first_name, last_name, classroom, roll_number, gender, avatar)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                """, (code, prefix, first, last, classroom, roll, gender, avatar))
                new_id = c.lastrowid

                c.execute("""
                INSERT INTO student_summary (student_id, total_stars, total_quiz_score, completed_missions_count)
                VALUES (?, 0, 0, 0);
                """, (new_id,))

                conn.commit()
                conn.close()
                self.send_json({
                    "id": new_id,
                    "student_code": code,
                    "prefix": prefix,
                    "first_name": first,
                    "last_name": last,
                    "full_name": f"{prefix}{first} {last}",
                    "classroom": classroom,
                    "roll_number": roll,
                    "gender": gender,
                    "avatar": avatar,
                    "total_stars": 0,
                    "total_quiz_score": 0,
                    "completed_missions_count": 0
                }, 201)
            except sqlite3.IntegrityError:
                self.send_json({"error": "รหัสนักเรียนนี้มีอยู่ในระบบแล้ว"}, 409)
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
            return

        if path == '/api/scores':
            try:
                conn = get_db()
                c = conn.cursor()
                student_id = int(data.get('student_id'))
                room_id = data.get('room_id')
                room_title = data.get('room_title', room_id)
                score = int(data.get('score', 0))
                max_score = int(data.get('max_score', 4))
                answers = json.dumps(data.get('answers', {}), ensure_ascii=False)
                percentage = round((score / max_score) * 100, 1)
                passed = 1 if score == max_score else 0

                c.execute("""
                INSERT INTO quiz_scores (student_id, room_id, room_title, score, max_score, percentage, passed, answers_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                """, (student_id, room_id, room_title, score, max_score, percentage, passed, answers))

                # Recalculate summary
                recalculate_student_summary(c, student_id)
                conn.commit()

                # Get updated summary
                c.execute("SELECT * FROM student_summary WHERE student_id = ?;", (student_id,))
                summary = c.fetchone()
                conn.close()

                self.send_json({
                    "success": True,
                    "student_id": student_id,
                    "room_id": room_id,
                    "score": score,
                    "max_score": max_score,
                    "percentage": percentage,
                    "passed": bool(passed),
                    "total_stars": summary["total_stars"] if summary else 0,
                    "total_quiz_score": summary["total_quiz_score"] if summary else 0
                })
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
            return

        if path == '/api/missions':
            try:
                conn = get_db()
                c = conn.cursor()
                student_id = int(data.get('student_id'))
                room_id = data.get('room_id')
                mission_key = data.get('mission_key')

                c.execute("""
                INSERT OR IGNORE INTO mission_progress (student_id, room_id, mission_key)
                VALUES (?, ?, ?);
                """, (student_id, room_id, mission_key))

                # Recalculate summary
                recalculate_student_summary(c, student_id)
                conn.commit()

                c.execute("SELECT * FROM student_summary WHERE student_id = ?;", (student_id,))
                summary = c.fetchone()
                conn.close()

                self.send_json({
                    "success": True,
                    "student_id": student_id,
                    "room_id": room_id,
                    "mission_key": mission_key,
                    "total_stars": summary["total_stars"] if summary else 0
                })
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
            return

        if path == '/api/reset-student':
            try:
                conn = get_db()
                c = conn.cursor()
                student_id = int(data.get('student_id'))
                c.execute("DELETE FROM quiz_scores WHERE student_id = ?;", (student_id,))
                c.execute("DELETE FROM mission_progress WHERE student_id = ?;", (student_id,))
                c.execute("""
                UPDATE student_summary 
                SET total_stars = 0, total_quiz_score = 0, completed_missions_count = 0, updated_at = CURRENT_TIMESTAMP
                WHERE student_id = ?;
                """, (student_id,))
                conn.commit()
                conn.close()
                self.send_json({"success": True, "student_id": student_id})
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
            return

        self.send_json({"error": "Route not found"}, 404)

def run_server(port=PORT):
    # Ensure database exists
    if not os.path.exists(DB_PATH):
        import init_db
        init_db.init_database()

    handler = STEMLabRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🚀 STEM Simple Machines Server running at http://localhost:{port}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"💾 Connected to database: {DB_PATH}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run_server(port)
