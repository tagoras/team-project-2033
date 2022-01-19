import react from "react";
import {Component} from "react";
import '../Navbar/Navbar.css';
import {Link, useNavigationType} from 'react-router-dom';
import {sentSyncrhonousAccessRequest} from "../../GenericFunctions";
import {useState} from "react/cjs/react.development";

export function Navbar() {
    const [admin, setAdmin] = useState("user");

    sentSyncrhonousAccessRequest('/get_role', 'GET').then((jsonResult) => {
        console.log(admin);
        setAdmin(jsonResult.role);
    })

    return (
        <nav>
            <ul className="NavbarUnorderedList">
                <li><Link to='/home'>Home</Link></li>
                <li><Link to='/register'>Register</Link></li>
                {
                    admin == 'admin' ? <li><Link to='/Admin'>Admin</Link></li> : <li><Link to='/login'>Login</Link></li>
                }
            </ul>
            </nav>
        )

}