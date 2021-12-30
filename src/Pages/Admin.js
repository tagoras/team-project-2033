import React from "react";
import data from '../Components/Complaint/Data';
import './Admin.style.css';
import ComplaintCard from "../Components/Complaint/ComplaintCard";

function AdminPage(){
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