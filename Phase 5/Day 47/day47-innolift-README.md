# EduTrack — Frontend (React + Vite)

*Part of the [EduTrack — Student Performance & Dropout Risk Predictor](../..#project-roadmap) capstone (Innolift Ventures 60-day internship). This is the React frontend — Module 3 build-out (Days 21–30), extended in Module 5 (Day 47) to connect the dropout-risk prediction API to the UI.*

## What this app does

- Lists and adds students (`StudentDirectory.jsx`, `StudentForm.jsx`), backed by the Flask + MySQL API
- A local, rule-based risk preview (`QuickRiskCheck.jsx`) — quick, client-side only, not the real model
- A real dropout-risk predictor (`PredictionForm.jsx`) — sends actual input to the trained model behind `POST /api/predict` and displays whatever comes back

## Day 47 — Prediction UI

`PredictionForm.jsx` is the newest piece. The Phase 2 model needs 36 raw dataset fields, so the form is grouped into six sections instead of one long list:

- Enrollment details
- Family background
- Semester 1
- Semester 2
- Macroeconomic indicators
- Yes/No (the 8 binary fields, rendered as checkboxes)

On submit, it POSTs to `${API_BASE}/api/predict`, shows a loading spinner while waiting, and renders the result — prediction, confidence, and the full probability breakdown — in a card styled to match `StudentRiskCard`. If the request fails (bad input, or the backend is unreachable), a clear error message is shown instead of a silent failure or a stuck UI.

## Structure

```
src/
├── App.jsx              # renders QuickRiskCheck + PredictionForm + StudentDirectory
├── apiBase.js            # resolves API_BASE — relative in dev, VITE_API_BASE_URL in prod
├── PredictionForm.jsx     # real /api/predict form (Day 47)
├── QuickRiskCheck.jsx     # local heuristic preview (not the real model)
├── StudentDirectory.jsx   # student list, pulls from /api/students
├── StudentForm.jsx        # add-student form, posts to /api/students
└── StudentRiskCard.jsx    # shared result-card styling
```

## Running locally

```bash
npm install
npm run dev
```

Requires the Flask backend running (`python app.py` in `backend/backend/`) — in dev, `apiBase.js` resolves to an empty string, so requests go through the Vite proxy to `localhost:5000`.

## Connecting to a deployed backend (Day 48)

Set `VITE_API_BASE_URL` (e.g. in `.env.production`) to the live backend URL, then `npm run build`. No code changes needed — every fetch call already reads from `API_BASE` instead of a hardcoded URL.

## Progress so far

1. ✅ Reviewed and confirmed `/api/predict` works correctly (Postman) before building the UI
2. ✅ Built the prediction input form covering all 36 model fields
3. ✅ Connected the form to the live API via `fetch`
4. ✅ Prediction result displayed clearly in the UI, not just the console
5. ✅ Loading state while the request is in flight
6. ✅ Error handling for invalid input and an unreachable backend
7. ✅ Verified multiple predictions update the UI correctly and don't leave stale results

## Remaining work

- Screenshots of the form, a successful prediction, and the error state — see `docs/day-47-prediction-ui.md`
- Point `VITE_API_BASE_URL` at the live backend once Day 48 deployment is done

## Related docs

- Full technical report: `docs/day-47-prediction-ui.md` (in the backend repo)
- Prediction API details: `docs/day-46-ml-integration.md`
