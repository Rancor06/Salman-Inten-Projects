# EduTrack — Individual Project Routes Plan

| Method | Route | What it does | Auth |
|---|---|---|---|
| POST | `/login` | Log in as admin or student (role-based session) | No |
| POST | `/logout` | Clear the session | No |
| GET | `/profile` | Return the logged-in user's own info + role | Login required |
| POST | `/admin/students` | Add a new student (creates student record + login account) | Admin only |
| GET | `/admin/students` | List all students | Admin only |
| GET | `/admin/students/<id>` | Get one student's full record, including dropout risk | Admin only |
| PUT | `/admin/students/<id>` | Update a student's attendance/performance data | Admin only |
| DELETE | `/admin/students/<id>` | Remove a student | Admin only |
| POST | `/admin/students/<id>/predict` | Run the dropout-risk model on this student, save + return the result | Admin only |
| GET | `/student/dashboard` | Logged-in student sees their own attendance + performance (no risk score) | Student only, own data |

## Notes

**Authentication:**
- `/admin/...` routes require an `admin_required` decorator (extends `login_required` with a `session["role"] == "admin"` check).
- `/student/dashboard` requires `login_required` plus a check that `session["role"] == "student"`, and only ever returns the student record linked to that session — never another student's data.

**ML model usage:**
- Only `/admin/students/<id>/predict` touches the trained `.pkl` dropout-risk model.
- No student-facing route calls the model or exposes the risk score — dropout risk is admin-only info per project scope.

**Response JSON shapes:**

`GET /student/dashboard`
```json
{ "name": "...", "attendance_percentage": 92.5, "gpa": 8.4, "subjects": [...] }
```

`GET /admin/students/<id>`
```json
{ "id": 1, "name": "...", "attendance_percentage": 92.5, "gpa": 8.4, "dropout_risk": "Low" }
```
