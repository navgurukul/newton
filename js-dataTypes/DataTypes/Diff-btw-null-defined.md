```ngMeta
name: Null vs Undefined
```


### Example:

```javascript
var empty = null;
console.log(empty); // Output: null
console.log(typeof(empty)); // Output: object
```

### Explanation:

Null is the value which we can assign to a variable and it means nothing. As you can see in the above example we have assigned a value “null” to a variable named “empty”. when we check the type of it, It will show us its type as object, which is the by default error in javascript which should not be there, but it can’t be changed also. 


Where as,

### Example:

```javascript
var notDefined;
console.log(notDefined); // Output: undefined
console.log(typeof(notDefined)); // Output: undefined
```

### Explanation:

Here in notDefined variable we have declared a variable but didn’t assign a value to it which means the variable is there but nothing is stored in it, so when we try to console it the output will be “undefined” as it is not defined yet. Here the value of a variable is not defined so it shows the type also as undefined.
