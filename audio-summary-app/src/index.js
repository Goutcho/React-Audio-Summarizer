import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import logo from './img/logo.png'; // Assurez-vous que le chemin du logo est correct

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '20px' }}>
      <img src={logo} alt="Logo" style={{ width: '200px', height: '200' }} /> {/* Ajustez la taille selon vos besoins */}
    </div>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
