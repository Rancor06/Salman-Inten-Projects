# Day 35 – MySQL Integration

Part of the 60-day ML/Full-Stack internship at Innolift Ventures — Crescent Batch.

## 📌 Tasks Completed
- Installed MySQL Community Server
- Created a database (`portfolio_db`) for the portfolio website
- Created tables for the website's data
- Inserted sample data into the tables
- Connected the database to the Flask backend

## 🗄️ Database Schema

### `projects`
| Column | Type | Description |
|---|---|---|
| id | INT (PK, AUTO_INCREMENT) | Unique project ID |
| title | VARCHAR(150) | Project name |
| description | TEXT | Project summary |
| tech_stack | VARCHAR(200) | Technologies used |

### `skills`
| Column | Type | Description |
|---|---|---|
| id | INT (PK, AUTO_INCREMENT) | Unique skill ID |
| name | VARCHAR(50) | Skill name |
| category | VARCHAR(50) | Skill category |
| proficiency | INT (1–100) | Self-rated proficiency |

## ⚙️ Setup Instructions

1. **Create the database and tables**
   ```bash
   mysql -u root -p < schema.sql
   ```

2. **Create a dedicated MySQL user** (optional but recommended)
   ```sql
   CREATE USER 'portfolio_user'@'localhost' IDENTIFIED BY 'yourpassword';
   GRANT ALL PRIVILEGES ON portfolio_db.* TO 'portfolio_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

3. **Install the Python MySQL connector**
   ```bash
   pip install mysql-connector-python
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Test the connection**
   Visit `http://127.0.0.1:5000/api/projects` — should return all projects as JSON.

## 📁 Project Structure
```
backend/
├── app.py         # Flask app + API routes
├── db.py          # MySQL connection helper
└── schema.sql      # Database schema + sample data
```

## 🔌 API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/projects` | Returns all projects as JSON |

## ✅ Verification
Confirmed working — `GET /api/projects` returns a `200` response with all 4 project records from `portfolio_db`.
