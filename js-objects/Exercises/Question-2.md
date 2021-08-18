

Write a programme to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

Sample input (n = 5) :

Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

```javascript
// please write code here
```

```solution
var prompt = require('readline-sync');
var n = prompt.questionInt('How many more times? ');
d = {}
for (let i = 0; i <= n; i++) {
   d[i] = i ** 2
}
console.log(d);
```