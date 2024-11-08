function DateObject2(day, month, year) {
    this.day = day;
    this.month = month;
    this.year = year;
}

DateObject2.prototype.getDay = function() {
    return this.day;
};

DateObject2.prototype.getMonth = function() {
    return this.month;
};

DateObject2.prototype.getYear = function() {
    return this.year;
};

DateObject2.prototype.setDay = function(day) {
    this.day = day;
};

DateObject2.prototype.setMonth = function(month) {
    this.month = month;
};

DateObject2.prototype.setYear = function(year) {
    this.year = year;
};

DateObject2.prototype.toString = function() {
    return `${this.day}/${this.month}/${this.year}`;
};

DateObject2.prototype.addDateToArray = function(array) {
    array.push(this);
};

function ExtendedDateObject2(day, month, year, description) {
    DateObject2.call(this, day, month, year); 
    this.description = description || '';
}

ExtendedDateObject2.prototype = Object.create(DateObject2.prototype);
ExtendedDateObject2.prototype.constructor = ExtendedDateObject2;

ExtendedDateObject2.prototype.getDescription = function() {
    return this.description;
};

ExtendedDateObject2.prototype.setDescription = function(description) {
    this.description = description;
};

ExtendedDateObject2.findLatestDate = function(array) {
    return array.reduce((latest, current) => {
        const currentDate = new Date(current.getYear(), current.getMonth() - 1, current.getDay());
        const latestDate = new Date(latest.getYear(), latest.getMonth() - 1, latest.getDay());
        return currentDate > latestDate ? current : latest;
    });
};

ExtendedDateObject2.prototype.displayAll = function(array) {
    return array.map(date => date.toString()).join('<br>');
};

ExtendedDateObject2.prototype.addDate = function(form) {
    const day = parseInt(form.day.value);
    const month = parseInt(form.month.value);
    const year = parseInt(form.year.value);
    const description = "UTC";
    return new ExtendedDateObject2(day, month, year, description);
}

const dateArray2 = [];

const date1 = new ExtendedDateObject2(12, 5, 2023, 'Event 1');
const date2 = new ExtendedDateObject2(20, 7, 2024, 'Event 2');
const date3 = new ExtendedDateObject2(15, 3, 2022, 'Event 3');

date1.addDateToArray(dateArray2);
date2.addDateToArray(dateArray2);
date3.addDateToArray(dateArray2);

let latestDate2 = ExtendedDateObject2.findLatestDate(dateArray2);

document.getElementById('datesList').innerHTML = `
    <h2>Все даты:</h2>
    <div>${date1.displayAll(dateArray2)}</div>
    <p>Самая поздняя дата: ${latestDate2.toString()}</p>
`;

const form2 = document.getElementById('dateForm');
form2.addEventListener('submit', function(event) {
    event.preventDefault();
    
    const extendedDate = new ExtendedDateObject2();
    const newDate = extendedDate.addDate(form2);
    dateArray2.push(newDate);

    latestDate2 = ExtendedDateObject2.findLatestDate(dateArray2);
    document.getElementById('datesList').innerHTML = `
    <h2>Все даты:</h2>
    <div>${date1.displayAll(dateArray2)}</div>
    <p>Самая поздняя дата: ${latestDate2.toString()}</p>
    `;
});