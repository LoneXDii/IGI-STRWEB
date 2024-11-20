const express = require("express");
const router = express.Router();
const passport = require('passport');

const Specialization = require("../models/specialization");

router.post("/", passport.authenticate('jwt', { session: false }), async (req, res) => {
    try {
        if (req.user.role.normalized_name !== "admin"){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }

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

router.delete("/:id", passport.authenticate('jwt', { session: false }), async (req, res) => {
    try {
        if (req.user.role.normalized_name !== "admin"){
            res.status(403).json({ message: "You have no access to do this" });
            return;
        }

        await Specialization.deleteOne({ _id: req.params.id });
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