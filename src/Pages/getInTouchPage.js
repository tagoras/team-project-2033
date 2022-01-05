import GetInTouch from "./Pages/GetInTouch.js";
import { useNavigate } from "react-router-dom";

function GetInTouchPage() {
    const navigate = useNavigate();
    function addMessagetHandler(messageData) {
      console.log(JSON.stringify(messageData));
      fetch("/get-in-touch", {
        method: "POST",
        body: JSON.stringify(messageData),
      }).then(
        (value) => {
          console.log(value);
          navigate("/home");
        },
        () => {
          console.log("ERROR");
          navigate("/home");
        }
      );
    }
    return (
      <section>
        <div className="getintouch">
          <GetInTouch addMessageForm={addMessagetHandler} />
        </div>
      </section>
    );
  }
  export default GetInTouchPage;
  
