import React, { useEffect, useState } from "react";
import "../../Profile.css";

function Register({changeState}){
    const [emailError, setEmailError] = useState(false);
    const [passwordError, setPasswordError] = useState(false);
    const [repeatPasswordError, setRepeatPasswordError] = useState(false);
    const [imageFile, setImageFile] = useState(null)

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [repeatPassword, setRepeatPassword] = useState('');

    const emailPattern = /^\S+@\S+\.\S+$/;
    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    const [isRedirrectToProfile, setRedirrectToProfile] = useState(false);

    useEffect(() => {
        if (localStorage.getItem('JWT')) {
            changeState('account');
        }
    }, []);

    function handleEmailChange(event){
        let newEmail = event.target.value;
        setEmail(newEmail);
    }

    function handlePasswordChange(event){
        let newPass = event.target.value;
        setPassword(newPass);
        let isOk = passwordPattern.test(newPass);
        setPasswordError(!isOk);
    }

    function handleRepeatPasswordChange(event){
        let newRepPass = event.target.value;
        setRepeatPassword(newRepPass);
        let isOk = newRepPass === password;
        setRepeatPasswordError(!isOk);
    }    

    function handleImageSelect(event){
        setImageFile(event.target.files[0])
    }

    async function handleButtonClick(){
        try{
            let isEmailOk = emailPattern.test(email);
            let isPasswordOk = passwordPattern.test(password);
            let isRepeatPasswordOk = password === repeatPassword;

            setEmailError(!isEmailOk);
            setPasswordError(!isPasswordOk);
            setRepeatPasswordError(!isRepeatPasswordOk);

            if (!(isEmailOk && isRepeatPasswordOk && isPasswordOk)){
                return
            }

            const formData = new FormData();
            formData.append('email', email);
            formData.append('password', password);

            if(imageFile){
                formData.append('image', imageFile);
            }

            let response = await fetch('http://localhost:3001/api/account/register', {
                method: 'POST',
                body: formData,
            });

            const user = {
                email: email,
                password: password
            };

            response = await fetch('http://localhost:3001/api/account/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(user),
            });

            const result = await response.json();

            localStorage.removeItem('JWT');
            localStorage.setItem('JWT', result.token);

            setRedirrectToProfile(true);
        }
        catch (error){
            console.log(error.response.status);
        }
    }

    useEffect(() => {
        if (isRedirrectToProfile) {
            changeState('account');
        }
    }, [isRedirrectToProfile, changeState]);

    return(
        <div>
            <label>Email</label>
            {emailError && (
                <div role="alert">
                    Пожалуйста, введите корректный адрес электронной почты
                </div>)}
            <input name=""  placeholder="email" type="email"
                value={email} onChange={handleEmailChange}
                style={{border: emailError ? '2px solid red' : null}}/>

            <label>Пароль</label>
            {passwordError && (
                <div role="alert">
                    Пожалуйста, введите корректный пароль
                </div>)}
            <input placeholder="password" type="password"
                   value={password} onChange={handlePasswordChange}
                   style={{border: passwordError ? '2px solid red' : null}}/>

            <label>Повторите пароль</label>
            <input placeholder="password" type="password"
                    value={repeatPassword} onChange={handleRepeatPasswordChange}
                    style={{border: repeatPasswordError ? '2px solid red' : null}}/>

            <label>Аватар:</label>
            <input type="file" name="image" accept="image/*" onChange={handleImageSelect} />

            <button onClick={() => handleButtonClick()}>
               Зарегистрироваться
            </button> 
        </div>
    );
}

export default Register;