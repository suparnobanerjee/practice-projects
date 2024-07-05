const express=require('express');
const app=express();
const mongoose=require('mongoose');
const Product=require('./models/product.model.js');
const { configDotenv } = require('dotenv');
configDotenv();
const productRoute=require('./routes/product.route.js');

//middleware
app.use(express.json());

//routes
app.use('/api/products',productRoute);

app.get("/", (req, res) => {
  res.send("Hello from Node API Server Updated!");
});

mongoose.connect(process.env.MONGODB_URL).then(()=>{
  console.log("Connected to database!");
  app.listen(3000,()=>{
    console.log("Server is running on port 3000");
  });
})
.catch(()=>{
  console.log("Connection to DB failed!");
});

