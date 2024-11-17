const mongoose = require('mongoose');
const Specialization = require('./specialization');

const Schema = mongoose.Schema;

let Service = new Schema({
    name: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true
    },
    specialization: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Specialization'
    }
});

module.exports = mongoose.model('Service', Service);