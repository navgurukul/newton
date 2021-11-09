Question-2_key1


Question-2_key2


Question-2_key3


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