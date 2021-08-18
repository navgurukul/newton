```ngMeta
name: for in vs for of
```

### Example:
 
```javascript

let Navgurukul = ['Pune', 'Bangalore', 'Sarjapur'];

// cmpKey are the property keys
for (let cmpKey in Navgurukul) {
 console.log(cmpKey);
}
console.log(“------------------”)
// cmpValue are the property values
for (let cmpValue of Navgurukul) {
 console.log(cmpValue)
}

// Output:

// 0
// 1
// 2
// ------------------------
// Pune
// Bangalore
// Sarjapur

```

### Explanation:

for (let cmpKey in Navgurukul) here cmpKey is the variable because of for in loop in cmpKey we will get index numbers only as 0, 1, 2 respectively.

for (let cmpValue of Navgurukul) here cmpValue is the variable because of for of in cmpValue we will get elements as values directly as Pune, Bangalore, Sarjapur.

#### Note: 

For in loop iterates on the keys or indexes that are there in the list but for of loop will run on the values. And for in will work on objects too but for of can’t.

```javascript
const campus={"camp_name":"Bangalore_campus","establish":2016,"election":"three_months"}
for(let pro in campus){
 console.log(campus[pro])
}

console.log("--------------");
 
for(let pro of campus){
 console.log(pro)
}
 
// Output:
// Bangalore_campus
// 2016
// three_months
// --------------
// It will throw an error because for of can’t iterate through objects.

```

### Explanation

for(let pro in campus) in this code for in can iterate on objects and in the variable pro we will get keys directly as camp_name, establish, election and used those keys and got the values as Bangalore_campus, 2016, three_months respectively.

for(let pro of campus) it will give error because for of can't run loop on objects,
