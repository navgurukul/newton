Write a function named check_numbers_list which takes two lists of integers and checks the numbers of the same index numbers whether they both are even or not. For checking both even or not you can use the function written in the previous question.
 
 
If you give these lists [2, 6, 18, 10, 3, 75] and [6, 19, 24, 12, 3, 87] then the output should come like this.
 
dono even hain

---------------

dono even nahi hai

---------------

dono even hain

---------------

dono even hain

---------------

dono even nahi hain

---------------

dono even nahi hain

---------------


```javascript
// please write code here
```


```solution:
function check_numbers(num1,num2){
   if(num1%2 ===0 && num2%2===0){
       console.log("Both are Even");
       console.log("-------------");
   }
   else{
       console.log("Both are not Even");
       console.log("-------------");
   }
}
 
function check_numbers_list(list1,list2){
   for(var i=0;i<6;i++){
       check_numbers(list1[i],list2[i]);
   }
}
 
check_numbers_list( [2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87]);
```