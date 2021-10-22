```ngMeta
name: switch statements
```
### Switch Statement
The switch statement evaluates an expression, matching the expression's value to a case clause, and executes statements associated with that case, as well as statements in cases that follow the matching case.
Expression 
An expression whose result is matched against each case clause.

### Example:
``` javascript
var day = "Wednesday"
 
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
The above example shows here the meetings scheduled of a person according to the days. Here in this situation the user wants to find that on "Wednesday" with whom he has a meeting? By using this switch statement program it will show "Meeting with academics team".  As on "Wednesday"  it is already mentioned in the schedule which we are depicting with the help of the switch statement mentioned above.

Here the program will check  var day = "Wednesday" this statement very first;

Then it move to the switch statement where it is mentioned switch (day);

Then it moves to the case 1 that is "Sunday" is not equal to day(Wednesday) and that means the day mentioned is not similar to the case so it will directly jump to the case 2.

Here in case 2 it will again check whether "Wednesday" is similar to the day mentioned above. This time it will find the similar input as mentioned in case 2. So it will console the statement mentioned inside the case that is "Meeting with academics team" ;

Then it will check the next statement which is break; and as you all know break statements help in breaking the flow of a program it will come out of the flow and the program ends.

Note :- Here after the each case break; statement is there because we don’t want it to check the whole program, once it will get the right case it will break the flow and come out of the program and this is the reason that it works faster than the if-else statements which you have read in the basics doc already.
