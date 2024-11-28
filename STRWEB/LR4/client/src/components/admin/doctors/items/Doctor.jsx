import React from "react";
import { useNavigate } from "react-router-dom";

function Doctor({_id, first_name, last_name, surname, image_url, onDelete}){
    const navigate = useNavigate();
    const defaultImage = '/noimage.png';

    function handleInfoClick(){
        navigate(`/admin/doctor/${_id}`);
    }

    function handleEditClick(){
        navigate(`/admin/doctor/update/${_id}`);
    }

    async function handleDeleteClick() {
        const token = localStorage.getItem('JWT');

        const headers = {
            'Authorization': `Bearer ${token}`
        };

        const response = await fetch(`http://localhost:3001/api/doctors/${_id}`, {
            method: 'DELETE',
            headers: headers
        });

        if (response.ok) {
            onDelete(); 
        } else {
            console.error("Ошибка при удалении врача");
        }
    }

    return(
        <li className="admin-item-info">
            <div className="info-container">
                <img src={image_url || defaultImage} alt="Profile" />
                <h3>{surname} {last_name} {first_name}</h3>
            </div>
            <div className="button-group">
                <button className="info-button" onClick={handleInfoClick}>Информация</button>
                <button className="edit-button" onClick={handleEditClick}>Изменить</button>
                <button className="delete-button" onClick={handleDeleteClick}>Удалить</button>
            </div>
        </li>
    );
}

export default Doctor;