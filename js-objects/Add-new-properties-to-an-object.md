```ngMeta
name: Adding new property
```

Here's how we would add a isGood property to myHome:

```javascript

var myHome = {
   "name": "Mannat",
   "location":"Mumbai",
   "Colour":"black",
   "owner":"sharukh khan",
   "neighbours": ["everything!"]
 };


myHome.isGood= true;

console.log(myHome);

// output

// {
//    name: ‘my Villa’,
//    location:"Mumbai",
//    Colour:"black",
//    Owner:”sharukh khan”,
//    neighbours: ["everything!"],
//    isGood:true
// }

```

If you see, the new property isGood is added in the object.

For adding:

objectName.NewPropertyName = value;

myHome.isGood= true;

Then in myHome object we are going to set a new property named isGood and we are giving value as true.


