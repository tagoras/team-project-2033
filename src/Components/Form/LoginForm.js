import Block from "../UI/Block.js";
import "./FormModules.css";
import {useRef} from 'react';

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
    <div className="registrationContainer">
        <form className="form" onSubmit={loginSubmitHandler}>
            <div className="legend">Login</div>
            <div className="control">
                <input type='text' required id='username' placeholder='Username' ref={usernameInputRef}/>
            </div>
            <div className="control">
                <input type='text' required id='password' placeholder='********' ref={passwordInputRef}/>
            </div>
            <div className="actions">
                <button>Log in</button>
            </div>
        </form>
    </div>
    );
}

export default LoginForm;