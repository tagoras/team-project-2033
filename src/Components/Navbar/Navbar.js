import react from "react";
import { Component } from "react";
import '../Navbar/Navbar.css';

export class Navbar extends Component{
    render(){
        return(
            <navbar>
                <ul className="NavbarUnorderedList">
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Login</a></li>
                    <li><a href="#">Get In Touch</a></li>
                </ul>
            </navbar>
        )
    }
}