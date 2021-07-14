Program to check whether the given number is a prime or not?

```javascript
var n=require("readline-sync");
const num=n.question("enter number: ");
let i=2
var count=0;
while (i<num) {
       if (num%i===0) {
       count=count+1
       }
       i++;
}
if (count===0) {
       console.log("prime number")
}
else {
   console.log("not prime number")
}

// Output:
// enter number: 3
// prime number

```