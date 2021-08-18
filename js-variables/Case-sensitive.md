```ngMeta
name: Case sensitive
```

### Example:
```javascript
var Name = "komal";
var name = "swati";
console.log(Name+name)
// output: komalswati

```
### Explanation:

As variables are case sensitive. It means x and X are different variables. You can see clearly in this above two variables one is Name we have with N (capital N) and second one is also name but started with n (small n), both are different  to look and JS feels also it as a different variable.


### Example:
```javascript
var num_12 = 24;
console.log(12num)

// Output : SyntaxError: Invalid or unexpected token

```
### Explanation:

As the above example throws an error because according to the rules of naming variables, We can not use numbers in the starting of variables Like 12num . If we do it then our computer will be confused and will throw an error because it doesn’t know to start a variable with a number.


