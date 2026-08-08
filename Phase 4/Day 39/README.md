# Day 39 – Individual Backend Project: Kickoff (EduTrack)

Part of the 60-day ML/Full-Stack internship at Innolift Ventures — Crescent Batch.
**Track:** Level 1 – HTML, CSS, Flask + MySQL
**Project:** EduTrack — student dropout risk tracking system

## 📌 Tasks Completed
- Planned all API routes for the individual backend project (`routes_plan.md`)
- Designed the database schema for students + role-based logins (`schema.sql`)
- Built and verified a running Flask skeleton with a working `/` health-check route

## 🧠 Project Overview

EduTrack has two user roles:
- **Admin (me):** adds/manages students, views attendance/GPA/dropout risk, triggers ML predictions
- **Student:** logs in to a personal dashboard to view their own attendance and performance — dropout risk is admin-only, not shown to students

## 🗄️ Database Schema

### `students`
| Column | Type | Description |
|---|---|---|
| id | INT (PK, AUTO_INCREMENT) | Unique student ID |
| name | VARCHAR(100) | Student name |
| roll_no | VARCHAR(20) UNIQUE | Roll number |
| attendance_percentage | DECIMAL(5,2) | Attendance % |
| gpa | DECIMAL(3,2) | GPA |
| dropout_risk | VARCHAR(20) | ML-predicted risk level (admin-only) |
| created_at | TIMESTAMP | Auto-set on insert |

### `users`
| Column | Type | Description |
|---|---|---|
| id | INT (PK, AUTO_INCREMENT) | Unique login ID |
| username | VARCHAR(50) UNIQUE | Login username |
| password_hash | VARCHAR(255) | Hashed password |
| role | ENUM('admin','student') | Account role |
| student_id | INT (FK → students.id) | NULL for admin; links to their record for students |

## 🔌 Planned API Routes

See `routes_plan.md` for the full table, response shapes, and auth notes. Summary:
- `/login`, `/logout`, `/profile` — shared, role-based auth (Day 38 pattern extended)
- `/admin/students` (GET/POST/PUT/DELETE) — admin-only student management
- `/admin/students/<id>/predict` — admin-only, runs the trained `.pkl` dropout-risk model
- `/student/dashboard` — student-only, returns their own record only

## ⚙️ Setup Instructions

1. **Create the database**
   ```bash
   mysql -u root -p < schema.sql
   ```

2. **Install dependencies**
   ```bash
   pip install flask mysql-connector-python werkzeug
   ```

3. **Run the skeleton app**
   ```bash
   python app.py
   ```

4. **Verify**
   Visit `http://127.0.0.1:5000/` — should return `{"status": "EduTrack API is running"}`

## 📁 Project Structure
```
edutrack-backend/
├── app.py           # Flask skeleton (routes to be built Day 40+)
├── db.py            # MySQL connection helper
├── schema.sql        # Database schema
└── routes_plan.md    # Full routes plan with auth + response shapes
```

## ✅ Verification
`/` route confirmed working, returning the API status JSON. Routes plan and schema submitted as the planning deliverable for Day 40's build.
