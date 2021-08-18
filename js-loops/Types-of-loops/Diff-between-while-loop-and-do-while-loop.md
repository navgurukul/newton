```ngMeta
name: Do While vs While
```

```javascript
let i=2
do{
   console.log(i);
}
while (i >10)
 
 
while(i>10){
   console.log(i);
}

// Output:
// 2
```
From do while : 2

From while : nothing will print

### Explanation: 

In the above example, if you see from do while it is printed 2  because in do while first it won’t check loop condition and it will run loop for 1 time and after a while it will check the loop condition i> 10 means 2>10 which is false.  So, it will never run.

In the while loop it will check the loop condition first. It is false so it won’t execute a block of code written inside that, so that’s why it won’t print anything.
