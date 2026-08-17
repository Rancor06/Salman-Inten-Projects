# EduTrack

### Student Performance & Dropout Risk Predictor

> A full-stack student management platform built with React, Flask, and MySQL, with a machine-learning dropout-risk prediction pipeline currently under integration.

---

## 📌 Overview

**EduTrack** is a full-stack student management and academic monitoring platform developed as part of an internship project.

The system is designed to manage student information through a modern React interface, a Flask REST API, and a MySQL database. The project also includes a machine-learning pipeline for future student dropout-risk prediction.

The current application focuses on establishing a reliable full-stack foundation:

**React Frontend**  
↓  
**Flask REST API**  
↓  
**MySQL Database**

The machine-learning prediction component is currently under integration and is intentionally kept separate from the existing student management functionality.

---

## ✨ Features

### 🎓 Student Management

- View student records through a dynamic React interface
- Retrieve student information directly from MySQL through the Flask API
- Add new students through a React form
- Store newly created students in MySQL
- Automatically generate a system roll number for new students
- Prevent duplicate student email addresses using a database UNIQUE constraint
- Display newly created students without requiring a page refresh

### 🔌 REST API

- `GET /api/students`
- `POST /api/students`
- JSON-based request and response handling
- Server-side input validation
- Database error handling
- Structured JSON error responses
- Custom handling for `404`, `405`, and `500` errors

### 🧪 API Testing

The Student Management API has been independently tested using Postman for:

- Successful GET
- Successful POST
- Empty name
- Missing email
- Missing course
- Empty JSON body
- No request body
- Duplicate email
- Invalid endpoint
- Unsupported HTTP method

### 🗄️ Database Integration

- MySQL-backed student records
- Persistent student data
- Database migrations
- Seed data support
- Unique email constraint
- Verification of API-created records directly through MySQL

### 🔐 Authentication & Authorization

The Flask backend includes authentication and role-based access functionality for:

- Admin users
- Student users
- Login-required routes
- Admin-only routes
- Student-only routes

---

# 🏗️ Architecture

```text
┌──────────────────────────────┐
│       React Frontend         │
│                              │
│  Student Directory           │
│  Add Student Form            │
│  Quick Risk Check            │
└──────────────┬───────────────┘
               │
               │ HTTP / JSON
               ▼
┌──────────────────────────────┐
│        Flask REST API        │
│                              │
│  GET  /api/students          │
│  POST /api/students          │
│                              │
│  Validation                  │
│  Error Handling              │
│  Authentication              │
└──────────────┬───────────────┘
               │
               │ SQL
               ▼
┌──────────────────────────────┐
│          MySQL               │
│                              │
│       edutrack_db            │
│                              │
│       students               │
└──────────────────────────────┘
```

---

# 🖥️ Frontend

The frontend is developed using **React** and **Vite**.

## Student Directory

The Student Directory retrieves live student information through:

```text
React
  ↓
GET /api/students
  ↓
Flask
  ↓
MySQL
  ↓
JSON Response
  ↓
React Student Directory
```

The directory:

- Fetches live records from the backend
- Displays student ID
- Displays student name
- Displays email
- Displays course
- Handles loading states
- Handles API/network failures
- Handles an empty database state
- Updates when new students are added

---

## Add Student Form

The React form sends JSON to:

```http
POST /api/students
```

Example:

```json
{
  "name": "Student Name",
  "email": "student@example.com",
  "course": "Computer Science"
}
```

The form uses controlled React inputs and handles loading, validation errors, API errors, success feedback, and dynamic list updates.

---

## ⚠️ Quick Risk Check

The application currently contains a frontend-only **Quick Risk Check** preview.

It accepts:

- Attendance percentage
- Previous GPA

It displays:

- **On Track**
- **Watch**
- **At Risk**

> **Important:** The Quick Risk Check is currently a UI preview/placeholder. It is **not** the actual machine-learning dropout prediction model.

---

# ⚙️ Backend

The backend is built using **Python and Flask**.

## Student API

### GET `/api/students`

Retrieves all student records from the MySQL `students` table.

**Success:** `200 OK`

Example response:

```json
[
  {
    "id": 1,
    "name": "Student Name",
    "email": "student@example.com",
    "course": "Computer Science"
  }
]
```

### POST `/api/students`

Creates a new student record.

Example request:

```json
{
  "name": "Test Student",
  "email": "test@example.com",
  "course": "Computer Science"
}
```

**Success:** `201 Created`

The API validates required fields, inserts the student into MySQL, generates a system roll number, returns the created student, and handles database errors.

---

# 🚨 Error Handling

The API provides structured JSON responses for common errors.

| Scenario | Status |
|---|---:|
| Successful GET | `200` |
| Successful POST | `201` |
| Invalid input | `400` |
| Duplicate email | `500` |
| Invalid endpoint | `404` |
| Unsupported method | `405` |

The duplicate-email implementation currently returns HTTP 500 because the Flask code catches MySQL error `1062` from the UNIQUE constraint and converts it into a JSON error response.

---

# 🗄️ Database

EduTrack uses **MySQL** for persistent student data.

**Database:** `edutrack_db`

**Primary table:** `students`

The student table includes fields such as:

- `id`
- `name`
- `roll_no`
- `email`
- `course`
- `admission_grade`
- `attendance_percentage`
- `gpa`
- Academic performance fields
- Dropout-risk-related fields
- `notes`
- `created_at`

Database setup and migration files include:

```text
schema.sql
full_setup.sql
seed_data.sql
migration_day42_add_email.sql
migration_day44_unique_email.sql
```

---

# 🤖 Machine Learning Status

EduTrack is designed to include machine-learning-based student dropout-risk prediction.

Previous ML development includes:

- Student dropout dataset exploration
- Data preprocessing
- Train/test splitting
- Decision Tree model development
- Classification evaluation
- Confusion matrix analysis
- Feature importance analysis
- Saved trained model artifact

However, the trained ML model is **not currently connected to the Flask prediction endpoint**.

### Completed

- ML experimentation/model development
- Full-stack student management
- Flask REST API
- MySQL persistence
- React integration
- API testing

### In Progress

- Integrating the trained model into `ml_predictor.py`
- Mapping database fields to model features
- Applying training-time preprocessing during inference
- Returning real prediction probabilities/classes
- Connecting prediction results to React

---

# 🧰 Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React, React DOM, Vite, JavaScript, CSS |
| Backend | Python, Flask, Flask-CORS |
| Database | MySQL |
| Database Driver | MySQL Connector/Python |
| Configuration | python-dotenv |
| Security Utilities | Werkzeug |
| API Testing | Postman |
| Version Control | Git, GitHub |
| Machine Learning | Python / Scikit-learn |

---

# 📁 Project Structure

```text
EduTrack/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── ml_predictor.py
│   ├── requirements.txt
│   ├── schema.sql
│   ├── full_setup.sql
│   ├── seed_data.sql
│   ├── migration_day42_add_email.sql
│   ├── migration_day44_unique_email.sql
│   ├── Student Management API.postman_collection.json
│   └── docs/
│       └── day-45-api-testing.md
│
├── frontend/
│   └── innolift/
│       ├── package.json
│       ├── vite.config.js
│       └── src/
│           ├── App.jsx
│           ├── StudentDirectory.jsx
│           ├── StudentForm.jsx
│           ├── QuickRiskCheck.jsx
│           └── StudentRiskCard.jsx
│
└── README.md
```

---

# 🚀 Installation & Setup

## Prerequisites

- Python
- MySQL
- Node.js
- npm
- Git

## Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

MySQL must be running before starting the Flask application.

## Environment Variables

Create a local `.env` file in the backend directory:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=edutrack_db
```

Never commit `.env` or database credentials to GitHub.

## Database

Start MySQL, create/use `edutrack_db`, run the provided schema/setup SQL, apply the required migrations, and optionally load seed data.

## Frontend

```bash
cd frontend/innolift
npm install
npm run dev
```

The Vite development server normally runs at:

```text
http://localhost:5173
```

API requests are proxied to:

```text
http://localhost:5000
```

---

# 🔄 Application Flow

## Retrieve Students

```text
React Student Directory
        │
        ▼
GET /api/students
        │
        ▼
Flask REST API
        │
        ▼
MySQL SELECT
        │
        ▼
JSON Response
        │
        ▼
React UI
```

## Create Student

```text
React Student Form
        │
        ▼
POST /api/students
        │
        ▼
Flask Validation
        │
        ▼
MySQL INSERT
        │
        ▼
Created Student
        │
        ▼
JSON Response
        │
        ▼
React UI Update
```

---

# 🧪 API Testing with Postman

The project includes:

```text
Student Management API.postman_collection.json
```

The API was tested independently from the React frontend.

| Test | Method | Status |
|---|---|---:|
| Get Students | GET | `200` |
| Create Student | POST | `201` |
| Empty Name | POST | `400` |
| Missing Email | POST | `400` |
| Missing Course | POST | `400` |
| Empty JSON | POST | `400` |
| No Request Body | POST | `400` |
| Duplicate Email | POST | `500` |
| Invalid Endpoint | GET | `404` |
| Unsupported Method | DELETE | `405` |

Successfully created records were also verified directly in MySQL.

---

# 📈 Development Progress

### Day 41
**React ↔ Flask integration**

Established communication between the React frontend and Flask backend.

### Day 42
**GET + POST + Form Handling**

Implemented student retrieval, student creation, and frontend form handling.

### Day 43
**Error Handling**

Improved frontend/API error handling and empty-state behavior.

### Day 44
**Flask ↔ MySQL**

Connected Flask to MySQL and implemented persistent student data storage.

### Day 45
**API Testing with Postman**

Tested valid requests, invalid inputs, duplicate data, invalid endpoints, unsupported methods, HTTP status codes, and database persistence.

---

# 🔐 Security Notes

The project is currently intended for local development and internship demonstration.

Before production deployment:

- Keep database credentials outside source control
- Never commit `.env`
- Use a secure production Flask secret key
- Restrict CORS to trusted origins
- Disable Flask debug mode in production
- Strengthen authentication and authorization
- Validate and sanitize user-controlled input
- Apply secure deployment configuration

---

# 🛣️ Future Roadmap

- [ ] Integrate the trained dropout-risk model
- [ ] Connect the prediction pipeline to student records
- [ ] Apply consistent preprocessing during inference
- [ ] Return actual prediction probabilities/classes
- [ ] Display real dropout-risk predictions in React
- [ ] Add richer student analytics
- [ ] Improve production authentication/security
- [ ] Add automated backend/API tests
- [ ] Expand API functionality
- [ ] Deploy the application

---

# 📸 Screenshots

### Student Directory

_Add project screenshot here._

### Postman API Testing

_Add Postman screenshots here._

### MySQL Verification

_Add MySQL verification screenshot here._

---

# 📚 Documentation

Detailed Day 45 API testing documentation:

```text
backend/docs/day-45-api-testing.md
```

---

# 👨‍💻 Author

**Salman Maricar**

B.Tech — Artificial Intelligence & Data Science

---

## 🔗 Repository

**EduTrack — Student Performance & Dropout Risk Predictor**

https://github.com/Rancor06/Edutrack---Student-Performance-Dropout-Risk-Predictor-Innolift-Internship-Project-

---

## 📌 Project Status

**Active Development**

The student management platform, REST API, MySQL persistence, React integration, and API testing workflow are implemented.

The machine-learning dropout-risk prediction component is currently under integration.

---

<p align="center">
  Built with React • Flask • MySQL • Python
</p>
