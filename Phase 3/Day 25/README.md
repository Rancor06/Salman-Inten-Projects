# EduTrack — Student Performance & Dropout Risk Predictor
### Frontend Track — Progress Report (Day 25)

**Intern:** Salman Maricar
**Phase / Day:** Phase 3 – Day 25
**Date:** 25th of July, 2026

> Part of the [EduTrack](#project-roadmap) capstone build (Innolift Ventures 60-day internship). This covers Module 3 — the frontend phase.

---

## Objectives

To design and build the teacher-facing frontend for EduTrack — a dashboard that lets instructors view student risk scores, review individual academic profiles, and monitor cohort-level trends — as the frontend phase (Module 3) of the larger 60-day EduTrack capstone. The goal was a fully navigable, responsive multi-page interface ready to be connected to a real backend and the dropout-risk ML model in later modules.

## Technologies Used

- **HTML5** — semantic structure across 6 pages
- **CSS3** — custom properties (design tokens), Flexbox, CSS Grid, media queries, pseudo-classes/elements, CSS-only animated toggle switches
- **Vanilla JavaScript (ES6)** — DOM manipulation, event listeners, array methods, dynamically generated SVG charts — no frameworks yet, since React is introduced later in the curriculum (Days 29–30)
- **Google Fonts** — Space Grotesk, IBM Plex Sans, IBM Plex Mono

## Modules / Pages Completed

| # | Page | Description |
|---|---|---|
| 1 | `login.html` | Teacher sign-in screen |
| 2 | `dashboard.html` | Cohort overview, stat strip, "needs attention" alerts |
| 3 | `students.html` | Searchable student register |
| 4 | `student-detail.html` | Individual academic record and risk-driver breakdown |
| 5 | `reports.html` | Risk distribution, cohort risk drivers, per-course breakdown |
| 6 | `settings.html` | Profile, notification preferences, risk thresholds |

## Features Implemented

- RAG (Red/Amber/Green) risk-status system used consistently across every page
- Live search filter on the student register (no page reload)
- Fully responsive layout with a working mobile hamburger navigation menu
- Animated risk-driver bars and a hand-built SVG trend chart (no chart library)
- CSS-only animated toggle switches for notification settings & live-updating threshold sliders
- Real data integration — 10 stratified sample records pulled directly from the UCI *"Predict Students' Dropout and Academic Success"* dataset (the same dataset the prediction model was trained on), replacing earlier placeholder/mock data

## UI Screenshots

| Login | Dashboard |
|---|---|
| ![Login page](Phase 3/Day 25/Screenshots/login.png) | ![Dashboard page](https://github.com/Rancor06/Salman-Inten-Projects/blob/150d8cde013ae1cdc1b686acf94b11b698ec16a5/Phase%203/Day%2025/Screenshots/dashboard.png) |

| Student Register | Student Detail |
|---|---|
| ![Students page](Phase 3/Day 25/Screenshots/students.png) | ![Student detail page](Phase 3/Day 25/Screenshots/student-detail.png) |

| Reports | Settings |
|---|---|
| ![Reports page](Phase 3/Day 25/Screenshots/reports.png) | ![Settings page](Phase 3/Day 25/Screenshots/settings.png) |

## Challenges Faced

- The project's curriculum hadn't reached React yet, so the frontend had to be built as a clean multi-page HTML/CSS/JS app rather than components — meaning navigation, state (like the active nav link), and page transitions all had to be handled manually.
- An early version of the dashboard combined the cohort overview and the full student list into one page, which made "Dashboard" and "Students" in the sidebar point to the same content — poor navigation design.
- The real UCI dataset has no student names, no attendance percentage, and no weekly/time-series data — only anonymized, single-snapshot academic features.
- Mobile responsiveness initially just hid the sidebar navigation entirely below a certain screen width, with no way to access it.

## Solutions Implemented

- Split the single dashboard into two dedicated pages — a cohort overview and a separate student register — giving each sidebar link a real, distinct destination.
- Built a working hamburger-menu toggle using JavaScript's `classList.toggle()` paired with CSS, restoring full navigation access on mobile.
- Rather than fabricating data the dataset doesn't contain, relabeled and derived fields honestly — e.g. "1st sem. completion" (units approved ÷ enrolled) in place of a nonexistent attendance figure — and clearly marked the Reports trend chart as illustrative since the dataset is a single-semester snapshot, not weekly data.
- Caught and corrected an earlier inconsistency where dashboard statistics claimed more students than were actually present in the register.

## Current Progress Status

All 6 planned frontend pages are complete, fully linked, and responsive. The interface is now backed by real (though sample-sized) data from the actual dataset the ML model uses, rather than fully synthetic placeholders. The frontend phase (Module 3) is functionally complete ahead of schedule relative to the 60-day roadmap.

## Pending Tasks

- [ ] Backend development — Flask REST API + MySQL database (Module 4)
- [ ] Connecting real authentication (login currently accepts any input)
- [ ] Persisting Settings changes, teacher notes, and risk thresholds (currently frontend-only, nothing saves)
- [ ] Migrating the UI to React components per the curriculum (Days 29–30)
- [ ] Wiring the actual trained dropout-risk model into the live UI (Module 5)
- [ ] **"Re-assess risk" feature** — a form where a teacher can manually update a student's key figures (e.g. attendance, units approved, grades) after the fact, submit them, and have the updated values run through the trained model live to return a fresh On track / Watch / At risk status — letting teachers check whether an intervention is actually working, rather than only seeing risk as a static one-time label
- [ ] Deployment (Module 6)

## Conclusion

The frontend phase of EduTrack is complete: a professional, responsive, six-page teacher dashboard built entirely in HTML/CSS/JS, using real dataset records rather than fully invented placeholder data. The next phase shifts from "what does it look like" to "what does it actually do" — building the backend and database that will let this interface persist data and eventually serve live predictions from the trained model, including a live re-assessment feature that lets teachers see how an updated student record changes their predicted risk.

## Project Roadmap

| Module | Days | Focus | Status |
|---|---|---|---|
| 1 | 1–10 | Python foundations + first baseline model | ✅ Done |
| 2 | 11–20 | Advanced ML + individual dropout-risk model | ✅ Done |
| 3 | 21–30 | Frontend — teacher dashboard (this repo) | ✅ Done |
| 4 | 31–40 | Backend — Flask REST API + MySQL | ⏳ Upcoming |
| 5 | 41–50 | Full-stack + ML integration, deploy backend/model | ⏳ Upcoming |
| 6 | 51–60 | Final deploy, end-to-end testing, Demo Day | ⏳ Upcoming |
