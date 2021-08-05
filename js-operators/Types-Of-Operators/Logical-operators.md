```ngMeta
name: Logical Operators
```


Logical operators are used to combine two or more conditions.


| Operator | Description | Example |
| -------- | ---------- | ---------- |
| && | && is known as AND operator.  It checks that two conditions are true then it returns true otherwise returns false | (10==20 && 20==33) = false |
| OR | is known as OR operator.  It checks that two conditions and at least 1 condition is true it returns true otherwise returns false |  (10==20 \|\| 20==33) = false|
| ! | ! is known as NOT operator. It reverses the boolean result of the operand (or condition) | !(10==20) = true |

## Exercises:
 
```javascript
var a = 5, b = 10;
console.log((a != b) && (a < b));
console.log((a > b) || (a == b));
console.log((a < b) || (a == b));
console.log(!(a < b));
console.log(!(a > b));
```
 
```solution
true
false
true
false
true
```
