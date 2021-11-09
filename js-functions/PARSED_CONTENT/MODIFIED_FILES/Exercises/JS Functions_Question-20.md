Question-20_key1


- Question-20_key2
- Question-20_key3
Question-20_key4


- Question-20_key5
Question-20_key6


Question-20_key7


Question-20_key8


Question-20_key9


Question-20_key10


Question-20_key11



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