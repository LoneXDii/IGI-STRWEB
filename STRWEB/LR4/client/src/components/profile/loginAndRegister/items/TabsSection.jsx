import React, { useEffect, useState } from "react";
import "../../Profile.css";

function TabsSection({state, changeState}){
    const [loginButton, setLoginButton] = useState('');
    const [registerButton, setRegisterButton] = useState('');

    useEffect(() => {
        if (state === 'login') {
            setLoginButton('disabled');
            setRegisterButton('active');
        } else if (state === 'register') {
            setLoginButton('active');
            setRegisterButton('disabled');
        }
    }, [state]);

    return(
        <ul className="button-container">
            <li>
                <button className={loginButton}
                    onClick={() => changeState('login')}>Войти</button>
            </li>
            <li>
                <button  className={registerButton}
                    onClick={() => changeState('register')}>Зарегистрироваться</button>
            </li>
        </ul>
    )
}

export default TabsSection;