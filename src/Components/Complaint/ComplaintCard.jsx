import react from "react";
import "./ComplaintCard.style.css";
import photo from "../Photos/photo7.jpg";

export function ComplaintCard() {

  return (
    <div class="MainContainer">
      <div class="CardContainer">
        <img src="./images/image-equilibrium.jpg" class="EquilibrumImage" />
        <div class="TextContainer">
          <h2 class="OnHoverChangeColor">Equilibrium #3429</h2>
          <span>
            Our Equilibrium collection promotes <br /> balance and calm.
          </span>
        </div>

        <div class="FaviconTimeContainer">
          <div>
            <img src="./images/icon-ethereum.svg" class="EthereumImage" />
            <span>0.041 ETH</span>
          </div>
          <div class="SecondChild">
            <img src="./images/icon-clock.svg" class="ClockImage" />
            <span>3 days left</span>
          </div>
        </div>
        <hr />

        <div class="AvatarNameContainer">
          <img src="./images/image-avatar.png" />
          <p>
            <span class="BlueText">Creation of </span>{" "}
            <span class="OnHoverChangeColor">Jules Wyvern</span>
          </p>
        </div>
      </div>
    </div>
  );
}

export default ComplaintCard;
