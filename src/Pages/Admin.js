import React from "react";
import data from '../Components/Complaint/Data';
import './Admin.style.css';
import ComplaintCard from "../Components/Complaint/ComplaintCard";
import "../GenericFunctions";
import { sentSyncrhonousAccessRequest } from "../GenericFunctions";

function AdminPage(){

    // Sent request for access by sending a cookie JWT
    let accessGranted = sentSyncrhonousAccessRequest("/admin");

    accessGranted.then((resultInJSON => {console.log(resultInJSON)}, (Error) => console.log(Error)));
    // If access denied -> Render Error Page;
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