```ngMeta
name: Storing a value into variable
```

### Example:
```javascript
var myLuckyNumber= 3; 
```
Here, we stored 3 as a value and it is stored in a variable named myLuckynumber.

```javascript
var myResult= 2+3;
console.log(myResult);
// output: 5
```


### Explanation:

A variable is simply the name of a storage location and variables work like a container to hold the value that we give after equal to (=). = (equal to ) is used to assign a value to a variable, if you do any operation such as addition, multiplication and it will compute first and assign the output to the variable.

### Note:

we use this console.log(); for printing the output in logs.

### Examples: 

1. Assign a boolean to a variable isHealthy?

```javascript
// please write code here
```

```solution
var isHealthy = true;

### Explanation:

In the above question we stored true a boolean value in a variable named as isHealthy, by this you can get to know we can store any data type as a value to a variable.
```

2. Multiply two numbers and store it in variable multiplyTwoNumbers?

```javascript
// please write code here
```

```solution
var multiplyTwoNumbers =3*3;
console.log(multiplyTwoNumbers);
// output: 9

### Explanation:

9 is the output because first it will compute 3*3 and assign it to a variable named multiplyTwoNumbers and print 9.
```

### Example:

```javascript
var myName;
myName = "kumar";
var myFullName;
myFullName = myName;
console.log(myFullName);
// output: kumar
```
### Explanation:

The above myName is declared with no value, then assigns a value “kumar” in it. And after that we declare a variable myFullName with no value. If you want to define “kumar” in myFullName you can do it by  directly assigning  myName to myFullname.

#### Note: You can assign a variable to another variable.

### Example:

```javascript
var myName;
myName = "kumar";
var myFullName;
myFullName="nayak Vadthya";
var FullName = myName+" "+myFullName;
console.log(FullName);
// output: kumar nayak Vadthya
```

### Explanation:

As you know from the previous example,you learnt how to store a variable into another variable. Now in this example We added two variables myName and myFullName which contain the values “kumar” and “nayak vadthya” respectively and store it in FullName. So when we printed FullName it showed the value as kumar nayak Vadthya.
