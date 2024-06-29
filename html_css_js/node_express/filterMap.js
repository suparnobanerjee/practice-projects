// using normal function
const arr=[1,2,3,4,5,6,7,8,9,10];
const newArr=[];
for(let i=0;i<arr.length;i++){
  if(arr[i]%2==0){
    newArr.push(arr[i]);
  }
}
console.log(newArr); // [2,4,6,8,10]

// // using filter and custom map function
// const arr=[1,2,3,4,5,6,7,8,9,10];
// const map=(arr,fn)=>{
//   const newArr=[];
//   for(let i=0;i<arr.length;i++){
//     newArr.push(fn(arr[i]));
//   }
//   return newArr;
// };
// const newArr=map(arr,num=>num%2===0?num:null).filter(num => num !== null); 
// console.log(newArr);

// // using just filter function
// const arr=[1,2,3,4,5,6,7,8,9,10];
// const newArr=arr.filter(num=>num%2==0);
// console.log(newArr);

// // A seperate example showing the implementation of map function
// const arr=[1,2,3,4,5,6,7,8,9,10];
// const newArr=arr.map(num=>num * 2);
// console.log(newArr);