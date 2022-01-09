import React from "react";
import data from '../Components/Complaint/Data';
import './Admin.style.css';
import ComplaintCard from "../Components/Complaint/ComplaintCard";
import "../GenericFunctions";
import { sentSyncrhonousAccessRequest } from "../GenericFunctions";
import {navigate} from 'react-router-dom';

function AdminPage(){

    // Have no idea why this request is bad
    let complaints =  sentSyncrhonousAccessRequest("/admin/view_all", "POST");
    complaints.then((text) => console.log(text));

    return(
        <div className="Container">
            <ul className="Grid-Unordered-List">
                
            </ul>
        </div>
    )
    
}

export default AdminPage;