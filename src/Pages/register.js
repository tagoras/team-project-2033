import RegisterForm from "../Components/Form/registerForm.js";
import "../Pages/Register.css"
function RegisterPage(){
    function addRegisterHandler(registerData){
        //FIXME: connect to the database
        console.log(JSON.stringify(registerData))
        fetch('/register2',{
            method:'POST',
            body: JSON.stringify(registerData)
        }).then((value) => console.log(value), () => console.log("ERROR"));
    }
    return <section>
        <div className="register">
        <RegisterForm addRegisterForm={addRegisterHandler}/>
        </div>
        
    </section>;
}
export default RegisterPage;