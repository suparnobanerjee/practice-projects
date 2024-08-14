// console.log(100); //console is object, log is method. Every object has a method and property. Property is the value and method is the function. '.' is used to call method inside object.
// console.log('Hello world!');
// console.table({Name: 'Ratul', Age: 26})


// console.group('simple');
// console.log(150);
// console.error('Alert');
// console.warn('Warning');
// console.groupEnd();


// const styles = 'padding: 10px; background-color: white; color: red';
// console.log('%cStyles',styles);


// //vaiable declaration: let, var, const
// let a=20;
// let b=30;
// console.log(a+b);

// const arr=[1,2,3,4,5];
// arr.push(6);
// console.log(arr);

// const person = {
//   name: 'Suparno'
// };
// person.name='Ratul';
// console.log(person);

// //JS is a dynamically typed language unlike typescript, which means defining the type of variable before declaration is NOT important. It makes it less verbose and more prone to errors relative to typescript.


// console.log("Name: %s",person.name);

// var cubes = 'ABCDEFG';
// //styling console output using CSS with a %c format specifier
// for (var i = 0; i < cubes.length; i++) {
//     var styles = "font-size: 40px; border-radius: 10px; border: 1px solid blue; background: pink; color: purple";
//     console.log("%c" + cubes[i], styles)
// }

// let carObj = {
//     year: 2024,
//     model: "Verna",
//     tspeed: 140
// }
// let carArr=['tspeed','model'];
// for(let i=0;i<carArr.length;i++){
//     console.log(carObj[carArr[i]]);
// }
 
// const person = '{"name":"A", "age":25, "gender": "Male"}'
// const user = JSON.parse(person)
// console.log(user["gender"]);