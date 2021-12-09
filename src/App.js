import React, {Component } from 'react';
import './App.css';
import {Navbar} from './Components/Navbar/Navbar';
import {Showcase} from './Components/Showcase/Showcase';
import RegisterForm from './Components/RegisterForm/RegisterForm';

import LoginForm from './Components/LoginForm/LoginForm';



class App extends Component {
  
  constructor(props){
    super(props);
    this.state = {
      isRegistering: true,
    };
  }

  render(){
    let isLoggedIn = this.state.isRegistering;
    console.log(isLoggedIn);
    return (
      <div className="AppContainer">
        <Navbar/>
        <Showcase/>
        {isLoggedIn ? <RegisterForm/> : <LoginForm/>}
        
        {/* <Routes>
          <Route path='/home' element={<Showcase/>}/>
          <Route path='/register' element ={<RegisterPage/>}/>
          <Route path='/login' element={<LoginPage/>}/>
        </Routes> */}
      </div>
    );
  }

}

export default App;
