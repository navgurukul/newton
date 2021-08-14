- Different-types-to-write-a-function_key1
Different-types-to-write-a-function_key2


```javascript

function addNumbers(parameter1, parameter2) {
 // code to be executed
}

```

Different-types-to-write-a-function_key3


Different-types-to-write-a-function_key4



- Different-types-to-write-a-function_key5
```javascript

// Function Declaration

function getSum(num1, num2) {
 var total = num1 + num2;
 return total;
}

```

Different-types-to-write-a-function_key6

 
```javascript

// Function Expression

var getSum = function(num1, num2) {
 var total = num1 + num2;
 return total;
};

```

Different-types-to-write-a-function_key7


Different-types-to-write-a-function_key8


Different-types-to-write-a-function_key9


Different-types-to-write-a-function_key10


```javascript

var getSum = function(num1, num2) {
 var total = num1 + num2;
 return total;
};
 
console.log(getSum(5, 10)); // 0utputs: 15
 
var sum = getSum(7, 25);
console.log(sum); // 0utputs: 32

```

Different-types-to-write-a-function_key11


Different-types-to-write-a-function_key12


Different-types-to-write-a-function_key13


Different-types-to-write-a-function_key14
```javascript
var isEqual = function(str1,str2){
   console.log(str1===str2)
}
isEqual("kumar","nayak");

```
- Different-types-to-write-a-function_key15
Different-types-to-write-a-function_key16


```javascript

(function myName () {
 var x = "Hello!! Nayak";  // I will invoke myself
 console.log(x);
})();
 
Output :-
Hello!! Nayak

```
 
Different-types-to-write-a-function_key17


Different-types-to-write-a-function_key18


Different-types-to-write-a-function_key19


Different-types-to-write-a-function_key20


Different-types-to-write-a-function_key21


Different-types-to-write-a-function_key22
```javascript
(function(str1,str2){
   console.log(str1===str2)
})("kumar","kumar");
```