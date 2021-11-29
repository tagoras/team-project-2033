import react, {Component} from "react";
import photo from '/Users/pvait/team-project-2033/src/Photos/photo7.jpg';
import '../Showcase/Showcase.css';

export class Showcase extends Component{
    render(){
        return(
            <div className="ShowcaseContainer">
                <div className="Filter"/>
                <h1>Let's build <br/> Infrastructure <br/> Together</h1>
            </div>
        )
    }
}