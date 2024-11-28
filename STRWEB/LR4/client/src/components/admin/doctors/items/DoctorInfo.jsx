import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "../Doctors.css";
import Navigation from "../../../navigation/Navigation";

const DoctorInfo = () => {
    const { id } = useParams();
    const [doctor, setDoctor] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchDoctor = async () => {
            try {
                console.log("url: ", `http://localhost:3001/api/doctors/${id}`);
                const response = await fetch(`http://localhost:3001/api/doctors/${id}`);
                if (!response.ok) throw new Error("Ошибка при получении данных");
                const data = await response.json();
                setDoctor(data);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };

        fetchDoctor();
    }, [id]);

    if (loading) return <p>Загрузка...</p>;
    if (error) return <p>Ошибка: {error}</p>;
    if (!doctor) return <p>Доктор не найден.</p>;

    return (
        <div>
            <Navigation/>
            <div className="doctor-info">
                <h2>Информация о докторе</h2>
                <img src={doctor.image_url || '/noimage.png'} alt={`${doctor.first_name} ${doctor.last_name}`} />
                <p><strong>Фамилия:</strong> {doctor.surname}</p>
                <p><strong>Имя:</strong> {doctor.first_name}</p>
                <p><strong>Отчество:</strong> {doctor.last_name}</p>
            </div>
        </div>
    );
};

export default DoctorInfo;