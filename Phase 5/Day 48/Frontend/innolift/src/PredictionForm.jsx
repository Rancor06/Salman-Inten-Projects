import { useState } from 'react';
import { API_BASE } from './apiBase';

// Day 47: unlike QuickRiskCheck (a local, rule-based "live preview" — see
// that file's own comments), this form sends real input to the actual
// Phase 2 model (DecisionTreeClassifier, all 36 raw dataset columns)
// behind POST /api/predict and displays whatever comes back. Nothing
// here is computed client-side. Grouped into sections since 36 raw
// fields in one flat form would be unusable.

const SECTIONS = [
  {
    title: 'Enrollment details',
    fields: [
      { key: 'marital_status', label: 'Marital status (code)' },
      { key: 'application_mode', label: 'Application mode (code)' },
      { key: 'application_order', label: 'Application order' },
      { key: 'course', label: 'Course (code)' },
      { key: 'previous_qualification', label: 'Previous qualification (code)' },
      { key: 'previous_qualification_grade', label: 'Previous qualification grade', step: 0.1 },
      { key: 'nationality', label: 'Nationality (code)' },
      { key: 'admission_grade', label: 'Admission grade', step: 0.1 },
      { key: 'age_at_enrollment', label: 'Age at enrollment' },
    ],
  },
  {
    title: 'Family background',
    fields: [
      { key: 'mothers_qualification', label: "Mother's qualification (code)" },
      { key: 'fathers_qualification', label: "Father's qualification (code)" },
      { key: 'mothers_occupation', label: "Mother's occupation (code)" },
      { key: 'fathers_occupation', label: "Father's occupation (code)" },
    ],
  },
  {
    title: 'Semester 1',
    fields: [
      { key: 'units_credited_sem1', label: 'Units credited' },
      { key: 'units_enrolled_sem1', label: 'Units enrolled' },
      { key: 'units_evaluations_sem1', label: 'Units evaluations' },
      { key: 'units_approved_sem1', label: 'Units approved' },
      { key: 'grade_sem1', label: 'Average grade', step: 0.1 },
      { key: 'units_without_eval_sem1', label: 'Units without evaluation' },
    ],
  },
  {
    title: 'Semester 2',
    fields: [
      { key: 'units_credited_sem2', label: 'Units credited' },
      { key: 'units_enrolled_sem2', label: 'Units enrolled' },
      { key: 'units_evaluations_sem2', label: 'Units evaluations' },
      { key: 'units_approved_sem2', label: 'Units approved' },
      { key: 'grade_sem2', label: 'Average grade', step: 0.1 },
      { key: 'units_without_eval_sem2', label: 'Units without evaluation' },
    ],
  },
  {
    title: 'Macroeconomic indicators (at enrollment)',
    fields: [
      { key: 'unemployment_rate', label: 'Unemployment rate (%)', step: 0.1 },
      { key: 'inflation_rate', label: 'Inflation rate (%)', step: 0.1 },
      { key: 'gdp', label: 'GDP', step: 0.01 },
    ],
  },
];

const TOGGLES = [
  { key: 'daytime_evening_attendance', label: 'Daytime attendance (unchecked = evening)' },
  { key: 'displaced', label: 'Displaced' },
  { key: 'educational_special_needs', label: 'Educational special needs' },
  { key: 'debtor', label: 'Debtor' },
  { key: 'tuition_up_to_date', label: 'Tuition fees up to date' },
  { key: 'gender', label: 'Gender (checked = male, per dataset coding)' },
  { key: 'scholarship_holder', label: 'Scholarship holder' },
  { key: 'international', label: 'International student' },
];

const ALL_FIELD_KEYS = [
  ...SECTIONS.flatMap((s) => s.fields.map((f) => f.key)),
  ...TOGGLES.map((t) => t.key),
];

const EMPTY_FORM = Object.fromEntries(
  ALL_FIELD_KEYS.map((key) => [key, TOGGLES.some((t) => t.key === key) ? false : ''])
);

const STATUS_STYLES = {
  Dropout: { bg: '#FBEAE9', fg: '#C4433F', dot: '#C4433F' },
  Enrolled: { bg: '#FBF0DD', fg: '#B9781E', dot: '#B9781E' },
  Graduate: { bg: '#E7F4ED', fg: '#2F8558', dot: '#2F8558' },
};

function PredictionForm() {
  const [form, setForm] = useState(EMPTY_FORM);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const setField = (key, value) => setForm((prev) => ({ ...prev, [key]: value }));

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    const body = { ...form };
    TOGGLES.forEach(({ key }) => {
      body[key] = form[key] ? 1 : 0;
    });

    try {
      const res = await fetch(`${API_BASE}/api/predict`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });

      let responseBody = {};
      try {
        responseBody = await res.json();
      } catch {
        responseBody = {};
      }

      if (!res.ok || !responseBody.success) {
        throw new Error(responseBody.error || 'Prediction failed.');
      }

      setResult(responseBody);
    } catch (err) {
      // Covers both "backend returned an error" and "backend unreachable"
      // (fetch() throws "Failed to fetch" for the latter, before res.json()).
      setError(err.message === 'Failed to fetch' ? 'Unable to reach the prediction service.' : err.message);
    } finally {
      setLoading(false);
    }
  };

  const style = result ? STATUS_STYLES[result.prediction] : null;

  return (
    <div className="prediction-form-wrap">
      <div className="qrc-intro">
        <h1>Dropout risk prediction</h1>
        <p>
          Sent to the trained Phase 2 model (Decision Tree, all 36 dataset fields) behind{' '}
          <code>POST /api/predict</code> — not computed in the browser.
        </p>
      </div>

      <form className="student-form" onSubmit={handleSubmit}>
        {SECTIONS.map((section) => (
          <fieldset className="pf-section" key={section.title}>
            <legend>{section.title}</legend>
            {section.fields.map(({ key, label, step }) => (
              <label key={key}>
                {label}
                <input
                  type="number"
                  step={step || 1}
                  value={form[key]}
                  onChange={(e) => setField(key, e.target.value)}
                  required
                />
              </label>
            ))}
          </fieldset>
        ))}

        <fieldset className="pf-section">
          <legend>Yes / no</legend>
          <div className="pf-toggles">
            {TOGGLES.map(({ key, label }) => (
              <label key={key} className="pf-toggle">
                <input
                  type="checkbox"
                  checked={form[key]}
                  onChange={(e) => setField(key, e.target.checked)}
                />
                {label}
              </label>
            ))}
          </div>
        </fieldset>

        <button type="submit" disabled={loading}>
          {loading ? (
            <>
              <span className="spinner" aria-hidden="true" />
              Generating prediction…
            </>
          ) : (
            'Predict'
          )}
        </button>

        {error && <p className="sf-message sf-message-error">{error}</p>}
      </form>

      {result && style && (
        <div className="risk-card">
          <div className="risk-card-head">
            <span className="risk-card-label">Model prediction</span>
            <span className="risk-pill" style={{ background: style.bg, color: style.fg }}>
              <span className="risk-pill-dot" style={{ background: style.dot }} />
              {result.prediction}
            </span>
          </div>
          <div className="risk-metric-row">
            <span className="k">Confidence</span>
            <span className="v">{Math.round(result.confidence * 100)}%</span>
          </div>
          {Object.entries(result.probabilities).map(([label, p]) => (
            <div className="risk-metric-row" key={label}>
              <span className="k">{label}</span>
              <span className="v">{Math.round(p * 100)}%</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default PredictionForm;
