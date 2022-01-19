
import { useNavigate } from 'react-router-dom';
import { Showcase } from '../../Components/Showcase/Showcase';

export const Logout = () => {
    console.log(document.cookie)
    document.cookie = `SessionID="";max-age=-1; path=/`;
    return <Showcase/>;
}