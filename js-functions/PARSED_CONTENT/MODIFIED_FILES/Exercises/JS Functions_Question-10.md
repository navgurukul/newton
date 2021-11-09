Question-10_key1



```javascript
// please write code here
```

```solution
function isGreaterThan20(num){
   if(num>20){
       return true
   }
}

function students(list_of_marks){
   count=0
   for(var i of list_of_marks){
       var result= isGreaterThan20(i)
       if (result === true){
           count++
       }
   }
   console.log(count);
}
students([21,25,19,25,33,54])
```