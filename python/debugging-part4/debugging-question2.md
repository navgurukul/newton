```ngMeta
name: Bagels
completionMethod: peer
```

In this exercise, you’ll learn a few new methods and functions that come with Python. You’ll also learn about augmented assignment operators and string interpolation. These things don’t let you do anything you couldn't do before, but they are nice shortcuts to make coding easier.

Bagels is a deduction game you can play with a friend. Your friend thinks up a random 3-digit number with no repeating digits, and you try to guess what the number is. After each guess, your friend gives you three types of clues:

1. **Bagels** – None of the three digits you guessed is in the secret number.
2. **Pico** – One of the digits is in the secret number, but your guess has the digit in the wrong place.
3. **Fermi** – Your guess has a correct digit in the correct place.

You can get multiple clues after each guess. If the secret number is 456 and your guess is 546 the clues would be “fermi pico pico”. The 6 provides “fermi” and the 5 and 4 provide “pico pico”.

Topics covered

* function returning the wrong value
* typeconversion problems

```python
import random
def getSecretNum(numDigits):
# Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
    secretNum += (numbers[i])
  print secretNum

def getClues(guess, secretNum):
# Returns a string with the pico, fermi, None clues to the user.
  if guess == secretNum:
    return 'You got it!'
  clue = []
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      clue.append('Fermi')
    elif guess[i] in secretNum:
      clue.append('Pico')
    if len(clue) == 0:
      return 'None'
  return ' '.join(clue)

def isOnlyDigits(num):
# Returns True if num is a string made up only of digits. Otherwise returns False.
  if num = '':
    return False

  for i in num:
    if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return False

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
  play = raw_input("Do you want to play again? Yes or No?") 
  return play.lower.startswith('y')

NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')

while True:
  secretNum = getSecretNum(NUMDIGITS)
  print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
  numGuesses = 1
  while numGuesses <= MAXGUESS:
    while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
      print 'Guess' + (numGuesses)
      guess = raw_input("Guess Again")

    clue = getClues(guess, secretNum)
    print(clue)
    numGuesses += 1
    if guess == secretNum:
      break
    if numGuesses < MAXGUESS:
      print 'You ran out of guesses. The answer was ' + secretNum
  if not playAgain:
    break
    
```