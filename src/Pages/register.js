import RegisterForm from "../Components/Form/registerForm.js";
import "../Pages/Register.css";
import { useNavigate } from "react-router-dom";

function RegisterPage() {
  const navigate = useNavigate();
  function addRegisterHandler(registerData) {
    console.log(JSON.stringify(registerData));
    fetch("/register2", {
      method: "POST",
      body: JSON.stringify(registerData),
    }).then(
      (value) => {
        console.log(value);
        navigate("/login");
      },
      () => console.log("ERROR")
    );
  }
  return (
    <section>
      <div className="register">
        <RegisterForm addRegisterForm={addRegisterHandler} />
      </div>
    </section>
  );
}
export default RegisterPage;
