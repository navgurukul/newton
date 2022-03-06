```ngMeta
name: Function parameters
```

Parameters will work as variables in a function which will store arguments as values. 

Parameters are set on the first line of the function inside the set of parentheses, like this:

```javascript

function functionName(parameter1, parameter2, parameter3) {
 // Code to be executed
}

functionName(argument1, argument2, argument3);

```

 
You can specify parameters when you define your function to accept input values when your code is running. The parameters work like placeholder variables within a function. They're going to replaced at run time by the values (known as argument) provided to the function at the time of function calling. See  in the above example we are given 3 arguments when we are calling the function and accessing by the parameters like parameter1, parameter2, parameter3.

### Example:

```javascript
// Defining function
function displaySum(num1, num2) {
 var total = num1 + num2;
 console.log(total);
}
 
// Calling function

displaySum(6, 20); // 0utputs: 26
displaySum(-5, 17); // 0utputs: 12
```

### Example:

```javascript

// Defining function

function showFullname(firstName, lastName) {
 console.log(firstName + " " + lastName);
}
 
// Calling function
showFullname("Kumar", "Nayak"); // 0utputs: Kumar Nayak
showFullname("Shwetha"); // 0utputs: Shwetha undefined

```

### Explanation:

In function parameters we given two named as firstName, lastName but when we calling a function we need to pass arguments there we passed only one that is Shwetha and if we are not passing an argument the parameter which is responsible for getting the value, it won't get anything and it has undefined in it, so it prints  **Shwetha undefined** as output.


#### Note:

You can declare as many parameters as you want. However for each parameter you write, a corresponding argument needs to be passed to the function when it is called, if not passed its value becomes undefined. 


### Exercises:

1. Write a function name it as displayMultiply() and pass 3 parameters and in runtime take the arguments with the names num1, num2, num3 and multiply them and return the result?

```javascript
// write code here
```

```solution
function displayMultiply(num1, num2, num3) {
   return num1*num2*num3
  }
  
console.log(displayMultiply(2, 3, 4));
```

2. What is the output of the following code?

```javascript
function getResult(num1,num2,num3,num4){
 console.log(num1-num2+num3-num4)
}
 
getResult(2,3,4,5);
```

```solution
-2
```

3. What is the error in this code?
```javascript
function getResult(num1,num2,num3){
 console.log(num1-num2+num3)
}
 
getResult(2,3,4,5);
```

```solution
No error. Even though an extra parameter (5) is passed, the function getResult simply does not use it.	
```


4. Write a program that will take two parameters and print its sum?


```javascript
// write code here
```

```solution
function SumOfNumbers(num1,num2){
   return num1+num2;
}
SumOfNumbers(1,2);
```


5. What is the output of the following code?

```javascript
function displayMultiply(a,b){
   console.log(a*b);
}
displayMultiply(2,3);
```

```solution
6
```

6. What is the error in the following code?

```javascript
	function displaySubtraction(a,b){
   console.log(ab);
}
displySubraction(2,3);
```

```solution
ReferenceError: display Subtraction is not defined

The function name is not matched with the calling name so it is given Reference Error.
```


