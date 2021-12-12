import React, { useState, useEffect } from 'react';
import './App.css';
import {Navbar} from './Components/Navbar/Navbar';
import {Showcase} from './Components/Showcase/Showcase';
import {Route, Routes,Navigate} from 'react-router-dom';
import LoginPage from './Pages/login';
import RegisterPage from './Pages/register';
import AboutUs from './Components/AboutUsSection/AboutUs';
import Footer from './Components/Footer/Footer.component';



function App() {
  return (
    <div className="AppContainer">
      <Navbar/>
      <Routes>
        <Route exact path="/" element={<Showcase/>}/>
        <Route path='/home' element={<Showcase/>}/>
        <Route path='/register' element ={<RegisterPage/>}/>
        <Route path='/login' element={<LoginPage/>}/>
      </Routes>
      <AboutUs/>
      <Footer/>
    </div>
  );
}

export default App;
