You have to make one program where it will take any array and it will check how  many elements are there in the array, at last will check the length of the array, it is like length property , we have the length property to find length, but we won’t use that here?

sample Input:

var numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]

sample Output:

9


```javascript
// please write code here
```


```solution
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7];
var count_element=0;
for(var i=0; i<numbers.length;i++){
   count_element++
}
console.log(count_element);
```