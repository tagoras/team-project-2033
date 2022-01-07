import LoginForm from "../Components/Form/loginForm.js";
import { useNavigate } from "react-router-dom";
import {useState} from 'react';

function LoginPage() {

  const [errorStatus, setErrorStatus] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

 

  const navigate = useNavigate();
  function addLoginHandler(loginData) {
    
    fetch("/login", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(loginData),
    }).then((response) => {
      console.log(response);
      return response.json();
    }).then(responseInJSON => {
      
      console.log(responseInJSON);
      if(responseInJSON.status == -1){
        setErrorStatus(true);
        setErrorMessage(responseInJSON.message);
      }

      else document.cookie = `SessionID=${responseInJSON.JWT}; path=/`;
      
    

    }).catch((error) => {
      if(error.status == -1) {
        console.log("Error Caught");
      }
    });
  }
  
  return (
    <section>
      <div className="login">
        <LoginForm addLoginForm={addLoginHandler} errorStatus={errorStatus} errorMessage={errorMessage}/>
      </div>
    </section>
  );
}
export default LoginPage;
