If water in the filter is less than 1L then more water needs to be filled. If the water quantity is between 1L and 10L then there is no need to fill water. If water is more than 10L then the water will overflow. take user input in a variable named water .


```javascript
// please write code here
```

```solution
let readlineSync = require("readline-sync");
var water=readlineSync.questionInt("enter water level");
if (water<1){
   console.log("more water needs to fill");
}
else if (water>=1 && water<=10){
   console.log("no need to fill water");
}
else{
   console.log("overflow");
}
```