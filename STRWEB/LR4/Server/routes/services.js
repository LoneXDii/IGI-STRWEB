const express = require("express");
const router = express.Router();

const Service = require("../models/service");

router.post('/', async (req, res) => {
    try {
        const service = new Service(req.body);

        await service.save();

        res.status(201).json(service);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});


module.exports = router;