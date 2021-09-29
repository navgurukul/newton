a-short-program-guess-the-number_key1
a-short-program-guess-the-number_key2



a-short-program-guess-the-number_key3



a-short-program-guess-the-number_key4
```python
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
Let’s look at this code line by line, starting at the top.


# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
```
a-short-program-guess-the-number_key5



a-short-program-guess-the-number_key6


a-short-program-guess-the-number_key7
a-short-program-guess-the-number_key8


```python
if guess < secretNumber:
    print('Your guess is too low.')
elif guess > secretNumber:
    print('Your guess is too high.')
```
a-short-program-guess-the-number_key9


```python
else:
    break    # This condition is the correct guess!
If the guess is neither higher nor lower than the secret number, then it must be equal to the secret number, in which case you want the program execution to break out of the for loop.


if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
```
a-short-program-guess-the-number_key10


a-short-program-guess-the-number_key11
a-short-program-guess-the-number_key12


a-short-program-guess-the-number_key13


a-short-program-guess-the-number_key14
