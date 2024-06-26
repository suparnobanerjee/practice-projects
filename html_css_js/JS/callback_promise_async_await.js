// // using call-back
// function myAsyncFn(callback){
//   //some logic here
//   return callback("Hello!");
// }
// async function main(){
//   myAsyncFn(function(value){
//     console.log(value);
//   })
// }
// main()


// // using promise
// function myAsyncFn(){
//   const p = new Promise(function(resolve){
//     //some logic here
//     return resolve("Hi there!");
//   });
//   return p;
// }
// async function main(){
//   myAsyncFn().then(function(value){
//     console.log(value);
//   });
// }
// main()

//using async-await
function myAsyncFn(){
  const p = new Promise(function(resolve){
    //some logic here
    return resolve("Whats up!");
  });
  return p;
}
async function main(){
  const value=await myAsyncFn();
  console.log(value);
}
main()
console.log("This should be printed before main function!")
