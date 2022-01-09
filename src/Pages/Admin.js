import React from "react";
import data from '../Components/Complaint/Data';
import './Admin.style.css';
import ComplaintCard from "../Components/Complaint/ComplaintCard";
import "../GenericFunctions";
import { sentSyncrhonousAccessRequest } from "../GenericFunctions";
import {navigate} from 'react-router-dom';

function AdminPage(){

    // WORKS!
    // let complaints =  sentSyncrhonousAccessRequest("/admin/view_all", "POST");
    // complaints.then((text) => console.log(text));

    let objectToSend = {
        method: `DELETE`,
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'Authorization': `Bearer ${document.cookie.substring(10)}`
        },
        id: 1
      }
    
    //console.log(JSON.stringify(objectToSend));
    console.log(JSON.parse(JSON.stringify(objectToSend)));
    let result = fetch(`/api/admin/delete`, {
        method: `POST`,
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'Authorization': `Bearer ${document.cookie.substring(10)}`
        },
        body: JSON.stringify({id: 5})
      });

    result.then((response) => response.text()).then((response) => console.log(response));

    return(
        <div className="Container">
            <ul className="Grid-Unordered-List">
                
            </ul>
        </div>
    )
    
}

export default AdminPage;