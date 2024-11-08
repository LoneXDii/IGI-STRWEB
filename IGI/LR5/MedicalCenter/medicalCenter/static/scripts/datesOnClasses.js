class DateObject {
    constructor(day, month, year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    getDate() {
        return `${this.day}/${this.month}/${this.year}`;
    }

    setDate(day, month, year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    toString() {
        return this.getDate();
    }
}

class ExtendedDateObject extends DateObject {
    constructor(day, month, year, timezone) {
        super(day, month, year);
        this.timezone = timezone;
    }

    getTimezone() {
        return this.timezone;
    }

    addDate(form) {
        const day = parseInt(form.day.value);
        const month = parseInt(form.month.value);
        const year = parseInt(form.year.value);
        const timezone = "UTC";
        return new ExtendedDateObject(day, month, year, timezone);
    }

    displayDates(datesArray) {
        const output = datesArray.map(date => date.getDate()).join('<br>');
        document.getElementById('datesListClass').innerHTML = output;
    }

    findLatestDate(datesArray) {
        return datesArray.reduce((latest, current) => {
            const currentDate = new Date(current.year, current.month - 1, current.day);
            const latestDate = new Date(latest.year, latest.month - 1, latest.day);
            return currentDate > latestDate ? current : latest;
        });
    }
}

const datesArray = [
    new ExtendedDateObject(15, 8, 2021, 'UTC'),
    new ExtendedDateObject(10, 6, 2022, 'UTC'),
    new ExtendedDateObject(1, 1, 2023, 'UTC')
];

const latestDate = datesArray[0].findLatestDate(datesArray);
datesArray[0].displayDates(datesArray);

const form = document.getElementById('dateFormClass');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    const extendedDate = new ExtendedDateObject();
    const newDate = extendedDate.addDate(form);
    datesArray.push(newDate);
    extendedDate.displayDates(datesArray);

    const latestDate = extendedDate.findLatestDate(datesArray);
    document.getElementById('outputClass').innerHTML = 'Самая поздняя дата: ' + latestDate.getDate();
});

document.getElementById('outputClass').innerHTML = 'Самая поздняя дата: ' + latestDate.getDate();