## Undefined


**Undefined:**
```javascript
var a;
var b = "Hello World!"
console.log(a) // Output: undefined
console.log(b) // Output: Hello World!
```
variable a is just declared and not assigned any value in it, whenever you will try to print before assigning a vlaue you will get undefined.

variable b is declared and assigned a value i.e., Hello World!

The **undefined** data type can only have one value-the special value undefined. If a variable has been declared, but has not been assigned a value, has the value undefined.

**Exercises:**

1. Write a program that prints undefined when I print with its variable name?
```javascript
var z;
console.log(z);
```
2. What is the output of the following code?

```javascript
var n;
console.log(n);
```
output:undefined

3. What is the error in the following code?
```javascript
var x=3;
console.log(X);
```
output: ReferenceError: X is not defined 

Because X is not defined here, JS is case sensitive so that's this x and this X is different.
