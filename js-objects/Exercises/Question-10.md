
Take 10 student inputs and marks and save them in an object.
 
Output :-

{
    'sonu':85,
    'Kartik':90,
    'Deepak':96,
    'Aman':76,
    'Somesh':60,
    'Umesh':85,
    'Amarpal':70,
    'Roshan':57,
    'Riyaz':98,
    'Shabid':56
}

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