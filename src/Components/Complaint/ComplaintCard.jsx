import react from "react";
import './ComplaintCard.style.css';
import photo from '../Photos/photo7.jpg';

export function ComplaintCard(props){
    console.log(props.complaint.id);
    return(
        <div className="complaintContainer">
            <img src={photo}></img>
            <div className="filter"></div>
            <div className="aboveFilterContent">
            <h1>{props.complaint.title}</h1>
            </div>
        </div>
    )
}

export default ComplaintCard;