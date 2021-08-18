Write a program where it will console these 3 parameters for odd and even numbers.


- count
- sum
- average

var elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]

```javascript
// please write code here
```

```solution
var elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
var count_odd_numbers=0;
var sum_odd_numbers=0;
var sum_even_numbers=0;
var count_even_numbers=0;
for(var i of elements){
   if(i%2 ===0){
       sum_even_numbers+=i;
       count_even_numbers+=1;
   }
   else{
       sum_odd_numbers+=i;
       count_odd_numbers+=1;
   }
}
console.log((sum_even_numbers+sum_odd_numbers)/2);
console.log(count_odd_numbers);
console.log(count_even_numbers);
console.log(sum_odd_numbers);
console.log(sum_even_numbers);
```