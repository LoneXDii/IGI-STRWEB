const express = require("express");
const router = express.Router();
const passport = require('passport');

const Order = require("../models/order");
const Service = require("../models/service");
const Doctor = require("../models/doctor")

router.post('/', passport.authenticate('jwt', { session: false }), async (req, res) => {
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

        order.user_id = req.user.role._id;

        await order.save();
        res.status(201).json(order);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

router.get("/", passport.authenticate('jwt', { session: false }), async (req, res) => {
    let filter = {};
    const is_active = req.query.active;

    if(req.user.role.normalized_name === 'customer'){
        filter.user_id = req.user._id;
    }

    if(req.user.role.normalized_name === 'doctor'){
        filter.doctor = req.user.doctor._id;
    }

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

        if(req.user.role.normalized_name === 'customer'){
            if (order.user_id !== req.user._id){
                res.status(403).json({ message: "You have no access to do this" });
                return;
            }
        }

        if(req.user.role.normalized_name === 'doctor'){
            if(order.doctor._id !== req.user.doctor._id){
                res.status(403).json({ message: "You have no access to do this" });
                return;
            }
        }

        res.status(200).json(order);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.get("/doctor/:id", async (req, res) => {
    try {
        if(req.user.role.normalized_name !== 'doctor'){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }

        if(req.user.doctor._id !== req.params.id){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }

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

        if(req.user.role.normalized_name === 'customer'){
            filter.user_id = req.user._id;
        }

        if(req.user.role.normalized_name === 'doctor'){
            filter.doctor = req.user.doctor._id;
        }

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

        if(req.user.role.normalized_name !== 'customer'){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }

        if(req.user._id !== order.user_id){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }

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

        if(req.user.role.normalized_name !== 'doctor'){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }

        const order = await Order.findOne({ _id: req.params.id });
    
        if(req.user.doctor._id !== order.doctor){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }

        order.is_active = false;

        await order.save();
        res.status(200).json(order);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

module.exports = router;