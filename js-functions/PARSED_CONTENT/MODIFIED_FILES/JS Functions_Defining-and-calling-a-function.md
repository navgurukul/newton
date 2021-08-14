Defining-and-calling-a-function_key1


Defining-and-calling-a-function_key2


Defining-and-calling-a-function_key3



![Function-flow](https://lh4.googleusercontent.com/oiDuF_9DK5Hv3xvWVmE3Tsc5JhQonAjOfwmWa8IFvnOd3Lj6RdREPXQXj9CKlDlduPF80AyhTOOXgrmWb3qapH7M34CQHHfIJEXv41PI)


Defining-and-calling-a-function_key4


```javascript

// Defining function

function sayHello(name) {
 return "Hello " + name
}
 
console.log(sayHello("Pragna"))
 
// Output :
// Hello pragna

```

- Defining-and-calling-a-function_key5
Defining-and-calling-a-function_key6


```javascript

function sayHello(name) {
 return "Hello " + name
}
// Calling function
console.log(sayHello("Pragna"))

```

Defining-and-calling-a-function_key7

 
Defining-and-calling-a-function_key8


Defining-and-calling-a-function_key9


Defining-and-calling-a-function_key10


Defining-and-calling-a-function_key11


1. Defining-and-calling-a-function_key12
Defining-and-calling-a-function_key13


```javascript
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
 
// Feedback after submit
// kumar nayak
 ```
3. Defining-and-calling-a-function_key15
```javascript
function getFullName(firstName,lastName){
 console.log(firstName+" "+lastName)
}
 
GetFullName("kumar","nayak");
 
// Feedback after submit:ReferenceError: GetFullName is not defined
```
Defining-and-calling-a-function_key16
