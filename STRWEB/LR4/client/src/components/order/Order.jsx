import React, { useCallback, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import DoctorsSelector from "./items/DoctorsSelector";
import Navigation from "../navigation/Navigation";
import ServiceInfo from "./items/ServiceInfo";
import "./Order.css";

function Order(){
    const { id } = useParams();
    const [service, setService] = useState(null);
    const [doctors, setDoctors] = useState([]);
    const [loading, setLoading] = useState(false);
    const [doctorId, setDoctorId] = useState(null);

    const navigate = useNavigate();

    useEffect(() =>{
        if (!localStorage.getItem('JWT')) {
            navigate('/profile');
        }
    }, []);

    let selector = null;
    let serviceInfo = null;

    const fetchDoctors = useCallback(async () => {
        setLoading(true);
        const serviceResponse = await fetch(`http://localhost:3001/api/services/${id}`);
        const serviceData = await serviceResponse.json();
        setService(serviceData);
        
        const response = await fetch(`http://localhost:3001/api/doctors/specialization/${serviceData.specialization._id}`);
        const data = await response.json();

        setDoctors(data);
        setLoading(false);
    },[]);

    useEffect(() => {
        fetchDoctors();
    }, [fetchDoctors]);

    async function handleOnClick(){
        if(doctorId === null){
            return;
        }

        const data = {
            doctor: doctorId,
            services: [
                id
            ]
        };

        const token = localStorage.getItem('JWT');

        const headers = {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        };

        const response = await fetch('http://localhost:3001/api/orders',{
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data)
        });
        console.log(response);
        navigate('/profile');
    }

    if(loading){
        selector = <p>Loading...</p>;
        serviceInfo = <p>Loading...</p>;
    }
    else{
        selector = <DoctorsSelector data={doctors} doctorId={doctorId} setDoctorId={setDoctorId}/>;
        serviceInfo = <ServiceInfo {...service} />
    }

    return(
        <div>
            <Navigation />
            <div className="container">
                {serviceInfo}
                {selector}
                <button onClick={handleOnClick} className="button">Записаться</button>
            </div>
        </div>
    );
}

export default Order;