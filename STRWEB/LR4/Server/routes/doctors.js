const express = require("express");
const router = express.Router();

const Doctor = require("../models/doctor");

router.post('/', async (req, res) => {
    try {
        const doctor = new Doctor(req.body);

        await doctor.save();

        res.status(201).json(doctor);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

module.exports = router;