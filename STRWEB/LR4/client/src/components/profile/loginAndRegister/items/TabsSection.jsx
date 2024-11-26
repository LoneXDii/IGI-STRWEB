import React, { useEffect, useState } from "react";
import "../../Profile.css";
import GoogleAuthButton from "./GoogleAuthButton";

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
                <button onClick={() => changeState('login')}
                    className={state === 'login' ? 'disabled-button' : 'enabled-button'}
                    >
                    Войти
                </button>
            </li>
            <li>
                <button  onClick={() => changeState('register')}
                    className={state === 'register' ? 'disabled-button' : 'enabled-button'}
                    >
                    Зарегистрироваться
                </button>
            </li>
            <li>
                <GoogleAuthButton />
            </li>
        </ul>
    )
}

export default TabsSection;