Write a programme to find the 3 maximum values of an object and print them.

Input :-

var my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
 
Output :-

[58,56,100]
 

```javascript
// please write code here
```

```solution:
const d = { 'a': 50, 'b': 58, 'c': 56, 'd': 40, 'e': 100, 'f': 20 }
var l = []
var m_l = []
var k = []
for (i in d) {
  l.push(d[i])
  for (j of l) {
      if (d[i] > j) {
          m_l.push(d[i])
       }
      if (m_l.length === 3) {
          break
       }
  }
}
console.log(m_l)
```

**For the next course [clickHere](https://www.merakilearn.org/course/138/exercise/3529)**