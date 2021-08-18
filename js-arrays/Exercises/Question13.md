#### Report Card

See this list:

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]

Think that this is marks of some students from last 3 years, you need to calculate the marks of all subjects.

For the above given list the total sum is- 1142.


```javascript
// please write code here
```


```solution
var marks = [
   [78, 76, 94, 86, 88],
   [91, 71, 98, 65, 76],
   [95, 45, 78, 52, 49]
];
var sum=0;
for(var i of marks){
   for(var j of i){
       sum+=j
   }
}
console.log(sum);

```
