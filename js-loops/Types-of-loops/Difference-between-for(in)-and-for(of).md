```ngMeta
name: for in vs for of
```

# Difference between for( in ) and for (of): 

let Navgurukul = ['Pune', 'Bangalore', 'Sarjapur'];
 
```javascript
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

**Explanation**:

**Note**: For in loop iterates on the keys or indexes that are there in the list but for of loop will run the values. And for in will work on objects too but for of can’t.

```javascript
const campus={"camp_name":"Bangalore_campus","establish":2016,"election":"three_months"}
for(let pro in campus){
 console.log(campus[pro])
}
 
for(let pro of campus){
 console.log(pro)
}
 
// Output:
// It will throw an error because for of can’t iterate through objects.

```

