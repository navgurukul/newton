Project_key1
Project_key2


Project_key3


@[youtube](AnRYS02tvRA)

Project_key4


[Project_key5](https://www.crazygames.com/game/rock-paper-scissors)

 
```javascript
// please write code here
```


```solution
let readlineSync = require("readline-sync");
 
var computerMoves = ['rock', 'paper', 'scissors'];
var randomMoveOfComputer = computerMoves[Math.floor(Math.random() * computerMoves.length)];
 
var playerName= readlineSync.question("What is your name: ")
console.log("hi "+ playerName )
console.log("choose any move in rock paper scissors")
var playerMove = readlineSync.question("Which move you want to do? ");
 
if (playerMove == randomMoveOfComputer){
   console.log("Match Draw");
}
else if(playerMove =="rock" && randomMoveOfComputer == "paper"){
   console.log("computer won the match");
}
else if(playerMove=="rock" && randomMoveOfComputer == "scissors"){
   console.log(playerName+" Won the match");
}
else if(playerMove=="scissors" && randomMoveOfComputer == "rock"){
   console.log("computer won the match");
}
else if(playerMove=="scissors" && randomMoveOfComputer == "paper"){
   console.log(playerName+" Won the match");
}
else if(playerMove=="paper" && randomMoveOfComputer == "rock"){
   console.log(playerName+" Won the match");
}
else if(playerMove=="paper" && randomMoveOfComputer == "scissors"){
   console.log("computer won the match");
}
```


Project_key6