import React, { useEffect } from 'react';

const GoogleAuthCallback = () => {
    useEffect(() => {
        const fetchToken = async () => {
            const queryParams = new URLSearchParams(window.location.search);
            const code = queryParams.get('code');

            if (code) {
                try {
                    const response = await fetch(`http://localhost:3001/oauth/?code=${code}`);
                    const data = await response.json();
                    console.log(data);
                    if (data.token) {
                        localStorage.removeItem('JWT');
                        localStorage.setItem('JWT', data.token);
                        window.location.href = '/profile';
                    } else {
                        console.log("Токен не получен");
                    }
                } catch (error) {
                    console.log("Ошибка при получении токена:", error);
                }
            }
        };

        fetchToken();
    }, []);

    return <div>Загрузка...</div>;
};

export default GoogleAuthCallback;