import Block from "../UI/Block.js";


function loginForm(){
    return (
    <Block>
        <form className={"form"}>
            <div className={"legend"}>Login</div>
            <div className={"control"}>
                <input type='text' required id='username' placeholder='Username'/>
            </div>
            <div className={"control"}>
                <input type='text' required id='password' placeholder='********'/>
            </div>
            <div className={"actions"}>
                <button>Log in</button>
            </div>
        </form>
    </Block>
    );
}

export default loginForm;