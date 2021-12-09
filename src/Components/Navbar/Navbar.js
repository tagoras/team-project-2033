import react from "react";
import { Component } from "react";
import '../Navbar/Navbar.css';
import {Link} from 'react-router-dom';

export class Navbar extends Component{
    render(){
        return(
            <navbar>
                <ul className="NavbarUnorderedList">
                    <li><a href="">Home</a></li>
                    <li><a href="">About Us</a></li>
                    <li><a href="">Get Started</a></li>
                    <li><a href="">Get In Touch</a></li>
                </ul>
            </navbar>
        )
    }
}