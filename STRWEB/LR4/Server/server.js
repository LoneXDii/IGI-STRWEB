require("express-async-errors");
const express = require("express");
const mongoose = require("mongoose");
const port = 3001;
const routes = require("./routes/index");
const exceptionMiddleware = require("./middleware/exceptionsMiddleware");
const passport = require('passport');
const passportConfig = require('./config/passrot');

main().catch((err) => console.log(err));

async function main() {
    const app = express();
    passportConfig(passport);
    app.use(passport.initialize());
    await mongoose.connect("mongodb://127.0.0.1:27017/expressdb");
    app.use(express.json());

    app.get('/protected', passport.authenticate('jwt', { session: false }), (req, res) => {
      res.json({ message: 'This is a protected route', user: req.user });
    });

    app.use("/api", routes);
    app.use(exceptionMiddleware);
  
    app.listen(port, () => {
      console.log(`Server is listening on port: ${port}`);
    });
}