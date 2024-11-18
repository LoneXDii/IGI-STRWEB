const express = require("express");
const router = express.Router();

const doctors = require('./doctors');
const orders = require('./orders');
const services = require('./services');
const specializations = require('./specializations');
const account = require('./account');

router.use("/doctors", doctors);
router.use("/orders", orders);
router.use("/services", services);
router.use("/specializations", specializations);
router.use("/account", account);

module.exports = router;