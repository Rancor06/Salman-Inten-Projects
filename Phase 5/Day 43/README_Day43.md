# Day 43 — API Response & Frontend-Backend Practice

Innolift Ventures Crescent Internship — Module 5, Day 43

## Overview

This task doesn't add new features — it hardens the existing Day 41/42
project so the UI honestly reflects what actually happened during a
request: success, failure, or success-with-no-data. No new project was
created; all changes were made directly to the existing `StudentDirectory`
and `StudentForm` components.

## Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Flask, Flask-CORS
- **Database:** MySQL

## What Was Built

- **Explicit error handling on GET** — `StudentDirectory.jsx` now wraps
  its fetch in `try/catch` and checks `response.ok` separately, since a
  `4xx`/`5xx` response does not cause `fetch()` to throw on its own.
  Shows `"Unable to load students."` on any failure, with `loading`
  guaranteed to resolve via `finally`.
- **Empty state** — if the API returns a successful but empty array,
  the UI shows `"No students found."` instead of a blank card grid.
  "Success" and "has data" are treated as two separate conditions.
- **Explicit error handling on POST** — `StudentForm.jsx` uses the same
  `try/catch` pattern, and defensively parses the response body so a
  malformed/empty response (e.g. from a dev proxy when Flask is down)
  can't leak a raw `JSON.parse` error into the UI.

## Project Structure

```
Frontend/innolift/src/
  StudentDirectory.jsx   → try/catch + response.ok + empty state
  StudentForm.jsx         → try/catch + defensive body parsing
```

## How to Run

1. **Backend**
   ```
   cd Backend
   python app.py
   ```

2. **Frontend** (separate terminal)
   ```
   cd Frontend/innolift
   npm run dev
   ```

3. Open `http://localhost:5173`.

## How to Test Each Case

| Case | How to trigger it | Expected result |
|---|---|---|
| GET network failure | Stop Flask, reload the page | `"Unable to load students."` |
| Empty state | Temporarily change the GET route to `return jsonify([])`, restart Flask | `"No students found."` |
| POST failure | Stop Flask, submit the form | `"Unable to add student."` |
| Full flow | Load app → view students → submit form → see success + instant list update | Works end to end, no page refresh |

## Data Flow (Failure Path)

```
fetch() called
  → try block
  → network fails (Flask down) → catch → "Unable to load students."
      OR
  → response received, response.ok is false → thrown manually → catch
  → finally → loading = false (always runs, success or failure)
```

## Submission Checklist

- [x] Error handling completed
- [x] Empty state completed
- [x] Full GET → POST → UI flow tested
- [x] At least one error case tested
- [ ] Project pushed to GitHub
- [ ] GitHub repository link submitted
