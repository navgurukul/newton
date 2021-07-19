```ngMeta
name: Do While vs While
```

## Difference between while and do while loops

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

**Explanation:** 

In the above example, if you see from do while 2 is printed because in do while first it won’t check loop condition and it will run 1 time because of do and after checking the loop condition it will never run.

In the while loop it will check the loop condition first. It is false so it won’t execute a block of code written inside that, so that’s why it won’t print anything.
