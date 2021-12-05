import RegisterForm from "../Components/Form/registerForm.js";
import "../Pages/Register.css"
function RegisterPage(){
    function addRegisterHandler(registerData){
        
      //  fetch('database url',{
      //      method:'POST',
      //      body: JSON.stringify(registerData)
      //  })
    }
    return <section>
        <div className={"register"}>
        <RegisterForm addRegisterForm={addRegisterHandler}/>
        </div>
        
    </section>;
}
export default RegisterPage;