# Day 37 – Authentication Basics

Part of the 60-day ML/Full-Stack internship at Innolift Ventures — Crescent Batch.
**Track:** Level 1 – HTML, CSS, Flask + MySQL

## 📌 Tasks Completed
- Created a `users` table for storing registered accounts
- Built a `/register` endpoint that hashes passwords before storing them
- Registered 3 test users and confirmed passwords are stored as hashes, never plain text

## 🗄️ Database

### `users`
| Column | Type | Description |
|---|---|---|
| id | INT (PK, AUTO_INCREMENT) | Unique user ID |
| username | VARCHAR(50) UNIQUE | Login username |
| password_hash | VARCHAR(255) | Hashed password (never plain text) |

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
```

## 🔌 API Endpoints

| Method | Route | Description |
|---|---|---|
| POST | `/register` | Register a new user with a hashed password |

## ⚙️ Setup Instructions

1. **Create the `users` table** (run in MySQL shell or add to schema.sql)
   ```sql
   USE portfolio_db;
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) UNIQUE NOT NULL,
       password_hash VARCHAR(255) NOT NULL
   );
   ```

2. **Install dependencies** (werkzeug ships with Flask, but confirm it's present)
   ```bash
   pip install flask mysql-connector-python werkzeug
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

## 🧪 Testing with Postman

| Method | URL | Body |
|---|---|---|
| POST | `http://127.0.0.1:5000/register` | `{"username":"salman01","password":"MySecret123"}` |
| POST | `http://127.0.0.1:5000/register` | `{"username":"testuser02","password":"AnotherPass456"}` |
| POST | `http://127.0.0.1:5000/register` | `{"username":"demo_user03","password":"HashMe789"}` |

Each should return `201` with `"User registered successfully"`. Re-registering an existing username returns `400 Username already exists`, confirming the `UNIQUE` constraint works.

**Verify hashing:**
```sql
SELECT * FROM users;
```
`password_hash` should show a long string like `pbkdf2:sha256:...` — never the original password.

## 📁 Project Structure
```
backend/
├── app.py         # Flask app + all CRUD + auth routes
├── db.py          # MySQL connection helper
└── schema.sql      # Database schema + sample data
```

## ⚠️ Note
All routes (including `/register`) must be defined **before** `app.run(debug=True)` in `app.py` — anything placed after it never registers, since Flask starts listening at that line.

## ✅ Verification
Registered 3 test users via Postman, all returning `201`. Confirmed via `SELECT * FROM users;` that all 3 passwords are stored as hashes, not plain text.
