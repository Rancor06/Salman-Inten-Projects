# Day 41 — Connecting Frontend to Backend

Innolift Ventures Crescent Internship — Module 5, Day 41

## Overview

This task connects the React frontend to the Flask backend using a REST API.
The React app fetches student data from Flask on page load and displays it —
no student data is hardcoded in the frontend.

## Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Flask, Flask-CORS
- **Database:** MySQL

## What Was Built

- `GET /api/students` — public Flask endpoint returning all students as JSON
  (id, name, email, course)
- `StudentDirectory.jsx` — React component that fetches from `/api/students`
  using `useEffect()`, stores the result with `useState()`, and renders it
  as a grid of student cards
- Vite dev-server proxy (`vite.config.js`) so `/api/*` calls from React
  reach Flask without CORS issues
- `docs/day-41-api-flow.md` — full API/data flow architecture write-up

## Project Structure

```
Backend/
  app.py            → GET /api/students route added
  db.py
Frontend/innolift/
  vite.config.js    → dev proxy: /api → localhost:5000
  src/
    App.jsx
    StudentDirectory.jsx
    StudentDirectory.css
docs/
  day-41-api-flow.md
```

## How to Run

1. **Backend**
   ```
   cd Backend
   pip install -r requirements.txt
   python app.py
   ```
   Runs on `http://localhost:5000`.

2. **Frontend** (separate terminal)
   ```
   cd Frontend/innolift
   npm run dev
   ```
   Runs on `http://localhost:5173`.

3. Open `http://localhost:5173` — the student directory loads live data
   from Flask.

## API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/students` | Returns all students as JSON |

## Data Flow

```
React (useEffect on mount)
  → fetch('/api/students')
  → Flask queries MySQL
  → JSON response
  → response.json()
  → setStudents() (useState)
  → React re-renders student cards
```

## Submission Checklist

- [x] Completed all 4 tasks
- [x] Tested the Flask API
- [x] Verified React ↔ Flask connection
- [x] Checked responsive UI
- [x] Added `docs/day-41-api-flow.md`
- [ ] Pushed the complete project to GitHub
- [ ] Submitted the GitHub repository link
