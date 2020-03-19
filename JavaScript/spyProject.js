var firstName = prompt("What is your first name?: ");
var lastName = prompt("What is you last name?: ");
var age = prompt("How old are you?: ");
var height = prompt("How tall are you in centimeters?: ");
var petName = prompt("What is your pet's name?: ");
alert("Thank you so much for the information!")
//All condtions need to be true for the spy to be discovered
//All with start off as null or false
var nameCond = null
var ageCond = null
var heightCond = null
var petCond = null

//Check nameCond
if (firstName[0] === lastName[0]){
  nameCond = true;
}else {
  nameCond = false;
}

//Spy is between the ages 20 and 30
if (age > 20 && age < 30){
  ageCond = true;
}else{
  ageCond = false;
}

//Spy is at least 170 cm tall
if (height >= 170){
  heightCond = true;
}else{
  heightCond = false;
}

//Spy has pet name that ends in the letter 'Y'
if (petName[petName.length-1] === "y"){
  petCond = true;
} else{
  petCond = false;
}

//Check for all four conditions
if(nameCond && ageCond && heightCond && petCond){
  //My secret message
  console.log("Welcome Comrade! You've passed the spy test!")
}else{
  console.log("Sorry,nothing to see here.")
}
