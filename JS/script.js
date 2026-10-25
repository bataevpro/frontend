console.log("миру мир");
const espresso = 200;
console.log(espresso);
const latte = 300;
const littleSize = 50;
const bigSize = 100;
const espressoBigSize = espresso + bigSize;
console.log(espressoBigSize);
function  calculateEspresso(Size) {
 const espresso = 200; 
 const littleSize = 50;
 const bigSize = 100;
 if (Size === "little") {
    return espresso+littleSize
     

 } else {
    return espresso+bigSize;
 }
}
console.log(calculateEspresso("little"));
console.log(calculateEspresso("big"));