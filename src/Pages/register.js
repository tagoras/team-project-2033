import RegisterForm from "../Components/Form/RegisterForm.js";
import "../Pages/Register.css";
import { useNavigate } from "react-router-dom";

function RegisterPage() {

  const navigate = useNavigate();

  function addRegisterHandler(registerData) {
    console.log(JSON.stringify(registerData));
    fetch("/register", {
      method: "POST",
      body: JSON.stringify(registerData),
    }).then(
      (response) => navigate("/login"),
      (error) => console.log("ERROR")
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
