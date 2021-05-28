```ngMeta
debugging-question2_key1
```
debugging-question2_key2

debugging-question2_key3

1. debugging-question2_key4
2. debugging-question2_key5
3. debugging-question2_key6
debugging-question2_key7

debugging-question2_key8

* debugging-question2_key9
* debugging-question2_key10
```python
import random
def getSecretNum(numDigits):
# Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
    secretNum += (numbers[i])
  print (secretNum)

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
  play = input("Do you want to play again? Yes or No?") 
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
      guess = input("Guess Again")

    clue = getClues(guess, secretNum)
    print(clue)
    numGuesses += 1
    if guess == secretNum:
      break
    if numGuesses < MAXGUESS:
      print ('You ran out of guesses. The answer was ' + secretNum)
  if not playAgain:
    break
    
```
