import react from "react";
import { Component } from "react";
import '../Navbar/Navbar.css';
import {Link} from 'react-router-dom';

export class Navbar extends Component{
    render(){
        return(
            <navbar>
                <ul className="NavbarUnorderedList">
                    <li><Link to='/home'>Home</Link></li>
                    <li><a href="#">About Us</a></li>
                    <li><Link to='/register'>Register</Link></li>
                    <li><a href="#">Get In Touch</a></li>
                    <li><Link to='login'>Login</Link></li>
                </ul>
            </navbar>
        )
    }
}