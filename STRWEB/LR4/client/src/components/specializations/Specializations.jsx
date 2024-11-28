import React from 'react';
import './Specializations.css';
import Navigation from '../navigation/Navigation';
import { useCallback, useEffect, useState } from "react";
import SpecializationsList from './items/SpecializationsList';

function Specializations() {
    const [specializations, setSpecializations] = useState([]);
    const [loading, setLoading] = useState(false);
    
    let items = null;

    const fetchSpecializations = useCallback(async () => {
        setLoading(true);
        const response = await fetch('http://localhost:3001/api/specializations');
        const data = await response.json();
        setSpecializations(data);
        setLoading(false);
    },[]);

    useEffect(() => {
        fetchSpecializations()
    }, [fetchSpecializations]);

    if(loading){
        items = <p>Loading...</p>;
    }
    else{
        items = <SpecializationsList data={specializations} />
    }

    return (
        <div>
            <Navigation />
            <div className='container'>
                {items}
            </div>
        </div>
    );
};

export default Specializations;