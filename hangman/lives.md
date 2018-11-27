Ab aapko ek feature implement karna hai, jisse ki user ke paas limited chances ho.
Maan lete hai ki user ke paas sirf 8 chances hai - aur aapko apne loop ko aise modify karna hai ki user ke paas 8 chances ho.

Inn 8 chances ke baad, user ka game over ho jaye.
Aur jab bhi user ka koi bhi galat guess ho toh - aap uska ek chance kam kar de.
Jab bhi user ka guess theek ho, toh aap uski number of lives ko kam na karein.

## Hint
- Iske liye aapko ek temporary variable ki jaroorat padegi - jis mei aap remaining lives store kareinge. Chale iss variable ko `remaining_lives` hi bol lete hai.
- Aap ko iss variable ko 8 se initialise karna hoga.
- Aap ko sahi se samajhna hoga ki kab kab yeh variable ko change karna hai.
- Aap ko sahi se samajhna hoga ki jab yeh variable zero ho jaye, toh aap
    - kaha par check karoge ki yeh variable ab zero ho gaya hai
    - jab yeh zero ho jayega toh aap kya karenge uss condition ko handle karne ke liye

## Possible Solution
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
    remaining_lives = 8
    
    while (remaining_lives > 0):
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
            print ""
            letters_guessed.append(letter)
            remaining_lives -= 1
            
    else:
        print "Sorry, you ran out of guesses. The word was " + str(secret_word) + "."

```

Aap yeh kaam alag tarah se bhi kar sakte hai, yeh sirf ek possible solution hai. Koshish karein ki hint mei pooche hue saare questions par aap ko clarity ho.