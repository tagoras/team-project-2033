import Block from "../UI/Block.js";
import "./FormModules.css";
import {useRef} from 'react';

function RegisterForm(props){
    const usernameInputRef = useRef();
    const passwordInputRef = useRef();
    const emailInputRef = useRef();
    const postcodeInputRef = useRef();

    function submitHandler(event) {
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

    return (<Block>
        <form className={"form"} onSubmit={submitHandler}>
            <div className={"legend"}>Register</div>
            <div className={"control"}>
                <label htmlFor="username">Username</label>
                <input type='text' required id='username' ref={usernameInputRef}/>
            </div>
            <div className={"control"}>
                <label htmlFor="password">Password</label>
                <input type='text' required id='password' placeholder='********' ref={passwordInputRef}/>
            </div>
            <div className={"control"}>
                <label htmlFor="email">Email</label>
                <input type='text' required id='email' placeholder='name@email.com' ref={emailInputRef}/>
            </div>
            <div className={"control"}>
                <label htmlFor="postcode">Postcode</label>
                <input type='text' required id='postcode' placeholder='e.g. NE4 5TG' ref={postcodeInputRef}/>
            </div>
            <div className={"actions"}>
                <button>Submit</button>
            </div>
        </form>
    </Block>);
}

export default RegisterForm;