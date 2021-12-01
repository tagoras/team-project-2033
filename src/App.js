import React, { useState, useEffect } from 'react';
import './App.css';
import {Navbar} from './Components/Navbar/Navbar';
import {Showcase} from './Components/Showcase/Showcase';
import {Route, Routes} from 'react-router-dom';
import loginPage from './Pages/login';
import registerPage from './Pages/register';



function App() {
  return (
    <div className="AppContainer">
      <Navbar/>
      <Routes>
        <Route path='/home' element={<Showcase/>}>
        </Route>
        <Route path='/register' element ={registerPage()}/>
        <Route path='/login' element={loginPage()}/>
      </Routes>
    </div>
  );
}

export default App;
