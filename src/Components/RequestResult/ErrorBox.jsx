import './ErrorBox.style.css';

const ErrorBox = (props) => {
    if(props.errorOccured){
        return(
            <div className='errorBox'>
                <p>{props.message}</p>
            </div>
        )
    }
    return null;
}

export default ErrorBox;