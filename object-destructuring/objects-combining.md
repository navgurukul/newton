```ngMeta
name: Objects combining
```


var silverScreenDetails={name:"Chiranjeevi",realTag:"super star"}
var realLifeDetails={realName:"Konidela siva prasad",oldTag:"Mega star"}
 
var allActors={...silverScreenDetails,...realLifeDetails}
console.log(allActors);

// {
//   name: 'Chiranjeevi',
//   realTag: 'super star',
//   realName: 'Konidera siva prasad',
//   oldTag: 'Mega star'
// }
 
Here you will combine two objects of the same person which have silver screen details and his real life details, you will get all key and value pairs in a new variable i.e., allActors.

var silverScreenDetails={name:"Chiranjeevi",tag:"super star"}
var realLifeDetails={realName:"Konidela siva prasad",tag:"Mega star"}
 
var allActors={...silverScreenDetails,...realLifeDetails}
console.log(allActors);

If it has the same key , you have to recognize the object didn’t have duplicate keys so it won't have two properties at same time.
