Defining-and-calling-a-function_key1


Defining-and-calling-a-function_key2


Defining-and-calling-a-function_key3


Defining-and-calling-a-function_key4



![Function-flow](images/function_flow.png)


Defining-and-calling-a-function_key5
```javascript
// Defining function

function sayHello(name) {
 return "Hello " + name
}
 
console.log(sayHello("Pragna"))
 
// Output :
// Hello pragna
```

- Defining-and-calling-a-function_key6
Defining-and-calling-a-function_key7


```javascript

function sayHello(name) {
 return "Hello " + name
}
// Calling function
console.log(sayHello("Pragna"))

```

Defining-and-calling-a-function_key8

 
Defining-and-calling-a-function_key9
Defining-and-calling-a-function_key10


Defining-and-calling-a-function_key11


Defining-and-calling-a-function_key12
1. Defining-and-calling-a-function_key13
```javascript
//please write code here
```

```solution
function sayBye(userName){
   return "Bye"+" "+userName
}
 
console.log(sayBye("Kumar"))
```

2. Defining-and-calling-a-function_key14
```javascript
 function getFullName(firstName,lastName){
 console.log(firstName+" "+lastName)
}
 
getFullName("kumar","nayak");
 ```

```solution
kumar nayak
```

3. Defining-and-calling-a-function_key15
```javascript
function getFullName(firstName,lastName){
 console.log(firstName+" "+lastName)
}
 
GetFullName("kumar","nayak");
 
```
```solution
ReferenceError: GetFullName is not defined


Because Javascript is case sensitive and here x and X both are different and you defined function name as getFullName and you are calling it with 
GetFullName and they both are different.. I hope you got it now.
```