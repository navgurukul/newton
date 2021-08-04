```ngMeta
name: Loop over an object
```

for in loop is a special type of loop that iterates over the object or an array of elements.
 

### Example:

```javascript

var cars = ["Maruti", "Mercedes", "BMW"];
for (car in cars){
console.log(cars[car]),
}

// Output:
// Maruti
// Mercedes
// BMW

```

### Explanation:

By for in when you are looping on an array, in the car each time its key (index number) will come like 0,1 ,2 respectively. 

When the first time loop is running the car value is 0, we said to print cars[car] means cars[0] so it prints Maruti because in the zeroth position of cars we have Maruthi.

When the second time loop is running, the car value is 1, we said to print cars[car] means cars[1] so it print Mercedes because in the first position of cars we have Mercedes.

When the third time loop is running, the car value is 2, we said to print cars[car] means cars[2] so it prints BMW because in the first position of cars we have BMW.


### Example:

```javascript

const campus_list=["Bangalore","Dharamshala","Pune","Bangalore_another"]
for(let campus in campus_list){
   console.log(campus)
}

// Output: 
// 0
// 1
// 2
// 3

```

### Explanation:

By for in when you are looping  on Array, in  the campus each time its key (index number) will come like 0,1 ,2, 3 respectively. 

In the above example, we are using an operator with for loop. For within operators, use to give the index of an array.

### Example:

```javascript

var person={"name":"gouri","surname":"maity","age":37}
 
for (person_details in person){
console.log(person_details+ "= "+person[person_details]);
}

// Output: 
// name= gouri
// surname= maity
// age= 37

```

### Explanation:

By for in when you are looping on Dictionary (object), in  person_details each time its key will come like name, surname, age respectively. 

When the first time loop is running the person_details value is name, we said to print person[person_details] means person[“name”] so it prints gouri because in person dictionary name key has the value of gouri.

With the string concatenation 
person_details+ "= "+person[“name”], name= gouri

When the second time loop is running, the person_details value is surname. We said to print person[person_details] means person[“surname] so it prints maity because in person dictionary surname key has the value maity.

With the string concatenation 
person_details+ "= "+person[“surname”],surname=maity

When the third time loop is running, the person_details value is age, we said to print person[person_details] means person[“age”] so it prints 37 because in the person dictionary age has the value of 37.

With the string concatenation 
person_details+ "= "+person[“age”],age= 37



## Example:

```javascript

const campus={"camp_name":"Bangalore_campus","establish":2016,"election":"three_months"}
for(let eachKey in campus){
  console.log(campus[pro])
}
 
 
// Output: 

// Bangalore_campus
// 2016
// three_months

```

By for in when you are looping on Dictionary (object), in  eachKey each time its key will come like camp_name, establish, election respectively. 

When the first time loop is running the eachKey value is camp_name, we said to print campus[pro] means campus[“camp_name”] so it prints Bangalore_campus  because in the campus dictionary camp_name key has the value of Bangalore_campus.

When the second time loop is running, the eachKey value is establish. We said to print  campus[pro] means campus[“establish”] so it prints 2016 because in the campus dictionary establish key has the value 2016.

When the third time loop is running, the eachKey value is election, we said to print campus[pro] means campus[“election”] so it prints three_months because in the campus dictionary election has the value of theree_months.
