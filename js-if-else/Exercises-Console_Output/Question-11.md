Take two numbers as input from the user. Console  the number which is greater.

```javascript
// please write code here
```

```solution
let readlineaSync = require("readline-sync");
var number1=readlineaSync.questionInt("enter a number");
var number2=readlineaSync.questionInt("enter a number");
if(number1>number2){
   console.log("number1 is greater");
}
else{
   console.log("number2 is greater");
}
```

