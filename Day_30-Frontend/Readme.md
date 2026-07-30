# Day 30 — Edutrack Frontend Review

**Innolift Ventures – Crescent College Internship**  
Phase 3 – Day 30 · Individual Project Review Prep

## Overview

Day 29's material was a UI/UX fundamentals deck (design principles, 60-30-10 color theory, typography, layout, header/footer conventions, component checklist) ahead of the Individual Project Review. Rather than treating it as a standalone exercise, this session used it as an audit tool against the actual EduTrack frontend — and used the review-prep window to fold three previously separate deliverables (Day 26's registration form, Day 27's component/props pattern, Day 28's `useState` pattern) into the live project instead of leaving them as isolated demos.

During the project review, additional usability improvements were suggested by the mentors. These focused on improving consistency across the application rather than introducing new functionality. The recommended changes were implemented immediately and are included in this README.

This README covers all of that work as one unit, since it was done together and touches the same files.

## What This Covers

1. **UI/UX audit** — every page checked against the deck's slide 15 submission checklist, item by item
2. **Header and footer consistency improvements** across the application
3. **Registration form integration** — Day 26's standalone form wired in as a real "Add student" flow with a consistent sidebar
4. **Downloadable Cohort Report** feature added to the Reports page
5. **Quick Risk Check widget** — a small React component combining Day 27's props pattern and Day 28's `useState` pattern, built as a preview of the eventual React migration
6. **A real bug, found and fixed** — a dark-mode CSS conflict in the React widget

---

## 1. UI/UX Audit

Checked all existing pages against the deck's final checklist:

| Checklist item | Result |
|---|---|
| Consistent colors (60-30-10) | ✅ Pass — neutral system + one brand color + RAG triad reserved strictly for risk-status data |
| Responsive layout | ✅ Pass — verified at 1280px / 768px / 375px |
| Proper spacing | ✅ Pass |
| Attractive buttons | ✅ Pass |
| Mobile friendly | ✅ Pass |
| Typography | ⚠️ Three fonts used intentionally (mono reserved only for numeric data) |
| Navigation | ⚠️ Sidebar navigation intentionally used for dashboard workflow |
| Footer | ❌ Missing during audit → Fixed |
| Header consistency | ⚠️ Review feedback received → Updated to use a consistent application header across pages |

The audit confirmed that the overall design followed the UI/UX principles taught during the session. The mentor review mainly focused on improving consistency between pages rather than redesigning existing layouts.

---

## 2. Header & Footer Improvements

Following the review comments, the application's layout was standardized.

### Header

A consistent page header was added across the dashboard pages to provide a uniform navigation experience and clearer page identity.

### Footer

The previously missing footer was added across all application pages except the login screen.

Added to:

- dashboard.html
- students.html
- reports.html
- settings.html
- student-detail.html

The footer includes EduTrack branding, quick navigation links, support contact, and copyright information.

---

## 3. Registration Form Integration (Day 26)

The standalone Day 26 registration form was fully integrated into EduTrack.

Changes include:

- Renamed files to project-specific names
- Added **+ Add Student** button
- Added navigation back to the student list
- Updated the registration page to use the same sidebar navigation as the rest of EduTrack for a consistent user experience.

---

## 4. Downloadable Cohort Report

A download option was added to the Reports page, allowing users to export the cohort report for offline viewing and sharing.

---

## 5. Quick Risk Check Widget (Day 27 + 28)

Built as a standalone Vite + React project combining reusable **props** components with **useState** state management while reusing EduTrack's attendance and GPA thresholds.

---

## 6. Bug Found and Fixed

A dark-mode CSS conflict from Vite's default `index.css` caused the widget heading to appear white on a white background.

**Fix:** Added:

```css
.qrc-intro h1 {
    color: var(--ink);
}
```

Verified in both light and dark mode using computed browser styles.

---

## File Structure

```text
edutrack/
├── login.html
├── app.js
├── edutrack.css
├── dashboard.html
├── students.html
├── reports.html
├── settings.html
├── student-detail.html
├── register-student.html
├── register-student.css
├── register-student.js
└── quick-risk-check/
```

## How to Run

### EduTrack

Open `login.html` or `dashboard.html`.

### Quick Risk Check

```bash
cd quick-risk-check
npm install
npm run dev
```

Visit `http://localhost:5173`.

---

## Talking Points for Review

- Consistent header and footer across dashboard pages.
- Registration page now uses the same sidebar.
- Cohort reports are downloadable.
- React widget demonstrates `props` + `useState` using EduTrack's real thresholds.

---

## Pending / Next Steps

- Backend integration (Flask + MySQL)
- Full React migration
- Persist registration submissions
- Persist settings and teacher notes
- Connect downloadable reports to backend-generated data

---

**Author:** Salman Maricar  
**Internship:** Innolift Ventures – 60-Day ML Internship, Phase 3 – Day 30  
**Project:** EduTrack (Student Dropout Risk Prediction System)
