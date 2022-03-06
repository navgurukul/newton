Write a function named showNumbers() which takes 1 argument named limit and program starts from o to limit and checks the numbers in between 0 to limit and prints whether the number is Even or odd like the below.

For example :

Input:-

3

Output :

0 EVEN

1 ODD

2 EVEN

3 ODD

```javascript
// write code here
```

```solution
function showNumbers(limit){
   for(i=0;i<=limit;i++){
       if(i%2 ===0){
           console.log(i," - Even");
       }
       else{
           console.log(i," - Odd");
       }
   }
}
showNumbers(3);
```