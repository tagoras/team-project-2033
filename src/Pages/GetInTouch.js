import react, { Component } from "react";
import backgroundImage from "../Components/Photos/x.jpg";
import "./GetInTouch.css";
import {FaPhone, FaEnvelope} from 'react-icons/fa';
export class GetInTouch extends Component{
    render(){
        return(
            <div className="body">
                <img src={backgroundImage}></img>
                <h1 className="getintouch">Get In Touch</h1>
                <p>Our team is ready to hear from you</p>
                <div className='contact-container'>
                    <div className="contact-info">
                        <h4>Contact info</h4>
                        <p>Fill out the form with any of your queries and click submit</p>
                        <div className="icon-text">
                            <FaPhone className="icon"/>
                            <span>+44 1632 960709</span>
                        </div>
                        <div className="icon-text">
                            <FaEnvelope className="icon"/>
                            <span>business@email.com</span>
                        </div>
                    </div>
                    <form>
                        <div className="col">
                            <div className="form-group">
                                <label>Name</label>
                                <input type='text'/>
                            </div>
                            <div className="form-group">
                                <label>Email</label>
                                <input type='text'/>
                            </div>
                        </div>
                        <div className="col">
                            <div className="form-group">
                                    <label>Type your message here</label>
                                    <textarea type='text'/>
                                </div>
                        </div>
                        <button className="submit">Submit</button>
                    </form>
                </div>
            </div>
        )
    }

}
export default GetInTouch;