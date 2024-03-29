import React, { useState, useEffect } from 'react';
import './App.css';
import {Navbar} from './Components/Navbar/Navbar';
import {Showcase} from './Components/Showcase/Showcase';
import {Route, Routes,Navigate} from 'react-router-dom';
import LoginPage from './Pages/Login/login';
import RegisterPage from './Pages/Register/register';
import AboutUs from './Components/AboutUsSection/AboutUs';
import Footer from './Components/Footer/Footer.component';
import UserPage from './Pages/User';


import AdminPage from './Pages/Admin/Admin';
import GetInTouch from './Pages/GetInTouch/GetInTouch';
import { Logout } from './Pages/Logout/Logout';



function App() {
  return (
    <div className="AppContainer">
      <Navbar/>
      <Routes>
        <Route path='/about-us' element={<AboutUs/>}/>
        <Route path="/" element={<Showcase/>}/>
        <Route path='/home' element={<Showcase/>}/>
        <Route path='/register' element ={<RegisterPage/>}/>
        <Route path='/login' element={<LoginPage/>}/>
        <Route path='/Admin' element={<AdminPage/>}></Route>
        <Route path='/User' element={<UserPage/>}></Route>
        <Route path='/Logout' element={<Logout/>}></Route>
        {/* TODO 
          Add Default Routing If Page Does not exist!!!
        */}
      </Routes>
    </div>
  );
}

export default App;
