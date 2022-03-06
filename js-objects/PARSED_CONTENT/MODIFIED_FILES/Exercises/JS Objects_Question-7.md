Question-7_key1


Question-7_key2


Question-7_key3


Question-7_key4

 

Question-7_key5


Question-7_key6

 


```javascript
// please write code here
```


```solution
var myDict= {
   1: 'NAVGURUKUL',
   2: 'IN',
   3:{  
        'A' : 'WELCOME',
        'B' : 'To',
        'C' : 'DHARAMSALA'
       }
   }
for (i in myDict){
   if ((typeof myDict[i]) === "object"){
       delete myDict[i]['A']
   }
}
console.log(myDict);
```