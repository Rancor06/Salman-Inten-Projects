# Day 29 — UI/UX Review & Multi-Day Integration

**Innolift Ventures – Crescent College Internship**
Phase 3 – Day 29 · Individual Project Review Prep

## Overview

Day 29's material was a UI/UX fundamentals deck (design principles, 60-30-10 color theory, typography, layout, header/footer conventions, component checklist) ahead of the Individual Project Review. Rather than treating it as a standalone exercise, this session used it as an audit tool against the actual EduTrack frontend — and used the review-prep window to fold three previously separate deliverables (Day 26's registration form, Day 27's component/props pattern, Day 28's `useState` pattern) into the live project instead of leaving them as isolated demos.

This README covers all of that work as one unit, since it was done together and touches the same files.

## What This Covers

1. **UI/UX audit** — every page checked against the deck's slide 15 submission checklist, item by item
2. **Footer** — the one genuine gap the audit found, added across all 5 app-shell pages
3. **Registration form integration** — Day 26's standalone form wired in as a real "Add student" flow
4. **Quick Risk Check widget** — a small React component combining Day 27's props pattern and Day 28's `useState` pattern, built as a preview of the eventual React migration
5. **A real bug, found and fixed** — a dark-mode CSS conflict in the React widget

---

## 1. UI/UX Audit

Checked all 6 existing pages against the deck's final checklist:

| Checklist item | Result |
|---|---|
| Consistent colors (60-30-10) | ✅ Pass — neutral system + one brand color + RAG triad reserved strictly for risk-status data, not decoration |
| Responsive layout | ✅ Pass — verified at 1280px / 768px / 375px |
| Proper spacing | ✅ Pass |
| Attractive buttons | ✅ Pass |
| Mobile friendly | ✅ Pass |
| Typography (max 2 fonts) | ⚠️ Technically 3 — justified: the third (mono) is reserved exclusively for numeric/data fields, never prose, matching financial-dashboard convention |
| Header/navbar | ⚠️ Sidebar nav, not a top navbar — intentional: standard convention for data-dense dashboard apps rather than marketing sites |
| **Footer** | ❌ **Missing on every page — the one real gap. Fixed (see below).** |

## 2. Footer

Added a single `.app-footer` component (dark background matching the sidebar, brand mark, quick nav links with the current page bolded, support contact, copyright) to:

- `dashboard.html`
- `students.html`
- `reports.html`
- `settings.html`
- `student-detail.html`

`login.html` was left without one deliberately — auth screens conventionally skip footers, and one would break the existing centered two-column layout.

**Styling:** appended to `edutrack.css` only — no existing rules touched. Uses the same color tokens as the rest of the app (`--ink`, `--line`, `--rag-green`), no new palette introduced.

**QA:** every page re-rendered at 1280px / 768px / 375px after the change; footer stacks vertically below 700px. Checked the browser console on all 6 pages — the only message anywhere was a `403` on the Google Fonts request from the offline test environment, not a real defect.

## 3. Registration Form Integration (Day 26)

The Day 26 form previously lived as a disconnected standalone deliverable. It fills a real gap in EduTrack — there was no way to add a new student — so it's now wired in as an actual flow instead of staying separate:

- Renamed `index.html` / `style.css` / `script.js` → `register-student.html` / `.css` / `.js` for clarity inside the project folder
- Added a **"+ Add student"** button to `students.html`, linking to the form
- Added a **"← Back to student register"** link inside the form for round-trip navigation

The form keeps its own distinct design system (Source Serif 4 / teal-amber "student file" aesthetic) rather than being reskinned to match the dashboard's Space Grotesk / slate-blue system — a data-entry document is meant to read differently from a monitoring dashboard, and the field set already matches exactly what the dropout-risk model consumes (attendance, GPA, active backlogs).

## 4. Quick Risk Check Widget (Day 27 + 28)

Built as a small standalone Vite + React project (`quick-risk-check/`) rather than a full dashboard rebuild — the curriculum schedules the actual React migration for later, so this is a proof-of-concept, not a replacement for the live HTML/CSS/JS dashboard.

**Combines two patterns from two different days into one real component:**

- **`StudentRiskCard.jsx`** — pure presentational component, same props-in/render-out shape as Day 27's `StudentProfileCard.jsx`
- **`QuickRiskCheck.jsx`** — controlled inputs via `useState`, same pattern as Day 28's `NamePreview.jsx` / `ThemeToggle.jsx`, but driving a real calculation instead of a toy example

**Design decision — the thresholds aren't arbitrary:**

| Input | On track | Watch | At risk |
|---|---|---|---|
| Attendance % | ≥ 80% | 65–79% | < 65% |
| Previous GPA (0–10) | ≥ 6.5 | 5–6.49 | < 5 |

Attendance cutoffs are pulled directly from the sliders already on `settings.html`. GPA uses the same 0.00–10.00 scale as the Day 26 registration form. The widget deliberately reuses EduTrack's own numbers rather than inventing new ones, so it reads as the same system, not a disconnected demo.

**Visual design:** matches EduTrack's actual CSS custom properties (`--ink`, `--paper`, `--brand`, RAG colors) rather than a new palette, since this previews a future React port of the existing dashboard.

## 5. Bug Found and Fixed

**Symptom:** the widget's "Quick risk check" heading was invisible — white text on a white card.

**Root cause:** Vite's default scaffold ships a leftover `index.css` with a `prefers-color-scheme: dark` media query that recolors all `h1`/`h2` elements to near-white. The new `App.css` never gave `.qrc-intro h1` its own explicit color, so on any system/browser in dark mode, that boilerplate rule silently took over.

**Fix:** added `color: var(--ink)` directly to `.qrc-intro h1` (and confirmed `.qrc-intro p` already had one), overriding the inherited boilerplate rule.

**Verification — done properly, not just by eye:** rather than trusting a screenshot, pulled the actual computed `color` value via a scripted browser check in both light and dark color-scheme modes:

```
light mode -> h1 color: rgb(26, 34, 51)  | card background: rgb(255, 255, 255)
dark mode  -> h1 color: rgb(26, 34, 51)  | card background: rgb(255, 255, 255)
```

`rgb(26, 34, 51)` is `#1A2233` — the intended ink color — confirmed identical in both modes. This is the same class of bug worth checking for in the Day 27/28 project too, since it uses the same Vite boilerplate `index.css`.

---

## File Structure

```
edutrack/
├── login.html                  # unchanged
├── app.js                       # unchanged
├── edutrack.css                  # updated — footer styles appended
├── dashboard.html                 # updated — footer added
├── students.html                   # updated — footer + "Add student" button
├── reports.html                     # updated — footer added
├── settings.html                     # updated — footer added
├── student-detail.html                # updated — footer added
├── register-student.html               # Day 26 form, renamed + linked in
├── register-student.css
├── register-student.js
└── quick-risk-check/                    # standalone Vite + React project
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── App.css
        ├── QuickRiskCheck.jsx
        └── StudentRiskCard.jsx
```

## How to Run

**EduTrack site (no build step):** open `login.html` or `dashboard.html` directly in a browser — all pages link to each other and to `edutrack.css` / `app.js` by relative filename, so the folder must stay together.

**Quick Risk Check widget:**
```bash
cd quick-risk-check
npm install
npm run dev
```
Open `http://localhost:5173`.

## Talking Points for Review

- **3 fonts, not 2:** the mono font is reserved exclusively for data (IDs, stat numbers, RAG labels) — never prose — matching financial-dashboard convention.
- **Sidebar, not top navbar:** the standard pattern for data-dense dashboard apps (Notion, Linear, Vercel) rather than a deviation from marketing-site convention.
- **RAG colors sit outside 60-30-10:** they're functional data encoding for risk status, not decorative accent color.
- **Quick Risk Check widget:** "Days 27–28 built props and `useState` through generic exercises. This applies both patterns to EduTrack's actual numbers instead — the same attendance and GPA thresholds already live on the Settings page."

## Pending / Next Steps

- [ ] Decide whether to reskin the registration form to match dashboard tokens, or keep its intentionally distinct "document" aesthetic
- [ ] Backend (Module 4) — Flask REST API + MySQL
- [ ] Full React migration of the dashboard (Days 29–30 curriculum target)
- [ ] Persisting Settings changes, teacher notes, and the new registration submissions (currently frontend-only)

---

**Author:** Salman Maricar
**Internship:** Innolift Ventures — 60-Day ML Internship, Phase 3, Day 29
**Project:** EduTrack (Student Dropout Risk Prediction System)
