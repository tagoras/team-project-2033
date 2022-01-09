import "./Login.style.css";
import {useRef,useState} from 'react';
import backgroundImage from "../Photos/x.jpg";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEye } from "@fortawesome/free-solid-svg-icons";
import {ErrorBox} from '../ErrorBox/ErrorBox';

const eye = <FontAwesomeIcon icon={faEye} />;

function LoginForm(props){
    const [passwordShown, setPasswordShown] = useState(false);
    const togglePasswordVisibility = () =>{
        setPasswordShown(passwordShown ? false:true);
    }
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
        <div className="filter"></div>
        <div className="loginFormContainer">
        
        <form className="form" onSubmit={loginSubmitHandler}>
            <div className="title">Login</div>
            <div className="loginInput">
                <input type='text' required id='username' placeholder='Username' ref={usernameInputRef}/>
            </div>
            <div className="loginInput">
                <input
                  type={passwordShown ? "text" : "password"}
                  required id='password'
                  placeholder='********' 
                  ref={passwordInputRef}
                  />
                <i onClick={togglePasswordVisibility}>{eye}</i>{" "}
            </div>
            <ErrorBox errorOccurred={props.errorStatus} text={props.errorMessage}/>
            <div className="loginSubmit">
                <button>Log in</button>
            </div>
        </form>
      
        </div>
    </div>
    );
}

export default LoginForm;