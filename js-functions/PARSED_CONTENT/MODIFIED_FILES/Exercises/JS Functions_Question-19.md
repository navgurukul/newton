Question-19_key1


Question-19_key2


Question-19_key3


Question-19_key4


Question-19_key5


Question-19_key6


```javascript
// write code here
```


```solution
function multiplesOfNumbers(limit){
   var sum=0
   for(i=0;i<=limit;i++){
       if(i%3 ===0){
           sum+=i;
       }
       if(i%5 ==0){
           sum+=i;
       }
   }
   console.log(sum);
}
multiplesOfNumbers(10);
```