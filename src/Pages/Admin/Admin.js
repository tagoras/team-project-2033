import React from "react";
import data from '../../Components/Complaint/Data';
import './Admin.style.css';
import ComplaintCard from "../../Components/Complaint/ComplaintCard";
import "../../GenericFunctions";
import { sentSyncrhonousAccessRequest } from "../../GenericFunctions";
import {navigate} from 'react-router-dom';
import {useState}  from 'react';

function AdminPage(){

  let [pageRefreshedTimes, setPageRefreshedTimes] = useState(0);
  let [data, setData] = useState([]);

  console.log(data);

  //This function executes properly
  function deleteComplaint(id){
    console.log("Deleting complaint with id of " + id);
    fetch(`/admin/delete`, {
          method: `DELETE`,
          headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': `Bearer ${document.cookie.substring(10)}`
          },
          body: JSON.stringify({id: id + 1})
    }).then((value) => value.json()).then((jsonRes) => console.log(jsonRes));

    //setPageRefreshedTimes(0);
  }

    // WORKS!
    // let complaints =  sentSyncrhonousAccessRequest("/admin/view_all", "POST");
    // complaints.then((text) => console.log(text));

   

    if(pageRefreshedTimes == 0){
      let complaints = sentSyncrhonousAccessRequest("/admin/view_all", "POST");

      let array = [];
  
      complaints.then((resultInJSON) => {
        array = resultInJSON['list of complaints'];
        console.log(array);
        setData(array);
      })
  
      console.log(data);
      setPageRefreshedTimes(++pageRefreshedTimes);
    }
    

    return(
        <div className="AdminMainContainer">
          {data.map((item, index, array) => {
            return <ComplaintCard key={index} id={index} complaint={item} handleDelete={deleteComplaint}/>
          })}
        </div>
    )
    
}

export default AdminPage;