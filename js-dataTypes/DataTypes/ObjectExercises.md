```ngMeta
name: Exercises on Objects
```

### Exercises:

1. Write a program where a variable contains an object related to you with the properties of firstName, lastName, Phone Number, and isHealthy (true or false), and print it on console? 

```javascript
// please write code here
```

```solution
var myDetails={
firstName:"kumar",
lastName:"Nayak",
phoneNumber:"123456789",
isHealthy:false
}
console.log(myDetails);
```
 
2. What is the output of the following code?

```javascript
var obj1 = { a: 5, b: 6 };
obj1["a"] =7;
console.log(obj1)     
```

```solution
{ a: 7, b: 6 }
```

3. What is the error of the following code?

```javascript
var myObj = { name: "kumar", height: 5.4 };
myObj[name] =7;
console.log(myObj)
```
```solution
Output:ReferenceError: name is not defined

Because the name key we need to give it in strings, otherwise it feels that it is a variable.
```