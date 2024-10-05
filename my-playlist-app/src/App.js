import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AudioProvider } from './components/AudioContext';
import { AuthProvider } from './components/AuthContext';
import Library from './components/Library';
import Login from './components/Login';
import './components/Common.css'; //css for the whole application is imported here
import './components/responsive.css';

function App() {
  return (
    <AuthProvider>
    <AudioProvider>
    <Router>
      <div className="app">
        <Routes>
          <Route exact path="/" element={<Library />} />
          <Route path="/login" component={Login} />
          <Route path="/playlist" element={<Library />} /> reason
        </Routes>
      </div>
    </Router>
    </AudioProvider>
    </AuthProvider>
  );
}

export default App;
