Question-12_key1


- Question-12_key2
- Question-12_key3
```javascript
// please write code here
```

```solution
let readlineaSync = require("readline-sync");
var number=readlineaSync.questionInt("enter a number");
if(number%5===0 && number%15===0){
   console.log("Divisible by both");
}
else{
   console.log("Not divisible by both");
}
```