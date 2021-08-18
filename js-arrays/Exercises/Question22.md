
var mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."

subStr = "over"

You need to remove the all occurrences of subStr in mainStr and give the output

Output: the quick brown fox jumped the lazy dog. The dog slept on the verandah.


```javascript
// please write code here
```

```solution
var mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
var subStr = "over";
 
var c = mainStr.split(" ");
output="";
for(var i of c){
   output=output+i+" "
}
console.log(output);
```

**For the next course [clickHere](https://www.merakilearn.org/course/150/exercise/3635)**