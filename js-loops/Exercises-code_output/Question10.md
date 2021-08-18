console this pattern using a loop. 1, -2, 3, -4, 5, -6 ..99, -100

#### Hint

Notice how the first number is positive, the second number negative, then the positive number and then the negative number. Pattern means positive (+) number, negative (-) number, positive (+) number, negative (-) number etc. And remember that we can make any number negative of any number by multiplying it by -1. 

Can you write this program using this hint?

```javascript
// please write code here
```


```solution
for (var i = 1;0 i <= 10; i++){
  if (i%2===0){
     console.log(-i);
  }else{
     console.log(i);
  }
};

```