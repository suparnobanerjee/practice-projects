const express=require("express");
const mongoose=require("mongoose");
const app=express();
app.use(express.json());

mongoose.connect("mongodb+srv://sparno:test123@cluster0.orvmkhm.mongodb.net/");

const Users=mongoose.model('User',{
  username: String,
  email: String,
  password: String
});

app.post('/signup',async(req,res)=>{
  const username=req.body.username;
  const email=req.body.email;
  const password=req.body.password;
  const checkUser=await Users.find({
    username: username
  });
  if(checkUser){
    return res.status(400).send("Username already exists!");
  }
  const user=new Users({
    username: username,
    email: email,
    password: password
  });
  user.save();
  res.json({
    "Msg": "User profile created successfully!"
  })
});

