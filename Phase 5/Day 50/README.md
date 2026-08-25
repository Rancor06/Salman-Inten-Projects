# Educere - Intelligent Student Risk Performance Analytics

## Day 50 — Final Testing & Submission

> **INNOLIFT VENTURES | Crescent Internship**

Educere is a full-stack student management and intelligent risk-analysis application built using React, Flask, MySQL, and a trained machine-learning model.

Day 50 represents the final testing, cleanup, documentation, and submission stage of the project.

---

## Project Overview

Educere combines student management with machine-learning-based student outcome prediction.

The complete application architecture is:

```text
                    User
                      ↓
              React Frontend
                      ↓
               Flask REST API
                 ↙        ↘
              MySQL       ML Model
                ↓            ↓
          Student Data   Prediction
                ↘            ↙
              API Response
                    ↓
              React UI Result
```

The project was developed incrementally across the internship and reaches its final testing stage on Day 50.

---

## Day 50 Objective

The goal of Day 50 is to verify the complete application as one connected system.

The final workflow must demonstrate:

- React frontend operation.
- Flask backend operation.
- MySQL database integration.
- Machine-learning prediction.
- Frontend-to-backend communication.
- Student record creation and persistence.
- Error handling.
- Final project cleanup.
- Documentation.
- GitHub submission.

---

## Main Features

### Student Management

- View student records.
- Create student records.
- Retrieve records from MySQL through Flask.
- Persist student data.
- Display database-backed records in React.

### Machine Learning Risk Prediction

The application provides a prediction interface connected to the Flask backend.

```text
User Input
 ↓
React Risk Predictor
 ↓
POST /api/predict
 ↓
Flask
 ↓
Decision Tree Model
 ↓
Prediction
 ↓
Confidence + Probabilities
 ↓
React UI
```

### Risk Analysis Persistence

Student records support risk-analysis information including:

```text
risk_prediction
risk_confidence
risk_probabilities
prediction_inputs
risk_analyzed_at
```

This allows ML analysis information to be associated with student records.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Backend | Python / Flask |
| Database | MySQL |
| Machine Learning | scikit-learn |
| ML Algorithm | Decision Tree Classifier |
| API | Flask REST API |
| Database Driver | MySQL Connector/Python |
| Production Server | Gunicorn |
| Backend Hosting | Render |
| Version Control | Git / GitHub |
| API Testing | Postman / Browser DevTools |

---

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/students` | Retrieve student records |
| POST | `/api/students` | Create a student |
| POST | `/api/predict` | Generate an ML prediction |
| GET | `/` | Backend health check |

---

## Example Prediction Response

The prediction endpoint returns structured JSON:

```json
{
  "success": true,
  "prediction": "Dropout",
  "confidence": 1.0,
  "probabilities": {
    "Dropout": 1.0,
    "Enrolled": 0.0,
    "Graduate": 0.0
  }
}
```

The React frontend displays the returned prediction and confidence information.

---

## Day 50 Testing

The final testing process covers six core areas:

### 1. React Application

The deployed frontend is opened and tested for:

- Successful loading.
- Correct UI rendering.
- Console errors.
- Failed API requests.

### 2. GET Students

The application requests student records:

```text
React
 ↓
GET /api/students
 ↓
Flask
 ↓
MySQL
 ↓
JSON
 ↓
React
```

### 3. Create Student

A new student is created through the UI:

```text
React Form
 ↓
POST /api/students
 ↓
Flask
 ↓
MySQL
 ↓
Response
 ↓
React
```

### 4. ML Prediction

The deployed ML workflow is tested:

```text
React
 ↓
POST /api/predict
 ↓
Flask
 ↓
Decision Tree
 ↓
Prediction
 ↓
React
```

### 5. Invalid Input

Invalid or incomplete input is tested to ensure the application displays an appropriate error instead of crashing.

### 6. Database Verification

A student created through the frontend is verified directly in MySQL to confirm persistence.

---

## Testing Evidence

Recommended final evidence includes:

1. React dashboard successfully loaded.
2. Browser Console showing no application errors.
3. Student list populated through the API.
4. Successful student creation.
5. `POST /api/students` request and response.
6. Successful ML prediction.
7. `POST /api/predict` request and response.
8. Invalid input validation/error message.
9. MySQL query showing the created student record.
10. Final GitHub repository and commit.

Sensitive credentials must not appear in screenshots.

---

## Database

The application uses a hosted MySQL database.

The production database contains the core:

```text
students
users
```

tables.

Day 49 risk-analysis fields are included in the student workflow.

Database configuration is supplied through environment variables.

---

## Deployment

The Flask backend is deployed using Render and runs through Gunicorn.

Production start command:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

Dependencies are installed using:

```bash
pip install -r requirements.txt
```

The frontend communicates with the deployed backend rather than depending on a local Flask server.

---

## Environment Variables

Production configuration should be stored securely in environment variables.

Typical variables include:

```env
DB_HOST=...
DB_PORT=...
DB_USER=...
DB_PASSWORD=...
DB_NAME=...
FLASK_SECRET_KEY=...
```

Never commit:

```text
.env
```

Use `.env.example` to document variable names without exposing real credentials.

---

## Project Structure

```text
Educere/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── .env.example
│   ├── schema.sql
│   ├── migration_day49_student_risk_analysis.sql
│   │
│   └── ml/
│       ├── model.py
│       └── dropout_model.pkl
│
├── frontend/
│   └── ...
│
├── docs/
│   ├── day-47-prediction-ui.md
│   ├── day-48-backend-deployment.md
│   └── day-50-final-testing.md
│
└── README.md
```

---

## Development Progress

```text
Day 41
React ↔ Flask

Day 42
GET + POST + Form Handling

Day 44
Flask ↔ MySQL

Day 45
API Testing with Postman

Day 46
Flask ↔ ML Model ↔ Prediction API

Day 47
React ↔ ML Prediction API ↔ UI

Day 48
Flask Backend Deployment

Day 49
Student Risk Analysis & Database Integration

Day 50
Final Testing & Submission
```

---

## Final Verification

Before submission:

```bash
git status
```

Review the files.

Then:

```bash
git add .
```

Review again:

```bash
git status
```

Commit:

```bash
git commit -m "Complete final project integration and testing"
```

Push:

```bash
git push origin main
```

After pushing, verify the GitHub repository manually.

---

## Security

Never commit or expose:

- Database passwords.
- API keys.
- Flask secret keys.
- `.env` files.
- Private credentials.
- Unnecessary personal student information.

Production configuration should remain in environment variables.

---

## Documentation

The project documentation includes:

```text
docs/
├── day-47-prediction-ui.md
├── day-48-backend-deployment.md
└── day-50-final-testing.md
```

The Day 50 report documents the final testing, database verification, ML testing, error testing, project cleanup, and GitHub submission process.

---

## Final Result

Educere reaches the final internship stage as a connected full-stack application:

```text
User
 ↓
React
 ↓
Flask
 ↓
MySQL / ML Model
 ↓
Response
 ↓
React
 ↓
User
```

The final submission demonstrates that the application can be tested, verified, documented, committed, and submitted as a complete system.

---

## Author

**Salman Maricar**

**INNOLIFT VENTURES | Crescent Internship**

**Day 50 — Educere - Intelligent Student Risk Performance Analytics**
