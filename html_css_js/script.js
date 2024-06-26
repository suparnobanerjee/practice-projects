const fs=require('fs');
function readFile(cb){
    fs.readFile('a.txt','utf-8',function(err,data){
        cb(data);
    });
}
function displayData(data){
    console.log(data);
}
readFile(displayData)
function sumT100(){
    let sum=0;
    for(let i=1;i<=100;i++){
        sum+=i;
    }
    return sum;
}
const total = sumT100();
console.log(total);
console.log("Hello!")