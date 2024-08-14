const express = require("express");
const app = express();

// // dumb way
// app.get("/health-checkup",(req,res)=>{
//   const username=req.headers.username;
//   const pass=req.headers.pass;
//   const kidneyID=req.query.kidneyID;
//   if(username!="sparno" || pass!="123"){
//     res.status(403).json({
//       "Message": "Somethings up with your input!"
//     })
//     return;
//   }
//   if(kidneyID!=1 && kidneyID!=2){
//     res.status(403).json({
//       "Message": "Somethings up with your input!"
//     })
//     return;
//   }
//   res.json({
//     "Message": "You are healthy!"
//   })
// });
// app.listen(3000);


// smart way (using middlewares)
function userMiddlewares(req,res,next){
  const username=req.headers.username;
  const pass=req.headers.pass;
  if(!(username=="sparno" && pass=="123")){
    res.status(403).json({
      "Message": "Somethings up with your input!"
    })
    return;
  }
  else{
    next();
  }
};
function kidneyMiddlewares(req,res,next){
  const kidneyID=req.query.kidneyID;
  if(!(kidneyID==1 || kidneyID==2)){
    res.status(403).json({
      "Message": "Somethings up with your input!"
    })
  }
  else{
    next();
  }
};
app.get('/health-checkup',userMiddlewares,kidneyMiddlewares,(req,res)=>{
  res.send("You are healthy!");
})
app.get('/kidney-check',userMiddlewares,kidneyMiddlewares,(req,res)=>{
  res.send("Your kidneys are healthy!");
})
app.get('/heart-check',userMiddlewares,(req,res)=>{
  res.send("Your heart is healthy!");
})
app.listen(3000);