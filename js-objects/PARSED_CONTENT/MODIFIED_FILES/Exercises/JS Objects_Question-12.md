Question-12_key1


Question-12_key2


Question-12_key3

   
Question-12_key4

   
Question-12_key5

   
Question-12_key6

 

Question-12_key7


Question-12_key8


```javascript
// please write code here
```
```solution
var dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'],
   'David': ['subj1', 'subj2']
}
var count = 0
for(i in dict){
   for (a in dict[i]){
       count ++
   }
}
 
console.log(count);
 
```