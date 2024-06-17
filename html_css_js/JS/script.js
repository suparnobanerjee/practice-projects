console.log(100); //console is object, log is method. Every object has a method and property. Property is the value and method is the function. '.' is used to call method inside object.
console.log('Hello world!');
console.table({Name: 'Ratul', Age: 26})


console.group('simple');
console.log(150);
console.error('Alert');
console.warn('Warning');
console.groupEnd();


const styles = 'padding: 10px; background-color: white; color: red';
console.log('%cStyles',styles);


//vaiable declaration: let, var, const
let a=20;
let b=30;
console.log(a+b);

const arr=[1,2,3,4,5];
arr.push(6);
console.log(arr);

const person = {
  name: 'Suparno'
};
person.name='Ratul';
console.log(person);

//JS is a dynamically typed language unlike typescript, which means defining the type of variable before declaration is NOT important. It makes it less verbose and more prone to errors relative to typescript.


