import React, { useCallback, useEffect, useState } from 'react';
import './Services.css';
import { useParams } from 'react-router-dom';
import ServicesList from './items/ServicesList';
import Navigation from '../navigation/Navigation';

function Services(){
    const { id } = useParams();
    const [services, setServices] = useState([]);
    const [loading, setLoading] = useState(false);

    let items = null;

    const fetchServices = useCallback(async () => {
        setLoading(true);
        const response = await fetch(`http://localhost:3001/api/services/specialization/${id}`);
        const data = await response.json();

        setServices(data);
        setLoading(false);
    },[]);

    useEffect(() => {
        fetchServices()
    }, [fetchServices]);

    if(loading){
        items = <p>Loading...</p>;
    }
    else{
        items = <ServicesList data={services}/>;
    }

    return(
        <div>
            <Navigation/>
            {items}
        </div>
    );
}

export default Services;