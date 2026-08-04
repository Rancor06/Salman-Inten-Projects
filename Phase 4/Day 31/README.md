# 🌐 Flask Portfolio Website

A simple, beginner-friendly personal portfolio website built with **Flask**, featuring a Home, About, and Contact page. This project was built as part of a **Day 31 Internship Task** focused on backend web development fundamentals.

## 🎯 Objectives

This project demonstrates:
- Setting up and running a basic Flask web server
- Creating multiple routes/pages within a single application
- Rendering dynamic HTML using Flask's templating engine
- Serving static assets (CSS) correctly within a Flask project
- Structuring a Flask project following standard conventions

## 🛠️ Technologies Used

- **Python** – core programming language
- **Flask** – lightweight Python web framework
- **HTML** – page structure and content
- **CSS** – styling and layout

## ✨ Features

- Flask development web server
- **Home page** introducing the portfolio
- **About page** with a short bio and skills
- **Contact page** with contact details
- HTML rendering using Flask's `render_template()` and Jinja2 templates
- CSS styling served from the `static/` folder
- Clean, organized folder structure separating templates and static assets
- Beginner-friendly, minimal codebase — easy to read and extend

## 📁 Project Structure

```
Day 31/
├── app.py
├── templates/
│   ├── index.html
│   ├── about.html
│   └── contact.html
└── static/
    └── css/
        └── style.css
```

## ⚙️ Installation

1. **Navigate to the project directory**
   ```bash
   cd "Day 31"
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

4. **Run the application**
   ```bash
   python app.py
   ```

## 🚀 Usage

Once the server is running, open your browser and visit:

```
http://127.0.0.1:5000
```

Navigate between the **Home**, **About**, and **Contact** pages using the navigation bar at the top of the site.

## 📸 Screenshots

| Home | 
|---|
| ![Home page](https://github.com/Rancor06/Salman-Inten-Projects/blob/ca6074fcb6f151ce8c57682e9dd05524e7e8ef8c/Phase%204/Day%2031/Screenshots/Home.png) | 

| About |
|---|
| ![About page](https://github.com/Rancor06/Salman-Inten-Projects/blob/ca6074fcb6f151ce8c57682e9dd05524e7e8ef8c/Phase%204/Day%2031/Screenshots/About.png) |

| Contact |
|---|
| ![Contact page](https://github.com/Rancor06/Salman-Inten-Projects/blob/ca6074fcb6f151ce8c57682e9dd05524e7e8ef8c/Phase%204/Day%2031/Screenshots/Contact.png) |

## 📚 Learning Outcomes

Through this project, the following concepts were learned and applied:
- Flask fundamentals and application setup
- Routing with `@app.route()`
- Using Jinja2 templates with `render_template()`
- Serving static files (CSS) via the `static/` folder
- Rendering HTML pages dynamically
- Linking and integrating CSS with `url_for()`

## 🔮 Future Improvements

- Add a functional contact form with backend form handling
- Integrate a database (e.g., SQLite) for dynamic content
- Improve responsiveness for mobile devices
- Add user authentication for an admin/edit panel

## 👤 Author

- **Name: Salman Maricar**
- **GitHub: https://github.com/Rancor06**
- **College: B.S. Abdur Rahman Crescent Institute of Science and Technology**
