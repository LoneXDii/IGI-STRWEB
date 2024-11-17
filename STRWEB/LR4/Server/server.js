const express = require("express");
const mongoose = require("mongoose");
const port = 3001;
const routes = require("./routes/index");

main().catch((err) => console.log(err));

async function main() {
    const app = express();
    await mongoose.connect("mongodb://127.0.0.1:27017/expressdb");

    app.use(express.json());
    app.use("/api", routes);
  
    app.listen(port, () => {
      console.log(`Server is listening on port: ${port}`);
    });
}