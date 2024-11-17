const express = require("express");
const router = express.Router();

const Order = require("../models/order");
const Service = require("../models/service");
const Doctor = require("../models/doctor")

router.post('/', async (req, res) => {
    try {
        const order = new Order(req.body);
        order.total_price = 0;
        order.is_active = true;
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

router.get("/", async (req, res) => {
    let filter = {};
    const is_active = req.query.active;

    if(is_active === 'true'){
        filter.is_active = true;
    }
    if(is_active === 'false'){
        filter.is_active = false;
    }

    const orders = await Order.find(filter).populate('services').populate('doctor');
    res.status(200).json(orders);
});

router.get("/:id", async (req, res) => {
    try {
        const order = await Order.findOne({ _id: req.params.id }).populate('services').populate('doctor');
        res.status(200).json(order);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.get("/doctor/:id", async (req, res) => {
    try {
        let filter = { doctor: req.params.id };
        const is_active = req.query.active;

        if(is_active === 'true'){
            filter.is_active = true;
        }
        if(is_active === 'false'){
            filter.is_active = false;
        }

        const orders = await Order.find(filter).populate('services').populate('doctor');
        res.status(200).json(orders);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.get("/service/:id", async (req, res) => {
    try {
        let filter = { services: req.params.id };
        const is_active = req.query.active;

        if(is_active === 'true'){
            filter.is_active = true;
        }
        if(is_active === 'false'){
            filter.is_active = false;
        }

        const orders = await Order.find(filter).populate('services').populate('doctor');
        res.status(200).json(orders);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.delete("/:id", async (req, res) => {
    try {
        const order = await Order.findOne({ _id: req.params.id});

        if(!order.is_active){
            res.status(400).json({ message: "Cannot delete completed order"});
            return;
        }
        
        await Order.deleteOne({ _id: req.params.id });
        res.status(204).send();
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.patch("/complete/:id", async (req, res) => {
    try {
        const order = await Order.findOne({ _id: req.params.id });
    
        order.is_active = false;

        await order.save();
        res.status(200).json(order);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

module.exports = router;