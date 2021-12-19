import { React } from "react";
import "./AboutUs.style.css";
import { Link } from "react-router-dom";

export const AboutUs = () => {
  return (
    <div className="aboutUsContainer">
      <div className="contentHolder">
        <h1>About Us</h1>
        <p>
          <span className="organizationName">[NAME]</span> is an organization that helps The Government of the United
          Kingdom to better tackle infrastructure issues by allowing direct
          communication with it's citizens.
        </p>
        <p>
          Here you can submit infrastructure complaints that you would like to be addressed at a local level.
        </p>
        <Link to="/register"><a className="Button-1" href="/home">Get Started</a></Link>
        
      </div>
    </div>
  );
};

export default AboutUs;
