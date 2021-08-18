Write a program where it will do the following things with 1 to 20 numbers:

When number is divisible by 3 print “Nav”

When number is divisible by 7 print “Gurukul”

The numbers which is divisible by 3 and 7 print “NavGurukul”

If it is not coming in any case above print number only.

Output:
1

2

Nav

4

5

Nav

Gurukul

8

Nav

10

11

Nav

13

Gurukul

Nav

16

17

Nav

19

20


```javascript
// please write code here
```


```solution
for(var i=1; i<= 100; i++){
   if(i%3 ===0 && i%7 === 0){
       console.log("NavGurukul");
   }
   else if (i%3 === 0){
       console.log("Nav");
   }
   else if (i%7 === 0){
       console.log("Gurukul");
   }
   else{
       console.log(i);
   }
}
```