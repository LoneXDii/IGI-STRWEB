const mongoose = require('mongoose');
const Specialization = require('./specialization');

const Schema = mongoose.Schema;

let Doctor = new Schema({
    first_name: {
        type: String,
        required: true
    },
    last_name: {
        type: String,
        required: true
    },
    surname: {
        type: String,
        required: true
    },
    image_url: {
        type: String,
        required: false
    },
    specialization: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Specialization'
    }
});

module.exports = mongoose.model('Doctor', Doctor);