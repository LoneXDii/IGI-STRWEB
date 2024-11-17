const express = require("express");
const router = express.Router();

const Specialization = require("../models/specialization");

router.post("/", async (req, res) => {
    try {
        const specialization = new Specialization(req.body);

        await specialization.save();
        
        res.status(201).json(specialization);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

module.exports = router;