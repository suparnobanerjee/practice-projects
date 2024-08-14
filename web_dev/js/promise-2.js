// // simple callback function
// function myFun(fn, duration){
//   setTimeout(fn,duration);
// }
// myFun(() => console.log("Done!"),3000);
// console.log("print immediately");



//using promise
function myFun(duration){
  const p = new Promise((resolve) => setTimeout(resolve,duration));
  return p;
}
// const ans=myFun(3000);
// ans.then(() => console.log("Hello there")); // faster and concise, but can lead to "callback hell"

// better for scalability and readability
async function main(){
  const ans = await myFun(3000);
  console.log("Hello there!");
}

main()

