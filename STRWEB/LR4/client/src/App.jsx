import React, { useEffect, useState } from 'react';
import './App.css';
import Navigation from './components/navigation/Navigation';

const App = () => {
    const [currentDate, setCurrentDate] = useState('');
    const [timeZone, setTimeZone] = useState('');

    useEffect(() => {
        const updateDateTime = () => {
            const now = new Date();
            setCurrentDate(now.toLocaleString());
        };
        updateDateTime();
        const intervalId = setInterval(updateDateTime, 1000); 
        return () => clearInterval(intervalId);
    }, []);

    useEffect(() => {
        setTimeZone(Intl.DateTimeFormat().resolvedOptions().timeZone);
    }, []);

    return (
        <div className="app">
            <Navigation />
            <header className="header">
                <h1 className="title">Добро пожаловать в Healthwell</h1>
                <p className="subtitle">Ваш надежный медицинский центр</p>
                <p className="date-info">Текущая дата и время: {currentDate}</p>
                <p className="timezone-info">Ваша тайм-зона: {timeZone}</p>
            </header>
            <main className="main-content">
                <section className="about">
                    <h2 className="section-title">О нас</h2>
                    <p className="about-text">
                        Healthwell предлагает широкий спектр медицинских услуг, 
                        включая диагностику и лечение различных заболеваний. 
                        Наша команда опытных специалистов готова помочь вам в 
                        решении любых медицинских вопросов.
                    </p>
                </section>
                <section className="services">
                    <h2 className="section-title">Наши Услуги</h2>
                    <ul className="services-list">
                        <li className="service-item">Консультации врачей</li>
                        <li className="service-item">Диагностика</li>
                        <li className="service-item">Лечение</li>
                        <li className="service-item">Реабилитация</li>
                    </ul>
                </section>
            </main>
            <footer className="footer">
                <p className="footer-text">© 2024 Healthwell. Все права защищены.</p>
            </footer>
        </div>
    );
};

export default App;