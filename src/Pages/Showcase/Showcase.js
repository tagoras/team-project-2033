import react, { Component } from "react";
import "../../Components/Photos/photo7.jpg";
import "./Showcase.css";
import AboutUs from "../../Components/AboutUsSection/AboutUs";

export class Showcase extends Component {
  render() {
    return (
      <div>
        <div className="ShowcaseContainer">
          <div className="Filter" />
          <h1>
            Building <br /> Infrastructure <br /> With <br /> People
          </h1>
        </div>
        <AboutUs />
      </div>
    );
  }
}
