# Day 41 — API / Data Flow Architecture

## Purpose of `/api/students`

`GET /api/students` is a public REST endpoint on the Flask backend that returns
the current list of students from the `edutrack_db.students` table as JSON.
It is the single source of truth for student data on the frontend — the React
UI never hardcodes student records; it only ever renders what this endpoint
returns.

## What is an HTTP Request?

An HTTP request is a message sent by a client (here, the React app running in
the browser) to a server (Flask), asking it to do something. It has a method
(GET, POST, etc.), a URL, headers, and optionally a body. `GET /api/students`
is a request asking the server to return the student list — it carries no
body since it isn't sending data, only asking for it.

## What is a JSON Response?

JSON (JavaScript Object Notation) is a lightweight, text-based format for
structured data — objects as `{ key: value }` pairs, lists as `[ ... ]`.
Flask's `jsonify()` converts the Python list of dictionaries into a JSON
array, which the browser can parse natively. Example:

```json
[
  { "id": 1, "name": "Kavya Rao", "email": "stu-20261001@crescent.edu", "course": "Management (evening)" },
  { "id": 2, "name": "Diya Verma", "email": "stu-20261002@crescent.edu", "course": "Social Service" }
]
```

## How data travels from Flask → React

1. **React mounts** — `StudentDirectory`'s `useEffect(() => {...}, [])` runs
   once, right after the component's first render.
2. **Request sent** — `fetch('/api/students')` sends an HTTP GET request.
   In development, Vite's proxy (configured in `vite.config.js`) forwards
   any `/api/*` request from `localhost:5173` to Flask at `localhost:5000`,
   so the browser never has to deal with a cross-origin request directly.
3. **Flask handles it** — the `/api/students` route queries the `students`
   table via `mysql-connector-python`, builds a list of dictionaries, and
   returns it with `jsonify()`.
4. **Response received** — `fetch()`'s promise resolves with a `Response`
   object; `.json()` parses the response body's JSON text into a real
   JavaScript array.
5. **State updates** — `setStudents(data)` (from `useState`) stores that
   array in component state.
6. **Re-render** — because state changed, React re-renders `StudentDirectory`,
   which maps over `students` and displays one card per student.

## Architecture Diagram

```
┌─────────────────────┐        GET /api/students         ┌──────────────────────┐
│   React (Vite)       │ ───────────────────────────────▶ │   Flask (port 5000)  │
│   localhost:5173      │      (proxied via vite.config)   │                        │
│                        │                                  │  /api/students route  │
│  useEffect() on mount  │                                  │  queries MySQL via     │
│  → fetch('/api/students')│                                │  db.get_connection()   │
└─────────────────────┘                                    └──────────┬───────────┘
          ▲                                                            │
          │              JSON array of student objects                 │
          │        [{id, name, email, course}, ...]                    ▼
          │                                                   ┌──────────────────┐
          │                                                   │  MySQL            │
          │                                                   │  edutrack_db      │
          │                                                   │  students table   │
          │                                                   └──────────────────┘
          │
   response.json() parses JSON
          │
          ▼
   setStudents(data)  ── useState
          │
          ▼
   React re-renders → student cards shown in UI
```

## Focus recap

- **REST API** — resource-based endpoint (`/api/students`) accessed with a
  standard HTTP method (GET).
- **HTTP Request** — the GET call from `fetch()`.
- **JSON Response** — the array of student objects Flask returns.
- **Frontend ↔ Backend Flow** — `useEffect` triggers `fetch`, `.json()`
  parses the response, `useState` stores it, React renders it.
