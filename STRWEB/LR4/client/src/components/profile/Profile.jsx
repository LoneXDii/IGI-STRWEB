import React, { useEffect, useState } from "react";
import Navigation from "../navigation/Navigation";
import LoginAndRegister from "./loginAndRegister/LoginAndRegister";
import "./Profile.css";
import Account from "./account/Account";

function Profile(){
    const [tab, setTab] = useState('account');

    useEffect(() => {
        if (!localStorage.getItem('JWT')) {
            setTab('login');
        }
    }, []); 

    return(
        <div>
            <Navigation tab={tab}/>
            <div className="profile-container">
                {tab !== 'account' && <LoginAndRegister state={tab} changeState={setTab} />}
                {tab === 'account' && <Account changeState={setTab}/>}
            </div>
        </div>
    );
}

export default Profile;