import LoginForm from "../Components/Form/loginForm.js";
import { useNavigate } from "react-router-dom";
function LoginPage() {
  const navigate = useNavigate();
  function addLoginHandler(loginData) {
    console.log(JSON.stringify(loginData));
    fetch("/login", {
      method: "GET",
      body: JSON.stringify(loginData),
    }).then(
      (value) => {
        console.log(value);
        navigate("/Admin");
      },
      () => {
        console.log("ERROR");
        navigate("/Admin");
      }
    );
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
