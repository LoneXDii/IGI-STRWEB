import React from "react";
import Order from "./Order";

function OrdersList(orders){
    const items = orders.orders.map(o => <Order key={o._id} {...o}/>)
    return(
        <div>
            <ul>
                {items}
            </ul>
        </div>
    );
}

export default OrdersList;