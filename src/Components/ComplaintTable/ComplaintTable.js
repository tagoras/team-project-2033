import react from "react";
import './ComplaintTable.style.css';
import data from './ComplaintData';

export function ComplaintTable(){
    return(
        <div className="mainContainer">
            <div className="complaintTableContainer">
                <table className="complaintTable">
                    <tr>
                        <th>Complaint ID</th>
                        <th>Submitted By</th>
                        <th>Complaint Message</th>
                        <th>Complaint Picture</th>
                        <th>View Complaint</th>
                    </tr>
                    {data.map( (item, index, array) => {
                    return(
                        <tr key = {item.id}>
                         <td>{item.id}</td>
                         <td>{item.subbmitBy}</td>
                         <td>{item.complaintMessage}</td>
                         <td>{item.complaintPicture}</td>
                        </tr>
                    )
                    })}
                </table>
            </div>
        </div>
    )
}

export default ComplaintTable;