Agar aap game ko chala kar dekhoge, toh game sirf ek baar chalta hai. Aapko code loop mei daalna hai jisse ki user multiple baar letter daal daal kar try kar sake.

Aapko bahut jyada dhyaan rakhna hai, ki kaunsi instructions loop mei jayengi, kaunsi nahi? 

## Hint
Wohi instructions loop mei jayengi jo aapko lagta hai ki aapko repeat karni hai - e.g. 
- user se input aapko har baar lena hai, toh woh loop mei jana chahiye
- Jab hum print karte hai "welcome to the game", woh sirf ek baar karein toh theek hai, toh isliye woh loop mei nahi hona chahiye

### One of the solutions:
Your `hangman` function can look like:

```python
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secretWord mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print ""

    lettersGuessed = []

    while (True)
        availableLetters = getAvailableLetters(lettersGuessed)
        print "Available letters: " + availableLetters

        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()

        if letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            print ""

            if isWordGuessed(secretWord, lettersGuessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break

        else:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            lettersGuessed.append(letter)
            print ""

```

Aapka solution alag ho sakta hai, depending on ki aap loop mei kaise enter karte hai, aur kaise loop se exit karte hai.