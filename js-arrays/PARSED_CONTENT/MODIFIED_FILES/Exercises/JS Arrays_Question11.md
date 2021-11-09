Question11_key1



Question11_key2


Question11_key3


Question11_key4


Question11_key5


Question11_key6


Question11_key7


Question11_key8


Question11_key9


Question11_key10


```javascript
// please write code here
```


```solution
var Name=['m','a','l','a','y','a','l','a','m'];
var new_array=[];
for (var i=Name.length-1; i>=0;i--){
   new_array.push(Name[i]);
}
var count=0;
for (var j=0; j<Name.length; j++){
   if (new_array[j]===Name[j]){
       count++;
   }
}
if(count===Name.length){
   console.log("This is palindrome");
}else{
   console.log("This is not a palindrome");
}

```