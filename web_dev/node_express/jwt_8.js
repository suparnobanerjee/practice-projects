const express = require("express");
const jwt = require("jsonwebtoken");
const jwtPassword = "123456";
const app=express();

app.use(express.json());

const usersArray=[
  {
    username: "sparno@gmail.com",
    password: "123",
    name: "Suparno Banerjee"
  },
  {
    username: "rocky@gmail.com",
    password: "abc",
    name: "Rocky Balboa"
  },
  {
    username: "neo.matrix@gmail.com",
    password: "abc123",
    name: "Thomas Anderson"
  }
];

function userExists(username,password){
  for(let i=0;i<usersArray.length;i++){
    if(username==usersArray[i].username && password==usersArray[i].password){
      return true;
    }
  }
  return false;
}

app.post("/signin", function (req, res) {
  const username = req.body.username;
  const password = req.body.password;

  if (!userExists(username, password)) {
    return res.status(403).json({
      msg: "either username or password is incorrect",
    });
  }

  let token = jwt.sign({ username: username }, jwtPassword);
  return res.json({
    token
  });
});

app.get("/users", function (req, res) {
  const token = req.headers.authorization;
  try {
    const decoded = jwt.verify(token, jwtPassword);
    const username = decoded.username;
    res.json({
      users: usersArray.filter((value)=>{
        if(value.username==username){
          return false;
        }
        else {
          return true;
        }
      })
    });
  } catch (err) {
    return res.status(403).json({
      msg: "Invalid token",
    });
  }
});

app.listen(3050)