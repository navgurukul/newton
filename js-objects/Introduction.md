```ngMeta
name: Objects
```

Think of a dictionary. It has people’s names and their phone numbers. If we have to store this type of data, i.e. people’s names and phone numbers, then we will use something called the Object data type.


The following example will show you the simplest way to create an object in JavaScript. you access the data in objects through what are called properties or keys.

```javascript

var emptyObject = {};
var myContacts= {"kumar": 9000000000, "shwetha": 9876543211, "komal": "0909990999"};
// For better reading
var campusCityState = {
   "Sarjapur": "Karnataka",
   "Pune": "Maharashtra",
   "Dharmashala": "Himachal Pradesh"
}

```

```javascript
var myDetails={"name":"kumar","surname":"nayak","age":24}
```
 
An object contains properties, defined as a key-value pair. In the example above, name, surname and age are keys, and Nayak, Kumar and 24 and their corresponding values.

The object is a complex data type that allows you to store collections of data.

You can omit the quotes around key names like shown in the example below.



```javascript

var myDetails= {
   name:"kumar",
   surname:"nayak",
   age:24
}

```

But, be aware that the following will throw an error.

```javascript

var myDetails= {
   first-name:"kumar",
   surname:"nayak",
   age:24
}

```

To make the above work, we will have to put quotes are required around first-name

```javascript

var myDetails= {
   “first-name”:"kumar",
   surname:"nayak",
   age:24
}

```

If the key value is one word, like name, or like firstName, that will work. But if it contains any dashes or spaces (like “first-name” or “first name”) then you have to put the inside quotes.


You can also use numbers as properties.

```javascript

var students ={
   1:"shwetha",
   2:"kumar",
   3:"komal"
}

```
