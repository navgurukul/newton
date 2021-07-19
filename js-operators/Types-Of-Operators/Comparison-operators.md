```ngMeta
name: Comparison Operators
```

## Comparison Operators

JavaScript language includes operators that compare two operands and return Boolean value (true or false).

Assume variable A holds 10 and variable B holds 20, then −


| Operators | Name | Description | Example | Result |
| ---------- | --------- | --------- | --------- | --------- | 
| == | Is equal to | Comparing equality of two operands without considering type | A==B | false |
| === | Is identical | Comparing equality of two operands with type also. | A===B | false |
| != | Not equal to | Comparing inequality of two operands. | A!=B | true |
| > | Greater Than | Check that the left side value is greater than right side value. If yes then returns true otherwise false. | A>B | false |
| < | Less Than | Checks that the left operand is less than the right operand. If yes then returns true otherwise false. | A < B | true |
| >= | Greater than or equal to | Checks that the left operand is greater than or equal to the right operand. If yes then returns true otherwise false. | A>=B | false |
| <= | Less than or equal to | Checks whether the left operand is less than or equal to the right operand. If yes then returns true otherwise false. | A<=B | true |


## Exercises:

```javascript
var a = 5, b = 10, c = "5";
var x = a;
console.log(a === c);
console.log(a == c);
console.log(a == x);
console.log(a != b);
console.log(a > b);
console.log(a < b);
console.log(a >= b);
console.log(a <= b);
console.log(a >= c);
console.log(a <= c);
```


```solution
false
true
true
true
false
true
false
true
true
true
```