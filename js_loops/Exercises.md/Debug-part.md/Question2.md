Print the maximum number in between the numbers given by user?

```js
let c=require("readline-sync");
let loop_time=c.question("enter loop time: ");
 
var maxi=0;
let lis=[ ]
for (let i=1;i<=loop_time;i++) {
   let num=c.question("enter number: ")
   lis.append(num)
}
var maxi=lis[0];
for (let j=0;j<lis:length;j==) {
   if (maxi<lis[j]) {
       [maxi=lis[j]]
   }
 
}
console.log(maxi)

```