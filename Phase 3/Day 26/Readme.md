# EduTrack — Student Registration Form

A responsive student registration form built for **EduTrack**, a dropout-risk prediction system. Built as part of the InnoLift Ventures internship, Day 26 — Form Validation (Tasks 01–04).

Unlike a generic sign-up form, this one is purpose-built around what the dropout-risk model actually needs: alongside standard personal/contact details, it captures academic data — attendance, GPA, and active backlogs — as a distinct "transcript record" section.

---

## Tasks Covered

| Task | Description | Where |
|------|-------------|-------|
| 01 | Responsive registration form (HTML5 + CSS3) | `index.html`, `style.css` |
| 02 | Client-side JavaScript validation | `script.js` |
| 03 | Regex-based validation (name, email, phone, roll no., password) | `script.js` (`RE` object) |
| 04 | Complete integrated system (all of the above + live UI feedback) | all three files together |

---

## File Structure

```
edutrack-task01/
├── index.html      # Form markup and structure
├── style.css        # Design system, layout, responsive rules
├── script.js         # Validation logic, regex, live UI feedback
└── README.md         # This file
```

All three files must stay together and linked as-is (`style.css` and `script.js` are referenced relatively from `index.html`) — don't rename or move them individually.

---

## Design Concept

The layout intentionally avoids the typical "stacked card" sign-up form. Instead it uses a **student file** metaphor:

- **Left sidebar (sticky)** — styled like the cover of a physical student file: a folder tab, a record stamp, an avatar placeholder, and a live section-progress checklist.
- **Right column** — the form itself flows as a continuous document, with large ghost-numeral margin markers (01, 02, 03, 04) instead of boxed cards. Fields are underlined rather than boxed, giving it a ledger/document feel.
- **Academic Details section** — the one deliberately boxed, monospaced "transcript strip" on the page. Since this is the data the dropout-risk model actually consumes, it's designed to visually stand out from the rest of the form.

On screens under ~900px, the sidebar collapses to a static block above the form.

### Color system — 60/30/10

| Role | Color | Usage |
|------|-------|-------|
| 60% Dominant | `#F7F8FA` (paper) | Page background |
| 30% Secondary | `#FFFFFF` surfaces, `#10151F` ink text, `#E1E5EB` borders | Cards, sidebar, body text, hairlines |
| 10% Accent | `#0F766E` (teal), `#B45309` (amber) | Buttons, focus states, section numerals, transcript border |

`#B42318` (error red) sits outside this ratio — it's a functional validation-state color, not part of the decorative palette.

### Typography

- **Source Serif 4** — headings, brand name, section titles (academic/document feel)
- **Public Sans** — body text, labels, inputs
- **IBM Plex Mono** — academic/numeric fields (roll no., attendance, GPA), record stamp, sidebar metadata — makes data fields read like transcript entries

---

## Features

- Fully responsive: desktop sidebar layout → stacked mobile layout
- Live sidebar checklist — section numbers turn into ✓ and fill teal as each of the 4 sections is completed
- Inline field-level error messages (no popups/alerts)
- Red/teal states on every field to show invalid/valid at a glance
- Live password strength meter (4-bar, Weak → Strong)
- Toast notification on successful submission
- No JavaScript dependency for layout — page is fully readable/usable with `script.js` removed (Task 01 in isolation)

---

## Validation Rules

| Field | Rule |
|-------|------|
| Full Name | Required, letters and spaces only, 3–50 characters |
| Date of Birth | Required, must calculate to age 18 or older |
| Gender | Required (one of three options) |
| Email | Required, standard email regex |
| Phone | Required, 10 digits, must start with 6–9 (Indian mobile format) |
| Roll Number | Required, 4–15 alphanumeric characters (dashes/slashes allowed) |
| Course / Dept | Required, must select from dropdown |
| Semester | Required, must select from dropdown |
| Attendance % | Required, numeric, 0–100 |
| Previous GPA | Required, numeric, 0.00–10.00 |
| Active Backlogs | Optional; if filled, must be a non-negative number |
| Password | Required, 8+ characters, at least one uppercase, one lowercase, one number, one special character |
| Confirm Password | Required, must match Password exactly |

All validation runs on submit; the password strength meter and section checklist also update live as the user types.

---

## How to Run

1. Keep all three files in the same folder.
2. Open `index.html` directly in any modern browser (Chrome, Edge, Firefox) — no build step or server required.
3. Requires an internet connection on first load (Google Fonts are loaded via CDN); the form itself works offline once fonts are cached.

---

## Notes

- This form is a standalone frontend deliverable (Tasks 01–04 of Day 26). It does not yet connect to a backend or database — submitted data is only shown in-browser via the success toast, not persisted.
- Built independently, referencing the InnoLift Ventures Day 26 demo materials for task scope only — layout, design system, and code are original.

---

**Author:** Salman
**Internship:** InnoLift Ventures — 60-Day ML Internship, Day 26
**Project:** EduTrack (Student Dropout Risk Prediction System)
