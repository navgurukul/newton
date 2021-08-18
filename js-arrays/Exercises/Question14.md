How to find all pairs in an array of integers whose sum is equal to the given number?

Sample Input:

var number = 30

var n = [10, 11, 12, 13, 14, 17, 18, 19]

Sample Output:

[
  [ 11, 19 ],
  [ 12, 18 ],
  [ 13, 17 ],
  [ 17, 13 ],
  [ 18, 12 ],
  [ 19, 11 ]
]

```javascript
// please write code here
```

```solution
var n = [10, 11, 12, 13, 14, 17, 18, 19]
var number =30;
output=[]
for(var i of n){
   for(var j of n){
       if (i+j === number){
           output.push([i,j])
       }
  }
}
console.log(output);
```