```ngMeta
name: Guessing game
```

## Project2

### Guessing game

The game is about guessing a number between 1 to 10, you can choose how many times you want to guess and guess those many times, if you are able to guess the secret number you won the game, or if your chances are completed means you completely lost the game. Are you ready to play the game?
 
 
Let’s play the game and understand with fun:[online game](https://www.funbrain.com/games/guess-the-number)

```javascript
let readlineSync = require("readline-sync");
let userChances = readlineSync.questionInt("how many times you want to guess: ");
let randomNumber= Math.floor(Math.random()*10);
chances = userChances;
 
for (let i = chances; i > 0; i--) {
   console.log("you have"+i+"chances to guess")
   userGuess = readlineSync.questionInt("guess number: ")
   if (userGuess == randomNumber) {
       console.log("congrats! ,your guess is right")
       break
   }
   else if(userGuess<randomNumber){
       console.log("go higher!");
   }
   else if(userGuess>randomNumber){
       console.log("go lower!");
   }
   else if(i == 1) {
       console.log("sadly!, your chances are completed")
   }
}
```

### For the next course [clickHere](https://www.merakilearn.org/course/126/exercise/3256)