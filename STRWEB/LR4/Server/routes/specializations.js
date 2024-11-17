const express = require("express");
const router = express.Router();

const Specialization = require("../models/specialization");

router.post("/", async (req, res) => {
    try {
        const specialization = new Specialization(req.body);
        await specialization.save();     
        res.status(201).json(specialization);
    } catch(err) {
        res.status(400).json({ message: err.message });
    }
});

router.get("/", async (req, res) => {
    const specializations = await Specialization.find();
    res.status(200).json(specializations);
});

router.get("/:id", async (req, res) => {
    try {
        const specialization = await Specialization.findOne({ _id: req.params.id });

        if(specialization === null){
            res.status(404).json({ message: "No such specialization" });
        }

        res.status(200).json(specialization);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.delete("/:id", async (req, res) => {
    try {
        await Specialization.deleteOne({ _id: req.params.id });
        res.status(204).send();
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

router.patch("/:id", async (req, res) => {
    try {
        const specialization = await Specialization.findOne({ _id: req.params.id });

        if (req.body.name) {
            specialization.name = req.body.name;
        }
        if (req.body.normalized_name) {
            specialization.normalized_name = req.body.normalized_name;
        }
        
        await specialization.save();
        res.status(200).json(specialization);
    } catch(err) {
        res.status(404).json({ message: err.message });
    }
});

module.exports = router;