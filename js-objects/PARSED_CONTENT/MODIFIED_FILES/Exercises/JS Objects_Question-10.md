Question-10_key1

 
Question-10_key2


Question-10_key3


```javascript
// please write code here
```

```solution
var readline = require('readline-sync');
var students={}
for (let step = 0; step <10; step++){
   var name =readline.question("Enter your name:");
   var marks=readline.questionInt("Enter the marks");
   students[name]=marks;
}
console.log(students);
```