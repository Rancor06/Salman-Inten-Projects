// Import the Express library we installed via npm
const express = require('express');

// Node's built-in 'path' module — helps build safe file paths
// that work on any operating system (Windows, Mac, Linux)
const path = require('path');

// Create an Express application instance
const app = express();

// Define which port the server will listen on
const PORT = 3000;

// Tell Express to serve any file inside 'public' automatically,
// without needing a route for each one. This is how style.css
// becomes reachable at /css/style.css in the browser.
app.use(express.static(path.join(__dirname, 'public')));


// ROUTES

// Home page — sends an actual HTML file from the 'views' folder
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

// About page
app.get('/about', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'about.html'));
});

// Contact page
app.get('/contact', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'contact.html'));
});

// Extra route demonstrating a plain TEXT response (not a file).
// Visiting /status shows Express can send raw text, not just HTML.
app.get('/status', (req, res) => {
    res.send('Server is running fine.');
});


// Start the server and listen for requests on PORT
app.listen(PORT, () => {
    console.log(`Server running at http://127.0.0.1:${PORT}`);
});
