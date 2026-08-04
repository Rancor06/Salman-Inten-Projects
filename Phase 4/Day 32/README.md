# 🌐 Node.js Express Portfolio Website

A beginner-friendly backend project built with **Node.js** and **Express.js**, featuring a Home, About, and Contact page. This project was built as part of a **Day 32 Internship Task** focused on backend web development with Express.

## 🎯 Objectives

This project demonstrates:
- Setting up and running a basic Express web server
- Creating multiple GET routes within a single application
- Serving HTML files as responses
- Sending plain text responses
- Serving static assets (CSS) correctly using Express's static middleware
- Structuring a Node.js project following standard conventions

## 🛠️ Technologies Used

- **Node.js** – JavaScript runtime for the backend
- **Express.js** – minimal web framework for Node.js
- **HTML** – page structure and content
- **CSS** – styling and layout

## ✨ Features

- Express server listening on a defined port
- **Home page** introducing the project
- **About page** describing the project
- **Contact page** with contact details
- Multiple **GET routes** mapped to different pages
- **Text response** route (`/status`) using `res.send()`
- **HTML rendering** using `res.sendFile()`
- **CSS rendering** served from the `public/` folder via `express.static()`
- Clean, organized folder structure separating views and static assets
- Beginner-friendly, minimal codebase — easy to read and extend

## 📁 Project Structure

```
Day 32/
├── server.js
├── package.json
├── public/
│   └── css/
│       └── style.css
└── views/
    ├── index.html
    ├── about.html
    └── contact.html
```

## ⚙️ Installation

1. **Navigate to the project directory**
   ```bash
   cd "Day 32"
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

## ▶️ Running the Server

Start the Express server with:
```bash
npm start
```

Or run it directly with Node:
```bash
node server.js
```

You should see a confirmation message in the terminal once the server starts.

## 🚀 Usage

Once the server is running, open your browser and visit:

```
http://127.0.0.1:3000
```

Navigate between the **Home**, **About**, and **Contact** pages using the navigation bar. Visit `http://127.0.0.1:3000/status` to see a plain text response.

## 📸 Screenshots

| Home | 
|---|
| ![Home page](PASTE_LINK_HERE) | 
| About |
|---|
| ![About page](PASTE_LINK_HERE) |
| Contact |
|---|
| ![Contact page](PASTE_LINK_HERE) |

## 📚 Learning Outcomes

Through this project, the following concepts were learned and applied:
- Node.js and Express fundamentals
- Setting up and configuring an Express server
- Defining GET routes with `app.get()`
- Sending HTML files with `res.sendFile()`
- Sending plain text responses with `res.send()`
- Serving static files (CSS) using `express.static()`
- Understanding `package.json` and dependency management with npm

## 🔮 Future Improvements

- Add a functional contact form with backend form handling
- Integrate a database (e.g., MongoDB or MySQL) for dynamic content
- Use a templating engine (e.g., EJS) for dynamic HTML rendering
- Add user authentication for an admin/edit panel

## 👤 Author

- **Name: Salman Maricar**
- **GitHub: https://github.com/Rancor06**
- **College: B.S. Abdur Rahman Crescent Institute of Science and Technology**
