```ngMeta
name: Type Coercion
```

### Example:
```javascript
var name = "navgurukul";
var num = 29;
var result = name + num;
console.log(result);
// Output :  navgurukul29 

```
### Explanation:

If you look at the variable result, you may think that this variable is trying to add a string (navgurukul) to a number (29). But that is not the case, because you cannot add a string to a number. JS in such circumstances, will convert the number 29 into the string “29” and will join (or concatenate) the two strings.  

Thus the output of result will be **navgurukul29**  

### Note

This auto converting of a value from one type to another — such as number to string — in JS is called **Type Coercion**.  


### Example:
```javascript
var measure = "height";
var val = 16.5;
var result = measure + val;
console.log(result);

// Output :- height16.5

```
### Explanation:

If you look at the variable result, you may think that this variable is trying to add a string (height) to a float (16.5). But that is not the case, because you cannot add a string to a number. JS in such circumstances, will convert the float 16.5 into the string “16.5” and will join (or concatenate) the two strings.  

Thus the output of result will be **height16.5**

### Note

This auto converting of a value from one type to another — such as float to string — in JS is called Type Coercion.

### Examples: 

1. What is the output of the following code?
```javascript
console.log(true + false)

// Output : 1

```
### Explanation:

1 is considered to be true because it is non-zero. Thus the reason true  value is 1, False value is 0. It will compute true+false as 1+0 and prints 1.


2. What is the error in this program?
```javascript
var num=24
var a="kumar"
console.log(24/"kumar")
// Output : NaN

```
### Explanation:

There is no error in this following code. But it will return a NaN, when a number is divided by non integer so it is not able to solve the problem.


