import React, { useEffect, useState, useCallback } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "../Doctors.css";
import Navigation from "../../../navigation/Navigation";

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

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleFileChange = (e) => {
        setImageFile(e.target.files[0]);
    };

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
                    <div>
                        <label>
                            Фамилия:
                            <input
                                type="text"
                                name="surname"
                                value={formData.surname}
                                onChange={handleChange}
                                required
                            />
                        </label>
                    </div>
                    <div>
                        <label>
                            Имя:
                            <input
                                type="text"
                                name="first_name"
                                value={formData.first_name}
                                onChange={handleChange}
                                required
                            />
                        </label>
                    </div>
                    <div>
                        <label>
                            Отчество:
                            <input
                                type="text"
                                name="last_name"
                                value={formData.last_name}
                                onChange={handleChange}
                                required
                            />
                        </label>
                    </div>
                    <div>
                        <label>
                            Фото:
                            <input
                                type="file"
                                name="image"
                                accept="image/*"
                                onChange={handleFileChange}
                            />
                        </label>
                    </div>
                    <button type="submit">Сохранить изменения</button>
                </form>
            </div>
        </div>
    );
};

export default EditDoctor;