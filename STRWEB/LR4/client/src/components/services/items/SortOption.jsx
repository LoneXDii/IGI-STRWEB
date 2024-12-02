import React from 'react';

function SortOptions({ onSortChange }) {
    const handleSortChange = (event) => {
        onSortChange(event.target.value);
    };

    return (
        <div className="sort-options">
            <label htmlFor="sort">Сортировать:</label>
            <select id="sort" onChange={handleSortChange}>
                <option value="">Без сортировки</option>
                <option value="name">По названию</option>
                <option value="price">По цене</option>
            </select>
        </div>
    );
}

export default SortOptions;