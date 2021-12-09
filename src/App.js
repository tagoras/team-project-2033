import React, { useState, useEffect } from 'react';
import './App.css';
import {Navbar} from './Components/Navbar/Navbar';
import {Showcase} from './Components/Showcase/Showcase';
import {Route, Routes} from 'react-router-dom';
import LoginPage from './Pages/login';
import RegisterPage from './Pages/register';
import RegisterForm from './Components/Form/RegisterForm';



function App() {
  return (
    <div className="AppContainer">
      <Navbar/>
      <Showcase/>
      <RegisterForm/>
      {/* <Routes>
        <Route path='/home' element={<Showcase/>}/>
        <Route path='/register' element ={<RegisterPage/>}/>
        <Route path='/login' element={<LoginPage/>}/>
      </Routes> */}
    </div>
  );
}

export default App;
