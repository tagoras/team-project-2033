import LoginForm from "../Components/Form/LoginForm.js";
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
        /*
           TODO: add a link from login page to someother page 
            navigate('/somepage');
           */
      },
      () => console.log("ERROR")
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
