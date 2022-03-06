```ngMeta
name: Updating a property
```

### For example, 

let's look at myHome:

```javascript

var myHome = {
   "name": "Mannat",
   "location":"Mumbai",
   "Colour":"black",
   "owner":"sharukh khan",
   "neighbours": ["everything!"]
 };
 
 
myHome.name="my Villa";
 
console.log(myHome);
 
//  output

// {
//    name: ‘my Villa’,
//    location:"Mumbai",
//    Colour:"black",
//    Owner:”sharukh khan”,
//    neighbours: ["everything!"]
// }

```

let's change object's property name to the string my Villa. 

Here's how we update his object's name property: 

myHome.name = "my Villa"; 

or 

myHome["name"] = "my Villa"; 

Now when we evaluate myHome.name, instead of getting Mannat, we'll get his new name, myVilla.


After you've created a JavaScript object, you can update its properties at any time just like you would update any other variable. You can use either dot or bracket notation to update.




