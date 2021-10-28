```ngMeta
name: switch statements
```
### Syntax
``` javascript
switch(condition) {
   case x:
   	  // code block
      break;
   case y:
      // code block
      break;
   default:
     // code block
}
```

### How default case works

#### Example:

```javascript
var num = "w"
switch (true){
   case num > 0:
       console.log("It is a positive number")
       break;
   case num < 0:
       console.log("It is a negative number")
       break;
   case num == 0:
       console.log("It is a zero")
       break;
   default:
       console.log("Invalid input")
}
```
### Explantion

Here the program will take user input ,this statement is very first;

Then it move to the switch statement where it is mentioned switch (true);

Then it  moves to the case 1 that is num is greater than zero and if that mentioned case is not similar to the case so it will directly jump to the case 2.
 
Here in case 2 it will again check whether num is less than zero is not similar to num above so it will directly jump to the case 3.

Here is case 3 it will again check whether num is equal to zero is not similar to num which is user input, so it will directly jump to the default case value and console "invalid input".
