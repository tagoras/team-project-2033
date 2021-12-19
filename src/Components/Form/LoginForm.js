import "./Login.style.css";
import {useRef} from 'react';
import backgroundImage from "../Photos/x.jpg";

function LoginForm(props){
    const usernameInputRef = useRef();
    const passwordInputRef = useRef();
    function loginSubmitHandler(event){
        event.preventDefault();
        const enteredUsername = usernameInputRef.current.value;
        const enteredPassword = passwordInputRef.current.value;
        const loginData={
            username: enteredUsername,
            password: enteredPassword,
        }
        props.addLoginForm(loginData);

    }
    return (
    <div className="mainContainer">
        <img src={backgroundImage}></img>
        <div className="filter2"></div>
        <div className="loginFormContainer">
        
        <form className="form" onSubmit={loginSubmitHandler}>
            <div className="title">Login</div>
            <div className="loginInput">
                <input type='text' required id='username' placeholder='Username' ref={usernameInputRef}/>
            </div>
            <div className="loginInput">
                <input type='text' required id='password' placeholder='********' ref={passwordInputRef}/>
            </div>
            <div className="loginSubmit">
                <button>Log in</button>
            </div>
        </form>
      
        </div>
    </div>
    );
}

export default LoginForm;