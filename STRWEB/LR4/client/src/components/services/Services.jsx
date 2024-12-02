import React, { useCallback, useEffect, useState } from 'react';
import './Services.css';
import { useParams } from 'react-router-dom';
import ServicesList from './items/ServicesList';
import Navigation from '../navigation/Navigation';
import SortOptions from './items/SortOption';

function Services() {
    const { id } = useParams();
    const [services, setServices] = useState([]);
    const [loading, setLoading] = useState(false);
    const [sortType, setSortType] = useState('');

    const fetchServices = useCallback(async () => {
        setLoading(true);
        const response = await fetch(`http://localhost:3001/api/services/specialization/${id}`);
        const data = await response.json();
        setServices(data);
        setLoading(false);
    }, [id]);

    useEffect(() => {
        fetchServices();
    }, [fetchServices]);

    const handleSortChange = (sortType) => {
        setSortType(sortType);
    };

    const sortedServices = [...services].sort((a, b) => {
        if (sortType === 'name') {
            return a.name.localeCompare(b.name);
        } else if (sortType === 'price') {
            return a.price - b.price;
        }
        return 0;
    });

    let items = loading ? <p>Loading...</p> : <ServicesList data={sortedServices} />;

    return (
        <div>
            <Navigation />
            <div className='container'>
                <SortOptions onSortChange={handleSortChange} />
                {items}
            </div>
        </div>
    );
}

export default Services;