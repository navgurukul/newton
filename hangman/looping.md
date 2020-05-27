```ngMeta
submission_type: url
```
Agar aap game ko chala kar dekhoge, toh game sirf ek baar user se input leta hai. Aapko code loop mei daalna hai jisse ki user multiple baar letter daal daal kar try kar sake.

Aapko bahut jyada dhyaan rakhna hai, ki kaunsi instructions loop mei jayengi, kaunsi nahi? 

## Hint
Wohi instructions loop mei jayengi jo aapko lagta hai ki aapko repeat karni hai - e.g. 
- user se input aapko har baar lena hai, toh woh loop mei jana chahiye
- Jab hum print karte hai "welcome to the game", woh sirf ek baar karein toh theek hai, toh isliye woh loop mei nahi hona chahiye

## Solution Video

@[youtube](https://www.youtube.com/watch?v=SZGo7oa8vsc)

## Possible Solution:
Your `hangman` function can look like:

```python
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    letters_guessed = []
    
    while (True):
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters

        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break

        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            print ""
```

Aapka solution alag ho sakta hai, depending on ki aap loop mei kaise enter karte hai, aur kaise loop se exit karte hai.
