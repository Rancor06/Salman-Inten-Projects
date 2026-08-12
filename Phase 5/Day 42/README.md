# Day 42 — POST API & Form Submission

Innolift Ventures Crescent Internship — Module 5, Day 42

## Overview

This task sends data from React to Flask — the reverse of Day 41. A
controlled React form collects a new student's details and POSTs them to
Flask, which validates, saves, and returns the created record. The new
student appears in the list immediately, with no page refresh.

## Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Flask, Flask-CORS
- **Database:** MySQL

## What Was Built

- `POST /api/students` — Flask endpoint that validates `name`, `email`,
  and `course`, inserts a new student, and returns the created record
  (`201`) or a validation error (`400`)
- `StudentForm.jsx` — controlled form (`useState` per field), `onSubmit` +
  `event.preventDefault()`, `fetch()` POST with JSON headers/body, a
  `loading` state that disables the button and shows a spinner, and a
  success/error message
- `StudentDirectory.jsx` — updated to render the form and append newly
  created students to the existing list via `setStudents(prev => [...prev, newStudent])`
  (no re-fetch, no page reload)
- `migration_day42_add_email.sql` — adds the `email` column the
  `students` table was missing

## Project Structure

```
Backend/
  app.py                          → POST /api/students added
  migration_day42_add_email.sql   → run once before testing
Frontend/innolift/src/
  StudentForm.jsx                 → new
  StudentDirectory.jsx            → renders form + list, handles append
  StudentDirectory.css            → form + spinner styling
```

## How to Run

1. **Run the migration once** (MySQL Workbench or CLI):
   ```
   mysql -u root -p edutrack_db < migration_day42_add_email.sql
   ```

2. **Backend**
   ```
   cd Backend
   python app.py
   ```

3. **Test in Postman before React** (per task instructions):
   - `POST http://localhost:5000/api/students`
   - Header: `Content-Type: application/json`
   - Body:
     ```json
     { "name": "Test Student", "email": "test@crescent.edu", "course": "AI & DS" }
     ```
   - Expect `201` with the created student. Try omitting a field to confirm
     the `400` validation response.

4. **Frontend** (separate terminal)
   ```
   cd Frontend/innolift
   npm run dev
   ```
   Fill in the form at `http://localhost:5173` and submit.

## API

| Method | Endpoint | Body | Description |
|---|---|---|---|
| GET | `/api/students` | — | Returns all students |
| POST | `/api/students` | `{ name, email, course }` | Creates a new student |

## Data Flow

```
Form (useState per field)
  → onSubmit → preventDefault()
  → loading = true
  → fetch POST /api/students (JSON body)
  → Flask validates → inserts → returns created student
  → loading = false
  → student appended to list, form cleared, success message shown
```

## Notes

- The form doesn't collect a roll number — the backend generates one
  (`NEW-<timestamp>`) since the `students` table requires a unique value
  there but a public form shouldn't be asking for it.

## Submission Checklist

- [x] Flask POST API created
- [ ] API tested successfully in Postman
- [x] React form created with controlled inputs
- [x] `useState()` used for form values
- [x] `onSubmit` and `onChange` implemented
- [x] React connected to Flask using `fetch()`
- [x] Loading spinner implemented
- [x] Submit button disabled while loading
- [x] Success message displayed
- [x] Form fields cleared after success
- [x] New student added without page refresh
- [ ] Project pushed to GitHub
- [ ] GitHub repository/link submitted
