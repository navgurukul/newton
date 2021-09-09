## The typeof function

```javascript
    typeof 15;  // Returns: "number"
    typeof (42.7);  // Returns: "number"
    typeof “Nayak”;  // Returns: "string"
```

The typeof operator can be used to find out what type of data a variable or operand contains. 

The typeof can be used with or without parentheses (typeof(x) or typeof x). 
In the example given above, the operand contains 15 so it returns the type of that operand i.e., number.

The typeof operator is particularly useful in the situations when you need to process the values of different types differently, but you need to be very careful, because it may produce unexpected result in some cases, as demonstrated in the following example:

// Null
```javascript
typeof Null;  // Output: "object"
```

**Explanation:**

As you can clearly see in the above example when we test the null value using the typeof operator , it returns "object" instead of "null".
This is a long-standing bug in JavaScript, but since lots of codes on the web are written around this behavior, and thus fixing it would create a lot more problems, so the idea of fixing this issue was rejected by the committee that design and maintains JavaScript.

// Numbers
```javascript
typeof 15;  // Output: "number"
typeof 42.7;  // Output: "number"
typeof 5.5e-6;  // Output: "number"
typeof Infinity;  // Output: "number"
typeof NaN;  // Output: "number". Despite being "Not-A-Number"
```
// Strings
```javascript
typeof '';  // Output: "string"
typeof 'hello';  // Output: "string"
typeof '12';  // Output: "string". Number within quotes is typeof string
```
// Booleans
```javascript
typeof true;  // Output: "boolean"
typeof false;  // Output: "boolean"
```
// Undefined
```javascript
typeof undefined;  // Output: "undefined"
typeof undeclaredVariable; // Output: "undefined"
```
// Objects
```javascript
typeof {name: "John", age: 18};  // Output: "object"
```
// Arrays
```javascript
typeof [1, 2, 4];  // Output: "object"
```
// Functions
```javascript
typeof addNumbers(){};  // Output: "function"
```