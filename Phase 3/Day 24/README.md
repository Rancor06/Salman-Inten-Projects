# EduTrack — Student Performance & Dropout Risk Predictor
### Project Progress Report — Day 24

## Project Title

EduTrack – Student Performance & Dropout Risk Predictor

## Work Completed Today

- Built the Reports page — risk distribution bar, cohort-wide risk-driver breakdown, and a per-course table, using the same RAG (Red/Amber/Green) system as the rest of the app instead of introducing a new visual language.
- Built the Settings page — profile fields, animated notification toggles, and adjustable risk-threshold sliders, built in pure CSS/JS to keep the frontend dependency-free ahead of backend integration.
- Enabled full sidebar navigation across all six pages — Reports and Settings were placeholder links as of yesterday, since they didn't exist yet; now every nav item resolves to a real page.
- Replaced all mock student data with a stratified sample of 10 real records from the UCI Student Dropout dataset, correcting yesterday's 7-vs-42 mismatch rather than papering over it with more invented rows.
- Updated the Student Details example to a real at-risk student's actual academic and enrollment values, so the risk-driver explanation reflects genuine feature data instead of a fictional profile.

## Screenshots of Developed Pages

| Login | Reports |
|---|---|
| ![Login page](screenshots/login.png) | ![Reports page](screenshots/reports.png) |

| Settings | Student Register (Real Data) |
|---|---|
| ![Settings page](screenshots/settings.png) | ![Student register page](screenshots/students.png) |

| Dashboard (Updated Stats) | |
|---|---|
| ![Dashboard page](screenshots/dashboard.png) | |

## Brief Explanation of Implemented Features

Today's work closed out the two modules flagged as "planned for future development" in yesterday's report, bringing all six EduTrack pages to a fully navigable, feature-complete frontend. Reports surfaces risk distribution, model feature importance at the cohort level, and per-course trends; Settings adds profile fields and configurable alert thresholds via animated toggle/slider controls, all built in plain CSS/JS with no external libraries. Equally important, the student data across the app was upgraded from illustrative mock values to a real, stratified sample drawn from the same UCI dataset the prediction model was trained on — including honestly relabelling fields the dataset doesn't actually contain (e.g. no attendance percentage exists, so a real derived "unit completion" metric was used instead). This puts the frontend in a complete, honestly-grounded state ahead of backend/database integration in Module 4.

## Current Project Progress

- [x] Login Page Completed
- [x] Dashboard Completed
- [x] Student Register Page Completed (real dataset)
- [x] Student Details Page Completed
- [x] Reports Page Completed
- [x] Settings Page Completed
- [x] Responsive Navigation Implemented
- [x] Mobile-Friendly Layout Added
- [x] Consistent UI Design Applied Across Pages
- [ ] Backend & Database Integration (Planned for Module 4)
