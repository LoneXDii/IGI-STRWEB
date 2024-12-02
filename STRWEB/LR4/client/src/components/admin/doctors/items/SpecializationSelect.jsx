import React, { useEffect, useState } from 'react';

const SpecializationSelect = ({ selectedSpecialization, setSelectedSpecialization }) => {
    const [specializations, setSpecializations] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchSpecializations = async () => {
            try {
                const response = await fetch('http://localhost:3001/api/specializations');
                if (!response.ok) throw new Error("Ошибка при загрузке специальностей");
                const data = await response.json();
                setSpecializations(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchSpecializations();
    }, []);

    if (loading) return <p>Загрузка специальностей...</p>;
    if (error) return <p className="error">{error}</p>;

    return (
        <div>
            <label htmlFor="specialization">Специальность:</label>
            <select
                id="specialization"
                value={selectedSpecialization}
                onChange={(e) => setSelectedSpecialization(e.target.value)}
            >
                <option value="">Выберите специальность</option>
                {specializations.map((spec) => (
                    <option key={spec._id} value={spec._id}>
                        {spec.name}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default SpecializationSelect;