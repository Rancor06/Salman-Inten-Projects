import { useState, useEffect } from 'react';
import StudentForm from './StudentForm';

// Day 41 task: fetch student data from the Flask backend and display it.
// Day 42 task: add a student via a form and update this list live.
// No student data is hardcoded — everything comes from GET/POST /api/students.
function StudentDirectory() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/students')
      .then((res) => {
        if (!res.ok) throw new Error(`Request failed: ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setStudents(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []); // empty dependency array = runs once when the component mounts

  // Day 42 Task 05: append the newly created student to state directly —
  // no re-fetch, no page reload, list just re-renders with the new card.
  const handleNewStudent = (newStudent) => {
    setStudents((prev) => [...prev, newStudent]);
  };

  const initials = (name) =>
    name
      .split(' ')
      .map((part) => part[0])
      .join('')
      .slice(0, 2)
      .toUpperCase();

  return (
    <div className="student-directory">
      <div className="sd-intro">
        <h1>Student directory</h1>
        <p>Live data pulled from the Flask API at <code>/api/students</code>.</p>
      </div>

      <StudentForm onCreated={handleNewStudent} />

      {loading && <p className="sd-status">Loading students…</p>}
      {error && <p className="sd-status sd-status-error">Couldn't load students: {error}</p>}

      {!loading && !error && (
        <div className="sd-grid">
          {students.map((student) => (
            <div className="student-card" key={student.id}>
              <div className="student-card-avatar">{initials(student.name)}</div>
              <div className="student-card-body">
                <h2>{student.name}</h2>
                <p className="student-card-course">{student.course}</p>
                <div className="student-card-row">
                  <span className="k">ID</span>
                  <span className="v">{student.id}</span>
                </div>
                <div className="student-card-row">
                  <span className="k">Email</span>
                  <span className="v">{student.email}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default StudentDirectory;
