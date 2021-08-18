```ngMeta
name: Deleting properties
```

```javascript

var myHome = {
   "name": "Mannat",
   "location":"Mumbai",
   "Colour":"black",
   "owner":"sharukh khan",
   "neighbours": ["everything!"],
   "isGood":true
 };
 
 delete myHome.isGood;
 console.log(myHome)


//output
// {
//   name: 'Mannat',
//   location: 'Mumbai',
//   Colour: 'black',
//   owner: 'sharukh khan',
//   neighbours: [ 'everything!' ]
// }

```

isGood property is deleted from an object myHome.

For deleting a particular property:

delete objectName.PropertyName;

delete myHome.isGood;

Then in myHome object we are going to delete a property named isGood and we are deleting isGood property.
