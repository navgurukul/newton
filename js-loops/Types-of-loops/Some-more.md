```ngMeta
name: Some more...
```

### Find length of object

To find the length of an object we can use builtin functions Object.keys() either we can use  Object.values().

### Example:

```javascript
const birds={name:"Bald Eagle",type:"Hawk",ScientificName:"HaliaeetusLeucocephalus"}
          
console.log(Object.keys(birds).length)

// Output: 
// 3

```

#### Explanation: 

Object.keys(objectName) will give you the list of property names.

So, Object.keys(birds) will give me the list i.e., 

[ 'name', 'type', 'ScientificName' ]
And when we use length on it , it gives 3. hooray!.....
	
#### Note:

Object.keys(objectName) will give you the list of property names.

Object.values(objectName) will give you the list of values.

### Example:

```javascript
const birds={name:"Bald Eagle",type:"Hawk",
   ScientificName:"HaliaeetusLeucocephalus"}
          
console.log(Object.values(birds).length)
      

// Output: 
//  3

```

#### Explanation:

Object.values(objectName) will give you the list of property values.

So, Object.keys(birds) will give me the list i.e., 

[ 'Bald Eagle', 'Hawk', 'HaliaeetusLeucocephalus' ]
And when we use length on it , it gives 3. hooray!.....	
