import { useState } from 'react';

function NamePreview() {
  const [name, setName] = useState('');

  return (
    <div>
      <h1>Name Preview</h1>
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <h2>{name ? `Hello, ${name}!` : 'Hello, Guest!'}</h2>
    </div>
  );
}

export default NamePreview;