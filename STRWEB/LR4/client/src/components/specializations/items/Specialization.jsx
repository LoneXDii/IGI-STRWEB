import React from 'react';
import '../Specializations.css';

function Specialization({name, normalized_name, _id}) {
    return (
        <li id={_id}>
            <h2>{name}</h2>
        </li>
    );
};

export default Specialization;