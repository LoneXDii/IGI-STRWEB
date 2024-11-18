const mongoose = require('mongoose');

const Schema = mongoose.Schema;

let Role = new Schema({
    name:{
        type: String,
        required: true
    },
    normalized_name:{
        type: String,
        required: true
    }
});

module.exports = mongoose.model('Role', Role);