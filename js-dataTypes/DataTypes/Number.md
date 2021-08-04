```ngMeta
name: Number
```


### Example:

```javascript
var a = 25;         // positive integer
var b = 80.5;       // floating-point number
var c = -2;         // negative number
```

Here in the above we stored a positive number i.e., 25 in a variable named a. 
The number data type is used to represent positive or negative numbers with or without decimal place.

The Number data type also includes some special values which are: Infinity, -Infinity and NaN. Infinity represents the mathematical Infinity ∞, which is greater than any number. Infinity is the result of dividing a nonzero number by 0, as demonstrated below:

### Example:

```javascript
console.log(16 / 0);  // Output: Infinity
console.log(-16 / 0); // Output: -Infinity
console.log(16 / -0); // Output: -Infinity
```

While NaN represents a special Not-a-Number value. It is a result of an invalid or an undefined mathematical operation, like taking the square root of -1 or dividing 0 by 0, etc.

```javascript
console.log("Nav Gurukul" / 2);       // Output: NaN
console.log("Dharamshala" / 2 + 10);  // Output: NaN
console.log(Math.sqrt(-1));         // Output: NaN
```