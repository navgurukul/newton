```ngMeta
name: Conditionals, Loop and Variable Naming
completionMethod: peer
```

Yeh rock paper scissors game ka program hai. Iss game ko aap computer ke against kheloge. Iss game ke 3 rules hai 

* Rock Paper se haar jata hai
* Paper Scissors se haar jaata hai
* Aur, Scissors Rock se.

Appko pehle rock,paper ya scissors mei se chose karna hoga. Aur uske baad computer randomly inme se ek option chose karega. Firr, upar diye gaye rules ke hisab se result aayega. Jaise:


* Agar aapne "Rock" chose kiya aur computer ne "Scissors"
* To aap jeet jaoge kyunki "Rock" "Scissors" ko hara deta hai. ( Rule 3 )

Aap iss game ke rules iss [youtube video](https://www.youtube.com/watch?v=d1ZduiNyvcM) se seekh sakte hai.

Topics covered:

* semantic/syntactic problems in if/else
* semantic error in while conditions
* errors in variable naming

```python
from random import randint

def win():
    print 'You win!'

def lose():
    print 'You lose!'

while False:
    player_choice = raw_input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = option[random_move]

    if player_choice = computer_choice:
        print 'Draw!'
    elif  == 'rock' and coMp == 'scissors':
        win()
    elif  == 'paper' and comp == 'scissors':
        lose()
    elif playe == 'scissors' and comp == 'paper':
        win()
    elif player == 'scissors' and Comp == 'rock':
        lose()
    elif payer == 'paper' and computer == 'rock':
        win()
    elif player ==  and comp == :
        lose()
    aGain = raw_input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break
```