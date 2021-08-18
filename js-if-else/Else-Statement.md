```ngMeta
name: Else statement
```

If any “ if ”  condition is false then an “else” statement comes into the picture.

### Example:
```javascript
var a = 10;
var b = 12;
if(a > b){
console.log(a," is greater than ",b);
}
else {
console.log(b," is greater than " ,a);
}

// Output :- 12 is greater than 10

```

### Explanation: 

In this example a value is 10, and b value is 12, after that it comes to check condition a>b means 10>12 which is false. Because of condition is false it won't execute the code that is written isnde curly braces, it will goes to the next statement that is else. So, else statement will execute b," is greater than " ,a means 12 is greater than 10.



### Example: 

Write a program to find the maximum between two numbers.

```javascript
var num1= 10;
var num2 = 20;
 
if(num1>num2){
   connsole.log("num1 is greater than num2");
}
else{
   console.log("num2 is greater than num1");;
}

// output: "num2 is greater than num1"

```

### Explanation:

The condition that we given num1> num2  which is false because num1 (10) which is not greater than num2(20). So, if condition is false it will go to execute else condition and print the num2 is greater than num1.
