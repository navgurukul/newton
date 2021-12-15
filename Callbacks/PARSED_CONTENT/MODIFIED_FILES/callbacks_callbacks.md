callbacks_key1


```javascript
// Create a function that accepts another function as an argument
 
const callbackWaalaFunction = (fn) => {
  // Calls the function with any required arguments
 
  return fn("kumar", 24, "chocolates")
}
// Callback gets arguments from the above call
 
const myDescription = (arg1, arg2, arg3) => {
 
  return "My name is "+arg1+" and I am "+arg2+"years old"+". I like "+arg3
}
// Passing a callback into a callback accepting function
 
const result = callbackWaalaFunction(myDescription)
console.log(result) // My name is kumar and I am 24years old. I like chocolates
```
 
callbacks_key2

 
callbacks_key3

 
callbacks_key4


 
callbacks_key5


callbacks_key6

 
callbacks_key7
```javascript
function Gurukul(){
   console.log("I am Navgurukul");
}
 
function Nav(callback){
   console.log("I am Nav");
   callback();
}
 
Nav(Gurukul);  //I am Nav I am Navgurukul
```

callbacks_key8
```javascript 
let calc= function (num1,num2,calcType){
  
   if (calcType=="add"){
       return num1+num2;
   }
   else if(calcType =="multiply"){
       return num1*num2;
   }
}
 
console.log(calc(2,3,"add"));
 
//Output
5
```

callbacks_key9

 
```javascript
let add = function(num1,num2){
   return num1+num2;
}
 
let multiply= function(num1,num2){
   return num1*num2;
}
 
let calc= function (num1,num2,callback){
   console.log(callback(num1,num2));
}
 
calc(2,3,add);
calc(2,3,multiply);
 
//output
5
6
```