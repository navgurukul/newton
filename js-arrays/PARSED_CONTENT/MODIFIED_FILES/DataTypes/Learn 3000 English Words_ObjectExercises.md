ObjectExercises_key1


1. ObjectExercises_key2
```solution
var myDetails={
firstName:"kumar",
lastName:"Nayak",
phoneNumber:"123456789",
isHealthy:false
}
console.log(myDetails);
```
 
2. ObjectExercises_key3
```javascript
var obj1 = { a: 5, b: 6 };
obj1["a"] =7;
console.log(obj1)     
```

```solution
{ a: 7, b: 6 }
```

3. ObjectExercises_key4
```javascript
var myObj = { name: "kumar", height: 5.4 };
myObj[name] =7;
console.log(myObj)
```
```solution
Output:ReferenceError: name is not defined

Because the name key we need to give it in strings, otherwise it feels that it is a variable.
```