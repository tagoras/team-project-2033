import Block from "../UI/Block.js";
import "./FormModules.css";

function registerForm(){
    return <Block>
        <form className={"form"}>
            <div className={"legend"}>Registration Form</div>
            <div className={"control"}>
                <label htmlFor="username">Username</label>
                <input type='text' required id='username'/>
            </div>
            <div className={"control"}>
                <label htmlFor="password">Password</label>
                <input type='text' required id='password'/>
            </div>
            <div className={"control"}>
                <label htmlFor="email">Email</label>
                <input type='text' required id='email'/>
            </div>
            <div className={"control"}>
                <label htmlFor="postcode">Postcode</label>
                <input type='text' required id='postcode'/>
            </div>
            <div className={"actions"}>
                <button>Submit</button>
            </div>
        </form>
    </Block>
}

export default registerForm;