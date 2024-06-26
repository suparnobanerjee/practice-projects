function myFun(duration){
  const p = new Promise((resolve) => setTimeout(resolve,duration));
  return p;
}
const ans=myFun(3000);
ans.then(() => console.log("Hello there"));