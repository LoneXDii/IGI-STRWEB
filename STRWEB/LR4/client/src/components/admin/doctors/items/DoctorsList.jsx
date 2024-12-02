import React, { useCallback, useEffect, useState } from "react";
import Doctor from "./Doctor";
import { useNavigate } from "react-router-dom";

function DoctorsList(){
    const [doctors, setDoctors] = useState([]);
    const [loading, setLoading] = useState(false);
    const [costyl, setCostyl] = useState(false);
    const navigate = useNavigate();

    const fetchDoctors = useCallback(async () => {
        setLoading(true);
        const response = await fetch(`http://localhost:3001/api/doctors`);
        const data = await response.json();
        setDoctors(data.map(d => <Doctor key={d._id} {...d} onDelete={handleDelete}/>));

        setLoading(false);
    },[]);

    useEffect(() => {
        fetchDoctors()
    }, [fetchDoctors, costyl]);

    const handleDelete = () => {
        setCostyl(!costyl);
    };

    function handleOnClick(){
        navigate('/admin/doctor/create');
    }

    return(
        <div>
            <button type="button" className="add-button"
                onClick={handleOnClick}>
                Создать доктора
                </button>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <ul className="admin-list">
                    {doctors}
                </ul>
            )}
        </div>
    );
}

export default DoctorsList;