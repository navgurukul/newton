# for of Loop

Loops over iterable objects such as array .
	
**Example**:
```javascript
arr=["a","b","g","r","t"]
for(let le of arr){
console.log(le);
}

// Output:

// a
// b
// g
// r
// t   

```
	
**Example**: 
```javascript
let name=["komal","shweta","rani","swati","mahi","shanti","sarmistha"]
for(let lname of name){
   console.log(lname);
}

Output: 
komal
shweta
rani
swati
mahi	
shanti
sarmistha

```

**Explanation**:

By for of loop, when we are looping on array, in lname we will get the each element one by one, like "komal","shweta","rani","swati","mahi","shanti","sarmistha" respectively.

When the loop is running for first time, lname value is “komal”, we asked to print lname only, it prints komal.

When the loop is running for second time, lname value is “shweta”, we asked to print lname only, it prints shweta.

When the loop is running for third time, lname value is “rani”, we asked to print lname only, it prints rani.

When the loop is running for fourth time, lname value is “swati”, we asked to print lname only, it prints swati.

When the loop is running for fifth time, lname value is “mahi”, we asked to print lname only, it prints mahi.

When the loop is running for sixth time, lname value is “shanti”, we asked to print lname only, it prints shanti.

When the loop is running for seventh time, lname value is “sarmistha”, we asked to print lname only, it prints sarmistha.




**Example**: 
```javascript
number_list=[23,"maan",67,"gouri",90,45,34]
for(let num of number_list){
console.log(num);
}
 

// Output: 

// 23
// maan
// 67
// gouri		
// 90
// 45
// 34

```
Explanation:
By for of loop, when we are looping on an array named as number_list, in num we will get each element one by one, like 23, “maan”, 67, “gouri”, 90, 45, 34 respectively.

When the loop is running for the first time, the num value is 23, we asked to print num only, it prints 23.

When the loop is running for a second time, the num value is “maan”. We asked to print num only, it prints maan.

When the loop is running for the third time, the num value is 67, we asked to print num only, it prints 67.

When the loop is running for the fourth time, the num value is “gouri”. We asked to print num only, it prints gouri.

When the loop is running for the fifth time, the num value is 90, we asked to print num only, it prints mahi.

When the loop is running for the sixth time, the num value is 45, we asked to print num only, it prints shanti.

When the loop is running for the seventh time, the num value is 34, we asked to print num only, it prints 34.



**Example:**

```javascript

let obj={"name":"sharmistha","age":21,"hobby":"watching movie",
   "goal":"fullstack_developer"}
for(let prop of obj){
   console.log(prop)
}
 

//  Output:

// TypeError: obj is not iterable.

```
	
**Explanation**: 

The for of loop doesn’t work with an object because it only works  with arrays.
you want to iterate over the properties(key,value pair) of the object you can use for in loop. 
