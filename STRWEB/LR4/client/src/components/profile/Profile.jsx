import React, { useEffect, useState } from "react";
import Navigation from "../navigation/Navigation";
import LoginAndRegister from "./loginAndRegister/LoginAndRegister";
import "./Profile.css";

function Profile(){
    const [tab, setTab] = useState('account');

    useEffect(() => {
        if (!localStorage.getItem('JWT')) {
            setTab('login');
        }
    }, []); 

    return(
        <div>
            <Navigation />
            <div className="profile-container">
                {tab !== 'account' && <LoginAndRegister state={tab} changeState={setTab} />}
            </div>
        </div>
    );
}

export default Profile;