Write a function named license_checker that checks drivers speed, this function needs to take a parameter named speed.

- If speed is less than 70 then prints “ok”.
- If speed is more than 70 then function gives 1 point for each 5 km (this won’t count 70).

Example: for speed 80 the points should be “points:2” .

- If the driver got more than 12 points, the function has to give  “License suspended” .

Input:-

85

135

Output :-

3

“License suspended”


```javascript
// write code here
```

```solution
function license_checker(speed){
   if(speed < 70){
       console.log("ok");
   }
   if(speed > 70){
       points=0
       for(var i=70;i<speed;i+=5){
           points+=1
       }
       if(points>12){
           console.log("License suspended");
       }
       else{
           console.log(points);
       }
   }
}
 
license_checker(135);
```