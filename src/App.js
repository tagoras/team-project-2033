import React, { useState, useEffect } from 'react';
import './App.css';
import { Component } from 'react';
import {Navbar} from './Components/Navbar/Navbar';
import {Showcase} from './Components/Showcase/Showcase';



function App() {
  return (
    <div>
      <Navbar/>
      <Showcase/>
    </div>
  );
}

export default App;
