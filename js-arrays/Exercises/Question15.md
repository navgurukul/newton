Write a program to count how many odd numbers are there and how many even numbers are there in a given list.

var elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]

```javascript
// please write code here
```

```solution
var elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43];
 
var odd_numbers=0;
var even_numbers=0;
for(var i of elements){
   if(i%2 ===0){
       even_numbers+=1
   }
   else{
       odd_numbers+=1
   }
}
console.log(odd_numbers);
console.log(even_numbers);
```