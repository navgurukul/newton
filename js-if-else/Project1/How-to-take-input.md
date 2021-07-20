```ngMeta
name: Project prereuisite
```

# Taking Input

In the world everyone has emotions and everyone will interact with each other. So in javascript also if we want to interact we can use different methods. One of them is readline-sync. 

To download “readline-sync” in your laptop run this command line:

> npm install readline-sync

To know more about “readline-sync” you can read this doc as well:
	
[Follow this link](https://launchschool.com/books/javascript/read/input_output)

Note : Before using “readline-sync” make sure that it is downloaded in your laptop then only you will be able to take the input from the user.

Example:

```javascript

let readlineSync = require("readline-sync");
var yourName= readlineSync.question("What is your name: ")
console.log(playerName);

```
**Explaination:**

readlineSync we imported by installation using npm install readline-sync. In readlineSync we have so many functions one function is question by this you will take input whatever that you entered here it will come as a string only.

If you want to use only Integer, then the question will give but its type is string not a number that we want.

For that , we have questionInt..

```javascript
let readlineSync = require("readline-sync");
var age= readlineSync.questionInt("What is your age: ")
console.log(age);
```