import Block from "../UI/Block.js";
import "./FormModules.css";

function loginForm(){
    return <Block>
        <form className={"form"}>
            <div className={"legend"}>Login</div>
            <div className={"control"}>
                <label htmlFor="username">Username</label>
                <input type='text' required id='username'/>
            </div>
            <div className={"control"}>
                <label htmlFor="password">Password</label>
                <input type='text' required id='password'/>
            </div>
            <div className={"actions"}>
                <button>Log in</button>
            </div>
        </form>
    </Block>
}

export default loginForm;