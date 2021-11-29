import React, { useState, useEffect } from 'react';
import './App.css';
import {Navbar} from './Components/Navbar/Navbar';
import {Showcase} from './Components/Showcase/Showcase';



function App() {
  return (
    <div className="AppContainer">
      <Navbar/>
      <Showcase/>
    </div>
  );
}

export default App;
