const express=require("express");
const app=express();

app.use(express.json());

app.post('/health-checkup',(req,res)=>{
  const kidneys=req.body.kidneys; //takes array
  if(!(kidneys==1 || kidneys==2)){
    res.status(411).json({
      "Msg": "Invalid input"
    })
    return;
  }
  res.send("You have "+kidneys+" kidneys.");
})

// Global Catches - for better error management
app.use((err,req,res,next)=>{
  res.json({
    "Msg": "Sorry somethings up with your server!"
  })
})

app.listen(3000);