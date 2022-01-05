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
      if(responseInJSON.status == -1) navigate("/home");
      else navigate("/Admin");
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
