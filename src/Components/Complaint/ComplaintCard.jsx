import react from "react";
import './ComplaintCard.style.css';
import photo from '../Photos/test.jpg';

export function ComplaintCard(props){
    console.log(props.id);
    return(
        <div className="ComplaintContainer">
            <img className="ComplaintCardImage" src={photo}/>
            <h3 className="ComplaintInfo">#{props.id}</h3>
            <p className="ComplaintInfo ComplaintText">{props.complaint.name}</p>
            <p className="ComplaintInfo">{props.complaint.date}</p>
            <div className="ComplaintIconHolder">
                <i className="fas fa-trash ComplaintInfo fa-2x" onClick={() => props.handleDelete(props.id)}></i>
            </div>
        </div>
    )
}

export default ComplaintCard;