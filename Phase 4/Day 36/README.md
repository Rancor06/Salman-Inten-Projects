# Day 36 – CRUD with a Database

Part of the 60-day ML/Full-Stack internship at Innolift Ventures — Crescent Batch.
**Track:** Level 1 – HTML, CSS, Flask + MySQL

## 📌 Tasks Completed
- Built full CRUD (Create, Read, Update, Delete) endpoints for the `projects` table
- Connected all endpoints to the existing `portfolio_db` MySQL database
- Tested every endpoint in Postman with request/response screenshots

## 🗄️ Database

Reused the existing `projects` table from Day 35 (no new tables needed):

| Column | Type | Description |
|---|---|---|
| id | INT (PK, AUTO_INCREMENT) | Unique project ID |
| title | VARCHAR(150) | Project name |
| description | TEXT | Project summary |
| tech_stack | VARCHAR(200) | Technologies used |

## 🔌 API Endpoints

| Method | Route | Description |
|---|---|---|
| POST | `/projects` | Create a new project |
| GET | `/api/projects` | Get all projects |
| GET | `/projects/<id>` | Get a single project by id |
| PUT | `/projects/<id>` | Update a project by id |
| DELETE | `/projects/<id>` | Delete a project by id |

## ⚙️ Setup Instructions

1. **Create the database and table** (if not already set up from Day 35)
   ```bash
   mysql -u root -p < schema.sql
   ```

2. **Install dependencies**
   ```bash
   pip install flask mysql-connector-python
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

## 🧪 Testing with Postman

| # | Method | URL | Body |
|---|---|---|---|
| 1 | POST | `http://127.0.0.1:5000/projects` | `{"title":"Test Project","description":"Testing CRUD","tech_stack":"Flask, MySQL"}` |
| 2 | GET | `http://127.0.0.1:5000/projects/<id>` | — |
| 3 | PUT | `http://127.0.0.1:5000/projects/<id>` | `{"title":"Test Project Updated","description":"Edited via PUT","tech_stack":"Flask, MySQL"}` |
| 4 | GET | `http://127.0.0.1:5000/projects/<id>` | — |
| 5 | DELETE | `http://127.0.0.1:5000/projects/<id>` | — |
| 6 | GET | `http://127.0.0.1:5000/projects/<id>` | — (expect 404, confirms deletion) |

For POST/PUT requests: set **Body → raw → JSON**, which auto-adds the `Content-Type: application/json` header.

## 📁 Project Structure
```
backend/
├── app.py         # Flask app + all CRUD routes
├── db.py          # MySQL connection helper
└── schema.sql      # Database schema + sample data
```

## ✅ Verification
All 4 CRUD operations (POST, GET, PUT, DELETE) tested end-to-end in Postman and confirmed working against `portfolio_db`.
