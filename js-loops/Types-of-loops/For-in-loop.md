```ngMeta
name: For in loop
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

By for in when you are looping on an array, in the car each time its key (index number) will come like 0, 1 ,2 respectively. 

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

In the above example, we used index number to get element from list. In this cureent example we prinnted the index number only be the varibale campus, and in the campus 0, 1, 2, 3 will come respectively.

#### For more understanding about for in loop go through this link:

- [click here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)

