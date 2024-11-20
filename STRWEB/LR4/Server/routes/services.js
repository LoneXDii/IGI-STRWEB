const express = require("express");
const router = express.Router();
const passport = require('passport');

const Service = require("../models/service");
const Specialization = require("../models/specialization");

router.post('/', passport.authenticate('jwt', { session: false }), async (req, res) => {
    try {
        if (req.user.role.normalized_name !== "admin"){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }
        
        const service = new Service(req.body);
        const specialization = await Specialization.findById(service.specialization);

        if (!specialization){
            res.status(400).json({ message: "No such specialization" });
            return;
        }

        await service.save();
        res.status(201).json(service);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

router.get("/", async (req, res) => {
    const services = await Service.find().populate('specialization');
    res.status(200).json(services);
});

router.get("/:id", async (req, res) => {
    try {
        const service = await Service.findOne({ _id: req.params.id }).populate('specialization');
        res.status(200).json(service);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.get("/specialization/:id", async (req, res) => {
    try {
        const services = await Service.find({ specialization: req.params.id }).populate('specialization');
        res.status(200).json(services);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.delete("/:id", passport.authenticate('jwt', { session: false }), async (req, res) => {
    try {
        if (req.user.role.normalized_name !== "admin"){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }
        
        await Service.deleteOne({ _id: req.params.id });
        res.status(204).send();
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.patch("/:id", passport.authenticate('jwt', { session: false }), async (req, res) => {
    try {
        if (req.user.role.normalized_name !== "admin"){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }
        
        const service = await Service.findOne({ _id: req.params.id });
    
        if (req.body.name) {
            service.name = req.body.name;
        }
        if (req.body.price) {
            service.price = req.body.price;
        }
        if (req.body.specialization) {
            service.specialization = req.body.specialization;
        }

        await service.save();
        res.status(200).json(service);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

module.exports = router;