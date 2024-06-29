// //basic code

const express=require("express");
const app=express();

function sum(n){
  let sum=0;
  for(let i=1;i<=n;i++) sum+=i;
  return sum;
}

app.get('/',(req,res)=>{
  const n=req.query.n;
  const ans=sum(n);
  res.send("Your answer is "+ans);
})

app.listen(3000);