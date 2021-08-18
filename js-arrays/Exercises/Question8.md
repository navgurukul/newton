Write the program, to find the max element of the array,and console it.

Sample Input:

var numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]

sample Output:

70


```javascript
// please write code here
```

```solution
var numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7];
var max_num=0;
for(var i=0; i<numbers.length;i++){
   if (numbers[i]>max_num){
       max_num=numbers[i]
 
   }
}

```