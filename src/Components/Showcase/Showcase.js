import react, {Component} from "react";
import photo from '/Users/pvait/team-project-2033/src/Photos/photo7.jpg';

export class Showcase extends Component{
    render(){
        return(
            <div>
                <img src={photo}></img>
            </div>
        )
    }
}