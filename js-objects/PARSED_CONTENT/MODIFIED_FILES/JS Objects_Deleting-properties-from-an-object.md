```ngMeta
Deleting-properties-from-an-object_key1
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
Deleting-properties-from-an-object_key2
