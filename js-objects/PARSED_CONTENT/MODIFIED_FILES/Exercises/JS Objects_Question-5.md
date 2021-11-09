Question-5_key1


Question-5_key2


Question-5_key3

 
Question-5_key4

 
Question-5_key5


```javascript
// please write code here
```

```solution
var readline = require('readline-sync');
let n =readline.question('Enter the property name:');
let dict={"name":"Raju", "marks":56}
for (i in dict){
if (i==n){
  console.log("exists");
  break
}else{
  console.log("not exist");
  break
}
}
```