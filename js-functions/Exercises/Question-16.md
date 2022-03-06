Write a function named perfect() which takes 1 parameter and checks that given parameter is a perfect number or not. Perfect number means we will count the factors of a given number including 1 but you need to exclude the own number as its factor.

If it is a perfect number prints num is a perfect number hai or else prints num is not a perfect number hain.

Example:

6 ek perfect number hai 6=1+2+3.

Output:

6 is a perfect number hain.


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