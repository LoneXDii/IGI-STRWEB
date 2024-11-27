import React, { useCallback, useEffect, useState } from "react";
import "../../Profile.css";

function Order({_id, services, doctor}){
    const [loading, setLoading] = useState(true);
    const [specialization, setSpecialization] = useState(null);

    let spec = null;

    const fectchSpecialization = useCallback( async () => {
        setLoading(true);
        const response = await fetch(`http://localhost:3001/api/specializations/${services[0].specialization}`);
        const data = await response.json();
        setSpecialization(data);
        setLoading(false);
    }, []);

    useEffect(() => {
        fectchSpecialization();
    }, fectchSpecialization);

    if(loading){
        spec = 'Loading...';
    }
    else{
        spec = specialization.name;
    }

    return(
        <li className="order-item">
            <h3>{services[0].name} ({spec}) {services[0].price} BYN</h3>
            <h3>{doctor.surname} {doctor.first_name} {doctor.last_name}</h3>
        </li>
    );
}

export default Order;