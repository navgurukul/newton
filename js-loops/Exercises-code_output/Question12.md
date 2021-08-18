Write a program to take 10 user input, and print the sum of that 10 inputs.

#### Note:  

For this program you need to initialize with 50, and try to use decrement and run loop.

Program may run like this. Everytime by using readline sync we will take an input.

Koi bhi number daaliye > 10

Koi bhi number daaliye > 16

Koi bhi number daaliye > 9

Koi bhi number daaliye > 10

Koi bhi number daaliye > 56

Koi bhi number daaliye > 78

Koi bhi number daaliye > 98

Koi bhi number daaliye > 43

Koi bhi number daaliye > 21

Koi bhi number daaliye > 76

Total Sum: 417

In the final line we print Total Sum: 417. 

This one prints 417 because 10+16+9+10+56+78+98+43+21+76 ka sum 417 hai.


```javascript
// please write code here
```

```solution
var sum = 0;
for (var i = 50; i >= 40; i--){
 const input = require('readline-sync');
 let number = input.questionInt('Enter the number');
 sum = sum +number
};
console.log(sum);

```