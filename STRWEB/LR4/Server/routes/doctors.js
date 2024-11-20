const express = require("express");
const router = express.Router();
const passport = require('passport');

const Doctor = require("../models/doctor");
const Specialization = require("../models/specialization");

router.post('/', passport.authenticate('jwt', { session: false }), async (req, res) => {
    try {
        if (req.user.role.normalized_name !== "admin"){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }
        
        const doctor = new Doctor(req.body);
        const specialization = await Specialization.findById(doctor.specialization);

        if (!specialization){
            res.status(400).json({ message: "No such specialization" });
            return;
        }

        await doctor.save();
        res.status(201).json(doctor);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

router.get("/", async (req, res) => {
    const doctors = await Doctor.find().populate('specialization');
    res.status(200).json(doctors);
});

router.get("/:id", async (req, res) => {
    try {
        const doctor = await Doctor.findOne({ _id: req.params.id }).populate('specialization');
        res.status(200).json(doctor);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.get("/specialization/:id", async (req, res) => {
    try {
        const doctors = await Doctor.find({ specialization: req.params.id }).populate('specialization');
        res.status(200).json(doctors);
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
        
        await Doctor.deleteOne({ _id: req.params.id });
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
        
        const doctor = await Doctor.findOne({ _id: req.params.id });
    
        if (req.body.first_name) {
            doctor.first_name = req.body.first_name;
        }
        if (req.body.last_name) {
            doctor.last_name = req.body.last_name;
        }
        if (req.body.surname) {
            doctor.surname = req.body.surname;
        }
        if (req.body.image_url) {
            doctor.image_url = req.body.image_url;
        }
        if (req.body.specialization) {
            doctor.specialization = req.body.specialization;
        }

        await doctor.save();
        res.status(200).json(doctor);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

module.exports = router;