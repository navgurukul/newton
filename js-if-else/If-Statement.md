```ngMeta
name: If statement
```

```javascript
if (condition is true) {
  statement is executed
}
```

If you want to run a piece of code, based on a certain condition, then you should use the if statement. The keyword if tells JavaScript to execute the code in the curly braces under certain conditions, that defined in the parentheses (). 

### Note: These conditions are known as Boolean conditions and they are only be true or false. 

When the condition evaluates to true, the program executes the statement inside the curly braces. When the Boolean condition evaluates to false, the statement inside the curly braces will not execute.

Let us see some more examples.

### Example:

```javascript
var a = 10;
var b = 12;
if(b > a){
  console.log( b," is greater than  ", a  );
}
// Output :- 12, is greater than, 10
```

### Explanation: 

Here 12 is greater than 10. So, the console will show us the output as 12, is greater than, 10.