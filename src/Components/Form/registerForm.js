import Block from ".../UI/Block";
import classes from ".../Form.modules.css";

function registerForm(){
    return <Block>
        <form className={classes.form}>
            <div className={classes.control}>
                <label htmlFor="username">Username</label>
                <input type='text' required id='username'/>
            </div>
            <div className={classes.control}>
                <label htmlFor="password">Password</label>
                <input type='text' required id='password'/>
            </div>
            <div className={classes.control}>
                <label htmlFor="email">Email</label>
                <input type='text' required id='email'/>
            </div>
            <div className={classes.control}>
                <label htmlFor="postcode">Postcode</label>
                <input type='text' required id='postcode'/>
            </div>
            <div className={classes.actions}>
                <button>Submit</button>
            </div>

        </form>
    </Block>
}

export default registerForm;