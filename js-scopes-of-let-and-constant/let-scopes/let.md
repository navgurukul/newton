```ngMeta
name:let
```

```javascript
{
   let num=10;
   console.log(num);
}
console.log(num);
```
 
##### Output: 10
ReferenceError: num is not defined

#### Explanation: 
Here we used curly braces for creating a block, inside that we declared a variable with let and printed num, it gives us 10, but outside of the block it won’t work, because of that it will give a reference error.

we use let for variable declarations too. Let is block scoped. It is limited upto a some place only.

Block means the set of rules that are written inside curly braces.

##### Example:
 
 ```javascript
isHeUsingAtm = true
if (isHeUsingAtm){
  let secretPin=1234
  console.log('please use Atm');
  console.log('while using Atm :'+secretPin);
  console.log('Thank you for using Atm');
}
console.log('After using Atm :'+ secretPin);
 ```
##### Output:
please use Atm
while using Atm :1234
Thank you for using Atm
ReferenceError: secretPin is not defined
 
#### Explanation: 
Here in this code secretPin is declared with let and because of let is block scoped. That's why when you tried to print console.log('After using Atm :'+ secretPin) outside of the if block also it didn’t work. This is the behaviour we want there in the atm. But this won’t be possible with var in if and for, while blocks.
 
I want to give a clarity here, the same kind of behaviour you will get with var also in function block but it won’t be possible with if and for, while blocks etc.,
 
#### Example:
 
 ```javascript
isHeUsingAtm = true
function UsingAtm(){
   if (isHeUsingAtm){
       var secretPinWithVar=1234
       console.log('please use Atm with secretPinWithVar');
       console.log('while using Atm with secretPinWithVar :'+secretPinWithVar);
       console.log('Thank you for using Atm with secretPinWithVar ');
}}
 
UsingAtm()
console.log('After using Atm :'+ secretPinWithVar);
```
 
### NOTE: 
var is function scoped when a variable with var is defined inside a function it will act as a local to that function and not be able to use that variable outside of the function. And if var is declared outside anywhere in the code that will act as a global variable and can be used anywhere in the code.
 
 #### Expalantion:
In this example your atm is not stored at all after you are using atm, this happened because you created a variable secretPinWithVar inside a function which means it is locally scooped inside a function and you can’t get that outside of function.

#### Example:
 
 ```Javascript
let myCampus = "Navgurukul Dharamshala Campus";
myCampus = "Navgurukul Sarjapur Campus";
 ```
We can update the let variables. Let will allow us to update the variables as same as var.
 
#### Example:
 
 ```javascript
let myCampus = "Navgurukul Dharamshala Campus";
let myCampus = "Navgurukul Sarjapur Campus";
```
 
// SyntaxError: Identifier 'myCampus' has already been declared
 
It will throw an error because the variables with let can’t redeclare

