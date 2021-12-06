import RegisterForm from "../Components/Form/registerForm.js";
import "../Pages/Register.css"
function RegisterPage(){
    function addRegisterHandler(registerData){
        //FIXME: connect to the database
        fetch('mongodb://cs-db.ncl.ac.uk:3306/csc2033_team32',{
            method:'POST',
            body: JSON.stringify(registerData)
        })
    }
    return <section>
        <div className={"register"}>
        <RegisterForm addRegisterForm={addRegisterHandler}/>
        </div>
        
    </section>;
}
export default RegisterPage;