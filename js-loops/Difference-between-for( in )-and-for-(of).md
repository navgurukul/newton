let Navgurukul = ['Pune', 'Bangalore', 'Sarjapur'];
 
```js
// cmpKey are the property keys
for (let cmpKey in Navgurukul) {
 console.log(cmpKey);
}
console.log(“------------------”)
// cmpValue are the property values
for (let cmpValue of arr) {
 console.log(cmpValue)
}

Output:

0
1
2
------------------------
Pune
Bangalore
Sarjapur

```

**Explanation**:

**Note**: For in loop iterates on the keys or indexes that are there in the list but for of loop will run the values. And for in will work on objects too but for of can’t.

```js
const campus={"camp_name":"Bangalore_campus","establish":2016,"election":"three_months"}
for(let pro in campus){
 console.log(campus[pro])
}
 
for(let pro of campus){
 console.log(pro)
}
 
Output:
It will throw an error because for of can’t iterate through objects.

```

**Find length of object**

To find the length of an object we can use Object.keys() either we can use  Object.values().

**Example**:-
```js
const birds={name:"Bald Eagle",type:"Hawk",
   ScientificName:"HaliaeetusLeucocephalus"}
          
console.log(Object.keys(birds).length)

Output: 
3

```

**Note**: 

Object.keys(objectName) will give you the list of property names.
So, Object.keys(birds) will give me the list i.e., 
[ 'name', 'type', 'ScientificName' ]
And when we use length on it , it gives 3. hooray!.....
	
**Example**:-
```javascript
const birds={name:"Bald Eagle",type:"Hawk",
   ScientificName:"HaliaeetusLeucocephalus"}
          
console.log(Object.values(birds).length)
      

Output: 
 3

```

Object.values(objectName) will give you the list of property values.
So, Object.keys(birds) will give me the list i.e., 
[ 'Bald Eagle', 'Hawk', 'HaliaeetusLeucocephalus' ]
And when we use length on it , it gives 3. hooray!.....	
