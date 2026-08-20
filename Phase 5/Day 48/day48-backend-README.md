# Educere — Backend (Flask + MySQL + ML)

*Part of the [Educere — Intelligent Student Risk & Performance Analytics](../..#project-roadmap) capstone (Innolift Ventures 60-day internship), formerly EduTrack. This is Module 5 (Day 48): preparing and deploying the Flask backend so the app runs from a live URL instead of `localhost`.*

## What this backend does

- `/api/students`, `/api/predict` — the REST API the React app (`frontend/innolift`) talks to
- `/login`, `/logout`, `/profile`, `/admin/*`, `/student/*` — session-cookie auth and the admin/student portal routes, used by the converted React pages (`LoginPage`, `DashboardPage`, `StudentsPage`, etc.)
- `ml/model.py` — the trained dropout-risk model (`DecisionTreeClassifier`, 36 features), loaded once at startup
- MySQL (`edutrack_db`) — the students table + auth

## Day 48 — Deployment prep

The backend now runs the same way locally and in production — the only thing that changes is *how* it's started and *where* its data lives.

| | Local (dev) | Production (deployed) |
|---|---|---|
| Start command | `python app.py` | `gunicorn app:app --bind 0.0.0.0:$PORT` (see `Procfile`) |
| Host/port | `127.0.0.1:5000` (Flask default) | `0.0.0.0:$PORT` (platform-assigned) |
| Database | Local MySQL (`localhost`) | Hosted MySQL — Render/Railway can't reach your laptop |
| Secrets | `.env` (git-ignored) | Environment variables set in the platform's dashboard |

## Structure

```
backend/
├── app.py                 # Flask routes; reads PORT from env when run directly
├── db.py                  # MySQL connection, via .env / platform env vars
├── ml/                     # Dropout-risk model (Day 46)
├── requirements.txt        # Pinned versions, incl. scikit-learn==1.6.1 to match the trained model
├── Procfile                 # gunicorn start command — what Render/Railway actually run
├── .env.example             # Documents required env vars without real values
├── .gitignore                # .env excluded
└── docs/
    ├── day-45-api-testing.md
    ├── day-46-ml-integration.md
    ├── day-47-prediction-ui.md
    └── day-48-backend-deployment.md
```

## Environment variables

Set these in Render/Railway's dashboard (never committed):

- `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` — pointed at a hosted MySQL, not `localhost`
- `PORT` — usually auto-set by the platform

## Connecting the frontend

`frontend/innolift/src/apiBase.js` reads `VITE_API_BASE_URL` at build time. Set it to the live backend URL and rebuild (`npm run build`) — every fetch call in the app (student pages, login, prediction form) already reads from that one constant, so no other code changes.

## Progress so far

1. ✅ `requirements.txt` finalized — everything the backend actually imports, pinned to match the trained model's library versions
2. ✅ `Procfile` added — real production start command via gunicorn
3. ✅ `app.py` reads `PORT` from the environment and binds `0.0.0.0` when run directly
4. ✅ No hardcoded secrets — DB credentials come from `.env` / platform env vars only
5. ✅ `.env` git-ignored; `.env.example` documents required keys without values

## Remaining work

- Provision a hosted MySQL and import the schema/data
- Actually deploy (Render or Railway), get the live URL
- Test `/api/students` and `/api/predict` against the live URL
- Set `VITE_API_BASE_URL` and rebuild the frontend
- Resolve any CORS issues between the deployed frontend and backend

## Related docs

- Full deployment log (build/start commands, env vars, live URL, problems + fixes): `docs/day-48-backend-deployment.md`
- ML integration: `docs/day-46-ml-integration.md`
- Prediction UI: `docs/day-47-prediction-ui.md`
