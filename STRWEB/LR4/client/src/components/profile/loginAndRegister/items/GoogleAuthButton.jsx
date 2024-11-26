import React from 'react';
import "../../Profile.css";

function GoogleAuthButton() {
    const handleLogin = async () => {
        try {
            const response = await fetch('http://localhost:3001/google');
            const data = await response.json();
            console.log(data);
            window.location.href = data.url;
        } catch (error) {
            console.error("Ошибка при получении URL авторизации:", error);
        }
    };

    return (
        <button onClick={handleLogin} className='enabled-button'>
            Войти через Google
        </button>
    );
};

export default GoogleAuthButton;