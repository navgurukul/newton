- Take two numbers as input from the user in variables varx and vary.
- Check whether varx is divisible by vary.
- If yes, console  **Divisible** else console **Not Divisible**.

```javascript
// please write code here
```

```solution
let readlineaSync = require("readline-sync");
var varX=readlineaSync.questionInt("enter a number");
var vary=readlineSync.questionInt("enter a number");
if(varX%vary===0){
   console.log("Divisible");
}
else{
   console.log("Not divisible");
}
```