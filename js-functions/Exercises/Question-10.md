You need to write a function named students where it will take marks of students in a list and tell how many students have more than 20 marks. For checking if the number is greater than 20 or not you will write one more function named isGreaterThen20 and compare and give the result.


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