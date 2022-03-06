```ngMeta
submission_type:url
```
## Hint
Aapko ab yeh change karna hai jisse jab bhi user input ke time par - agar `hint` likhein, toh aap usse koi bhi ek letter jo abhi tak user ne guess nahi kiya hai, woh letter guess kar kar, accordingly word display kar de.

## Hint implement karne ke liye Hint
- `hint` ko aapko valid input mei daalna hoga
- Ek aisa function likho jo bacche hue letters (jo abhi tak guess nahi hue hai) unko use kar kar, ek letter select karein aur usse user_input maan kar proceed kar sakte ho

## Solution

@[youtube](https://www.youtube.com/watch?v=M24bOAARprA)

## Possible Solution
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

..................... in the hangman function ............................
...
...
...
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
```
...
...
...

Aap yeh kaam alag tarah se bhi kar sakte hai, yeh sirf ek possible solution hai.
