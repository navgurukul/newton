Remove the duplicates and put them in a separate list
 
var n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]

```javascript
// please write code here
```

```solution
var number_list = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
uniques=[]
duplicates=[]
for(var i of number_list){
  if(!uniques.includes(i)){
      uniques.push(i)
  }
}
 
for(var j of uniques){
  count=0
  for(var k of number_list){
      if (j === k){
          count+=1
      }
  }
 if(count >1){
   duplicates.push(j);
 };
}
 
console.log(duplicates);
```