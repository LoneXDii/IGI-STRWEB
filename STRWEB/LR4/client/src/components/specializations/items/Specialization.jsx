import React from 'react';
import '../Specializations.css';
import { useNavigate } from 'react-router-dom';

function Specialization({name, normalized_name, _id}) {
    const navigate = useNavigate();

    function handleOnClick(){
        navigate(`/services/${_id}`);
    };

    return (
        <li id={_id} onClick={handleOnClick}>
            <h2>{name}</h2>
        </li>
    );
};

export default Specialization;