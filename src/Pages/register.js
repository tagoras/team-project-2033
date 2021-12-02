import registerForm from "../Components/Form/registerForm.js";
import "../Pages/Register.css"
function registerPage(){
    return <section>
        <div className={"register"}>
        {registerForm()}
        </div>
        
    </section>;
}
export default registerPage;