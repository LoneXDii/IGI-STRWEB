require("express-async-errors");
const express = require("express");
const mongoose = require("mongoose");
const port = 3001;
const routes = require("./routes/index");
const exceptionMiddleware = require("./middleware/exceptionsMiddleware");
const passport = require('passport');
const passportConfig = require('./config/passrot');
const cors = require('cors');

const authRouter = require('./routes/oauth');
const googleRouter = require('./routes/google');

main().catch((err) => console.log(err));

async function main() {
    const app = express();
    passportConfig(passport);
    app.use(passport.initialize());
    await mongoose.connect("mongodb://127.0.0.1:27017/expressdb");
    app.use(express.urlencoded({ extended: true }));
    app.use(express.json());

    const corsOptions = {
      origin: ['http://localhost:3000', 'http://127.0.0.1:3000'],
      methods: ['GET', 'POST', 'PUT', 'DELETE'],
      credentials: true,
  };
    app.use(cors(corsOptions));

    app.get('/protected', passport.authenticate('jwt', { session: false }), (req, res) => {
      res.json({ message: 'This is a protected route', user: req.user });
    });

    app.use("/api", routes);
    app.use('/oauth', authRouter);
    app.use('/google', googleRouter);
    app.use(exceptionMiddleware);
  
    app.listen(port, () => {
      console.log(`Server is listening on port: ${port}`);
    });
}