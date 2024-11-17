const express = require("express");
const router = express.Router();

const Order = require("../models/order");
const Service = require("../models/service");
const Doctor = require("../models/doctor")

router.post('/', async (req, res) => {
    try {
        const order = new Order(req.body);
        
        order.total_price = 0;

        let doctor = await Doctor.findById(order.doctor);

        if(!doctor){
            res.status(400).json({ message: "No such doctor" });

            return;
        }

        for (service_id of order.services){
            
            let service = await Service.findById(service_id);

            if (!service){
                res.status(400).json({ message: "No such service" });

                return;
            }

            order.total_price += service.price;
        }

        await order.save();

        res.status(201).json(order);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

module.exports = router;