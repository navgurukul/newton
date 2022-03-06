Difference-between-for(in)-and-for(of)_key1
 
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

Difference-between-for(in)-and-for(of)_key2
Difference-between-for(in)-and-for(of)_key3


Difference-between-for(in)-and-for(of)_key4


Difference-between-for(in)-and-for(of)_key5
Difference-between-for(in)-and-for(of)_key6


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

Difference-between-for(in)-and-for(of)_key7
Difference-between-for(in)-and-for(of)_key8


Difference-between-for(in)-and-for(of)_key9
