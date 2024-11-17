const express = require("express");
const router = express.Router();

const Service = require("../models/service");
const Specialization = require("../models/specialization");

router.post('/', async (req, res) => {
    try {
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


module.exports = router;