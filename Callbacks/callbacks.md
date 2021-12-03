```ngMeta
name: Callbacks
```

The example below shows you how to write a callback function and a callback-accepting function:

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
 
callbackWaalaFunction is a function which accepts one more function as a parameter i.e., fn and then called inside that like fn(1,2,3) and it went to perform some task as per that function.
 
A callback function is a function (it can be any name function, anonymous function or an arrow function) passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action given. (Developers say you “call” a function when you execute a function, which is why callbacks are named callbacks)
 
const result = callbackWaalaFunction(myDescription)
Notice in this line, when you pass a callback function (i.e. myDescription) into another function (callbackWaalaFunction), you only pass the reference to the call back without executing it. This is why myDescription does not have any parenthesis next to it.

 
You only invoke (call) the callback in the callbackWaalaFunction. When you do so, you can pass any number of arguments that the callback may require:

Phew! That’s the basic idea for callbacks! Just remember that passing a function into another function is called callback
 
**Example:**
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

**Example:**
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

If this calc function is in a library, the user needs to use the whole syntax for any kind of operation, so the best way to do it is to abstract into a tiny function and here callback plays a prominent role.
 
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
