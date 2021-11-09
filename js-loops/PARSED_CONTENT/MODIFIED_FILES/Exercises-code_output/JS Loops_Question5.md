Question5_key1


Question5_key2


Question5_key3


Question5_key4


```javascript
// please write code here
```

```solution
const n=require("readline-sync");
var name=n.question("enter name: ")
const store=name;
var string=""
for (let i=name.length-1;i>=0;i--) {
  string=string+name[i]
}
if (store===string) {
  console.log("its palindrome string")
}
else {
  console.log("it's not a palindrome string")
}

```