Given a string, write a program to check if it is palindrome or not. 

A string is said to be palindrome if the reverse of the string is the same as the string. 

For example :

“RADAR” is a palindrome, but “RADIX” is not a palindrome

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