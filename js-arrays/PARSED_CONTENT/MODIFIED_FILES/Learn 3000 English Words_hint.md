hint_key1
hint_key2


hint_key3
- hint_key4
- hint_key5
hint_key6
@[youtube](https://www.youtube.com/watch?v=M24bOAARprA)

hint_key7
```python
def get_hint(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek character jo abhi tak guess nahi hua hai
    '''

    import random
    letters_not_guessed = []
    
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)

        index += 1

    return random.choice(letters_not_guessed)
```

hint_key8
```python
        guess = raw_input("Please guess a letter: ")
        if guess == "hint":
            letter = get_hint(secret_word, letters_guessed)
        
        else:
            letter = guess.lower()

            if (not ifValid(letter))
                continue

        if letter in secret_word:
            letters_guessed.append(letter)
```hint_key9


hint_key10
