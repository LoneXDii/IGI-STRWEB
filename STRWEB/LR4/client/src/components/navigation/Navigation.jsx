import React from 'react';
import './Navigation.css';

function Navigation() {
    return (
        <nav className="navigation">
            <ul>
                <li><a href="/">Главная</a></li>
                <li><a href="/specializations">Услуги</a></li>
                <li><a href="/profile">Профиль</a></li>
            </ul>
        </nav>
    );
};

export default Navigation;