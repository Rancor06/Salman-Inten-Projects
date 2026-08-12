import { useState } from 'react';

// Day 42 task: controlled form that POSTs a new student to Flask.
// Calls onCreated(newStudent) so the parent can add it to the displayed
// list without a page refresh or a re-fetch.
function StudentForm({ onCreated }) {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [course, setCourse] = useState('');

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault(); // stop the browser's default full-page-reload submit

    setLoading(true);
    setError(null);
    setSuccess(false);

    fetch('/api/students', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, course }),
    })
      .then(async (res) => {
        const body = await res.json();
        if (!res.ok || !body.success) {
          throw new Error(body.error || `Request failed: ${res.status}`);
        }
        return body.student;
      })
      .then((newStudent) => {
        onCreated(newStudent);   // add to the list in the parent, no refresh
        setName('');
        setEmail('');
        setCourse('');
        setSuccess(true);
      })
      .catch((err) => {
        setError(err.message);
      })
      .finally(() => {
        setLoading(false);       // runs whether it succeeded or failed
      });
  };

  return (
    <form className="student-form" onSubmit={handleSubmit}>
      <h2>Add a student</h2>

      <label>
        Student name
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="e.g. Rahul Nair"
          required
        />
      </label>

      <label>
        Email
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="e.g. rahul@crescent.edu"
          required
        />
      </label>

      <label>
        Course
        <input
          type="text"
          value={course}
          onChange={(e) => setCourse(e.target.value)}
          placeholder="e.g. AI & Data Science"
          required
        />
      </label>

      <button type="submit" disabled={loading}>
        {loading ? (
          <>
            <span className="spinner" aria-hidden="true" />
            Adding…
          </>
        ) : (
          'Add student'
        )}
      </button>

      {error && <p className="sf-message sf-message-error">{error}</p>}
      {success && <p className="sf-message sf-message-success">Student added!</p>}
    </form>
  );
}

export default StudentForm;
