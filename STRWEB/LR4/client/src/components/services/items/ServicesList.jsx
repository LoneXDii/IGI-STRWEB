import React from "react";
import '../Services.css';
import Service from "./Service";

function ServicesList(data){
    const items = data.data.map(service => <Service key={service._id} {...service} />);

    return(
        <div>
            <ul className="services">
                {items}
            </ul>
        </div>
    );
}

export default ServicesList;