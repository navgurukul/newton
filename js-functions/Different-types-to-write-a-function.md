```ngMeta
name: Different types to write a function
```

- **Name Function**

Earlier in this tutorial, you learned that functions are declared with the following syntax:

```javascript

function addNumbers(parameter1, parameter2) {
 // code to be executed
}

```

functionName(argument1 , argument2);

We can call a function with a name, like addNumbers above, any time we need it by referencing its name and passing some arguments to it. This function has a name. Named functions are useful if we need to call a function many times to pass different values to it or run it several times.


- **Function Expressions ( Anonymous function )**

```javascript

// Function Declaration

function getSum(num1, num2) {
 var total = num1 + num2;
 return total;
}

```

Here we have just declared the function getSum. We haven’t called it yet. Declared functions are not executed immediately. They are "saved for later use", and will be executed later, when they are invoked (called upon).
 
```javascript

// Function Expression

var getSum = function(num1, num2) {
 var total = num1 + num2;
 return total;
};

```

Notice how in the function declaration above we will declare function by writing a function and do the tasks, but in function expressions we will assign to it a variable and perform tasks.

The syntax that we've used before to create functions is called function declaration. There is another syntax for creating a function that is called a function expression. A function expression can be stored in a variable:

**Example:**

Functions stored in variables do not need function names. They are always invoked (called) using the variable name.

```javascript

var getSum = function(num1, num2) {
 var total = num1 + num2;
 return total;
};
 
console.log(getSum(5, 10)); // 0utputs: 15
 
var sum = getSum(7, 25);
console.log(sum); // 0utputs: 32

```

The function above is actually an anonymous function (a function without a name).

**Exercises:**

Define an Anonymous function and call it by taking two arguments to whether they are       equal or not?

Feedback after Submit
```javascript
var isEqual = function(str1,str2){
   console.log(str1===str2)
}
isEqual("kumar","nayak");

```
- **Self-Invoking Functions ( Immediately invoked function expression)**

You have to add parentheses around the function to indicate that it is a function expression:

```javascript

(function myName () {
 var x = "Hello!! Nayak";  // I will invoke myself
 console.log(x);
})();
 
Output :-
Hello!! Nayak

```
 
**Explanation:**

As we see in the example, we are not giving names and not storing the function in any variable. We are declaring it after that we are accessing it using parentheses. So, output is showing Hello!! Nayak

A self-invoking expression is invoked (started) automatically, without being called.
Function expressions will execute automatically if the expression is followed by ().
You cannot self-invoke a function declaration.

**Exercises:**

1.Define an Self invoking function and call it by taking two arguments to whether they are  equal or not?

Feedback after submit
```javascript
(function(str1,str2){
   console.log(str1===str2)
})("kumar","kumar");
```