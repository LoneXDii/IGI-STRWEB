const mongoose = require('mongoose');
const Doctor = require('./doctor');
const Service = require('./service');

const Schema = mongoose.Schema;

let Order = new Schema({
    services: [{
        type: mongoose.Schema.Types.ObjectId, 
        ref: 'Service' 
    }],
    doctor: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Doctor'
    },
    total_price:{
        type: Number
    },
    is_active:{
        type: Boolean
    },
    user_id:{
        type: String
    }
});

module.exports = mongoose.model('Order', Order);