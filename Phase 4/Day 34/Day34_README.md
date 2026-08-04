# 📡 Flask REST API - Projects

A beginner-friendly REST API built with **Flask**, managing project data entirely in memory (no database). Supports full CRUD operations through standard HTTP methods, with a logging middleware that records every request and response. This project was built as part of a **Day 34 Internship Task** focused on REST APIs and middleware.

## 🎯 Objectives

This project demonstrates:
- Designing a REST API around a single resource ("projects")
- Implementing full CRUD (Create, Read, Update, Delete) operations
- Returning JSON responses instead of HTML
- Using correct HTTP status codes (200, 201, 400, 404)
- Building request/response logging middleware using Flask's `before_request` and `after_request` hooks
- Structuring a Flask project professionally, separating data, logic, and presentation

## 🛠️ Technologies Used

- **Python** – core programming language
- **Flask** – lightweight Python web framework
- **REST API** – architectural style for the endpoints
- **JSON** – data format for all API requests and responses

## ✨ Features

- **GET API** – retrieve all projects or a single project by id
- **POST API** – create a new project
- **PUT API** – update an existing project
- **DELETE API** – remove a project
- **Logging Middleware** – logs every incoming request and outgoing response with a timestamp
- **JSON Responses** – all endpoints return structured JSON, not HTML
- **In-memory Project Storage** – data lives in a Python list, no database required
- Input validation with proper `400`/`404` error responses
- Simple HTML docs page listing all available endpoints

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/projects` | Get all projects |
| GET | `/projects/<id>` | Get a single project by id |
| POST | `/projects` | Create a new project |
| PUT | `/projects/<id>` | Update an existing project |
| DELETE | `/projects/<id>` | Delete a project |

## 📁 Project Structure

```
Day 34/
├── app.py
├── data.py
├── templates/
│   └── index.html
└── static/
    └── css/
        └── style.css
```

## ⚙️ Installation

1. **Navigate to the project directory**
   ```bash
   cd "Day 34"
   ```

2. **Create a virtual environment** *(optional but recommended)*
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install Flask**
   ```bash
   pip install flask
   ```

## ▶️ Running the Project

Start the Flask development server:
```bash
python app.py
```

The API will be available at:
```
http://127.0.0.1:5000
```

Visit the base URL in your browser for a docs page listing all endpoints, or query `/projects` directly to see JSON output.

## 🧪 Testing with Postman

1. Open Postman and create a new request.
2. Set the request URL to `http://127.0.0.1:5000/projects` (add `/<id>` for a specific project).
3. Select the appropriate method: `GET`, `POST`, `PUT`, or `DELETE`.
4. For `POST` and `PUT`, go to the **Body** tab → select **raw** → choose **JSON**, then enter a body such as:
   ```json
   {
     "title": "New Project",
     "description": "Testing POST",
     "tech": "Flask"
   }
   ```
5. Click **Send** and check the response body and status code.

## 📸 Screenshots

| API Docs Homepage |
|---|
| ![API docs homepage](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e833272fa72efbeb1cd73af0b3d70102ef83ce0/Phase%204/Day%2034/Screenshots/API%20Docs%20Homepage.png) |

| GET all projects |
|---|
| ![GET all projects](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e833272fa72efbeb1cd73af0b3d70102ef83ce0/Phase%204/Day%2034/Screenshots/GET%20all%20projects.png) |

| GET one project |
|---|
| ![GET one project](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e833272fa72efbeb1cd73af0b3d70102ef83ce0/Phase%204/Day%2034/Screenshots/GET%20one%20project.png) |

| POST — create a project |
|---|
| ![POST create project](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e833272fa72efbeb1cd73af0b3d70102ef83ce0/Phase%204/Day%2034/Screenshots/POST%20%E2%80%94%20create%20a%20project.png) |

| PUT — update a project |
|---|
| ![PUT update project](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e833272fa72efbeb1cd73af0b3d70102ef83ce0/Phase%204/Day%2034/Screenshots/PUT%20%E2%80%94%20update%20a%20project.png) |

| DELETE — remove a project |
|---|
| ![DELETE remove project](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e833272fa72efbeb1cd73af0b3d70102ef83ce0/Phase%204/Day%2034/Screenshots/DELETE%20%E2%80%94%20remove%20a%20project.png) |

## 📚 Learning Outcomes

Through this project, the following concepts were learned and applied:
- The difference between a website (HTML) and an API (JSON)
- Mapping CRUD operations to HTTP methods (GET, POST, PUT, DELETE)
- Using status codes correctly to communicate success and failure (200, 201, 400, 404)
- Reading and validating JSON request bodies with `request.get_json()`
- Building middleware-like behavior in Flask using `before_request` and `after_request`
- Structuring an API project by separating data (`data.py`) from route logic (`app.py`)

## 🔮 Future Improvements

- Replace in-memory storage with a real database (e.g., SQLite or MongoDB)
- Add authentication/API keys to protect write operations
- Add pagination and filtering for the GET /projects endpoint
- Write automated tests for each endpoint

## 👤 Author

- **Name: Salman Maricar**
- **GitHub: https://github.com/Rancor06**
- **College: B.S. Abdur Rahman Crescent Institute of Science and Technology**
