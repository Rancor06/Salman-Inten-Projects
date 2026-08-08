# Day 38 – Sessions & Login

Part of the 60-day ML/Full-Stack internship at Innolift Ventures — Crescent Batch.
**Track:** Level 1 – HTML, CSS, Flask + MySQL

## 📌 Tasks Completed
- Implemented `/login` — verifies credentials and starts a session
- Implemented `/logout` — clears the session
- Built a `login_required` decorator to protect routes
- Added `/profile` as a protected test route
- Tested the full flow: login → access → logout → blocked

## 🔐 How It Works

Sessions let Flask remember who's logged in across requests using a signed cookie:
- `/login` checks the submitted username/password against the hashed password in the `users` table (from Day 37). On success, it stores `user_id` and `username` in the session.
- `/logout` clears the session, forgetting who was logged in.
- `login_required` is a decorator that blocks access to a route with `401 Please log in first` unless a valid session exists.
- `/profile` is a protected route that only works while logged in — used to prove the flow works.

## 🔌 API Endpoints

| Method | Route | Description | Protected? |
|---|---|---|---|
| POST | `/login` | Log in with username + password, starts a session | No |
| POST | `/logout` | Clears the current session | No |
| GET | `/profile` | Returns the logged-in user's username | Yes (`login_required`) |

## ⚙️ Setup Instructions

1. **Set a Flask secret key** (required to sign session cookies securely)
   ```python
   app.secret_key = "change-this-to-a-real-secret-key"
   ```

2. **Install dependencies** (all already included with Flask)
   ```bash
   pip install flask mysql-connector-python werkzeug
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

## 🧪 Testing with Postman — Full Flow

| # | Method | URL | Body | Expect |
|---|---|---|---|---|
| 1 | POST | `http://127.0.0.1:5000/login` | `{"username":"salman01","password":"MySecret123"}` | `200`, "Welcome back" |
| 2 | GET | `http://127.0.0.1:5000/profile` | — | `200`, shows username |
| 3 | POST | `http://127.0.0.1:5000/logout` | — | `200`, "Logged out successfully" |
| 4 | GET | `http://127.0.0.1:5000/profile` | — | `401`, "Please log in first" |

Run all 4 in the same Postman session so the session cookie carries over automatically between requests (check the **Cookies** link below Send to confirm one was set after login).

## 📁 Project Structure
```
backend/
├── app.py         # Flask app + CRUD + auth + session routes
├── db.py          # MySQL connection helper
└── schema.sql      # Database schema + sample data
```

## ⚠️ Note
All routes, including `/login`, `/logout`, and `/profile`, must be defined **before** `app.run(debug=True)` in `app.py` — anything placed after it never registers.

## ✅ Verification
Full login → access → logout → blocked flow tested and confirmed in Postman, with the `/profile` route correctly switching from `200` to `401` after logout.
