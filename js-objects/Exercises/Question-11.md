You need to count the number of occurrences of each unique character of a word "MISSISSIPPI" and store them in an object in key, value pairs.


Example:-

Output :-

{M:1,I:4,S:4,P:2}

```javascript
// please write code here
```
 
```solution
const list1=[]
const word="MISSISSIPPI"
let output={}
for (var i of word) {
      if(list1.includes(i)){
       output[i]=output[i]+1
    
  }else{
       list1.push(i);
       output[i]=1;
  }
}
console.log(output);
```