import react from "react";
import './SearchBar.style.css';

export function SearchBar(props){
    return(
        <div>
            <form className="SearchForm">
                <label>Enter complaint details</label>
                <input type="text" className="SearchBarInput" onInput={(e) => props.changePattern(e.target.value)}></input>
            </form>
        </div>
    )
}