# Day 27 – React JS: Components, JSX & Props

**Innolift Ventures – Crescent College Internship**
Full Stack Web Development Internship – Day 27 Task Assignment

## Overview

This project demonstrates core React fundamentals — JSX syntax, reusable components, and passing data between components using props — through a Student Profile application built with React + Vite.

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

### Task 01 – React Project Setup
Initialized a new React project using Vite (`npm create vite@latest innolift -- --template react`), installed dependencies, and verified the dev server runs successfully.

### Task 02 – Student Profile using JSX
Built a static Student Profile page directly in `App.jsx` using JSX, displaying name, department, college, email, and a skills list.

### Task 03 – Reusable Components
Refactored the single-file profile into three independent components:
- `Header.jsx` – page title
- `StudentProfileCard.jsx` – profile details
- `Footer.jsx` – footer text

All three are imported and composed inside `App.jsx`.

### Task 04 – Multiple Profiles using Props
Modified `StudentProfileCard` to accept `props` (`name`, `department`, `college`, `email`) instead of hardcoded data, then rendered it three times in `App.jsx` with different student data — demonstrating how one component can be reused with different inputs.

## Project Structure

```
src/
├── App.jsx
├── Header.jsx
├── StudentProfileCard.jsx
├── Footer.jsx
└── assets/
```

## Concepts Covered

- JSX syntax and embedding JS expressions with `{}`
- Functional components
- Props (parent → child data flow, read-only)
- Component reusability