import LoginForm from "../Components/Form/LoginForm.js";
function LoginPage (){
    function addLoginHandler(loginData){
        console.log(JSON.stringify(loginData))
        fetch('/login',{
            method:'GET',
            body: JSON.stringify(loginData)
        }).then((value) => console.log(value), () => console.log("ERROR"));
    }
     return <section>
        <div className="login">
        <LoginForm addLoginForm={addLoginHandler}/>
        </div>
     </section>;
    
}
export default LoginPage;
