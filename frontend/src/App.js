import React from 'react';
import './App.css';
import ConversationForm from './components/ConversationForm';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 style={{ fontSize: '30px' }}>GMO Volunteer Matcher</h1>
      </header>
      <ConversationForm />
    </div>
  );
}

export default App;
