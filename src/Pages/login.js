import LoginForm from "../Components/Form/loginForm.js";
import { useNavigate } from "react-router-dom";
import {useState} from 'react';
import {sentSyncrhonousAccessRequest} from "../GenericFunctions";

function LoginPage() {

  const [errorStatus, setErrorStatus] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

 

  const navigate = useNavigate();
  async function addLoginHandler(loginData) {
    
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

      
      document.cookie = `SessionID=${responseInJSON.JWT}; path=/`;
      let access = sentSyncrhonousAccessRequest("/get_role", "GET")
      access.then((response) => {
        if(response.role == 'user') navigate("/User");
        else if(response.role == 'admin') navigate("/admin");
      });
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
