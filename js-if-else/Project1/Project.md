```ngMeta
name: Rock Paper Scissors
```

# Project1

Have you ever played a game called Rock Paper Scissors? We are going to create that game now.

You can see a video on how to play Rock paper scissors.

@[youtube](AnRYS02tvRA)

Let’s play it online and see how it works :

[Play Online Game](https://www.crazygames.com/game/rock-paper-scissors)
 
 
### Feedback after submit:

```javascript
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


**For the next course [clickHere](https://www.merakilearn.org/course/137/exercise/3536)**
