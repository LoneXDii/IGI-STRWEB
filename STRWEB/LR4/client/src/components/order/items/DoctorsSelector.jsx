import React from "react";

function DoctorsSelector({data, doctorId, setDoctorId}){
    console.log(data);

    const selectors = data.map(d => <option key={d._id} value={d._id}>{d.surname} {d.first_name} {d.last_name}</option>);

    function handleChange(event){
        setDoctorId(event.target.value);
    }

    return(
        <div>
            <select value={doctorId} onChange={handleChange}>
                <option value={null}>Выберите доктора</option>
                {selectors}
            </select>
        </div>
    );
}

export default DoctorsSelector