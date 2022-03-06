```ngMeta
submission_type:url
```

## Hangman Images
Aapko images.py se IMAGES import kar kar, woh images print karni hai. Jab bhi user koi galat input deta hai, toh aap corresponding image dikhayenge. 

## Hint
Toh agar user ne teesri baar galat answer diya, toh aap teesri wali image dikhayeing, `remaining_lives` ko graphically show karne ke liye.

## Solution

@[youtube](https://www.youtube.com/watch?v=T1WK-Rutm-Q)

## Possible Solution


..................... in the hangman function ............................
...
...
...
```python
    from images import IMAGES
    while (True):
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print (IMAGES[8-remaining_lives])
            print ("Remaining Lives : ", remaining_lives)
            print ("")
            letters_guessed.append(letter)
            remaining_lives -= 1
```
...
...
...
