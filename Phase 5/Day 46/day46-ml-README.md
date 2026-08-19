# ML Integration — Dropout Risk Prediction API

*Part of the [EduTrack — Student Performance & Dropout Risk Predictor](../..#project-roadmap) capstone (Innolift Ventures 60-day internship). This is the Module 5 (Day 46) integration step: the Phase 2 model ([Module 2, Days 19–20](https://github.com/Rancor06) — see that project's own README) is wired into this Flask backend as a live prediction endpoint.*

## What this does

Takes the trained `DecisionTreeClassifier` from Phase 2 and exposes it as `POST /api/predict`, so the React frontend (or Postman, or anything else) can send a student's data and get a Dropout / Enrolled / Graduate prediction back as JSON — instead of the model living only in a Colab notebook.

## Model

- **Type:** `DecisionTreeClassifier(max_depth=8, class_weight="balanced", random_state=42)`
- **Trained on:** UCI "Predict Students' Dropout and Academic Success" dataset (`data.csv`, 4,424 rows), all 36 raw feature columns, no scaling
- **Target:** `Dropout` / `Enrolled` / `Graduate`
- **Test accuracy:** 67% (macro F1 0.64) — same numbers as the Phase 2 notebook's own evaluation
- **File:** `ml/dropout_model.pkl`, reproducible via `ml/train_model.py`

## Structure

```
backend/
├── app.py                # Flask routes, including POST /api/predict
├── ml/
│   ├── model.py           # loading, validation, inference — kept separate from routes
│   ├── train_model.py     # reproduces dropout_model.pkl from data.csv
│   └── dropout_model.pkl  # the trained model
└── requirements.txt        # pins scikit-learn==1.6.1 to match the training version
```

`ml/model.py` loads the model once at import time (not per-request), validates all 36 required fields before touching the model, and never lets a bad request crash the server.

## API

**Request** — `POST /api/predict`, JSON body with all 36 fields (see `docs/day-46-ml-integration.md` for the full list and field-name mapping).

**Response (success, 200):**
```json
{
  "success": true,
  "prediction": "Dropout",
  "confidence": 0.614,
  "probabilities": { "Dropout": 0.614, "Enrolled": 0.1157, "Graduate": 0.2703 }
}
```

**Response (invalid input, 400):**
```json
{ "success": false, "error": "Missing required field(s): course, admission_grade" }
```

## Progress so far

1. ✅ Verified the trained model loads and predicts correctly outside Flask
2. ✅ Separated ML logic (`ml/model.py`) from API routes (`app.py`)
3. ✅ Model loads once at Flask startup, reused across requests
4. ✅ `POST /api/predict` endpoint built and tested
5. ✅ Invalid-input handling: missing fields, empty body, wrong type, invalid binary values, no body — all return clean 400s, never a crash
6. ✅ Tested in Postman (see `Student Management API.postman_collection.json`)
7. ✅ Confirmed prediction consistency (same input → same output, every time)
8. ✅ Confirmed existing `/api/students` routes still work unchanged

## Remaining work

- Postman screenshots and filled-in test results — see `docs/day-46-ml-integration.md`
- Live deployment (Day 48)

## Related docs

- Full technical report: `docs/day-46-ml-integration.md`
- Original model project: see its own `README.md` (Module 2, Days 19–20)
