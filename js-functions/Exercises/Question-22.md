Write a function squares_of_numbers which takes a number as a parameter, and runs a loop from 1 to the given number, and makes the number and square of a number as key, value pair. See the example below.


Input : 20

Output :

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}

```javascript
// write code here
```
 
 
```solution
function squares_of_numbers(limit){
   var output={}
   for(var i=1;i<=limit;i++){
       output[i]=i*i
   }
   console.log(output);
}
squares_of_numbers(20)
```


**For the next course [clickHere](https://www.merakilearn.org/course/147/exercise/3549)**