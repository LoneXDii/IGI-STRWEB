import React from "react";

function Order({_id, services, doctor}){
    return(
        <li>
            <h2>{services[0].name} {services[0].price} BYN</h2>
            <h2>{doctor.surname} {doctor.first_name} {doctor.last_name}</h2>
        </li>
    );
}

export default Order;