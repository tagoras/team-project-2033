import RegisterForm from "../Components/Form/registerForm.js";
import "../Pages/Register.css";
import { useNavigate } from "react-router-dom";
import React from "react";
import { Component } from "react/cjs/react.production.min";

class RegisterPage extends Component{
  
  constructor(props){
    super(props);
    let registrationStatus = -1;

    this.state = {
      errorOccured: false,
    }
    this.addRegisterHandler = this.addRegisterHandler.bind(this);
  }
 
  

  render(){
    return (
      <section>
        <div className="register">
          <RegisterForm addRegisterForm={this.addRegisterHandler} errorOccured = {true}/>
        </div>
      </section>
    );
  }

  async addRegisterHandler(registerData) {
    console.log(JSON.stringify(registerData));
    let fetchPromise = await fetch("/register", {
      method: "POST",
      body: JSON.stringify(registerData),
    })
    console.log(fetchPromise.statusText);
    this.setState({errorOccured: fetchPromise.ok});

  }

}

export default RegisterPage;