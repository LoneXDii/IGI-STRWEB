import React from 'react';
import '../Specializations.css';
import Specialization from './Specialization';

function SpecializationsList(data) {
    const items = data.data.map(specialization => <Specialization key={specialization._id} {...specialization} />);

    return (
        <div>
            <ul className='specializations'>
                {items}
            </ul>
        </div>
    );
};

export default SpecializationsList;