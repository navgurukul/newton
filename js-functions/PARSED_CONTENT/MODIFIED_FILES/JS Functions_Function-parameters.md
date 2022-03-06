Function-parameters_key1


Function-parameters_key2


```javascript

function functionName(parameter1, parameter2, parameter3) {
 // Code to be executed
}

functionName(argument1, argument2, argument3);

```

 
Function-parameters_key3


Function-parameters_key4
```javascript
// Defining function
function displaySum(num1, num2) {
 var total = num1 + num2;
 console.log(total);
}
 
// Calling function

displaySum(6, 20); // 0utputs: 26
displaySum(-5, 17); // 0utputs: 12
```

Function-parameters_key5
```javascript

// Defining function

function showFullname(firstName, lastName) {
 console.log(firstName + " " + lastName);
}
 
// Calling function
showFullname("Kumar", "Nayak"); // 0utputs: Kumar Nayak
showFullname("Shwetha"); // 0utputs: Shwetha undefined

```

Function-parameters_key6
Function-parameters_key7



Function-parameters_key8
Function-parameters_key9



Function-parameters_key10
1. Function-parameters_key11
```javascript
// write code here
```

```solution
function displayMultiply(num1, num2, num3) {
   return num1*num2*num3
  }
  
console.log(displayMultiply(2, 3, 4));
```

2. Function-parameters_key12
```javascript
function getResult(num1,num2,num3,num4){
 console.log(num1-num2+num3-num4)
}
 
getResult(2,3,4,5);
```

```solution
-2
```

3. Function-parameters_key13
```javascript
function getResult(num1,num2,num3){
 console.log(num1-num2+num3)
}
 
getResult(2,3,4,5);
```

```solution
No error. Even though an extra parameter (5) is passed, the function getResult simply does not use it.	
```


4. Function-parameters_key14
```javascript
// write code here
```

```solution
function SumOfNumbers(num1,num2){
   return num1+num2;
}
SumOfNumbers(1,2);
```


5. Function-parameters_key15
```javascript
function displayMultiply(a,b){
   console.log(a*b);
}
displayMultiply(2,3);
```

```solution
6
```

6. Function-parameters_key16
```javascript
	function displaySubtraction(a,b){
   console.log(ab);
}
displySubraction(2,3);
```

```solution
ReferenceError: display Subtraction is not defined

The function name is not matched with the calling name so it is given Reference Error.
```