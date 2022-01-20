import React from "react";
import data from '../../Components/Complaint/Data';
import './Admin.style.css';
import ComplaintCard from "../../Components/Complaint/ComplaintCard";
import "../../GenericFunctions";
import { sentSyncrhonousAccessRequest } from "../../GenericFunctions";
import {navigate} from 'react-router-dom';
import {useState} from 'react';
import {useNavigate} from 'react-router-dom';

function AdminPage() {

    let [pageRefreshedTimes, setPageRefreshedTimes] = useState(0);
    let [data, setData] = useState([]);

   

    let navigate = useNavigate();
    let result = sentSyncrhonousAccessRequest('/get_role', 'GET').then((jsonResult) => {
        if (jsonResult.role != 'admin') {
            console.log(jsonResult.role);
            navigate('/login');
        }
    })

    //This function executes properly
    function deleteComplaint(id) {
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

   
    let urls;
    if(pageRefreshedTimes == 0){
      let complaints = sentSyncrhonousAccessRequest("/admin/view_all", "POST");

      let array = [];
       urls = [];
      complaints.then((resultInJSON) => {
        console.log(resultInJSON);
        array = resultInJSON['list of complaints'];
        setData(array);
      })
  

      setPageRefreshedTimes(++pageRefreshedTimes);
    }

    return(
        <div className="AdminMainContainer">
          <div className="CardMainContainer">
          {data.map((item, index, array) => {
            return <ComplaintCard key={index} id={index} complaint={item} handleDelete={deleteComplaint}/>
          })}
          </div>
        </div>
        
    )
    
}

export default AdminPage;