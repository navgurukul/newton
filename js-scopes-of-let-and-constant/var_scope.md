```ngMeta
name:var_scope
```
``` javascript
var myName="kumar"; // global scope
 
function sayHi(){
  console.log(myName); //output kumar
  var frdsName="Pavan";   // local scope or function scope
  console.log(frdsName); //output pavan
}
 
sayHi();
console.log(myName) //output kumar
console.log(frdsName) //output Error: ReferenceError: frdsName is not defined
```
##### //output
kumar
pavan
kumar
ReferenceError: frdsName is not defined

In the above example var myName is declared in outside of function and var frdsName is declared inside the function. 

The variable which is declared outside of the function has the global scope, we can access it anywhere in the code. 

The variable which is declared inside of the function has the local/function scope, we can access it in the function only. 

As you can see, we have used the variable myName inside sayHi function and also outisided using console.log(myName).

The variable frdsName has local scope since it is defined inside the sayHi function. So we can use it only inside the sayHi function. The moment we try to use it outside the sayHi function our programm throws an error that frdsName is not defined. Let's look at each line of the programme more carefully.

```javascript
var myName="kumar";
 
function sayHi(){
  console.log(myName);
  var frdsName="Pavan";
  console.log(frdsName);
}
 
sayHi();
console.log(myName);
console.log(frdsName);
 ```
 ##### Explantion
When the sayHi function is called  it prints  the console.log(myName) which is kumar. Since the variable myName has global scope we can use it inside the function. After that frdsName is declared inside the function and it prints because we wrote to console frdsName.

```javascript
var myName="kumar";
 
function sayHi(){
  console.log(myName);
  var frdsName="Pavan";
  console.log(frdsName);
}
 
sayHi();
console.log(myName);
console.log(frdsName);
```
 ##### Explantion
Then look at the line console .log(myName); it prints kumar because myName has the global scope.
myName is declared globally so we can use it inside the function or outside of the function too.

```javascript
var myName="kumar";
 
function sayHi(){
  console.log(myName);
  var frdsName="Pavan";
  console.log(frdsName);
}
 
sayHi();
console.log(myName);
console.log(frdsName);
 ```
 
##### Explantion:
Now Let's look at the line which is giving an error console.log(frdsName). Since frdsName is declared inside the function it has local scope it is limited to that function. But here we are trying to use that variable outside the function. Thus the programme gives us the error.

we are asking to print a local scope variable , 
After that it came to the line console.log(frds name); and it is trying to print frdsName but because of frdsName is declared inside the function it has local scope, it is not able to get that and throws an error frdsname is not defined.

When declared inside a function with var, the variable is scoped to that function.

#### Example:
 
```javascript
var myName="kumar";
console.log(myName);
myName="Nayak";
console.log(myName);
 ```
##### //output
kumar
Nayak
 
##### Explantion:
In the above example, we declared a variable myName and assigned kumar into it, and after that because of console.log(myName); it printed kumar. And after printing we updated that value to Nayak, so now myName contains the value Nayak.
 
We can update the var variables. Here myName is updated with a new value as Nayak.

#### Example:
 
 ```javascript
var myName = "Kumar";
console.log(myName)
var myName = "Kumar Nayak";
console.log(myName);
``` 
##### // output
Kumar
Kumar Nayak
 
 #### Explantion:
In the above example, we declared a variable myName and assigned kumar into it, and after that because of console.log(myName); it printed Kumar. And after printing we redeclared that variable and assigned Kumar Nayak to it, so now myName contains the value Kumar Nayak right now.
 
We can redeclare the variables with var. It won’t give any error.
