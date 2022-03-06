Returning-Values-from-a-Function_key1
```javascript
// Defining function
function getSum(num1, num2) {
 var total = num1 + num2;
 return total;
}

```
Returning-Values-from-a-Function_key2
Returning-Values-from-a-Function_key3


Returning-Values-from-a-Function_key4
```javascript

// Defining function
function getSum(num1, num2) {
 var total = num1 + num2;
 return total;
}

// Displaying returned value
var result1 = getSum(6, 20);
console.log(result1) // 0utputs: 26
var result2 = getSum(-5, 17);
console.log(result2) // 0utputs: 12
```
 
Returning-Values-from-a-Function_key5


```javascript

// Defining function
function getSum(num1, num2) {
 var total = num1 + num2;
 return total;
 console.log("it won't prints this because return works like break");
}

// Displaying returned value
var result1 = getSum(6, 20);
console.log(result1) // 0utputs: 26
var result2 = getSum(-5, 17);
console.log(result2) // 0utputs: 12
```
 
Returning-Values-from-a-Function_key6



Returning-Values-from-a-Function_key7
1. Returning-Values-from-a-Function_key8
```javascript
// write code here
```

```solution
function averageOfSubjects(maths,science){
   return ((maths+science)/2);
}
console.log(averageOfSubjects(25,30));
 ```

2. Returning-Values-from-a-Function_key9
```javascript
function insertingElement(arr){
   var a=5;
   arr.push(a);
   return arr;
   console.log(arr);
 
}
console.log(insertingElement([1,2,3,4]));

```

```solution
[ 1, 2, 3, 4, 5 ]
```
Returning-Values-from-a-Function_key10
Returning-Values-from-a-Function_key11


3. Returning-Values-from-a-Function_key12
```javascript

function multiplyString(string,num){
   string*num;
}
 
console.log(multiplyString("kumar",2));
```

```solution
Undefined

We returned nothing that’s why when we consoled it also it was given undefined.
```