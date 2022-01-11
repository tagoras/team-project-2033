import {react} from 'react';
import './ErrorBox.style.css';

export function ErrorBox(props){
    if(props.errorOccurred){
        return(
            <div className='container'>
                <p>{props.text}</p>
            </div>
        )
    }
    return null;
}

export default ErrorBox;