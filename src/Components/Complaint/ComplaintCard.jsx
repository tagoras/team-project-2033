import react from "react";
import "./ComplaintCard.style.css";
import photo from "../Photos/photo7.jpg";

export function ComplaintCard(props) {

  return (
    <div className="CardContainer">
      <img className="ComplaintImage" src={photo}/>
      <h3>{props.complaintObject.id}</h3>
      <p>{props.complaintObject.title}</p>
      <p>{props.complaintObject.date}</p>
    </div>
  );
}

export default ComplaintCard;
