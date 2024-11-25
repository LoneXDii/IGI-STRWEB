import React, { useEffect, useState } from "react";

function Account({ changeState }) {
    const [decodedPayload, setDecodedPayload] = useState(null);

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

    return (
        <div>
            <h1>Аккаунт</h1>
            {decodedPayload ? (
                <h3>Email: {decodedPayload.email}</h3>
            ) : (
                <h3>Загрузка...</h3>
            )}
            <button onClick={handleButtonClick}>Выйти</button>
        </div>
    );
}

export default Account;