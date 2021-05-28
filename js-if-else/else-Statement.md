> If any “ if ”  condition is false then an “else” statement comes into the picture.

**Example**:
```js
var a = 10;
var b = 12;
if(a > b){
console.log(a," is greater than ",b);
}
else {
console.log(b," is greater than " ,a);
}

Output :- 12 is greater than 10

```

**Explanation**: 

    In this example if a condition is false. So, else statement will execute


**Example**:
```js

var num1= 10;
var num2 = 20;
 
if(num1>num2){
   connsole.log("num1 is greater than num2");
}
else{
   console.log("num2 is greater than num1");;
}

output: "num2 is greater than num1"

```

**Explanation**:

    The condition that we given num1> num2  is false because num1 (10) is not greater than num2(20), So, if condition is false it will go to else condition and print the
    num2 is greater than num1.
