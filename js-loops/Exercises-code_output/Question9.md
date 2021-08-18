Create a loop that takes 10 numbers as input from the user. 

After taking the input console the sum of all those numbers. 

This program will go like this. Each time using readline-sync will take a number input from the user.  

Sample : input 10

Then for example 10+16+9+10+56+78+98+43+21+76.. Total sum of number 417 

Sample : output  417


```javascript
// please write code here
```

```solution
var sum = 0;
for (var i = 1; i <= 10; i++){
  const input = require('readline-sync');
  let number = input.questionInt('Enter the number');
  sum = sum +number
};
console.log(sum);
```