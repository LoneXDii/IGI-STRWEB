import React from "react";

function ServiceInfo({_id, name, price}){
    return(
        <div>
            <h1>{name}</h1>
            <h2>{price} BYN</h2>
        </div>
    );
}

export default ServiceInfo;