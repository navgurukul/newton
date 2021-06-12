First :

To download “readline-sync” in your laptop run this command line:-

-npm install readline-sync

To know more about “readline-sync” you can read this doc as well:-
	
https://launchschool.com/books/javascript/read/input_output


Note : Before using “readline-sync” make sure that it is downloaded in your laptop then only you will be able to run the following code mentioned below.

```javascript	
let chan = require("readline-sync");
let ch = chan.question("how many times you want to guess: ")
assume = 6;
for (let i = 1; i <= ch; i++) {
   req = require("readline-sync");
   guess = req.question("guess number: ")
   if (guess == assume) {
       console.log("congrats! ,your guess is right")
       break
   }
   else {
       console.log("sadly!, your guess is wrong")
   }
}

```