```ngMeta
name: Common operations can be done on Arrays
```

## Common operations can be done on Arrays


- **Create an array**

**Example :**
```javascript
var fruits = ['Apple', 'Banana'];
console.log(fruits.length); 
// output 2
```

**Explanation :**

In this we have used the length property to find the length of the array. It depends generally on the elements present in the arrays.

- **Access an Array item using the index position**

**Example :**

```javascript
var fruits = ['Apple', 'Banana', ‘Orange’]
console.log(fruits[1]); // output ‘Banana’
```
**Explanation :**

In javascript arrays elements can be accessed by indexing which specify the position of the current element in the array. And it starts with 0.

- **Loop over an Array**
	
**Example :**

```javascript
var array = [ 1, 2, 3, 4, 5, 6 ];
for (var index = 0; index < array.length; index++) {
console.log(array[index]);
}
//output
// 1
// 2
// 3
// 4
// 5
```
    
**Explanation :**
    
The index starts with 0 as (index = 0) and it will run upto the length of the array 
(index < array.length) which is according to the elements present in the array, currently it is 6.

When this loop runs the first time, the value of index is 0, 0<6 is true, and it is incremented due to index++, index value will become 1, therefore array [index] is printed

When this loop runs the second time, the value of index is 0, 1<6 is true, and it is incremented due to index++, index value will become 2, therefore array [index] is printed

When this loop runs the third time, the value of index is 0, 2<6 is true, and it is incremented due to index++, index value will become 3, therefore array [index] is printed

When this loop runs the fourth time, the value of index is 0, 3<6 is true, and it is incremented due to index++, index value will become 4, therefore array [index] is printed

When this loop runs the fifth time, the value of index is 0, 4<6 is true, and it is incremented due to index++, index value will become 5, therefore array [index] is printed

When this loop runs the sixth time, the value of index is 0, 5<6 is true, and it is incremented due to index++, index value will become 5, therefore array [index] is printed

When this loop runs the seventh time, the value of the index is 6. Clearly, 6<6 false, so the for loop will stop there.

 
 
- **Add an item to the end of an Array**
	
**Example :**

```javascript
var fruits = ['Apple', 'Banana']
fruits.push('Orange')
console.log (fruits)
// output ["Apple", "Banana", "Orange"]
```
- **Remove an item from the end of an Array**
    
**Example :**

```javascript
var fruits = ['Apple', 'Banana', ‘Orange’]
fruits.pop()
console.log(fruits)
// output ["Apple", "Banana"]
```

- **Remove an item from the beginning of an Array**

**Example :**

```javascript
var fruits = ['Apple', 'Banana', ’orange’]
fruits.shift()
console.log(fruits)

// output [‘Banana’, ‘orange’ ]
```
- **Add an item to the beginning of an Array**


**Example :**
```javascript
var fruits = ['Apple', 'Banana']
fruits.unshift(‘Grapes’)
console.log(fruits);
// output : [ 'Grapes', 'Apple', 'Banana' ]
```
- **Find an index of an items the Array**
	
**Example :**
```javascript
let fruits = ['Apple', 'Banana', ‘Orange’]
let position = fruits.indexOf('Banana')
console.log(position);
//  output 1
```
- **Remove an item by its index position**
	
**Example :**
```javascript
var fruits = ['Apple', 'Banana', ‘Orange’]

let removedItem = fruits.splice(1,1)
// output [‘Apple’, ‘Orange’]
```

Note: while using splice(position, number of items to be removed) method you have to specify the position to start from and the number of items you want to remove from the array.
So here, we are saying begin from position 1, which is Banana, and remove one item from the array. Thus Banana will be removed.
 
- **Accessing Array Elements**

JavaScript arrays are zero-indexed. The first element of an array is at index 0. 

**Example :**
```javascript
var arr = ['shweta', 'nayak', 'komal', 'zeba']
console.log(arr[0])              // output 'shweta' the first element
console.log(arr[1])              // logs 'nayak' the second element
console.log(arr[arr.length - 1]) // logs 'Zeba' the last element. 
```

In this example, arr.length gives us the total number of elements in the array, which is 4. 4 - 1 is 3. So this statement prints out arr[3], which is Zeba.

**Example :**

let arr = ['shweta', 'nayak', 'komal', ‘Zeba’]
console.log(arr.0)   // syntax error

**Explanation :-**

The above example will throw a syntax error in javascript because here in javascript while accessing the elements from an array we generally use [ ] (brackets notation) instead of .(dot notation)
