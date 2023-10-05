function doSomething(){
    const el=document.getElementById('p1');
    el.style.color='blue';
    alert('blue is my favourite colour!');
}

const el=document.getElementById('myCanvas');
const ctx=el.getContext('2d');

ctx.beginPath();
ctx.lineWidth=7;
ctx.moveTo(100,300);
ctx.lineTo(300,300);
ctx.lineTo(300,100);
ctx.lineTo(200,50);
ctx.lineTo(100,100);
ctx.lineTo(100,300);
ctx.fillStyle='#EBF014';
ctx.fill();
ctx.stroke();

ctx.beginPath();
ctx.moveTo(100,100);
ctx.lineTo(80,110);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(300,100);
ctx.lineTo(320,110);
ctx.stroke();

ctx.beginPath();
ctx.arc(200,200,50,0,2*Math.PI);
ctx.fillStyle='#0096FF';
ctx.fill();
ctx.stroke();

ctx.beginPath();
ctx.rect(100,300,200,20);
ctx.fillStyle='#F014EC';
ctx.fill();
ctx.stroke();






