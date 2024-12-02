import React, { useEffect, useState, useCallback } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "../Doctors.css";
import Navigation from "../../../navigation/Navigation";
import DoctorForm from './DoctorForm';

const EditDoctor = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [doctor, setDoctor] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [formData, setFormData] = useState({
        surname: '',
        first_name: '',
        last_name: '',
        image_url: null,
    });
    const [imageFile, setImageFile] = useState(null);

    const fetchDoctor = useCallback(async () => {
        try {
            const response = await fetch(`http://localhost:3001/api/doctors/${id}`);
            if (!response.ok) throw new Error("Ошибка при получении данных");
            const data = await response.json();
            setDoctor(data);
            setFormData(data);
            setLoading(false);
        } catch (err) {
            setError(err.message);
            setLoading(false);
        }
    }, [id]);

    useEffect(() => {
        fetchDoctor();
    }, [fetchDoctor]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = new FormData();
        data.append("surname", formData.surname);
        data.append("first_name", formData.first_name);
        data.append("last_name", formData.last_name);
        if (imageFile) {
            data.append("image", imageFile);
        }

        try {
            const token = localStorage.getItem('JWT');

            const headers = {
                'Authorization': `Bearer ${token}`
            };

            const response = await fetch(`http://localhost:3001/api/doctors/${id}`, {
                method: 'PATCH',
                body: data,
                headers: headers
            });
            if (!response.ok) throw new Error("Ошибка при обновлении данных");
            alert("Доктор успешно обновлён!");
            navigate('/admin');
        } catch (err) {
            setError(err.message);
        }
    };

    if (loading) return <p>Загрузка...</p>;
    if (error) return <p>Ошибка: {error}</p>;
    if (!doctor) return <p>Доктор не найден.</p>;

    return (
        <div>
            <Navigation />
            <div className="form-container">
                <form onSubmit={handleSubmit}>
                    <DoctorForm
                        formData={formData}
                        setFormData={setFormData}
                        setImageFile={setImageFile}
                    />
                    <button type="submit">Сохранить изменения</button>
                </form>
            </div>
        </div>
    );
};

export default EditDoctor;