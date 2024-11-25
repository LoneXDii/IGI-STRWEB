import React, { useEffect, useState } from "react";
import "../../Profile.css";

function Login({changeState}){
    const [emailError, setEmailError] = useState(false);
    const [passwordError, setPasswordError] = useState(false);

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const [isRedirrectToProfile, setRedirrectToProfile] = useState(false);
    const [isLoginError, setIsLoginError] = useState(false);

    const emailPattern = /^\S+@\S+\.\S+$/;

    useEffect(() => {
        if (localStorage.getItem('JWT')) {
            changeState('account');
        }
    }, []);

    function handleEmailChange(event){
        let newEmail = event.target.value
        setEmail(newEmail)
    }

    function handlePasswordChange(event){
        let newPass = event.target.value
        setPassword(newPass)
    }

    async function handleButtonClick(){
        try{
            let isEmailOk = emailPattern.test(email);
            let isPasswordOk = !(password === "");
            
            setIsLoginError(false);
            setEmailError(!isEmailOk);
            setPasswordError(!isPasswordOk);

            if(!(isEmailOk && isPasswordOk)){
                return;
            }

            const user = {
                email: email,
                password: password
            };

            const response = await fetch('http://localhost:3001/api/account/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(user),
            });

            if(response.status !== 200){
                setIsLoginError(true);
                return;
            }

            const result = await response.json();

            localStorage.removeItem('JWT');
            localStorage.setItem('JWT', result.token);
            
            setRedirrectToProfile(true);
        }
        catch (error){
            console.log(error.response.status);
            setIsLoginError(true);
        }
    }

    useEffect(() => {
        if (isRedirrectToProfile) {
            changeState('account');
        }
    }, [isRedirrectToProfile, changeState]);

    return(
        <div>
            {isLoginError && (
                <div role="alert">
                    Некорректный адрес электронной почты или пароль
                </div>)}

            <label>Email</label>
            {emailError && (
                <div role="alert">
                    Пожалуйста, введите корректный адрес электронной почты
                </div>)}
            <input name=""  placeholder="email" type="email"
                value={email} onChange={handleEmailChange}
                style={{border: emailError ? '2px solid red' : null}}/>

            <label>Password</label>
            {passwordError && (
                <div role="alert">
                    Пожалуйста, введите корректный пароль
                </div>)}
            <input placeholder="password" type="password"
                   value={password} onChange={handlePasswordChange}
                   style={{border: passwordError ? '2px solid red' : null}}/>

            <button onClick={() => handleButtonClick()}>
               Войти
            </button> 
        </div>
    );
}

export default Login;