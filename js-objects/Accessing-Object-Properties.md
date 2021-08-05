```ngMeta
name: Accessing Object Properties
```

In two ways we can access properties i.e., dot notation (.) and bracket notation ([ ]), similar to an array. 


Here is a sample of using dot notation (.) to read an object's property:

```javascript

var vegetables ={
   veg1:"potato",
   veg2:"brinjal",
   veg3:"bottle gourd"
}
 
var vegetable1= vegetables.veg1;
var vegetable2= vegetables.veg2;
var vegetable3= vegetables.veg3;


console.log(vegetable1);
console.log(vegetable2);
console.log(vegetable3);
 
//output:
// potato
// brinjal
// bottle gourd

```

### Explanation:

vegetables.veg1 would have the value of potato, vegetables.veg2 would have the value of brinjal, vegetables.veg3 would have the value of bottle gourd.

The second way to access the properties of an object is bracket notation ([ ]). If the property of the object you are trying to access has a space in its name, you will need to use bracket notation.


However, you can still use bracket notation on object properties without spaces.


Here is a sample of using bracket notation to read an object's property:

```javascript

var myDetails={
   "first name":"kumar",
   "last name": "vadthya",
   "middle name":"nayak"
}
 
console.log(myDetails["first name"])
console.log(myDetails["last name"])
console.log(myDetails["middle name"])
 
// output
// kumar
// vadthya
// nayak

```

### Explanation:

myDetails["first name"] would be the string “kumar”, myDetails["last name"] would be the string “vadthya”, myDetails["middle name"] would be the string “nayak”.
