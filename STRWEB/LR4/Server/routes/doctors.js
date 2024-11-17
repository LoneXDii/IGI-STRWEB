const express = require("express");
const router = express.Router();

const Doctor = require("../models/doctor");
const Specialization = require("../models/specialization");

router.post('/', async (req, res) => {
    try {
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

module.exports = router;