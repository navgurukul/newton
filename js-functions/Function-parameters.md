Parameters will work as variables in a function which will store arguments as values. 

Parameters are set on the first line of the function inside the set of parentheses, like this:

```javascript

function functionName(parameter1, parameter2, parameter3) {
 // Code to be executed
}

```

functionName(argument1, argument2, argument3);
 
You can specify parameters when you define your function to accept input values when your code is running. The parameters work like placeholder variables within a function; they're replaced at run time by the values (known as argument) provided to the function at the time of function calling. See  in the above example we are given 3 arguments when we are calling the function and accessing by the parameters like parameter1, parameter2, parameter3.

**Example:**

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

You can declare as many parameters as you want. However for each parameter you write, a corresponding argument needs to be passed to the function when it is called, if not passed its value becomes undefined. Let's consider the following example:

```javascript

// Defining function

function showFullname(firstName, lastName) {
 console.log(firstName + " " + lastName);
}
 
// Calling function
showFullname("Kumar", "Nayak"); // 0utputs: Kumar Nayak
showFullname("Shwetha"); // 0utputs: Shwetha undefined

```

