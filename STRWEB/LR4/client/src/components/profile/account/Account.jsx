import React, { useEffect } from "react";

function Account({changeState}){
    useEffect(() => {
        const token = localStorage.getItem('JWT');
        if (!token) {
            changeState('login');
            return; 
        }

        const parts = token.split('.');

        const payload = parts[1];
        let decodedPayload;

        try {
            decodedPayload = JSON.parse(atob(payload.replace(/-/g, '+').replace(/_/g, '/')));
        } catch (e) {
            changeState('login');
            return;
        }
    }, [changeState]);

    function handleButtonClick() {
        localStorage.removeItem('JWT');
        changeState('login');
    }

    return(
        <div>
            <h1>Аккаунт</h1>
            <h3>Email: decodedPayload.email</h3>
            <button onClick={handleButtonClick}>Выйти</button>
        </div>
    );
}

export default Account;