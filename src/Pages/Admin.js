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

    accessGranted.catch((responseInJSON) => console.log(responseInJSON));


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