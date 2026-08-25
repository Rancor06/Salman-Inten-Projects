# Educere - Intelligent Student Risk Performance Analytics

## Day 49 — Connected Student Risk Analysis & Analytics

> **INNOLIFT VENTURES | Crescent Internship**

Educere is a full-stack student management and intelligent risk-analysis application that combines a React frontend, Flask backend, MySQL database, and a trained machine-learning model.

Day 49 focuses on connecting the machine-learning risk prediction workflow with persistent student records so that prediction results can be associated with individual students and stored in the database.

---

## Project Overview

Educere provides a student-management workflow with integrated machine-learning analysis.

The Day 49 architecture is:

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
              Risk Analysis
                    ↓
             Stored in MySQL
                    ↓
              React Dashboard
```

The system builds on the work completed during the previous development days and connects student management with the ML prediction workflow.

---

## Day 49 Objective

The main objective of Day 49 is to connect the student's stored information with the machine-learning risk-analysis workflow.

The implementation adds persistent fields to the student database record for:

- Risk prediction
- Prediction confidence
- Class probabilities
- Prediction input data
- Risk-analysis timestamp

This allows the application to retain information about a student's ML-based analysis instead of treating the prediction as only a temporary API response.

---

## Key Features

### Student Management

- View student records
- Create student records
- Store student information in MySQL
- Retrieve student information through Flask APIs
- Maintain persistent student records

### Intelligent Risk Analysis

The system integrates a trained machine-learning model into the Flask backend.

The prediction workflow is:

```text
Student / Prediction Input
          ↓
       React UI
          ↓
   POST /api/predict
          ↓
    Flask Backend
          ↓
   ML Prediction Model
          ↓
 Prediction + Confidence
 + Class Probabilities
          ↓
     Risk Analysis
          ↓
       MySQL
```

### Persistent Risk Information

Day 49 adds the following risk-analysis information to student records:

| Database Field | Purpose |
|---|---|
| `risk_prediction` | Stores the predicted outcome |
| `risk_confidence` | Stores the model confidence |
| `risk_probabilities` | Stores the probability distribution |
| `prediction_inputs` | Stores the input values used for prediction |
| `risk_analyzed_at` | Stores when the analysis was performed |

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
| Configuration | Environment Variables / `.env` |
| Production Server | Gunicorn |
| Backend Deployment | Render |
| Version Control | Git / GitHub |
| API Testing | Postman / Browser DevTools |

---

## Machine Learning Integration

The machine-learning model predicts student outcomes using the academic, enrollment, demographic, and other model features collected by the prediction interface.

The model is exposed through the Flask backend using:

```text
POST /api/predict
```

A successful response contains:

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

The React application receives the response and displays the prediction result to the user.

---

## Day 49 Database Integration

The Day 49 database migration is:

```text
backend/migration_day49_student_risk_analysis.sql
```

The migration extends the existing `students` table with risk-analysis fields.

The resulting workflow is:

```text
Student Record
      ↓
Prediction Request
      ↓
Flask /api/predict
      ↓
Decision Tree Model
      ↓
Prediction Result
      ↓
Risk Analysis Data
      ↓
Student Database Record
```

This creates a persistent connection between the student's record and the machine-learning analysis.

---

## Database

The deployed application uses a hosted MySQL database.

The database contains the core tables required by the application, including:

```text
students
users
```

The `students` table contains the student information and Day 49 risk-analysis fields.

Database credentials are supplied through environment variables and should never be committed to GitHub.

---

## API Endpoints

### Student Management

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/students` | Retrieve student records |
| POST | `/api/students` | Create a student |

### Machine Learning

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/predict` | Generate an ML prediction |

### Health Check

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check whether the backend is running |

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
│   ├── ml/
│   │   ├── model.py
│   │   └── dropout_model.pkl
│   │
│   └── docs/
│       ├── day-47-prediction-ui.md
│       ├── day-48-backend-deployment.md
│       └── day-49-student-risk-analysis.md
│
├── frontend/
│   └── ...
│
└── README.md
```

---

## Development Progress

Educere was developed incrementally throughout the internship.

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
Connected Student Risk Analysis & Database Integration
```

---

## Day 49 Testing

The Day 49 workflow should be verified across the complete application:

### Test 1 — Student Data

```text
React
 ↓
GET /api/students
 ↓
Flask
 ↓
MySQL
 ↓
Student Data
 ↓
React
```

### Test 2 — Student Creation

```text
React Form
 ↓
POST /api/students
 ↓
Flask
 ↓
MySQL
 ↓
Student Record
```

### Test 3 — ML Prediction

```text
React Prediction Form
 ↓
POST /api/predict
 ↓
Flask
 ↓
ML Model
 ↓
Prediction
 ↓
React UI
```

### Test 4 — Risk Analysis Persistence

```text
Prediction
 ↓
Risk Analysis Data
 ↓
Student Record
 ↓
MySQL
```

The important verification is that the ML prediction workflow and student-management workflow operate as connected parts of the same application.

---

## Deployment

The Flask backend is deployed as a live service.

### Backend Platform

**Render**

### Production Server

```text
Gunicorn
```

### Start Command

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

### Dependency Installation

```bash
pip install -r requirements.txt
```

Production configuration is supplied through environment variables.

---

## Environment Variables

Sensitive configuration should be stored in environment variables.

Typical backend configuration includes:

```env
DB_HOST=...
DB_PORT=...
DB_USER=...
DB_PASSWORD=...
DB_NAME=...
FLASK_SECRET_KEY=...
```

Do not commit:

```text
.env
```

to GitHub.

Use:

```text
.env.example
```

to document the required variable names without exposing real credentials.

---

## Security

The following information must never be included in the repository or screenshots:

- Database passwords
- API keys
- Flask secret keys
- Private credentials
- Other sensitive configuration
- Unnecessary personal student information

The project uses environment variables for sensitive deployment configuration.

---

## Documentation

The project documentation includes:

```text
docs/
├── day-47-prediction-ui.md
├── day-48-backend-deployment.md
└── day-49-student-risk-analysis.md
```

### Day 47

Documents the React prediction interface and its connection to the ML prediction API.

### Day 48

Documents Flask backend deployment and live API verification.

### Day 49

Documents the connection between student records, ML risk analysis, and persistent database storage.

---

## Day 49 Expected Outcome

The final Day 49 workflow is:

```text
                    USER
                      ↓
                REACT FRONTEND
                      ↓
                FLASK BACKEND
                  ↙       ↘
              MYSQL      ML MODEL
                ↓           ↓
         Student Record  Prediction
                ↘           ↙
              Risk Analysis
                    ↓
              Persistent Data
                    ↓
                React UI
```

The application therefore combines:

**Student Management + MySQL Persistence + Machine Learning + Risk Analysis**

into one connected student-intelligence platform.

---

## Repository

GitHub:

```text
https://github.com/Rancor06/Edutrack---Student-Performance-Dropout-Risk-Predictor-Innolift-Internship-Project-
```

---

## Author

**Salman Maricar**

**INNOLIFT VENTURES | Crescent Internship**

**Day 49 — Educere - Intelligent Student Risk Performance Analytics**

---

## Conclusion

Day 49 extends Educere from a student-management application with an ML prediction API into a more integrated student risk-analysis system.

The machine-learning prediction workflow is connected with the student's persistent database record, allowing prediction results and supporting analysis information to be retained alongside student data.

The completed architecture demonstrates the integration of:

```text
React
+
Flask
+
MySQL
+
Machine Learning
+
Risk Analysis
```

as a unified full-stack student analytics application.
