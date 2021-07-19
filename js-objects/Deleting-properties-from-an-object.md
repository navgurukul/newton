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

