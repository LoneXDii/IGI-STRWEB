import React, { useEffect, useState } from "react";
import '../Services.css';
import { useNavigate } from "react-router-dom";

function Service({name, price, _id}){
    const navigate = useNavigate();
    const [isDisabled, setDisabled] = useState(false);

    useEffect(() => {
        if (!localStorage.getItem('JWT')) {
            setDisabled(true);
        }
    }, []); 

    function handleOnClick(){

    };

    return(
        <li id={_id}>
            <h2>{name}</h2>
            <h2>{price} BYN</h2>
            <button type="button" 
                className={isDisabled? "disabled-button" : "enabled-button"}
                onClick={handleOnClick} disabled={isDisabled}>
                Записаться
            </button>
        </li>
    );
}

export default Service;