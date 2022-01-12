import React from "react";
import data from '../../Components/Complaint/Data';
import './Admin.style.css';
import ComplaintCard from "../../Components/Complaint/ComplaintCard";
import "../../GenericFunctions";
import { sentSyncrhonousAccessRequest } from "../../GenericFunctions";
import {navigate} from 'react-router-dom';
import {useState}  from 'react';

function AdminPage(){

  let [data, setData] = useState([]);
  console.log(data);

    // WORKS!
    // let complaints =  sentSyncrhonousAccessRequest("/admin/view_all", "POST");
    // complaints.then((text) => console.log(text));

    // WORKS!
    // let objectToSend = {
    //     method: `DELETE`,
    //     headers: {
    //       'Content-Type': 'application/json;charset=utf-8',
    //       'Authorization': `Bearer ${document.cookie.substring(10)}`
    //     },
    //     id: 1
    //   }
    
    // //console.log(JSON.stringify(objectToSend));
    // console.log(JSON.parse(JSON.stringify(objectToSend)));
    // let result = fetch(`/admin/delete`, {
    //     method: `DELETE`,
    //     headers: {
    //       'Content-Type': 'application/json;charset=utf-8',
    //       'Authorization': `Bearer ${document.cookie.substring(10)}`
    //     },
    //     body: JSON.stringify({id: 9})
    //   });

    // result.then((response) => response.text()).then((response) => console.log(response));

    //Testing Edit
    //

    if(data.length == 0){
      let complaints = sentSyncrhonousAccessRequest("/admin/view_all", "POST");

      let array = [];
  
      complaints.then((resultInJSON) => {
        array = resultInJSON['list of complaints'];
        console.log(array);
        setData(array);
      })
  
      console.log(complaints);
    }
    

    return(
        <div>
          {data.map((item, index, array) => {
            return <h1>{item.id}</h1>
          })}
        </div>
    )
    
}

export default AdminPage;