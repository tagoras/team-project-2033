import react, { Component } from "react";
import photo from "../Photos/photo7.jpg";
import "./Showcase.css";
import AboutUs from "../AboutUsSection/AboutUs";

export class Showcase extends Component {
  render() {
    return (
      <div>
        <div className="ShowcaseContainer">
          <div className="Filter"/>
          <img src={photo} className="BackgroundPicture"/>
          <h1>
            Building <br /> Infrastructure <br /> With <br /> People
          </h1>
        </div>
        <AboutUs />
      </div>
    );
  }
}
