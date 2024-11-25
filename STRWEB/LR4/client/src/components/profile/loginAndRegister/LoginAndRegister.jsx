import React from "react";
import TabsSection from "./items/TabsSection";
import Login from "./items/Login";
import Register from "./items/Register";
import "../Profile.css";

function LoginAndRegister({state, changeState}){
    return(
        <div>
            <TabsSection state={state} changeState={changeState}/>
            <div>
                {state === 'login' && <Login changeState={changeState} />}
                {state === 'register' && <Register changeState={changeState} />}
            </div>
        </div>
    );
}

export default LoginAndRegister;