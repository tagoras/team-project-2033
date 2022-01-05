import LoginForm from "../Components/Form/loginForm.js";
import { useNavigate } from "react-router-dom";
function LoginPage() {
  const navigate = useNavigate();
  function addLoginHandler(loginData) {
    console.log(JSON.stringify(loginData));
    fetch("/login", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(loginData),
    }).then(
      (responseObject) => {
        console.log(responseObject.status);
        return responseObject.json();
      },
      (ErrorObject) => {
        console.log(ErrorObject);
      }
    ).then(responseInJSON => {
      console.log(responseInJSON);
<<<<<<< HEAD
      document.cookie = `SessionID=${responseInJSON.JWT}; path=/`;
=======

      document.cookie = `SessionID=${responseInJSON.JWT}`;
>>>>>>> 196f9b14e8ec02358edaee77f9c843dbd8fecb5d
      if(responseInJSON.status == -1) console.log("Bad Login");
      else console.log("");

      console.log(document.cookie.substring(10));

    });
  }
  return (
    <section>
      <div className="login">
        <LoginForm addLoginForm={addLoginHandler} />
      </div>
    </section>
  );
}
export default LoginPage;
