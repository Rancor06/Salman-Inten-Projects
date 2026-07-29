import { useState } from 'react';

function ThemeToggle() {
  const [isDark, setIsDark] = useState(false);

  const pageStyle = {
    backgroundColor: isDark ? '#1a1a1a' : '#ffffff',
    color: isDark ? '#ffffff' : '#000000',
    minHeight: '100vh',
    padding: '20px',
  };

  return (
    <div style={pageStyle}>
      <h1>Theme Toggle</h1>
      <button onClick={() => setIsDark(!isDark)}>
        {isDark ? 'Dark Mode' : 'Light Mode'}
      </button>
    </div>
  );
}

export default ThemeToggle;