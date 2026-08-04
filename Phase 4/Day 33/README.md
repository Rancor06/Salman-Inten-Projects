# 🌐 Flask Portfolio Website

A modern, responsive personal portfolio website built with **Flask**, featuring a Home, About, Projects, and Contact page. Project cards are generated dynamically using Jinja2 rather than hardcoded in HTML. This project was built as part of a **Day 33 Internship Task** focused on intermediate Flask concepts.

## 🎯 Objectives

This project demonstrates:
- Building a multi-page Flask application with clean routing
- Using Jinja2 templates to generate dynamic HTML
- Passing data from Python into templates with `render_template()`
- Looping over Python data structures with Jinja2 to generate repeated HTML elements
- Structuring a Flask project with separated content, logic, and presentation
- Building a responsive, modern UI using only hand-written CSS

## 🛠️ Technologies Used

- **Python** – core programming language
- **Flask** – lightweight Python web framework
- **HTML** – page structure and content
- **CSS** – styling, layout, and responsiveness

## ✨ Features

- Flask routing across multiple pages
- **Dynamic project cards** generated from a Python data file using Jinja2 loops
- **Jinja2 templates** with `render_template()` for all pages
- **Responsive design** using CSS Grid and media queries
- Static CSS served from the `static/` folder
- **Multiple pages**: Home, About, Projects, Contact
- Modern portfolio UI with a navbar, hero section, skills section, project cards, contact section, and footer
- Hover animations and a consistent, professional color palette
- Font Awesome icons throughout

## 📁 Project Structure

```
Day_32/
├── app.py
├── data.py
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   └── contact.html
└── static/
    └── css/
        └── style.css
```

## ⚙️ Installation

1. **Navigate to the project directory**
   ```bash
   cd flask_portfolio
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

Then open your browser and visit:

```
http://127.0.0.1:5000
```

Navigate between the **Home**, **About**, **Projects**, and **Contact** pages using the navigation bar.

## 📸 Screenshots

| Home | 
|---|
| ![Home page](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e2f4783c55bc5200210b33a3f19eab7d90e2d59/Phase%204/Day%2033/Screenshots/Home.png) | 

| About |
|---|
| ![About page](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e2f4783c55bc5200210b33a3f19eab7d90e2d59/Phase%204/Day%2033/Screenshots/About.png) |

| Projects |
|---|
| ![Projects page](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e2f4783c55bc5200210b33a3f19eab7d90e2d59/Phase%204/Day%2033/Screenshots/Projects.png) |

| Contact |
|---|
| ![Contact page](https://github.com/Rancor06/Salman-Inten-Projects/blob/5e2f4783c55bc5200210b33a3f19eab7d90e2d59/Phase%204/Day%2033/Screenshots/Contact.png) |

## 📚 Learning Outcomes

Through this project, the following concepts were learned and applied:
- How Jinja2 generates HTML dynamically before sending it to the browser
- The difference between `{{ }}` (output) and `{% %}` (logic/control)
- Writing Jinja2 `for` loops to generate repeated HTML elements from a Python list
- Passing Python lists and dictionaries into templates via `render_template()`
- Separating content (`data.py`) from structure (templates) and logic (`app.py`)
- Building responsive layouts with CSS Grid and hover animations

## 🔮 Future Improvements

- Add a functional contact form with backend form handling
- Integrate a database (e.g., SQLite) to manage projects instead of a Python file
- Add Jinja2 template inheritance (`base.html`) to reduce repeated navbar/footer code
- Add user authentication for an admin/edit panel

## 👤 Author

- **Name: Salman Maricar**
- **GitHub: https://github.com/Rancor06**
- **College: B.S. Abdur Rahman Crescent Institute of Science and Technology**
