Question-16_key1


Question-16_key2


Question-16_key3


Question-16_key4


Question-16_key5


Question-16_key6



```javascript
// write code here
```


```solution
function perfect(num){
   sum=0
   for(var i=1;i<num;i++){
       if(num%i === 0){
           sum+=i
       }
   }
   if(sum === num){
       console.log(num," is a perfect number");
   }
   else{
       console.log(num," is not a perfect number");
   }
}
perfect(6);
```