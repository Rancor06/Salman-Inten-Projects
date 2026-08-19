import QuickRiskCheck from './QuickRiskCheck';
import PredictionForm from './PredictionForm';
import StudentDirectory from './StudentDirectory';
import './App.css';
import './StudentDirectory.css';

function App() {
  return (
    <div className="app-shell app-shell-stacked">
      <QuickRiskCheck />
      {/* Day 47: real model prediction, separate from the local-only preview above */}
      <PredictionForm />
      <StudentDirectory />
    </div>
  );
}

export default App;
