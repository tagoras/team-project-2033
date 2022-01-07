import React from "react";
import data from '../Components/Complaint/Data';
import './Admin.style.css';
import ComplaintCard from "../Components/Complaint/ComplaintCard";
import "../GenericFunctions";
import { sentSyncrhonousAccessRequest } from "../GenericFunctions";
import {navigate} from 'react-router-dom';

function AdminPage(){

    // Sent request for access by sending a cookie JWT
    let accessGranted = sentSyncrhonousAccessRequest("/admin/view_all");
    let booleanValue = true;

    accessGranted.then((responseInJSON) => console.log(responseInJSON));
    let userRole = sentSyncrhonousAccessRequest("/get_role");
    userRole.then((resultInJSON => {
        let role = resultInJSON.role;
        if(role == "admin"){
            console.log("Render successful");
        }  
        else{
            booleanValue = false;
        }
    }));

    if(!booleanValue) return null;

    return(
        <div className="Container">
            <ul className="Grid-Unordered-List">
                {data.map( complaint => {
                    return <li key={complaint.complaintID}><ComplaintCard complaint={complaint}/></li>
                })}
            </ul>
        </div>
    )
    
}

export default AdminPage;