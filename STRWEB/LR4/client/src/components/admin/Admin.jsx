import React from "react";
import Navigation from "../navigation/Navigation";
import DoctorsList from "./doctors/items/DoctorsList";
import "./Admin.css";

const Admin = () => {
    return(
        <div>
            <Navigation />
            <div className="admin-container">
                <DoctorsList />
            </div>
        </div>
    );
}

export default Admin;