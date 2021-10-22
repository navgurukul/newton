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
``` javascript 

var day = "Holiday"
 
switch (day) {
  case "Sunday":
      console.log("Meeting with curriculum team")
  	 break;
 
  case "Wednesday":
       console.log("Meeting with academics team")
  	  break;
 
  case "Tuesday":
       console.log("Normal working day")
  	  break;
 
  default:
       console.log("invalid input")
}
```
### Explanation:

Here the program will check  var day = "Holiday" this statement very first;

Then it move to the switch statement where it is mentioned switch (day);

Then it moves to the case 1 that is "Sunday" is not equal to day(Holiday) and that means the day mentioned is not similar to the case so it will directly jump to the case 2.

Here in case 2 it will again check whether "Wednesday" is similar to the day mentioned above. This time it will not find the similar input as mentioned to the variable. It will jump to case 3.

Here in case 3 it will again check whether "Tuesday" is similar to the day mentioned above. This time also it will not find the similar input as mentioned to the variable. It will jump to the default case value and console "invalid input".
