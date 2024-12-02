import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../Doctors.css";
import Navigation from "../../../navigation/Navigation";
import DoctorForm from './DoctorForm';
import SpecializationSelect from './SpecializationSelect'; 

const CreateDoctor = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        surname: '',
        first_name: '',
        last_name: '',
        image_url: null,
    });
    const [imageFile, setImageFile] = useState(null);
    const [error, setError] = useState(null);
    const [selectedSpecialization, setSelectedSpecialization] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!formData.surname || !formData.first_name || !formData.last_name || !selectedSpecialization) {
            setError("Все поля, включая специальность, обязательны для заполнения.");
            return;
        }

        const data = new FormData();
        data.append("surname", formData.surname);
        data.append("first_name", formData.first_name);
        data.append("last_name", formData.last_name);
        data.append("specialization", selectedSpecialization);
        if (imageFile) {
            data.append("image", imageFile);
        }

        try {
            const token = localStorage.getItem('JWT');
            const headers = {
                'Authorization': `Bearer ${token}`
            };

            const response = await fetch(`http://localhost:3001/api/doctors`, {
                method: 'POST',
                body: data,
                headers: headers
            });
            if (!response.ok) throw new Error("Ошибка при создании доктора");
            alert("Доктор успешно создан!");
            navigate('/admin');
        } catch (err) {
            setError(err.message);
        }
    };

    return (
        <div>
            <Navigation />
            <div className="form-container">
                <form onSubmit={handleSubmit}>
                    {error && <p className="error">{error}</p>}
                    <DoctorForm
                        formData={formData}
                        setFormData={setFormData}
                        setImageFile={setImageFile}
                    />
                    <SpecializationSelect
                        selectedSpecialization={selectedSpecialization}
                        setSelectedSpecialization={setSelectedSpecialization}
                    />
                    <button type="submit">Создать доктора</button>
                </form>
            </div>
        </div>
    );
};

export default CreateDoctor;