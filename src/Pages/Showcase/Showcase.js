import react, { Component } from "react";
import "../../Components/Photos/photo7.jpg";
import "./Showcase.css";
import AboutUs from "../../Components/AboutUsSection/AboutUs";
import { Navbar } from "../../Components/Navbar/Navbar";
import Footer from "../../Components/Footer/Footer.component";

export class Showcase extends Component {
  render() {
    return (
      <div>
      <Navbar/>
        <div className="ShowcaseContainer">
          <div className="Filter" />
          <h1>
            Building <br /> Infrastructure <br /> With <br /> People
          </h1>
        </div>
        <AboutUs />
        <Footer/>
      </div>
    );
  }
}
