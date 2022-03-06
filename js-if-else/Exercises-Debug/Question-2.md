code the change like if I give number as 21, 21 is divisible by both 3 and 7 so it should give Chacolate as answer to me.

sample inputs and outputs:

for 21 answer Chacolate

for 15 answer choco

for 14 answer late

for 13 answer Not divisible by 3 , 7

Debug the code and try to get exact solutions with different inputs


```javascript
var number = 12;
 
if(Number%3 === 0){
   console.log("choco")
}
elif(number % 7){
   console.log("late")
}
elif(a%3==0 and a%7==0) {
   console.log("Chocolate")
}
else {
   console.log("Not divisible by 3 , 7")
}

```