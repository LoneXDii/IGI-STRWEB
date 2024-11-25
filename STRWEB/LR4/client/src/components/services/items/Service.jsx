import React from "react";
import '../Services.css';
import { useNavigate } from "react-router-dom";

function Service({name, price, _id}){
    const navigate = useNavigate();

    function handleOnClick(){

    };

    return(
        <li id={_id}>
            <h2>{name}</h2>
            <h2>{price} BYN</h2>
            <button type="button" onClick={handleOnClick}>
                Записаться
            </button>
        </li>
    );
}

export default Service;