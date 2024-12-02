import React, { useEffect, useState } from 'react';
import './Navigation.css';

function Navigation({tab}) {
    const [admin, setAdmin] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem("JWT");
        if(token){
            const parts = token.split('.');
            const payload = parts[1];
            const decoded = JSON.parse(atob(payload.replace(/-/g, '+').replace(/_/g, '/')));
            setAdmin(decoded.role === 'admin');
        }
        else{
            setAdmin(false);
        }
    }, [tab]);

    return (
        <nav className="navigation">
            <ul>
                <li><a href="/">Главная</a></li>
                <li><a href="/specializations">Услуги</a></li>
                <li><a href="/profile">Профиль</a></li>
                <li><a href="/news">Новости</a></li>
                {admin && <li><a href="/admin">Админка</a></li>}
            </ul>
        </nav>
    );
};

export default Navigation;