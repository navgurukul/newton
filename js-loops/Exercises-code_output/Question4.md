Program to print table of a given number

```javascript
let n=require("readline-sync");
let num=parseInt(n.question("enter number: "));
for (let i=1;i<=10;i++) {
       multi=num*i;
       console.log(num + "*" + i + "=" + multi)
   }
	
// Output:

// enter number: 2
// 2*1=2
// 2*2=4
// 2*3=6
// 2*4=8
// 2*5=10
// 2*6=12
// 2*7=14
// 2*8=16
// 2*9=18
// 2*10=20

```