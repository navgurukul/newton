lives_key1


lives_key2


lives_key3
- lives_key4
- lives_key5
- lives_key6
- lives_key7
lives_key8
@[youtube](https://www.youtube.com/watch?v=FPXBIGZGjoQ)

lives_key9
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
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = []
    remaining_lives = 8
    
    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)

        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break

        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print ("Remaining Lives : ", remaining_lives)
            print ("")
            letters_guessed.append(letter)
            remaining_lives -= 1
            
    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")

```

lives_key10
