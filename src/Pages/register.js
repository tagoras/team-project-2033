import RegisterForm from "../Components/Form/RegisterForm.js";
import "../Pages/Register.css";
import { useNavigate } from "react-router-dom";
import { useState } from "react";

function RegisterPage() {

  let [status, updateStatus] = useState({});

  const navigate = useNavigate();

  async function addRegisterHandler(registerData) {
    console.log(JSON.stringify(registerData));
    let response = await fetch("/register", {
      method: "POST",
      body: JSON.stringify(registerData),
    })

    let jsonResponse = await response.json();
    
    console.log(jsonResponse);
    
    updateStatus(status = {statusCode: jsonResponse.status, message: jsonResponse.message});
    console.log(`${status.statusCode} -- ${status.message}`);
    if(status.statusCode != -1) navigate('/login');
  }

  return (
    <section>
      <div className="register">
        <RegisterForm addRegisterForm={addRegisterHandler} errorOccurred = {status.statusCode == -1} errorText={status.message}/>
      </div>
    </section>
  );
}
export default RegisterPage;
