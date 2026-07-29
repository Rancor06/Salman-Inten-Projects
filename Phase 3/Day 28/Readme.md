# Day 28 – React Hooks & useState

**Innolift Ventures – Crescent College Internship**
Full Stack Web Development Internship – Day 28 Task Assignment

## Overview

This project demonstrates React's `useState` Hook through two small interactive components — a live-updating name greeting and a light/dark theme toggle — covering controlled components, boolean state, event handling, and conditional/dynamic styling.

## Tech Stack

- React
- Vite (build tool / dev server)
- JavaScript (JSX)

## Setup

```bash
npm install
npm run dev
```

Dev server runs at `http://localhost:5173/`.

## Tasks Completed

### Task 01 – Name Preview using useState
Built an input field whose value is tracked with `useState` and updated live via the `onChange` event. As the user types, the input is a **controlled component** — its displayed value comes directly from state, not the browser's default input handling. A conditional (ternary) render shows "Hello, `<name>`!" while the field has text, and "Hello, Guest!" when it's empty.

### Task 02 – Theme Toggle using useState
Built a button backed by a boolean state value (`isDark`). Clicking it flips the boolean with `setIsDark(!isDark)`, which drives an inline style object to switch the page's background and text color between light and dark, and updates the button's own label between "Light Mode" and "Dark Mode" — demonstrating boolean state, conditional rendering, and dynamic styling.

## Project Structure

```
src/
├── App.jsx
├── NamePreview.jsx
├── ThemeToggle.jsx
└── assets/
```

## Concepts Covered

- `useState` Hook — reading and updating component state
- Controlled components (`value` + `onChange`)
- Boolean state and toggling with `!state`
- Conditional rendering with ternaries
- Dynamic inline styling based on state
- Correct event handler syntax (`onClick={() => ...}` vs calling the function directly)