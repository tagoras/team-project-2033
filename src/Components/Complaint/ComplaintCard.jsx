import react from "react";
import './ComplaintCard.style.css';
import photo from '../Photos/test.jpg';

export function ComplaintCard(props){
    // import {photo} from `../../../api/data/2/a52149b3-b0fa-40c7-a99b-6c61ba1c849c.png`;
    // console.log(props.complaint.url);
    console.log(props.complaint.id);
    return(
        <div className="ComplaintContainer">
            <img className="ComplaintCardImage" src={props.complaint.url}/>
            <h3 className="ComplaintInfo">#{props.complaint.id}</h3>
            <p className="ComplaintInfo ComplaintText">{props.complaint.name}</p>
            <p className="ComplaintInfo">{props.complaint.date}</p>
            <p>{props.complaint.description}</p>
            <div className="ComplaintIconHolder">
                <i className="fas fa-trash ComplaintInfo fa-2x" onClick={() => props.handleDelete(props.id)}></i>
            </div>
        </div>
    )
}

export default ComplaintCard;