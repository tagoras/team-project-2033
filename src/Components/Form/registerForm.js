import Block from "../UI/Block.js";
import "./Register.style.css";
import {useRef} from 'react';
import backgroundImage from '../Photos/x.jpg';

function RegisterForm(props){
    const usernameInputRef = useRef();
    const passwordInputRef = useRef();
    const emailInputRef = useRef();
    const postcodeInputRef = useRef();

    function registerSubmitHandler(event) {
        event.preventDefault();
        const enteredUsername = usernameInputRef.current.value;
        const enteredPassword = passwordInputRef.current.value; 
        const enteredEmail = emailInputRef.current.value;
        const enteredPostcode = postcodeInputRef.current.value;
        const registerData ={
            username: enteredUsername,
            password: enteredPassword,
            email: enteredEmail,
            postcode: enteredPostcode,

        }
       props.addRegisterForm(registerData);
    }

    return (
    <div className="containerContainer">
        <img src={backgroundImage} className="backgroundImage"></img>
        <div className="filter"></div>
        <div className="formContainer">
            <form className="form" onSubmit={registerSubmitHandler}>
            <div className="legend">Register</div> 
            <div className="control">
                <label htmlFor="username">Username</label> <br/>
                <input type='text' required id='username' ref={usernameInputRef}/>
            </div>
            <div className="control">
                <label htmlFor="password">Password</label> <br/>
                <input type='text' required id='password' placeholder='********' ref={passwordInputRef}/>
            </div>
            <div className="control">
                <label htmlFor="email">Email</label> <br/>
                <input type='text' required id='email' placeholder='name@email.com' ref={emailInputRef}/>
            </div>
            <div className="control"> 
                <label htmlFor="postcode">Postcode</label> <br/>
                <input type='text' required id='postcode' placeholder='e.g. NE4 5TG' ref={postcodeInputRef}/>
            </div>
            <div className="actions">
                <button className="submitButton">Submit</button>
            </div>
        </form>
    </div>
    </div>
    );
}

export default RegisterForm;