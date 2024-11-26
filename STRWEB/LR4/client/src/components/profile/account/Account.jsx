import React, { useCallback, useEffect, useState } from "react";
import OrdersList from "./items/OrdersList";

function Account({ changeState }) {
    const [decodedPayload, setDecodedPayload] = useState(null);
    const [activeOrders, setActiveOrders] = useState([]);
    const [oldOrders, setOldOrders] = useState([]);

    const [loading, setLoading] = useState(false);

    let active = null;
    let old = null;

    const fetchOrders = useCallback(async () =>{
        setLoading(true);

        const token = localStorage.getItem('JWT');

        const headers = {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        };

        let response = await fetch('http://localhost:3001/api/orders?active=true',{
            method: 'GET',
            headers: headers
        });
        let data = await response.json();
        setActiveOrders(data);

        response = await fetch('http://localhost:3001/api/orders?active=false',{
            method: 'GET',
            headers: headers
        });
        data = await response.json();
        setOldOrders(data);

        setLoading(false);
    }, []);

    useEffect(() =>{
        fetchOrders();
    }, [fetchOrders]);

    useEffect(() => {
        const token = localStorage.getItem('JWT');
        if (!token) {
            changeState('login');
            return; 
        }

        const parts = token.split('.');
        const payload = parts[1];

        try {
            const decoded = JSON.parse(atob(payload.replace(/-/g, '+').replace(/_/g, '/')));
            setDecodedPayload(decoded);
            console.log(decoded);
        } catch (e) {
            changeState('login');
            return;
        }
    }, [changeState]);

    function handleButtonClick() {
        localStorage.removeItem('JWT');
        changeState('login');
    }

    if(loading){
        active = <p>Loading...</p>;
        old = <p>Loading...</p>;
    }
    else{
        active = <OrdersList orders={activeOrders}/>;
        old = <OrdersList orders={oldOrders}/>
    }

    return (
        <div>
            <h1>Аккаунт</h1>
            {decodedPayload ? (
                <h3>Email: {decodedPayload.email}</h3>
            ) : (
                <h3>Загрузка...</h3>
            )}
            <button onClick={handleButtonClick}>Выйти</button>
            <h2>Активные записи:</h2>
            {active}
            <h2>Завершенные записи:</h2>
            {old}
        </div>
    );
}

export default Account;