Question14_key1


Question14_key2


Question14_key3


Question14_key4


Question14_key5


Question14_key6


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